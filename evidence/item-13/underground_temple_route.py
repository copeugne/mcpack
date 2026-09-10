"""Validate declared Underground Temple links against the first retained assembly.

Geometry and conditional task accounting are scoped to the retained first assembly.
"""

# pyright: standard
# ruff: noqa: INP001, S101, ANN001, ANN201, T201, PLR2004
import gzip
import hashlib
import heapq
import importlib
import json
import math
from collections import Counter
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
removed = set()
opened_doors = set()
modeled_scaffold_feet = set()
interaction_rays = {}


clear, verify_path = importlib.import_module("evidence.item-13.temple_geometry").path_checks(
    c, removed, opened_doors, modeled_scaffold_feet
)


hall_rings = {}
hall_spokes = {}
for center_z in (0, 28):
    for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        radial = [
            (-288 + dx * radius, y, center_z + dz * radius)
            for radius, y in ((8, 39), (7, 39), (6, 38), (5, 38), (4, 37), (3, 37))
        ]
        verify_path(radial)
        verify_path(list(reversed(radial)))
        hall_spokes[(center_z, dx, dz)] = radial
    ring = (
        [(-288 + x, 37, center_z - 3) for x in range(-3, 4)]
        + [(-285, 37, center_z + z) for z in range(-2, 4)]
        + [(-288 + x, 37, center_z + 3) for x in range(2, -4, -1)]
        + [(-291, 37, center_z + z) for z in range(2, -4, -1)]
    )
    verify_path(ring)
    hall_rings[center_z] = ring
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
        interaction_rays.setdefault(target, []).append((eye, end))
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
    interaction_rays.setdefault(target, []).append((eye, end))


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

south_shaft_approach = [(x, 39, 28) for x in range(-296, -299, -1)]
verify_path(south_shaft_approach)
verify_path(list(reversed(south_shaft_approach)))
clear([-298.8, 33, 28.2, -298.2, 40.8, 28.8])
clear([-298.8, 39, 28.2, -297.2, 40.8, 28.8])
verify_path([(-299, 33, 28), (-298, 33, 28)])
verify_path([(-298, 33, 28), (-299, 33, 28)])
vein = (-299, 33, 28)
assert at(c, *vein)["Name"] == "minecraft:sculk_vein"
assert at(c, *vein)["Properties"]["down"] == "true"
check_ray((-297.5, 34.62, 28.5), (-298.5, 33.03125, 28.5), vein)
removed.add(vein)
assert at(c, -299, 32, 28)["Name"] == "minecraft:stone_bricks"
check_ray((-297.5, 34.62, 28.5), (-298.5, 33, 28.5), (-299, 32, 28))
check_ray((-297.5, 34.62, 28.5), (-298, 33.95, 28.5), (-299, 33, 28))
verify_path([(-299, 33, 28), (-300, 33, 28)])
last_source_branches = (
    (
        [(-317, 33, z) for z in range(7, -8, -1)],
        {
            (-317, 34, 1),
            (-317, 34, -1),
            (-317, 34, -2),
            (-317, 33, -2),
            (-317, 33, -3),
            (-317, 34, -5),
            (-317, 33, -5),
        },
    ),
    (
        [(x, 33, 28) for x in range(-300, -318, -1)],
        {
            (-305, 34, 28),
            (-305, 33, 28),
            (-307, 33, 28),
            (-308, 34, 28),
            (-308, 33, 28),
            (-309, 34, 28),
            (-311, 34, 28),
        },
    ),
    (
        [(-300, 33, z) for z in range(28, 46)],
        {
            (-300, 34, 33),
            (-300, 33, 33),
            (-300, 33, 35),
            (-300, 34, 36),
            (-300, 33, 36),
            (-300, 34, 37),
            (-300, 34, 39),
        },
    ),
)
for path, targets in last_source_branches:
    handled = set()
    for a, b in pairwise(path):
        for y in (34, 33):
            target = (b[0], y, b[2])
            if target in targets:
                assert at(c, *target)["Name"] in {"minecraft:cobweb", "minecraft:spawner"}
                check_ray(
                    (a[0] + 0.5, 34.62, a[2] + 0.5), (b[0] + 0.5, y + 0.5, b[2] + 0.5), target
                )
                removed.add(target)
                handled.add(target)
        verify_path([a, b])
    assert handled == targets
    verify_path(list(reversed(path)))
    print("PASS source branch", path[0], path[-1], 2 * (len(path) - 1), "horizontal return")
for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    arm = [(-317 + dx * r, 33, 28 + dz * r) for r in range(4)]
    verify_path(arm)
    verify_path(list(reversed(arm)))
assert at(c, -317, 34, -8)["Name"] == "minecraft:calcite"
spawner_positions = {
    (b["x"], b["y"], b["z"]) for b in c["block_entities"] if b["id"] == "minecraft:mob_spawner"
}
assert len(spawner_positions) == 9
assert spawner_positions <= removed
print(
    "PASS all nine saved sources have local access/removal geometry; realized encounters unmeasured"
)

