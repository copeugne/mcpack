#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 4 ]]; then
  echo "usage: stage_item7_raw_evidence.sh MODE PROJECT_ROOT RAW_ROOT OUTPUT_DIRECTORY" >&2
  exit 2
fi

project=$2
exec uv run --project "$project" python "$project/tools/stage_item7_world.py" "$@"
