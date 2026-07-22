#!/usr/bin/env bash
# .devcontainer/oncreate.sh — Runs once when the container image is built (prebuild-cached).
# Downloads RCC, builds the holotree environment, installs the Checkmk agent and Firefox.

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

RCC_URL="https://github.com/elabit/robotmk/releases/download/v4.0.0/rcc_linux64"
RCC_BIN="$HOME/bin/rcc"

# ── Step 1: Download RCC ──────────────────────────────────────────────────────
step "Downloading RCC ..."
mkdir -p "$HOME/bin"
curl -fsSL -o "$RCC_BIN" "$RCC_URL"
chmod +x "$RCC_BIN"
ok "RCC $(${RCC_BIN} --version 2>&1 | head -1) ready at ${RCC_BIN}"

# ── Step 2: Build holotree environment ────────────────────────────────────────
step "Building RCC holotree environment (this takes a few minutes on first run) ..."
info "robot.yaml: $(pwd)/robot.yaml"
SPACE_ROOT=$(
  "$RCC_BIN" holotree vars --robot robot.yaml 2>&1 \
    | grep '^export RCC_HOLOTREE_SPACE_ROOT=' \
    | cut -d= -f2
)
ok "Environment ready at ${SPACE_ROOT}"

# ── Step 3: Symlink ~/.rcc-env ────────────────────────────────────────────────
step "Creating symlink ~/.rcc-env → ${SPACE_ROOT} ..."
ln -sfn "${SPACE_ROOT}" "$HOME/.rcc-env"
ok "~/.rcc-env → ${SPACE_ROOT}"

# ── Step 7: Install Checkmk agent ────────────────────────────────────────────
step "Installing Checkmk agent ..."
bash "$(dirname "$0")/install_cmk_agent.sh" vanilla
ok "Checkmk agent installed."

# ── Step 8: Install Firefox via Mozilla PPA ───────────────────────────────────
step "Installing Firefox via Mozilla PPA ..."
apt-get update -qq
apt-get install -y --no-install-recommends software-properties-common
add-apt-repository -y ppa:mozillateam/ppa
# Pin Mozilla PPA above Ubuntu's snap redirect (priority 1001 > default 500)
cat > /etc/apt/preferences.d/mozilla-firefox <<'EOF'
Package: *
Pin: release o=LP-PPA-mozillateam
Pin-Priority: 1001
EOF
apt-get update -qq
apt-get install -y --no-install-recommends firefox-esr
ok "Firefox installed."

# install additional tools
apt-get install -y --no-install-recommends jq curl wget vim htop sudo python3-pip

echo ""
echo -e "${GREEN}${BOLD}Container creation complete.${RESET}"
