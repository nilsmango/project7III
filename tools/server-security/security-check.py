#!/usr/bin/python3
"""Read-only health checks. --send delivers one checked Telegram daily report."""
import argparse
import datetime as dt
import fcntl
import gzip
import json
import pathlib
import re
import socket
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

STAMP = re.compile(r"^(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\]")
ACTIONABLE = re.compile(r"FastCGI sent in stderr|internal redirection cycle|upstream|Permission denied|too many open files|worker process.*exited", re.I)

def nginx_counts(directory, now):
    """Include each vhost and rotated logs; ignore ordinary denied probes/404s."""
    result = {"errors_24h": 0, "actionable_1h": 0, "actionable_15m": 0, "sites": {}}
    for path in sorted(pathlib.Path(directory).glob("*error.log*")):
        if not re.search(r"error\.log(?:\.\d+(?:\.gz)?)?$", path.name):
            continue
        site = path.name.split(".error.log")[0] if ".error.log" in path.name else "shared/static sites"
        opener = gzip.open if path.suffix == ".gz" else open
        with opener(path, "rt", errors="replace") as handle:
            for line in handle:
                match = STAMP.match(line)
                if not match or match[2] not in {"error", "crit", "alert", "emerg"}:
                    continue
                stamp = dt.datetime.strptime(match[1], "%Y/%m/%d %H:%M:%S")
                age = now - stamp
                if not dt.timedelta(0) <= age <= dt.timedelta(hours=24):
                    continue
                result["errors_24h"] += 1
                result["sites"][site] = result["sites"].get(site, 0) + 1
                if age <= dt.timedelta(hours=1) and (match[2] != "error" or ACTIONABLE.search(line)):
                    result["actionable_1h"] += 1
                    if age <= dt.timedelta(minutes=15):
                        result["actionable_15m"] += 1
    return result

def run(*args):
    return subprocess.run(args, check=True, text=True, capture_output=True, timeout=60).stdout

def incident_issues(incident):
    issues = []
    if incident.get("status") == "contained_not_remediated":
        issues.append("Confirmed WordPress backdoors contained; trusted rebuild and credential rotation still required")
    elif incident.get("status") == "rebuilt_followups_pending":
        if incident.get("external_provider_rotation_pending"):
            issues.append("Ministry rebuilt; potentially exposed external provider credentials still need rotation")
        if not incident.get("host_forensic_clearance_complete"):
            issues.append("Host integrity review remains open after the WordPress incident")
    if incident.get("foildata_api_key_rotation_pending_client_coordination"):
        issues.append("Foildata API key was publicly readable; access is blocked but client-coordinated rotation is still required")
    if incident.get("store_office_2fa_pending"):
        issues.append("Store office (Sol) shop-manager account needs two-factor enrollment")
    return issues

def origin_status(host):
    return int(run("curl", "--silent", "--show-error", "--max-time", "10",
                   "--resolve", host + ":443:127.0.0.1", "--output", "/dev/null",
                   "--write-out", "%{http_code}", "https://" + host + "/"))

