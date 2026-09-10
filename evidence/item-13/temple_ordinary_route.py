"""Validate the second retained temple assembly with explicit local paths."""

# pyright: standard
# ruff: noqa: INP001, S101, T201, PLR2004
import gzip
import hashlib
import importlib
import json
from itertools import pairwise
from pathlib import Path

raw = (
    Path(__file__).parent / "fixed-blocks/explorations-underground-temple-ordinary-r1.json.gz"
).read_bytes()
assert (
    hashlib.sha256(raw).hexdigest()
    == "faed7df352cdcfc1938fb4d49f4f84b2519ad4f1ee55044fa661ae55e6f81d5c"
)
case = json.loads(gzip.decompress(raw))["cases"][0]
at = importlib.import_module("evidence.item-13.render_pilot").state_at
clear, verify = importlib.import_module("evidence.item-13.temple_geometry").path_checks(
    case, set(), set(), set()
)
slabs = []
for y in range(8, 25):
    for x in range(195, 198):
        for z in range(341, 344):
            state = at(case, x, y, z)
            if state["Name"] == "minecraft:deepslate_brick_slab":
                assert state["Properties"] == {"type": "bottom", "waterlogged": "true"}
                assert at(case, x, y + 1, z)["Name"] == "minecraft:air"
                slabs.append((x, y, z))
assert len(slabs) == 17
assert [p[1] for p in slabs] == list(range(8, 25))
print("Saved wet spiral slabs", slabs)
try:
    verify([(195, 25, 342)])
except AssertionError:
    print("PASS dry integer-floor model rejects the wet bottom-slab support")
else:
    message = "unsupported wet bottom slab incorrectly treated as full floor"
    raise AssertionError(message)

spokes = {}
for dx, dz in ((0, -1), (1, 0), (0, 1), (-1, 0)):
    path = [
        (208 + dx * r, y, 384 + dz * r)
        for r, y in ((8, 32), (7, 32), (6, 31), (5, 31), (4, 30), (3, 30))
    ]
    verify(path)
    verify(list(reversed(path)))
    spokes[(dx, dz)] = path
ring = (
    [(208 + x, 30, 381) for x in range(-3, 4)]
    + [(211, 30, 384 + z) for z in range(-2, 4)]
    + [(208 + x, 30, 387) for x in range(2, -4, -1)]
    + [(205, 30, 384 + z) for z in range(2, -4, -1)]
)
verify(ring)
verify(list(reversed(ring)))
print("PASS ordinary hall four bidirectional spokes and 24-block inner circuit")
chamber_approach = [(208, 32, z) for z in range(376, 369, -1)]
verify(chamber_approach)
verify(list(reversed(chamber_approach)))
print("PASS north chamber approach, six horizontal blocks each way")

rays = {}
check_ray = importlib.import_module("evidence.item-13.temple_geometry").ray_check(case, set(), rays)
for dx, dz in ((0, -1), (1, 0), (0, 1), (-1, 0)):
    target = (208 + dx, 30, 384 + dz)
    station = (208 + 3 * dx, 30, 384 + 3 * dz)
    assert at(case, *target)["Name"] == "minecraft:chest"
    assert at(case, target[0], 31, target[2])["Name"] == "minecraft:air"
    check_ray(
        (station[0] + 0.5, 31.62, station[2] + 0.5),
        (target[0] + 0.5, 30.5, target[2] + 0.5),
        target,
    )
assert at(case, 208, 30, 384)["Name"] == "minecraft:gold_block"
chamber_ring = (
    [(x, 32, 370) for x in range(208, 212)]
    + [(211, 32, z) for z in range(369, 363, -1)]
    + [(x, 32, 364) for x in range(210, 204, -1)]
    + [(205, 32, z) for z in range(365, 371)]
    + [(x, 32, 370) for x in range(206, 209)]
)
verify(chamber_ring)
verify(list(reversed(chamber_ring)))
for dx, dz in ((0, -1), (1, 0), (0, 1), (-1, 0)):
    target = (208 + 2 * dx, 32, 367 + 2 * dz)
    station = (208 + 3 * dx, 32, 367 + 3 * dz)
    assert at(case, *target)["Name"] == "minecraft:chest"
    assert at(case, target[0], 33, target[2])["Name"] == "minecraft:air"
    check_ray(
        (station[0] + 0.5, 33.62, station[2] + 0.5),
        (target[0] + 0.5, 32.5, target[2] + 0.5),
        target,
    )
