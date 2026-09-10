"""Existing temple clearance rules shared by retained assembly/component checks."""

# pyright: standard
# ruff: noqa: INP001, S101, ANN001, ANN201, PLR2004
import importlib
import math
from itertools import pairwise

at = importlib.import_module("evidence.item-13.render_pilot").state_at
overlap = importlib.import_module("evidence.item-13.collision.clearance").overlaps


def path_checks(c, removed, opened_doors, modeled_scaffold_feet, *, bottom_slabs=()):  # noqa: C901
    """Bind the existing checks to one raw case and explicit hypothetical state."""

    def clear(box) -> None:
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
                        n == "minecraft:sculk_vein"
                        and state["Properties"]["waterlogged"] == "false"
                    ):
                        continue
                    height = 1.5 if n.endswith(("_wall", "_fence")) else 1
                    if (x, y, z) in bottom_slabs:
                        assert n == "minecraft:deepslate_brick_slab"
                        assert state["Properties"] == {"type": "bottom", "waterlogged": "true"}
                        height = 0.5
                    assert not overlap(box, [x, y, z, x + 1, y + height, z + 1]), (
                        box,
                        (x, y, z),
                        n,
                    )

    def verify_path(points, *, crouch_up=False) -> None:
        """Check adult .6 by 1.8 occupancy and conservative step/jump sweeps."""
        for x, y, z in points:
            if y % 1 == 0.5:
                support = (x, math.floor(y), z)
                assert support in bottom_slabs, ("undeclared fractional support", (x, y, z))
                assert support not in removed, ("removed fractional support", support)
                assert at(c, *support) == {
                    "Name": "minecraft:deepslate_brick_slab",
                    "Properties": {"type": "bottom", "waterlogged": "true"},
                }
            elif (x, y, z) not in modeled_scaffold_feet:
                assert y % 1 == 0, ("unsupported standing height", y)
                assert (x, y - 1, z) not in removed, ("removed support", (x, y, z))
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
            horizontal_step = abs(a[0] - b[0]) + abs(a[2] - b[2])
            if horizontal_step == 0:
                assert a in modeled_scaffold_feet
                assert b in modeled_scaffold_feet
                assert abs(a[1] - b[1]) == 1
            else:
                assert horizontal_step == 1
            assert abs(a[1] - b[1]) <= 1
            high = max(a[1], b[1]) + (0.3 if b[1] > a[1] and horizontal_step else 0)
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

    return clear, verify_path


def ray_check(c, removed, interaction_rays):
    """Bind the existing interaction-ray check to one case and removal state."""

    def check_ray(eye, end, target) -> None:
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

    return check_ray
