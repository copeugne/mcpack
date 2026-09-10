"""Check the declared ordinary modular-fortress route and conditional task."""

# pyright: standard
# ruff: noqa: INP001, S101, ANN001, ANN201, D103, T201, PLR2004, PT018
import gzip
import hashlib
import importlib
import json
import math
from collections import deque
from itertools import pairwise
from pathlib import Path

raw = (
    Path(__file__).parent / "fixed-blocks/adorabuild-nether-fortress-ordinary-r2.json.gz"
).read_bytes()
assert (
    hashlib.sha256(raw).hexdigest()
    == "f4f27779a3d28a151c963a9e3c84f5ca1ae6373cad044d6b922f410018fcb0bd"
)
c = json.loads(gzip.decompress(raw))["cases"][0]
at = importlib.import_module("evidence.item-13.render_pilot").state_at
overlap = importlib.import_module("evidence.item-13.collision.clearance").overlaps
removed = set()


def shape(x, y, z):
    if (x, y, z) in removed:
        return None
    s = at(c, x, y, z)
    n = s["Name"]
    if n in {"minecraft:air", "minecraft:cave_air"}:
        return None
    if n == "minecraft:nether_brick_slab":
        assert s["Properties"]["type"] == "top"
        b = [0, 0.5, 0, 1, 1, 1]
    elif n == "minecraft:soul_sand":
        b = [0, 0, 0, 1, 14 / 16, 1]
    elif n == "minecraft:chest":
        assert s["Properties"]["type"] == "single"
        b = [1 / 16, 0, 1 / 16, 15 / 16, 14 / 16, 15 / 16]
    elif n in {"minecraft:nether_brick_wall", "minecraft:nether_brick_fence"}:
        b = [0, 0, 0, 1, 1.5, 1]  # Conservative whole-cell avoidance, including upward extension.
    elif n in {
        "minecraft:nether_bricks",
        "minecraft:nether_brick_stairs",
        "minecraft:lava",
        "minecraft:basalt",
        "minecraft:netherrack",
        "minecraft:nether_gold_ore",
        "minecraft:nether_quartz_ore",
        "minecraft:gravel",
        "minecraft:soul_soil",
        "minecraft:crimson_nylium",
        "minecraft:crimson_roots",
        "minecraft:magma_block",
    }:
        b = [0, 0, 0, 1, 1, 1]  # Partial/trigger cells are excluded, never used as route support.
    else:
        raise ValueError(n)
    return [b[i] + (x, y, z)[i % 3] for i in range(6)]


def clear(box):
    for x in range(math.floor(box[0]), math.ceil(box[3])):
        for y in range(math.floor(box[1]) - 1, math.ceil(box[4])):
            for z in range(math.floor(box[2]), math.ceil(box[5])):
                b = shape(x, y, z)
                assert b is None or not overlap(box, b), (box, (x, y, z), at(c, x, y, z))


route = [(-254, 33, -120)]
crouches = []


def go(targets, *, crouch=False):
    for b in targets:
        a = route[-1]
        if a == b:
            continue
        horizontal = abs(b[0] - a[0]) + abs(b[2] - a[2])
        assert (a[0] == b[0]) != (a[2] == b[2])
        assert b[1] == a[1] or (horizontal == 1 and abs(b[1] - a[1]) == 1)
        dx = (b[0] > a[0]) - (b[0] < a[0])
        dz = (b[2] > a[2]) - (b[2] < a[2])
        for i in range(1, horizontal + 1):
            route.append((a[0] + i * dx, b[1], a[2] + i * dz))
            crouches.append(crouch)


small1 = [(-254, 33, -119), (-253, 34, -119), (-253, 35, -120), (-253, 36, -121), (-254, 37, -121)]
small2 = [(-254, 33, -131), (-255, 34, -131), (-255, 35, -130), (-255, 36, -129), (-254, 37, -129)]


def medium(y):
    return [
        (-263, y, -110),
        (-263, y + 1, -111),
        (-264, y + 2, -111),
        (-265, y + 3, -111),
        (-265, y + 4, -110),
    ]


go([small1[0]])
go(small1[1:], crouch=True)
go([(-254, 37, -120), (-254, 37, -130), small2[-1]])
go(list(reversed(small2))[1:])
go([(-254, 33, -130), small2[0]])
go(small2[1:], crouch=True)
go([(-254, 37, -110), (-264, 37, -110), medium(33)[-1]])
go(list(reversed(medium(33)))[1:])
go([(-263, 33, -109), medium(33)[0]])
go(medium(33)[1:], crouch=True)
go([medium(37)[0]])
go(medium(37)[1:], crouch=True)
go([(-263, 41, -110), (-263, 41, -109), medium(41)[0]])
go(medium(41)[1:], crouch=True)
go(list(reversed(medium(41)))[1:])
go([medium(37)[-1]])
go(list(reversed(medium(37)))[1:])
go([(-264, 37, -110), (-254, 37, -110), small1[-1]])
go(list(reversed(small1))[1:])
go([route[0]])

for x, y, z in route:
    state = at(c, x, y - 1, z)
    assert state["Name"] in {"minecraft:nether_bricks", "minecraft:nether_brick_slab"}
    b = shape(x, y - 1, z)
    assert b is not None and b[4] == y
    clear([x + 0.2, y, z + 0.2, x + 0.8, y + 1.8, z + 0.8])
