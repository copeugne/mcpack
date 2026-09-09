"""Focused checks on Item 12's new measurement boundaries."""

# pyright: standard
from array import array

from tools.analyze_discoverability import FIELDS, observe, ray, select_cases
from tools.analyze_route_opportunities import MISSING


def test_ray_retains_blocker_and_unknown() -> None:
    heights = array("h", [0]) * (1024 * 1024)
    assert ray(heights, [0.5, 3, 0.5], [4.5, 3, 0.5]) == {"status": "CLEAR"}
    heights[512 * 1024 + 514] = 3
    blocked = ray(heights, [0.5, 3, 0.5], [4.5, 3, 0.5])
    assert blocked["status"] == "OCCLUDED"
    assert blocked["at"] == [2, 0]
    heights[512 * 1024 + 514] = MISSING
    assert ray(heights, [0.5, 3, 0.5], [4.5, 3, 0.5])["status"] == "UNKNOWN"


def test_family_selection_is_order_independent_and_keeps_density() -> None:
    rows = [
        {"registry_id": "test:a", "family_id": "test:a", "chunk_x": x, "chunk_z": 0}
        for x in range(4)
    ]
    census = {"classification": {"occurrences": rows}, "occurrence_biomes": [], "full_chunks": 4096}
    first = select_cases(census)
    rows.reverse()
    assert select_cases(census) == first
    assert len(first) == 1
    assert first[0]["family_count"] == 4
    assert first[0]["density_chunks"] == 4096
    assert first[0]["target"] is None


def test_same_eye_foliage_contrast_and_missing_extremum() -> None:
    maps = {name: array("h", [0]) * (1024 * 1024) for name in FIELDS}
    maps[FIELDS[0]][512 * 1024 + 530] = 20
    case = {"envelope": None, "target": [0, 5, 0]}
    result = observe(case, maps)
    assert result["low_view"] == result["high_view"] == 0
    assert result["relief"] == 0
    view = result["views"][0]
    assert view["rays"][FIELDS[0]][0]["status"] == "OCCLUDED"
    assert view["rays"][FIELDS[1]][0]["status"] == "CLEAR"
    assert view["eye"] == [64.5, 2.62, 0.5]
    maps[FIELDS[1]][512 * 1024 + 576] = MISSING
    result = observe(case, maps)
    assert result["low_view"] is None
    assert result["high_view"] is None
    assert result["relief"] is None
    assert result["views"][0]["rays"][FIELDS[0]][0]["status"] == "UNKNOWN"


def test_target_on_top_boundary_is_not_its_own_occluder() -> None:
    heights = array("h", [0]) * (1024 * 1024)
    assert ray(heights, [0.5, 3, 0.5], [4.5, 1, 0.5]) == {"status": "CLEAR"}
    heights[512 * 1024 + 514] = 2
    assert ray(heights, [0.5, 3, 0.5], [4.5, 1, 0.5])["status"] == "OCCLUDED"


def test_internal_observers_cannot_count_as_external_discovery() -> None:
    maps = {name: array("h", [0]) * (1024 * 1024) for name in FIELDS}
    # Inclusive saved-block envelope ends at x=64; the observer cell is internal.
    case = {"envelope": [-64, 0, -10, 64, 4, 10], "target": [0, 5, 0]}
    result = observe(case, maps)
    assert result["low_view"] is None
    assert result["high_view"] is None
    assert result["relief"] is None
    for i in (0, 4):
        view = result["views"][i]
        assert view["eye"] is not None
        for field in FIELDS:
            assert all(
                r == {"status": "UNKNOWN", "reason": "observer_inside_envelope"}
                for r in view["rays"][field]
            )
    assert result["views"][2]["rays"][FIELDS[0]][0]["status"] == "CLEAR"
    case["envelope"] = [-64, 0, -64, 64, 4, 64]
    result = observe(case, maps)
    assert all(
        r["status"] == "UNKNOWN"
        for v in result["views"]
        for field in FIELDS
        for r in v["rays"][field]
    )
