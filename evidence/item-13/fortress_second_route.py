"""Validate the second preselected fortress task against its own saved geometry."""

# pyright: standard
# ruff: noqa: INP001, S101, ANN001, ANN201, D103, T201, PLR2004
import argparse
import gzip
import hashlib
import importlib
import json
import math
from itertools import pairwise
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "--native", action="store_true", help="Reproduce rejection without the declared removals"
)
args = parser.parse_args()

m = importlib.import_module("evidence.item-13.fortress_route")
raw = (
    Path(__file__).parent / "fixed-blocks/adorabuild-nether-fortress-biome-diverse-r1.json.gz"
).read_bytes()
assert (
    hashlib.sha256(raw).hexdigest()
    == "099575deb8e07624b33c4e8e98a5f4d8d9848eb90c8ac19cbfc7f717e15adef8"
)
vars(m)["c"] = json.loads(gzip.decompress(raw))["cases"][0]
m.route[:] = [(-14, 33, 408)]
m.crouches[:] = []
go = m.go


def gap(target):
    a = m.route[-1]
    assert a[1] == target[1]
    assert abs(a[0] - target[0]) + abs(a[2] - target[2]) == 2
    m.route.append(target)
    m.crouches.append(False)


def medium(x, z, y):
    return [
        (x - 1, y, z),
        (x - 1, y + 1, z + 1),
        (x, y + 2, z + 1),
        (x + 1, y + 3, z + 1),
        (x + 1, y + 4, z),
    ]


def visit_medium(x, z):
    go([medium(x, z, 33)[-1]])
    go(list(reversed(medium(x, z, 33)))[1:])
    go([(x - 1, 33, z - 1), medium(x, z, 33)[0]])
    go(medium(x, z, 33)[1:], crouch=True)
    go([(x, 37, z), medium(x, z, 37)[0]])
    go(medium(x, z, 37)[1:], crouch=True)
    go([(x, 41, z), medium(x, z, 41)[0]])
    go(medium(x, z, 41)[1:], crouch=True)
    go(list(reversed(medium(x, z, 41)))[1:])
    go([(x, 41, z), medium(x, z, 37)[-1]])
    go(list(reversed(medium(x, z, 37)))[1:])
    go([(x, 37, z)])


small = [(-2, 33, 409), (-1, 34, 409), (-1, 35, 408), (-1, 36, 407), (-2, 37, 407)]
go([(-13, 34, 408)], crouch=True)
go([(-12, 35, 408), (-11, 36, 408), (-10, 37, 408), (-2, 37, 408), small[-1]])
go(list(reversed(small))[1:])
go([(-2, 33, 408), small[0]])
go(small[1:], crouch=True)
go([(-2, 37, 398), (-2, 37, 408)])
gap((0, 37, 408))
go([(8, 37, 408)])
visit_medium(8, 408)
go([(18, 37, 408)])
visit_medium(18, 408)
go([(0, 37, 408)])
gap((-2, 37, 408))
go([(-2, 37, 418), medium(-2, 418, 33)[-1]])
go(list(reversed(medium(-2, 418, 33)))[1:])
go([(-2, 33, 418), medium(-2, 418, 33)[0]])
go(medium(-2, 418, 33)[1:], crouch=True)
go([(-2, 37, 418), (8, 37, 418)])
visit_medium(8, 418)
go([(-2, 37, 418)])
gap((-2, 37, 420))
go([(-2, 37, 428)])


def end_flight(y):
    return [(-2, y, 427), (-3, y + 1, 427), (-3, y + 2, 428), (-3, y + 3, 429), (-2, y + 4, 429)]


go([end_flight(33)[-1]])
go(list(reversed(end_flight(33)))[1:])
go([(-2, 33, 428), end_flight(33)[0]])
go(end_flight(33)[1:], crouch=True)
go([(-2, 37, 428), end_flight(37)[0]])
go(end_flight(37)[1:], crouch=True)
go([(-2, 41, 428), end_flight(41)[0]])
go(end_flight(41)[1:], crouch=True)
go(list(reversed(end_flight(41)))[1:])
go([(-2, 41, 428), end_flight(37)[-1]])
go(list(reversed(end_flight(37)))[1:])
go([(-2, 37, 428), (-2, 37, 420)])
gap((-2, 37, 418))
go([(-2, 37, 408), (-10, 37, 408), (-11, 36, 408), (-12, 35, 408), (-13, 34, 408), m.route[0]])
if args.native:
    m.check_route()
    message = "Native-route rejection unexpectedly absent"
    raise ValueError(message)

removals = {
    (-2, 33, 409),
    (-2, 34, 409),
    (8, 37, 418),
    (8, 38, 418),
    (8, 39, 419),
    (9, 40, 419),
    (9, 41, 419),
    (9, 42, 418),
    (9, 42, 419),
    (9, 44, 419),
    (8, 42, 407),
}
original_route = m.route[:]
original_crouches = m.crouches[:]
mining = []
for index, (a, b) in enumerate(pairwise(original_route)):
    m.clear([a[0] + 0.2, a[1], a[2] + 0.2, a[0] + 0.8, a[1] + 1.8, a[2] + 0.8])
    eye = [a[0] + 0.5, a[1] + (1.27 if original_crouches[index] else 1.62), a[2] + 0.5]
    changed = True
    while changed:
        changed = False
        for cell in sorted(removals - m.removed):
            assert m.at(m.c, *cell)["Name"] == "minecraft:nether_wart_block"
            for axis in range(3):
                for side in (0, 1):
                    target = [cell[0] + 0.5, cell[1] + 0.5, cell[2] + 0.5]
                    target[axis] = cell[axis] + side
                    if (side == 0 and eye[axis] >= target[axis]) or (
                        side == 1 and eye[axis] <= target[axis]
                    ):
                        continue
                    if math.dist(eye, target) > 4.5:
                        continue
                    try:
                        m.clear(
                            [min(eye[i], target[i]) for i in range(3)]
                            + [max(eye[i], target[i]) for i in range(3)]
                        )
                    except AssertionError:
                        continue
                    m.removed.add(cell)
                    mining.append(
                        {"route_index": index, "station": a, "block": cell, "face": target}
                    )
                    changed = True
                    break
                if cell in m.removed:
                    break
    m.route[:] = [a, b]
    m.crouches[:] = [original_crouches[index]]
    m.check_route()
