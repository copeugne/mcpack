"""Saved block observations preserve missing evidence and bind world inputs."""

import hashlib
import json
from pathlib import Path
from typing import cast

import pytest
from tools.analyze_structure_density import (
    nonregistry_analysis,
    saved_block_at,
    saved_content_observations,
)

from tests.item7.anvil_support import packed_values
from tests.item10.test_density_census import make_region


def test_saved_palette_order_at_negative_coordinates() -> None:
    values = [0] * 4096
    values[15 + 16 * 2 + 256 * 3] = 1
    chunk = {
        "xPos": -1,
        "zPos": -2,
        "sections": [
            {
                "Y": -1,
                "block_states": {
                    "palette": [{"Name": "minecraft:air"}, {"Name": "supplementaries:urn"}],
                    "data": packed_values(tuple(values), 4),
                },
            }
        ],
    }
    assert saved_block_at(chunk, (-1, -13, -30)) == {"Name": "supplementaries:urn"}
    assert saved_block_at(chunk, (-2, -13, -30)) == {"Name": "minecraft:air"}
    assert saved_block_at(chunk, (-1, 0, -30)) is None
    with pytest.raises(ValueError, match="supplied chunk"):
        _ = saved_block_at(chunk, (0, -13, -30))


@pytest.mark.parametrize("external", [False, True])
def test_missing_blocks_and_chunks_remain_observations(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, *, external: bool
) -> None:
    _ = make_region(tmp_path, monkeypatch, external=external)
    manifest = {
        path.relative_to(tmp_path).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in (tmp_path / "region").iterdir()
    }
    result = saved_content_observations(
        tmp_path, {"minecraft:overworld": {(0, 0, 0), (16, 0, 0)}}, manifest, {}
    )
    observations = cast("list[dict[str, object]]", result["observations"])
    assert [row["unavailable_reason"] for row in observations] == [
        "MISSING_BLOCK_SECTION",
        "MISSING_CHUNK",
    ]
    assert len(cast("list[object]", result["anvil_inputs"])) == len(manifest)


def test_world_manifest_mismatch_rejects_observation(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _ = make_region(tmp_path, monkeypatch)
    with pytest.raises(ValueError, match="retained world manifest"):
        _ = saved_content_observations(tmp_path, {"minecraft:overworld": {(0, 0, 0)}}, {}, {})


def test_full_reader_reproduces_retained_urn_saved_states() -> None:
    root = Path(__file__).resolve().parents[2]
    custody = root / "evidence/raw/item10/urn-pilot-r1-custody"
    world = custody / "restored-world/world"
    if not world.is_dir():
        pytest.skip("Restored urn world is required for saved-content integration")
    manifest = cast(
        "dict[str, list[dict[str, str]]]",
        json.loads((custody / "restored/world-backup.json").read_text()),
    )
    expected = cast(
        "dict[str, dict[str, list[dict[str, object]]]]",
        json.loads((root / "evidence/item-10/urn-pilot-r1/write-corroboration.json").read_text()),
    )
    rows = expected["urn_capture"]["observations"]
    positions = {tuple(cast("list[int]", row["position"])) for row in rows}
    result = saved_content_observations(
        world,
        {"minecraft:overworld": cast("set[tuple[int, int, int]]", positions)},
        {row["path"]: row["sha256"] for row in manifest["world_files"]},
        {},
    )
    observed = {
        tuple(cast("list[int]", row["position"])): row["saved_state"]
        for row in cast("list[dict[str, object]]", result["observations"])
    }
    assert observed == {
        tuple(cast("list[int]", row["position"])): row["saved_state"] for row in rows
    }


def test_integrated_retained_urn_analysis_binds_census_and_preserves_failures() -> None:
    root = Path(__file__).resolve().parents[2]
    custody = root / "evidence/raw/item10/urn-pilot-r1-custody"
    world = custody / "restored-world/world"
    if not world.is_dir():
        pytest.skip("Restored urn evidence required")
    archive = root / "evidence/item-10/urn-pilot-r1/archive-manifest.json"
    result = nonregistry_analysis(
        world,
        custody / "restored",
        archive,
        {},
        {"overworld": ("minecraft:overworld", (-4, 4, -4, 4))},
        census_inputs=[],
    )
    attempts = cast("list[dict[str, object]]", result["attempts"])
    assert len(attempts) == 1291
    assert sum(row["outcome"] == "NO_CONTENT_OBSERVED" for row in attempts) == 1195
    assert (
        sum(cast("dict[str, int]", row["saved_block_checks"]).get("MATCH", 0) for row in attempts)
        == 429
    )
    assert result["status"] == "CANDIDATES_AWAITING_ACCEPTANCE"
    observations = cast("list[dict[str, object]]", result["location_observations"])
    assert sum(row["disposition"] == "OBSERVED_LOCATION" for row in observations) == 7
    with pytest.raises(ValueError, match="registry census inputs differ"):
        _ = nonregistry_analysis(
            world,
            custody / "restored",
            archive,
            {},
            {},
            census_inputs=[{"path": "region/r.0.0.mca", "sha256": "0" * 64}],
        )
