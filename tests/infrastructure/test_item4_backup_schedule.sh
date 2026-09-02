#!/usr/bin/env bash
set -euo pipefail

root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)
service="$root/infrastructure/systemd/mcpack-item4-backup@.service"
timer="$root/infrastructure/systemd/mcpack-item4-backup@.timer"

test -x "$root/infrastructure/bin/item4-automated-backup"
rg -F 'ExecStart=/workspace/mcpack/infrastructure/bin/item4-automated-backup' "$service" >/dev/null
rg -F 'User=mcpack' "$service" >/dev/null
rg -F 'Group=mcpack' "$service" >/dev/null
rg -F 'NoNewPrivileges=true' "$service" >/dev/null
rg -F 'ProtectSystem=strict' "$service" >/dev/null
rg -F 'ReadWritePaths=/workspace/mcpack/instances/item4' "$service" >/dev/null
rg -F 'ReadWritePaths=/workspace/mcpack/backups/item4/automated' "$service" >/dev/null
rg -F 'ReadWritePaths=/workspace/mcpack/evidence/raw/item4/automated-backups' "$service" >/dev/null
rg -F 'sudo chown -R --no-dereference mcpack:mcpack \' \
  "$root/test-environment/README.md" >/dev/null
rg -F '/workspace/mcpack/backups/item4/automated \' \
  "$root/test-environment/README.md" >/dev/null
rg -F '/workspace/mcpack/evidence/raw/item4/automated-backups' \
  "$root/test-environment/README.md" >/dev/null
rg -F 'OnCalendar=*-*-* 03:15:00 UTC' "$timer" >/dev/null
rg -F 'Persistent=true' "$timer" >/dev/null
rg -F 'WantedBy=timers.target' "$timer" >/dev/null
