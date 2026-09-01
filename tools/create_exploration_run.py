#!/usr/bin/env python3
"""Create a non-overwriting draft Item 11 run manifest."""
import argparse
import json
from pathlib import Path

BEARINGS = {"fixed_time": [0, 120, 240], "fixed_distance": [60, 180, 300]}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--seed", required=True)
    parser.add_argument("--mode", choices=["foot","standardized_horse","vanilla_boat"], required=True)
    parser.add_argument("--endpoint", choices=sorted(BEARINGS), required=True)
    parser.add_argument("--replicate", type=int, choices=[1,2,3], required=True)
    parser.add_argument("--operator", required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit(f"refusing to overwrite {args.output}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "run_id": f"{args.seed}-{args.mode}-{args.endpoint}-r{args.replicate}",
        "seed": args.seed,
        "mode": args.mode,
        "endpoint": args.endpoint,
        "replicate": args.replicate,
        "bearing_degrees": BEARINGS[args.endpoint][args.replicate - 1],
        "operator_id": args.operator,
        "status": "draft",
        "observations": [],
        "meaningful_intervals": [],
        "review": {"reviewer_id": "", "decision": "pending"},
        "artifacts": {}
    }
    args.output.write_text(json.dumps(row, indent=2) + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

