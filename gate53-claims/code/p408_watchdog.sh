#!/bin/bash
# Phase 408 pool-priority watchdog: while any p408_pool process runs on the
# pool, sample available RAM every ~2 min. If available < 2500 MiB on 3
# consecutive samples (~5 min sustained), kill the p408 search
# (checkpoint-safe), log POOL-PRIORITY YIELD, and exit.
LOG=~/workspace/warp-pilot/phase408/results/p408_ram_log.txt
SSH() { ssh -o ProxyCommand="python3 ~/workspace/laptop-compute/proxy-connect.py %h %p" -i ~/.ssh/id_ed25519 -o ConnectTimeout=20 spark@100.71.86.14 "$@" 2>/dev/null; }
echo "$(date -u +%FT%TZ) watchdog start" >> "$LOG"
low=0
while true; do
  running=$(SSH 'pgrep -fc p408_pool || true')
  avail=$(SSH "free -m | awk '/^Mem:/{print \$7}'")
  ts=$(date -u +%FT%TZ)
  echo "$ts avail_MiB=${avail:-NA} p392_procs=${running:-NA}" >> "$LOG"
  if [ -z "$running" ] || [ "$running" = "0" ]; then
    echo "$ts no p408 processes; watchdog exit" >> "$LOG"
    exit 0
  fi
  if [ -n "$avail" ] && [ "$avail" -lt 2500 ]; then
    low=$((low+1))
    echo "$ts LOW RAM count=$low" >> "$LOG"
  else
    low=0
  fi
  if [ "$low" -ge 3 ]; then
    echo "$ts POOL-PRIORITY YIELD: available RAM < 2.5 GiB sustained ~5 min; killing p408 search (checkpoint-safe)" >> "$LOG"
    SSH 'pkill -f p408_pool || true'
    exit 2
  fi
  sleep 120
done
