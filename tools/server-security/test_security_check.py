import datetime as dt
import gzip
import importlib.util
import pathlib
import tempfile
import unittest
from unittest.mock import Mock

spec = importlib.util.spec_from_file_location("monitor", pathlib.Path(__file__).with_name("security-check.py"))
monitor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(monitor)

class NginxTests(unittest.TestCase):
    def test_time_window_rotations_and_probe_classification(self):
        now = dt.datetime(2026, 9, 16, 11)
        with tempfile.TemporaryDirectory() as folder:
            root = pathlib.Path(folder)
            (root / "error.log").write_text(
                '2026/09/16 06:50:08 [error] 1: rewrite or internal redirection cycle\n'
                '2026/09/16 10:30:00 [error] 1: access forbidden by rule\n'
                '2026/09/16 10:40:00 [notice] 1: using inherited sockets\n'
                '2026/09/17 10:40:00 [error] 1: upstream unavailable\n')
            (root / "ministryofchemistry.com.error.log").write_text(
                '2026/09/16 10:30:00 [error] 1: FastCGI sent in stderr: PHP Warning\n')
            (root / "error.log.1").write_text(
                '2026/09/15 12:00:00 [error] 1: upstream unavailable\n'
                '2026/09/15 10:59:59 [error] 1: upstream unavailable\n')
            with gzip.open(root / "error.log.2.gz", "wt") as handle:
                handle.write('2026/09/14 12:00:00 [error] 1: upstream unavailable\n')
            (root / "error.log.notes").write_text('2026/09/16 10:30:00 [error] 1: upstream unavailable\n')
            result = monitor.nginx_counts(root, now)
            self.assertEqual(result["errors_24h"], 4)
            self.assertEqual(result["actionable_1h"], 1)
            self.assertEqual(result["actionable_15m"], 0)
            self.assertEqual(result["sites"]["ministryofchemistry.com"], 1)

    def test_old_errors_are_not_current(self):
        with tempfile.TemporaryDirectory() as folder:
            pathlib.Path(folder, "error.log").write_text('2026/09/14 12:00:00 [error] 1: internal redirection cycle\n' * 100)
            self.assertEqual(monitor.nginx_counts(folder, dt.datetime(2026, 9, 16, 11))["errors_24h"], 0)

class AlertTests(unittest.TestCase):
    def test_foildata_and_shop_auth_followups_independent_of_ministry_status(self):
        issues = monitor.incident_issues({"foildata_api_key_rotation_pending_client_coordination": True, "store_office_2fa_pending": True})
        self.assertEqual(len(issues), 2)
        self.assertTrue(any("client-coordinated rotation" in issue for issue in issues))
        self.assertTrue(any("two-factor enrollment" in issue for issue in issues))
        self.assertEqual(monitor.incident_issues({"foildata_api_key_rotation_pending_client_coordination": False, "store_office_2fa_pending": False}), [])

    def test_confirmed_office_owner_does_not_clear_two_factor_followup(self):
        incident = {"store_office_owner": "Sol", "store_office_owner_confirmed": True, "store_office_2fa_pending": True}
        issues = monitor.incident_issues(incident)
        self.assertEqual(len(issues), 1)
        self.assertIn("office (Sol)", issues[0])
        self.assertIn("two-factor enrollment", issues[0])
        self.assertNotIn("confirmed ownership", issues[0])
        incident["store_office_2fa_pending"] = False
        self.assertEqual(monitor.incident_issues(incident), [])

    def test_rebuilt_incident_does_not_claim_rebuild_is_pending(self):
        issues = monitor.incident_issues({"status": "rebuilt_followups_pending", "external_provider_rotation_pending": True, "host_forensic_clearance_complete": False})
        self.assertEqual(len(issues), 2)
        self.assertTrue(any("provider" in issue for issue in issues))
        self.assertFalse(any("rebuild and credential rotation still required" in issue for issue in issues))
        self.assertEqual(monitor.incident_issues({"status": "rebuilt_followups_pending", "external_provider_rotation_pending": False, "host_forensic_clearance_complete": True}), [])

    def test_offline_containment_remains_actionable(self):
        self.assertIn("trusted rebuild", monitor.incident_issues({"status": "contained_not_remediated"})[0])

    def test_change_notification_and_repeat_suppression(self):
        sender = Mock()
        condition = {"nginx": "Nginx is down"}
        self.assertTrue(monitor.deliver_changes(condition, {}, sender))
        sender.assert_called_once()
        sender.reset_mock()
        self.assertFalse(monitor.deliver_changes(condition, condition, sender))
        sender.assert_not_called()
        self.assertTrue(monitor.deliver_changes({}, condition, sender))
        self.assertIn("No longer detected", sender.call_args[0][0])
    def test_delivery_failure_is_not_success(self):
        with self.assertRaises(RuntimeError):
            monitor.deliver_changes({"nginx": "down"}, {}, Mock(side_effect=RuntimeError("failed")))
    def test_old_totals_do_not_trigger_urgent_alerts(self):
        result = {"issues": ["53 actionable Nginx errors in the last hour"], "nginx": {"actionable_15m": 0}}
        self.assertEqual(monitor.alert_conditions(result), {})
        result["nginx"]["actionable_15m"] = 1
        first = monitor.alert_conditions(result)
        result["nginx"]["actionable_15m"] = 2
        self.assertEqual(set(first), set(monitor.alert_conditions(result)))

if __name__ == "__main__":
    unittest.main()