# Count the union, not the sum of overlapping local demonstrations. Active mining
# alone excludes aiming, tool changes, placement, movement and encounters.
removal_counts = Counter(at(c, *position)["Name"] for position in removed)
active_ticks_by_block = {
    "minecraft:chiseled_stone_bricks": 6,
    "minecraft:cobweb": 8,
    "minecraft:cracked_stone_bricks": 6,
    "minecraft:gravel": 18,
    "minecraft:iron_bars": 19,
    "minecraft:mossy_stone_brick_stairs": 6,
    "minecraft:mossy_stone_bricks": 6,
    "minecraft:sculk_vein": 6,
    "minecraft:spawner": 19,
    "minecraft:stone": 6,
    "minecraft:stone_brick_stairs": 6,
    "minecraft:stone_bricks": 6,
    "minecraft:vine": 6,
}
active_mining_ticks = sum(
    count * active_ticks_by_block[name] for name, count in removal_counts.items()
)
print("Unique hypothetical removals:", json.dumps(dict(sorted(removal_counts.items()))))
print(
    "Construction subtotal:",
    len(removed),
    "unique removals;",
    active_mining_ticks,
    "active mining ticks;",
    active_mining_ticks / 20,
    "conditional seconds at 20 TPS",
)

native_connector_paths = {
    "upper west lava approach": [(-300, 39, z) for z in range(0, -17, -1)],
    "north junction terminal": [(x, 39, -23) for x in range(-288, -297, -1)],
    "southern hall lava approach": [(x, 39, 40) for x in range(-288, -282)],
    "lower west south lava approach": [(-300, 33, z) for z in range(7, 12)],
    "lower west north stair": [(-300, min(33, max(27, z + 31)), z) for z in range(7, -9, -1)],
    "cells east stair": [(x, min(39, max(33, -x - 225)), 28) for x in range(-280, -251)],
    "library north connector": [(-295, 27, z) for z in range(-22, -33, -1)],
    "east junction north ledge": [(-252, 33, z) for z in range(28, 13, -1)],
    "east junction east approach": [(x, 33, 28) for x in range(-252, -244)],
    "east junction south terminal": [(-252, 33, z) for z in range(28, 39)],
    "southeast connector east stub": [(x, 33, 35) for x in range(-252, -248)],
    "southeast connector west stub": [(x, 33, 35) for x in range(-252, -255, -1)],
    "library north east stub": [(x, 27, -29) for x in range(-295, -291)],
    "library north west stub": [(x, 27, -29) for x in range(-295, -298, -1)],
}
for name, path in native_connector_paths.items():
    verify_path(path)
    verify_path(list(reversed(path)))
    print(
        "PASS native connector",
        name,
        2 * (len(path) - 1),
        "horizontal return;",
        2 * sum(abs(a[1] - b[1]) for a, b in pairwise(path)),
        "vertical return",
    )
for position in ((-300, 39, -17), (-282, 39, 40), (-300, 33, 12), (-300, 27, -9)):
    assert at(c, *position)["Name"] == "minecraft:lava"
assert at(c, -297, 40, -23)["Name"] == "minecraft:calcite"
for position, name in {
    (-295, 27, -33): "minecraft:stone",
    (-298, 27, -29): "minecraft:stone_bricks",
    (-291, 27, -29): "minecraft:stone_bricks",
    (-252, 33, 39): "minecraft:calcite",
    (-248, 33, 35): "minecraft:calcite",
    (-255, 33, 35): "minecraft:stone_bricks",
    (-243, 34, 28): "minecraft:stone",
    (-244, 32, 28): "creatingspace:nickel_ore",
    (-252, 31, 13): "minecraft:air",
    (-252, 32, 13): "minecraft:sculk_vein",
    (-300, 33, 25): "minecraft:sculk",
    (-300, 33, 24): "minecraft:stone",
    (-295, 27, -18): "minecraft:stone",
    (-317, 33, 24): "minecraft:stone",
    (-317, 33, 32): "minecraft:stone",
    (-321, 33, 28): "minecraft:stone",
}.items():
    assert at(c, *position)["Name"] == name
campfire = at(c, -245, 33, 29)
assert campfire["Name"] == "minecraft:campfire"
assert campfire["Properties"]["lit"] == "true"

