from __future__ import annotations

import hashlib
import struct
import subprocess
import sys
import zlib
from collections import defaultdict
from typing import TYPE_CHECKING, Literal

import pytest
from pydantic import BaseModel

from mcpack_evidence.item7_selections import CONTROL_SELECTIONS, PILOT_SELECTIONS, WorldgenSelection
from mcpack_evidence.item7_world_manifest import WorldManifestError, build_world_manifest

if TYPE_CHECKING:
    from pathlib import Path


class _SelectionView(BaseModel):
    observed_chunk_count: int


class _RegionView(BaseModel):
    zero_byte_placeholder: bool


class _ExternalView(BaseModel):
    path: str


class _PayloadView(BaseModel):
    schema_version: Literal["item7-world-manifest-v1"]
    selections: tuple[_SelectionView, ...]
    regions: tuple[_RegionView, ...]
    external_chunks: tuple[_ExternalView, ...]
    extra_chunks: tuple[dict[str, str | int], ...]


SECTOR_BYTES = 4096


def _named(value: str) -> bytes:
    encoded = value.encode()
    return struct.pack(">H", len(encoded)) + encoded


def _chunk_nbt(chunk_x: int, chunk_z: int, status: str = "minecraft:full") -> bytes:
    def integer(name: str, value: int) -> bytes:
        return b"\x03" + _named(name) + struct.pack(">i", value)

    def text(name: str, value: str) -> bytes:
        return b"\x08" + _named(name) + _named(value)

    return (
        b"\x0a\x00\x00"
        + integer("DataVersion", 3955)
        + integer("xPos", chunk_x)
        + integer("zPos", chunk_z)
        + text("Status", status)
        + b"\x00"
    )


def _coordinates(selection: WorldgenSelection) -> set[tuple[int, int]]:
    center_x = selection.center_x // 16
    center_z = selection.center_z // 16
    radius = selection.radius_chunks
    return {
        (chunk_x, chunk_z)
        for chunk_x in range(center_x - radius, center_x + radius + 1)
        for chunk_z in range(center_z - radius, center_z + radius + 1)
    }


