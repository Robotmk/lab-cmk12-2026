#!/usr/bin/env bash
# .devcontainer/oncreate.sh — Runs once when the container image is built (prebuild-cached).
# Downloads RCC and builds the holotree environment.

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

echo ""
echo -e "${GREEN}${BOLD}Container creation complete.${RESET}"