def collect():
    now = dt.datetime.now()
    errors = []
    def checked(name, fn, default):
        try:
            return fn()
        except (OSError, ValueError, subprocess.SubprocessError):
            errors.append(name + " could not be checked")
            return default
    nginx = checked("Nginx logs", lambda: nginx_counts("/var/log/nginx", now), None)
    ssh = checked("SSH journal", lambda: run("journalctl", "_COMM=sshd", "--since", "24 hours ago", "--no-pager", "-o", "cat"), "")
    failed_ssh = len(re.findall(r"Failed (?:password|publickey)|authentication failure", ssh))
    invalid_users = len(re.findall(r"Invalid user", ssh))
    failed = checked("Failed services", lambda: run("systemctl", "list-units", "--state=failed", "--no-legend", "--plain", "--no-pager"), "")
    failed_units = [line.split()[0] for line in failed.splitlines() if line.strip()]
    active = {}
    for service in ("nginx", "ssh", "fail2ban", "php8.3-fpm", "mariadb", "redis-server"):
        active[service] = checked(service, lambda s=service: run("systemctl", "show", s, "--property=ActiveState", "--value").strip(), "unknown")
    disk = checked("Disk usage", lambda: int(run("df", "--output=pcent", "/").splitlines()[-1].strip().rstrip("%")), None)
    packages = checked("Pending updates", lambda: run("apt", "list", "--upgradable"), "")
    pending = [line for line in packages.splitlines() if "[upgradable from:" in line]
    security_pending = sum("security" in line for line in pending)
    certs = {}
    for cert in pathlib.Path("/etc/letsencrypt/live").glob("*/fullchain.pem"):
        expiry = checked("Certificate " + cert.parent.name, lambda c=cert: run("openssl", "x509", "-in", str(c), "-noout", "-enddate").strip(), "")
        if expiry:
            when = dt.datetime.strptime(expiry.removeprefix("notAfter="), "%b %d %H:%M:%S %Y %Z")
            certs[cert.parent.name] = (when - dt.datetime.now(dt.timezone.utc).replace(tzinfo=None)).days
    if not certs:
        errors.append("No TLS certificates could be checked")
    baseline_path = pathlib.Path("/var/lib/aide/aide.db")
    baseline = baseline_path.is_file()
    aide_status = "not yet checked against this baseline"
    aide_log = pathlib.Path("/var/log/aide/aide.log")
    if baseline and aide_log.exists() and aide_log.stat().st_mtime >= baseline_path.stat().st_mtime:
        aide_text = checked("AIDE report", aide_log.read_text, "")
        code = re.search(r"AIDE returned with exit code (\d+)", aide_text)
        if "AIDE returned with a zero exit code" in aide_text:
            aide_status = "no changes detected"
        elif code:
            aide_status = "filesystem changes detected; review /var/log/aide/aide.log" if int(code[1]) <= 7 else "integrity check error"
        else:
            aide_status = "latest check incomplete; review /var/log/aide/aide.log"
    issues = []
    incident = {}
    incident_path = pathlib.Path("/etc/security-check/incident.json")
    if incident_path.exists():
        incident = checked("Security incident status", lambda: json.loads(incident_path.read_text()), {})
        issues += incident_issues(incident)
    origins = {}
    for host in ("project7iii.com", "nilsmango.ch", "moleculestore.com", "ministryofchemistry.com", "reitcoaching.ch"):
        status = checked("Origin HTTPS " + host, lambda name=host: origin_status(name), None)
        origins[host] = status
        expected = 503 if host == "ministryofchemistry.com" and incident.get("site_offline") else 200
        if status is not None and status != expected:
            issues.append("Origin " + host + " returned HTTP " + str(status) + "; expected " + str(expected))
    issues += [name + " is " + state for name, state in active.items() if state != "active"]
    issues += ["Failed services: " + ", ".join(failed_units)] if failed_units else []
    if nginx and nginx["actionable_1h"] > 20:
        issues.append(str(nginx["actionable_1h"]) + " actionable Nginx errors in the last hour")
    if failed_ssh > 50:
        issues.append(str(failed_ssh) + " failed SSH authentications in 24h")
    if disk is not None and disk > 85:
        issues.append("Disk usage is " + str(disk) + "%")
    if not baseline:
        issues.append("AIDE integrity baseline is missing")
    elif aide_status not in {"no changes detected", "not yet checked against this baseline"}:
        issues.append("AIDE: " + aide_status)
    issues += ["Certificate " + name + " expires in " + str(days) + " days" for name, days in certs.items() if days < 21]
    reboot = pathlib.Path("/var/run/reboot-required").exists()
    issues = errors + issues
    return {"time": now.isoformat(timespec="seconds"), "host": socket.gethostname(), "issues": issues, "nginx": nginx,
            "failed_ssh_24h": failed_ssh, "invalid_user_attempts_24h": invalid_users, "disk_percent": disk,
            "failed_services": failed_units, "services": active, "origin_https_status": origins, "pending_updates": len(pending),
            "pending_candidate_security_updates": security_pending, "reboot_required": reboot,
            "aide_baseline_present": baseline, "aide_status": aide_status, "certificate_days_remaining": certs}

def report_text(result):
    nginx = result["nginx"]
    lines = [("⚠️" if result["issues"] else "✅") + " [" + result["host"] + "] Daily server report",
             "Check: " + result["time"], "Status: " + ("; ".join(result["issues"]) or "No actionable issues detected"),
             "Failed SSH authentications (24h): " + str(result["failed_ssh_24h"]),
             "Invalid-user attempts (24h; not successful logins): " + str(result["invalid_user_attempts_24h"]),
             "Nginx logged errors (24h, all sites): " + (str(nginx["errors_24h"]) if nginx else "unknown"),
             "Actionable Nginx errors (1h): " + (str(nginx["actionable_1h"]) if nginx else "unknown"),
             "Disk usage: " + str(result["disk_percent"]) + "%",
             "Pending OS updates: " + str(result["pending_updates"]),
             "Reboot required: " + ("yes; automatic at 02:30 if no user is logged in" if result["reboot_required"] else "no"),
             "AIDE baseline: " + ("present" if result["aide_baseline_present"] else "missing"),
             "AIDE latest check: " + result["aide_status"],
             "Full report: /var/log/security-check.log"]
    return "\n".join(lines)[:3900]

