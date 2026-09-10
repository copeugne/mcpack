"""Conditional routes through manually inspected saved small-dungeon chambers."""

# pyright: standard
# ruff: noqa: ANN001, ANN201, D103, EM101, TRY003, INP001, PLR2004
from __future__ import annotations

import gzip
import hashlib
import itertools
import json
import math
from collections import deque
from pathlib import Path

from render_pilot import state_at

ROOT = Path(__file__).resolve().parent
AIR = {"minecraft:air", "minecraft:cave_air"}
SUPPORT = {"minecraft:cobblestone", "minecraft:mossy_cobblestone"}


def paths(
    cells: set[tuple[int, int, int]], start: tuple[int, int, int]
) -> dict[tuple[int, int, int], list[tuple[int, int, int]]]:
    if start not in cells:
        raise ValueError("declared entry is not a supported standing cell")
    found = {start: [start]}
    queue = deque([start])
    while queue:
        x, y, z = queue.popleft()
        for nxt in sorted(((x - 1, y, z), (x + 1, y, z), (x, y, z - 1), (x, y, z + 1))):
            if nxt in cells and nxt not in found:
                found[nxt] = [*found[(x, y, z)], nxt]
                queue.append(nxt)
    return found


def intersects(start, end, block):
    """Conservative closed voxel/segment intersection; corner touches block sight."""
    lower, upper = 0.0, 1.0
    for a, b, c in zip(start, end, block, strict=True):
        delta = b - a
        if abs(delta) < 1e-12:
            if not c <= a <= c + 1:
                return False
        else:
            limits = sorted(((c - a) / delta, (c + 1 - a) / delta))
            lower, upper = max(lower, limits[0]), min(upper, limits[1])
            if lower > upper:
                return False
    return upper > 0 and lower < 1


def visible(case, cell, target):
    start = (cell[0] + 0.5, cell[1] + 1.62, cell[2] + 0.5)
    end = tuple(c + 0.5 for c in target)
    if math.dist(start, end) > 3:
        return False
    axes = [
        range(math.floor(min(a, b)), math.floor(max(a, b)) + 1)
        for a, b in zip(start, end, strict=True)
    ]
    return all(
        block == target
        or not intersects(start, end, block)
        or state_at(case, *block)["Name"] in AIR
        for block in itertools.product(*axes)
    )


def analyze(case, coding):
    room = coding["rooms"][0]
    x0, z0, x1, z1 = room["interior_xz"]
    y = room["floor_y"] + 1
    cells = {
        (x, y, z)
        for x in range(x0, x1 + 1)
        for z in range(z0, z1 + 1)
        if state_at(case, x, y, z)["Name"] in AIR
        and state_at(case, x, y + 1, z)["Name"] in AIR
        and state_at(case, x, y - 1, z)["Name"] in SUPPORT
    }
    entry = tuple(coding["entry"])
    spawners = [b for b in case["block_entities"] if b["id"] == "minecraft:mob_spawner"]
    if len(spawners) != 1:
        raise ValueError("pilot requires exactly one saved spawner")
    containers = sorted(
        (b for b in case["block_entities"] if "LootTable" in b),
        key=lambda b: (b["x"], b["y"], b["z"]),
    )
    route = [entry]
    segments = []
    for target in [*spawners, *containers]:
        position = tuple(target[k] for k in ("x", "y", "z"))
        reachable = paths(cells, route[-1])
        options = [p for p in reachable if visible(case, p, position)]
        if not options:
            message = f"no reachable interaction cell for {position}"
            raise ValueError(message)
        stop = min(options, key=lambda p: (len(reachable[p]), p))
        path = reachable[stop]
        route.extend(path[1:])
        segments.append(
            {"target": position, "kind": target["id"], "path": path, "steps": len(path) - 1}
        )
    home = paths(cells, route[-1])[entry]
    route.extend(home[1:])
    spawner = spawners[0]
    enemy = spawner["SpawnData"]["entity"]["id"]
    hits = {"minecraft:skeleton": 4, "minecraft:spider": 3}[enemy]
    count = spawner["SpawnCount"]
    cover = [p[2] - case["envelope"][4] for p in case["surface_xzy"]]
    return {
        "id": case["id"],
        "standing_cells": len(cells),
        "reachable_standing_cells": len(paths(cells, entry)),
        "segments": segments,
        "return_path": home,
        "route": route,
        "route_length_blocks": len(route) - 1,
        "modeled_traversal_seconds_by_speed": {
            str(speed): (len(route) - 1) / speed for speed in (3, 4, 5)
        },
        "saved_spawners": 1,
        "saved_enemy_types": [enemy],
        "modeled_one_wave_enemy_count": [0, count],
        "modeled_active_attack_seconds": [0, count * hits * 13 / 20],
        "modeled_50_percent_contact_seconds": [0, count * hits * 13 / 10],
        "saved_initial_delay_ticks": spawner["Delay"],
        "active_spawner_clear_time": "UNKNOWN; no finite upper bound established",
        "loot_table_containers": len(containers),
        "container_types": {
            kind: sum(b["id"] == kind for b in containers)
            for kind in sorted({b["id"] for b in containers})
        },
        "container_room_distribution": {"R1": len(containers)},
        "surface_top_minus_envelope_top_blocks": [min(cover), max(cover)],
        "human_times_realized_encounters_generated_or_acquired_loot": "NOT MEASURED",
    }


def main():
    raw = (ROOT / "pilot/observations.json.gz").read_bytes()
    coding_bytes = (ROOT / "pilot/coding.json").read_bytes()
    coding = json.loads(coding_bytes)
    if hashlib.sha256(raw).hexdigest() != coding["source_sha256"]:
        raise ValueError("manual coding does not match raw observation hash")
    observations = json.loads(gzip.decompress(raw))
    by_world = {c["world"]: c for c in coding["cases"]}
    if set(by_world) != {c["world"] for c in observations["cases"]}:
        raise ValueError("manual coding and observation cases differ")
    result = {
        "raw_sha256": coding["source_sha256"],
        "coding_sha256": hashlib.sha256(coding_bytes).hexdigest(),
        "cases": [analyze(c, by_world[c["world"]]) for c in observations["cases"]],
    }
    (ROOT / "pilot/results.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
