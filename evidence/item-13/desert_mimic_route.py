"""Check the complete declared Desert Mimic case against retained blocks."""

# pyright: standard
# ruff: noqa: INP001, S101, ANN001, ANN201, D103, T201, PLR2004
import copy
import gzip
import hashlib
import importlib
import json
import sys
from itertools import pairwise
from pathlib import Path

raw = (Path(__file__).parent / "fixed-blocks/towns-and-towers-desert-mimic.json.gz").read_bytes()
assert (
    hashlib.sha256(raw).hexdigest()
    == "02a98398ed6deae4c084055a095d2e3d9ed0454a2595beff41278216b7ee884a"
)
original = json.loads(gzip.decompress(raw))["cases"][0]
c = copy.deepcopy(original)
at = importlib.import_module("evidence.item-13.render_pilot").state_at
geometry = importlib.import_module("evidence.item-13.temple_geometry")
removed = set()
placed = set()
route = [(344, 59, 281)]
mining = []
rays = {}
sys.path.insert(0, str(Path(__file__).parent))
paths = importlib.import_module("analyze_pilot").paths


def check(points):
    geometry.path_checks(c, removed, set(), set())[1](points, crouch_up=True)


def go(target):
    a = route[-1]
    if a == target:
        return
    h = abs(a[0] - target[0]) + abs(a[2] - target[2])
    assert h
    assert (a[0] == target[0]) != (a[2] == target[2])
    assert a[1] == target[1] or (h == 1 and abs(a[1] - target[1]) == 1)
    dx = (target[0] > a[0]) - (target[0] < a[0])
    dz = (target[2] > a[2]) - (target[2] < a[2])
    points = [a] + [(a[0] + i * dx, target[1], a[2] + i * dz) for i in range(1, h + 1)]
    check(points)
    route.extend(points[1:])


def ray(target, endpoint=None):
    x, y, z = route[-1]
    eye = (x + 0.5, y + 1.62, z + 0.5)
    end = endpoint or (target[0] + 0.5, target[1] + 0.999, target[2] + 0.5)
    geometry.ray_check(c, removed, rays)(eye, end, target)


def mine(target, expected, endpoint=None):
    assert at(original, *target)["Name"] == "minecraft:" + expected
    ray(target, endpoint)
    mining.append((target, expected))
    removed.add(target)


# Whole upper hall circuit, reusing the accepted flat-grid path finder.
upper_cells = set()
for x in range(337, 356):
    for z in range(273, 291):
        try:
            check([(x, 59, z)])
        except AssertionError:
            continue
        upper_cells.add((x, 59, z))
for target in [(339, 59, 273), (353, 59, 273), (351, 59, 287), (341, 59, 287), (344, 59, 281)]:
    segment = paths(upper_cells, route[-1])[target]
    check(segment)
    route.extend(segment[1:])
    if target[2] == 273:
        side = 338 if target[0] == 339 else 354
        outer = 337 if side == 338 else 355
        go((target[0], 59, 274))
        go((side, 60, 274))
        go((side, 61, 275))
        go((outer, 61, 275))
        go((side, 61, 275))
        go((side, 60, 274))
        go((target[0], 59, 274))
        go(target)
print("upper cells", len(upper_cells), "connected", len(paths(upper_cells, route[0])))
upper = list(route)
ring = [
    (345, 281),
    (345, 282),
    (345, 283),
    (346, 283),
    (347, 283),
    (347, 282),
    (347, 281),
    (346, 281),
]
for x, z in ring[1:]:
    mine((x, 58, z), "orange_terracotta" if x != 346 and z != 282 else "sandstone")
mine((346, 58, 282), "blue_terracotta")
go((345, 59, 281))
# Every placed cube is explicit hypothetical construction, not changed raw evidence.
for step in range(1, 22):
    x, z = ring[step % 8]
    y = 59 - step
    target = (x, y - 1, z)
    assert at(c, *target)["Name"] == "minecraft:air"
    if x == 345:
        wall = (344, y - 1, z)
        end = (344.999, y - 0.5, z + 0.5)
    elif x == 347:
        wall = (348, y - 1, z)
        end = (348.001, y - 0.5, z + 0.5)
    elif z == 281:
        wall = (x, y - 1, 280)
        end = (x + 0.5, y - 0.5, 280.999)
    else:
        wall = (x, y - 1, 284)
        end = (x + 0.5, y - 0.5, 284.001)
    name = at(c, *wall)["Name"]
    assert name in {
        "minecraft:cut_sandstone",
        "minecraft:chiseled_sandstone",
        "minecraft:sandstone",
        "minecraft:trapped_chest",
    }, (wall, name)
    if name == "minecraft:trapped_chest":
        end = (348 + 1 / 16 + 0.001, y - 0.5, z + 0.5)
    ray(wall, end)
    b = c["bounds"]
    index = (
        ((target[1] - b[1]) * (b[5] - b[2] + 1) + target[2] - b[2]) * (b[3] - b[0] + 1)
        + target[0]
        - b[0]
    )
    c["palette"].append({"Name": "minecraft:cobblestone"})
    c["blocks_yzx"][index] = len(c["palette"]) - 1
    placed.add(target)
    go((x, y, z))
go((347, 37, 281))
stairs = list(route[len(upper) :])
go((346, 37, 281))
mine((346, 37, 282), "stone_pressure_plate", (346.5, 37.062, 282.5))
mine((348, 37, 282), "trapped_chest", (348.5, 37.874, 282.5))
go((346, 37, 282))
for target in [(346, 37, 280), (346, 37, 284), (344, 37, 282)]:
    mine(target, "trapped_chest", (target[0] + 0.5, 37.874, target[2] + 0.5))