chamber_survey = chamber_approach + chamber_ring[1:] + list(reversed(chamber_approach))[1:]
verify(chamber_survey)
assert len(chamber_survey) - 1 == 36
assert len(rays) == 8
print("PASS eight chest rays; native chamber survey 36 horizontal blocks, zero vertical")


_, slab_verify = importlib.import_module("evidence.item-13.temple_geometry").path_checks(
    case, set(), set(), set(), bottom_slabs=set(slabs)
)
slab_stations = [(x, y + 0.5, z) for x, y, z in slabs]
slab_verify(slab_stations)
slab_verify(list(reversed(slab_stations)))
print("PASS wet slab geometry: 17 stations, 16 horizontal and 16 vertical blocks each way")

try:
    verify([slab_stations[0]])
except AssertionError:
    print("PASS fractional support remains rejected without explicit slab declaration")
else:
    message = "fractional support leaked into the default dry checker"
    raise AssertionError(message)

# Alternative solid-clearance model, not a dry or runtime movement assertion.
# Removed waterlogged slabs can release water; see the report's fluid limitation.
shaft_removals = {(195, 15, 343), (195, 23, 343)}
shaft_feet = {(195, y, 343) for y in range(8, 27)}
shaft_clear, shaft_verify = importlib.import_module("evidence.item-13.temple_geometry").path_checks(
    case, shaft_removals, set(), shaft_feet
)
assert at(case, 195, 7, 343)["Name"] == "minecraft:stone_bricks"
for y in range(8, 29):
    assert at(case, 195, y, 343)["Name"] == (
        "minecraft:deepslate_brick_slab" if (195, y, 343) in shaft_removals else "minecraft:air"
    )
shaft_path = [(194, 8, 343), *[(195, y, 343) for y in range(8, 27)], (194, 26, 343)]
shaft_verify(shaft_path)
shaft_verify(list(reversed(shaft_path)))
for retained_slab in shaft_removals:
    _, reject_uncleared = importlib.import_module("evidence.item-13.temple_geometry").path_checks(
        case, shaft_removals - {retained_slab}, set(), shaft_feet
    )
    try:
        reject_uncleared(shaft_path)
    except AssertionError:
        print("PASS uncleared shaft obstruction rejected", retained_slab)
    else:
        message = "uncleared waterlogged slab was ignored by construction geometry"
        raise AssertionError(message)

shaft_rays = {}
shaft_ray = importlib.import_module("evidence.item-13.temple_geometry").ray_check(
    case, shaft_removals, shaft_rays
)
for feet_y, target_y in ((13, 15), (21, 23)):
    # Stop the supported column below the overhead target, before extending it.
    assert (195, target_y, 343) in shaft_removals
    shaft_ray((195.5, feet_y + 1.62, 343.5), (195.5, target_y, 343.5), (195, target_y, 343))
    # North offset permits an ordinary side click on the current top scaffold.
    # Its 0.1 block overlap retains top support under the existing scaffold model.
    shaft_clear([195.2, feet_y, 342.5, 195.8, feet_y + 1.8, 343.8])
    shaft_ray(
        (195.5, feet_y + 1.62, 342.8),
        (195.5, feet_y - 0.05, 343),
        (195, feet_y - 1, 343),
    )
shaft_ray((194.5, 9.62, 343.5), (195, 8.95, 343.5), (195, 8, 343))
print(
    "PASS shaft construction solid geometry: two removals, 18 scaffold placements in 5/8/5 stages; "
    "6.8 horizontal and 36 vertical blocks including two placement offsets; fluid motion unresolved"
)

shaft_upper_link = (
    [(194, 26, z) for z in range(343, 345)]
    + [(x, 26, 344) for x in range(195, 197)]
    + [(196, max(26, min(32, z - 322)), z) for z in range(345, 358)]
)
shaft_chamber_link = (
    [(196, 32, z) for z in range(357, 368)]
    + [(x, 32, 367) for x in range(197, 206)]
    + [(205, 32, z) for z in range(368, 371)]
    + [(x, 32, 370) for x in range(206, 209)]
    + [(208, 32, z) for z in range(371, 377)]
)
upper_access = shaft_upper_link + shaft_chamber_link[1:]
verify(upper_access)
verify(list(reversed(upper_access)))
assert len(upper_access) - 1 == 47
print("PASS shaft upper landing to hall north threshold: 47 horizontal, six ascent blocks")
false_south_link = [(196, 32, z) for z in range(374, 385)]
south_rejection = None
try:
    verify(false_south_link)