assert m.removed == removals, removals - m.removed
m.route[:] = original_route
m.crouches[:] = original_crouches
m.check_route()
print(json.dumps({"mining_sequence": mining}, indent=2))
print("Second route support, chronological mining access and sweeps pass")

for station, chest in (
    ((7, 33, 407), (8, 33, 407)),
    ((8, 41, 408), (8, 41, 407)),
    ((18, 41, 408), (18, 41, 407)),
    ((8, 41, 418), (8, 41, 417)),
    ((-2, 41, 428), (-1, 41, 428)),
):
    assert station in m.route
    assert m.at(m.c, *chest)["Name"] == "minecraft:chest"
    assert (chest[0], chest[1] + 1, chest[2]) in m.removed or m.at(
        m.c, chest[0], chest[1] + 1, chest[2]
    )["Name"] == "minecraft:air"
    eye = [station[0] + 0.5, station[1] + 1.62, station[2] + 0.5]
    target = [chest[0] + 0.5, chest[1] + 0.5, chest[2] + 0.5]
    if station[0] != chest[0]:
        target[0] = chest[0] + (1 / 16 if station[0] < chest[0] else 15 / 16)
    else:
        target[2] = chest[2] + (1 / 16 if station[2] < chest[2] else 15 / 16)
    assert math.dist(eye, target) < 4.5
    m.clear([min(eye[i], target[i]) for i in range(3)] + [max(eye[i], target[i]) for i in range(3)])
for x in (8, 9):
    assert m.at(m.c, x, 32, 408)["Name"] == "minecraft:nether_bricks"
    m.clear([x + 0.2, 33, 408.2, x + 0.8, 34.8, 408.8])
    assert math.dist((7.5, 33, 407.5), (x + 0.5, 33, 408.5)) <= 3
    m.clear([7.5, 34.4, 407.5, x + 0.5, 34.41, 408.5])
print("Five chest stations/lids and two stipulated melee positions pass")

horizontal = sum(abs(b[0] - a[0]) + abs(b[2] - a[2]) for a, b in pairwise(m.route))
crouched = sum(m.crouches)
vertical = sum(abs(b[1] - a[1]) for a, b in pairwise(m.route))
upward = sum(b[1] > a[1] for a, b in pairwise(m.route))
gaps = sum(abs(b[0] - a[0]) + abs(b[2] - a[2]) == 2 for a, b in pairwise(m.route))
directions = [
    ((b[0] > a[0]) - (b[0] < a[0]), (b[2] > a[2]) - (b[2] < a[2])) for a, b in pairwise(m.route)
]
turns = sum(a != b for a, b in pairwise(directions))
toggles = sum(a != b for a, b in pairwise([False, *m.crouches, False]))
print(
    json.dumps(
        {
            "horizontal": horizontal,
            "crouched": crouched,
            "vertical": vertical,
            "upward": upward,
            "gaps": gaps,
            "turns": turns,
            "toggles": toggles,
        }
    )
)

for u, cu, j, n, a, s, k, v, duty in (
    (5, 1.5, 1, 0.5, 0.25, 0.25, 1, 2, 1),
    (4, 1.2, 0.5, 1, 0.5, 0.5, 2, 4, 0.75),
    (3, 0.9, 0.25, 1.5, 1, 1, 4, 8, 0.5),
):
    base = (
        (horizontal - crouched - 2 * gaps) / u
        + crouched / cu
        + vertical / j
        + gaps * max(2 / u, 1 / j)
        + 16.5
        + (44 + upward + gaps + turns) * n
        + (16 + toggles) * a
        + 3 * s
        + 5 * k
        + v
    )
    print(json.dumps({"no_enemy_seconds": base, "two_blaze_seconds": base + 2 * n + 5.2 / duty}))

m.removed.clear()
assert m.at(m.c, 8, 31, 405)["Name"] == "minecraft:crimson_nylium"
assert m.at(m.c, 8, 33, 406) == {
    "Name": "minecraft:nether_brick_stairs",
    "Properties": {"facing": "south", "half": "top", "shape": "straight", "waterlogged": "false"},
}
m.clear([8.2, 32, 405.2, 8.8, 33.8, 405.8])
eye = [8.5, 33.62, 405.5]
for target in ([8.5, 33.75, 406], [8.5, 33.5, 407.0625]):
    assert math.dist(eye, target) < 4.5
    m.clear([min(eye[i], target[i]) for i in range(3)] + [max(eye[i], target[i]) for i in range(3)])
    m.removed.add((8, 33, 406))
print("Independent lower chest exterior access passes after one window-stair removal")
