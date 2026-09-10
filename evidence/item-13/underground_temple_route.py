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
                        plate = (
                            [x + left, y, z, x + right, y + 1, z + 1]
                            if state["Properties"]["facing"] in {"north", "south"}
                            else [x, y, z + left, x + 1, y + 1, z + right]
                        )
                        assert not overlap(box, plate)
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
            "minecraft:cobblestone",
            "minecraft:calcite",
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
        if s["Name"] == "minecraft:vine" or (
            s["Name"] == "minecraft:sculk_vein" and s["Properties"]["waterlogged"] == "false"
        ):
            x, y, z = (p[i] - cell[i] for i in range(3))
            faces = {k for k, v in s["Properties"].items() if v == "true"}
            hit = {
                "west": x <= 1 / 16,
                "east": x >= 15 / 16,
                "north": z <= 1 / 16,
                "south": z >= 15 / 16,
                "up": y >= 15 / 16,
                "down": y <= 1 / 16,
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

# Northern tower door and engineered descent beside the armed hatch landing.
for z, facing, endpoint_z in ((-35, "south", -34.9), (-37, "north", -36.1)):
    target = (-289, 41, z)
    assert at(c, *target) == {
        "Name": "minecraft:stone_button",
        "Properties": {"face": "wall", "facing": facing, "powered": "false"},
    }
    assert at(c, -289, 41, -36)["Name"] == "minecraft:stone_bricks"
    check_ray((-288.5, 40.62, z + 0.5), (-288.5, 41.5, endpoint_z), target)
for y, half in ((39, "lower"), (40, "upper")):
    assert at(c, -289, y, -36) == {
        "Name": "minecraft:iron_door",
        "Properties": {
            "facing": "north",
            "half": half,
            "hinge": "right",
            "open": "false",
            "powered": "false",
        },
    }
    opened_doors.add((-289, y, -36))
hatch_approach = [
    (-287, 39, -35),
    (-288, 39, -35),
    (-289, 39, -35),
    (-289, 39, -36),
    (-289, 39, -37),
    (-288, 39, -37),
]
verify_path(hatch_approach)
verify_path(list(reversed(hatch_approach)))
floor_target = (-288, 38, -38)
assert at(c, *floor_target)["Name"] == "minecraft:stone_bricks"
check_ray((-287.5, 40.62, -36.5), (-287.5, 39, -37.5), floor_target)
removed.add(floor_target)
clear([-287.8, 35, -37.8, -287.2, 40.8, -37.2])
clear([-287.8, 39, -37.8, -287.2, 40.8, -36.2])
verify_path([(-288, 35, -38), (-288, 35, -37)])
verify_path([(-288, 35, -37), (-288, 35, -38)])
# Base placement ray from the southern lower stance to the retained floor.
assert at(c, -288, 34, -38)["Name"] == "minecraft:stone_bricks"
check_ray((-287.5, 36.62, -36.5), (-287.5, 35, -37.5), (-288, 34, -38))
# Three side clicks on the same base extend the distance-zero scaffold upward.
check_ray((-287.5, 36.62, -36.5), (-287.5, 35.95, -37), (-288, 35, -38))
for x in (-289, -288, -287):
    wire = at(c, x, 35, -39)
    assert wire["Name"] == "minecraft:tripwire"
    assert wire["Properties"]["attached"] == "true"
    assert wire["Properties"]["disarmed"] == "false"
for x, facing in ((-290, "east"), (-286, "west")):
    assert at(c, x, 35, -39)["Name"] == "minecraft:tripwire_hook"
    assert at(c, x, 36, -39) == {
        "Name": "minecraft:dispenser",
        "Properties": {"facing": facing, "triggered": "false"},
    }
print("PASS tower alternate descent: one floor removal, four scaffolds; 4-block fall retained")

# Middle piston-panel breach under the declared unchanged circuit condition.
verify_path([(-288, 35, z) for z in range(-37, -34)])
for y in (35, 36):
    target = (-288, y, -34)
    assert at(c, *target)["Name"] in {
        "minecraft:cracked_stone_bricks",
        "minecraft:chiseled_stone_bricks",
    }
    check_ray((-287.5, 36.62, -34.5), (-287.5, y + 0.5, -34), target)
    removed.add(target)
middle_route = [(-288, 35, z) for z in range(-37, -29)] + [
    (-287, 35, -30),
    (-287, 35, -29),
]
verify_path(middle_route)
verify_path(list(reversed(middle_route)))
assert at(c, -286, 35, -29)["Name"] == "minecraft:chest"
assert at(c, -286, 36, -29)["Name"] == "minecraft:air"
check_ray((-286.5, 36.62, -28.5), (-285.9375, 35.5, -28.5), (-286, 35, -29))
for y in (35, 36, 37):
    for x, facing in ((-291, "east"), (-285, "west")):
        assert at(c, x, y, -34) == {
            "Name": "minecraft:sticky_piston",
            "Properties": {"extended": "true", "facing": facing},
        }
print("PASS middle chest: 18 horizontal return blocks; two-block panel breach conditional")

target = (-287, 34, -30)
assert at(c, *target)["Name"] == "minecraft:cracked_stone_bricks"
check_ray((-286.5, 36.62, -28.5), (-286.5, 35, -29.5), target)
removed.add(target)
clear([-286.8, 31, -29.8, -286.2, 36.8, -29.2])
clear([-286.8, 35, -29.8, -286.2, 36.8, -28.2])
verify_path([(-287, 31, -30), (-287, 31, -29)])
verify_path([(-287, 31, -29), (-287, 31, -30)])
assert at(c, -287, 30, -30)["Name"] == "minecraft:stone_bricks"
check_ray((-286.5, 32.62, -28.5), (-286.5, 31, -29.5), (-287, 30, -30))
check_ray((-286.5, 32.62, -28.5), (-286.5, 31.95, -29), (-287, 31, -30))
print("PASS next tower descent: one floor removal, four scaffolds; 4 horizontal/8 vertical return")

# Lower tower has two separate timed doors and an eastern descending branch.
verify_path([(-287, 31, -29), (-287, 31, -30)])
target = (-288, 31, -30)
assert at(c, *target)["Name"] == "minecraft:cobweb"
check_ray((-286.5, 32.62, -29.5), (-287, 31.5, -29.5), target)
removed.add(target)
for door_z, door_facing, hinge in ((-32, "north", "right"), (-36, "south", "left")):
    for z, facing, endpoint_z in (
        (door_z + 1, "south", door_z + 1.1),
        (door_z - 1, "north", door_z - 0.1),
    ):
        target = (-288, 33, z)
        assert at(c, *target) == {
            "Name": "minecraft:stone_button",
            "Properties": {"face": "wall", "facing": facing, "powered": "false"},
        }
        assert at(c, -288, 33, door_z)["Name"] in {
            "minecraft:stone_bricks",
            "minecraft:cracked_stone_bricks",
        }
        check_ray((-287.5, 32.62, z + 0.5), (-287.5, 33.5, endpoint_z), target)
    for y, half in ((31, "lower"), (32, "upper")):
        assert at(c, -288, y, door_z) == {
            "Name": "minecraft:iron_door",
            "Properties": {
                "facing": door_facing,
                "half": half,
                "hinge": hinge,
                "open": "false",
                "powered": "false",
            },
        }
        opened_doors.add((-288, y, door_z))
lower_tower = [(-287, 31, -29), (-287, 31, -30)] + [(-288, 31, -z) for z in range(30, 39)]
verify_path(lower_tower)
verify_path(list(reversed(lower_tower)))
print("PASS lower tower two-door route: 20 horizontal return blocks, one web removal")
descending_branch = (
    [(-288 + dx, 31, -34) for dx in range(18)]
    + [(x, -x - 240, -34) for x in range(-270, -265)]
    + [(x, 25, -34) for x in range(-265, -260)]
)
verify_path(descending_branch)
verify_path(list(reversed(descending_branch)))
print("PASS eastern lower branch to shaft ledge: 54 horizontal/12 vertical return blocks")

terminal_rim = (
    [(-261, 25, z) for z in range(-34, -37, -1)]
    + [(x, 25, -36) for x in range(-260, -256)]
    + [(-257, 25, z) for z in range(-35, -31)]
    + [(x, 25, -32) for x in range(-258, -262, -1)]
    + [(-261, 25, -33), (-261, 25, -34)]
)
verify_path(terminal_rim)
verify_path(list(reversed(terminal_rim)))
assert all(at(c, -260, y, -34)["Name"] == "minecraft:air" for y in range(21, 26))
assert not any(
    -262 <= b["x"] <= -256 and 24 <= b["y"] <= 29 and -37 <= b["z"] <= -31
    for b in c["block_entities"]
)
print("PASS terminal rim: 16 horizontal blocks; pit continuation below raw Y21 unresolved")

# Final tower descent and a dry zigzag beside the alternating lava tongues.
target = (-288, 30, -38)
assert at(c, *target)["Name"] == "minecraft:stone_bricks"
check_ray((-287.5, 32.62, -36.5), (-287.5, 31, -37.5), target)
removed.add(target)
clear([-287.8, 27, -37.8, -287.2, 32.8, -37.2])
clear([-287.8, 31, -37.8, -287.2, 32.8, -36.2])
verify_path([(-288, 27, -38), (-288, 27, -37)])
verify_path([(-288, 27, -37), (-288, 27, -38)])
assert at(c, -288, 26, -38)["Name"] == "minecraft:cracked_stone_bricks"
check_ray((-287.5, 28.62, -36.5), (-287.5, 27, -37.5), (-288, 26, -38))
check_ray((-287.5, 28.62, -36.5), (-287.5, 27.95, -37), (-288, 27, -38))
bottom_zigzag = [
    (-288, 27, -37),
    (-287, 27, -37),
    (-286, 27, -37),
    (-286, 27, -36),
    (-286, 27, -35),
    (-286, 27, -34),
    (-287, 27, -34),
    (-287, 27, -33),
    (-288, 27, -33),
    (-288, 27, -32),
    (-289, 27, -32),
    (-289, 27, -31),
    (-290, 27, -31),
    (-290, 27, -30),
    (-290, 27, -29),
    (-289, 27, -29),
    (-289, 27, -28),
    (-289, 27, -27),
    (-288, 27, -27),
    (-288, 27, -26),
    (-288, 27, -25),
]
verify_path(bottom_zigzag)
verify_path(list(reversed(bottom_zigzag)))
print("PASS final tower descent: four scaffolds; dry lava zigzag 40 horizontal return blocks")

# Bedroom: rotate the conservative door plates and retain both bed bays as one room.
bedroom_approach = [(-288, 27, z) for z in range(-25, -21)] + [(-287, 27, -22)]
verify_path(bedroom_approach)
for target, facing, support, eye, end in (
    ((-287, 28, -21), "west", (-286, 28, -21), (-286.5, 28.62, -21.5), (-286.9, 28.5, -20.5)),
    ((-285, 28, -23), "east", (-286, 28, -23), (-284.5, 28.62, -21.5), (-284.1, 28.5, -22.5)),
):
    assert at(c, *target) == {
        "Name": "minecraft:oak_button",
        "Properties": {"face": "wall", "facing": facing, "powered": "false"},
    }
    assert at(c, *support)["Name"] == "minecraft:stone_bricks"
    check_ray(eye, end, target)
for y, half in ((27, "lower"), (28, "upper")):
    assert at(c, -286, y, -22) == {
        "Name": "minecraft:iron_door",
        "Properties": {
            "facing": "east",
            "half": half,
            "hinge": "left",
            "open": "false",
            "powered": "false",
        },
    }
    opened_doors.add((-286, y, -22))
bedroom_crossing = [(x, 27, -22) for x in range(-287, -284)]
bedroom_aisle = [
    (-285, 27, -22),
    (-284, 27, -22),
    (-284, 27, -23),
    (-284, 27, -24),
    (-283, 27, -24),
    (-284, 27, -24),
    (-284, 27, -23),
    (-284, 27, -22),
    (-284, 27, -21),
    (-284, 27, -20),
    (-283, 27, -20),
    (-284, 27, -20),
    (-284, 27, -21),
    (-284, 27, -22),
    (-285, 27, -22),
]
for path in (bedroom_approach, bedroom_crossing, bedroom_aisle):
    verify_path(path)
    verify_path(list(reversed(path)))
for station_z, chest_z, barrel_zs in ((-24, -25, (-24, -23)), (-20, -19, (-21, -20))):
    eye = (-282.5, 28.62, station_z + 0.5)
    chest = (-282, 27, chest_z)
    assert at(c, *chest)["Name"] == "minecraft:chest"
    assert at(c, -282, 28, chest_z)["Name"] == "minecraft:air"
    end_z = chest_z + (0.9375 if chest_z < station_z else 0.0625)
    check_ray(eye, (-281.5, 27.5, end_z), chest)
    for z in barrel_zs:
        assert at(c, -281, 30, z)["Name"] == "minecraft:barrel"
        check_ray(eye, (-281, 30.5, z + 0.5), (-281, 30, z))
for z in (-23, -21):
    assert at(c, -283, 27, z)["Name"] == "minecraft:red_bed"
    check_ray((-283.5, 28.62, z + 0.5), (-283, 27.3, z + 0.5), (-283, 27, z))
assert at(c, -284, 27, -19)["Name"] == "minecraft:blast_furnace"
check_ray((-283.5, 28.62, -19.5), (-283.5, 27.5, -19), (-284, 27, -19))
print("PASS bedroom: one room, two chests/four barrels, two beds/furnace interaction rays")
assert all(2 / speed < 30 / 20 for speed in (5, 4, 3))
for path in (
    [(-288, 27, z) for z in range(-25, -13)],
    [(x, 27, -22) for x in range(-288, -296, -1)],
):
    verify_path(path)
    verify_path(list(reversed(path)))
for cx, cz in ((-288, -14), (-295, -22)):
    for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        arm = [(cx + dx * r, 27, cz + dz * r) for r in range(4)]
        verify_path(arm)
        verify_path(list(reversed(arm)))
print("PASS bedroom passage: 11-block south link, 7-block west link, two four-arm junctions")

# Dungeon room native survey must run before its four source-exposure holes.
dungeon_entry = [(-288, 27, z) for z in range(-14, -4)]
dungeon_ring = (
    [(x, 27, -5) for x in range(-288, -284)]
    + [(-285, 27, z) for z in range(-4, 2)]
    + [(x, 27, 1) for x in range(-286, -292, -1)]
    + [(-291, 27, z) for z in range(0, -6, -1)]
    + [(x, 27, -5) for x in range(-290, -287)]
)
for path in (dungeon_entry, dungeon_ring):
    verify_path(path)
    verify_path(list(reversed(path)))
dungeon_sources = (
    ((-288, -5), (-288, -6), (-288, -4)),
    ((-285, -2), (-285, -3), (-286, -2)),
    ((-288, 1), (-288, 2), (-288, 0)),
    ((-291, -2), (-291, -3), (-290, -2)),
)
for (x, z), _, (sx, sz) in dungeon_sources:
    assert at(c, sx, 27, sz)["Name"] == "minecraft:chest"
    assert at(c, sx, 28, sz)["Name"] == "minecraft:air"
    check_ray((x + 0.5, 28.62, z + 0.5), (sx + 0.5, 27.5, sz + 0.5), (sx, 27, sz))
print("PASS dungeon native survey: 42 horizontal return blocks, four chest approaches")
for (x, z), (ax, az), (sx, sz) in dungeon_sources:
    verify_path([(ax, 27, az), (x, 27, z)])
    eye = (ax + 0.5, 28.62, az + 0.5)
    if x in (-285, -291):
        vein = (x, 27, z)
        assert at(c, *vein)["Name"] == "minecraft:sculk_vein"
        assert at(c, *vein)["Properties"]["down"] == "true"
        check_ray(eye, (x + 0.5, 27.03125, z + 0.5), vein)
        removed.add(vein)
    floor = (x, 26, z)
    assert at(c, *floor)["Name"] in {"minecraft:stone_bricks", "minecraft:cracked_stone_bricks"}
    assert at(c, x, 25, z)["Name"] == "minecraft:stone"
    check_ray(eye, (x + 0.5, 27, z + 0.5), floor)
    removed.add(floor)
    verify_path([(ax, 27, az), (x, 26, z)])
    verify_path([(x, 26, z), (ax, 27, az)])
    source = (sx, 26, sz)
    assert at(c, *source)["Name"] == "minecraft:spawner"
    end = ((x + sx) / 2 + 0.5, 26.5, (z + sz) / 2 + 0.5)
    check_ray((x + 0.5, 27.62, z + 0.5), end, source)
    removed.add(source)
print("PASS four buried sources: four floor holes, two vein removals; encounters not measured")

# Library entrance survey, with blocked elevated chest lids retained as a defect.
library_front = (
    [(x, 27, -22) for x in range(-295, -305, -1)]
    + [(-304, 27, -23), (-305, 27, -23), (-306, 27, -23)]
    + [(-306, 27, -22), (-306, 27, -21)]
    + [(x, 27, -21) for x in range(-305, -299)]
    + [(-300, 27, -22)]
    + [(x, 27, -22) for x in range(-299, -294)]
)
verify_path(library_front)
verify_path(list(reversed(library_front)))
for x, lid in ((-307, "minecraft:stone_bricks"), (-300, "minecraft:mossy_stone_bricks")):
    assert at(c, x, 31, -25)["Name"] == "minecraft:chest"
    assert at(c, x, 32, -25)["Name"] == lid
print("PASS library front circuit:", len(library_front) - 1, "horizontal; both chest lids blocked")

# Explicit elevation and lid breach; original blocked-state checks precede these edits.
for x, adjacent, chest_x in ((-302, -301, -300), (-305, -306, -307)):
    approach = (
        [(-304, 27, -22), (-303, 27, -22), (-302, 27, -22), (-302, 27, -23), (-302, 27, -24)]
        if x == -302
        else [(-304, 27, -22), (-304, 27, -23), (-305, 27, -23), (-305, 27, -24)]
    )
    verify_path(approach)
    verify_path(list(reversed(approach)))
    eye = (x + 0.5, 28.62, -23.5)
    target = (x, 27, -25)
    expected = "minecraft:cobweb" if x == -302 else "minecraft:sculk_vein"
    assert at(c, *target)["Name"] == expected
    endpoint = (x + 0.5, 27.5, -24.5) if x == -302 else (x + 0.96875, 27.5, -24.5)
    check_ray(eye, endpoint, target)
    removed.add(target)
    assert at(c, x, 26, -25)["Name"] in {"minecraft:stone_bricks", "minecraft:cracked_stone_bricks"}
    check_ray(eye, (x + 0.5, 27, -24.5), (x, 26, -25))
    check_ray(eye, (x + 0.5, 27.95, -24), (x, 27, -25))
    clear([x + 0.2, 27, -24.8, x + 0.8, 31.8, -24.2])
    verify_path([(x, 27, -24), (x, 27, -25)])
    verify_path([(x, 27, -25), (x, 27, -24)])
    eye = (x + 0.5, 31.62, -24.5)
    stair = (adjacent, 31, -25)
    assert at(c, *stair)["Name"].endswith("stone_brick_stairs")
    assert at(c, *stair)["Properties"]["half"] == "top"
    check_ray(eye, (adjacent + 0.5, 31.75, -24.5), stair)
    removed.add(stair)
    roof = (adjacent, 32, -25)
    assert at(c, *roof)["Name"] == "minecraft:stone_bricks"
    check_ray(eye, (adjacent + 0.5, 32, -24.5), roof)
    removed.add(roof)
    lid = (chest_x, 32, -25)
    face_x = chest_x if chest_x > x else chest_x + 1
    check_ray(eye, (face_x, 32.5, -24.5), lid)
    removed.add(lid)
    chest = (chest_x, 31, -25)
    face_x += 0.0625 if chest_x > x else -0.0625
    check_ray(eye, (face_x, 31.5, -24.5), chest)
print("PASS both library chest remedies: six scaffolds, six masonry, one web and one vein")

library_aisles = (
    [(-302, 27, z) for z in range(-25, -33, -1)]
    + [(x, 27, -32) for x in range(-303, -306, -1)]
    + [(-305, 27, z) for z in range(-31, -23)]
    + [(x, 27, -24) for x in range(-304, -301)]
    + [(-302, 27, -25)]
)
aisle_webs = {
    (-302, 28, -27),
    (-302, 27, -31),
    (-303, 27, -32),
    (-305, 27, -31),
    (-305, 28, -30),
    (-305, 27, -30),
    (-305, 27, -26),
    (-304, 27, -24),
}
handled = set()
for a, b in pairwise(library_aisles):
    for y in (28, 27):
        target = (b[0], y, b[2])
        if target in aisle_webs:
            assert at(c, *target)["Name"] == "minecraft:cobweb"
            check_ray((a[0] + 0.5, 28.62, a[2] + 0.5), (b[0] + 0.5, y + 0.5, b[2] + 0.5), target)
            removed.add(target)
            handled.add(target)
    verify_path([a, b])
assert handled == aisle_webs
verify_path(list(reversed(library_aisles)))
print("PASS library aisle circuit:", len(library_aisles) - 1, "horizontal; eight additional webs")

for x, chest_z in ((-295, -16), (-281, -12)):
    step = 1 if x > -288 else -1
    path = [(xx, 27, -14) for xx in range(-288, x + step, step)]
    verify_path(path)
    verify_path(list(reversed(path)))
    chest = (x, 27, chest_z)
    assert at(c, *chest)["Name"] == "minecraft:chest"
    lid = at(c, x, 28, chest_z)
    assert lid["Name"] == "minecraft:stone_brick_stairs"
    assert lid["Properties"]["half"] == "top"
    assert lid["Properties"]["shape"] == "straight"
    check_ray((x + 0.5, 28.62, -13.5), (x + 0.5, 27.5, chest_z + 0.5), chest)
print("PASS two lower terminal rewards: 28 horizontal total, non-full stair lids")

cell_routes = (
    (-275, [(-275, 39, 25), (-276, 39, 25), (-276, 39, 24), (-276, 39, 23)]),
    (
        -270,
        [
            (-270, 39, 25),
            (-270, 39, 24),
            (-270, 39, 23),
            (-270, 39, 24),
            (-271, 39, 24),
            (-272, 39, 24),
            (-272, 39, 23),
        ],
    ),
)
for x, inside in cell_routes:
    approach = [(xx, 39, 28) for xx in range(-280, x + 1)] + [(x, 39, 27)]
    verify_path(approach)
    for y in (40, 39):
        target = (x, y, 26)
        assert at(c, *target)["Name"] == "minecraft:iron_bars"
        check_ray((x + 0.5, 40.62, 27.5), (x + 0.5, y + 0.5, 26.5), target)
        removed.add(target)
    entrance = [(x, 39, z) for z in (27, 26, 25)]
    for path in (approach, entrance, inside):
        verify_path(path)
        verify_path(list(reversed(path)))
for target, eye, end in (
    ((-274, 39, 25), (-274.5, 40.62, 25.5), (-274, 39.5, 25.5)),
    ((-272, 39, 22), (-271.5, 40.62, 23.5), (-271.5, 39.5, 23)),
):
    assert at(c, *target)["Name"] == "minecraft:barrel"
    check_ray(eye, end, target)
for bed_x, station_x in ((-275, -276), (-271, -270)):
    assert at(c, bed_x, 39, 23)["Name"] == "minecraft:gray_bed"
    edge = bed_x if station_x < bed_x else bed_x + 1
    check_ray((station_x + 0.5, 40.62, 23.5), (edge, 39.3, 23.5), (bed_x, 39, 23))
assert at(c, -272, 39, 25)["Name"] == "minecraft:cauldron"
check_ray((-271.5, 40.62, 24.5), (-271.5, 39.5, 25), (-272, 39, 25))
print("PASS two barred cells: four bar removals, two barrels, two beds and empty cauldron")

south_terminal = [(-288, 39, z) for z in range(36, 48)]
verify_path(south_terminal)
verify_path(list(reversed(south_terminal)))
for dx, dz in ((0, -1), (1, 0), (0, 1)):
    arm = [(-288 + dx * r, 39, 40 + dz * r) for r in range(4)]
    verify_path(arm)
    verify_path(list(reversed(arm)))
for chest, eye in (
    ((-290, 39, 47), (-287.5, 40.62, 47.5)),
    ((-324, 33, 5), (-323.5, 34.62, 7.5)),
):
    x, y, z = chest
    assert at(c, *chest)["Name"] == "minecraft:chest"
    lid = at(c, x, y + 1, z)
    assert lid["Name"] == "minecraft:stone_brick_stairs"
    assert lid["Properties"]["half"] == "top"
    assert lid["Properties"]["shape"] == "straight"
    check_ray(eye, (x + 0.5, y + 0.5, z + 0.5), chest)
upper_west = [(-300, 39, z) for z in range(6)]
verify_path(upper_west)
verify_path(list(reversed(upper_west)))
clear([-299.8, 33, 6.2, -299.2, 40.8, 6.8])
clear([-299.8, 39, 5.2, -299.2, 40.8, 6.8])
verify_path([(-300, 33, 6), (-300, 33, 5)])
verify_path([(-300, 33, 5), (-300, 33, 6)])
assert at(c, -300, 32, 6)["Name"] == "minecraft:cracked_stone_bricks"
check_ray((-299.5, 34.62, 5.5), (-299.5, 33, 6.5), (-300, 32, 6))
check_ray((-299.5, 34.62, 5.5), (-299.5, 33.95, 6), (-300, 33, 6))
verify_path([(-300, 33, 6), (-300, 33, 7)])
western_actions = (
    (-305, 34, "minecraft:cobweb"),
    (-307, 34, "minecraft:cobweb"),
    (-308, 34, "minecraft:cobweb"),
    (-308, 33, "minecraft:spawner"),
    (-309, 33, "minecraft:cobweb"),
    (-311, 34, "minecraft:cobweb"),
    (-311, 33, "minecraft:cobweb"),
)
previous_x = -300
for x, y, expected in western_actions:
    station_x = x + 1
    verify_path([(xx, 33, 7) for xx in range(previous_x, station_x - 1, -1)])
    target = (x, y, 7)
    assert at(c, *target)["Name"] == expected
    check_ray((station_x + 0.5, 34.62, 7.5), (x + 1, y + 0.5, 7.5), target)
    removed.add(target)
    previous_x = station_x
western_terminal_route = [(x, 33, 7) for x in range(-300, -325, -1)]
verify_path(western_terminal_route)
verify_path(list(reversed(western_terminal_route)))
print(
    "PASS final terminal rewards: south 22H; west corridor/terminal 48H return, shaft conditional"
)

# Dry overhead hall bypass; keep the rejected native lava link above unchanged.
hall_breach = []
for y in (42, 43, 44):
    target = (-288, y, 8)
    assert at(c, *target)["Name"] in {
        "minecraft:stone_bricks",
        "minecraft:mossy_stone_bricks",
        "minecraft:cracked_stone_bricks",
    }
    check_ray((-287.5, 40.62, 8.5), (-287.5, y, 8.5), target)
    removed.add(target)
    hall_breach.append(target)
verify_path([(-288, 39, 7), (-288, 39, 8)])
check_ray((-287.5, 40.62, 7.5), (-287.5, 39, 8.5), (-288, 38, 8))
check_ray((-287.5, 40.62, 7.5), (-287.5, 39.95, 8), (-288, 39, 8))
clear([-287.8, 39, 8.2, -287.2, 44.8, 8.8])
for z in range(9, 21):
    for y in (44, 43):
        target = (-288, y, z)
        assert at(c, *target)["Name"] in {"minecraft:stone", "minecraft:stone_bricks"}
        check_ray((-287.5, 44.62, z - 0.5), (-287.5, y + 0.5, z), target)
        removed.add(target)
        hall_breach.append(target)
    if z > 9:
        verify_path([(-288, 43, z - 1), (-288, 43, z)])
    else:
        clear([-287.8, 43, 8.2, -287.2, 44.8, 9.8])
target = (-288, 42, 20)
assert at(c, *target)["Name"] == "minecraft:stone_bricks"
check_ray((-287.5, 44.62, 19.5), (-287.5, 43, 20.5), target)
removed.add(target)
hall_breach.append(target)
clear([-287.8, 39, 20.2, -287.2, 44.8, 20.8])
clear([-287.8, 43, 19.2, -287.2, 44.8, 20.8])
verify_path([(-288, 39, 20), (-288, 39, 21)])
verify_path([(-288, 39, 21), (-288, 39, 20)])
check_ray((-287.5, 40.62, 21.5), (-287.5, 39, 20.5), (-288, 38, 20))
check_ray((-287.5, 40.62, 21.5), (-287.5, 39.95, 21), (-288, 39, 20))
verify_path([(-288, 43, z) for z in range(9, 20)])
verify_path([(-288, 43, z) for z in range(19, 8, -1)])
assert len(hall_breach) == 28
for x, y, z in hall_breach:
    for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        state = at(c, x + dx, y + dy, z + dz)
        assert state["Name"] not in {
            "minecraft:water",
            "minecraft:lava",
            "minecraft:gravel",
            "minecraft:sand",
        }
        assert state.get("Properties", {}).get("waterlogged", "false") == "false"
print(
    "PASS main-hall overhead link: 28 removals, eight scaffolds; native lava route still rejected"
)