except AssertionError as error:
    south_rejection = error.args[0]
else:
    message = "water-filled inter-piece gap was accepted as a supported dry connection"
    raise AssertionError(message)
assert south_rejection == (
    (196, 32, 378),
    {"Name": "minecraft:water", "Properties": {"level": "0"}},
)
print("REJECT false south dry connection: water support at (196,31,378)")
for z in range(378, 381):
    for y in range(31, 35):
        assert at(case, 196, y, z) == {
            "Name": "minecraft:water",
            "Properties": {"level": "0"},
        }
assert all(at(case, 196, y, 377)["Name"] == "minecraft:air" for y in range(32, 35))
assert [at(case, 196, y, 381)["Name"] for y in range(32, 35)] == [
    "minecraft:stone_bricks",
    "minecraft:chiseled_stone_bricks",
    "minecraft:stone_bricks",
]

# Supported post-removal chamber circuit, with source and reward work at side stations.
chamber_work = (
    ((207, 32, 370), (208, 31, 370), (208, 31, 369)),
    ((205, 32, 366), (205, 31, 367), (206, 31, 367)),
    ((207, 32, 364), (208, 31, 364), (208, 31, 365)),
    ((211, 32, 366), (211, 31, 367), (210, 31, 367)),
)
chamber_removed = set()
work_rays = {}
work_ray = importlib.import_module("evidence.item-13.temple_geometry").ray_check(
    case, chamber_removed, work_rays
)
_, work_verify = importlib.import_module("evidence.item-13.temple_geometry").path_checks(
    case, chamber_removed, set(), set()
)
for station, floor, source in chamber_work:
    work_verify([station])
    eye = (station[0] + 0.5, 33.62, station[2] + 0.5)
    assert at(case, *floor)["Name"] in {
        "minecraft:stone_bricks",
        "minecraft:mossy_stone_bricks",
        "minecraft:cracked_stone_bricks",
    }
    assert at(case, floor[0], 30, floor[2])["Name"] == "minecraft:water"
    work_ray(eye, (floor[0] + 0.5, 31.999, floor[2] + 0.5), floor)
    chamber_removed.add(floor)
    assert at(case, *source)["Name"] == "minecraft:spawner"
    work_ray(
        eye,
        (
            (floor[0] + source[0]) / 2 + 0.5 + (source[0] - floor[0]) * 0.001,
            31.5,
            (floor[2] + source[2]) / 2 + 0.5 + (source[2] - floor[2]) * 0.001,
        ),
        source,
    )
    chamber_removed.add(source)
    chest = (source[0], 32, source[2])
    assert at(case, *chest)["Name"] == "minecraft:chest"
    assert at(case, chest[0], 33, chest[2])["Name"] == "minecraft:air"
    work_ray(eye, (chest[0] + 0.5, 32.5, chest[2] + 0.5), chest)

outer_ring = (
    [(x, 32, 371) for x in range(208, 203, -1)]
    + [(204, 32, z) for z in range(370, 362, -1)]
    + [(x, 32, 363) for x in range(205, 213)]
    + [(212, 32, z) for z in range(364, 372)]
    + [(x, 32, 371) for x in range(211, 207, -1)]
)
detours = dict(
    zip(
        ((207, 32, 371), (204, 32, 366), (207, 32, 363), (212, 32, 366)),
        (station for station, _, _ in chamber_work),
        strict=True,
    )
)
work_circuit = []
for point in outer_ring:
    work_circuit.append(point)
    if point in detours:
        work_circuit.extend((detours[point], point))
assert len(work_circuit) - 1 == 40
work_verify(work_circuit)
work_verify(list(reversed(work_circuit)))
work_approach = [(208, 32, z) for z in range(376, 370, -1)]
complete_chamber = (
    work_approach + work_circuit[1:] + work_circuit[1:] + list(reversed(work_approach))[1:]
)
work_verify(complete_chamber)
assert len(complete_chamber) - 1 == 90
assert set(detours.values()) <= set(complete_chamber)
assert len(work_rays) == 12
for _, floor, _ in chamber_work:
    try:
        work_verify([(floor[0], 32, floor[2])])
    except AssertionError:
        continue
    message = "chamber circuit allowed standing on a removed exposure floor"
    raise AssertionError(message)
print("PASS four supported source/loot stations; eight removals; 90H complete local task route")

