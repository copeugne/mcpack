import json
from pathlib import Path
from typing import cast

import pytest
from tools.analyze_structure_density import census, classify_census, main, start_origins

from mcpack_evidence.item7_anvil import decode_region, decode_region_payloads
from tests.item7 import anvil_support


def make_region(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, *, external: bool = False) -> Path:
    original = anvil_support.chunk_nbt
    marker = anvil_support.string("id", "minecraft:village_plains")

    def with_origins(x: int, z: int) -> bytes:
        return original(x, z).replace(
            marker, marker + anvil_support.integer("ChunkX", x) + anvil_support.integer("ChunkZ", z)
        )

    monkeypatch.setattr(anvil_support, "chunk_nbt", with_origins)
    directory = tmp_path / "region"
    directory.mkdir()
    region = directory / "r.0.0.mca"
    anvil_support.write_region(region, anvil_support.ChunkFixture(0, 0, 0, 2, external=external))
    return region


def test_raw_payload_access_preserves_original_normalized_output(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    region = make_region(tmp_path, monkeypatch)
    ((record, payload),) = tuple(decode_region_payloads(region))
    assert (record,) == tuple(decode_region(region))
    assert start_origins(payload, (0, 0)) == [
        {"registry_id": "minecraft:village_plains", "chunk_x": 0, "chunk_z": 0}
    ]


@pytest.mark.parametrize("external", [False, True])
def test_census_counts_complete_selected_chunks(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, external: bool
) -> None:
    _ = make_region(tmp_path, monkeypatch, external=external)
    result = census(tmp_path, "minecraft:overworld", (0, 0, 0, 0), {})
    assert result["full_chunks"] == 1
    assert result["total_starts"] == 1
    assert result["starts_per_1000_chunks"] == 1000
    inputs = result["anvil_inputs"]
    assert isinstance(inputs, list)
    assert len(cast("list[object]", inputs)) == (2 if external else 1)


def test_missing_selected_chunk_cannot_shrink_the_denominator(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _ = make_region(tmp_path, monkeypatch)
    with pytest.raises(ValueError, match="1 of 2 full chunks"):
        _ = census(tmp_path, "minecraft:overworld", (0, 1, 0, 0), {})


def test_wrong_dimension_cannot_supply_the_denominator(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _ = make_region(tmp_path, monkeypatch)
    with pytest.raises(ValueError, match="0 of 1 full chunks"):
        _ = census(tmp_path, "minecraft:the_end", (0, 0, 0, 0), {})


def test_missing_authoritative_origin_is_not_inferred() -> None:
    with pytest.raises(ValueError, match="authoritative chunk"):
        _ = start_origins(anvil_support.chunk_nbt(0, 0), (0, 0))


def test_inconsistent_authoritative_origin_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    region = make_region(tmp_path, monkeypatch)
    ((_, payload),) = tuple(decode_region_payloads(region))
    with pytest.raises(ValueError, match="authoritative chunk"):
        _ = start_origins(payload, (1, 0))


def test_nonfull_selected_chunk_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    region = make_region(tmp_path, monkeypatch)
    original = anvil_support.chunk_nbt

    def nonfull(x: int, z: int) -> bytes:
        return original(x, z).replace(
            anvil_support.string("Status", "minecraft:full"),
            anvil_support.string("Status", "minecraft:features"),
        )

    monkeypatch.setattr(anvil_support, "chunk_nbt", nonfull)
    anvil_support.write_region(region, anvil_support.ChunkFixture(0, 0, 0, 2))
    with pytest.raises(ValueError, match="incomplete or duplicated"):
        _ = census(tmp_path, "minecraft:overworld", (0, 0, 0, 0), {})


def test_cli_writes_new_output_and_refuses_overwrite(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    world = tmp_path / "world"
    world.mkdir()
    _ = make_region(world, monkeypatch)
    output = tmp_path / "result.json"
    monkeypatch.setattr(
        "sys.argv",
        [
            "census",
            str(world),
            str(output),
            "--dimension",
            "minecraft:overworld",
            "--bounds",
            "0",
            "0",
            "0",
            "0",
        ],
    )
    main()
    original = output.read_bytes()
    assert json.loads(original)["full_chunks"] == 1
    with pytest.raises(SystemExit):
        main()
    assert output.read_bytes() == original


def test_classification_preserves_distinct_starts_in_one_canonical_family() -> None:
    measured: dict[str, object] = {
        "full_chunks": 1000,
        "occurrences": [
            {"registry_id": "minecraft:shipwreck", "chunk_x": 0, "chunk_z": 0},
            {"registry_id": "minecraft:shipwreck_beached", "chunk_x": 1, "chunk_z": 0},
        ],
    }
    before = json.dumps(measured)
    result = classify_census(measured)
    rows = cast("list[dict[str, object]]", result["occurrences"])
    assert len(rows) == 2
    assert {row["family_id"] for row in rows} == {"minecraft:shipwreck"}
    assert all(row["confidence"] and row["ambiguity"] for row in rows)
    counts = cast("dict[str, dict[str, float]]", result["exclusive_roles"])
    assert sum(row["count"] for row in counts.values()) == 2
    assert sum(row["per_1000_chunks"] for row in counts.values()) == 2
    assert json.dumps(measured) == before


def test_classification_does_not_silently_drop_unmapped_observations() -> None:
    with pytest.raises(ValueError, match="outside accepted active families"):
        _ = classify_census(
            {
                "full_chunks": 1,
                "occurrences": [{"registry_id": "unknown:start", "chunk_x": 0, "chunk_z": 0}],
            }
        )


def test_combined_classification_counts_only_observed_nonregistry_locations() -> None:
    location = {
        "candidate_id": 0,
        "family": "supplementaries:cave_urn_cache",
        "dimension": "minecraft:overworld",
        "chunk_x": 0,
        "chunk_z": 0,
        "anchor_x": 3,
        "anchor_y": 40,
        "anchor_z": 7,
    }
    measured: dict[str, object] = {
        "full_chunks": 1,
        "dimension": "minecraft:overworld",
        "bounds_chunks": [0, 0, 0, 0],
        "occurrences": [{"registry_id": "minecraft:shipwreck", "chunk_x": 0, "chunk_z": 0}],
        "nonregistry_candidates": {
            "locations": [location, {**location, "candidate_id": 1}],
            "location_observations": [
                {"candidate_id": 0, "disposition": "OBSERVED_LOCATION"},
                {"candidate_id": 1, "disposition": "OVERLAP_REVIEW_REQUIRED"},
            ],
        },
    }
    before = json.dumps(measured)
    result = classify_census(measured)
    categories = cast("dict[str, dict[str, float]]", result["categories"])
    assert categories["all_locations"] == {"count": 2, "per_1000_chunks": 2000}
    assert "all_registry" not in categories
    rows = cast("list[dict[str, object]]", result["occurrences"])
    assert rows[1]["family_id"] == "supplementaries:cave_urn_cache"
    assert rows[1]["anchor_x"] == 3
    assert json.dumps(measured) == before
    location["dimension"] = "minecraft:the_end"
    with pytest.raises(ValueError, match="census dimension"):
        _ = classify_census(measured)


def test_classification_rejects_changed_upstream_identity(monkeypatch: pytest.MonkeyPatch) -> None:
    original = Path.read_bytes

    def altered(path: Path) -> bytes:
        return original(path) + b"\n" if path.name == "classification.md" else original(path)

    monkeypatch.setattr(Path, "read_bytes", altered)
    with pytest.raises(ValueError, match="input identity changed"):
        _ = classify_census({"full_chunks": 1, "occurrences": []})
