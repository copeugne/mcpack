"""Validate declared Underground Temple links against the first retained assembly.

This is partial topology evidence, not a complete dungeon route or timing model.
"""

# pyright: standard
# ruff: noqa: INP001, S101, ANN001, ANN201, T201, PLR2004
import gzip
import hashlib
import importlib
import json
import math
from itertools import pairwise
from pathlib import Path

raw = (
    Path(__file__).parent / "fixed-blocks/explorations-underground-temple-mountainous-r2.json.gz"
).read_bytes()
assert (
    hashlib.sha256(raw).hexdigest()
    == "e86316d3e1fd412a6507533b0f3ac603e3948cb5585d6d95a917fe5168164085"
)
c = json.loads(gzip.decompress(raw))["cases"][0]
at = importlib.import_module("evidence.item-13.render_pilot").state_at
overlap = importlib.import_module("evidence.item-13.collision.clearance").overlaps
removed = set()
opened_doors = set()


def clear(box):
    """Avoid non-air cells except source-verified dry plants with no collision."""
    for x in range(math.floor(box[0]), math.ceil(box[3])):
        for y in range(math.floor(box[1]) - 1, math.ceil(box[4])):
            for z in range(math.floor(box[2]), math.ceil(box[5])):
                state = at(c, x, y, z)
                n = state["Name"]
                if (x, y, z) in removed:
                    continue
                if (x, y, z) in opened_doors:
                    for left, right in ((0, 3 / 16), (13 / 16, 1)):
                        assert not overlap(box, [x + left, y, z, x + right, y + 1, z + 1])
                    continue
                if n in {"minecraft:air", "minecraft:vine"} or (
                    n == "minecraft:sculk_vein" and state["Properties"]["waterlogged"] == "false"
                ):
                    continue
                height = 1.5 if n.endswith(("_wall", "_fence")) else 1
                assert not overlap(box, [x, y, z, x + 1, y + height, z + 1]), (
                    box,
                    (x, y, z),
                    n,
                )


def verify_path(points, *, crouch_up=False):
    """Check adult .6 by 1.8 occupancy and conservative step/jump sweeps."""
    for x, y, z in points:
        s = at(c, x, y - 1, z)
        n = s["Name"]
        assert n in {
            "minecraft:stone_bricks",
            "minecraft:cracked_stone_bricks",
            "minecraft:mossy_stone_bricks",
            "minecraft:chiseled_stone_bricks",
            "minecraft:deepslate_bricks",
            "minecraft:cracked_deepslate_bricks",
            "minecraft:stone_brick_stairs",
            "minecraft:mossy_stone_brick_stairs",
            "minecraft:gravel",
            "minecraft:stone",
        }, ((x, y, z), s)
        if n == "minecraft:gravel":
            assert at(c, x, y - 2, z)["Name"] in {
                "minecraft:stone_bricks",
                "minecraft:mossy_stone_bricks",
                "minecraft:cracked_stone_bricks",
            }
        if n.endswith("_stairs"):
            assert s["Properties"]["half"] == "bottom"
            assert s["Properties"]["shape"] == "straight"
            # A centered .6-wide actor overlaps the upper supporting half.
            # The conservative full-cell obstacle remains below its feet.
        clear([x + 0.2, y, z + 0.2, x + 0.8, y + 1.8, z + 0.8])
    for a, b in pairwise(points):
        assert abs(a[0] - b[0]) + abs(a[2] - b[2]) == 1
        assert abs(a[1] - b[1]) <= 1
        high = max(a[1], b[1]) + (0.3 if b[1] > a[1] else 0)
        height = 1.5 if crouch_up and b[1] > a[1] else 1.8
        clear(
            [
                min(a[0], b[0]) + 0.2,
                high,
                min(a[2], b[2]) + 0.2,
                max(a[0], b[0]) + 0.8,
                high + height,
                max(a[2], b[2]) + 0.8,
            ]
        )
        for x, y, z in (a, b):
            clear([x + 0.2, y, z + 0.2, x + 0.8, high + height, z + 0.8])


for center_z in (0, 28):
    for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        radial = [
            (-288 + dx * radius, y, center_z + dz * radius)
            for radius, y in ((8, 39), (7, 39), (6, 38), (5, 38), (4, 37), (3, 37))
        ]
        verify_path(radial)
        verify_path(list(reversed(radial)))
    ring = (
        [(-288 + x, 37, center_z - 3) for x in range(-3, 4)]
        + [(-285, 37, center_z + z) for z in range(-2, 4)]
        + [(-288 + x, 37, center_z + 3) for x in range(2, -4, -1)]
        + [(-291, 37, center_z + z) for z in range(2, -4, -1)]
    )
    verify_path(ring)
    print("PASS hall", center_z, "four bidirectional spokes and connected 24-block floor circuit")