entities_by_position = {(e["x"], e["y"], e["z"]): e for e in case["block_entities"]}
for (_, _, source), enemy in zip(
    chamber_work, ("skeleton", "witch", "spider", "zombie"), strict=True
):
    saved = entities_by_position[source]
    assert saved["id"] == "minecraft:mob_spawner"
    assert saved["SpawnData"] == {"entity": {"id": "minecraft:" + enemy}}
    assert saved["SpawnPotentials"] == []
    for key, value in {
        "Delay": 0,
        "MaxNearbyEntities": 6,
        "MinSpawnDelay": 200,
        "MaxSpawnDelay": 800,
        "RequiredPlayerRange": 16,
        "SpawnCount": 4,
        "SpawnRange": 4,
    }.items():
        assert saved[key] == value
    saved_chest = entities_by_position[(source[0], 32, source[2])]
    assert saved_chest["LootTable"] == "explorations:chests/underground_temple/dungeon"
    assert "Items" not in saved_chest
    assert "Lock" not in saved_chest

directions = [(b[0] - a[0], b[2] - a[2]) for a, b in pairwise(complete_chamber)]
turns = sum(a != b for a, b in pairwise(directions))
nav_events = turns + 11
print("Chamber direction changes", turns, "navigation events including task choices", nav_events)
combat_work = 6 * (5 + 3 + 4 + 4) * 13 / 20
assert combat_work == 62.4
for label, u, n, a, s, k, v, d in (
    ("A", 5, 0.5, 0.25, 0.25, 1, 2, 1),
    ("B", 4, 1, 0.5, 0.5, 2, 4, 0.75),
    ("C", 3, 1.5, 1, 1, 4, 8, 0.5),
):
    noncombat = 90 / u + 5 + nav_events * n + 12 * a + 3 * s + 4 * k + v
    print(
        label,
        "chamber noncombat",
        noncombat,
        "combat",
        combat_work / d,
        "conditional complete local task",
        noncombat + combat_work / d,
    )

alcove_paths = (
    ("north", [(208, 32, z) for z in range(363, 354, -1)], (210, 32, 355), "east"),
    (
        "west-south",
        [(x, 32, 384) for x in range(200, 195, -1)] + [(196, 32, z) for z in range(385, 392)],
        (194, 32, 391),
        "west",
    ),
)
for name, path, target, stair_facing in alcove_paths:
    work_verify(path)
    work_verify(list(reversed(path)))
    assert at(case, *target)["Name"] == "minecraft:chest"
    assert at(case, target[0], 33, target[2]) == {
        "Name": "minecraft:stone_brick_stairs",
        "Properties": {
            "facing": stair_facing,
            "half": "top",
            "shape": "straight",
            "waterlogged": "true",
        },
    }
    station = path[-1]
    face_x = target[0] + (0.0625 if station[0] < target[0] else 0.9375)
    work_ray((station[0] + 0.5, 33.62, station[2] + 0.5), (face_x, 32.5, target[2] + 0.5), target)
    loot = entities_by_position[target]
    assert loot["LootTable"] == "explorations:chests/underground_temple/dead_end"
    assert "Items" not in loot
    assert "Lock" not in loot
    circuit = path + list(reversed(path))[1:]
    movement = len(circuit) - 1
    headings = [(b[0] - a[0], b[2] - a[2]) for a, b in pairwise(circuit)]
    decisions = sum(a != b for a, b in pairwise(headings)) + 3
    print("PASS alcove", name, movement, "H", decisions, "navigation events; stair lid non-full")
    for label, u, n, a, s, k, v in (
        ("A", 5, 0.5, 0.25, 0.25, 1, 2),
        ("B", 4, 1, 0.5, 0.5, 2, 4),
        ("C", 3, 1.5, 1, 1, 4, 8),
    ):
        print(
            name,
            label,
            "conditional local task seconds",
            movement / u + decisions * n + a + s + k + v,
        )

campfires = [p for p, e in entities_by_position.items() if e["id"] == "minecraft:campfire"]
assert len(campfires) == 9
for position in campfires:
    state = at(case, *position)
    assert state["Name"] == "minecraft:campfire"
    assert state["Properties"]["lit"] == "false"
    assert state["Properties"]["waterlogged"] == "true"
print("PASS all nine saved campfires waterlogged and unlit; zero lit campfires in this sample")

