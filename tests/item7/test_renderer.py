from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import ClassVar

import pytest
from pydantic import BaseModel, ConfigDict, JsonValue
from tools.render_item7_world import read_region_hashes

from mcpack_evidence.item7_render import RenderInputError, RenderMetadata, render_jsonl

REGION_HASH = "a" * 64


class _ManifestMetadata(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True, strict=True)

    run_id: str
    seed_role: str
    seed: str
    dimension: str
    input_region_hashes: dict[str, str]
    chunks_sha256: str


class _Manifest(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True, strict=True)

    schema_version: str
    metadata: _ManifestMetadata
    artifact_hashes: dict[str, str]


def _metadata() -> RenderMetadata:
    return RenderMetadata(
        "run-a", "ordinary", "42", "minecraft:overworld", {"region/r.0.0.mca": REGION_HASH}
    )


def _record() -> str:
    heights: list[JsonValue] = [64 if index % 2 == 0 else 63 for index in range(256)]
    ocean_floor: list[JsonValue] = [62 for _ in range(256)]
    record = {
        "schema_version": "item7-anvil-chunk-v1",
        "dimension": "minecraft:overworld",
        "region": [0, 0],
        "slot": [0, 0],
        "timestamp": "2026-09-04T00:00:00Z",
        "chunk_x": 0,
        "chunk_z": 0,
        "data_version": 4189,
        "status": "minecraft:full",
        "full": True,
        "compression": 2,
        "external": False,
        "heightmaps": [
            {"name": "WORLD_SURFACE", "values": heights},
            {"name": "OCEAN_FLOOR", "values": ocean_floor},
        ],
        "biome_sections": [{"section_y": 3, "palette": ["minecraft:plains"], "indices": [0] * 64}],
        "structure_starts": [
            {
                "structure_id": "example:watchtower",
                "start_id": "watchtower-start",
                "boxes": [{"bounds": [1, 50, 1, 14, 90, 14]}],
            }
        ],
    }
    return json.dumps(record, sort_keys=True)


def _write_input(path: Path) -> None:
    _ = path.write_text(_record() + "\n", encoding="utf-8")


def _hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_renderer_emits_deterministic_gallery_and_hashed_manifest(tmp_path: Path) -> None:
    chunks = tmp_path / "chunks.jsonl"
    _write_input(chunks)
    source_hash = _hash(chunks)
    first, second = tmp_path / "first", tmp_path / "second"
    render_jsonl(chunks, first, _metadata(), expected_chunks_sha256=source_hash)
    render_jsonl(chunks, second, _metadata(), expected_chunks_sha256=source_hash)

    expected = ("index.html", "topdown.svg", "cross-section-x.svg", "cross-section-z.svg")
    assert all((first / name).is_file() for name in expected)
    assert {name: _hash(first / name) for name in expected} == {
        name: _hash(second / name) for name in expected
    }
    manifest = _Manifest.model_validate_json((first / "manifest.json").read_bytes())
    assert manifest.artifact_hashes == {name: _hash(first / name) for name in expected}
    assert manifest.metadata.input_region_hashes == {"region/r.0.0.mca": REGION_HASH}
    assert manifest.metadata.chunks_sha256 == source_hash


def test_renderer_marks_water_boxes_and_both_honest_cross_section_axes(tmp_path: Path) -> None:
    chunks = tmp_path / "chunks.jsonl"
    _write_input(chunks)
    output = tmp_path / "render"
    render_jsonl(chunks, output, _metadata())

    topdown = (output / "topdown.svg").read_text(encoding="utf-8")
    x_section = (output / "cross-section-x.svg").read_text(encoding="utf-8")
    z_section = (output / "cross-section-z.svg").read_text(encoding="utf-8")
    assert 'class="water-candidate"' in topdown
    assert 'fill="#1c' in topdown
    assert 'class="structure"' in topdown
    assert 'data-provider="example"' in topdown
    assert 'class="background"' in x_section
    assert 'data-axis="x" data-block-accurate="false"' in x_section
    assert 'data-axis="z" data-block-accurate="false"' in z_section
    assert "Heightmap-derived surface profile" in x_section


def test_renderer_rejects_stale_decoded_input_hash(tmp_path: Path) -> None:
    chunks = tmp_path / "chunks.jsonl"
    _write_input(chunks)

    with pytest.raises(RenderInputError, match="render input hash mismatch"):
        render_jsonl(chunks, tmp_path / "render", _metadata(), expected_chunks_sha256="b" * 64)


def test_renderer_streams_decoded_jsonl_without_reading_the_whole_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    chunks = tmp_path / "chunks.jsonl"
    _write_input(chunks)

    def reject_read_text(*_args: object, **_kwargs: object) -> str:
        message = "decoded JSONL must be streamed"
        raise AssertionError(message)

    monkeypatch.setattr(Path, "read_text", reject_read_text)

    render_jsonl(chunks, tmp_path / "render", _metadata())

    assert (tmp_path / "render/manifest.json").is_file()


def test_render_cli_derives_dimension_region_hashes_from_world_manifest(tmp_path: Path) -> None:
    manifest = tmp_path / "world-manifest.json"
    payload = {
        "schema_version": "item7-world-manifest-v1",
        "mode": "run",
        "regions": [
            {
                "path": "world/region/r.0.0.mca",
                "dimension": "minecraft:overworld",
                "region_x": 0,
                "region_z": 0,
                "size_bytes": 8192,
                "sha256": REGION_HASH,
                "zero_byte_placeholder": False,
                "decoded_chunk_count": 1,
            }
        ],
        "external_chunks": [],
        "selections": [],
        "extra_chunks": [],
        "decoded": {
            "path": "chunks.jsonl",
            "size_bytes": 1,
            "sha256": "b" * 64,
            "record_count": 1,
        },
    }
    _ = manifest.write_text(json.dumps(payload), encoding="utf-8")

    hashes = read_region_hashes(manifest, "minecraft:overworld")

    assert hashes == {"world/region/r.0.0.mca": REGION_HASH}
