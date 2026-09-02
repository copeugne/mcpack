"""Strict contracts and deterministic processing for Item 5 measurements."""

from __future__ import annotations

import csv
import hashlib
import json
import statistics
from collections.abc import Iterable  # noqa: TC003 - Pydantic resolves this annotation.
from datetime import datetime  # noqa: TC003 - Pydantic resolves this annotation.
from pathlib import Path  # noqa: TC003 - Pydantic resolves this annotation.
from typing import Annotated, ClassVar, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

REQUIRED_METRICS: set[str] = {
    "idle_mspt",
    "active_combat_mspt",
    "fresh_worldgen_mspt",
    "tps",
    "memory",
    "garbage_collection",
    "entity_count",
    "pathfinding_cost",
    "chunk_generation_cost",
    "structure_count",
    "structures_per_1000_chunks",
    "actionable_locations_per_1000_chunks",
    "combat_encounters_per_1000_chunks",
    "proper_dungeons_per_1000_chunks",
    "major_expeditions_per_1000_chunks",
    "inter_structure_distance",
    "travel_time",
    "dungeon_duration",
    "death_rate",
    "loot_value",
    "unique_structure_families_per_hour",
    "time_to_first_repeated_structure_family",
    "repeated_dungeon_layout_frequency",
    "adventure_activity_ratio",
}
REQUIRED_PLAYER_CASES: set[str] = {"solo", "two", "four", "normal", "peak"}


class StrictModel(BaseModel):
    """Forbid silent schema drift in evidence records."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True)


NonEmpty = Annotated[str, Field(min_length=1)]
PositiveInt = Annotated[int, Field(gt=0)]
NonNegativeFloat = Annotated[float, Field(ge=0)]


class EnvironmentIdentity(StrictModel):
    """Immutable identities relevant to a measurement."""

    git_commit: Annotated[str, Field(pattern=r"^[0-9a-f]{40}$")]
    git_dirty: bool
    protocol_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
    retained_manifest_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
    configuration_version: NonEmpty
    minecraft_version: NonEmpty
    neoforge_version: NonEmpty
    java_version: NonEmpty
    host_evidence_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]


class MetricContract(StrictModel):
    """Complete, executable methodology for one required metric."""

    metric_id: NonEmpty
    purpose: NonEmpty
    measured_quantity: NonEmpty
    unit: NonEmpty
    collection_procedure: tuple[NonEmpty, ...]
    warm_up: NonEmpty
    sample_interval_seconds: PositiveInt
    sample_window_seconds: PositiveInt
    total_run_duration_seconds: PositiveInt
    repetitions: PositiveInt
    seed_cases: tuple[Literal["ordinary", "mountainous", "ocean-heavy", "biome-diverse"], ...]
    player_cases: tuple[Literal["solo", "two", "four", "normal", "peak"], ...]
    raw_format: Literal["csv", "json", "sparkprofile", "jvm_gc_log"]
    raw_path_template: NonEmpty
    processed_format: Literal["json"]
    processed_path_template: NonEmpty
    aggregation: NonEmpty
    acceptance_rule: NonEmpty
    invalid_run_rule: NonEmpty
    uncertainty_treatment: NonEmpty
    required_environment_hashes: tuple[NonEmpty, ...]

    @model_validator(mode="after")
    def validate_windows(self) -> MetricContract:
        """Reject internally impossible timing and empty case lists."""
        if self.sample_window_seconds > self.total_run_duration_seconds:
            message = "sample window exceeds total duration"
            raise ValueError(message)
        if not self.collection_procedure or not self.seed_cases or not self.player_cases:
            message = "collection procedure, seeds, and player cases cannot be empty"
            raise ValueError(message)
        return self


class PlayerCase(StrictModel):
    """Material player-count case."""

    case_id: Literal["solo", "two", "four", "normal", "peak"]
    players: PositiveInt
    source: NonEmpty


class MeasurementProtocol(StrictModel):
    """Complete Item 5 protocol."""

    schema_version: Literal["item5-measurement-protocol-v1"]
    protocol_id: NonEmpty
    player_cases: tuple[PlayerCase, ...]
    metrics: tuple[MetricContract, ...]

    @model_validator(mode="after")
    def validate_coverage(self) -> MeasurementProtocol:
        """Require exact metric and case coverage without duplicates."""
        metrics = [metric.metric_id for metric in self.metrics]
        cases = [case.case_id for case in self.player_cases]
        if len(metrics) != len(set(metrics)) or set(metrics) != REQUIRED_METRICS:
            message = "protocol must cover every required metric exactly once"
            raise ValueError(message)
        if len(cases) != len(set(cases)) or set(cases) != REQUIRED_PLAYER_CASES:
            message = "protocol must cover every required player case exactly once"
            raise ValueError(message)
        return self


class ArtifactIdentity(StrictModel):
    """Hash identity for an immutable run artifact."""

    path: NonEmpty
    size_bytes: Annotated[int, Field(ge=0)]
    sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]


class PilotRun(StrictModel):
    """Machine-readable end-to-end pilot receipt."""

    schema_version: Literal["item5-pilot-run-v1"]
    run_id: NonEmpty
    status: Literal["accepted", "rejected"]
    started_at: datetime
    ended_at: datetime
    exact_commands: tuple[NonEmpty, ...]
    seed: int
    player_case: Literal["solo", "two", "four", "normal", "peak"]
    environment: EnvironmentIdentity
    raw_artifacts: tuple[ArtifactIdentity, ...]
    processed_artifacts: tuple[ArtifactIdentity, ...]
    rejection_reasons: tuple[NonEmpty, ...]

    @model_validator(mode="after")
    def validate_status(self) -> PilotRun:
        """Ensure status, timing, and rejection details agree."""
        if self.ended_at <= self.started_at:
            message = "pilot end must follow its start"
            raise ValueError(message)
        if (self.status == "rejected") != bool(self.rejection_reasons):
            message = "only rejected runs have rejection reasons"
            raise ValueError(message)
        if not self.raw_artifacts:
            message = "a pilot must preserve raw evidence"
            raise ValueError(message)
        return self


def sha256_file(path: Path) -> str:
    """Return a streamed SHA-256 digest."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def artifact_identity(path: Path, *, root: Path) -> ArtifactIdentity:
    """Build a relative, content-addressed artifact identity."""
    resolved = path.resolve()
    return ArtifactIdentity(
        path=resolved.relative_to(root.resolve()).as_posix(),
        size_bytes=resolved.stat().st_size,
        sha256=sha256_file(resolved),
    )


def analyze_samples(rows: Iterable[dict[str, str]]) -> dict[str, object]:
    """Deterministically aggregate long-form numeric samples."""
    grouped: dict[str, list[float]] = {}
    for row in rows:
        grouped.setdefault(row["metric_id"], []).append(float(row["value"]))
    return {
        metric: {
            "count": len(values),
            "min": min(values),
            "median": statistics.median(values),
            "max": max(values),
            "mean": statistics.fmean(values),
        }
        for metric, values in sorted(grouped.items())
    }


def analyze_csv(source: Path, output: Path) -> None:
    """Process an immutable CSV into canonical JSON."""
    with source.open(encoding="utf-8", newline="") as stream:
        result = analyze_samples(csv.DictReader(stream))
    _ = output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
