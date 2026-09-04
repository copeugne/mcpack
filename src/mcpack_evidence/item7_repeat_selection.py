"""Selection-stream loading for Item 7 repeat completion."""

from __future__ import annotations

from pathlib import Path  # noqa: TC003
from typing import TYPE_CHECKING

from mcpack_evidence.item7_completion_io import fail, require_regular, strict_model
from mcpack_evidence.item7_repeat import ChunkKey, RepeatWorldManifest
from mcpack_evidence.item7_repeat_aggregate import (
    ComparisonGeometry,
    SelectedRecords,
    read_chunk_records,
    region_payload,
    validate_world_manifest,
)
from mcpack_evidence.item7_selection_extract import SelectionReceipt

if TYPE_CHECKING:
    from pydantic import JsonValue

    from mcpack_evidence.item7_nbt import ChunkRecord


def load_selection_seed(
    root: Path, role: str, geometry: ComparisonGeometry, protocol_sha256: str
) -> tuple[dict[str, JsonValue], SelectedRecords]:
    """Load one run role from all accepted canonical selection streams."""
    seed_root = root / role
    manifest = _manifest(seed_root / "world-manifest.json", geometry)
    selected = tuple(
        _selection_records(
            seed_root / "selections" / f"{selection.label}.jsonl",
            (
                selection.label,
                selection.dimension,
                selection.center_x,
                selection.center_z,
                selection.radius_chunks,
                selection.expected_chunk_count,
            ),
            protocol_sha256,
        )
        for selection in geometry.protocol.selections
    )
    return {"regions": [region_payload(row) for row in manifest.regions]}, selected


def _manifest(path: Path, geometry: ComparisonGeometry) -> RepeatWorldManifest:
    manifest = strict_model(path, RepeatWorldManifest)
    validate_world_manifest(manifest, geometry.protocol)
    return manifest


def _selection_records(
    path: Path,
    expected: tuple[str, str, int, int, int, int],
    protocol_sha256: str,
) -> dict[ChunkKey, ChunkRecord]:
    label, dimension, center_x, center_z, radius, expected_count = expected
    receipt = strict_model(path.with_suffix(".jsonl.receipt.json"), SelectionReceipt)
    selection = receipt.selection
    geometry = (
        selection.label,
        selection.dimension,
        selection.center_block_x,
        selection.center_block_z,
        selection.radius_chunks,
        selection.expected_chunk_count,
        selection.observed_chunk_count,
    )
    if (
        geometry != (label, dimension, center_x, center_z, radius, expected_count, expected_count)
        or receipt.protocol.sha256 != protocol_sha256
        or receipt.selected.path != path.name
        or receipt.selected.record_count != expected_count
    ):
        fail("repeat selection source identity", path)
    require_regular(path)
    records = read_chunk_records(
        path,
        receipt.selected.sha256,
        receipt.selected.size_bytes,
        receipt.selected.record_count,
    )
    coordinates = {
        (dimension, chunk_x, chunk_z)
        for chunk_x in range(center_x // 16 - radius, center_x // 16 + radius + 1)
        for chunk_z in range(center_z // 16 - radius, center_z // 16 + radius + 1)
    }
    selected: dict[ChunkKey, ChunkRecord] = {}
    for record in records:
        key = (record.dimension, record.chunk_x, record.chunk_z)
        if key in selected or key not in coordinates or not record.full:
            fail("repeat selection records", path)
        if record.status != "minecraft:full":
            fail("repeat selection records", path)
        selected[key] = record
    if len(selected) != expected_count or set(selected) != coordinates:
        fail("repeat selection records", path)
    return selected
