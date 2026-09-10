"""Boundary checks for positive-volume actor collision."""

# pyright: standard
# ruff: noqa: INP001, S101, D103
import importlib

import pytest

clearance = importlib.import_module("evidence.item-13.collision.clearance")


def test_touching_floor_and_face_allow_clearance_but_overlap_rejects() -> None:
    actor = [0.2, 1.0, 0.2, 0.8, 2.8, 0.8]
    assert not clearance.overlaps(actor, [0, 0, 0, 1, 1, 1])
    assert not clearance.overlaps(actor, [0.8, 1, 0, 1, 3, 1])
    assert clearance.overlaps(actor, [0.79, 1, 0, 1, 3, 1])
    assert clearance.overlaps(actor, [0, 2.79, 0, 1, 3, 1])
    assert not clearance.overlaps(actor, [0, 2.8, 0, 1, 3, 1])


def test_expansion_rejects_missing_collision_cells() -> None:
    with pytest.raises(ValueError, match="omits"):
        clearance.expand_shapes({"shape_indices_yzx": [], "local_aabbs": []}, [0, 0, 0, 0, 0, 0])


def test_balcony_transition_rejects_collision_free_midair_ascent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    route = importlib.import_module("evidence.item-13.collision.house_route")
    assert route.verify(crouch_balcony=True)["collision_free"]
    unsupported = [point.copy() for point in route.OUTBOUND]
    for point in unsupported:
        if point[0] in (464.3, 464.7):
            point[0] = 464.5
    # Remove the now-duplicate lower point; retain the old unsupported ascent.
    unsupported = [
        point for i, point in enumerate(unsupported) if i == 0 or point != unsupported[i - 1]
    ]
    monkeypatch.setattr(route, "OUTBOUND", unsupported)
    with pytest.raises(ValueError, match="No adjacent support"):
        route.verify(crouch_balcony=True)


def test_second_house_rejects_unsupported_z_transition(monkeypatch: pytest.MonkeyPatch) -> None:
    route = importlib.import_module("evidence.item-13.collision.house_route")
    assert route.verify(second_house=True, crouch_balcony=True)["collision_free"]
    unsupported = [point.copy() for point in route.SECOND_OUTBOUND]
    for point in unsupported:
        if point[2] in (112.3, 112.7):
            point[2] = 112.5
    unsupported = [
        point for i, point in enumerate(unsupported) if i == 0 or point != unsupported[i - 1]
    ]
    monkeypatch.setattr(route, "SECOND_OUTBOUND", unsupported)
    with pytest.raises(ValueError, match="No adjacent support"):
        route.verify(second_house=True, crouch_balcony=True)
