"""Check the declared nonnegative Slime Cave local task and conditional workload."""

# pyright: standard
# ruff: noqa: INP001, S101, ANN001, ANN201, D103, T201, PLR2004, PT018
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
    "--negative", action="store_true", help="Check the selected below-zero material state"
)
args = parser.parse_args()
filename = "negative" if args.negative else "nonnegative"
raw = (
    Path(__file__).parent / f"fixed-blocks/explorations-slime-cave-{filename}.json.gz"
).read_bytes()
expected = (
    "f8856e2278ea08228569af7757ee8f12849cd1a38010e8f9f04c19212034f3bb"
    if args.negative
    else "90f69949a5240ddb05c98fd9035d2ea7a456e9d23116377ab7abd5c0a066fef9"
)
assert hashlib.sha256(raw).hexdigest() == expected
c = json.loads(gzip.decompress(raw))["cases"][0]
state_at = importlib.import_module("evidence.item-13.render_pilot").state_at


def at(case, x, y, z):
    if args.negative:
        return state_at(case, z + 368, y - 38, -320 - x)
    return state_at(case, x, y, z)


overlap = importlib.import_module("evidence.item-13.collision.clearance").overlaps
removed = set()


def clear(box, *, collision=True):
    for x in range(math.floor(box[0]), math.ceil(box[3])):
        for y in range(math.floor(box[1]), math.ceil(box[4])):
            for z in range(math.floor(box[2]), math.ceil(box[5])):
                n = at(c, x, y, z)["Name"]
                if n == "minecraft:air" or (x, y, z) in removed:
                    continue
                if collision and n in {"minecraft:short_grass", "minecraft:tall_grass"}:
                    continue
                if n == "minecraft:chest":
                    shape = [x + 1 / 16, y, z + 1 / 16, x + 15 / 16, y + 14 / 16, z + 15 / 16]
                else:
                    shape = [
                        x,
                        y,
                        z,
                        x + 1,
                        y + 1,
                        z + 1,
                    ]  # Conservative avoidance, including water/plants.
                assert not overlap(box, shape), (box, (x, y, z), n)


def support(p, width=0.6, height=1.8):
    x, y, z = p
    assert at(c, x, y - 1, z)["Name"] in {
        "minecraft:stone",
        "minecraft:mossy_cobblestone",
        "minecraft:moss_block",
        "minecraft:deepslate",
        "minecraft:tuff",
        "minecraft:gravel",
    }, (p, at(c, x, y - 1, z))
    if at(c, x, y - 1, z)["Name"] == "minecraft:gravel":
        assert at(c, x, y - 2, z)["Name"] in {"minecraft:stone", "minecraft:deepslate"}
    clear(
        [
            x + 0.5 - width / 2,
            y,
            z + 0.5 - width / 2,
            x + 0.5 + width / 2,
            y + height,
            z + 0.5 + width / 2,
        ]
    )


leg = [(70, 2, -358), (71, 2, -358), (72, 2, -358), (73, 2, -358), (73, 3, -359)]
route = leg + list(reversed(leg))[1:] + leg[1:] + list(reversed(leg))[1:]
for p in route:
    support(p)
for a, b in pairwise(route):
    apex = max(a[1], b[1]) + (0.3 if b[1] > a[1] else 0)
    clear(
        [
            min(a[0], b[0]) + 0.2,
            apex,
            min(a[2], b[2]) + 0.2,
            max(a[0], b[0]) + 0.8,
            apex + 1.8,
            max(a[2], b[2]) + 0.8,
        ]
    )
    for p in (a, b):
        clear([p[0] + 0.2, p[1], p[2] + 0.2, p[0] + 0.8, apex + 1.8, p[2] + 0.8])

parents = [(71, 2, -364), (77, 2, -363), (69, 2, -361), (70, 2, -359), (77, 2, -359), (75, 3, -359)]
query = [69, -1, -364, 78, 8, -355]
for p in parents:
    support(p, 1.04, 1.04)
    x, y, z = p
    assert overlap(
        [x + 0.5 - 0.52, y, z + 0.5 - 0.52, x + 0.5 + 0.52, y + 1.04, z + 0.5 + 0.52], query
    )

spawner = next(r for r in c["block_entities"] if r["id"] == "minecraft:mob_spawner")
assert [spawner[k] for k in ("x", "y", "z")] == ([8, -35, -393] if args.negative else [73, 3, -360])
assert spawner["MaxNearbyEntities"] == 6 and spawner["SpawnRange"] == 4
assert spawner["SpawnData"]["entity"] == {"id": "minecraft:slime"}
eye = [73.5, 4.62, -358.5]
# Independent chest access before source removal: direct loot is a local bypass.
clear([73.5, 4.5, -359.0625, 73.51, 4.62, -358.5], collision=False)
for target in ([73.5, 3.5, -359], [73.5, 4.5, -359.0625]):
    assert math.dist(eye, target) < 4.5
    clear(
        [min(eye[i], target[i]) for i in range(3)] + [max(eye[i], target[i]) for i in range(3)],
        collision=False,
    )
    removed.add((73, 3, -360))
assert at(c, 73, 5, -360)["Name"] == "minecraft:air"
support((70, 2, -359), 1.04, 1.04)
clear([70.5, 2.8, -358.5, 70.51, 3.62, -357.5], collision=False)
assert math.dist((70.5, 2, -357.5), (70.5, 2, -358.5)) <= 3

horizontal = sum(abs(b[0] - a[0]) + abs(b[2] - a[2]) for a, b in pairwise(route))
vertical = sum(abs(b[1] - a[1]) for a, b in pairwise(route))
upward = sum(b[1] > a[1] for a, b in pairwise(route))
directions = [(b[0] - a[0], b[2] - a[2]) for a, b in pairwise(route)]
turns = sum(a != b for a, b in pairwise(directions))
print(
    json.dumps(
        {
            "horizontal": horizontal,
            "vertical": vertical,
            "upward": upward,
            "turns": turns,
            "initial_slimes": len(parents),
        }
    )
)
for u, j, n, a, s, k, v, duty in (
    (5, 1, 0.5, 0.25, 0.25, 1, 2, 1),
    (4, 0.5, 1, 0.5, 0.5, 2, 4, 0.75),
    (3, 0.25, 1.5, 1, 1, 4, 8, 0.5),
):
    base = (
        horizontal / u
        + vertical / j
        + 19 / 20
        + (11 + upward + turns + 6) * n
        + 2 * a
        + 2 * s
        + k
        + v
    )
    disable = 4 / u + 1 / j + 19 / 20 + 4 * n + a + s
    print(
        json.dumps(
            {
                "disable_seconds": disable,
                "noncombat_seconds": base,
                "six_size2_min_children_seconds": base + 18 * 0.65 / duty,
                "six_size2_max_children_seconds": base + 30 * 0.65 / duty,
            }
        )
    )
print("Dry route, conditional initial bodies/query, source/chest rays and kill station pass")
