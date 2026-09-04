"""Aggregate-world loading for the Item 7 repeat comparator."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import NoReturn

from pydantic import JsonValue, ValidationError

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json
from mcpack_evidence.item7_nbt import ChunkRecord
from mcpack_evidence.item7_protocol import Item7Protocol
from mcpack_evidence.item7_repeat import (
    ChunkKey,
    RepeatComparisonError,
    RepeatRegion,
    RepeatWorldManifest,
)

type SelectedRecords = tuple[dict[ChunkKey, ChunkRecord], ...]


@dataclass(frozen=True, slots=True)
class ComparisonGeometry:
    """Fixed chunk ownership generated from the frozen protocol."""

    protocol: Item7Protocol
    owners: dict[ChunkKey, int]
    expected: tuple[set[ChunkKey], ...]

    @classmethod
    def from_protocol(cls, protocol: Item7Protocol) -> ComparisonGeometry:
        """Construct nonoverlapping expected coordinate sets."""
        owners: dict[ChunkKey, int] = {}
        expected: list[set[ChunkKey]] = []
        for index, selection in enumerate(protocol.selections):
            center_x, center_z = selection.center_x // 16, selection.center_z // 16
            coordinates = {
                (selection.dimension, chunk_x, chunk_z)
                for chunk_x in range(
                    center_x - selection.radius_chunks, center_x + selection.radius_chunks + 1
                )
                for chunk_z in range(
                    center_z - selection.radius_chunks, center_z + selection.radius_chunks + 1
                )
            }
            if owners.keys() & coordinates:
                _fail("overlapping protocol selections", selection.label)
            owners.update((coordinate, index) for coordinate in coordinates)
            expected.append(coordinates)
        return cls(protocol, owners, tuple(expected))


def load_comparison_protocol(path: Path) -> tuple[Item7Protocol, str]:
    """Load the exact strict protocol and its byte identity."""
    if path.is_symlink() or not path.is_file():
        _fail("protocol is not a regular file", path)
    try:
        protocol_bytes = path.read_bytes()
        document = parse_strict_json(protocol_bytes)
        protocol = Item7Protocol.model_validate_json(
            json.dumps(document, separators=(",", ":")), strict=True
        )
    except (OSError, StrictJsonError, ValidationError) as error:
        issue = "non-strict protocol"
        raise RepeatComparisonError(issue, str(path)) from error
    return protocol, hashlib.sha256(protocol_bytes).hexdigest()


def load_aggregate_seed(
    root: Path, role: str, geometry: ComparisonGeometry, _: str
) -> tuple[dict[str, JsonValue], SelectedRecords]:
    """Load one stopped-world aggregate into fixed comparison selections."""
    directory, manifest_path = _paths(root, role)
    manifest = load_world_manifest(manifest_path)
    validate_world_manifest(manifest, geometry.protocol)
    decoded = _decoded(directory, manifest)
    selected: SelectedRecords = tuple({} for _ in geometry.expected)
    seen: set[ChunkKey] = set()
    count = 0
    for record in read_chunk_records(
        decoded,
        manifest.decoded.sha256,
        manifest.decoded.size_bytes,
        manifest.decoded.record_count,
    ):
        count += 1
        key = (record.dimension, record.chunk_x, record.chunk_z)
        if key in seen:
            _fail("duplicate decoded chunk", key)
        seen.add(key)
        owner = geometry.owners.get(key)
        if owner is not None:
            if not record.full or record.status != "minecraft:full":
                _fail("nonfull selected chunk", key)
            selected[owner][key] = record
    if count != manifest.decoded.record_count:
        _fail("stale decoded record count", decoded)
    _require_complete(selected, geometry.expected)
    return {"regions": [region_payload(row) for row in manifest.regions]}, selected


def _fail(issue: str, subject: str | Path | ChunkKey) -> NoReturn:
    raise RepeatComparisonError(issue, str(subject))


def load_world_manifest(path: Path) -> RepeatWorldManifest:
    """Parse one strict stopped-world manifest."""
    try:
        document = parse_strict_json(path.read_bytes())
        encoded = json.dumps(document, separators=(",", ":"))
        return RepeatWorldManifest.model_validate_json(encoded, strict=True)
    except OSError as error:
        issue = "cannot read evidence"
        raise RepeatComparisonError(issue, str(path)) from error
    except (StrictJsonError, ValidationError) as error:
        issue = "non-strict JSON"
        raise RepeatComparisonError(issue, str(path)) from error


def validate_world_manifest(manifest: RepeatWorldManifest, protocol: Item7Protocol) -> None:
    """Require a manifest to retain the frozen protocol geometry."""
    expected = tuple(
        (
            row.label,
            row.dimension,
            row.center_x,
            row.center_z,
            row.radius_chunks,
            row.expected_chunk_count,
            row.expected_chunk_count,
        )
        for row in protocol.selections
    )
    observed = tuple(
        (
            row.label,
            row.dimension,
            row.center_block_x,
            row.center_block_z,
            row.radius_chunks,
            row.expected_chunk_count,
            row.observed_chunk_count,
        )
        for row in manifest.selections
    )
    if observed != expected:
        _fail("stale manifest selections", "world-manifest.json")
    paths = [row.path for row in manifest.regions]
    if len(paths) != len(set(paths)):
        _fail("duplicate manifest region", "world-manifest.json")
    for row in manifest.regions:
        path = Path(row.path)
        if path.is_absolute() or ".." in path.parts or path.suffix != ".mca":
            _fail("escaped region path", row.path)
        if row.zero_byte_placeholder != (row.size_bytes == 0):
            _fail("stale manifest region kind", row.path)
    if sum(row.decoded_chunk_count for row in manifest.regions) != manifest.decoded.record_count:
        _fail("stale manifest region counts", "world-manifest.json")


def read_chunk_records(
    path: Path, sha256: str, size_bytes: int, record_count: int
) -> list[ChunkRecord]:
    """Parse and hash-bind one canonical decoded JSONL stream."""
    records: list[ChunkRecord] = []
    digest = hashlib.sha256()
    size = 0
    try:
        with path.open("rb") as stream:
            for number, line in enumerate(stream, start=1):
                digest.update(line)
                size += len(line)
                try:
                    document = parse_strict_json(line)
                    encoded = json.dumps(document, separators=(",", ":"))
                    records.append(ChunkRecord.model_validate_json(encoded, strict=True))
                except (StrictJsonError, ValidationError) as error:
                    issue = "non-strict decoded record"
                    raise RepeatComparisonError(issue, f"{path}:{number}") from error
    except OSError as error:
        issue = "cannot read decoded evidence"
        raise RepeatComparisonError(issue, str(path)) from error
    if (digest.hexdigest(), size, len(records)) != (sha256, size_bytes, record_count):
        _fail("stale decoded manifest", path)
    return records


def _paths(root: Path, role: str) -> tuple[Path, Path]:
    directory = root / role
    manifest_path = directory / "world-manifest.json"
    if root.is_symlink() or not root.is_dir() or directory.is_symlink():
        _fail("run root is not a real directory", root)
    if manifest_path.is_symlink() or not manifest_path.is_file():
        _fail("seed manifest is not a regular file", manifest_path)
    return directory, manifest_path


def _decoded(directory: Path, manifest: RepeatWorldManifest) -> Path:
    candidate = Path(manifest.decoded.path)
    if candidate.name != manifest.decoded.path or candidate.is_absolute():
        _fail("escaped decoded path", manifest.decoded.path)
    decoded = directory / candidate
    if decoded.is_symlink() or not decoded.is_file():
        _fail("decoded path is not a regular file", decoded)
    return decoded


def _require_complete(selected: SelectedRecords, expected: tuple[set[ChunkKey], ...]) -> None:
    for index, coordinates in enumerate(expected):
        missing = coordinates - selected[index].keys()
        if missing:
            _fail("missing selected chunk", min(missing))


def region_payload(region: RepeatRegion) -> dict[str, JsonValue]:
    """Return one stable JSON-compatible raw region identity."""
    payload = parse_strict_json(region.model_dump_json().encode())
    if not isinstance(payload, dict):
        _fail("invalid region payload", region.path)
    return payload
