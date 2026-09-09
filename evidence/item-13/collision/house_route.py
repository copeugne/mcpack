"""Check the predeclared first-house route against complete swept actor boxes."""

# pyright: standard
# ruff: noqa: INP001, D103, EM101, TRY003
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from itertools import pairwise
from pathlib import Path

from .clearance import ROOT, expand_shapes, overlaps

UPRIGHT_HEIGHT = 1.8

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


def verify(*, crouch_balcony: bool = False) -> dict[str, object]:
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
    for a, b in pairwise(route):
        height = 1.5 if crouch_balcony and min(a[1], b[1]) > OUTBOUND[0][1] else UPRIGHT_HEIGHT
        if sum(x != y for x, y in zip(a, b, strict=True)) != 1:
            raise ValueError("Only cardinal or vertical segments are declared")
        sweep = [
            min(a[0], b[0]) - 0.3,
            min(a[1], b[1]),
            min(a[2], b[2]) - 0.3,
            max(a[0], b[0]) + 0.3,
            max(a[1], b[1]) + height,
            max(a[2], b[2]) + 0.3,
        ]
        collisions = [box for box in boxes if overlaps(sweep, box)]
        segments.append(
            {
                "from": a,
                "to": b,
                "actor_height": height,
                "swept_box": sweep,
                "collisions": collisions,
            }
        )
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


def measure_saved_route() -> dict[str, object]:
    source = Path(__file__).with_name("r2-route.json")
    raw = source.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != "1174496c1e0629df468b31516a0d70ca583d9c485094b9a39bc808e9720c9aca":
        raise ValueError("The predeclared route identity differs")
    route = json.loads(raw)
    segments = route["segments"]
    if not route["collision_free"] or any(s["collisions"] for s in segments):
        raise ValueError("Cannot time a rejected route")
    if segments[0]["from"] != segments[-1]["to"]:
        raise ValueError("Inspection circuit is not closed")
    distances = dict.fromkeys(("upright_horizontal", "crouched_horizontal", "vine", "step"), 0.0)
    ascent = descent = 0.0
    for segment in segments:
        a, b = segment["from"], segment["to"]
        dy = b[1] - a[1]
        ascent += max(0, dy)
        descent += max(0, -dy)
        if dy:
            category = "vine" if segment["actor_height"] == UPRIGHT_HEIGHT else "step"
        else:
            category = (
                "upright_horizontal"
                if segment["actor_height"] == UPRIGHT_HEIGHT
                else "crouched_horizontal"
            )
        distances[category] += sum(abs(x - y) for x, y in zip(a, b, strict=True))
    profiles = {
        "nominal": (4, 1.2, 1, 0.5),
        "faster": (5, 1.5, 2, 1),
        "slower": (3, 0.9, 0.5, 0.25),
    }
    modeled = {
        name: {
            "rates_blocks_per_second": dict(zip(distances, rates, strict=True)),
            "seconds": sum(
                distance / rate for distance, rate in zip(distances.values(), rates, strict=True)
            ),
        }
        for name, rates in profiles.items()
    }
    heights = [point[1] for s in segments for point in (s["from"], s["to"])]
    return {
        "route_sha256": digest,
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "distances_blocks": distances,
        "total_route_blocks": sum(distances.values()),
        "feet_height_span_blocks": max(heights) - min(heights),
        "ascent_blocks": ascent,
        "descent_blocks": descent,
        "model_scenarios": modeled,
        "human_traversal_time": "NOT MEASURED",
        "scope": "Conditional local inspection circuit, not full clear or all-container survey",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--crouch-balcony", action="store_true")
    mode.add_argument("--measure", action="store_true")
    args = parser.parse_args()
    result = measure_saved_route() if args.measure else verify(crouch_balcony=args.crouch_balcony)
    with args.output.open("x") as stream:
        _ = stream.write(json.dumps(result, indent=2) + "\n")
