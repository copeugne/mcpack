from pathlib import Path
from typing import cast

import pytest
from tools import analyze_structure_density as analysis


def test_all_strata_share_one_observation_pass_without_cross_frame_counts(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    world = tmp_path / "world"
    world.mkdir()
    calls: list[tuple[str, tuple[int, int, int, int]]] = []
    observation_calls: list[int] = []
    # Synthetic routing fixtures exercise inclusion, not generation plausibility.
    locations = [
        {
            "candidate_id": i,
            "family": "supplementaries:cave_urn_cache",
            "dimension": dimension,
            "frame": frame,
            "anchor_x": x,
            "anchor_z": x,
            "anchor_y": 20,
            "chunk_x": x // 16,
            "chunk_z": x // 16,
        }
        for i, (dimension, frame, x) in enumerate(
            (
                ("minecraft:overworld", "overworld", 0),
                ("minecraft:the_end", "end-central", 0),
                ("minecraft:the_end", "end-outer", 8192),
                ("minecraft:overworld", None, 20000),
            )
        )
    ]
    observations: dict[str, object] = {
        "locations": locations,
        "location_observations": [
            {"candidate_id": i, "disposition": "OBSERVED_LOCATION"} for i in range(4)
        ],
    }

    def census(
        world: Path,
        dimension: str,
        bounds: tuple[int, int, int, int],
        geometry: dict[str, tuple[int, int]],
        *,
        include_biomes: bool,
    ) -> dict[str, object]:
        del world, geometry
        assert include_biomes
        calls.append((dimension, bounds))
        return {
            "dimension": dimension,
            "bounds_chunks": list(bounds),
            "full_chunks": 4096,
            "occurrences": [],
            "anvil_inputs": [{"path": str(len(calls)), "sha256": "a" * 64}],
        }

    def nonregistry(  # noqa: PLR0913 - match the existing analysis interface.
        world: Path,
        raw: Path,
        manifest: Path,
        geometry: dict[str, tuple[int, int]],
        frames: dict[str, tuple[str, tuple[int, int, int, int]]],
        *,
        census_inputs: list[dict[str, str]],
        include_biomes: bool,
        require_complete_observer: bool,
    ) -> dict[str, object]:
        del world, raw, manifest, geometry
        assert include_biomes
        assert require_complete_observer
        assert len(census_inputs) == 11
        assert frames["end-central"][1] == (-32, 31, -32, 31)
        assert frames["end-outer"][1] == (480, 543, 480, 543)
        observation_calls.append(1)
        return observations

    monkeypatch.setattr(analysis, "census", census)
    monkeypatch.setattr(analysis, "nonregistry_analysis", nonregistry)
    result = analysis.full_world_census(world, tmp_path / "raw", tmp_path / "manifest", {})
    assert len(calls) == 11
    assert observation_calls == [1]
    assert result["nonregistry_candidates"] is observations
    strata = cast("dict[str, dict[str, object]]", result["strata"])
    assert sum(cast("int", row["full_chunks"]) for row in strata.values()) == 45056
    for label, row in strata.items():
        assert "nonregistry_candidates" not in row
        classification = cast("dict[str, object]", row["classification"])
        classified = cast("list[dict[str, object]]", classification["occurrences"])
        expected = {"overworld": [0], "end-central": [1], "end-outer": [2]}.get(label, [])
        assert [entry["candidate_id"] for entry in classified] == expected
