"""Validate the scoped saved large_hall_down floor and central-opening boundary."""

# pyright: standard
# ruff: noqa: INP001, S101, T201, PLR2004
import gzip
import hashlib
import importlib
import json
from itertools import pairwise
from pathlib import Path

raw = (
    Path(__file__).parent / "fixed-blocks/explorations-underground-temple-large-hall-down.json.gz"
).read_bytes()
assert (
    hashlib.sha256(raw).hexdigest()
    == "a62c45cb2dd69fce020e28b78faf438314ff7e5abb97ebda149ec29699a84c8a"
)
case = json.loads(gzip.decompress(raw))["cases"][0]
_, verify = importlib.import_module("evidence.item-13.temple_geometry").path_checks(
    case, set(), set(), set()
)
ring = (
    [(-480 + x, 42, 50) for x in range(-3, 4)]
    + [(-477, 42, 53 + z) for z in range(-2, 4)]
    + [(-480 + x, 42, 56) for x in range(2, -4, -1)]
    + [(-483, 42, 53 + z) for z in range(2, -4, -1)]
)
verify(ring)
verify(list(reversed(ring)))
spokes = {}
for dx, dz in ((0, -1), (1, 0), (0, 1), (-1, 0)):
    path = [
        (-480 + dx * r, y, 53 + dz * r)
        for r, y in ((8, 44), (7, 44), (6, 43), (5, 43), (4, 42), (3, 42))
    ]
    verify(path)
    verify(list(reversed(path)))
    spokes[(dx, dz)] = path
rim = [(-480, 42, 50), (-480, 42, 51)]
verify(rim)
verify(list(reversed(rim)))
try:
    verify([(-480, 42, 53)])
except AssertionError:
    print("PASS rejected central air-floor standing cell")
else:
    message = "central opening incorrectly accepted as supported"
    raise AssertionError(message)
# Rotate the existing ring to its northern spoke, preserving checked edges.
open_ring = ring[:-1]
index = open_ring.index(rim[0])
loop = open_ring[index:] + open_ring[:index] + [rim[0]]
route = list(spokes[(0, -1)])
route += rim[1:] + rim[-2::-1]
for point in loop[1:]:
    route.append(point)
    for direction, spoke in spokes.items():
        if direction != (0, -1) and point == spoke[-1]:
            route += list(reversed(spoke))[1:] + spoke[1:]
route += list(reversed(spokes[(0, -1)]))[1:]
verify(route)
assert route[0] == route[-1] == (-480, 44, 45)
print("PASS native hall four spokes, ring and supported rim")
horizontal = sum(abs(a[0] - b[0]) + abs(a[2] - b[2]) for a, b in pairwise(route))
ascent = sum(max(0, b[1] - a[1]) for a, b in pairwise(route))
descent = sum(max(0, a[1] - b[1]) for a, b in pairwise(route))
print("Survey horizontal", horizontal)
print("Survey ascent", ascent)
print("Survey descent", descent)

steps = [tuple(b[i] - a[i] for i in range(3)) for a, b in pairwise(route)]
decisions = 1 + sum(a != b for a, b in pairwise(steps))
print("Survey decisions", decisions)
for label, u, j, n, v in (("A", 5, 1, 0.5, 2), ("B", 4, 0.5, 1, 4), ("C", 3, 0.25, 1.5, 8)):
    print(
        "Complete conditional survey seconds",
        label,
        horizontal / u + (ascent + descent) / j + decisions * n + v,
    )

at = importlib.import_module("evidence.item-13.render_pilot").state_at
for x, z in ((-480, 44), (-471, 53), (-489, 53)):
    assert at(case, x, 43, z)["Name"] == "minecraft:stone_bricks"
    assert all(at(case, x, y, z)["Name"] == "minecraft:air" for y in (44, 45))
assert all(at(case, -480, y, 62)["Name"] == "minecraft:water" for y in (43, 44, 45))
assert all(at(case, -479, y, z)["Name"] == "minecraft:air" for y in range(38, 42) for z in (52, 53))
print("PASS three dry neighboring cells, southern water exposure and below-boundary opening")
surface = [y for x, z, y in case["surface_xzy"] if -488 <= x <= -472 and 45 <= z <= 61]
assert len(surface) == 289
assert set(surface) == {62}
print("Hall footprint WORLD_SURFACE Y62; top separation 7, low-floor separation 20")
