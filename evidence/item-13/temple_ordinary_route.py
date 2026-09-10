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