north = [(-288, 39, z) for z in range(-8, -21, -1)]
verify_path(north)
verify_path(list(reversed(north)))
assert all(
    at(c, x, y, z)["Name"] == "minecraft:air"
    for x in range(-289, -286)
    for y in range(39, 41)
    for z in range(-19, -8)
)
print("PASS north corridor center, 12 horizontal blocks, Y39")

for cx, cz, directions in (
    (-288, -23, ((0, 1), (0, -1), (-1, 0))),
    (-300, 0, ((1, 0), (0, -1), (0, 1))),
):
    for dx, dz in directions:
        arm = [(cx + dx * r, 39, cz + dz * r) for r in range(4)]
        verify_path(arm)
        verify_path(list(reversed(arm)))
print("PASS three native arms at northern and western junctions, Y39")

west = [(x, 39, 0) for x in range(-296, -301, -1)]
verify_path(west)
verify_path(list(reversed(west)))
print("PASS first hall west doorway to western junction, 4 horizontal blocks")

for center_z in (0, 28):
    for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        target = (-288 + dx, 37, center_z + dz)
        x, y, z = (-288 + 3 * dx, 37, center_z + 3 * dz)
        eye = (x + 0.5, y + 1.62, z + 0.5)
        end = (target[0] + 0.5, target[1] + 0.875, target[2] + 0.5)
        assert math.dist(eye, end) < 4.5
        assert at(c, *target)["Name"] == "minecraft:chest"
        assert at(c, target[0], target[1] + 1, target[2])["Name"] == "minecraft:air"
        # Ray samples only empty cells until its assigned target. No entity ray claimed.
        for step in range(1001):
            p = tuple(eye[i] + (end[i] - eye[i]) * step / 1000 for i in range(3))
            cell = tuple(math.floor(v) for v in p)
            if cell != target:
                assert at(c, *cell)["Name"] == "minecraft:air", (cell, at(c, *cell))
    assert at(c, -288, 37, center_z)["Name"] == "minecraft:gold_block"
print("PASS eight hall chest approaches and clear lids; two saved central gold blocks")

lava_center = [z for z in range(9, 20) if at(c, -288, 39, z)["Name"] == "minecraft:lava"]
assert lava_center == list(range(11, 18))
assert all(
    at(c, x, 39, z)["Name"] == "minecraft:lava" for x in range(-289, -286) for z in range(12, 17)
)
for x, z in ((-289, 13), (-287, 15)):
    assert at(c, x, 42, z) == {"Name": "minecraft:lava", "Properties": {"level": "0"}}
    assert all(at(c, x, y, z)["Name"] == "minecraft:lava" for y in (40, 41))
rejection = None
try:
    verify_path([(-288, 39, z) for z in range(9, 20)])
except AssertionError as exc:
    rejection = exc.args
assert rejection is not None, "Native lava centerline unexpectedly passed dry clearance"
assert rejection[0][1:] == ((-288, 39, 11), "minecraft:lava"), rejection
print("REJECT native south centerline: lava at X-288,Y39,Z11..17; engineered link pending")

# Declared eastern shaft: controlled initial drop, then six carried scaffolds.
ledge = [(x, 39, 0) for x in range(-280, -277)]
verify_path(ledge)
verify_path(list(reversed(ledge)))
assert at(c, -277, 32, 0)["Name"] == "minecraft:mossy_stone_bricks"
assert all(at(c, -277, y, 0)["Name"] == "minecraft:air" for y in range(33, 41))
assert not any(
    at(c, x, y, z)["Name"] == "minecraft:ladder"
    for x in range(-279, -272)
    for y in range(32, 44)
    for z in range(-3, 4)
)
# Horizontal transfer at the upper ledge, then a separate vertical shaft envelope.
# There is deliberately no claimed raw standing support at the top of the hole.
clear([-277.8, 39, 0.2, -276.2, 40.8, 0.8])
clear([-276.8, 33, 0.2, -276.2, 40.8, 0.8])
bottom = [(-277, 33, 0), (-278, 33, 0)]
verify_path(bottom)
verify_path(list(reversed(bottom)))
eye = (-277.5, 34.62, 0.5)
base_face = (-277, 33.95, 0.5)
base_floor = (-276.5, 33, 0.5)
for target in (base_floor, base_face):
    assert math.dist(eye, target) < 4.5
    for step in range(1000):
        p = tuple(eye[i] + (target[i] - eye[i]) * step / 1000 for i in range(3))
        assert at(c, *(math.floor(v) for v in p))["Name"] == "minecraft:air"
