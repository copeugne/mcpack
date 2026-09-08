import json
from pathlib import Path
from typing import cast

import pytest
from tools.analyze_structure_density import census, main, start_origins

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
