#!/usr/bin/env bash
set -euo pipefail

project_root=$(realpath -- "$(dirname -- "$0")/../..")
output="/tmp/mcpack-host-discovery-test-$$.json"
cleanup() {
  status=$?
  trap - EXIT
  unlink -- "$output" 2>/dev/null || true
  exit "$status"
}
trap cleanup EXIT

"$project_root/infrastructure/bin/host-discovery" "$project_root" "$output"
matching_probe_count=$(jq '[
  .authoritative_host_reachability[] |
  select(
    .endpoint == "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json" and
    .http_status == "200"
  )
] | length' "$output")
[[ "$matching_probe_count" == "1" ]]
