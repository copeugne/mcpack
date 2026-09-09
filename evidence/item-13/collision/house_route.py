"""Check the predeclared first-house route against complete swept actor boxes."""

# pyright: standard
# ruff: noqa: INP001, D103, EM101, TRY003
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

from .clearance import ROOT, expand_shapes, overlaps

# Coordinates mark turns, vine transfer and the central trapdoor height change.
OUTBOUND = [
    [467.5, 45.0, 435.5],
    [467.5, 45.0, 433.5],
    [461.5, 45.0, 433.5],
    [461.5, 45.0, 431.5],
    [461.5, 47.5, 431.5],
    [464.5, 47.5, 431.5],
    [464.5, 47.1875, 431.5],
    [464.5, 47.5, 431.5],
    [466.5, 47.5, 431.5],
]


def verify() -> dict[str, object]:
    collision = ROOT / "evidence/item-13/collision/r1-collision.json.gz"
    raw = collision.read_bytes()
    shapes = json.loads(gzip.decompress(raw))
    blocks = ROOT / "evidence/item-13/fixed-blocks/mns-medium-house.json.gz"
    if hashlib.sha256(blocks.read_bytes()).hexdigest() != shapes["input_sha256"]:
        raise ValueError("Saved blocks and collision input differ")
    case = json.loads(gzip.decompress(blocks.read_bytes()))["cases"][0]
    if shapes["bounds"] != case["bounds"] or shapes["unsupported"]:
        raise ValueError("Collision coverage is incomplete")
    boxes = expand_shapes(shapes, case["bounds"])
    route = OUTBOUND + list(reversed(OUTBOUND[:-1]))
    segments = []
    for a, b in zip(route, route[1:], strict=False):
        if sum(x != y for x, y in zip(a, b, strict=True)) != 1:
            raise ValueError("Only cardinal or vertical segments are declared")
        sweep = [
            min(a[0], b[0]) - 0.3,
            min(a[1], b[1]),
            min(a[2], b[2]) - 0.3,
            max(a[0], b[0]) + 0.3,
            max(a[1], b[1]) + 1.8,
            max(a[2], b[2]) + 0.3,
        ]
        collisions = [box for box in boxes if overlaps(sweep, box)]
        segments.append({"from": a, "to": b, "swept_box": sweep, "collisions": collisions})
    return {
        "collision_gzip_sha256": hashlib.sha256(raw).hexdigest(),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "geometry_helper_sha256": hashlib.sha256(
            Path(__file__).with_name("clearance.py").read_bytes()
        ).hexdigest(),
        "segments": segments,
        "collision_free": all(not s["collisions"] for s in segments),
        "support": "Manual block inspection required; this checker verifies collision only",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    with args.output.open("x") as stream:
        _ = stream.write(json.dumps(verify(), indent=2) + "\n")
