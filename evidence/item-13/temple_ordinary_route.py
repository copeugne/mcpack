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
