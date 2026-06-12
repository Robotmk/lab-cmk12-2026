#!/bin/bash

# https://docs.checkmk.com/latest/en/agent_linux_legacy.html#unencrypted

case "${1:-host}" in
  vanilla)
    AGENT_DEB="/omd/sites/cmk/var/check_mk/agents/linux_deb/references/_VANILLA"
    ;;
  localhost|host)
    AGENT_DEB="/omd/sites/cmk/var/check_mk/agents/linux_deb/references/localhost"
    ;;
  *)
    echo "Usage: $0 [vanilla|localhost|host]" >&2
    exit 1
    ;;
esac

echo "▹ Installing the Checkmk agent..."

dpkg -i "$AGENT_DEB" 2> /dev/null

bash /var/lib/cmk-agent/scripts/super-server/1_xinetd/setup deploy
bash /var/lib/cmk-agent/scripts/super-server/1_xinetd/setup trigger

if [[ -f /etc/check_mk/robotmk.json ]]; then
  echo "▹ robotmk.json found — starting RobotMK scheduler in the background..."
  /usr/lib/check_mk_agent/robotmk/robotmk_scheduler /etc/check_mk/robotmk.json &
fi