# Six source-supported scaffold cells hypothetically occupy Y33..38, with top39.
# Their source climb/standing rules are reused from the accepted tower derivation.
scaffold_cells = [(-277, y, 0) for y in range(33, 39)]
for dx, dz in ((1, 0), (0, 1), (0, -1)):
    arm = [(-276 + dx * r, 33, dz * r) for r in range(4)]
    verify_path(arm)
    verify_path(list(reversed(arm)))
verify_path([(-277, 33, 0), (-276, 33, 0)])
horizontal = 2 * (len(ledge) - 1) + 2 * (len(bottom) - 1) + 2
vertical = 2 * (ledge[-1][1] - bottom[0][1])
print(
    f"PASS conditional eastern shaft geometry: {len(scaffold_cells)} scaffolds, "
    f"{horizontal} horizontal/{vertical} vertical blocks; "
    "initial fall exposure retained, no runtime placement or damage observation"
)
print("PASS lower shaft junction three horizontal arms, Y33; vertical return is conditional")

for sign in (1, -1):
    branch = [(-276, 34 if 7 <= z <= 9 else 33, sign * z) for z in range(18)]
    rejection = None
    try:
        verify_path(branch, crouch_up=True)
    except AssertionError as exc:
        rejection = exc.args
    assert rejection is not None, "Declared rubble route unexpectedly passed"
    assert rejection[0][1] == (-276, 34, sign * 8), rejection
    print("REJECT declared rubble branch", sign, rejection[0][1:])


def check_ray(eye, end, target):
    """Check the declared ray, retaining vine outline faces rather than collision."""
    assert math.dist(eye, end) <= 4.5
    for step in range(2001):
        p = tuple(eye[i] + (end[i] - eye[i]) * step / 2000 for i in range(3))
        cell = tuple(math.floor(v) for v in p)
        if cell == target or cell in removed:
            continue
        s = at(c, *cell)
        if s["Name"] == "minecraft:air":
            continue
        if s["Name"] == "minecraft:vine":
            x, y, z = (p[i] - cell[i] for i in range(3))
            faces = {k for k, v in s["Properties"].items() if v == "true"}
            hit = {
                "west": x <= 1 / 16,
                "east": x >= 15 / 16,
                "north": z <= 1 / 16,
                "south": z >= 15 / 16,
                "up": y >= 15 / 16,
            }
            assert faces, (cell, p, s)
            assert not any(hit[f] for f in faces), (cell, p, s)
            continue
        raise AssertionError((cell, p, s))


for sign in (1, -1):
    verify_path([(-276, 33, sign * z) for z in range(7)])
    actions = [(6, 33, 7), (7, 34, 8), (7, 33, 8), (8, 33, 9)]
    if sign == 1:
        actions.insert(1, (7, 34, 7))
    for station_z, target_y, target_z in actions:
        station = (-276, 33, sign * station_z)
        verify_path([station])
        target = (-276, target_y, sign * target_z)
        name = at(c, *target)["Name"]
        assert name in {
            "minecraft:gravel",
            "minecraft:vine",
            "minecraft:stone_bricks",
            "minecraft:mossy_stone_bricks",
            "minecraft:cracked_stone_bricks",
        }
        eye = (-275.5, 34.62, sign * station_z + 0.5)
        face_z = target[2] if sign == 1 else target[2] + 1
        if name == "minecraft:vine":
            assert target == (-276, 34, 7)
            end = (-275.5, 34.5, 7.95)
        else:
            end = (-275.5, target_y + 0.5, face_z)
        check_ray(eye, end, target)
        removed.add(target)
    branch = [(-276, 33, sign * z) for z in range(18)]
    verify_path(branch)
    verify_path(list(reversed(branch)))
    print(
        "PASS breached rubble branch",
        sign,
        len(actions),
        "ordered removals; 34 horizontal/0 vertical return blocks",
    )

chest = (-278, 33, 17)
assert at(c, *chest)["Name"] == "minecraft:chest"
assert at(c, -278, 34, 17) == {
    "Name": "minecraft:stone_brick_stairs",
    "Properties": {"facing": "west", "half": "top", "shape": "straight", "waterlogged": "false"},
}
# ChestBlock tests the above block's redstone-conductor predicate, not air.
# The pinned legacy straight stair has a non-full collision shape and fails that predicate.
check_ray((-275.5, 34.62, 17.5), (-277.0625, 33.5, 17.5), chest)
print(
    "PASS southern chest approach and source lid rule beneath straight stair; transfer not measured"
)

