#!/usr/bin/env python3
"""Reconstructed streaming counter for rerun structure-start JSON Lines."""
import argparse
import collections
import json
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="JSONL rows with registry_id, category, seed")
    parser.add_argument("output", type=Path)
    parser.add_argument("--full-chunks", type=int, required=True)
    args = parser.parse_args()
    counts = collections.Counter()
    families = collections.Counter()
    seeds = collections.Counter()
    with args.input.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            row = json.loads(line)
            for key in ("registry_id", "category", "seed"):
                if key not in row:
                    raise ValueError(f"line {number}: missing {key}")
            counts[row["category"]] += 1
            families[row["registry_id"]] += 1
            seeds[str(row["seed"])] += 1
    result = {
        "schema_version": "structure-density-analysis-v0.1-reconstructed",
        "full_chunks": args.full_chunks,
        "total_starts": sum(families.values()),
        "per_1000_chunks": 1000 * sum(families.values()) / args.full_chunks,
        "categories": dict(sorted(counts.items())),
        "families": dict(sorted(families.items())),
        "seeds": dict(sorted(seeds.items())),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

