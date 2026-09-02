"""Strict contracts and deterministic processing for Item 5 measurements."""

from __future__ import annotations

import csv
import hashlib
import json
import math
import random
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
RATIO_METRICS: set[str] = {
    "structures_per_1000_chunks",
    "actionable_locations_per_1000_chunks",
    "combat_encounters_per_1000_chunks",
    "proper_dungeons_per_1000_chunks",
    "major_expeditions_per_1000_chunks",
    "death_rate",
    "unique_structure_families_per_hour",
    "repeated_dungeon_layout_frequency",
    "adventure_activity_ratio",
}


class StrictModel(BaseModel):
    """Forbid silent schema drift in evidence records."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True)


NonEmpty = Annotated[str, Field(min_length=1)]
PositiveInt = Annotated[int, Field(gt=0)]
BOOTSTRAP_RESAMPLES = 10_000


class EnvironmentIdentity(StrictModel):
    """Immutable identities relevant to a measurement."""

    git_commit: Annotated[str, Field(pattern=r"^[0-9a-f]{40}$")]
    git_dirty: bool
    protocol_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
    retained_manifest_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
    configuration_version: NonEmpty
    configuration_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")] | None
    world_snapshot_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")] | None
    spark_overlay_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")] | None
    spark_artifact_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")] | None
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
    warm_up_seconds: PositiveInt
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
        minimum_duration = self.warm_up_seconds + self.sample_window_seconds
        if minimum_duration > self.total_run_duration_seconds:
            message = "warm-up plus sample window exceeds total duration"
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
        if self.status == "accepted" and not self.processed_artifacts:
            message = "an accepted pilot must preserve processed evidence"
            raise ValueError(message)
        if self.status == "accepted" and (
            self.environment.configuration_sha256 is None
            or self.environment.world_snapshot_sha256 is None
            or self.environment.spark_overlay_sha256 is None
            or self.environment.spark_artifact_sha256 is None
        ):
            message = "an accepted pilot must record every environment and Spark hash"
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
    ratio_inputs: dict[str, list[tuple[float, float]]] = {}
    for row in rows:
        try:
            metric_id = row["metric_id"]
            value = float(row["value"])
        except (KeyError, TypeError, ValueError) as error:
            message = "sample rows require metric_id and finite numeric value"
            raise ValueError(message) from error
        if not metric_id or not math.isfinite(value):
            message = "sample rows require nonempty metric_id and finite numeric value"
            raise ValueError(message)
        if metric_id in RATIO_METRICS:
            try:
                numerator = float(row["numerator"])
                denominator = float(row["denominator"])
            except (KeyError, TypeError, ValueError) as error:
                message = f"ratio metric {metric_id} requires numerator and denominator"
                raise ValueError(message) from error
            if not math.isfinite(numerator) or not math.isfinite(denominator) or denominator <= 0:
                message = (
                    f"ratio metric {metric_id} requires finite inputs and positive denominator"
                )
                raise ValueError(message)
            ratio_inputs.setdefault(metric_id, []).append((numerator, denominator))
        grouped.setdefault(metric_id, []).append(value)
    if not grouped:
        message = "sample input contains no data rows"
        raise ValueError(message)
    return {
        metric: _summarize(metric, values, ratio_inputs.get(metric))
        for metric, values in sorted(grouped.items())
    }


def _percentile(values: list[float], percentile: float) -> float:
    """Return a linearly interpolated percentile for nonempty values."""
    ordered = sorted(values)
    position = (len(ordered) - 1) * percentile
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower
    return ordered[lower] + (ordered[upper] - ordered[lower]) * fraction


def _bootstrap_median_ci(metric: str, values: list[float]) -> list[float]:
    """Return a reproducible percentile-bootstrap 95% CI for the median."""
    seed = int.from_bytes(hashlib.sha256(metric.encode()).digest()[:8], "big")
    generator = random.Random(seed)  # noqa: S311 - reproducibility, not security.
    medians = [
        statistics.median(generator.choices(values, k=len(values)))
        for _ in range(BOOTSTRAP_RESAMPLES)
    ]
    return [_percentile(medians, 0.025), _percentile(medians, 0.975)]


def _summarize(
    metric: str, values: list[float], ratio_inputs: list[tuple[float, float]] | None
) -> dict[str, object]:
    """Produce every dispersion and uncertainty statistic promised by the protocol."""
    values = sorted(values)
    first_quartile = _percentile(values, 0.25)
    third_quartile = _percentile(values, 0.75)
    minimum, maximum = min(values), max(values)
    summary: dict[str, object] = {
        "count": len(values),
        "min": minimum,
        "median": statistics.median(values),
        "mean": statistics.fmean(values),
        "p95": _percentile(values, 0.95),
        "p99": _percentile(values, 0.99),
        "max": maximum,
        "range": maximum - minimum,
        "iqr": third_quartile - first_quartile,
        "bootstrap_median_95ci": _bootstrap_median_ci(metric, values),
        "bootstrap_resamples": BOOTSTRAP_RESAMPLES,
    }
    if ratio_inputs is not None:
        summary["numerators"] = [numerator for numerator, _ in ratio_inputs]
        summary["denominators"] = [denominator for _, denominator in ratio_inputs]
        summary["numerator_sum"] = math.fsum(numerator for numerator, _ in ratio_inputs)
        summary["denominator_sum"] = math.fsum(denominator for _, denominator in ratio_inputs)
    return summary


def analyze_csv(source: Path, output: Path) -> None:
    """Process an immutable CSV into canonical JSON."""
    with source.open(encoding="utf-8", newline="") as stream:
        result = analyze_samples(csv.DictReader(stream))
    _ = output.write_text(
        json.dumps(result, allow_nan=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