# Seven ordered removals through the eastern source corridor, after branch checks.
verify_path([(x, 33, 0) for x in range(-276, -271)])
source_actions = [
    (-272, -271, 34, "minecraft:cobweb"),
    (-270, -269, 34, "minecraft:cobweb"),
    (-269, -268, 34, "minecraft:cobweb"),
    (-269, -268, 33, "minecraft:spawner"),
    (-268, -267, 33, "minecraft:cobweb"),
    (-266, -265, 34, "minecraft:cobweb"),
    (-266, -265, 33, "minecraft:cobweb"),
]
last_station = -272
for station_x, target_x, y, expected_name in source_actions:
    verify_path([(x, 33, 0) for x in range(last_station, station_x + 1)])
    target = (target_x, y, 0)
    assert at(c, *target)["Name"] == expected_name
    check_ray((station_x + 0.5, 34.62, 0.5), (target_x, y + 0.5, 0.5), target)
    removed.add(target)
    last_station = station_x
east = [(x, 33, 0) for x in range(-276, -247)]
verify_path(east)
verify_path(list(reversed(east)))
print("PASS eastern corridor to junction: six webs/one source removed, 56 horizontal return blocks")

# Native button-operated entrance. Each crossing is conditional on its own press.
verify_path([(-248, 33, z) for z in range(4)])
for y, half in ((33, "lower"), (34, "upper")):
    assert at(c, -248, y, 5) == {
        "Name": "minecraft:iron_door",
        "Properties": {
            "facing": "south",
            "half": half,
            "hinge": "right",
            "open": "false",
            "powered": "false",
        },
    }
for target, facing, support, eye, end in (
    ((-249, 34, 4), "north", (-249, 34, 5), (-247.5, 34.62, 3.5), (-248.5, 34.5, 4.9)),
    ((-248, 35, 6), "south", (-248, 35, 5), (-247.5, 34.62, 6.5), (-247.5, 35.5, 6.1)),
):
    assert at(c, *target) == {
        "Name": "minecraft:oak_button",
        "Properties": {"face": "wall", "facing": facing, "powered": "false"},
    }
    assert at(c, *support)["Name"] == "minecraft:stone_bricks"
    check_ray(eye, end, target)
opened_doors.update({(-248, 33, 5), (-248, 34, 5)})
crossing = [(-248, 33, z) for z in range(3, 7)]
verify_path(crossing)
verify_path(list(reversed(crossing)))
# The entrance contains vine: use a declared 3-block/s transfer for every profile.
assert all(3 / min(speed, 3) < 30 / 20 for speed in (5, 4, 3))
for station, target in (((-248, 33, 6), (-249, 33, 6)), ((-251, 33, 9), (-252, 33, 9))):
    if target[0] == -252:
        verify_path([(-248 - dx, 33, 6) for dx in range(4)])
        verify_path([(-251, 33, z) for z in range(6, 10)])
    verify_path([station])
    assert at(c, *target)["Name"] == "minecraft:cobweb"
    check_ray(
        (station[0] + 0.5, 34.62, station[2] + 0.5), (target[0] + 1, 33.5, target[2] + 0.5), target
    )
    removed.add(target)
room_route = (
    [(-248 - dx, 33, 6) for dx in range(4)]
    + [(-251, 33, z) for z in range(7, 10)]
    + [(-252, 33, 9)]
)
verify_path(room_route)
verify_path(list(reversed(room_route)))
assert at(c, -252, 33, 10)["Name"] == "minecraft:chest"
assert at(c, -252, 34, 10)["Name"] == "minecraft:cobweb"
# Source noCollission makes the above web non-full and nonconducting for the chest rule.
check_ray((-251.5, 34.62, 9.5), (-251.5, 33.5, 10.0625), (-252, 33, 10))
print("PASS enchanting room: two timed door presses, two web removals, chest access beneath web")
assert at(c, -250, 33, 7)["Name"] == "minecraft:enchanting_table"
assert at(c, -245, 33, 7)["Name"] == "minecraft:brewing_stand"
check_ray((-250.5, 34.62, 7.5), (-250, 33.625, 7.5), (-250, 33, 7))
check_ray((-247.5, 34.62, 6.5), (-244.5, 33.5, 7.5), (-245, 33, 7))
print("PASS room facility interaction rays; recipes, enchanting power and outputs not measured")

