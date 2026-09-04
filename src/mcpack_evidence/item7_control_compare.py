"""Compare the Item 7 retained control with the Chunky pilot selection."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar, Final, Literal, NoReturn, override

from pydantic import BaseModel, ConfigDict, ValidationError

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json
from mcpack_evidence.item7_nbt import ChunkRecord
from mcpack_evidence.item7_repeat import (
    field_mismatch_counts,
    normalized_chunk,
    normalized_sha256,
)

_FIELDS: Final = (
    "schema_version",
    "dimension",
    "slot",
    "chunk_x",
    "chunk_z",
    "data_version",
    "status",
    "full",
    "heightmaps",
    "biome_sections",
    "structure_starts",
)
_EXPECTED: Final = {("minecraft:overworld", x, z) for x in range(-4, 5) for z in range(-4, 5)}


@dataclass(frozen=True, slots=True)
class ControlComparisonInputs:
    """Filesystem inputs needed by the retained-control comparison."""

    control_root: Path
    pilot_root: Path
    repeat_comparison: Path
    output: Path


@dataclass(frozen=True, slots=True)
class ControlComparisonError(Exception):
    """One control evidence boundary failed."""

    issue: str
    subject: str

    @override
    def __str__(self) -> str:
        return f"Item 7 control comparison failed: {self.issue}: {self.subject}"


class _Model(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore", strict=True)


class _Preflight(_Model):
    seed: Literal["42"]
    java_version: Literal["Temurin-21.0.12.1+1-LTS"]
    retained_manifest_sha256: Literal[
        "78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb"
    ]
    frozen_manifest_sha256: Literal[
        "2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f"
    ]
    config_audit_sha256: Literal["181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd"]
    seed_suite_sha256: Literal["de5e5e89bd04b6f75dac4eab2e84524956f46faa91660b5315c8eade269d39ae"]


class _ControlPreflight(_Preflight):
    candidate_count: Literal[136]
    runtime_sha256: str


class _PilotPreflight(_Preflight):
    retained_candidate_count: Literal[136]
    instrumented_candidate_count: Literal[137]
    retained_runtime_sha256: str
    instrumented_runtime_sha256: str
    chunky_sha256: Literal["d72f235cf1f56f2c374f52c00bdda5034524b28142305a84cfc123a3f92ad274"]


class _Lifecycle(_Model):
    ready: Literal[True]
    save_all_flush: Literal[True]
    clean_stop: Literal[True]
    return_code: Literal[0]
    process_group_killed: Literal[False]
    rejection_reason: None


class _ControlReceipt(_Model):
    preflight: _ControlPreflight
    lifecycle: _Lifecycle
    rejection_reason: None


class _PilotReceipt(_Model):
    preflight: _PilotPreflight
    lifecycle: _Lifecycle
    rejection_reason: None


class _Repeat(_Model):
    schema_version: Literal["item7-repeat-comparison-v1"]
    equal: bool


def _fail(issue: str, subject: str | Path | tuple[str, int, int]) -> NoReturn:
    raise ControlComparisonError(issue, str(subject))


def _regular(path: Path) -> None:
    if path.is_symlink() or not path.is_file():
        _fail("input is not a regular file", path)


def _identity(path: Path, records: int) -> dict[str, str | int]:
    return {
        "path": path.name,
        "sha256": _sha256(path),
        "size_bytes": path.stat().st_size,
        "record_count": records,
    }


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _model[T: _Model](path: Path, model: type[T]) -> T:
    _regular(path)
    try:
        value = parse_strict_json(path.read_bytes())
        return model.model_validate_json(json.dumps(value, separators=(",", ":")), strict=True)
    except (OSError, StrictJsonError, ValidationError) as error:
        issue = "invalid strict receipt"
        raise ControlComparisonError(issue, str(path)) from error


def _records(path: Path) -> tuple[dict[tuple[str, int, int], ChunkRecord], int]:
    _regular(path)
    selected: dict[tuple[str, int, int], ChunkRecord] = {}
    total = 0
    try:
        with path.open("rb") as stream:
            for line_no, line in enumerate(stream, start=1):
                if not line.endswith(b"\n"):
                    _fail("decoded JSONL line lacks newline", str(line_no))
                value = parse_strict_json(line[:-1])
                record = ChunkRecord.model_validate_json(
                    json.dumps(value, separators=(",", ":")), strict=True
                )
                total += 1
                key = (record.dimension, record.chunk_x, record.chunk_z)
                if key in _EXPECTED:
                    if key in selected:
                        _fail("duplicate selected identity", key)
                    if not record.full or record.status != "minecraft:full":
                        _fail("selected identity is not minecraft:full", key)
                    selected[key] = record
    except (OSError, StrictJsonError, ValidationError) as error:
        issue = "invalid decoded JSONL"
        raise ControlComparisonError(issue, str(path)) from error
    missing = _EXPECTED - selected.keys()
    if missing:
        _fail("missing selected identity", min(missing))
    if selected.keys() != _EXPECTED:
        _fail("extra selected identity", "overworld -4..4 selection")
    return selected, total


def _write(output: Path, payload: dict[str, object]) -> None:
    if output.is_symlink() or output.parent.is_symlink():
        _fail("unsafe output path", output)
    output.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix=f".{output.name}.", dir=output.parent)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            _ = stream.write(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        _ = temporary.replace(output)
    except OSError as error:
        temporary.unlink(missing_ok=True)
        issue = "cannot write comparison receipt"
        raise ControlComparisonError(issue, str(output)) from error


def compare_control(inputs: ControlComparisonInputs) -> bool:
    """Validate, compare, and atomically emit the exact 81-chunk control result."""
    for root in (inputs.control_root, inputs.pilot_root):
        if root.is_symlink() or not root.is_dir():
            _fail("input root is not a real directory", root)
    control_receipt = inputs.control_root / "run-receipt.json"
    pilot_receipt = inputs.pilot_root / "run-receipt.json"
    control_chunks = inputs.control_root / "chunks.jsonl"
    pilot_chunks = inputs.pilot_root / "chunks.jsonl"
    repeat = _model(inputs.repeat_comparison, _Repeat)
    control_boundary = _model(control_receipt, _ControlReceipt)
    pilot_boundary = _model(pilot_receipt, _PilotReceipt)
    control, control_count = _records(control_chunks)
    pilot, pilot_count = _records(pilot_chunks)
    counts = field_mismatch_counts((control, pilot), _FIELDS)
    equal = not any(counts.values())
    if not equal and repeat.equal:
        _fail(
            "repeat receipt does not prove measured stack nondeterminism",
            inputs.repeat_comparison,
        )
    first: dict[str, str | int] | None = None
    for key in sorted(control):
        for field in _FIELDS:
            if normalized_chunk(control[key])[field] != normalized_chunk(pilot[key])[field]:
                first = {"dimension": key[0], "chunk_x": key[1], "chunk_z": key[2], "field": field}
                break
        if first is not None:
            break
    disposition = (
        "no_instrumentation_effect_observed"
        if equal
        else "not_attributable_due_to_measured_stack_nondeterminism"
    )
    payload: dict[str, object] = {
        "schema_version": "item7-control-comparison-v1",
        "selection": {
            "dimension": "minecraft:overworld",
            "minimum_chunk": -4,
            "maximum_chunk": 4,
            "expected_count": 81,
        },
        "control": {
            "run_receipt": _identity(control_receipt, 1),
            "chunks": _identity(control_chunks, control_count),
            "normalized_sha256": normalized_sha256(control),
            "preflight": control_boundary.preflight.model_dump(),
            "lifecycle": control_boundary.lifecycle.model_dump(),
        },
        "pilot": {
            "run_receipt": _identity(pilot_receipt, 1),
            "chunks": _identity(pilot_chunks, pilot_count),
            "normalized_sha256": normalized_sha256(pilot),
            "preflight": pilot_boundary.preflight.model_dump(),
            "lifecycle": pilot_boundary.lifecycle.model_dump(),
        },
        "repeat_comparison": _identity(inputs.repeat_comparison, 1),
        "equal": equal,
        "field_mismatch_counts": counts,
        "first_mismatch": first,
        "disposition": disposition,
    }
    _write(inputs.output, payload)
    return equal