# Activity/fixture footprints, not claims that every enclosed voxel is playable.
# The report explains the room partition and its corridor/alcove sensitivity.
room_bounds = {
    "R01": (-295, 37, -7, -281, 41, 7),
    "R02": (-295, 37, 21, -281, 41, 35),
    "R03": (-290, 39, -35, -286, 41, -27),
    "R04": (-290, 35, -40, -286, 37, -28),
    "R05": (-290, 27, -40, -286, 29, -28),
    "R06": (-285, 27, -25, -281, 30, -19),
    "R07": (-307, 27, -32, -300, 31, -21),
    "R08": (-295, 26, -9, -281, 34, 5),
    "R09": (-278, 39, 22, -274, 40, 25),
    "R10": (-272, 39, 22, -268, 40, 25),
    "R11": (-252, 33, 5, -244, 37, 10),
    "R12": (-272, 33, -1, -264, 35, 1),
    "R13": (-312, 33, 6, -304, 35, 8),
    "R14": (-318, 33, -7, -316, 35, 2),
    "R15": (-312, 33, 27, -304, 35, 29),
    "R16": (-301, 33, 32, -299, 35, 40),
    "R17": (-296, 39, -24, -293, 41, -22),
    "R18": (-277, 33, -18, -275, 35, -15),
    "R19": (-247, 33, 27, -244, 35, 29),
    "R20": (-301, 33, 43, -299, 35, 46),
    "R21": (-278, 33, 15, -275, 35, 18),
    "R22": (-290, 39, 45, -287, 41, 48),
    "R23": (-325, 33, 5, -322, 35, 8),
    "R24": (-296, 27, -16, -293, 29, -13),
    "R25": (-283, 27, -15, -280, 29, -12),
}
room_entities = {room: Counter() for room in room_bounds}
for entity in c["block_entities"]:
    if entity["id"] not in {
        "minecraft:chest",
        "minecraft:barrel",
        "minecraft:mob_spawner",
        "minecraft:campfire",
    }:
        continue
    rooms = [
        room
        for room, bounds in room_bounds.items()
        if all(bounds[i] <= entity[axis] <= bounds[i + 3] for i, axis in enumerate("xyz"))
    ]
    assert len(rooms) == 1, (entity, rooms)
    room_entities[rooms[0]][entity["id"]] += 1
    if entity["id"] == "minecraft:campfire":
        state = at(c, entity["x"], entity["y"], entity["z"])
        assert state["Properties"]["lit"] == "true"
        assert state["Properties"]["waterlogged"] == "false"
for room, counts in room_entities.items():
    print("Activity footprint", room, dict(counts))

# Contract locally inspected transitions. This does not replace the remaining
# complete coordinate-route/phase integration or a runtime traversal observation.
graph_children = {
    "R01": ("J01", "J02", "J03", "R02"),
    "J01": ("R03", "R17"),
    "R03": ("R04",),
    "R04": ("J07",),
    "J07": ("R05", "T07"),
    "R05": ("J08",),
    "J08": ("R06", "J09", "J10"),
    "J09": ("R07", "J11", "T08"),
    "J11": ("T09", "T10"),
    "J10": ("R08", "R24", "R25"),
    "J02": ("T01", "J04"),
    "J04": ("R13", "T02", "T03"),
    "R13": ("J05",),
    "J05": ("R14", "R23"),
    "J03": ("R12", "R18", "R21"),
    "R12": ("J06",),
    "J06": ("R11", "T04", "J19"),
    "J19": ("T05", "T06"),
    "R02": ("J12", "J16", "J17"),
    "J12": ("R09", "J13"),
    "J13": ("R10", "J14"),
    "J14": ("R19", "T11", "J15"),
    "J15": ("T12", "T13"),
    "J16": ("R22", "T14"),
    "J17": ("R15", "R16"),
    "R15": ("J18",),
    "J18": ("T15", "T16", "T17"),
    "R16": ("R20",),
}
graph_edges = [(parent, child) for parent, children in graph_children.items() for child in children]
graph_nodes = {node for edge in graph_edges for node in edge}
assert {node for node in graph_nodes if node.startswith("R")} == set(room_bounds)
adjacency = {node: set() for node in graph_nodes}
for parent, child in graph_edges:
    assert child not in adjacency[parent], (parent, child)
    adjacency[parent].add(child)
    adjacency[child].add(parent)
depth = {"R01": 0}
frontier = ["R01"]
while frontier:
    following = []
    for node in frontier:
        for neighbor in sorted(adjacency[node] - depth.keys()):
            depth[neighbor] = depth[node] + 1
            following.append(neighbor)
    frontier = following
assert depth.keys() == graph_nodes
print(
    "Contracted inspected graph:",
    len(graph_nodes),
    "nodes;",
    len(graph_edges),
    "edges; one component;",
    len(graph_edges) - len(graph_nodes) + 1,
    "independent cycles",
)
print("Decision nodes:", sorted(n for n in graph_nodes if len(adjacency[n]) >= 3))
print("Leaf nodes:", sorted(n for n in graph_nodes if len(adjacency[n]) == 1))
print("Entry R01 edge depths:", json.dumps(dict(sorted(depth.items()))))
reward_depths = Counter()
source_depths = Counter()
for room, counts in room_entities.items():
    reward_depths[depth[room]] += counts["minecraft:chest"] + counts["minecraft:barrel"]
    source_depths[depth[room]] += counts["minecraft:mob_spawner"]
