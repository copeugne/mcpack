"""Reproduce the two declared Basalt routes from immutable saved blocks.

This is a conditional static check, not an actor simulation or observed timing.
"""

# pyright: standard
# ruff: noqa: INP001, S101, ANN001, ANN201, D103, T201, PLR2004, PT018
import gzip
import hashlib
import importlib
import json
import math
import sys
from collections import deque
from itertools import pairwise
from pathlib import Path

assert len(sys.argv) == 2 and sys.argv[1] in {"first", "second"}
second = sys.argv[1] == "second"
name = "ordinary" if second else "biome-diverse"
r = (Path(__file__).parent / f"fixed-blocks/basalt-chambers-{name}-r2.json.gz").read_bytes()
expected = (
    "f77a6dc8a1d956d0d6c0c45b5efe80e6554709b50a2152da601b2265394ed803"
    if second
    else "c51074175f8e721caad92936f701a8d8259f940804378931ef7cbd36dddaf2c0"
)
assert hashlib.sha256(r).hexdigest() == expected
c = json.loads(gzip.decompress(r))["cases"][0]
at = importlib.import_module("evidence.item-13.render_pilot").state_at
overlap = importlib.import_module("evidence.item-13.collision.clearance").overlaps
barriers = (
    ((156, -148), (142, -148), (128, -148), (156, -120))
    if second
    else ((4, -500), (10, -492), (4, -486))
)
removed = {(x, y, z) for x, z in barriers for y in (14, 15)}
assert all(at(c, *p)["Name"] == "minecraft:polished_basalt" for p in removed)
barrier_removals = sorted(removed)
placed = set()
full = {
    "polished_basalt",
    "smooth_basalt",
    "basalt",
    "blackstone",
    "netherrack",
    "crying_obsidian",
    "ancient_debris",
    "spawner",
    "tnt",
    "nether_gold_ore",
    "nether_quartz_ore",
}


def shape(x, y, z):
    if (x, y, z) in placed:
        return [x, y, z, x + 1, y + 1, z + 1]
    if (x, y, z) in removed:
        return None
    state = at(c, x, y, z)
    name = state["Name"].split(":")[1]
    if name == "air":
        return None
    if name == "chain":
        a = [6.5 / 16] * 3 + [9.5 / 16] * 3
        axis = "xyz".index(state["Properties"]["axis"])
        a[axis] = 0
        a[axis + 3] = 1
    elif name in full or name in {"lava", "tripwire", "tripwire_hook"}:
        a = [0, 0, 0, 1, 1, 1]  # fluids/triggers excluded conservatively, not collision claims
    else:
        raise ValueError(name)
    return [a[i] + (x, y, z)[i % 3] for i in range(6)]


def clear(box):
    for x in range(math.floor(box[0]), math.ceil(box[3])):
        for y in range(math.floor(box[1]), math.ceil(box[4])):
            for z in range(math.floor(box[2]), math.ceil(box[5])):
                b = shape(x, y, z)
                assert b is None or not overlap(box, b), (box, (x, y, z), at(c, x, y, z))


def point(x, z):
    floor = next((b for y in (13, 12, 11) if (b := shape(x, y, z)) is not None), None)
    assert floor is not None
    y = floor[4]
    assert (x, math.floor(y - 1e-8), z) in placed or at(c, x, math.floor(y - 1e-8), z)[
        "Name"
    ].split(":")[1] in full | {"chain"}, (x, z, y, at(c, x, math.floor(y - 1e-8), z))
    assert floor[0] <= x + 0.5 <= floor[3] and floor[2] <= z + 0.5 <= floor[5]
    p = (x + 0.5, y, z + 0.5)
    clear([p[0] - 0.3, y, p[2] - 0.3, p[0] + 0.3, y + 1.8, p[2] + 0.3])
    return p


