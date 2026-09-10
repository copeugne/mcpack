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

tower_parts = {z: {"removed": set(), "doors": set(), "rays": {}} for z in (367, 384)}

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
    assert all(2 / u < 20 / 20 for u in (5, 4, 3))
    tower_parts[center_z]["upper"] = upper_tower_path
    tower_parts[center_z]["removed"].update(tower_removed)
    tower_parts[center_z]["doors"].update(tower_doors)
    tower_parts[center_z]["rays"].update(tower_rays)
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
    tower_parts[center_z]["inner"] = room_link
    tower_parts[center_z]["removed"].update(inner_removed)
    tower_parts[center_z]["doors"].update(inner_doors)
    tower_parts[center_z]["rays"].update(inner_rays)
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
    tower_parts[center_z]["middle"] = middle_path
    tower_parts[center_z]["removed"].update(middle_removed)
    tower_parts[center_z]["rays"].update(middle_rays)
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
    tower_parts[center_z]["lower"] = lower_crossing
    tower_parts[center_z]["alcove"] = attached_alcove
    tower_parts[center_z]["removed"].update(lower_removed)
    tower_parts[center_z]["doors"].update(lower_doors)
    tower_parts[center_z]["rays"].update(lower_rays)
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
    tower_parts[center_z]["bottom"] = bottom_zigzag
    tower_parts[center_z]["removed"].update(bottom_removed)
    tower_parts[center_z]["rays"].update(bottom_rays)
    print(
        "PASS bottom zigzag",
        center_z,
        "42H return, center lava rejected; "
        "third shaft four scaffolds/one removal, 4H/8V return, initial fall retained",
    )

for center_z, parts in tower_parts.items():
    segments = [
        parts["upper"],
        parts["inner"],
        [(181, y, center_z) for y in range(32, 27, -1)] + [(181, 28, center_z + 1)],
        parts["middle"],
        [(189, y, center_z - 1) for y in range(28, 23, -1)] + [(190, 24, center_z - 1)],
        parts["lower"],
        [(181, 24, center_z + 1)],
        [(181, y, center_z) for y in range(24, 19, -1)] + [(181, 20, center_z + 1)],
        parts["bottom"],
    ]
    outbound = []
    for segment in segments:
        outbound.extend(segment[1:] if outbound and outbound[-1] == segment[0] else segment)
    circuit = outbound + list(reversed(outbound))[1:]
    full = []
    added_alcove = False
    for point in circuit:
        full.append(point)
        if point == parts["alcove"][0] and not added_alcove:
            full.extend(parts["alcove"][1:])
            full.extend(list(reversed(parts["alcove"]))[1:])
            added_alcove = True
    assert added_alcove
    assert full[0] == full[-1] == (196, 32, center_z)
    columns = ((181, center_z, 28, 32), (189, center_z - 1, 24, 28), (181, center_z, 20, 24))
    supports = {(x, y, z) for x, z, base, top in columns for y in range(base, top + 1)}
    _, full_verify = importlib.import_module("evidence.item-13.temple_geometry").path_checks(
        case, parts["removed"], parts["doors"], supports
    )
    full_verify(full)
    visited = set(full)
    for target, rays in parts["rays"].items():
        assert any(
            (int(eye[0]), round(eye[1] - 1.62, 6), int(eye[2])) in visited for eye, _ in rays
        ), target
    horizontal = sum(abs(b[0] - a[0]) + abs(b[2] - a[2]) for a, b in pairwise(full))
    ascent = sum(max(0, b[1] - a[1]) for a, b in pairwise(full))
    descent = sum(max(0, a[1] - b[1]) for a, b in pairwise(full))
    assert (horizontal, ascent, descent) == (148, 12, 12)
    assert len(parts["removed"]) == 7
    assert sum(at(case, *p)["Name"] == "minecraft:cobweb" for p in parts["removed"]) == 2
    assert len(parts["doors"]) == 8
    rewards = {
        p
        for p in parts["rays"]
        if p in entities_by_position and entities_by_position[p]["id"] == "minecraft:chest"
    }
    assert len(rewards) == 4
    for x, z, base, top in columns:
        drop = [(x, y, z) for y in range(top, base - 1, -1)]
        assert sum(full[i : i + len(drop)] == drop for i in range(len(full) - len(drop) + 1)) == 1
    velocity = 0.0
    distance = 0.0
    fall_ticks = 0
    while distance < 4:
        distance -= velocity
        fall_ticks += 1
        velocity = (velocity - 0.08) * 0.9800000190734863
    vectors = [tuple(b[i] - a[i] for i in range(3)) for a, b in pairwise(full)]
    decisions = sum(a != b for a, b in pairwise(vectors)) + 1
    interactions = 7 + 12 + 8 + 4
    selections = 7 + 3 + 8 + 4
    parts["complete"] = full
    print(
        "PASS complete western tower",
        center_z,
        horizontal,
        "H",
        ascent,
        "up",
        descent,
        "down;",
        decisions,
        "decisions",
        interactions,
        "interactions",
        selections,
        "selections; fall ticks",
        fall_ticks,
    )
    for label, u, j, n, a, s, k, v in (
        ("A", 5, 1, 0.5, 0.25, 0.25, 1, 2),
        ("B", 4, 0.5, 1, 0.5, 0.5, 2, 4),
        ("C", 3, 0.25, 1.5, 1, 1, 4, 8),
    ):
        total = (
            horizontal / u
            + 12 / j
            + 3 * fall_ticks / 20
            + 46 / 20
            + decisions * n
            + interactions * a
            + selections * s
            + 4 * k
            + v
        )
        print(
            center_z,
            label,
            "complete conditional tower task seconds",
            total,
            "combat zero by scenario",
        )