print("Reward assignments by contracted edge depth:", dict(sorted(reward_depths.items())))
print("Saved sources by contracted edge depth:", dict(sorted(source_depths.items())))

# Direct regression for the raw-support/hypothetical-removal boundary.
verify_path([(-288, 37, -3)])
removed.add((-288, 36, -3))
support_rejection = None
try:
    verify_path([(-288, 37, -3)])
except AssertionError as failure:
    support_rejection = failure.args
finally:
    removed.remove((-288, 36, -3))
assert support_rejection == (("removed support", (-288, 37, -3)),)
print("PASS hypothetical removed support is rejected; original scenario restored")

east_excursion = [(-276, 33, 0)]
east_excursion_parts = []
for sign in (-1, 1):
    branch = [(-276, 33, sign * z) for z in range(18)]
    east_excursion_parts.extend((branch, list(reversed(branch))))
enchanting_visit = [(-248, 33, z) for z in range(7)] + room_route[1:]
east_excursion_parts.extend(
    (
        east,
        enchanting_visit,
        list(reversed(enchanting_visit)),
        north_arm,
        rim,
        pit,
        list(reversed(pit)),
        list(reversed(north_arm)),
        east_link,
    )
)
for arm in terminal_arms:
    east_excursion_parts.extend((arm, list(reversed(arm))))
east_excursion_parts.extend((list(reversed(east_link)), list(reversed(east))))
for part in east_excursion_parts:
    assert east_excursion[-1] == part[0], (east_excursion[-1], part[0])
    east_excursion.extend(part[1:])
assert east_excursion[-1] == east_excursion[0]
verify_path(east_excursion)
print(
    "PASS joined eastern excursion:",
    len(east_excursion) - 1,
    "horizontal blocks;",
    sum(abs(a[1] - b[1]) for a, b in pairwise(east_excursion)),
    "vertical blocks; start/end J03",
)

hole_plan_positions = {position for position, _, _ in dungeon_sources}
post_mining_entry, post_mining_ring = (
    [(x, 26 if (x, z) in hole_plan_positions else y, z) for x, y, z in path]
    for path in (dungeon_entry, dungeon_ring)
)
post_mining_dungeon = (
    post_mining_entry + post_mining_ring[1:] + list(reversed(post_mining_entry))[1:]
)
assert post_mining_dungeon[0] == post_mining_dungeon[-1] == (-288, 27, -14)
verify_path(post_mining_dungeon)
verify_path(list(reversed(post_mining_dungeon)))
print(
    "PASS post-mining dungeon survey:",
    len(post_mining_dungeon) - 1,
    "horizontal blocks;",
    sum(abs(a[1] - b[1]) for a, b in pairwise(post_mining_dungeon)),
    "vertical blocks; no hole refill",
)

west_excursion_parts = [
    western_terminal_route[:18],
    last_source_branches[0][0],
    list(reversed(last_source_branches[0][0])),
    western_terminal_route[17:],
    list(reversed(western_terminal_route)),
]
for name in ("lower west south lava approach", "lower west north stair"):
    path = native_connector_paths[name]
    west_excursion_parts.extend((path, list(reversed(path))))
southwest_excursion_parts = [last_source_branches[1][0]]
for dx, dz in ((0, -1), (0, 1), (-1, 0)):
    arm = [(-317 + dx * r, 33, 28 + dz * r) for r in range(4)]
    southwest_excursion_parts.extend((arm, list(reversed(arm))))
southwest_excursion_parts.extend(
    (
        list(reversed(last_source_branches[1][0])),
        last_source_branches[2][0],
        list(reversed(last_source_branches[2][0])),
    )
)
lower_excursions = {}
for name, parts in (
    ("western lower J04", west_excursion_parts),
    ("southwestern lower J17", southwest_excursion_parts),
):
    joined = [parts[0][0]]
    for part in parts:
        assert joined[-1] == part[0], (joined[-1], part[0])
        joined.extend(part[1:])
    assert joined[0] == joined[-1]
    verify_path(joined)
    lower_excursions[name] = joined
    print(
        "PASS joined excursion",
        name,
        len(joined) - 1,
        "horizontal blocks;",
        sum(abs(a[1] - b[1]) for a, b in pairwise(joined)),
        "vertical blocks",
    )

scaffold_columns = (
    (-277, 0, 33, 39),
    (-300, 6, 33, 39),
    (-299, 28, 33, 39),
    (-288, -38, 35, 39),
    (-287, -30, 31, 35),
    (-288, -38, 27, 31),
    (-302, -25, 27, 30),
    (-305, -25, 27, 30),
    (-288, 8, 39, 43),
    (-288, 20, 39, 43),
)
assert sum(top - base for _, _, base, top in scaffold_columns) == 44
for x, z, base, top in scaffold_columns:
    verify_path([(x, base, z)])
    clear([x + 0.2, base, z + 0.2, x + 0.8, top + 1.8, z + 0.8])
