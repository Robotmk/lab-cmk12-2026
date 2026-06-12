#!/usr/bin/env bash
# .devcontainer/postcreate.sh — Runs each time a Codespace is created (not prebuild-cached).
# Configures the user session: PATH, VS Code settings, VNC resolution, and Fluxbox menu.

set -euo pipefail

# ── Colors ────────────────────────────────────────────────────────────────────
BOLD='\033[1m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RESET='\033[0m'

step()  { echo -e "\n${CYAN}${BOLD}▶ $*${RESET}"; }
ok()    { echo -e "${GREEN}✓ $*${RESET}"; }
info()  { echo -e "  ${YELLOW}$*${RESET}"; }

# Resolve SPACE_ROOT from the symlink created during oncreate
SPACE_ROOT="$(readlink -f "$HOME/.rcc-env")"

# ── Step 4: Add to PATH in ~/.bashrc ─────────────────────────────────────────
step "Configuring PATH in ~/.bashrc ..."
MARKER="# rcc-holotree-path"
if grep -q "${MARKER}" "$HOME/.bashrc" 2>/dev/null; then
  info "PATH entry already present — skipping."
else
  echo "${MARKER}" >> "$HOME/.bashrc"
  echo "export PATH=${SPACE_ROOT}/bin:\$PATH" >> "$HOME/.bashrc"
  ok "Added ${SPACE_ROOT}/bin to PATH"
fi

# ── Step 5: Write .vscode/settings.json ──────────────────────────────────────
step "Writing .vscode/settings.json ..."
mkdir -p .vscode
cat > .vscode/settings.json <<EOF
{
  "python.defaultInterpreterPath": "${SPACE_ROOT}/bin/python",
  "python-envs.defaultEnvManager": "ms-python.python:system",
  "robotcode.run.openOutputAfterRun": "log",
  "window.autoDetectColorScheme": true
}
EOF
ok "python.defaultInterpreterPath → ${SPACE_ROOT}/bin/python"

# ── Step 6: Configure fluxbox resolution ─────────────────────────────────────
step "Configuring fluxbox resolution ..."
FLUXBOX_STARTUP="$HOME/.fluxbox/startup"
VNC_RESOLUTION="1280x1024"
if grep -q '^VNC_RESOLUTION=' .env 2>/dev/null; then
  VNC_RESOLUTION="$(grep '^VNC_RESOLUTION=' .env | cut -d= -f2 | tr -d '[:space:]')"
fi
XRANDR_LINE="xrandr --output VNC-0 --mode ${VNC_RESOLUTION}"
if grep -qF "xrandr --output VNC-0 --mode" "${FLUXBOX_STARTUP}" 2>/dev/null; then
  info "xrandr entry already present — skipping."
else
  sed -i "s|^exec fluxbox|${XRANDR_LINE}\nexec fluxbox|" "${FLUXBOX_STARTUP}"
  ok "Set VNC resolution to ${VNC_RESOLUTION} in ${FLUXBOX_STARTUP}"
fi

# ── Step 9: Configure Fluxbox menu ───────────────────────────────────────────
step "Configuring Fluxbox menu ..."
MENU_FILE="${HOME}/.fluxbox/menu"
if [[ -f "${MENU_FILE}" ]] && ! grep -qF "firefox" "${MENU_FILE}"; then
  sed -i '/^\[begin\]/a\  [exec] (Checkmk) {firefox-esr http://localhost:5000/cmk}' "${MENU_FILE}"
  ok "Checkmk shortcut added to Fluxbox menu."
else
  info "Fluxbox menu entry already present — skipping."
fi
# Restart Fluxbox to pick up menu changes (if already running)
pkill fluxbox 2>/dev/null || true
nohup fluxbox >/dev/null 2>&1 &
disown

echo ""
echo -e "${GREEN}${BOLD}Setup complete.${RESET} Open a new terminal to activate the PATH."
