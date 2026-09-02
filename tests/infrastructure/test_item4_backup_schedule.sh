#!/usr/bin/env bash
set -euo pipefail

root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)
service="$root/infrastructure/systemd/mcpack-item4-backup@.service"
timer="$root/infrastructure/systemd/mcpack-item4-backup@.timer"

test -x "$root/infrastructure/bin/item4-automated-backup"
rg -F 'ExecStart=/workspace/mcpack/infrastructure/bin/item4-automated-backup' "$service" >/dev/null
rg -F 'OnCalendar=*-*-* 03:15:00 UTC' "$timer" >/dev/null
rg -F 'Persistent=true' "$timer" >/dev/null
rg -F 'WantedBy=timers.target' "$timer" >/dev/null