for x, z, base, top in scaffold_columns:
    modeled_scaffold_feet.update((x, y, z) for y in range(base, top + 1))
assert all((-288, y, -38) not in modeled_scaffold_feet for y in range(32, 35))
column_gap_rejected = False
try:
    verify_path([(-288, 31, -38), (-288, 32, -38)])
except AssertionError:
    column_gap_rejected = True
assert column_gap_rejected

bedroom_entry = [(-288, 27, -22), *bedroom_crossing]
library_link = [(x, 27, -22) for x in range(-288, -296, -1)]
lower_activity_parts = [
    bedroom_entry,
    bedroom_aisle,
    list(reversed(bedroom_entry)),
    library_link,
    library_front[:10],
]
for x in (-302, -305):
    approach = (
        [(-304, 27, -22), (-303, 27, -22), (-302, 27, -22), (-302, 27, -23), (-302, 27, -24)]
        if x == -302
        else [(-304, 27, -22), (-304, 27, -23), (-305, 27, -23), (-305, 27, -24)]
    )
    column_visit = [(x, 27, -24)] + [(x, y, -25) for y in range(27, 31)]
    lower_activity_parts.extend((approach, column_visit))
    lower_activity_parts.append(list(reversed(column_visit))[:4])
    if x == -302:
        lower_activity_parts.append(library_aisles)
    lower_activity_parts.extend(([(x, 27, -25), (x, 27, -24)], list(reversed(approach))))
lower_activity_parts.append(library_front[9:])
library_north = native_connector_paths["library north connector"]
lower_activity_parts.append(library_north[:8])
for name in ("library north east stub", "library north west stub"):
    path = native_connector_paths[name]
    lower_activity_parts.extend((path, list(reversed(path))))
library_south = [(-295, 27, z) for z in range(-22, -18)]
dungeon_link = [(-288, 27, z) for z in range(-22, -13)]
lower_activity_parts.extend(
    (
        library_north[7:],
        list(reversed(library_north)),
        library_south,
        list(reversed(library_south)),
        list(reversed(library_link)),
        dungeon_link,
    )
)
for direction in (-1, 1):
    terminal = [(-288 + direction * r, 27, -14) for r in range(8)]
    lower_activity_parts.extend((terminal, list(reversed(terminal))))
lower_activity_parts.extend((post_mining_dungeon, list(reversed(dungeon_link))))
lower_activity_route = [(-288, 27, -22)]
for part in lower_activity_parts:
    assert lower_activity_route[-1] == part[0], (lower_activity_route[-1], part[0])
    lower_activity_route.extend(part[1:])
assert lower_activity_route[-1] == lower_activity_route[0]
verify_path(lower_activity_route)
for (x, z), _, (sx, sz) in dungeon_sources:
    check_ray((x + 0.5, 27.62, z + 0.5), (sx + 0.5, 27.5, sz + 0.5), (sx, 27, sz))
print(
    "PASS joined lower activity circuit:",
    sum(abs(a[0] - b[0]) + abs(a[2] - b[2]) for a, b in pairwise(lower_activity_route)),
    "horizontal blocks;",
    sum(abs(a[1] - b[1]) for a, b in pairwise(lower_activity_route)),
    "vertical blocks; start/end J08",
)

tower_first_shaft = (
    [(-288, 39, -37)] + [(-288, y, -38) for y in range(39, 34, -1)] + [(-288, 35, -37)]
)
tower_second_shaft = (
    [(-287, 35, -29)] + [(-287, y, -30) for y in range(35, 30, -1)] + [(-287, 31, -29)]
)
tower_third_shaft = [(-288, y, -38) for y in range(31, 26, -1)] + [(-288, 27, -37)]
tower_lower_link = [(-288, 27, z) for z in range(-25, -21)]
tower_prefix = (
    tower_approach,
    tower_crossing,
    tower_rewards,
    hatch_approach,
    tower_first_shaft,
    middle_route,
    tower_second_shaft,
)
tower_suffix = (tower_third_shaft, bottom_zigzag, tower_lower_link)
tower_transit = [(-288, 39, -23)]
for part in (*tower_prefix, lower_tower, *tower_suffix):
    assert tower_transit[-1] == part[0], (tower_transit[-1], part[0])
    tower_transit.extend(part[1:])
tower_circuit = [(-288, 39, -23)]
for part in (
    *tower_prefix,
    lower_tower[:7],
    descending_branch,
    terminal_rim,
    list(reversed(descending_branch)),
    lower_tower[6:],
    *tower_suffix,
    lower_activity_route,
    list(reversed(tower_transit)),
):
    assert tower_circuit[-1] == part[0], (tower_circuit[-1], part[0])
    tower_circuit.extend(part[1:])