for center_z in (367, 384):
    straight_failure = None
    try:
        verify([(x, 32, center_z) for x in range(196, 179, -1)])
    except AssertionError as error:
        straight_failure = error.args[0]
    assert straight_failure is not None
    assert straight_failure[1:] == ((191, 32, center_z), "minecraft:cobweb")
    tower_removed = set()
    tower_doors = set()
    _, tower_verify = importlib.import_module("evidence.item-13.temple_geometry").path_checks(
        case, tower_removed, tower_doors, set()
    )
    tower_rays = {}
    tower_ray = importlib.import_module("evidence.item-13.temple_geometry").ray_check(
        case, tower_removed, tower_rays
    )
    approach = [(x, 32, center_z) for x in range(196, 191, -1)] + [
        (x, 32, center_z - 1) for x in range(192, 189, -1)
    ]
    tower_verify(approach)
    web = (189, 32, center_z - 1)
    assert at(case, *web)["Name"] == "minecraft:cobweb"
    tower_ray((190.5, 33.62, center_z - 0.5), (189.9375, 32.5, center_z - 0.5), web)
    tower_removed.add(web)
    approach += [(189, 32, center_z - 1), (188, 32, center_z - 1)]
    crossing = [(x, 32, center_z - 1) for x in (188, 187, 186)]
    closed_failure = None
    try:
        tower_verify(crossing)
    except AssertionError as error:
        closed_failure = error.args[0]
    assert closed_failure is not None
    assert closed_failure[1:] == ((187, 32, center_z - 1), "minecraft:iron_door")
    for x, facing, end_x in ((188, "east", 188.0625), (186, "west", 186.9375)):
        button = (x, 34, center_z - 1)
        assert at(case, *button) == {
            "Name": "minecraft:stone_button",
            "Properties": {"face": "wall", "facing": facing, "powered": "false"},
        }
        tower_ray((x + 0.5, 33.62, center_z - 0.5), (end_x, 34.5, center_z - 0.5), button)
    for y, half in ((32, "lower"), (33, "upper")):
        door = (187, y, center_z - 1)
        assert at(case, *door) == {
            "Name": "minecraft:iron_door",
            "Properties": {
                "facing": "west",
                "half": half,
                "hinge": "left",
                "open": "false",
                "powered": "false",
            },
        }
        tower_doors.add(door)
    inner = [
        (186, 32, center_z - 1),
        (185, 32, center_z - 1),
        (185, 32, center_z),
        (185, 32, center_z + 1),
    ]
    for target, station, end_x in (
        ((184, 32, center_z - 2), inner[1], 184.9375),
        ((186, 32, center_z + 2), inner[-1], 186.0625),
    ):
        assert at(case, *target)["Name"] == "minecraft:chest"
        assert at(case, target[0], 33, target[2])["Name"] == "minecraft:air"
        tower_ray(
            (station[0] + 0.5, 33.62, station[2] + 0.5), (end_x, 32.5, target[2] + 0.5), target
        )
        loot = entities_by_position[target]
        assert loot["LootTable"] == "explorations:chests/underground_temple/quest_tower"
        assert "Items" not in loot
        assert "Lock" not in loot
    upper_tower_path = approach + crossing[1:] + inner[1:]
    tower_verify(upper_tower_path)
    tower_verify(list(reversed(upper_tower_path)))
    assert all(2 / u < 30 / 20 for u in (5, 4, 3))
    print(
        "PASS western tower upper segment",
        center_z,
        2 * (len(upper_tower_path) - 1),
        "H return; one web, two button operations, two chest rays; lower floors pending",
    )

