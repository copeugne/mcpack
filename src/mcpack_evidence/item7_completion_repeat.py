"""Repeat-evidence acceptance for Item 7 completion."""

from __future__ import annotations

from pathlib import Path  # noqa: TC003
from typing import ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict, Field, JsonValue

from mcpack_evidence.item7_completion_io import fail, identity, strict_model
from mcpack_evidence.item7_completion_models import ArtifactIdentity  # noqa: TC001
from mcpack_evidence.item7_repeat_comparison import rebuild_selection_comparison

_STRUCTURAL: Final = frozenset(
    {
        "schema_version",
        "dimension",
        "slot",
        "chunk_x",
        "chunk_z",
        "data_version",
        "status",
        "full",
    }
)


class _RepeatReport(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    schema_version: Literal["item7-repeat-comparison-v1"]
    protocol_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    raw_region_hash_treatment: Literal["preserve_and_explain_not_compare"]
    equal: Literal[False]
    first_mismatch: dict[str, JsonValue]
    seeds: tuple[dict[str, JsonValue], ...]


def validate_repeat(path: Path, protocol_path: Path) -> ArtifactIdentity:
    """Require the reported receipt to exactly match rebuilt selection evidence."""
    report = strict_model(path, _RepeatReport)
    rebuilt = rebuild_selection_comparison(protocol_path, path.parent)
    if report.model_dump(mode="json") != rebuilt:
        fail("repeat comparison source binding", path)
    if _has_structural_mismatch(rebuilt):
        fail("repeat structural mismatch", path)
    return identity(path, "repeat-comparison.json")


def _has_structural_mismatch(report: dict[str, JsonValue]) -> bool:
    seeds = report["seeds"]
    if not isinstance(seeds, list):
        fail("repeat selection accounting", "seeds")
    for seed in seeds:
        if not isinstance(seed, dict):
            fail("repeat seed accounting", "seed")
        selections = seed.get("selections")
        if not isinstance(selections, list):
            fail("repeat selection accounting", "selections")
        for selection in selections:
            if not isinstance(selection, dict):
                fail("repeat selection accounting", "selection")
            counts = selection.get("field_mismatch_counts")
            if not isinstance(counts, dict):
                fail("repeat field accounting", "field_mismatch_counts")
            if any(counts.get(field) != 0 for field in _STRUCTURAL):
                return True
    return False