assert tower_circuit[-1] == tower_circuit[0]
verify_path(tower_circuit)
print(
    "PASS joined tower/lower activity circuit:",
    sum(abs(a[0] - b[0]) + abs(a[2] - b[2]) for a, b in pairwise(tower_circuit)),
    "horizontal blocks;",
    sum(abs(a[1] - b[1]) for a, b in pairwise(tower_circuit)),
    "vertical blocks; start/end J01",
)


def join_route_parts(parts):
    """Join existing path coordinates without teleporting across part seams."""
    joined = [parts[0][0]]
    for part in parts:
        assert joined[-1] == part[0], (joined[-1], part[0])
        joined.extend(part[1:])
    return joined


hall_ports = {}
anchored_rings = {}
for center_z, ring in hall_rings.items():
    anchor = (-288, 37, center_z - 3)
    ring_open = ring[:-1]
    offset = ring_open.index(anchor)
    ring_open = ring_open[offset:] + ring_open[:offset]
    anchored_rings[center_z] = [*ring_open, anchor]
    for dx, dz in ((0, -1), (1, 0), (0, 1), (-1, 0)):
        spoke = hall_spokes[(center_z, dx, dz)]
        index = ring_open.index(spoke[-1])
        inner = min((ring_open[: index + 1], [anchor, *reversed(ring_open[index:])]), key=len)
        hall_ports[(center_z, dx, dz)] = join_route_parts((inner, list(reversed(spoke))))

cell_circuit_parts = []
for x, inside in cell_routes:
    entry = [(xx, 39, 28) for xx in range(-280, x + 1)] + [(x, 39, z) for z in (27, 26, 25)]
    cell_circuit_parts.extend((entry, inside, list(reversed(inside)), list(reversed(entry))))
cell_stairs = native_connector_paths["cells east stair"]
cell_circuit_parts.append(cell_stairs)
for name in ("east junction north ledge", "east junction east approach"):
    path = native_connector_paths[name]
    cell_circuit_parts.extend((path, list(reversed(path))))
southeast_terminal = native_connector_paths["east junction south terminal"]
cell_circuit_parts.append(southeast_terminal[:8])
for name in ("southeast connector east stub", "southeast connector west stub"):
    path = native_connector_paths[name]
    cell_circuit_parts.extend((path, list(reversed(path))))
cell_circuit_parts.extend(
    (southeast_terminal[7:], list(reversed(southeast_terminal)), list(reversed(cell_stairs)))
)
cell_circuit = join_route_parts(cell_circuit_parts)
assert cell_circuit[0] == cell_circuit[-1] == (-280, 39, 28)