# Third west-facing tower: reuse the existing route, but query actual translated cells.
def third_tower_point(point):  # noqa: ANN001, ANN201
    """Apply this one retained tower's observed (+1,-8,+33) translation."""
    return (point[0] + 1, point[1] - 8, point[2] + 33)


third_source = tower_parts[367]
third_removed = {third_tower_point(p) for p in third_source["removed"]}
third_doors = {third_tower_point(p) for p in third_source["doors"]}
third_feet = {
    third_tower_point((x, y, z))
    for x, z, base, top in ((181, 367, 28, 32), (189, 366, 24, 28), (181, 367, 20, 24))
    for y in range(base, top + 1)
}
_, third_verify = importlib.import_module("evidence.item-13.temple_geometry").path_checks(
    case, third_removed, third_doors, third_feet
)
third_route = [third_tower_point(p) for p in third_source["complete"]]
third_verify(third_route)
third_rays = {}
third_ray = importlib.import_module("evidence.item-13.temple_geometry").ray_check(
    case, third_removed, third_rays
)
for target, rays in third_source["rays"].items():
    actual = third_tower_point(target)
    for eye, end in rays:
        third_ray(third_tower_point(eye), third_tower_point(end), actual)
    if target in entities_by_position:
        source_entity = entities_by_position[target]
        actual_entity = entities_by_position[actual]
        assert actual_entity["id"] == source_entity["id"]
        if "LootTable" in source_entity:
            assert actual_entity["LootTable"] == source_entity["LootTable"]
            assert "Items" not in actual_entity
            assert "Lock" not in actual_entity
for p in third_source["doors"]:
    assert at(case, *third_tower_point(p)) == at(case, *p)
for p in third_source["removed"]:
    name = at(case, *third_tower_point(p))["Name"]
    if at(case, *p)["Name"] == "minecraft:cobweb":
        assert name == "minecraft:cobweb"
    else:
        assert name in {
            "minecraft:stone_bricks",
            "minecraft:cracked_stone_bricks",
            "minecraft:mossy_stone_bricks",
            "minecraft:chiseled_stone_bricks",
        }
material_groups = (
    {
        "minecraft:stone_bricks",
        "minecraft:cracked_stone_bricks",
        "minecraft:mossy_stone_bricks",
        "minecraft:chiseled_stone_bricks",
    },
    {"minecraft:stone_brick_stairs", "minecraft:mossy_stone_brick_stairs"},
    {"minecraft:stone_brick_wall", "minecraft:mossy_stone_brick_wall"},
)
compared = 0
material_changes = 0
other_changes = []
for lo_x, lo_y, lo_z, hi_x, hi_y, hi_z in (
    (178, 19, 364, 192, 35, 370),
    (183, 23, 358, 187, 27, 363),
):
    for x in range(lo_x, hi_x + 1):
        for y in range(lo_y, hi_y + 1):
            for z in range(lo_z, hi_z + 1):
                a = at(case, x, y, z)
                b = at(case, *third_tower_point((x, y, z)))
                compared += 1
                if a == b:
                    continue
                if a.get("Properties") == b.get("Properties") and any(
                    a["Name"] in group and b["Name"] in group for group in material_groups
                ):
                    material_changes += 1
                else:
                    other_changes.append(((x, y, z), a, b))
