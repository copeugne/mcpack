from itertools import product
from typing import cast

import pytest
from tools.analyze_structure_density import category_occurrences, spatial_summary


def starts(*points: tuple[int, int]) -> list[dict[str, str | int]]:
    return [
        {"registry_id": f"test:start_{index}", "chunk_x": x, "chunk_z": z}
        for index, (x, z) in enumerate(points)
    ]


def test_coincident_distinct_starts_have_exact_zero_distance() -> None:
    result = spatial_summary(starts((0, 0), (0, 0)), (-16, 15, -16, 15))
    assert result["mean_nearest_neighbor_blocks"] == 0
    neighbors = cast("list[dict[str, object]]", result["nearest_neighbors"])
    assert len(neighbors) == 2
    assert all(row["boundary_censored"] is False for row in neighbors)


def test_boundary_censoring_retains_observed_distance_and_lower_bound() -> None:
    result = spatial_summary(starts((0, 0), (10, 0)), (0, 31, 0, 31))
    assert result["mean_nearest_neighbor_blocks"] is None
    neighbors = cast("list[dict[str, object]]", result["nearest_neighbors"])
    assert result["mean_nearest_observed_blocks"] == 160
    assert all(row["nearest_observed_blocks"] == 160 for row in neighbors)
    assert all(row["boundary_censored"] is True for row in neighbors)
    assert all(row["nearest_distance_lower_bound_blocks"] == 8 for row in neighbors)


def test_interior_distance_and_population_cell_dispersion() -> None:
    result = spatial_summary(starts((1, 1), (2, 1)), (-16, 15, -16, 15))
    assert result["mean_nearest_neighbor_blocks"] == 16
    assert result["full_cell_variance_over_mean"] == 1.5
    assert result["full_cell_zero_fraction"] == 0.75


@pytest.mark.parametrize("points", [(), ((0, 0),)])
def test_absent_neighbor_has_no_estimated_mean(points: tuple[tuple[int, int], ...]) -> None:
    result = spatial_summary(starts(*points), (-16, 15, -16, 15))
    assert result["mean_nearest_neighbor_blocks"] is None
    neighbors = cast("list[dict[str, object]]", result["nearest_neighbors"])
    assert all(row["nearest_observed_blocks"] is None for row in neighbors)


def test_partial_cells_keep_denominators_but_cannot_expand_empty_rectangle() -> None:
    result = spatial_summary([], (-31, 31, -31, 31))
    cells = cast("list[dict[str, int]]", result["cells"])
    assert sum(row["full_chunks"] for row in cells) == 3969
    assert result["full_cell_count"] == 9
    assert result["full_cell_variance_over_mean"] is None
    assert result["largest_empty_full_cell_rectangle"] == {
        "area_chunks": 2304,
        "bounds_chunks": [-16, 31, -16, 31],
    }


def test_largest_empty_rectangle_matches_exhaustive_small_grid() -> None:
    grid = list(product(range(3), range(2)))
    for mask in range(1 << len(grid)):
        occupied = {cell for index, cell in enumerate(grid) if mask & (1 << index)}
        result = spatial_summary(starts(*[(16 * x, 16 * z) for x, z in occupied]), (0, 47, 0, 31))
        candidates: list[tuple[int, list[int]]] = []
        for left, right, top, bottom in product(range(3), range(3), range(2), range(2)):
            if left > right or top > bottom:
                continue
            cells = set(product(range(left, right + 1), range(top, bottom + 1)))
            if not cells & occupied:
                candidates.append(
                    (len(cells) * 256, [left * 16, right * 16 + 15, top * 16, bottom * 16 + 15])
                )
        expected = min(candidates, key=lambda row: (-row[0], row[1])) if candidates else (0, None)
        assert result["largest_empty_full_cell_rectangle"] == {
            "area_chunks": expected[0],
            "bounds_chunks": expected[1],
        }