north_hall_link = [(-288, 39, z) for z in range(-8, -24, -1)]
east_shaft_link = join_route_parts(
    (ledge, [(-278, 39, 0), *[(-277, y, 0) for y in range(39, 32, -1)], (-276, 33, 0)])
)
west_shaft_link = join_route_parts(
    (upper_west, [(-300, 39, 5), *[(-300, y, 6) for y in range(39, 32, -1)], (-300, 33, 7)])
)
southwest_shaft_link = join_route_parts(
    (
        south_shaft_approach,
        [(-298, 39, 28), *[(-299, y, 28) for y in range(39, 32, -1)], (-300, 33, 28)],
    )
)
overhead_link = (
    [(-288, y, 8) for y in range(39, 44)]
    + [(-288, 43, z) for z in range(9, 21)]
    + [(-288, y, 20) for y in range(42, 38, -1)]
)
between_halls = join_route_parts(
    (hall_ports[(0, 0, 1)], overhead_link, list(reversed(hall_ports[(28, 0, -1)])))
)
whole_circuit_parts = [anchored_rings[0], hall_ports[(0, 0, -1)], north_hall_link]
terminal = native_connector_paths["north junction terminal"]
whole_circuit_parts.extend(
    (
        terminal,
        list(reversed(terminal)),
        tower_circuit,
        list(reversed(north_hall_link)),
        list(reversed(hall_ports[(0, 0, -1)])),
        hall_ports[(0, -1, 0)],
        west,
    )
)
upper_lava = native_connector_paths["upper west lava approach"]
whole_circuit_parts.extend(
    (
        upper_lava,
        list(reversed(upper_lava)),
        west_shaft_link,
        lower_excursions["western lower J04"],
        list(reversed(west_shaft_link)),
        list(reversed(west)),
        list(reversed(hall_ports[(0, -1, 0)])),
        hall_ports[(0, 1, 0)],
        east_shaft_link,
        east_excursion,
        list(reversed(east_shaft_link)),
        list(reversed(hall_ports[(0, 1, 0)])),
        between_halls,
        anchored_rings[28],
        hall_ports[(28, 1, 0)],
        cell_circuit,
        list(reversed(hall_ports[(28, 1, 0)])),
        hall_ports[(28, 0, 1)],
        south_terminal[:5],
    )
)
south_lava = native_connector_paths["southern hall lava approach"]
whole_circuit_parts.extend(
    (
        south_lava,
        list(reversed(south_lava)),
        south_terminal[4:],
        list(reversed(south_terminal)),
        list(reversed(hall_ports[(28, 0, 1)])),
        hall_ports[(28, -1, 0)],
        southwest_shaft_link,
        lower_excursions["southwestern lower J17"],
        list(reversed(southwest_shaft_link)),
        list(reversed(hall_ports[(28, -1, 0)])),
        list(reversed(between_halls)),
    )
)
whole_circuit = join_route_parts(whole_circuit_parts)
assert whole_circuit[0] == whole_circuit[-1] == (-288, 37, -3)
verify_path(whole_circuit)
whole_horizontal = sum(abs(a[0] - b[0]) + abs(a[2] - b[2]) for a, b in pairwise(whole_circuit))
whole_ascent = sum(max(0, b[1] - a[1]) for a, b in pairwise(whole_circuit))
whole_descent = sum(max(0, a[1] - b[1]) for a, b in pairwise(whole_circuit))
print(
    "PASS complete post-construction movement circuit:",
    whole_horizontal,
    "horizontal blocks;",
    whole_ascent,
    "ascent;",
    whole_descent,
    "descent; feet range",
    min(p[1] for p in whole_circuit),
    max(p[1] for p in whole_circuit),
)
visited = set(whole_circuit)
visited_rooms = {
    room
    for room, bounds in room_bounds.items()
    if any(all(bounds[i] <= point[i] <= bounds[i + 3] for i in range(3)) for point in visited)
}
assert visited_rooms == set(room_bounds)
reward_positions = {
    (entity["x"], entity["y"], entity["z"])
    for entity in c["block_entities"]
    if entity["id"] in {"minecraft:chest", "minecraft:barrel"}
}
reward_rays = {
    target: rays for target, rays in interaction_rays.items() if target in reward_positions
}
assert reward_rays.keys() == reward_positions
scaffold_blocks = {(x, y, z) for x, z, base, top in scaffold_columns for y in range(base, top)}
reward_stations = {}
for target, rays in reward_rays.items():
    accepted = []
    for eye, end in rays:
        station = (math.floor(eye[0]), round(eye[1] - 1.62, 6), math.floor(eye[2]))
        if station not in visited:
            continue
        ray_cells = {
            tuple(math.floor(eye[i] + (end[i] - eye[i]) * step / 2000) for i in range(3))
            for step in range(2001)
        }
        if ray_cells.isdisjoint(scaffold_blocks):
            accepted.append(station)
    assert accepted, ("no visited unobstructed reward station", target)
    reward_stations[target] = set(accepted)
print("PASS full movement circuit visits all 25 activity footprints and all 31 reward ray stations")

# Validate forward western source access before removing its local obstructions.
before_western_access = removed.copy()
try:
    removed.difference_update({(-291, 27, -2), (-291, 26, -2), (-290, 26, -2)})
    verify_path([(-291, 27, -1)])
    eye = (-290.5, 28.62, -0.5)
    check_ray(eye, (-290.5, 27.03125, -1.5), (-291, 27, -2))
    removed.add((-291, 27, -2))
    check_ray(eye, (-290.5, 27, -1.5), (-291, 26, -2))
    removed.add((-291, 26, -2))
    verify_path([(-291, 27, -1), (-291, 26, -2)])
    check_ray((-290.5, 27.62, -1.5), (-290, 26.5, -1.5), (-290, 26, -2))
finally:
    removed.clear()
    removed.update(before_western_access)

shaft_placement_detours = {
    (-277, 33, 0): (-278, 33, 0),
    (-300, 33, 6): (-300, 33, 5),
    (-299, 33, 28): (-298, 33, 28),
}
inserted_placement_detours = set()
southern_floor_detours = 0
work_route = [whole_circuit[0]]
for a, b in pairwise(whole_circuit):
    if a == (-287, 27, 1) and b == (-288, 26, 1):
        work_route.extend(((-287, 27, 2), (-288, 27, 2)))
        southern_floor_detours += 1
    work_route.append(b)
    if b in shaft_placement_detours and b not in inserted_placement_detours:
        work_route.extend((shaft_placement_detours[b], b))
        inserted_placement_detours.add(b)
assert inserted_placement_detours == shaft_placement_detours.keys()
assert southern_floor_detours == 1
assert work_route[0] == work_route[-1] == whole_circuit[0]
verify_path(work_route)
work_visited = set(work_route)
assert visited <= work_visited
assert all(station in work_visited for station in shaft_placement_detours.values())
for target in removed:
    assert target in interaction_rays, ("missing construction ray", target)
    stations = {
        (math.floor(eye[0]), round(eye[1] - 1.62, 6), math.floor(eye[2]))
        for eye, _ in interaction_rays[target]
    }
    assert stations & work_visited, ("missing construction station", target, stations)
