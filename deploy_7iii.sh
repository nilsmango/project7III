#!/bin/bash
set -euo pipefail

# Always build from source; never deploy a stale or partially generated public/.
DEPLOY_SITE_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
source "$DEPLOY_SITE_DIR/deploy_config.sh"

DEPLOY_MODE="${1:-}"
if [[ $# -gt 1 || ( -n "$DEPLOY_MODE" && "$DEPLOY_MODE" != --dry-run ) ]]; then
    echo "Usage: $0 [--dry-run]" >&2
    exit 2
fi
[[ "$DEPLOY_HOST" == 46.225.71.191 && "$DEPLOY_USER" == simxn ]] || {
    echo "Unexpected deployment host or account; refusing deployment." >&2; exit 1;
}
[[ "$DEPLOY_REMOTE_PATH" == /var/www/project7iii.com ]] || {
    echo "Unexpected deletion target; refusing deployment." >&2; exit 1;
}
[[ -r "$DEPLOY_SSH_KEY" ]] || { echo "SSH key is not readable." >&2; exit 1; }
command -v zola >/dev/null
command -v rsync >/dev/null

DEPLOY_BUILD_DIR="$(mktemp -d "${TMPDIR:-/tmp}/project7iii-deploy.XXXXXX")"
cleanup() {
    # Only remove the exact temporary directory this invocation created.
    if [[ "$DEPLOY_BUILD_DIR" == */project7iii-deploy.* && -d "$DEPLOY_BUILD_DIR" ]]; then
        rm -rf -- "$DEPLOY_BUILD_DIR"
    fi
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

(cd "$DEPLOY_SITE_DIR" && zola build --output-dir "$DEPLOY_BUILD_DIR/site")
for DEPLOY_REQUIRED_FILE in index.html 404.html robots.txt tap/index.html tap/manual/index.html water/index.html apps/index.html projects/index.html; do
    [[ -s "$DEPLOY_BUILD_DIR/site/$DEPLOY_REQUIRED_FILE" ]] || {
        echo "Build is incomplete: missing $DEPLOY_REQUIRED_FILE. Server unchanged." >&2
        exit 1
    }
done
# No symlinks from a generated build should be installed on the server.
if [[ -n "$(find "$DEPLOY_BUILD_DIR/site" -type l -print -quit)" ]]; then
    echo "Unexpected symlink in build; refusing deployment." >&2
    exit 1
fi

# Fresh builds have fresh mtimes; compare contents instead of re-uploading them.
DEPLOY_RSYNC_OPTIONS=(--recursive --checksum --compress --verbose --itemize-changes
    --delay-updates --delete-delay --exclude=/foildata/ --no-perms --omit-dir-times
    --chmod=Du=rwx,Dgo=rx,Fu=rw,Fgo=r)
[[ "$DEPLOY_MODE" != --dry-run ]] || DEPLOY_RSYNC_OPTIONS+=(--dry-run)
printf -v DEPLOY_SSH_COMMAND 'ssh -o BatchMode=yes -o ConnectTimeout=15 -o StrictHostKeyChecking=yes -i %q' "$DEPLOY_SSH_KEY"
rsync "${DEPLOY_RSYNC_OPTIONS[@]}" -e "$DEPLOY_SSH_COMMAND" \
    "$DEPLOY_BUILD_DIR/site/" "$DEPLOY_USER@$DEPLOY_HOST:$DEPLOY_REMOTE_PATH/"

if [[ "$DEPLOY_MODE" == --dry-run ]]; then
    echo "Fresh build validated; dry run complete. Server unchanged."
    exit 0
fi
# Check Nginx directly, bypassing Cloudflare's command-line bot challenge.
ssh -o BatchMode=yes -o ConnectTimeout=15 -o StrictHostKeyChecking=yes -i "$DEPLOY_SSH_KEY" \
    "$DEPLOY_USER@$DEPLOY_HOST" 'set -eu
for path in / /tap/ /tap/manual/ /water/ /robots.txt; do
    code=$(curl -ksS --max-time 15 --resolve project7iii.com:443:127.0.0.1 -o /dev/null -w "%{http_code}" "https://project7iii.com$path")
    printf "%s HTTP %s\n" "$path" "$code"
    test "$code" = 200
done
code=$(curl -ksS --max-time 15 --resolve project7iii.com:443:127.0.0.1 -o /dev/null -w "%{http_code}" https://project7iii.com/__deployment_missing_page_check)
test "$code" = 404'
echo "Deployment and origin checks passed."