for center_z in (367, 384):
    inner_removed = set()
    inner_doors = set()
    inner_feet = set()
    inner_clear, inner_verify = importlib.import_module(
        "evidence.item-13.temple_geometry"
    ).path_checks(case, inner_removed, inner_doors, inner_feet)
    inner_rays = {}
    inner_ray = importlib.import_module("evidence.item-13.temple_geometry").ray_check(
        case, inner_removed, inner_rays
    )
    crossing = [(x, 32, center_z + 1) for x in (184, 183, 182)]
    closed_failure = None
    try:
        inner_verify(crossing)
    except AssertionError as error:
        closed_failure = error.args[0]
    assert closed_failure is not None
    assert closed_failure[1:] == ((183, 32, center_z + 1), "minecraft:iron_door")
    for x, facing, face_x in ((184, "east", 184.0625), (182, "west", 182.9375)):
        button = (x, 34, center_z + 1)
        assert at(case, *button) == {
            "Name": "minecraft:stone_button",
            "Properties": {"face": "wall", "facing": facing, "powered": "false"},
        }
        inner_ray((x + 0.5, 33.62, center_z + 1.5), (face_x, 34.5, center_z + 1.5), button)
    for y, half in ((32, "lower"), (33, "upper")):
        door = (183, y, center_z + 1)
        assert at(case, *door) == {
            "Name": "minecraft:iron_door",
            "Properties": {
                "facing": "west",
                "half": half,
                "hinge": "right",
                "open": "false",
                "powered": "false",
            },
        }
        inner_doors.add(door)
    room_link = [(x, 32, center_z + 1) for x in range(185, 180, -1)]
    inner_verify(room_link)
    inner_verify(list(reversed(room_link)))
    floor = (181, 31, center_z)
    assert at(case, *floor)["Name"] == "minecraft:stone_bricks"
    inner_ray((181.5, 33.62, center_z + 1.5), (181.5, 31.999, center_z + 0.5), floor)
    inner_removed.add(floor)
    assert at(case, 181, 27, center_z)["Name"] in {
        "minecraft:stone_bricks",
        "minecraft:cracked_stone_bricks",
    }
    assert all(at(case, 181, y, center_z)["Name"] == "minecraft:air" for y in range(28, 31))
    inner_clear([181.2, 28, center_z + 0.2, 181.8, 33.8, center_z + 0.8])
    lower = [(181, 28, center_z), (181, 28, center_z + 1)]
    inner_verify(lower)
    inner_verify(list(reversed(lower)))
    # Base and repeated ordinary side clicks, from the adjacent supported station.
    lower_eye = (181.5, 29.62, center_z + 1.5)
    inner_ray(lower_eye, (181.5, 27.999, center_z + 0.5), (181, 27, center_z))
    inner_ray(lower_eye, (181.5, 28.95, center_z + 1), (181, 28, center_z))
    inner_feet.update((181, y, center_z) for y in range(28, 33))
    column = [(181, y, center_z) for y in range(28, 33)]
    inner_verify(column)
    inner_verify(list(reversed(column)))
    inner_verify([(181, 32, center_z), (181, 32, center_z + 1)])
    inner_verify([(181, 32, center_z + 1), (181, 32, center_z)])
    trapdoor = at(case, 180, 31, center_z)
    assert trapdoor == {
        "Name": "minecraft:oak_trapdoor",
        "Properties": {
            "facing": "east",
            "half": "top",
            "open": "false",
            "powered": "false",
            "waterlogged": "true",
        },
    }
    wire = at(case, 180, 28, center_z)
    assert wire["Name"] == "minecraft:tripwire"
    assert wire["Properties"]["attached"] == "true"
    assert wire["Properties"]["disarmed"] == "false"
    assert wire["Properties"]["powered"] == "false"
    print(
        "PASS western tower middle connection",
        center_z,
        "12H/8V return, one masonry removal, four scaffolds, two inner button operations; "
        "closed trapdoor/tripwire untouched, initial four-block fall retained",
    )