for (a, b), crouch in zip(pairwise(route), crouches, strict=True):
    height = 1.5 if crouch else 1.8
    high = max(a[1], b[1])
    apex = high + 0.3 if b[1] > a[1] else high
    clear(
        [
            min(a[0], b[0]) + 0.2,
            apex,
            min(a[2], b[2]) + 0.2,
            max(a[0], b[0]) + 0.8,
            apex + height,
            max(a[2], b[2]) + 0.8,
        ]
    )
    for p in (a, b):
        clear([p[0] + 0.2, p[1], p[2] + 0.2, p[0] + 0.8, apex + height, p[2] + 0.8])

for eye, target, chest in (
    ([-253.5, 34.62, -129.5], [-252.9375, 33.5, -129.5], (-253, 33, -130)),
    ([-262.5, 34.62, -108.5], [-263.0625, 33.5, -108.5], (-264, 33, -109)),
    ([-262.5, 42.62, -108.5], [-263.0625, 41.5, -108.5], (-264, 41, -109)),
):
    assert math.dist(eye, target) < 4.5
    assert at(c, *chest)["Name"] == "minecraft:chest"
    assert at(c, chest[0], chest[1] + 1, chest[2])["Name"] == "minecraft:air"
    clear([min(eye[i], target[i]) for i in range(3)] + [max(eye[i], target[i]) for i in range(3)])
for x in (-264, -265):
    assert at(c, x, 32, -110)["Name"] == "minecraft:nether_bricks"
    clear([x + 0.2, 33, -109.8, x + 0.8, 34.8, -109.2])
    assert math.dist((-262.5, 33, -108.5), (x + 0.5, 33, -109.5)) <= 3
    clear([x + 0.5, 34.4, -109.5, -262.5, 34.41, -108.5])

horizontal = len(route) - 1
crouched = sum(crouches)
vertical = sum(abs(b[1] - a[1]) for a, b in pairwise(route))
jumps = sum(b[1] > a[1] for a, b in pairwise(route))
directions = [(b[0] - a[0], b[2] - a[2]) for a, b in pairwise(route)]
turns = sum(a != b for a, b in pairwise(directions))
assert sum(a != b for a, b in pairwise([False, *crouches, False])) == 10
print(
    json.dumps(
        {
            "horizontal": horizontal,
            "crouched_horizontal": crouched,
            "support_elevation_travel": vertical,
            "upward_jumps": jumps,
            "heading_changes": turns,
            "feet_span": [min(p[1] for p in route), max(p[1] for p in route)],
        },
        indent=2,
    )
)
for u, cu, j, n, a, s, k, v, duty in (
    (5, 1.5, 1, 0.5, 0.25, 0.25, 1, 2, 1),
    (4, 1.2, 0.5, 1, 0.5, 0.5, 2, 4, 0.75),
    (3, 0.9, 0.25, 1.5, 1, 1, 4, 8, 0.5),
):
    base = (
        (horizontal - crouched) / u
        + crouched / cu
        + vertical / j
        + (15 + jumps + turns) * n
        + 13 * a
        + s
        + 3 * k
        + v
    )
    print(json.dumps({"no_enemy_seconds": base, "two_blaze_seconds": base + 2 * n + 5.2 / duty}))

adjacency = {}
for a, b in pairwise(route):
    adjacency.setdefault(a, set()).add(b)
    adjacency.setdefault(b, set()).add(a)
distance = {route[0]: 0}
pending = deque([route[0]])
while pending:
    node = pending.popleft()
    for neighbor in adjacency[node]:
        if neighbor not in distance:
            distance[neighbor] = distance[node] + 1
            pending.append(neighbor)
print(
    json.dumps(
        {
            "shortest_checked_network_horizontal": {
                name: distance[p]
                for name, p in {
                    "small2_chest": (-254, 33, -130),
                    "medium_lower_chest": (-263, 33, -109),
                    "medium_upper_chest": (-263, 41, -109),
                    "medium_upper_terrace": (-265, 45, -110),
                }.items()
            }
        },
        indent=2,
    )
)

for foot, target, window, mining_target in (
    ([-250.5, 32, -129.5], [-252.0625, 33.5, -129.5], (-252, 33, -130), [-251, 33.75, -129.5]),
    ([-263.5, 31.875, -106.5], [-263.5, 33.5, -108.0625], (-264, 33, -108), [-263.5, 33.75, -107]),
):
    assert at(c, *window)["Name"] == "minecraft:nether_brick_stairs"
    floor = shape(math.floor(foot[0]), 31, math.floor(foot[2]))
    assert floor is not None and floor[4] == foot[1]
    clear([foot[0] - 0.3, foot[1], foot[2] - 0.3, foot[0] + 0.3, foot[1] + 1.8, foot[2] + 0.3])
    eye = [foot[0], foot[1] + 1.62, foot[2]]
    assert math.dist(eye, mining_target) < 4.5
    clear(
        [min(eye[i], mining_target[i]) for i in range(3)]
        + [max(eye[i], mining_target[i]) for i in range(3)]
    )
    removed.add(window)
    assert math.dist(eye, target) < 4.5
    clear([min(eye[i], target[i]) for i in range(3)] + [max(eye[i], target[i]) for i in range(3)])
print("Both independent ground-window chest accesses pass after one stair removal each")
