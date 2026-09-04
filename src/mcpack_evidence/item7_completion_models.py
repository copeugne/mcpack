"""Typed outputs and narrow input adapters for Item 7 completion."""

from __future__ import annotations

from typing import ClassVar, Literal

from pydantic import BaseModel, ConfigDict, Field, JsonValue


class FrozenModel(BaseModel):
    """Strict immutable evidence model."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True, strict=True)


class ArtifactIdentity(FrozenModel):
    """Portable identity of one accepted artifact."""

    path: str
    sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    size_bytes: int = Field(ge=0)


class ProviderTotals(FrozenModel):
    """Exact final disposition totals for the 37 retained components."""

    direct_observed: int = Field(ge=0)
    targeted_observed: int = Field(ge=0)
    observed_generation_failure: int = Field(ge=0)
    indirect_observed: int = Field(ge=0)
    not_observed_with_limit: int = Field(ge=0)
    total_components: int = Field(ge=0)


class ProviderComponent(FrozenModel):
    """One final provider component disposition."""

    candidate_filename: str
    mod_id: str
    role: str
    sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    disposition: Literal[
        "direct_observed",
        "targeted_observed",
        "observed_generation_failure",
        "indirect_observed",
        "not_observed_with_limit",
    ]
    direct_observations: tuple[JsonValue, ...]
    targeted_starts: tuple[JsonValue, ...]
    limitation: str | None
    downstream_action: str | None


class ProviderLabel(FrozenModel):
    """One provider label and all retained components assigned to it."""

    label: str
    components: tuple[ProviderComponent, ...]


class ProviderDisposition(FrozenModel):
    """Narrow adapter for the separately produced provider disposition."""

    schema_version: Literal["item7-provider-disposition-v1"]
    catalog_path: str
    catalog_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    coverage_path: str
    coverage_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    inputs: tuple[JsonValue, ...]
    labels: tuple[ProviderLabel, ...]
    totals: ProviderTotals


class VisualManifestIdentity(FrozenModel):
    """Capture manifest identity embedded by an independent review."""

    archive_path: str
    sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    size_bytes: int = Field(ge=0)
    capture_count: int = Field(ge=0)


class VisualReview(FrozenModel):
    """One independent visual evidence verdict."""

    schema_version: Literal["item7-visual-review-v1"]
    lane: Literal["capture-and-source-integrity", "visual-fidelity"]
    verdict: Literal["PASS"]
    confidence: Literal["HIGH"]
    renderer_commit: str = Field(pattern=r"^[0-9a-f]{40}$")
    capture_tool_commit: str = Field(pattern=r"^[0-9a-f]{40}$")
    capture_manifest: VisualManifestIdentity
    checked: dict[str, int]
    findings: tuple[JsonValue, ...]
    observations: tuple[str, ...]


class ProviderSummary(FrozenModel):
    """Accepted provider completion summary."""

    total_components: int
    disposition_counts: ProviderTotals


class VisualSummary(FrozenModel):
    """Accepted visual evidence summary."""

    capture_count: int
    review_count: Literal[2]
    renderer_commit: str
    capture_tool_commit: str


class CompletionReport(FrozenModel):
    """Portable deterministic Item 7 completion result."""

    schema_version: Literal["item7-completion-v1"] = "item7-completion-v1"
    exit_gate: Literal["PASS"] = "PASS"
    artifacts: tuple[ArtifactIdentity, ...]
    run_count: Literal[8] = 8
    seed_count: Literal[4] = 4
    selections_per_run: Literal[4] = 4
    run_a_analysis_reports: Literal[16] = 16
    anomaly_rows: Literal[192] = 192
    repeat_equal: Literal[False] = False
    repeat_cause: Literal["UNKNOWN"] = "UNKNOWN"
    repeat_disposition: Literal["measured_semantic_nondeterminism"] = (
        "measured_semantic_nondeterminism"
    )
    warning_signatures: Literal[1222] = 1222
    warning_occurrences: Literal[14003] = 14003
    provider_summary: ProviderSummary
    control_disposition: Literal["not_attributable_due_to_measured_stack_nondeterminism"]
    gap_run_count: Literal[2] = 2
    targeted_structure_count: Literal[4] = 4
    visual_summary: VisualSummary
    archive_count: Literal[4] = 4
    archive_release_url: str
    limitations: tuple[str, ...]