for center_z in (367, 384):
    middle_removed = set()
    middle_feet = set()
    middle_clear, middle_verify = importlib.import_module(
        "evidence.item-13.temple_geometry"
    ).path_checks(case, middle_removed, set(), middle_feet)
    middle_rays = {}
    middle_ray = importlib.import_module("evidence.item-13.temple_geometry").ray_check(
        case, middle_removed, middle_rays
    )
    panel_approach = [(181, 28, center_z + 1)] + [(x, 28, center_z) for x in range(181, 185)]
    middle_verify(panel_approach)
    blocked = None
    try:
        middle_verify([(184, 28, center_z), (185, 28, center_z)])
    except AssertionError as error:
        blocked = error.args[0]
    assert blocked is not None
    assert blocked[1] == (185, 28, center_z)
    for y in (28, 29):
        panel = (185, y, center_z)
        assert at(case, *panel)["Name"] in {
            "minecraft:stone_bricks",
            "minecraft:mossy_stone_bricks",
            "minecraft:cracked_stone_bricks",
            "minecraft:chiseled_stone_bricks",
        }
        middle_ray((184.5, 29.62, center_z + 0.5), (185.001, y + 0.5, center_z + 0.5), panel)
        middle_removed.add(panel)
    middle_path = (
        panel_approach
        + [(x, 28, center_z) for x in range(185, 190)]
        + [(189, 28, center_z - 1), (190, 28, center_z - 1)]
    )
    middle_verify(middle_path)
    middle_verify(list(reversed(middle_path)))
    chest = (190, 28, center_z - 2)
    assert at(case, *chest)["Name"] == "minecraft:chest"
    assert at(case, 190, 29, center_z - 2)["Name"] == "minecraft:air"
    middle_eye = (190.5, 29.62, center_z - 0.5)
    middle_ray(middle_eye, (190.5, 28.5, center_z - 1.0625), chest)
    saved = entities_by_position[chest]
    assert saved["LootTable"] == "explorations:chests/underground_temple/quest_tower"
    assert "Items" not in saved
    assert "Lock" not in saved
    for y in (28, 29, 30):
        for z, facing in ((center_z - 3, "south"), (center_z + 3, "north")):
            assert at(case, 185, y, z) == {
                "Name": "minecraft:sticky_piston",
                "Properties": {"extended": "true", "facing": facing},
            }
    floor = (189, 27, center_z - 1)
    assert at(case, *floor)["Name"] == "minecraft:stone_bricks"
    middle_ray(middle_eye, (189.5, 27.999, center_z - 0.5), floor)
    middle_removed.add(floor)
    assert at(case, 189, 23, center_z - 1)["Name"] == "minecraft:stone_bricks"
    assert all(at(case, 189, y, center_z - 1)["Name"] == "minecraft:air" for y in range(24, 27))
    middle_clear([189.2, 24, center_z - 0.8, 189.8, 29.8, center_z - 0.2])
    lower = [(189, 24, center_z - 1), (190, 24, center_z - 1)]
    middle_verify(lower)
    middle_verify(list(reversed(lower)))
    lower_eye = (190.5, 25.62, center_z - 0.5)
    middle_ray(lower_eye, (189.5, 23.999, center_z - 0.5), (189, 23, center_z - 1))
    middle_ray(lower_eye, (190, 24.95, center_z - 0.5), (189, 24, center_z - 1))
    middle_feet.update((189, y, center_z - 1) for y in range(24, 29))
    column = [(189, y, center_z - 1) for y in range(24, 29)]
    middle_verify(column)
    middle_verify(list(reversed(column)))
    middle_verify(middle_path)
    middle_verify(list(reversed(middle_path)))
    assert 2 * (len(middle_path) - 1) == 22
    print(
        "PASS western tower middle reward",
        center_z,
        "22H return, two panel removals, one chest; next shaft four scaffolds/one floor removal, "
        "4H/8V return and four-block initial fall",
    )

for center_z in (367, 384):
    lower_removed = set()
    lower_doors = set()
    _, lower_verify = importlib.import_module("evidence.item-13.temple_geometry").path_checks(
        case, lower_removed, lower_doors, set()
    )
    lower_rays = {}
    lower_ray = importlib.import_module("evidence.item-13.temple_geometry").ray_check(
        case, lower_removed, lower_rays
    )
    lower_approach = [(190, 24, center_z - 1), (189, 24, center_z - 1)]
    lower_verify(lower_approach)
    web = (189, 24, center_z)
    assert at(case, *web)["Name"] == "minecraft:cobweb"
    lower_ray((189.5, 25.62, center_z - 0.5), (189.5, 24.5, center_z + 0.001), web)
    lower_removed.add(web)
    for door_x, facing, hinge in ((187, "west", "right"), (183, "east", "left")):
        crossing = [(x, 24, center_z) for x in (door_x + 1, door_x, door_x - 1)]
        rejected = None
        try:
            lower_verify(crossing)
        except AssertionError as error:
            rejected = error.args[0]
        assert rejected is not None
        assert rejected[1:] == ((door_x, 24, center_z), "minecraft:iron_door")
        for side in (1, -1):
            x = door_x + side
            button = (x, 26, center_z)
            assert at(case, *button) == {
                "Name": "minecraft:stone_button",
                "Properties": {
                    "face": "wall",
                    "facing": "east" if side == 1 else "west",
                    "powered": "false",
                },
            }
            face_x = x + (0.0625 if side == 1 else 0.9375)
            lower_ray((x + 0.5, 25.62, center_z + 0.5), (face_x, 26.5, center_z + 0.5), button)
        for y, half in ((24, "lower"), (25, "upper")):
            door = (door_x, y, center_z)
            assert at(case, *door) == {
                "Name": "minecraft:iron_door",
                "Properties": {
                    "facing": facing,
                    "half": half,
                    "hinge": hinge,
                    "open": "false",
                    "powered": "false",
                },
            }
            lower_doors.add(door)
    lower_crossing = lower_approach + [(x, 24, center_z) for x in range(189, 180, -1)]
    lower_verify(lower_crossing)
    lower_verify(list(reversed(lower_crossing)))
    attached_alcove = [(185, 24, z) for z in range(center_z, center_z - 8, -1)]
    lower_verify(attached_alcove)
    lower_verify(list(reversed(attached_alcove)))
    target = (187, 24, center_z - 7)
    assert at(case, *target)["Name"] == "minecraft:chest"
    assert at(case, 187, 25, center_z - 7) == {
        "Name": "minecraft:stone_brick_stairs",
        "Properties": {"facing": "east", "half": "top", "shape": "straight", "waterlogged": "true"},
    }
    lower_ray((185.5, 25.62, center_z - 6.5), (187.0625, 24.5, center_z - 6.5), target)
    saved = entities_by_position[target]
    assert saved["LootTable"] == "explorations:chests/underground_temple/dead_end"
    assert "Items" not in saved
    assert "Lock" not in saved
    assert 2 * (len(lower_crossing) - 1) == 20
    assert 2 * (len(attached_alcove) - 1) == 14
    for x in (183, 184, 185, 188, 189, 190):
        assert at(case, x, 20, center_z)["Name"] == "minecraft:lava"
    print(
        "PASS lower tower doors/alcove",
        center_z,
        "20H lower return plus14H reward excursion; one web, four button operations, one chest; "
        "six central bottom lava cells retained, bottom route pending",
    )

