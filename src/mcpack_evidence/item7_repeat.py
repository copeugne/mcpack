"""Compare normalized Item 7 run evidence."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, Final, Literal, final, override

from pydantic import BaseModel, ConfigDict, Field

from mcpack_evidence.item6_json import parse_strict_json

if TYPE_CHECKING:
    from mcpack_evidence.item7_nbt import ChunkRecord

type JsonValue = str | int | float | bool | list[JsonValue] | dict[str, JsonValue] | None
type ChunkKey = tuple[str, int, int]
type Dimension = Literal["minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"]
_SHA256: Final = r"^[0-9a-f]{64}$"


class _FrozenModel(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)


class RepeatRegion(_FrozenModel):
    """One region identity preserved but excluded from semantic comparison."""

    path: str
    dimension: Dimension
    region_x: int
    region_z: int
    size_bytes: int = Field(ge=0)
    sha256: str = Field(pattern=_SHA256)
    zero_byte_placeholder: bool
    decoded_chunk_count: int = Field(ge=0)


class RepeatExternalChunk(_FrozenModel):
    """One external Anvil payload identity."""

    path: str
    dimension: Dimension
    chunk_x: int
    chunk_z: int
    size_bytes: int = Field(ge=0)
    sha256: str = Field(pattern=_SHA256)


class RepeatSelection(_FrozenModel):
    """One fixed selection summary from a stopped-world manifest."""

    label: str
    dimension: Dimension
    center_block_x: int
    center_block_z: int
    radius_chunks: int
    expected_chunk_count: int
    observed_chunk_count: int


class RepeatExtraChunk(_FrozenModel):
    """One decoded chunk outside the fixed comparison geometry."""

    dimension: Dimension
    chunk_x: int
    chunk_z: int


class RepeatDecodedIdentity(_FrozenModel):
    """Hash-bound decoded JSON Lines identity."""

    path: str
    size_bytes: int = Field(ge=0)
    sha256: str = Field(pattern=_SHA256)
    record_count: int = Field(ge=0)


class RepeatWorldManifest(_FrozenModel):
    """Strict stopped-world manifest accepted by the repeat comparator."""

    schema_version: Literal["item7-world-manifest-v1"]
    mode: Literal["run"]
    regions: tuple[RepeatRegion, ...]
    external_chunks: tuple[RepeatExternalChunk, ...]
    selections: tuple[RepeatSelection, ...]
    extra_chunks: tuple[RepeatExtraChunk, ...]
    decoded: RepeatDecodedIdentity


@dataclass(frozen=True, slots=True)
class ComparisonInputs:
    """Paths required for one complete Run A versus Run B comparison."""

    protocol: Path
    run_a_root: Path
    run_b_root: Path
    output: Path


@final
class RepeatComparisonError(Exception):
    """A repeat-comparison evidence boundary failed."""

    __slots__ = ("issue", "subject")

    def __init__(self, issue: str, subject: str) -> None:
        """Create a typed evidence-boundary failure."""
        super().__init__(issue, subject)
        self.issue = issue
        self.subject = subject

    @override
    def __str__(self) -> str:
        return f"{self.issue}: {self.subject}"


def normalized_chunk(record: ChunkRecord) -> dict[str, JsonValue]:
    """Project a decoded record onto the protocol's semantic fields."""
    return {
        "schema_version": record.schema_version,
        "dimension": record.dimension,
        "slot": record.slot,
        "chunk_x": record.chunk_x,
        "chunk_z": record.chunk_z,
        "data_version": record.data_version,
        "status": record.status,
        "full": record.full,
        "heightmaps": [
            parse_strict_json(row.model_dump_json().encode()) for row in record.heightmaps
        ],
        "biome_sections": [
            parse_strict_json(row.model_dump_json().encode()) for row in record.biome_sections
        ],
        "structure_starts": [
            parse_strict_json(row.model_dump_json().encode()) for row in record.structure_starts
        ],
    }


def normalized_sha256(records: dict[ChunkKey, ChunkRecord]) -> str:
    """Hash sorted normalized records using canonical JSON Lines."""
    digest = hashlib.sha256()
    for key in sorted(records):
        canonical = json.dumps(
            normalized_chunk(records[key]),
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        digest.update(canonical.encode("utf-8") + b"\n")
    return digest.hexdigest()


def first_mismatch(
    identity: tuple[str, str],
    records: tuple[dict[ChunkKey, ChunkRecord], dict[ChunkKey, ChunkRecord]],
    fields: tuple[str, ...],
) -> dict[str, JsonValue]:
    """Identify the first semantic field mismatch in sorted coordinate order."""
    role, label = identity
    left, right = records
    for key in sorted(left):
        left_row, right_row = normalized_chunk(left[key]), normalized_chunk(right[key])
        for field in fields:
            if left_row[field] != right_row[field]:
                return {
                    "seed_role": role,
                    "selection": label,
                    "dimension": key[0],
                    "chunk_x": key[1],
                    "chunk_z": key[2],
                    "field": field,
                }
    issue = "comparison mismatch has no differing field"
    raise RepeatComparisonError(issue, label)


def field_mismatch_counts(
    records: tuple[dict[ChunkKey, ChunkRecord], dict[ChunkKey, ChunkRecord]],
    fields: tuple[str, ...],
) -> dict[str, JsonValue]:
    """Count differing chunks independently for every frozen semantic field."""
    left, right = records
    counts = dict.fromkeys(fields, 0)
    for key in sorted(left):
        left_row, right_row = normalized_chunk(left[key]), normalized_chunk(right[key])
        for field in fields:
            if left_row[field] != right_row[field]:
                counts[field] += 1
    result: dict[str, JsonValue] = dict(counts)
    return result


def write_receipt(output: Path, payload: dict[str, JsonValue]) -> None:
    """Atomically write one deterministic strict JSON receipt."""
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
        raise RepeatComparisonError(issue, str(output)) from error