def test_overlapping_categories_recompute_neighbors_from_the_selected_union() -> None:
    rows: list[dict[str, object]] = [
        {
            "registry_id": "test:ambient",
            "chunk_x": 0,
            "chunk_z": 0,
            "role": "T0",
            "comparison_groups": ["village"],
        },
        {
            "registry_id": "test:civilization",
            "chunk_x": 1,
            "chunk_z": 0,
            "role": "C",
            "comparison_groups": [],
        },
        {
            "registry_id": "test:encounter",
            "chunk_x": 2,
            "chunk_z": 0,
            "role": "T1",
            "comparison_groups": ["village", "other"],
        },
        {
            "registry_id": "test:dungeon",
            "chunk_x": 3,
            "chunk_z": 0,
            "role": "T2",
            "comparison_groups": ["not_village"],
        },
        {
            "registry_id": "test:expedition",
            "chunk_x": 4,
            "chunk_z": 0,
            "role": "T3",
            "comparison_groups": [],
        },
        {
            "registry_id": "test:objective",
            "chunk_x": 5,
            "chunk_z": 0,
            "role": "T4",
            "comparison_groups": [],
        },
    ]
    groups = category_occurrences(rows)
    assert groups["actionable_candidates"] == rows[1:]
    assert groups["encounter_sites"] == rows[2:]
    assert groups["villages"] == [rows[0], rows[2]]
    assert groups["T2"] == [rows[3]]
    assert groups["T3"] == [rows[4]]
    assert groups["T4"] == [rows[5]]
    selected = cast("list[dict[str, str | int]]", groups["encounter_sites"])
    result = spatial_summary(selected, (-16, 15, -16, 15))
    assert result["mean_nearest_neighbor_blocks"] == 16
    # Individual singleton tiers have no neighbor; averaging their means would be wrong.
    assert (
        spatial_summary([selected[0]], (-16, 15, -16, 15))["mean_nearest_neighbor_blocks"] is None
    )


def test_empty_categories_retain_zero_counts_and_unknown_distances() -> None:
    for selected in category_occurrences([]).values():
        result = spatial_summary(cast("list[dict[str, str | int]]", selected), (-16, 15, -16, 15))
        assert result["nearest_neighbors"] == []
        assert result["mean_nearest_neighbor_blocks"] is None


def test_actual_anchors_keep_within_chunk_distances() -> None:
    rows = starts((0, 0), (0, 0))
    rows[0].update(anchor_x=1, anchor_z=2)
    rows[1].update(anchor_x=4, anchor_z=6)
    result = spatial_summary(rows, (-16, 15, -16, 15))
    assert result["mean_nearest_neighbor_blocks"] == 5


def test_negative_chunk_anchor_uses_floor_inclusion_and_actual_boundary() -> None:
    rows = starts((-1, -1), (0, -1))
    rows[0].update(anchor_x=-1, anchor_z=-1)
    rows[1].update(anchor_x=1, anchor_z=-1)
    result = spatial_summary(rows, (-1, 0, -1, 0))
    assert result["mean_nearest_neighbor_blocks"] == 2
    neighbors = cast("list[dict[str, object]]", result["nearest_neighbors"])
    assert [row["boundary_distance_blocks"] for row in neighbors] == [15, 15]


@pytest.mark.parametrize(
    "patch",
    [
        {"anchor_x": 1},
        {"anchor_x": True, "anchor_z": 2},
        {"anchor_x": "1", "anchor_z": 2},
        {"anchor_x": 16, "anchor_z": 2},
        {"chunk_x": True},
        {"chunk_x": 16},
    ],
)
def test_spatial_rejects_ambiguous_or_outside_anchors(patch: dict[str, str | int]) -> None:
    rows = starts((0, 0))
    rows[0].update(patch)
    with pytest.raises(ValueError, match="occurrence"):
        _ = spatial_summary(rows, (-16, 15, -16, 15))
