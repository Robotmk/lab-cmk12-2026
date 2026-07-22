#!/usr/bin/env bash
# https://docs.checkmk.com/latest/en/agent_linux_legacy.html#unencrypted
#set -euo pipefail

# ---------------------------------------------------------------------------
# Resolve agent package path from argument
# ---------------------------------------------------------------------------
readonly AGENT_REFS_DIR="/omd/sites/cmk/var/check_mk/agents/linux_deb/references"

case "${1:-host}" in
  vanilla)
    AGENT_DEB="${AGENT_REFS_DIR}/_VANILLA"
    ;;
  host)
    AGENT_DEB="${AGENT_REFS_DIR}/$(hostname)"
    ;;
  localhost)
    AGENT_DEB="${AGENT_REFS_DIR}/localhost"
    ;;
  *)
    echo "Usage: $0 [vanilla|localhost|host]" >&2
    exit 1
    ;;
esac
readonly AGENT_DEB

if [[ ! -f "$AGENT_DEB" ]]; then
    echo "ERROR: Checkmk agent deb package not found: $AGENT_DEB" >&2
    exit 1
fi

# ---------------------------------------------------------------------------
# Install
# ---------------------------------------------------------------------------
echo "▹ Installing Checkmk agent from: $AGENT_DEB"

# In devcontainers systemctl exists but systemd is not the init system.
# The package's preinst script calls systemctl and fails, causing dpkg to
# abort before unpacking any files. Stub systemctl with a no-op for the
# duration of dpkg so maintainer scripts don't break the installation.
if command -v systemctl >/dev/null 2>&1 && ! systemctl is-system-running >/dev/null 2>&1; then
    _STUB_DIR=$(mktemp -d)
    printf '#!/bin/sh\nexit 0\n' > "$_STUB_DIR/systemctl"
    chmod +x "$_STUB_DIR/systemctl"
    export PATH="$_STUB_DIR:$PATH"
    trap 'rm -rf "$_STUB_DIR"' EXIT
fi

dpkg -i "$AGENT_DEB"

ensure_user_shell() {
    # in the devcontainer, the non-root agent user is not allowed to have an interactive shell, which prevents the 
    # scheduler to start properly. We fix this here. 
    local user="$1"
    local desired_shell="/bin/bash"
    local current_shell

    current_shell=$(getent passwd "$user" | cut -d: -f7 || true)
    if [[ -z "$current_shell" ]]; then
        echo "ERROR: user '$user' not found in /etc/passwd" >&2
        exit 1
    fi

    if [[ "$current_shell" != "$desired_shell" ]]; then
        echo "  - updating shell for user '$user' from '$current_shell' to '$desired_shell'"
        if command -v usermod >/dev/null 2>&1; then
            usermod -s "$desired_shell" "$user"
        else
            sed -i -E "s#^($user:[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:).*#\1$desired_shell#" /etc/passwd
        fi
    fi
}

# ---------------------------------------------------------------------------
# Configure xinetd and optionally start the RobotMK scheduler
# ---------------------------------------------------------------------------
setup_agent() {
    local setup_script="$1"
    local robotmk_config="$2"
    local scheduler_bin="$3"
    local run_as_user="${4:-}"

    echo "  - $setup_script deploy"
    bash "$setup_script" deploy

    echo "  - $setup_script trigger"
    bash "$setup_script" trigger

    if [[ -f "$robotmk_config" ]]; then
        echo "▹ robotmk.json found — starting RobotMK scheduler in the background..."
        if pkill -f "robotmk_scheduler" 2>/dev/null; then
            echo "  - killed existing robotmk_scheduler instance"
        fi
        if [[ -n "$run_as_user" ]]; then
            ensure_user_shell "$run_as_user"
            echo "  - starting scheduler as user: $run_as_user"
            su -l "$run_as_user" -c "\"$scheduler_bin\" \"$robotmk_config\"" &
        else
            "$scheduler_bin" "$robotmk_config" &
        fi
    fi
}

if [[ -d /opt/checkmk/agent/ ]]; then
    echo "▹ USER-agent detected"
    _RUNTIME_DIR="/opt/checkmk/agent/default/runtime"
    _AGENT_USER=$(stat -c '%U' "$_RUNTIME_DIR" 2>/dev/null)
    if [[ -z "$_AGENT_USER" ]]; then
        echo "ERROR: could not determine owner of $_RUNTIME_DIR" >&2
        exit 1
    fi
    echo "  - runtime dir owner: $_AGENT_USER"
    setup_agent \
        "/opt/checkmk/agent/default/package/scripts/super-server/1_xinetd/setup" \
        "/opt/checkmk/agent/default/package/config/robotmk.json" \
        "/opt/checkmk/agent/default/package/robotmk/robotmk_scheduler" \
        "$_AGENT_USER"
else
    echo "▹ ROOT-agent detected"
    setup_agent \
        "/var/lib/cmk-agent/scripts/super-server/1_xinetd/setup" \
        "/etc/check_mk/robotmk.json" \
        "/usr/lib/check_mk_agent/robotmk/robotmk_scheduler"
fi