ab = [(-1, -500), (9, -500), (9, -497), (10, -497), (10, -487)]
east = [(10, -487), (13, -487), (13, -486), (23, -486)]
west = [(10, -487), (9, -487), (9, -486), (-1, -486)]
a_pick = [(-1, -500), (-1, -499), (-2, -499), (-1, -499), (-1, -500)]
c_pick = [(-1, -486), (-1, -485), (-2, -485), (-1, -485), (-1, -486)]
waypoints = (
    a_pick
    + ab[1:]
    + east[1:]
    + list(reversed(east))[1:]
    + west[1:]
    + c_pick[1:]
    + list(reversed(west))[1:]
    + list(reversed(ab))[1:]
)
if second:
    waypoints = [
        (159, -140),
        (159, -139),
        (155, -139),
        (155, -140),
        (145, -140),
        (145, -143),
        (142, -143),
        (142, -153),
        (142, -154),
        (145, -154),
        (145, -155),
        (144, -155),
        (145, -155),
        (145, -154),
        (142, -154),
        (142, -153),
        (142, -143),
        (141, -143),
        (141, -140),
        (131, -140),
        (131, -143),
        (128, -143),
        (128, -153),
        (128, -143),
        (127, -143),
        (127, -140),
        (117, -140),
        (127, -140),
        (127, -139),
        (128, -139),
        (128, -129),
        (128, -139),
        (131, -139),
        (131, -140),
        (141, -140),
        (141, -139),
        (145, -139),
        (145, -140),
        (155, -140),
        (155, -139),
        (159, -139),
        (159, -140),
        (159, -141),
        (158, -141),
        (159, -141),
        (159, -140),
        (159, -143),
        (156, -143),
        (156, -153),
        (156, -154),
        (159, -154),
        (159, -155),
        (158, -155),
        (159, -155),
        (159, -154),
        (156, -154),
        (156, -153),
        (156, -143),
        (155, -143),
        (155, -139),
        (156, -139),
        (156, -129),
        (155, -129),
        (155, -125),
        (156, -125),
        (156, -115),
        (155, -115),
        (155, -111),
        (156, -111),
        (156, -101),
        (156, -111),
        (155, -111),
        (155, -112),
        (145, -112),
        (155, -112),
        (155, -115),
        (156, -115),
        (156, -125),
        (155, -125),
        (155, -129),
        (156, -129),
        (156, -139),
        (159, -139),
        (159, -140),
    ]

    def intersects(eye, target, box):
        """Closed segment/slab hit; contacts before the intended endpoint obstruct."""
        low, high = 0.0, 1.0
        for i in range(3):
            delta = target[i] - eye[i]
            if delta == 0:
                if not box[i] <= eye[i] <= box[i + 3]:
                    return False
            else:
                a, b = sorted(((box[i] - eye[i]) / delta, (box[i + 3] - eye[i]) / delta))
                low, high = max(low, a), min(high, b)
                if low > high:
                    return False
        return low < 1 - 1e-9 and high >= 0

    # Check each cut before declaring that string removed. Other strings are
    # conservatively excluded as cubes; the intended target uses its source outline.
    for x in (142, 156):
        eye = [x + 0.5, 15.62, -151.5]
        clear([x + 0.2, 14, -151.8, x + 0.8, 15.8, -151.2])
        for y in (14, 13):
            pos = (x, y, -153)
            state = at(c, *pos)
            assert state["Name"] == "minecraft:tripwire"
            assert state["Properties"]["attached"] == "true"
            assert state["Properties"]["disarmed"] == "false"
            target = [x + 0.5, y + 0.1, -152.5]
            assert math.dist(eye, target) < 4.5
            assert intersects(eye, target, [x, y + 1 / 16, -153, x + 1, y + 2.5 / 16, -152])
            for xx in range(x - 1, x + 2):
                for yy in range(y, 16):
                    for zz in range(-153, -150):
                        box = shape(xx, yy, zz)
                        assert (
                            (xx, yy, zz) == pos or box is None or not intersects(eye, target, box)
                        ), (pos, (xx, yy, zz))
            removed.add(pos)
    print("Four ordered shear rays clear before each declared removal")
    assert at(c, 157, 12, -154)["Properties"]["axis"] == "z"
    assert at(c, 157, 12, -154)["Name"] == "minecraft:chain"
    assert at(c, 159, 12, -154)["Name"] == "minecraft:polished_basalt"
    for x, eye, target in (
        (156, [156.5, 14.62, -152.5], [157.40625, 12.5, -153.5]),
        (158, [156.5, 14.62, -153.5], [159, 12.5, -153.5]),
    ):
        assert at(c, x, 12, -154)["Name"] == "minecraft:air"
        assert math.dist(eye, target) < 4.5
        for xx in range(156, 160):
            for yy in range(12, 15):
                for zz in range(-154, -151):
                    box = shape(xx, yy, zz)
                    assert box is None or not intersects(eye, target, box), (
                        "placement",
                        x,
                        (xx, yy, zz),
                    )
        placed.add((x, 12, -154))
    print("Two support-placement rays clear in order; targets are saved air")
columns = [waypoints[0]]
for a, b in pairwise(waypoints):
    assert (a[0] == b[0]) != (a[1] == b[1])
    dx = (b[0] > a[0]) - (b[0] < a[0])
    dz = (b[1] > a[1]) - (b[1] < a[1])
    columns += [
        (a[0] + i * dx, a[1] + i * dz) for i in range(1, abs(b[0] - a[0]) + abs(b[1] - a[1]) + 1)
    ]
