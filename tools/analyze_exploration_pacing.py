#!/usr/bin/env python3
"""Reconstructed integrity-first exploration-run analyzer."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

REQUIRED = {"client_video", "position_trace_5s", "event_log", "server_log", "post_run_world_archive"}

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = []
    errors = []
    operators = set()
    cells = Counter()
    for manifest in sorted(args.runs.glob("*/run.json")):
        row = json.loads(manifest.read_text(encoding="utf-8"))
        missing = REQUIRED - set(row.get("artifacts", {}))
        if missing:
            errors.append(f"{manifest}: missing artifacts {sorted(missing)}")
        for name, meta in row.get("artifacts", {}).items():
            path = manifest.parent / meta["path"]
            if not path.is_file() or sha256(path) != meta["sha256"]:
                errors.append(f"{manifest}: artifact mismatch {name}")
        if row.get("review", {}).get("decision") == "valid":
            operators.add(row["operator_id"])
            cells[(row["seed"], row["mode"], row["endpoint"])] += 1
            rows.append(row)
    result = {
        "schema_version":"exploration-analysis-v0.1-reconstructed",
        "valid_runs":len(rows),
        "operators":sorted(operators),
        "cell_counts":{"|".join(k):v for k,v in sorted(cells.items())},
        "errors":errors,
        "gate_passed":not errors and len(operators) >= 2
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return 0 if result["gate_passed"] else 1

if __name__ == "__main__":
    raise SystemExit(main())