for center_z in (367, 384):
    bottom_removed = set()
    bottom_feet = set()
    bottom_clear, bottom_verify = importlib.import_module(
        "evidence.item-13.temple_geometry"
    ).path_checks(case, bottom_removed, set(), bottom_feet)
    bottom_rays = {}
    bottom_ray = importlib.import_module("evidence.item-13.temple_geometry").ray_check(
        case, bottom_removed, bottom_rays
    )
    floor = (181, 23, center_z)
    assert at(case, *floor)["Name"] in {"minecraft:stone_bricks", "minecraft:cracked_stone_bricks"}
    bottom_verify([(181, 24, center_z + 1)])
    bottom_ray((181.5, 25.62, center_z + 1.5), (181.5, 23.999, center_z + 0.5), floor)
    bottom_removed.add(floor)
    assert at(case, 181, 19, center_z)["Name"] in {
        "minecraft:stone_bricks",
        "minecraft:cracked_stone_bricks",
    }
    assert all(at(case, 181, y, center_z)["Name"] == "minecraft:air" for y in range(20, 23))
    bottom_clear([181.2, 20, center_z + 0.2, 181.8, 25.8, center_z + 0.8])
    bottom_verify([(181, 20, center_z), (181, 20, center_z + 1)])
    eye = (181.5, 21.62, center_z + 1.5)
    bottom_ray(eye, (181.5, 19.999, center_z + 0.5), (181, 19, center_z))
    bottom_ray(eye, (181.5, 20.95, center_z + 1), (181, 20, center_z))
    bottom_feet.update((181, y, center_z) for y in range(20, 25))
    shaft = [(181, y, center_z) for y in range(20, 25)]
    bottom_verify(shaft)
    bottom_verify(list(reversed(shaft)))
    bottom_verify([(181, 24, center_z), (181, 24, center_z + 1)])
    bottom_verify([(181, 24, center_z + 1), (181, 24, center_z)])
    bottom_verify([(181, 20, center_z + 1), (181, 20, center_z)])
    bottom_zigzag = [
        (x, 20, center_z + dz)
        for x, dz in (
            (181, 1),
            (181, 0),
            (181, -1),
            (182, -1),
            (182, -2),
            (183, -2),
            (184, -2),
            (185, -2),
            (185, -1),
            (186, -1),
            (186, 0),
            (187, 0),
            (187, 1),
            (188, 1),
            (188, 2),
            (189, 2),
            (190, 2),
            (190, 1),
            (191, 1),
            (191, 0),
            (192, 0),
            (193, 0),
        )
    ]
    bottom_verify(bottom_zigzag)
    bottom_verify(list(reversed(bottom_zigzag)))
    center_failure = None
    try:
        bottom_verify([(x, 20, center_z) for x in range(181, 194)])
    except AssertionError as error:
        center_failure = error.args[0]
    assert center_failure is not None
    assert center_failure[1:] == ((183, 20, center_z), "minecraft:lava")
    assert 2 * (len(bottom_zigzag) - 1) == 42
    print(
        "PASS bottom zigzag",
        center_z,
        "42H return, center lava rejected; "
        "third shaft four scaffolds/one removal, 4H/8V return, initial fall retained",
    )