# Northern blind shaft: native rim and one-block terrain-backed pit, no scaffold.
north_arm = [(-248, 33, -z) for z in range(6)]
rim = (
    [(-248 - dx, 33, -5) for dx in range(3)]
    + [(-250, 33, -z) for z in range(6, 10)]
    + [(x, 33, -9) for x in range(-249, -245)]
    + [(-246, 33, z) for z in range(-8, -4)]
    + [(x, 33, -5) for x in (-247, -248)]
)
pit = [(-248, 33, -5)] + [(-248, 32, -z) for z in range(6, 9)]
for path in (north_arm, rim, pit):
    verify_path(path)
    verify_path(list(reversed(path)))
assert not any(
    -251 <= b["x"] <= -245 and 32 <= b["y"] <= 37 and -10 <= b["z"] <= -4
    for b in c["block_entities"]
)
assert at(c, -248, 35, -7)["Name"] == "minecraft:lantern"
horizontal = 2 * (len(north_arm) - 1) + len(rim) - 1 + 2 * (len(pit) - 1)
print(
    "PASS northern blind-shaft inspection:",
    horizontal,
    "horizontal, 2 vertical; encounter occupancy unknown",
)

# Terminal connector has local terrain caps, not three onward room links.
east_link = [(x, 33, 0) for x in range(-248, -240)]
terminal_arms = (
    [(x, 33, 0) for x in range(-241, -237)],
    [(-241, 33, -z) for z in range(4)],
    [(-241, 33, z) for z in range(3)],
)
for path in (east_link, *terminal_arms):
    verify_path(path)
    verify_path(list(reversed(path)))
for target in ((-237, 33, 0), (-241, 33, -4), (-241, 33, 3)):
    assert at(c, *target)["Name"] in {"minecraft:stone", "minecraft:stone_bricks"}
assert not any(
    -244 <= b["x"] <= -238 and 32 <= b["y"] <= 36 and -3 <= b["z"] <= 3 for b in c["block_entities"]
)
horizontal = 2 * (len(east_link) - 1 + sum(len(arm) - 1 for arm in terminal_arms))
print("PASS terminal connector inspection:", horizontal, "horizontal, 0 vertical; local caps")

# Quest tower upper rewards: one web and a timed button-operated iron door.
tower_approach = [(-288, 39, -z) for z in range(23, 28)] + [(-287, 39, -z) for z in range(27, 30)]
verify_path(tower_approach)
target = (-287, 39, -30)
assert at(c, *target)["Name"] == "minecraft:cobweb"
check_ray((-286.5, 40.62, -28.5), (-286.5, 39.5, -29), target)
removed.add(target)
tower_approach += [(-287, 39, -30), (-287, 39, -31)]
verify_path(tower_approach)
for z, facing, endpoint_z in ((-31, "south", -30.9), (-33, "north", -32.1)):
    target = (-287, 41, z)
    assert at(c, *target) == {
        "Name": "minecraft:stone_button",
        "Properties": {"face": "wall", "facing": facing, "powered": "false"},
    }
    assert at(c, -287, 41, -32)["Name"] == "minecraft:stone_bricks"
    check_ray((-286.5, 40.62, z + 0.5), (-286.5, 41.5, endpoint_z), target)
for y, half in ((39, "lower"), (40, "upper")):
    assert at(c, -287, y, -32) == {
        "Name": "minecraft:iron_door",
        "Properties": {
            "facing": "north",
            "half": half,
            "hinge": "left",
            "open": "false",
            "powered": "false",
        },
    }
    opened_doors.add((-287, y, -32))
tower_crossing = [(-287, 39, -z) for z in range(31, 34)]
assert all(2 / speed < 20 / 20 for speed in (5, 4, 3))
tower_rewards = [
    (-287, 39, -33),
    (-288, 39, -33),
    (-289, 39, -33),
    (-289, 39, -34),
    (-288, 39, -34),
    (-287, 39, -34),
    (-287, 39, -35),
]
for path in (tower_approach, tower_crossing, tower_rewards):
    verify_path(path)
    verify_path(list(reversed(path)))
for chest, eye, end in (
    ((-290, 39, -33), (-288.5, 40.62, -32.5), (-289.0625, 39.5, -32.5)),
    ((-286, 39, -35), (-286.5, 40.62, -34.5), (-285.9375, 39.5, -34.5)),
):
    assert at(c, *chest)["Name"] == "minecraft:chest"
    assert at(c, chest[0], chest[1] + 1, chest[2])["Name"] == "minecraft:air"
    check_ray(eye, end, chest)
horizontal = 2 * sum(len(p) - 1 for p in (tower_approach, tower_crossing, tower_rewards))
print(
    "PASS tower upper two-chest route:", horizontal, "horizontal, 0 vertical; lower tower pending"
)
