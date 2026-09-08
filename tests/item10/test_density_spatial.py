from itertools import product
from typing import cast

import pytest
from tools.analyze_structure_density import spatial_summary


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
