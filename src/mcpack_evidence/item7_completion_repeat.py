"""Repeat-evidence acceptance for Item 7 completion."""

from __future__ import annotations

from pathlib import Path  # noqa: TC003
from typing import ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict, Field, JsonValue

from mcpack_evidence.item7_completion_io import fail, identity, strict_model
from mcpack_evidence.item7_completion_models import ArtifactIdentity  # noqa: TC001

_ROLES: Final = ("ordinary", "mountainous", "ocean-heavy", "biome-diverse")
_SELECTIONS: Final = ("overworld", "nether", "end-central", "end-outer")
_FIELDS: Final = frozenset(
    {
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
    }
)
_STRUCTURAL: Final = _FIELDS - {"heightmaps", "biome_sections", "structure_starts"}


class _RepeatReport(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    schema_version: Literal["item7-repeat-comparison-v1"]
    protocol_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    raw_region_hash_treatment: Literal["preserve_and_explain_not_compare"]
    equal: Literal[False]
    first_mismatch: dict[str, JsonValue]
    seeds: tuple[dict[str, JsonValue], ...]


def validate_repeat(path: Path, protocol_sha256: str) -> ArtifactIdentity:
    """Require measured semantic divergence with intact comparison geometry."""
    report = strict_model(path, _RepeatReport)
    if report.protocol_sha256 != protocol_sha256 or len(report.seeds) != len(_ROLES):
        fail("repeat identity or seed accounting", path)
    differences = tuple(
        _seed_has_difference(path, role, seed)
        for role, seed in zip(_ROLES, report.seeds, strict=True)
    )
    if not any(differences) or not report.first_mismatch:
        fail("repeat nondeterminism evidence", path)
    return identity(path, "repeat-comparison.json")


def _seed_has_difference(path: Path, role: str, seed: dict[str, JsonValue]) -> bool:
    if seed.get("role") != role:
        fail("repeat seed role accounting", path)
    selections = seed.get("selections")
    if not isinstance(selections, list) or len(selections) != len(_SELECTIONS):
        fail("repeat selection accounting", path)
    return any(
        _selection_has_difference(path, label, selection)
        for label, selection in zip(_SELECTIONS, selections, strict=True)
    )


def _selection_has_difference(path: Path, label: str, selection: JsonValue) -> bool:
    if not isinstance(selection, dict) or selection.get("label") != label:
        fail("repeat selection label accounting", path)
    counts = selection.get("field_mismatch_counts")
    if not isinstance(counts, dict) or set(counts) != set(_FIELDS):
        fail("repeat field accounting", path)
    values = tuple(_count(path, value) for value in counts.values())
    if any(counts[field] != 0 for field in _STRUCTURAL):
        fail("repeat structural mismatch", path)
    return any(value > 0 for value in values)


def _count(path: Path, value: JsonValue) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        fail("repeat mismatch count", path)
    return value
