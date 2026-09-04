#!/usr/bin/env python3
"""Compare exact normalized Item 7 Run A and Run B evidence."""

from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, NoReturn

from pydantic import ValidationError

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json
from mcpack_evidence.item7_nbt import ChunkRecord
from mcpack_evidence.item7_protocol import Item7Protocol
from mcpack_evidence.item7_repeat import (
    ChunkKey,
    ComparisonInputs,
    JsonValue,
    RepeatComparisonError,
    RepeatDecodedIdentity,
    RepeatRegion,
    RepeatWorldManifest,
    field_mismatch_counts,
    first_mismatch,
    normalized_sha256,
    write_receipt,
)

if TYPE_CHECKING:
    from collections.abc import Iterator


@dataclass(frozen=True, slots=True)
class _Geometry:
    protocol: Item7Protocol
    owners: dict[ChunkKey, int]
    expected: tuple[set[ChunkKey], ...]


def _fail(issue: str, subject: str | Path | ChunkKey) -> NoReturn:
    raise RepeatComparisonError(issue, str(subject))


def _strict_manifest(path: Path) -> RepeatWorldManifest:
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


def _geometry(protocol: Item7Protocol) -> _Geometry:
    owners: dict[ChunkKey, int] = {}
    expected: list[set[ChunkKey]] = []
    for index, selection in enumerate(protocol.selections):
        center_x, center_z = selection.center_x // 16, selection.center_z // 16
        radius = selection.radius_chunks
        coordinates = {
            (selection.dimension, x, z)
            for x in range(center_x - radius, center_x + radius + 1)
            for z in range(center_z - radius, center_z + radius + 1)
        }
        if owners.keys() & coordinates:
            _fail("overlapping protocol selections", selection.label)
        owners.update((coordinate, index) for coordinate in coordinates)
        expected.append(coordinates)
    return _Geometry(protocol, owners, tuple(expected))


def _validate_manifest(manifest: RepeatWorldManifest, protocol: Item7Protocol) -> None:
    if len(manifest.selections) != len(protocol.selections):
        _fail("stale manifest selections", "world-manifest.json")
    for actual, expected in zip(manifest.selections, protocol.selections, strict=True):
        identity = (
            actual.label,
            actual.dimension,
            actual.center_block_x,
            actual.center_block_z,
            actual.radius_chunks,
            actual.expected_chunk_count,
            actual.observed_chunk_count,
        )
        frozen = (
            expected.label,
            expected.dimension,
            expected.center_x,
            expected.center_z,
            expected.radius_chunks,
            expected.expected_chunk_count,
            expected.expected_chunk_count,
        )
        if identity != frozen:
            _fail("stale manifest selections", actual.label)
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


def _records(path: Path, seal: RepeatDecodedIdentity) -> Iterator[ChunkRecord]:
    digest = hashlib.sha256()
    size = 0
    count = 0
    try:
        with path.open("rb") as stream:
            for number, line in enumerate(stream, start=1):
                digest.update(line)
                size += len(line)
                try:
                    document = parse_strict_json(line)
                    encoded = json.dumps(document, separators=(",", ":"))
                    count += 1
                    yield ChunkRecord.model_validate_json(encoded, strict=True)
                except (StrictJsonError, ValidationError) as error:
                    issue, detail = "non-strict decoded record", f"{path}:{number}"
                    raise RepeatComparisonError(issue, detail) from error
    except OSError as error:
        issue = "cannot read decoded evidence"
        raise RepeatComparisonError(issue, str(path)) from error
    if (digest.hexdigest(), size, count) != (seal.sha256, seal.size_bytes, seal.record_count):
        _fail("stale decoded manifest", path)


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


