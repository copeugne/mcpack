"""Strict Item 7 provider-disposition evidence models."""

from __future__ import annotations

from enum import StrEnum
from typing import ClassVar, Literal

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item7_coverage_models import Observation  # noqa: TC001


class _FrozenModel(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)


class DispositionStatus(StrEnum):
    """Evidence-honest closure status for one retained component."""

    DIRECT_OBSERVED = "direct_observed"
    TARGETED_OBSERVED = "targeted_observed"
    OBSERVED_GENERATION_FAILURE = "observed_generation_failure"
    INDIRECT_OBSERVED = "indirect_observed"
    NOT_OBSERVED_WITH_LIMIT = "not_observed_with_limit"


class FileBinding(_FrozenModel):
    """Content identity for one provider-closure input."""

    path: str
    sha256: str
    size_bytes: int
    record_count: int


class SavedStart(_FrozenModel):
    """One targeted structure start saved by an accepted gap run."""

    run: Literal["gap-a", "gap-b"]
    structure_id: str
    chunk_x: int
    chunk_z: int


class DispositionComponent(_FrozenModel):
    """Final Item 7 disposition for one catalog component."""

    candidate_filename: str
    mod_id: str
    role: Literal["direct_structure", "terrain_biome", "library"]
    sha256: str
    disposition: DispositionStatus
    direct_observations: tuple[Observation, ...]
    targeted_starts: tuple[SavedStart, ...]
    limitation: str
    downstream_action: str | None


class DispositionLabel(_FrozenModel):
    """One protocol label and its retained components."""

    label: str
    components: tuple[DispositionComponent, ...]


class DispositionTotals(_FrozenModel):
    """Frozen exact totals for the complete provider closure."""

    direct_observed: Literal[23]
    targeted_observed: Literal[4]
    observed_generation_failure: Literal[1]
    indirect_observed: Literal[7]
    not_observed_with_limit: Literal[2]
    total_components: Literal[37]


class ProviderDispositionReport(_FrozenModel):
    """Complete provider closure without Item 8 family grouping."""

    schema_version: Literal["item7-provider-disposition-v1"]
    catalog_path: str
    catalog_sha256: str
    coverage_path: str
    coverage_sha256: str
    inputs: tuple[FileBinding, ...]
    labels: tuple[DispositionLabel, ...]
    totals: DispositionTotals
