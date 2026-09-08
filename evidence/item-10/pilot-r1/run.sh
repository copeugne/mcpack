#!/usr/bin/env bash
set -euo pipefail
# Run from the repository root. Never overwrite a prior attempt.
test ! -e instances/item10/pilot-r2
test ! -e evidence/raw/item10/pilot-r2
mkdir -p evidence/raw/item10/pilot-r2
TIMEFORMAT='real %R user %U sys %S'
{ time uv run --no-sync python -m tools.run_item7_worldgen run \
  --pristine instances/pristine-baseline-v0 \
  --artifact-manifest evidence/item-3/artifact-acquisition-manifest.json \
  --retained-manifest evidence/item-3/runtime/retained-server-candidates.txt \
  --seed-suite test-environment/seed-suite.json \
  --frozen-config evidence/item-6/frozen \
  --frozen-manifest evidence/item-6/generated-config-manifest.json \
  --config-audit evidence/item-6/config-audit.json \
  --java-home downloads/item2/temurin/extracted/jdk-21.0.12.1+1 \
  --target instances/item10/pilot-r2 \
  --log-path evidence/raw/item10/pilot-r2/console.log \
  --captured-config evidence/raw/item10/pilot-r2/captured-config \
  --receipt evidence/raw/item10/pilot-r2/run.json \
  --role ordinary --timeout-seconds 900 \
  > evidence/raw/item10/pilot-r2/driver-output.json
} 2> evidence/raw/item10/pilot-r2/time.txt