work_horizontal = sum(abs(a[0] - b[0]) + abs(a[2] - b[2]) for a, b in pairwise(work_route))
work_ascent = sum(max(0, b[1] - a[1]) for a, b in pairwise(work_route))
work_descent = sum(max(0, a[1] - b[1]) for a, b in pairwise(work_route))
print(
    "PASS route with construction stations:",
    work_horizontal,
    "horizontal blocks;",
    work_ascent,
    "ascent;",
    work_descent,
    "descent; all 112 removal targets have a visited ray station",
)

initial_fall_columns = (
    (-277, 0, 33, 39),
    (-300, 6, 33, 39),
    (-299, 28, 33, 39),
    (-288, -38, 35, 39),
    (-287, -30, 31, 35),
    (-288, -38, 27, 31),
    (-288, 20, 39, 43),
)
for x, z, base, top in initial_fall_columns:
    descent = [(x, y, z) for y in range(top, base - 1, -1)]
    matches = [
        i
        for i in range(len(work_route) - len(descent) + 1)
        if work_route[i : i + len(descent)] == descent
    ]
    assert len(matches) == 1, (descent, matches)
fall_ticks_by_height = {}
for height in (4, 6):
    velocity = 0.0
    distance = 0.0
    ticks = 0
    while distance < height:
        distance -= velocity
        ticks += 1
        velocity = (velocity - 0.08) * 0.9800000190734863
    fall_ticks_by_height[height] = ticks
fall_vertical = sum(top - base for _, _, base, top in initial_fall_columns)
fall_ticks = sum(fall_ticks_by_height[top - base] for _, _, base, top in initial_fall_columns)
step_vectors = [tuple(b[i] - a[i] for i in range(3)) for a, b in pairwise(work_route)]
direction_changes = sum(a != b for a, b in pairwise(step_vectors))
combat_groups = 6
decisions = direction_changes + 1 + 2 * combat_groups
button_operations = 2 * sum(
    at(c, *position)["Properties"]["half"] == "lower" for position in opened_doors
)
mining_operations = len(removed)
placement_operations = len(scaffold_blocks)
acquisitions = len(reward_positions)
interaction_operations = mining_operations + placement_operations + button_operations + acquisitions
tool_selections = (
    mining_operations + len(scaffold_columns) + combat_groups + button_operations + acquisitions
)
print(
    "P6 action counts:",
    direction_changes,
    "direction changes;",
    decisions,
    "decisions;",
    interaction_operations,
    "interaction inputs;",
    tool_selections,
    "tool selections;",
    acquisitions,
    "acquisitions",
)
print("Nominal initial fall ticks:", fall_ticks_by_height, "total", fall_ticks)
for label, u, j, n, a, s, k, v, duty in (
    ("A", 5, 1, 0.5, 0.25, 0.25, 1, 2, 1),
    ("B", 4, 0.5, 1, 0.5, 0.5, 2, 4, 0.75),
    ("C", 3, 0.25, 1.5, 1, 1, 4, 8, 0.5),
):
    movement = (
        (work_horizontal - 6) / u
        + 6 / 3
        + (work_ascent + work_descent - fall_vertical) / j
        + fall_ticks / 20
    )
    noncombat = (
        movement
        + active_mining_ticks / 20
        + decisions * n
        + interaction_operations * a
        + tool_selections * s
        + acquisitions * k
        + v
    )
    combat = 2028 / 20 / duty
    print(
        "P6 complete conditional seconds",
        label,
        "noncombat",
        noncombat,
        "combat",
        combat,
        "total",
        noncombat + combat,
    )


# Scoped shortest depth on checked transitions, after the declared remedies.
route_edges = {point: {} for point in work_visited}
for a, b in pairwise(work_route):
    weight = sum(abs(a[i] - b[i]) for i in range(3))
    if a != b:
        route_edges[a][b] = weight
station_depth = {work_route[0]: 0}
queue = [(0, work_route[0])]
while queue:
    cost, point = heapq.heappop(queue)
    if cost != station_depth[point]:
        continue
    for neighbor, weight in route_edges[point].items():
        candidate = cost + weight
        if candidate < station_depth.get(neighbor, math.inf):
            station_depth[neighbor] = candidate
            heapq.heappush(queue, (candidate, neighbor))
assert station_depth.keys() == work_visited
for room, bounds in room_bounds.items():
    room_depth = min(
        distance
        for point, distance in station_depth.items()
        if all(bounds[i] <= point[i] <= bounds[i + 3] for i in range(3))
    )
    print("Scoped shortest room-footprint blocks", room, room_depth)
for target, stations in sorted(reward_stations.items()):
    print("Scoped shortest reward-station blocks", target, min(station_depth[p] for p in stations))
print("Scoped deepest checked station", max(station_depth.values()))
