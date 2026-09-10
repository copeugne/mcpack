"""Validate the second retained temple assembly with explicit local paths."""

# pyright: standard
# ruff: noqa: INP001, S101, T201, PLR2004
import gzip
import hashlib
import importlib
import json
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
shaft_clear, shaft_verify = importlib.import_module(
    "evidence.item-13.temple_geometry"
).path_checks(case, shaft_removals, set(), shaft_feet)
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