def _load_seed(
    root: Path, role: str, geometry: _Geometry
) -> tuple[RepeatWorldManifest, tuple[dict[ChunkKey, ChunkRecord], ...]]:
    directory, manifest_path = _paths(root, role)
    manifest = _strict_manifest(manifest_path)
    _validate_manifest(manifest, geometry.protocol)
    decoded = _decoded(directory, manifest)
    selected: tuple[dict[ChunkKey, ChunkRecord], ...] = tuple({} for _ in geometry.expected)
    seen: set[ChunkKey] = set()
    count = 0
    for record in _records(decoded, manifest.decoded):
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
    for index, coordinates in enumerate(geometry.expected):
        missing = coordinates - selected[index].keys()
        if missing:
            _fail("missing selected chunk", min(missing))
    return manifest, selected


def _region(region: RepeatRegion) -> JsonValue:
    return parse_strict_json(region.model_dump_json().encode())


def compare_runs(inputs: ComparisonInputs) -> bool:
    """Validate, normalize, compare, and emit one four-seed receipt."""
    if inputs.protocol.is_symlink() or not inputs.protocol.is_file():
        _fail("protocol is not a regular file", inputs.protocol)
    try:
        protocol_bytes = inputs.protocol.read_bytes()
        protocol_document = parse_strict_json(protocol_bytes)
        protocol = Item7Protocol.model_validate_json(
            json.dumps(protocol_document, separators=(",", ":")), strict=True
        )
    except (OSError, StrictJsonError, ValidationError) as error:
        issue = "non-strict protocol"
        raise RepeatComparisonError(issue, str(inputs.protocol)) from error
    geometry = _geometry(protocol)
    seeds: list[JsonValue] = []
    first: dict[str, JsonValue] | None = None
    for seed in protocol.seeds:
        manifest_a, selected_a = _load_seed(inputs.run_a_root, seed.role, geometry)
        manifest_b, selected_b = _load_seed(inputs.run_b_root, seed.role, geometry)
        selections: list[JsonValue] = []
        for index, selection in enumerate(protocol.selections):
            left, right = selected_a[index], selected_b[index]
            mismatch_counts = field_mismatch_counts(
                (left, right), protocol.normalization.chunk_compare_fields
            )
            equal = not any(mismatch_counts.values())
            selections.append(
                {
                    "label": selection.label,
                    "count": len(left),
                    "run_a_normalized_sha256": normalized_sha256(left),
                    "run_b_normalized_sha256": normalized_sha256(right),
                    "equal": equal,
                    "field_mismatch_counts": mismatch_counts,
                }
            )
            if not equal and first is None:
                first = first_mismatch(
                    (seed.role, selection.label),
                    (left, right),
                    protocol.normalization.chunk_compare_fields,
                )
        seeds.append(
            {
                "role": seed.role,
                "seed": seed.seed,
                "selections": selections,
                "run_a_regions": [_region(row) for row in manifest_a.regions],
                "run_b_regions": [_region(row) for row in manifest_b.regions],
            }
        )
    payload: dict[str, JsonValue] = {
        "schema_version": "item7-repeat-comparison-v1",
        "protocol_sha256": hashlib.sha256(protocol_bytes).hexdigest(),
        "raw_region_hash_treatment": protocol.normalization.raw_region_hash_treatment,
        "equal": first is None,
        "seeds": seeds,
        "first_mismatch": first,
    }
    write_receipt(inputs.output, payload)
    return first is None


def _parse(argv: tuple[str, ...]) -> ComparisonInputs:
    flags = ("--protocol", "--run-a", "--run-b", "--output")
    if len(argv) != len(flags) * 2 or tuple(argv[::2]) != flags:
        usage = "usage: compare_item7_runs.py --protocol JSON --run-a DIR --run-b DIR --output JSON"
        raise SystemExit(usage)
    return ComparisonInputs(Path(argv[1]), Path(argv[3]), Path(argv[5]), Path(argv[7]))


def main(argv: tuple[str, ...] | None = None) -> int:
    """Run the exact comparison and return nonzero for semantic inequality."""
    arguments = tuple(sys.argv[1:]) if argv is None else argv
    return 0 if compare_runs(_parse(arguments)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
