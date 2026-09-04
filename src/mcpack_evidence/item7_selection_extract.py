"""Extract hash-bound renderer input from aggregate Item 7 world evidence."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar, Final, Literal, NoReturn, override

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json
from mcpack_evidence.item7_nbt import ChunkRecord
from mcpack_evidence.item7_protocol import Item7Protocol, load_protocol

__all__ = ("SelectionExtractError", "SelectionReceipt", "extract_selection")

_SHA256_LENGTH: Final = 64


@dataclass(frozen=True, slots=True)
class SelectionExtractError(Exception):
    """Report one unsafe or incomplete selection-evidence boundary."""

    issue: str
    subject: str

    @override
    def __str__(self) -> str:
        return f"Item 7 selection extraction failed: {self.issue}: {self.subject}"


class _FrozenModel(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)


class _Artifact(_FrozenModel):
    path: str
    size_bytes: int = Field(ge=0)
    sha256: str
    record_count: int = Field(ge=0)


class _ManifestSelection(_FrozenModel):
    label: Literal["overworld", "nether", "end-central", "end-outer"]
    dimension: Literal["minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"]
    center_block_x: int
    center_block_z: int
    radius_chunks: int = Field(gt=0)
    expected_chunk_count: int = Field(gt=0)
    observed_chunk_count: int = Field(ge=0)


class _WorldManifest(_FrozenModel):
    schema_version: Literal["item7-world-manifest-v1"]
    mode: Literal["control", "pilot", "run"]
    regions: tuple[dict[str, str | int | bool], ...]
    external_chunks: tuple[dict[str, str | int | bool], ...]
    selections: tuple[_ManifestSelection, ...]
    extra_chunks: tuple[dict[str, str | int], ...]
    decoded: _Artifact


class SelectionReceipt(_FrozenModel):
    """Identity receipt for one renderer-ready selection JSONL artifact."""

    schema_version: Literal["item7-selection-extract-receipt-v1"]
    protocol: _Artifact
    world_manifest: _Artifact
    aggregate: _Artifact
    selection: _ManifestSelection
    selected: _Artifact


type _ChunkKey = tuple[str, int, int]


def _fail(issue: str, subject: str | Path | int | _ChunkKey) -> NoReturn:
    raise SelectionExtractError(issue, str(subject))


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _identity(path: Path, record_count: int) -> _Artifact:
    return _Artifact(
        path=path.as_posix(),
        size_bytes=path.stat().st_size,
        sha256=_sha256(path),
        record_count=record_count,
    )


def _strict_model(path: Path, model: type[_WorldManifest]) -> _WorldManifest:
    try:
        document = parse_strict_json(path.read_bytes())
        return model.model_validate_json(json.dumps(document, separators=(",", ":")), strict=True)
    except (OSError, StrictJsonError, ValidationError):
        _fail("invalid strict world manifest", path)


def _safe_decoded_path(manifest: Path, aggregate: Path, claimed: str) -> None:
    relative = Path(claimed)
    if relative.is_absolute() or ".." in relative.parts:
        _fail("decoded path escapes manifest directory", claimed)
    expected = manifest.parent / relative
    if aggregate.is_symlink() or aggregate.resolve() != expected.resolve():
        _fail("aggregate path does not match manifest decoded path", aggregate)


def _validate_sha256(value: str, subject: str) -> None:
    if len(value) != _SHA256_LENGTH or any(
        character not in "0123456789abcdef" for character in value
    ):
        _fail("invalid SHA-256 identity", subject)


def _selection(protocol: Item7Protocol, manifest: _WorldManifest, label: str) -> _ManifestSelection:
    expected = tuple(protocol.selections)
    actual = manifest.selections
    if len(actual) != len(expected):
        _fail("manifest selection count differs from protocol", len(actual))
    for requirement, observed in zip(expected, actual, strict=True):
        requirement_fields = (
            requirement.label,
            requirement.dimension,
            requirement.center_x,
            requirement.center_z,
            requirement.radius_chunks,
            requirement.expected_chunk_count,
        )
        observed_fields = (
            observed.label,
            observed.dimension,
            observed.center_block_x,
            observed.center_block_z,
            observed.radius_chunks,
            observed.expected_chunk_count,
        )
        selection_complete = observed.observed_chunk_count == requirement.expected_chunk_count
        if requirement_fields != observed_fields or not selection_complete:
            _fail("manifest selection geometry differs from protocol", observed.label)
    for observed in actual:
        if observed.label == label:
            return observed
    _fail("selection label is absent from frozen protocol", label)


def _coordinates(selection: _ManifestSelection) -> set[_ChunkKey]:
    center_x, center_z = selection.center_block_x // 16, selection.center_block_z // 16
    return {
        (selection.dimension, chunk_x, chunk_z)
        for chunk_x in range(
            center_x - selection.radius_chunks, center_x + selection.radius_chunks + 1
        )
        for chunk_z in range(
            center_z - selection.radius_chunks, center_z + selection.radius_chunks + 1
        )
    }


def _record(line: bytes, line_number: int) -> ChunkRecord:
    if not line.endswith(b"\n"):
        _fail("aggregate JSONL line lacks newline", line_number)
    try:
        document = parse_strict_json(line[:-1])
        encoded = json.dumps(document, separators=(",", ":"))
        return ChunkRecord.model_validate_json(encoded, strict=True)
    except (StrictJsonError, ValidationError):
        _fail("invalid aggregate JSONL record", line_number)


def _write_selection(
    aggregate: Path, selection: _ManifestSelection, destination: Path
) -> tuple[int, str, str]:
    expected: set[_ChunkKey] = _coordinates(selection)
    seen: set[_ChunkKey] = set()
    digest, aggregate_digest, total = hashlib.sha256(), hashlib.sha256(), 0
    with aggregate.open("rb") as source, destination.open("wb") as output:
        for line_number, line in enumerate(source, start=1):
            aggregate_digest.update(line)
            record = _record(line, line_number)
            key: _ChunkKey = (record.dimension, record.chunk_x, record.chunk_z)
            if key in seen:
                _fail("duplicate aggregate chunk coordinate", line_number)
            seen.add(key)
            total += 1
            if key not in expected:
                continue
            if not record.full or record.status != "minecraft:full":
                _fail("selected chunk is not minecraft:full", line_number)
            encoded = (record.model_dump_json() + "\n").encode()
            _ = output.write(encoded)
            digest.update(encoded)
    missing = expected - seen
    if missing:
        _fail("missing frozen selection coordinate", min(missing))
    return total, aggregate_digest.hexdigest(), digest.hexdigest()


def _temporary(path: Path) -> Path:
    descriptor, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    os.close(descriptor)
    return Path(name)


def _unchanged(path: Path, identity: _Artifact) -> None:
    if path.stat().st_size != identity.size_bytes or _sha256(path) != identity.sha256:
        _fail("bound input changed during extraction", path)


def extract_selection(
    protocol_path: Path, manifest_path: Path, aggregate_path: Path, label: str, output_path: Path
) -> SelectionReceipt:
    """Emit one complete canonical selection JSONL and its bound receipt atomically."""
    if protocol_path.is_symlink() or manifest_path.is_symlink() or not aggregate_path.is_file():
        _fail("input path is not a real regular evidence file", aggregate_path)
    protocol_identity, manifest_identity = _identity(protocol_path, 1), _identity(manifest_path, 1)
    protocol, manifest = load_protocol(protocol_path), _strict_model(manifest_path, _WorldManifest)
    _unchanged(protocol_path, protocol_identity)
    _unchanged(manifest_path, manifest_identity)
    _safe_decoded_path(manifest_path, aggregate_path, manifest.decoded.path)
    _validate_sha256(manifest.decoded.sha256, manifest.decoded.path)
    selection = _selection(protocol, manifest, label)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    selected_temp = _temporary(output_path)
    receipt_path = output_path.with_suffix(f"{output_path.suffix}.receipt.json")
    receipt_temp = _temporary(receipt_path)
    try:
        total, aggregate_sha256, selected_sha256 = _write_selection(
            aggregate_path, selection, selected_temp
        )
        selected_size = selected_temp.stat().st_size
        if (total, aggregate_path.stat().st_size, aggregate_sha256) != (
            manifest.decoded.record_count,
            manifest.decoded.size_bytes,
            manifest.decoded.sha256,
        ):
            _fail("aggregate bytes differ from world manifest", aggregate_path)
        _unchanged(protocol_path, protocol_identity)
        _unchanged(manifest_path, manifest_identity)
        receipt = SelectionReceipt(
            schema_version="item7-selection-extract-receipt-v1",
            protocol=protocol_identity,
            world_manifest=manifest_identity.model_copy(update={"path": manifest_path.name}),
            aggregate=_Artifact(
                path=manifest.decoded.path,
                size_bytes=manifest.decoded.size_bytes,
                sha256=aggregate_sha256,
                record_count=total,
            ),
            selection=_ManifestSelection(
                label=selection.label,
                dimension=selection.dimension,
                center_block_x=selection.center_block_x,
                center_block_z=selection.center_block_z,
                radius_chunks=selection.radius_chunks,
                expected_chunk_count=selection.expected_chunk_count,
                observed_chunk_count=selection.expected_chunk_count,
            ),
            selected=_Artifact(
                path=output_path.name,
                size_bytes=selected_size,
                sha256=selected_sha256,
                record_count=selection.expected_chunk_count,
            ),
        )
        _ = receipt_temp.write_text(
            receipt.model_dump_json(indent=2) + "\n", encoding="utf-8", newline="\n"
        )
        _ = selected_temp.replace(output_path)
        _ = receipt_temp.replace(receipt_path)
    except OSError:
        _fail("selection artifact publication failed", output_path)
    finally:
        selected_temp.unlink(missing_ok=True)
        receipt_temp.unlink(missing_ok=True)
    return receipt
