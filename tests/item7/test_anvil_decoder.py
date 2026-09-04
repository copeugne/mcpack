from __future__ import annotations

import struct
import subprocess
import sys
from pathlib import Path

import pytest

from mcpack_evidence.item7_anvil import RegionDecodeError, decode_region
from mcpack_evidence.item7_nbt import ChunkRecord, ChunkSource, decode_chunk_nbt
from tests.item7.anvil_support import (
    SECTOR_BYTES,
    ChunkFixture,
    compound,
    integer,
    string,
    tag,
    write_region,
)


@pytest.mark.parametrize("method", [1, 2, 3, 4])
def test_chunk_is_decoded_when_region_uses_supported_compression(
    tmp_path: Path, method: int
) -> None:
    region = tmp_path / "r.-1.-2.mca"
    fixture = ChunkFixture(slot=31, chunk_x=-1, chunk_z=-64, compression=method)
    write_region(region, fixture)

    records = tuple(decode_region(region))

    assert len(records) == 1
    record = records[0]
    assert (record.chunk_x, record.chunk_z, record.status, record.full) == (
        -1,
        -64,
        "minecraft:full",
        True,
    )
    assert record.heightmaps[0].values == (0,) * 256
    assert record.biome_sections[0].indices == tuple(index % 2 for index in range(64))
    assert record.structure_starts[0].boxes[0].bounds == (0, 60, 0, 15, 80, 15)


def test_chunk_is_decoded_when_payload_is_external(tmp_path: Path) -> None:
    region = tmp_path / "r.0.0.mca"
    fixture = ChunkFixture(slot=0, chunk_x=0, chunk_z=0, compression=2, external=True)
    write_region(region, fixture)

    record = next(decode_region(region))

    assert record.external is True
    assert record.compression == "zlib"


def test_region_is_rejected_when_slots_overlap(tmp_path: Path) -> None:
    region = tmp_path / "r.0.0.mca"
    write_region(region, ChunkFixture(slot=0, chunk_x=0, chunk_z=0, compression=2))
    data = bytearray(region.read_bytes())
    struct.pack_into(">I", data, 4, struct.unpack_from(">I", data, 0)[0])
    _ = region.write_bytes(data)

    with pytest.raises(RegionDecodeError, match="overlap"):
        _ = tuple(decode_region(region))


def test_zero_byte_region_placeholder_decodes_no_chunks(tmp_path: Path) -> None:
    region = tmp_path / "r.2.-1.mca"
    region.touch()

    assert tuple(decode_region(region)) == ()


def test_region_is_rejected_when_slot_coordinates_disagree(tmp_path: Path) -> None:
    region = tmp_path / "r.0.0.mca"
    write_region(region, ChunkFixture(slot=0, chunk_x=1, chunk_z=0, compression=2))

    with pytest.raises(RegionDecodeError, match="coordinate"):
        _ = tuple(decode_region(region))


def test_region_is_rejected_when_external_slot_contains_inline_bytes(tmp_path: Path) -> None:
    region = tmp_path / "r.0.0.mca"
    write_region(
        region,
        ChunkFixture(slot=0, chunk_x=0, chunk_z=0, compression=2, external=True),
    )
    data = bytearray(region.read_bytes())
    struct.pack_into(">I", data, SECTOR_BYTES * 2, 2)
    _ = region.write_bytes(data)

    with pytest.raises(RegionDecodeError, match="external"):
        _ = tuple(decode_region(region))


def test_jsonl_is_stable_when_cli_decodes_world(tmp_path: Path) -> None:
    world = tmp_path / "world"
    region_dir = world / "region"
    region_dir.mkdir(parents=True)
    write_region(
        region_dir / "r.0.0.mca",
        ChunkFixture(slot=0, chunk_x=0, chunk_z=0, compression=2),
    )
    first = tmp_path / "first.jsonl"
    second = tmp_path / "second.jsonl"
    command = ["uv", "run", "tools/decode_item7_world.py", str(world)]

    first_run = subprocess.run(
        [*command, "--output", str(first)], check=False, capture_output=True, text=True
    )
    second_run = subprocess.run(
        [*command, "--output", str(second)], check=False, capture_output=True, text=True
    )

    assert first_run.returncode == second_run.returncode == 0
    assert first.read_bytes() == second.read_bytes()
    row = ChunkRecord.model_validate_json(first.read_text(encoding="utf-8"))
    assert row.schema_version == "item7-anvil-chunk-v1"


def test_nbt_string_length_uses_unsigned_short_encoding() -> None:
    payload = compound(
        "",
        (
            string("large", "x" * 32768),
            integer("xPos", 0),
            integer("zPos", 0),
            string("Status", "minecraft:full"),
        ),
    )
    source = ChunkSource(
        dimension="minecraft:overworld",
        region="region/r.0.0.mca",
        slot=0,
        timestamp=0,
        compression="raw",
        external=False,
        min_y=-64,
        build_height=384,
    )

    record = decode_chunk_nbt(payload, source)

    assert record.full is True


def test_nbt_string_accepts_java_modified_utf8_surrogate_pair() -> None:
    modified_utf8_emoji = struct.pack(">H", 6) + b"\xed\xa0\xbd\xed\xb8\x80"
    payload = compound(
        "",
        (
            tag(8, "note", modified_utf8_emoji),
            integer("xPos", 0),
            integer("zPos", 0),
            string("Status", "minecraft:full"),
        ),
    )
    source = ChunkSource(
        dimension="minecraft:overworld",
        region="region/r.0.0.mca",
        slot=0,
        timestamp=0,
        compression="raw",
        external=False,
        min_y=-64,
        build_height=384,
    )

    record = decode_chunk_nbt(payload, source)

    assert record.full is True


def test_cli_does_not_replace_output_when_decode_fails(tmp_path: Path) -> None:
    world = tmp_path / "world"
    region_dir = world / "region"
    region_dir.mkdir(parents=True)
    write_region(
        region_dir / "r.0.0.mca",
        ChunkFixture(slot=0, chunk_x=1, chunk_z=0, compression=2),
    )
    output = tmp_path / "chunks.jsonl"
    _ = output.write_text("preserved\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, "tools/decode_item7_world.py", str(world), "--output", str(output)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert output.read_text(encoding="utf-8") == "preserved\n"
