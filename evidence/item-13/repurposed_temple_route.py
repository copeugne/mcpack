"""Check ordered whole-temple operations against the five retained alternatives."""

# pyright: standard
# ruff: noqa: INP001, S101, T201, PLR2004
import argparse
import copy
import gzip
import hashlib
import importlib
import json
import sys
from itertools import pairwise
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("variant", choices=["basalt", "crimson"])
args = parser.parse_args()
raw = (
    Path(__file__).parent / f"fixed-blocks/repurposed-temple-{args.variant}.json.gz"
).read_bytes()
hashes = {
    "basalt": "a6884f33bf59e7a2a6be7e01df478ee5339b47ca7c258d5bf85400b78c1c8341",
    "crimson": "4d7415d4c2bfefd2ffc5d588d78d09481f5342c02d1765dd9dd7155c7d085724",
}
assert hashlib.sha256(raw).hexdigest() == hashes[args.variant]
c = json.loads(gzip.decompress(raw))["cases"][0]
original = copy.deepcopy(c)
at = importlib.import_module("evidence.item-13.render_pilot").state_at
geometry = importlib.import_module("evidence.item-13.temple_geometry")
removed = set()
rays = {}
_, verify = geometry.path_checks(c, removed, set(), set())
ray = geometry.ray_check(c, removed, rays)
route = [(399, 61, 318)]
# Full middle/upper survey, then source closet, then lower trap/reward branch.
# Mining targets are actual saved cells; no native failure is relabeled a route.
operations = [
    ("go", (398, 61, 318)),
    ("go", (398, 61, 320)),
    ("go", (398, 62, 321)),
    ("go", (398, 63, 322)),
    ("go", (398, 64, 323)),
    ("go", (397, 64, 323)),
    ("go", (397, 64, 317)),
    ("go", (402, 64, 317)),
    ("go", (402, 64, 323)),
    ("go", (398, 64, 323)),
    ("go", (398, 63, 322)),
    ("go", (398, 62, 321)),
    ("go", (398, 61, 320)),
    ("go", (397, 61, 320)),
    ("go", (398, 61, 320)),
    ("go", (398, 61, 318)),
    ("go", (402, 61, 318)),
    ("go", (402, 61, 322)),
    ("go", (402, 61, 318)),
    ("go", (399, 61, 318)),
    ("go", (399, 61, 319)),
    ("go", (399, 60, 320)),
    ("go", (399, 59, 321)),
    ("go", (399, 58, 322)),
    ("go", (399, 57, 323)),
    ("go", (399, 57, 325)),
    ("mine", (402, 58, 325)),
    ("mine", (403, 58, 325)),
    ("go", (403, 57, 325)),
    ("mine", (403, 58, 324)),
    ("mine", (403, 57, 324)),
    ("go", (403, 57, 324)),
    ("mine", (403, 57, 323)),
    ("go", (403, 57, 323)),
    ("mine", (403, 57, 322)),
    ("go", (403, 57, 322)),
    ("mine", (403, 58, 321)),
    ("open", (403, 57, 321)),
    ("go", (403, 57, 325)),
    ("go", (396, 57, 325)),
    ("go", (396, 57, 324)),
    ("bridge", (396, 56, 323)),
    ("go", (396, 57, 322)),
    ("mine", (396, 57, 321)),
    ("go", (396, 57, 319)),
    ("go", (397, 57, 319)),
    ("bridge", (397, 56, 318)),
    ("go", (397, 57, 317)),
    ("go", (398, 57, 317)),
    ("mine", (399, 57, 317)),
    ("go", (400, 57, 317)),
    ("mine", (401, 57, 317)),
    ("go", (401, 57, 317)),
    ("mine", (403, 58, 316)),
    ("open", (403, 57, 316)),
    ("go", (400, 57, 317)),
    ("go", (397, 57, 317)),
    ("go", (397, 57, 319)),
    ("go", (396, 57, 319)),
    ("go", (396, 57, 325)),
    ("go", (399, 57, 325)),
    ("go", (399, 57, 323)),
    ("go", (399, 58, 322)),
    ("go", (399, 59, 321)),
    ("go", (399, 60, 320)),
    ("go", (399, 61, 319)),
    ("go", (399, 61, 318)),
]
if args.variant == "crimson":
    route = [(143, 65, 62)]
    lower_start = operations.index(("mine", (402, 58, 325)))
    operations = [
        (kind, (t[0] - 256, t[1] + 4, t[2] - 256))
        for kind, t in operations[lower_start:]
        if kind != "bridge" and (kind, t) != ("mine", (399, 57, 317))
    ]
    prefix = [
        (142, 65, 62),
        (142, 65, 64),
        (142, 66, 65),
        (142, 67, 66),
        (142, 68, 67),
        (141, 68, 67),
        (141, 68, 61),
        (141, 68, 67),
        (146, 68, 67),
        (146, 68, 64),
        (146, 68, 67),
        (142, 68, 67),
        (142, 67, 66),
        (142, 66, 65),
        (142, 65, 64),
        (141, 65, 64),
        (141, 65, 61),
        (141, 65, 64),
        (142, 65, 64),
        (142, 65, 62),
        (143, 65, 62),
        (143, 65, 60),
        (145, 65, 60),
        (145, 65, 61),
        (146, 65, 61),
        (146, 65, 65),
        (146, 65, 64),
        (145, 65, 64),
        (145, 65, 63),
        (144, 65, 63),
        (144, 64, 64),
        (144, 63, 65),
        (144, 62, 66),
        (144, 61, 67),
        (144, 61, 69),
        (143, 61, 69),
    ]
    operations = (
        [("mine", (142, 66, 62)), ("mine", (142, 65, 62))]
        + [("go", t) for t in prefix]
        + operations
    )
    # Exact material trap inputs, disabled before each corresponding crossing.
    extra = {
        ("mine", (147, 62, 60)): [
            ("mine", (146, 62, 61)),
            ("mine", (145, 61, 60)),
            ("go", (145, 61, 60)),
            ("mine", (146, 61, 60)),
            ("mine", (146, 62, 60)),
        ],
        ("go", (146, 65, 65)): [("mine", (146, 66, 63))],
        ("go", (140, 61, 68)): [("mine", (140, 62, 68)), ("mine", (140, 61, 68))],
        ("go", (140, 61, 66)): [("mine", (140, 61, 66))],
        ("go", (140, 61, 63)): [("mine", (140, 61, 64))],
        ("go", (141, 61, 61)): [("mine", (141, 61, 62))],
        ("go", (144, 61, 61)): [("mine", (144, 62, 61)), ("mine", (144, 61, 61))],
    }
    augmented = []
    for op in operations:
        augmented.extend(extra.pop(op, []))
        augmented.append(op)
        if op == ("open", (147, 61, 60)):
            augmented.append(("go", (145, 61, 61)))
    assert not extra, extra
    operations = augmented
    # Return via the actual unobstructed east stair, not the blocked west head cell.
    cutoff = operations.index(("go", (143, 61, 67)), len(prefix))
    operations = operations[:cutoff] + [
        ("go", t)
        for t in [
            (144, 61, 69),
            (144, 61, 67),
            (144, 62, 66),
            (144, 63, 65),
            (144, 64, 64),
            (144, 65, 63),
            (144, 65, 62),
            (143, 65, 62),
        ]
    ]
