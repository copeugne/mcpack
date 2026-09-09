"""Boundary checks for positive-volume actor collision."""

# pyright: standard
# ruff: noqa: INP001, S101, D103
import importlib

clearance = importlib.import_module("evidence.item-13.collision.clearance")


def test_touching_floor_and_face_allow_clearance_but_overlap_rejects() -> None:
    actor = [0.2, 1.0, 0.2, 0.8, 2.8, 0.8]
    assert not clearance.overlaps(actor, [0, 0, 0, 1, 1, 1])
    assert not clearance.overlaps(actor, [0.8, 1, 0, 1, 3, 1])
    assert clearance.overlaps(actor, [0.79, 1, 0, 1, 3, 1])
    assert clearance.overlaps(actor, [0, 2.79, 0, 1, 3, 1])
    assert not clearance.overlaps(actor, [0, 2.8, 0, 1, 3, 1])