def _write_regions(
    directory: Path,
    coordinates: set[tuple[int, int]],
    *,
    external: tuple[int, int] | None = None,
    nonfull: tuple[int, int] | None = None,
) -> None:
    grouped: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
    for chunk_x, chunk_z in coordinates:
        grouped[(chunk_x // 32, chunk_z // 32)].append((chunk_x, chunk_z))
    directory.mkdir(parents=True, exist_ok=True)
    for (region_x, region_z), chunks in sorted(grouped.items()):
        header = bytearray(SECTOR_BYTES * 2)
        bodies: list[bytes] = []
        for sector_offset, (chunk_x, chunk_z) in enumerate(sorted(chunks), start=2):
            slot = (chunk_x % 32) + (chunk_z % 32) * 32
            status = "minecraft:carv" if (chunk_x, chunk_z) == nonfull else "minecraft:full"
            payload = zlib.compress(_chunk_nbt(chunk_x, chunk_z, status))
            is_external = (chunk_x, chunk_z) == external
            stored = bytes([0x82 if is_external else 0x02])
            if is_external:
                _ = directory.joinpath(f"c.{chunk_x}.{chunk_z}.mcc").write_bytes(payload)
            else:
                stored += payload
            struct.pack_into(">I", header, slot * 4, (sector_offset << 8) | 1)
            struct.pack_into(">I", header, SECTOR_BYTES + slot * 4, 123456)
            body = struct.pack(">I", len(stored)) + stored
            bodies.append(body + bytes(SECTOR_BYTES - len(body)))
        _ = directory.joinpath(f"r.{region_x}.{region_z}.mca").write_bytes(
            header + b"".join(bodies)
        )


def _pilot_world(
    root: Path,
    *,
    omit: tuple[str, int, int] | None = None,
    nonfull: tuple[str, int, int] | None = None,
) -> Path:
    world = root / "world"
    directories = {
        "minecraft:overworld": world / "region",
        "minecraft:the_nether": world / "DIM-1" / "region",
        "minecraft:the_end": world / "DIM1" / "region",
    }
    by_dimension: dict[str, set[tuple[int, int]]] = defaultdict(set)
    for selection in PILOT_SELECTIONS:
        by_dimension[selection.dimension].update(_coordinates(selection))
    if omit is not None:
        by_dimension[omit[0]].remove((omit[1], omit[2]))
    for dimension, coordinates in by_dimension.items():
        changed = None if nonfull is None or nonfull[0] != dimension else nonfull[1:]
        external = (0, 0) if dimension == "minecraft:overworld" else None
        _write_regions(directories[dimension], coordinates, external=external, nonfull=changed)
    (world / "region" / "r.2.-1.mca").touch()
    return world


def _control_world(root: Path) -> Path:
    world = root / "world"
    _write_regions(world / "region", _coordinates(CONTROL_SELECTIONS[0]))
    return world


def test_end_outer_block_center_maps_to_chunk_center_96() -> None:
    selection = PILOT_SELECTIONS[-1]

    coordinates = _coordinates(selection)

    assert (96, 0) in coordinates
    assert min(chunk_x for chunk_x, _ in coordinates) == 92
    assert max(chunk_x for chunk_x, _ in coordinates) == 100


def test_control_manifest_requires_only_the_81_chunk_overworld_selection(tmp_path: Path) -> None:
    world = _control_world(tmp_path)
    output = tmp_path / "manifest.json"
    decoded = tmp_path / "chunks.jsonl"

    manifest = build_world_manifest(world, output, decoded, mode="control")
    payload = _PayloadView.model_validate_json(output.read_bytes())

    assert manifest.record_count == 81
    assert tuple(row.observed_chunk_count for row in payload.selections) == (81,)


def test_manifest_is_deterministic_and_inventories_all_evidence(tmp_path: Path) -> None:
    world = _pilot_world(tmp_path)
    _write_regions(world / "region", {(100, 100)})
    output = tmp_path / "manifest.json"
    decoded = tmp_path / "chunks.jsonl"

    manifest = build_world_manifest(world, output, decoded, mode="pilot")
    first = (output.read_bytes(), decoded.read_bytes())
    manifest_again = build_world_manifest(world, output, decoded, mode="pilot")
    payload = _PayloadView.model_validate_json(output.read_bytes())

    assert (output.read_bytes(), decoded.read_bytes()) == first
    assert manifest == manifest_again
    assert sum(row.observed_chunk_count for row in payload.selections) == 324
    assert manifest.record_count == 325
    assert payload.extra_chunks == (
        {"dimension": "minecraft:overworld", "chunk_x": 100, "chunk_z": 100},
    )
    assert any(row.zero_byte_placeholder for row in payload.regions)
    assert payload.external_chunks[0].path == "region/c.0.0.mcc"
    assert manifest.decoded_sha256 == hashlib.sha256(decoded.read_bytes()).hexdigest()


def test_manifest_rejects_missing_selected_chunk(tmp_path: Path) -> None:
    world = _pilot_world(tmp_path, omit=("minecraft:overworld", 4, 4))
    manifest_path, decoded_path = tmp_path / "manifest.json", tmp_path / "chunks.jsonl"
    _ = manifest_path.write_bytes(b"old manifest")
    _ = decoded_path.write_bytes(b"old decoded")

    with pytest.raises(WorldManifestError, match="missing selected chunk"):
        _ = build_world_manifest(world, manifest_path, decoded_path, mode="pilot")
    assert (manifest_path.read_bytes(), decoded_path.read_bytes()) == (
        b"old manifest",
        b"old decoded",
    )


def test_manifest_rejects_selected_chunk_that_is_not_full(tmp_path: Path) -> None:
    world = _pilot_world(tmp_path, nonfull=("minecraft:the_nether", 0, 0))

    with pytest.raises(WorldManifestError, match="not minecraft:full"):
        _ = build_world_manifest(
            world, tmp_path / "manifest.json", tmp_path / "chunks.jsonl", mode="pilot"
        )


def test_manifest_rejects_symlink_and_nonzero_malformed_region(tmp_path: Path) -> None:
    world = tmp_path / "world"
    region = world / "region"
    region.mkdir(parents=True)
    target = tmp_path / "r.0.0.mca"
    _ = target.write_bytes(b"invalid")
    region.joinpath("r.0.0.mca").symlink_to(target)

    with pytest.raises(WorldManifestError, match="symlink"):
        _ = build_world_manifest(
            world, tmp_path / "manifest.json", tmp_path / "chunks.jsonl", mode="pilot"
        )

    region.joinpath("r.0.0.mca").unlink()
    _ = region.joinpath("r.0.0.mca").write_bytes(b"invalid")
    with pytest.raises(Exception, match="complete Anvil sector"):
        _ = build_world_manifest(
            world, tmp_path / "manifest.json", tmp_path / "chunks.jsonl", mode="pilot"
        )


def test_manifest_rejects_duplicate_region_coordinates(tmp_path: Path) -> None:
    region = tmp_path / "world" / "region"
    (region / "nested").mkdir(parents=True)
    (region / "r.0.0.mca").touch()
    (region / "nested" / "r.0.0.mca").touch()

    with pytest.raises(WorldManifestError, match="duplicate region coordinates"):
        _ = build_world_manifest(
            tmp_path / "world", tmp_path / "manifest.json", tmp_path / "chunks.jsonl", mode="pilot"
        )


def test_manifest_rejects_unreferenced_external_chunk(tmp_path: Path) -> None:
    world = _pilot_world(tmp_path)
    _ = world.joinpath("region/c.999.999.mcc").write_bytes(b"orphan")

    with pytest.raises(WorldManifestError, match="external inventory"):
        _ = build_world_manifest(
            world, tmp_path / "manifest.json", tmp_path / "chunks.jsonl", mode="pilot"
        )


def test_cli_writes_strict_manifest_and_decoded_jsonl(tmp_path: Path) -> None:
    world = _pilot_world(tmp_path)
    output = tmp_path / "manifest.json"
    decoded = tmp_path / "chunks.jsonl"

    completed = subprocess.run(  # noqa: S603 - sys.executable is the active uv environment.
        [
            sys.executable,
            "tools/build_item7_world_manifest.py",
            str(world),
            "--manifest",
            str(output),
            "--decoded",
            str(decoded),
            "--mode",
            "pilot",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0
    assert _PayloadView.model_validate_json(output.read_bytes()).schema_version == (
        "item7-world-manifest-v1"
    )
    assert len(decoded.read_text(encoding="utf-8").splitlines()) == 324
