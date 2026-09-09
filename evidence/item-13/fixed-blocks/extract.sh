#!/usr/bin/env bash
# Run from repository root and supply a new output directory.
set -euo pipefail
output_dir="${1:?supply a new reproduction directory}"
mkdir "$output_dir"
set -o noclobber
for root in mns:medium_house mns:circle_nether_brick mns:giant_skull \
  mns:large_house_1 mns:medium_house_2 mns:nether_tower mns:warped_dome \
  mss:desert_pyramid mss:small_tower; do
  label="${root//:/-}"
  if [[ "$root" == mns:medium_house ]]; then label=mns-medium-house; fi
  uv run python -m evidence.item-13.measure --fixed-root "$root" \
    --output "${output_dir}/${label}.json.gz" > "${output_dir}/${label}-execution.txt" 2>&1
done
