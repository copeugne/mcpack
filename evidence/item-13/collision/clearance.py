"""Compute predeclared static standing clearance from retained collision AABBs."""

# pyright: standard
# ruff: noqa: INP001, D103, EM101, TRY003
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def overlaps(a: list[float], b: list[float]) -> bool:
    return all(a[i] < b[i + 3] and b[i] < a[i + 3] for i in range(3))


def calculate() -> dict[str, object]:  # noqa: C901 - one bounded geometric pass.
    source = ROOT / "evidence/item-13/collision/r1-collision.json.gz"
    raw = source.read_bytes()
    shapes = json.loads(gzip.decompress(raw))
    blocks = ROOT / "evidence/item-13/fixed-blocks/mns-medium-house.json.gz"
    if hashlib.sha256(blocks.read_bytes()).hexdigest() != shapes["input_sha256"]:
        raise ValueError("Collision source does not match saved blocks")
    case = json.loads(gzip.decompress(blocks.read_bytes()))["cases"][0]
    b = case["bounds"]
    e = case["envelope"]
    if b != shapes["bounds"] or shapes["unsupported"]:
        raise ValueError("Unsupported or mismatched collision coverage")
    nx, nz = b[3] - b[0] + 1, b[5] - b[2] + 1
    cells = shapes["shape_indices_yzx"]
    if len(cells) != len(case["blocks_yzx"]):
        raise ValueError("Missing collision cells")
    world_boxes: list[list[float]] = []
    for i, index in enumerate(cells):
        if not 0 <= index < len(shapes["local_aabbs"]):
            raise ValueError("Invalid collision shape index")
        xyz = [b[0] + i % nx, b[1] + i // (nx * nz), b[2] + i // nx % nz]
        world_boxes.extend(
            [box[j] + xyz[j % 3] for j in range(6)] for box in shapes["local_aabbs"][index]
        )
    accepted: list[list[float]] = []
    candidates = 0
    for z in range(e[2], e[5] + 1):
        for x in range(e[0], e[3] + 1):
            cx, cz = x + 0.5, z + 0.5
            nearby = [
                a
                for a in world_boxes
                if a[0] < cx + 0.3 and a[3] > cx - 0.3 and a[2] < cz + 0.3 and a[5] > cz - 0.3
            ]
            heights = sorted(
                {
                    a[4]
                    for a in nearby
                    if a[0] <= cx <= a[3]
                    and a[2] <= cz <= a[5]
                    and a[1] < a[4]
                    and e[1] <= a[4] <= e[4]
                }
            )
            for y in heights:
                actor = [cx - 0.3, y, cz - 0.3, cx + 0.3, y + 1.8, cz + 0.3]
                if any(actor[j] < b[j] or actor[j + 3] > b[j + 3] + 1 for j in range(3)):
                    raise ValueError("Actor clearance extends outside retained bounds")
                candidates += 1
                if not any(overlaps(actor, box) for box in nearby):
                    accepted.append([cx, y, cz])
    return {
        "collision_gzip_sha256": hashlib.sha256(raw).hexdigest(),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "envelope": e,
        "actor_width": 0.6,
        "actor_height": 1.8,
        "candidate_positions": candidates,
        "standing_positions": sorted(accepted, key=lambda v: (v[1], v[2], v[0])),
        "meaning": "Static empty-context clearance only; reachability and rooms NOT MEASURED",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    result = calculate()
    with args.output.open("x") as stream:
        _ = stream.write(json.dumps(result, indent=2) + "\n")