assert compared == 1935
assert material_changes == 448
assert other_changes == [
    (
        (184, 24, 358),
        {"Name": "minecraft:water", "Properties": {"level": "0"}},
        {"Name": "minecraft:seagrass"},
    )
]
assert len(third_rays) == 25
print(
    "PASS third western tower: translated148H/12up/12down circuit and25 ray groups; "
    "1935 footprint cells,448 masonry changes and one retained seagrass difference"
)
third_fixture_count = 0
for position, source_entity in entities_by_position.items():
    x, y, z = position
    if not (
        (178 <= x <= 192 and 19 <= y <= 35 and 364 <= z <= 370)
        or (183 <= x <= 187 and 23 <= y <= 27 and 358 <= z <= 363)
    ):
        continue
    actual_entity = entities_by_position[third_tower_point(position)]
    ignored_fields = {"x", "y", "z", "keepPacked", "LootTableSeed"}
    assert {k: v for k, v in source_entity.items() if k not in ignored_fields} == {
        k: v for k, v in actual_entity.items() if k not in ignored_fields
    }
    third_fixture_count += 1
assert third_fixture_count == 7
print("PASS third tower seven fixture payloads match except coordinates/packing/loot seeds")
actual_third_fixtures = {
    p
    for p in entities_by_position
    if (
        (179 <= p[0] <= 193 and 11 <= p[1] <= 27 and 397 <= p[2] <= 403)
        or (184 <= p[0] <= 188 and 15 <= p[1] <= 19 and 391 <= p[2] <= 396)
    )
}
assert len(actual_third_fixtures) == third_fixture_count


def fourth_tower_block(point):  # noqa: ANN001, ANN201
    """Rotate this saved tower's block origins, including the cell-width offset."""
    return (point[2] - 159, point[1], 585 - point[0])


def fourth_tower_ray(point):  # noqa: ANN001, ANN201
    """Rotate continuous coordinates rather than lower block corners."""
    return (point[2] - 159, point[1], 586 - point[0])


fourth_source = tower_parts[367]
fourth_removed = {fourth_tower_block(p) for p in fourth_source["removed"]}
fourth_doors = {fourth_tower_block(p) for p in fourth_source["doors"]}
fourth_feet = {
    fourth_tower_block((x, y, z))
    for x, z, lo, hi in ((181, 367, 28, 32), (189, 366, 24, 28), (181, 367, 20, 24))
    for y in range(lo, hi + 1)
}
_, fourth_verify = importlib.import_module("evidence.item-13.temple_geometry").path_checks(
    case, fourth_removed, fourth_doors, fourth_feet
)
fourth_bad_start = None
try:
    fourth_verify([fourth_tower_block(p) for p in fourth_source["complete"]])
except AssertionError as error:
    fourth_bad_start = error.args[0]
assert fourth_bad_start == ((208, 32, 389), {"Name": "minecraft:air"})
false_reward = fourth_tower_block((187, 24, 360))
assert at(case, *false_reward)["Name"] == "minecraft:stone_bricks"
assert false_reward not in entities_by_position
fourth_canonical = fourth_source["complete"][3:-3]
old_excursion = fourth_source["alcove"] + fourth_source["alcove"][-2::-1]
indices = [
    i
    for i in range(len(fourth_canonical) - len(old_excursion) + 1)
    if fourth_canonical[i : i + len(old_excursion)] == old_excursion
]
assert len(indices) == 1
corridor = [(185, 24, z) for z in range(367, 355, -1)]
corridor += corridor[-2::-1]
index = indices[0]
fourth_canonical = (
    fourth_canonical[:index] + corridor + fourth_canonical[index + len(old_excursion) :]
)
fourth_route = [fourth_tower_block(p) for p in fourth_canonical]
assert fourth_route[0] == fourth_route[-1] == (208, 32, 392)
assert (197, 24, 400) in fourth_route
assert (208, 20, 392) in fourth_route
fourth_verify(fourth_route)
fourth_rays = {}
fourth_check_ray = importlib.import_module("evidence.item-13.temple_geometry").ray_check(
    case, fourth_removed, fourth_rays
)
fourth_rewards = set()
for target, rays in fourth_source["rays"].items():
    if target == (187, 24, 360):
        continue
    actual = fourth_tower_block(target)
    for eye, end in rays:
        fourth_check_ray(fourth_tower_ray(eye), fourth_tower_ray(end), actual)
    if target in entities_by_position and entities_by_position[target]["id"] == "minecraft:chest":
        assert at(case, *actual)["Name"] == "minecraft:chest"
        assert at(case, actual[0], actual[1] + 1, actual[2])["Name"] == "minecraft:air"
        loot = entities_by_position[actual]
        assert loot["LootTable"] == entities_by_position[target]["LootTable"]
        assert "Items" not in loot
        assert "Lock" not in loot
        fourth_rewards.add(actual)
