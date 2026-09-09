#!/usr/bin/env bash
# Run from repository root. Existing outputs are preserved and cause rejection.
set -euo pipefail
output_dir="${1:-evidence/item-13/start-inspection}"
mkdir -p "$output_dir"
for role in biome-diverse mountainous ocean-heavy ordinary; do
  for repetition in 1 2; do
    world="full-${role}-r${repetition}-baseline"
    uv run python -m evidence.item-13.inspect_starts \
      --world "$world" \
      --output "${output_dir}/${world}.json.gz"
  done
done