def send_telegram(message):
    credentials = json.loads(pathlib.Path("/etc/security-check/telegram.json").read_text())
    payload = urllib.parse.urlencode({"chat_id": credentials["chat_id"], "text": message}).encode()
    request = urllib.request.Request("https://api.telegram.org/bot" + credentials["token"] + "/sendMessage", data=payload)
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            result = json.load(response)
        if result.get("ok") is not True:
            raise RuntimeError("Telegram rejected the report")
    except urllib.error.HTTPError as error:
        # Do not include the request URL: it contains the bot token.
        raise RuntimeError("Telegram returned HTTP " + str(error.code)) from None
    except urllib.error.URLError:
        raise RuntimeError("Telegram connection failed") from None

def alert_conditions(result):
    # Historical daily totals aren't a reason to interrupt the user now.
    issues = [issue for issue in result["issues"] if "actionable Nginx errors in the last hour" not in issue]
    nginx = result["nginx"]
    if nginx and nginx["actionable_15m"]:
        issues.append(str(nginx["actionable_15m"]) + " actionable Nginx errors in 15m; review site error logs")
    return {re.sub(r"\b\d+\b", "#", issue): issue for issue in issues}

def deliver_changes(current, previous, sender):
    added = set(current) - set(previous)
    removed = set(previous) - set(current)
    if not added and not removed:
        return False
    lines = ["⚠️ Server conditions changed"]
    lines += ["New: " + current[key] for key in sorted(added)]
    lines += ["No longer detected: " + previous[key] for key in sorted(removed)]
    sender("\n".join(lines)[:3900])
    return True

def send_changed_alerts(result):
    state_dir = pathlib.Path("/var/lib/security-check")
    with (state_dir / "alerts.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        state_path = state_dir / "alerts.json"
        previous = json.loads(state_path.read_text()) if state_path.exists() else {}
        current = alert_conditions(result)
        sent = deliver_changes(current, previous, lambda message: send_telegram("[" + result["host"] + "] " + message))
        # Store state only after successful delivery so failures get retried.
        temporary = state_dir / "alerts.json.new"
        temporary.write_text(json.dumps(current) + "\n")
        temporary.chmod(0o600)
        temporary.replace(state_path)
        return sent

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--send", action="store_true", help="send one daily Telegram report")
    parser.add_argument("--reboot-notice", action="store_true", help="notify after the upgrade job, only if a reboot is required")
    parser.add_argument("--alerts", action="store_true", help="send only new/resolved actionable conditions")
    args = parser.parse_args()
    if args.reboot_notice:
        if pathlib.Path("/var/run/reboot-required").exists():
            try:
                send_telegram("ℹ️ [" + socket.gethostname() + "] Updates require a reboot. Automatic reboot scheduled for 02:30 server time, if no user is logged in.")
            except (OSError, ValueError, RuntimeError):
                print("Telegram reboot notice failed; token not logged.", file=sys.stderr)
                return 1
            print("Telegram reboot notice confirmed")
        return 0
    result = collect()
    if args.alerts:
        try:
            sent = send_changed_alerts(result)
        except (OSError, ValueError, RuntimeError):
            print("Telegram alert delivery/state update failed; token not logged.", file=sys.stderr)
            return 1
        if sent:
            with pathlib.Path("/var/log/security-check.log").open("a") as handle:
                handle.write(json.dumps(result, sort_keys=True) + "\n")
        print("Telegram condition change confirmed" if sent else "No condition change; no Telegram sent")
        return 0
    print(json.dumps(result, indent=2))
    if args.send:
        log = pathlib.Path("/var/log/security-check.log")
        with log.open("a") as handle:
            handle.write(json.dumps(result, sort_keys=True) + "\n")
        try:
            send_telegram(report_text(result))
        except (OSError, ValueError, RuntimeError):
            # A failed notification is a failed systemd job, not silent success.
            print("Telegram delivery failed; check credentials/network. Token not logged.", file=sys.stderr)
            return 1
        print("Telegram delivery confirmed")
    return 0

if __name__ == "__main__":
    sys.exit(main())