points = [point(*p) for p in columns]
vertical = 0
for a, b in pairwise(points):
    high = max(a[1], b[1])
    low = min(a[1], b[1])
    vertical += high - low
    assert high - low <= 1
    # One-block rises require a jump. Reserve0.3 head clearance above the upper support.
    apex = high + 0.3 if b[1] - a[1] > 0.6 else high
    clear(
        [
            min(a[0], b[0]) - 0.3,
            apex,
            min(a[2], b[2]) - 0.3,
            max(a[0], b[0]) + 0.3,
            apex + 1.8,
            max(a[2], b[2]) + 0.3,
        ]
    )
    for p in (a, b):
        clear([p[0] - 0.3, p[1], p[2] - 0.3, p[0] + 0.3, apex + 1.8, p[2] + 0.3])
directions = [(b[0] - a[0], b[1] - a[1]) for a, b in pairwise(columns)]
turns = sum(a != b for a, b in pairwise(directions))
print(
    json.dumps(
        {
            "horizontal_blocks": len(columns) - 1,
            "support_elevation_travel": vertical,
            "heading_changes": turns,
            "feet_span": [min(p[1] for p in points), max(p[1] for p in points)],
            "barrier_removals": barrier_removals,
        },
        indent=2,
    )
)

rays = (
    ([-0.5, 14.62, -499.5], [-2, 15.25, -498.5]),
    ([-0.5, 14.62, -485.5], [-2, 15.25, -484.5]),
    ([23.5, 14.62, -485.5], [25, 15.25, -484.5]),
    ([-0.5, 14.62, -499.5], [-2.40625, 14.5, -498.5]),
    ([-0.5, 14.62, -485.5], [-2.40625, 14.5, -484.5]),
)
chains = [(-3, 14, -499), (-3, 14, -485)]
if second:
    rays = [
        ([145.5, 14.62, -139.5], [144, 15.25, -140.5]),
        ([156.5, 14.62, -100.5], [157.5, 15.25, -99]),
    ]
    chains = [(157, 14, -141), (143, 14, -155), (157, 14, -155)]
    for x, _, z in chains:
        rays.extend(
            [
                ([x + 2.5, 14.62, z + 1.5], [x + 1, 15.25, z + 0.5]),
                ([x + 2.5, 14.62, z + 1.5], [x + 0.59375, 14.5, z + 0.5]),
            ]
        )
for eye, target in rays:
    assert math.dist(eye, target) < 4.5
    clear([min(eye[i], target[i]) for i in range(3)] + [max(eye[i], target[i]) for i in range(3)])
for p in chains:
    assert at(c, *p) == {
        "Name": "minecraft:chain",
        "Properties": {"axis": "y", "waterlogged": "false"},
    }
print(f"{len(rays)} conservative interaction-ray bounds clear; all support chains match")
if second:
    for actor, targets in (
        ((145.5, 13, -139.5), ((145.5, 13, -138.5), (145.5, 13, -141.5))),
        ((156.5, 13, -100.5), ((155.5, 13, -100.5), (159.5, 13, -100.5))),
    ):
        for target in targets:
            assert math.dist(actor, target) <= 3
            assert point(math.floor(target[0]), math.floor(target[2])) == target
            clear(
                [
                    min(actor[0], target[0]),
                    14,
                    min(actor[2], target[2]),
                    max(actor[0], target[0]) + 0.001,
                    14.01,
                    max(actor[2], target[2]) + 0.001,
                ]
            )
    print("Four stipulated melee stations have support and clear height-14 lines")
    adjacency = {}
    for a, b in pairwise(columns):
        adjacency.setdefault(a, set()).add(b)
        adjacency.setdefault(b, set()).add(a)
    distance = {columns[0]: 0}
    pending = deque([columns[0]])
    while pending:
        for neighbor in adjacency[node := pending.popleft()]:
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                pending.append(neighbor)
    print(
        json.dumps(
            {
                "shortest_checked_network_station_blocks": {
                    label: distance[station]
                    for label, station in {
                        "central_reward": (159, -140),
                        "west_source": (145, -140),
                        "west_trap_reward": (145, -154),
                        "east_trap_reward": (159, -154),
                        "south_source": (156, -101),
                        "west_empty": (117, -140),
                        "northwest_empty": (128, -153),
                        "southwest_empty": (128, -129),
                        "lower_west_empty": (145, -112),
                    }.items()
                }
            },
            indent=2,
        )
    )
    for u, j, n, a, s, k, v, duty in (
        (5, 1, 0.5, 0.25, 0.25, 1, 2, 1),
        (4, 0.5, 1, 0.5, 0.5, 2, 4, 0.75),
        (3, 0.25, 1.5, 1, 1, 4, 8, 0.5),
    ):
        base = (
            (len(columns) - 1) / u
            + vertical / j
            + 23.7
            + (40 + turns) * n
            + 22 * a
            + 11 * s
            + 3 * k
            + v
        )
        print(
            json.dumps(
                {
                    "no_enemy_seconds": base,
                    "four_blaze_seconds": base + 4 * n + 10.4 / duty,
                    "source_window_seconds": 15 / u + 2 / j + 6 * n + 0.95 + a,
                }
            )
        )