assert fourth_rewards == {(206, 32, 401), (210, 32, 399), (206, 28, 395)}
for rays in fourth_rays.values():
    assert any(
        (int(eye[0]), round(eye[1] - 1.62, 6), int(eye[2])) in set(fourth_route) for eye, _ in rays
    )
rotation = {"east": "north", "north": "west", "west": "south", "south": "east"}
for original in fourth_source["doors"]:
    expected = at(case, *original)
    expected = {"Name": expected["Name"], "Properties": dict(expected["Properties"])}
    expected["Properties"]["facing"] = rotation[expected["Properties"]["facing"]]
    assert at(case, *fourth_tower_block(original)) == expected
for original in fourth_source["removed"]:
    name = at(case, *fourth_tower_block(original))["Name"]
    assert (
        name == "minecraft:cobweb"
        if at(case, *original)["Name"] == "minecraft:cobweb"
        else name in material_groups[0]
    )
fourth_h = sum(abs(b[0] - a[0]) + abs(b[2] - a[2]) for a, b in pairwise(fourth_route))
fourth_up = sum(max(0, b[1] - a[1]) for a, b in pairwise(fourth_route))
fourth_down = sum(max(0, a[1] - b[1]) for a, b in pairwise(fourth_route))
assert (fourth_h, fourth_up, fourth_down) == (150, 12, 12)
fourth_vectors = [tuple(b[i] - a[i] for i in range(3)) for a, b in pairwise(fourth_route)]
fourth_decisions = sum(a != b for a, b in pairwise(fourth_vectors)) + 1
assert fourth_decisions == 79
print(
    "PASS fourth tower corrected route150H/12up/12down,24 action-ray groups,three rewards; "
    "copied start and nonexistent alcove reward rejected"
)
for label, u, j, n, a, s, k, v in (
    ("A", 5, 1, 0.5, 0.25, 0.25, 1, 2),
    ("B", 4, 0.5, 1, 0.5, 0.5, 2, 4),
    ("C", 3, 0.25, 1.5, 1, 1, 4, 8),
):
    total = 150 / u + 12 / j + 1.65 + 2.3 + 79 * n + 30 * a + 21 * s + 3 * k + v
    print("fourth tower", label, "complete conditional task seconds", total)

fourth_exact = 0
fourth_material = 0
for x in range(178, 193):
    for y in range(19, 36):
        for z in range(364, 371):
            source_state = at(case, x, y, z)
            expected = {"Name": source_state["Name"]}
            if "Properties" in source_state:
                props = {}
                for key, value in source_state["Properties"].items():
                    mapped_key = rotation.get(key, key)
                    mapped_value = value
                    if key == "facing":
                        mapped_value = rotation.get(value, value)
                    elif key == "axis":
                        mapped_value = {"x": "z", "z": "x", "y": "y"}[value]
                    props[mapped_key] = mapped_value
                expected["Properties"] = props
            actual = at(case, *fourth_tower_block((x, y, z)))
            if expected == actual:
                fourth_exact += 1
            else:
                assert expected.get("Properties") == actual.get("Properties")
                assert any(
                    expected["Name"] in group and actual["Name"] in group
                    for group in material_groups
                )
                fourth_material += 1
assert (fourth_exact, fourth_material) == (1342, 443)
fourth_fixture_positions = set()
for position, source_entity in entities_by_position.items():
    x, y, z = position
    if not (178 <= x <= 192 and 19 <= y <= 35 and 364 <= z <= 370):
        continue
    actual_position = fourth_tower_block(position)
    actual_entity = entities_by_position[actual_position]
    ignored_fields = {"x", "y", "z", "keepPacked", "LootTableSeed"}
    assert {k: v for k, v in source_entity.items() if k not in ignored_fields} == {
        k: v for k, v in actual_entity.items() if k not in ignored_fields
    }
    fourth_fixture_positions.add(actual_position)
assert fourth_fixture_positions == {
    p
    for p in entities_by_position
    if 205 <= p[0] <= 211 and 19 <= p[1] <= 35 and 393 <= p[2] <= 407
}
assert len(fourth_fixture_positions) == 5
assert len(fourth_rays) == 24
print(
    "PASS fourth tower1785 rotated footprint states:1342 exact/443 masonry variants; "
    "all five fixture payloads agree except coordinates/packing/loot seeds"
)
