"""Persisted models for Item 3 static compatibility evaluation."""

from __future__ import annotations

from typing import ClassVar, Literal

from pydantic import BaseModel, ConfigDict, Field


class ProvidedMod(BaseModel):
    """One active NeoForge mod identity supplied by a candidate or nested JAR."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    mod_id: str
    version: str
    provider_candidate: str
    origin: Literal["outer", "nested"]
    source_path: str


class RangeCheck(BaseModel):
    """One exact version-range request and oracle result."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    subject: str
    installed_version: str
    declared_range: str
    result: Literal["pass", "fail", "invalid", "missing_oracle_result"]
    fallback_version: str | None = None


class DependencyCheck(BaseModel):
    """Evaluated active dependency under dedicated-server physical-side semantics."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    owner_mod_id: str
    dependency_mod_id: str
    kind: str
    side: str
    status: Literal[
        "pass",
        "missing_required",
        "version_mismatch",
        "incompatible_present",
        "discouraged_present",
        "optional_absent",
        "ignored_physical_side",
        "orphan_owner",
        "unresolved",
    ]
    provider_candidates: tuple[str, ...]
    range_checks: tuple[RangeCheck, ...]


class CandidateCompatibility(BaseModel):
    """Static compatibility result for one exact candidate artifact."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    candidate_filename: str
    artifact_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    archive_role: str
    active_metadata_paths: tuple[str, ...]
    inactive_metadata_paths: tuple[str, ...]
    provided_mods: tuple[ProvidedMod, ...]
    loader_checks: tuple[RangeCheck, ...]
    minecraft_checks: tuple[RangeCheck, ...]
    neoforge_checks: tuple[RangeCheck, ...]
    dependency_checks: tuple[DependencyCheck, ...]
    hazard_flags: tuple[str, ...]
    static_status: Literal["compatible", "incompatible", "unresolved"]
    disposition: Literal["runtime_test_candidate", "disabled", "quarantined", "unresolved"]
    confidence: Literal["high", "medium", "low"]
    missing_runtime_evidence: tuple[str, ...]


class CompatibilityReport(BaseModel):
    """Complete static compatibility evaluation for the candidate inventory."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    schema_version: Literal["item3-static-compatibility-v1"]
    target_minecraft: Literal["1.21.1"]
    target_neoforge: Literal["21.1.249"]
    physical_side: Literal["dedicated_server"]
    candidate_count: int = Field(gt=0)
    candidates: tuple[CandidateCompatibility, ...]
