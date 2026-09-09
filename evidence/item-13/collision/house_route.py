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
DEFAULT_STEP_HEIGHT = 0.6

# Coordinates mark turns, vine transfer and the central trapdoor height change.
OUTBOUND = [
    [467.5, 45.0, 435.5],
    [467.5, 45.0, 433.5],
    [461.5, 45.0, 433.5],
    [461.5, 45.0, 431.5],
    [461.5, 47.5, 431.5],
    [464.3, 47.5, 431.5],
    [464.3, 47.1875, 431.5],
    [464.7, 47.1875, 431.5],
    [464.7, 47.5, 431.5],
    [466.5, 47.5, 431.5],
]


SECOND_OUTBOUND = [
    [19.5, 34.0, 115.5],
    [19.5, 34.0, 112.5],
    [15.5, 34.0, 112.5],
    [15.5, 34.0, 114.5],
    [14.5, 34.0, 114.5],
    [14.5, 36.5, 114.5],
    [14.5, 36.5, 112.7],
    [14.5, 36.1875, 112.7],
    [14.5, 36.1875, 112.3],
    [14.5, 36.5, 112.3],
    [14.5, 36.5, 111.5],
]


def verify(  # noqa: C901 - same bounded verifier for two current layouts.
    *, crouch_balcony: bool = False, second_house: bool = False
) -> dict[str, object]:
    collision = Path(__file__).with_name(
        "house2-r1-collision.json.gz" if second_house else "r1-collision.json.gz"
    )
    raw = collision.read_bytes()
    shapes = json.loads(gzip.decompress(raw))
    blocks = (
        ROOT
        / "evidence/item-13/fixed-blocks"
        / ("mns-medium_house_2.json.gz" if second_house else "mns-medium-house.json.gz")
    )
    if hashlib.sha256(blocks.read_bytes()).hexdigest() != shapes["input_sha256"]:
        raise ValueError("Saved blocks and collision input differ")
    case = json.loads(gzip.decompress(blocks.read_bytes()))["cases"][0]
    if shapes["bounds"] != case["bounds"] or shapes["unsupported"]:
        raise ValueError("Collision coverage is incomplete")
    if second_house:
        bounds = case["bounds"]
        nx, nz = bounds[3] - bounds[0] + 1, bounds[5] - bounds[2] + 1
        for y, half in ((34, "lower"), (35, "upper")):
            index = ((y - bounds[1]) * nz + 115 - bounds[2]) * nx + 19 - bounds[0]
            state = case["palette"][case["blocks_yzx"][index]]
            if state != {
                "Name": "minecraft:crimson_door",
                "Properties": {
                    "facing": "north",
                    "half": half,
                    "hinge": "right",
                    "open": "false",
                    "powered": "false",
                },
            }:
                raise ValueError("Second-house door state differs from the declared model")
            shape_index = shapes["shape_indices_yzx"][index]
            if shapes["local_aabbs"][shape_index] != [[0, 0, 0.8125, 1, 1, 1]]:
                raise ValueError("Second-house closed-door collision differs")
            shapes["shape_indices_yzx"][index] = len(shapes["local_aabbs"])
            shapes["local_aabbs"].append([[0.8125, 0, 0, 1, 1, 1]])
    boxes = expand_shapes(shapes, case["bounds"])
    outbound = SECOND_OUTBOUND if second_house else OUTBOUND
    route = outbound + list(reversed(outbound[:-1]))
    segments = []
    for a, b in pairwise(route):
        height = 1.5 if crouch_balcony and min(a[1], b[1]) > outbound[0][1] else UPRIGHT_HEIGHT
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
        if height < UPRIGHT_HEIGHT and a[1] != b[1]:
            lower, upper = sorted((a[1], b[1]))
            if upper - lower > DEFAULT_STEP_HEIGHT:
                raise ValueError("Balcony transition exceeds declared default step height")
            adjacent = [
                box
                for box in boxes
                if box[4] == upper
                and box[1] <= lower < box[4]
                and any(
                    (box[axis + 3] == sweep[axis] or box[axis] == sweep[axis + 3])
                    and box[2 - axis] < sweep[5 - axis]
                    and sweep[2 - axis] < box[5 - axis]
                    for axis in (0, 2)
                )
            ]
            if not adjacent:
                raise ValueError("No adjacent support at the balcony height transition")
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
        "modeled_state_changes": (
            "Right crimson door at 19,34/35,115 opened in geometry only" if second_house else None
        ),
        "segments": segments,
        "collision_free": all(not s["collisions"] for s in segments),
        "support": (
            "Manual floor/vine inspection required; checker verifies swept collision "
            "and balcony step adjacency"
        ),
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
    parser.add_argument("--second-house", action="store_true")
    args = parser.parse_args()
    if args.measure and args.second_house:
        parser.error("--measure retains the historical first-house r2 calculation only")
    result = (
        measure_saved_route()
        if args.measure
        else verify(crouch_balcony=args.crouch_balcony, second_house=args.second_house)
    )
    with args.output.open("x") as stream:
        _ = stream.write(json.dumps(result, indent=2) + "\n")