mining = []
opened = []
verify(route)
for kind, target in operations:
    if kind == "go":
        a = route[-1]
        h = abs(a[0] - target[0]) + abs(a[2] - target[2])
        assert h > 0
        assert (a[0] == target[0]) != (a[2] == target[2])
        assert a[1] == target[1] or (h == 1 and abs(a[1] - target[1]) == 1)
        dx = (target[0] > a[0]) - (target[0] < a[0])
        dz = (target[2] > a[2]) - (target[2] < a[2])
        segment = [a] + [(a[0] + i * dx, target[1], a[2] + i * dz) for i in range(1, h + 1)]
        verify(segment, crouch_up=True)
        route.extend(segment[1:])
    elif kind == "bridge":
        assert at(c, *target)["Name"] == "minecraft:lava"
        anchor = (target[0], target[1], target[2] - 1)
        assert at(c, *anchor)["Name"] == "minecraft:blackstone"
        ray(
            (route[-1][0] + 0.5, route[-1][1] + 1.62, route[-1][2] + 0.5),
            (anchor[0] + 0.5, anchor[1] + 0.5, anchor[2] + 0.999),
            anchor,
        )
        b = c["bounds"]
        index = (
            ((target[1] - b[1]) * (b[5] - b[2] + 1) + target[2] - b[2]) * (b[3] - b[0] + 1)
            + target[0]
            - b[0]
        )
        c["palette"].append({"Name": "minecraft:cobblestone"})
        c["blocks_yzx"][index] = len(c["palette"]) - 1
    else:
        state = at(c, *target)
        eye = (route[-1][0] + 0.5, route[-1][1] + 1.62, route[-1][2] + 0.5)
        end = (target[0] + 0.5, target[1] + 0.5, target[2] + 0.5)
        if state["Name"] == "minecraft:tripwire":
            end = (target[0] + 0.5, target[1] + 0.1, target[2] + 0.5)
        if state["Name"] == "minecraft:redstone_wire" or state["Name"].endswith("_pressure_plate"):
            end = (target[0] + 0.5, target[1] + 0.03, target[2] + 0.5)
        if state["Name"] in {"minecraft:lever", "minecraft:polished_blackstone_button"}:
            assert state["Properties"]["facing"] == "south"
            assert state["Properties"]["face"] == "wall"
            end = (target[0] + 0.5, target[1] + 0.5, target[2] + 0.1)
        if args.variant == "crimson" and target == (146, 61, 60):
            end = (146.3, 61.5, 60.5)
        ray(eye, end, target)
        if kind == "mine":
            assert target not in removed, (kind, target)
            assert state["Name"] not in {"minecraft:air", "minecraft:lava"}
            mining.append((target, state))
            removed.add(target)
        elif kind == "open":
            assert "chest" in state["Name"]
            assert (
                at(c, target[0], target[1] + 1, target[2])["Name"] == "minecraft:air"
                or (target[0], target[1] + 1, target[2]) in removed
            )
            opened.append(target)
        else:
            raise ValueError("unrecognized operation " + kind)