go((344, 37, 282))
mine((343, 37, 282), "cut_sandstone", (343.999, 37.5, 282.5))
mine((343, 38, 282), "chiseled_sandstone", (343.999, 38.5, 282.5))
go((330, 37, 282))
mine((329, 37, 282), "tripwire", (329.999, 37.1, 282.5))
go((326, 37, 282))
mine((325, 37, 282), "raw_gold_block", (325.999, 37.5, 282.5))
go((325, 37, 282))
mine((324, 38, 282), "yellow_candle", (324.5, 38.2, 282.5))
mine((324, 37, 282), "gold_block", (324.999, 37.5, 282.5))
go((324, 36, 282))
go((322, 36, 282))
mine((320, 36, 282), "spawner", (320.999, 36.5, 282.5))
source_station = route[-1]
chests = [(324, 36, 280), (324, 36, 284), (318, 36, 282)]
for target, station in zip(chests, [(321, 36, 280), (321, 36, 284), (319, 36, 282)], strict=True):
    go((station[0], 36, 282))
    if station[2] != 282:
        go(station)
    assert at(c, *target)["Name"] == "minecraft:chest"
    assert at(c, target[0], target[1] + 1, target[2])["Name"] == "minecraft:air"
    ray(target, (target[0] + 0.5, 36.874, target[2] + 0.5))
    if station[2] != 282:
        go((station[0], 36, 282))
# Return through every shared station without repeating mining or construction.
go((324, 36, 282))
go((325, 37, 282))
go((326, 37, 282))
go((344, 37, 282))
go((346, 37, 282))
go((346, 37, 281))
go((347, 37, 281))
for target in reversed(stairs[:-1]):
    go(target)
go((344, 59, 281))
geometry.path_checks(original, set(), set(), set())[1](upper)
check(route[len(upper) - 1 :])
print(
    "route",
    len(route) - 1,
    "horizontal",
    sum(abs(a[0] - b[0]) + abs(a[2] - b[2]) for a, b in pairwise(route)),
    "up",
    sum(max(0, b[1] - a[1]) for a, b in pairwise(route)),
    "down",
    sum(max(0, a[1] - b[1]) for a, b in pairwise(route)),
)
print("mining", mining)
print("placed", len(placed), "rays", len(rays), "source station", source_station)

# Complete task arithmetic, as predeclared in the family report.
deltas = [tuple(b[i] - a[i] for i in range(3)) for a, b in pairwise(route)]
turns = sum(a != b for a, b in pairwise(deltas))
vertical = sum(abs(d[1]) for d in deltas)
flat = len(deltas) - vertical
assert vertical == 54
assert flat == 148
work = {
    "sandstone": 3,
    "orange_terracotta": 5,
    "blue_terracotta": 5,
    "stone_pressure_plate": 2,
    "trapped_chest": 10,
    "cut_sandstone": 3,
    "chiseled_sandstone": 3,
    "tripwire": 0,
    "raw_gold_block": 19,
    "yellow_candle": 3,
    "gold_block": 12,
    "spawner": 19,
}
ticks = sum(work[name] for _, name in mining)
assert ticks == 133
assert len(mining) == 20
assert len(placed) == 21
print(
    "complete counts",
    {
        "flat": flat,
        "coupled_steps": vertical,
        "turns": turns,
        "decisions": turns + 8,
        "interactions": 44,
        "selections": 9,
        "acquisitions": 9,
        "active_mining_ticks": ticks,
        "checked_ray_events": sum(len(v) for v in rays.values()),
    },
)
for label, u, j, n, a, s, k, v, duty in [
    ("A", 5, 1, 0.5, 0.25, 0.25, 1, 2, 1),
    ("B", 4, 0.5, 1, 0.5, 0.5, 2, 4, 0.75),
    ("C", 3, 0.25, 1.5, 1, 1, 4, 8, 0.5),
]:
    movement = (flat + 24) / u + vertical * max(1 / u, 1 / j)
    total = movement + ticks / 20 + (turns + 8) * n + 44 * a + 9 * s + 9 * k + v + 15.6 / duty
    print(
        label,
        "movement including conditional pickup",
        movement,
        "combat",
        15.6 / duty,
        "complete",
        total,
    )

# Native failures stay explicit; constructed and pre-removal states are separate.
for label, points in [
    ("upper pillar", [(344, 59, 281), (344, 59, 280)]),
    ("west tower cap", [(338, 61, 275), (338, 62, 276)]),
    ("east tower cap", [(354, 61, 275), (354, 62, 276)]),
    ("shaft without construction", stairs),
]:
    try:
        geometry.path_checks(original, set(), set(), set())[1](points, crouch_up=True)
    except AssertionError as error:
        print("retained native rejection", label, str(error))
    else:
        raise AssertionError("expected native rejection did not occur: " + label)

# Independent external bypass into the western reward room, under the original state.
bypass_removed = {(321, 36, 286), (321, 37, 286)}
bypass = [(321, 36, 287), (321, 36, 286), (321, 36, 285)]
for target in sorted(bypass_removed):
    assert at(original, *target)["Name"] == "minecraft:cut_sandstone"
    geometry.ray_check(original, bypass_removed - {target}, {})(
        (321.5, 37.62, 287.5), (321.5, target[1] + 0.5, 286.999), target
    )
geometry.path_checks(original, bypass_removed, set(), set())[1](bypass)
geometry.ray_check(original, bypass_removed, {})(
    (321.5, 37.62, 285.5), (324.5, 36.874, 284.5), (324, 36, 284)
)
print("external bypass", bypass, "two sandstone removals; chest access, not combat avoidance")
for target in [(339, 59, 273), (353, 59, 273)]:
    print("upper graph branch distance", target, len(paths(upper_cells, route[0])[target]) - 1)
