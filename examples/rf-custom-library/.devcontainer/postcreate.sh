#!/usr/bin/env bash
# .devcontainer/postcreate.sh — Runs each time a Codespace is created (not prebuild-cached).
# Configures the user session: PATH and VS Code settings.

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

echo ""
echo -e "${GREEN}${BOLD}Setup complete.${RESET} Open a new terminal to activate the PATH."