verify(route, crouch_up=True)
print(
    "route",
    len(route) - 1,
    "up",
    sum(max(0, b[1] - a[1]) for a, b in pairwise(route)),
    "down",
    sum(max(0, a[1] - b[1]) for a, b in pairwise(route)),
)
print("mining", mining)
print("opened", opened)
print("rays", sum(len(v) for v in rays.values()))

if args.variant != "basalt":
    pending_message = (
        "Crimson geometry checked; complete model and quality integration still pending"
    )
    raise RuntimeError(pending_message)

# Supported external side-wall entry; this is not the whole objective's second time.
external_removed = {(403, 61, 321), (403, 62, 321)}
external = [(406, 61, 321), (405, 61, 321), (404, 61, 321), (403, 61, 321), (402, 61, 321)]
for target in [(403, 62, 321), (403, 61, 321)]:
    assert at(original, *target)["Name"] == (
        "minecraft:basalt" if target[1] == 62 else "minecraft:blackstone"
    )
    geometry.ray_check(original, external_removed - {target}, {})(
        (404.5, 62.62, 321.5), (403.999, target[1] + 0.5, 321.5), target
    )
geometry.path_checks(original, external_removed, set(), set())[1](external)
print("external side entry", external)
turns = sum(
    a != b for a, b in pairwise([tuple(b[i] - a[i] for i in range(3)) for a, b in pairwise(route)])
)
print("turns", turns)
for label, u, j, n, a, s, k, v, duty in [
    ("A", 5, 1, 0.5, 0.25, 0.25, 1, 2, 1),
    ("B", 4, 0.5, 1, 0.5, 0.5, 2, 4, 0.75),
    ("C", 3, 0.25, 1.5, 1, 1, 4, 8, 0.5),
]:
    movement = (110 - 14 + 4) / u + 14 * max(1 / u, 1 / j)
    noncombat = movement + 12.25 + (turns + 7) * n + 15 * a + 8 * s + 3 * k + v
    print(
        label,
        "movement",
        movement,
        "noncombat",
        noncombat,
        "complete by initial size",
        [
            (size, noncombat + low / duty, noncombat + high / duty)
            for size, low, high in [(1, 3.9, 3.9), (2, 11.7, 19.5), (4, 42.9, 97.5)]
        ],
    )

# Local depth on the retained post-work lower-floor network, not new excavation.
sys.path.insert(0, str(Path(__file__).parent))
paths = importlib.import_module("analyze_pilot").paths
cells = set()
for x in range(394, 406):
    for z in range(313, 328):
        try:
            verify([(x, 57, z)])
        except AssertionError:
            continue
        cells.add((x, 57, z))
local_paths = paths(cells, (399, 57, 325))
for target, distance in [((403, 57, 322), 7), ((401, 57, 317), 16)]:
    assert len(local_paths[target]) - 1 == distance
    print("lower depth", target, distance)
for target in [(397, 61, 318), (396, 57, 323), (397, 57, 318), (397, 57, 322)]:
    try:
        geometry.path_checks(original, set(), set(), set())[1]([target])
    except AssertionError as error:
        print("retained native rejection", target, str(error))
    else:
        raise AssertionError("native hazard unexpectedly accepted " + str(target))
