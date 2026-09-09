"""Regression checks for conditional route and visibility boundaries."""

# pyright: standard
# ruff: noqa: D103, INP001, S101
import pytest
from analyze_pilot import intersects, paths, visible


def test_routes_do_not_cross_missing_cells() -> None:
    cells = {(0, 1, 0), (1, 1, 0), (3, 1, 0)}
    result = paths(cells, (0, 1, 0))
    assert result[(1, 1, 0)] == [(0, 1, 0), (1, 1, 0)]
    assert (3, 1, 0) not in result
    with pytest.raises(ValueError, match="standing cell"):
        paths(cells, (2, 1, 0))


def test_ray_rejects_intervening_solid_and_range() -> None:
    case = {
        "bounds": [0, 0, 0, 4, 2, 0],
        "palette": [{"Name": "minecraft:air"}, {"Name": "minecraft:stone"}],
        "blocks_yzx": [0] * 15,
    }
    assert visible(case, (0, 0, 0), (2, 0, 0))
    case["blocks_yzx"][1] = 1
    case["blocks_yzx"][6] = 1
    assert not visible(case, (0, 0, 0), (2, 0, 0))
    assert not visible(case, (0, 0, 0), (4, 0, 0))


def test_corner_touch_is_conservatively_occluded() -> None:
    assert intersects((0.5, 0.5, 0.5), (2.5, 2.5, 0.5), (1, 0, 0))
    assert not intersects((0.5, 0.5, 0.5), (2.5, 2.5, 0.5), (2, 0, 0))


def test_coding_rejects_changed_observations(tmp_path, monkeypatch) -> None:  # noqa: ANN001
    import analyze_pilot  # noqa: PLC0415

    pilot = tmp_path / "pilot"
    pilot.mkdir()
    (pilot / "observations.json.gz").write_bytes(b"changed evidence")
    (pilot / "coding.json").write_text('{"source_sha256": "wrong"}')
    monkeypatch.setattr(analyze_pilot, "ROOT", tmp_path)
    with pytest.raises(ValueError, match="raw observation hash"):
        analyze_pilot.main()
    assert not (pilot / "results.json").exists()
