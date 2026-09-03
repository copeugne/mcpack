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
IDLE_PLAYER_CASE: str = "zero"
PLAYER_COUNTS: dict[str, int] = {
    "zero": 0,
    "solo": 1,
    "two": 2,
    "four": 4,
    "normal": 6,
    "peak": 10,
}
REQUIRED_SEED_CASES: set[str] = {
    "ordinary",
    "mountainous",
    "ocean-heavy",
    "biome-diverse",
}
REQUIRED_ENVIRONMENT_HASHES: set[str] = {
    "protocol",
    "retained_manifest",
    "configuration",
    "host",
    "world_snapshot",
}
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
RATIO_SCALES: dict[str, float] = {
    "structures_per_1000_chunks": 1000.0,
    "actionable_locations_per_1000_chunks": 1000.0,
    "combat_encounters_per_1000_chunks": 1000.0,
    "proper_dungeons_per_1000_chunks": 1000.0,
    "major_expeditions_per_1000_chunks": 1000.0,
    "death_rate": 1.0,
    "unique_structure_families_per_hour": 1.0,
    "repeated_dungeon_layout_frequency": 1.0,
    "adventure_activity_ratio": 1.0,
}
PROPORTION_METRICS = {"repeated_dungeon_layout_frequency", "adventure_activity_ratio"}
MULTI_AXIS_METRICS = {
    "memory",
    "garbage_collection",
    "entity_count",
    "pathfinding_cost",
    "chunk_generation_cost",
    "inter_structure_distance",
    "death_rate",
    "loot_value",
}
SAMPLE_UNITS: dict[str, set[str]] = {
    "idle_mspt": {"milliseconds per tick"},
    "active_combat_mspt": {"milliseconds per tick"},
    "fresh_worldgen_mspt": {"milliseconds per tick"},
    "tps": {"ticks per second"},
    "memory": {"bytes"},
    "garbage_collection": {"milliseconds", "collections"},
    "entity_count": {"entities"},
    "pathfinding_cost": {"milliseconds", "percent CPU"},
    "chunk_generation_cost": {"milliseconds per chunk"},
    "structure_count": {"unique starts"},
    "structures_per_1000_chunks": {"starts per 1000 chunks"},
    "actionable_locations_per_1000_chunks": {"locations per 1000 chunks"},
    "combat_encounters_per_1000_chunks": {"encounters per 1000 chunks"},
    "proper_dungeons_per_1000_chunks": {"dungeons per 1000 chunks"},
    "major_expeditions_per_1000_chunks": {"expeditions per 1000 chunks"},
    "inter_structure_distance": {"blocks"},
    "travel_time": {"seconds"},
    "dungeon_duration": {"seconds"},
    "death_rate": {"deaths per exposure"},
    "loot_value": {"value-vector components"},
    "unique_structure_families_per_hour": {"families per player-hour"},
    "time_to_first_repeated_structure_family": {"seconds"},
    "repeated_dungeon_layout_frequency": {"proportion"},
    "adventure_activity_ratio": {"ratio"},
}


class StrictModel(BaseModel):
    """Forbid silent schema drift in evidence records."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True)


NonEmpty = Annotated[str, Field(min_length=1)]
PositiveInt = Annotated[int, Field(gt=0)]
NonNegativeInt = Annotated[int, Field(ge=0)]
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
    input_world_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")] | None = None
    spark_overlay_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")] | None
    spark_artifact_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")] | None
    runtime_mods_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")] | None
    minecraft_version: NonEmpty
    neoforge_version: NonEmpty
    java_version: NonEmpty
    java_archive_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
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
    player_cases: tuple[Literal["zero", "solo", "two", "four", "normal", "peak"], ...]
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
        if not self.collection_procedure:
            message = "collection procedure, seeds, and player cases cannot be empty"
            raise ValueError(message)
        if (
            len(self.seed_cases) != len(set(self.seed_cases))
            or set(self.seed_cases) != REQUIRED_SEED_CASES
        ):
            message = "metric must cover every required seed case exactly once"
            raise ValueError(message)
        expected_player_cases = REQUIRED_PLAYER_CASES | (
            {IDLE_PLAYER_CASE} if self.metric_id == "idle_mspt" else set[str]()
        )
        if (
            len(self.player_cases) != len(set(self.player_cases))
            or set(self.player_cases) != expected_player_cases
        ):
            message = "metric must cover every required player case exactly once"
            raise ValueError(message)
        if (
            len(self.required_environment_hashes) != len(set(self.required_environment_hashes))
            or set(self.required_environment_hashes) != REQUIRED_ENVIRONMENT_HASHES
        ):
            message = "metric must require every environment hash exactly once"
            raise ValueError(message)
        return self


class PlayerCase(StrictModel):
    """Material player-count case."""

    case_id: Literal["zero", "solo", "two", "four", "normal", "peak"]
    players: NonNegativeInt
    source: NonEmpty

    @model_validator(mode="after")
    def validate_count(self) -> PlayerCase:
        """Prevent semantic case labels from drifting away from fixed loads."""
        if self.players != PLAYER_COUNTS[self.case_id]:
            message = (
                f"player case {self.case_id} must contain {PLAYER_COUNTS[self.case_id]} players"
            )
            raise ValueError(message)
        return self


class MeasurementProtocol(StrictModel):
    """Complete Item 5 protocol."""

    schema_version: Literal["item5-measurement-protocol-v1"]
    protocol_id: NonEmpty
    combat_fixture_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
    worldgen_fixture_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
    pathfinding_fixture_sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
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
        expected_cases = REQUIRED_PLAYER_CASES | {IDLE_PLAYER_CASE}
        if len(cases) != len(set(cases)) or set(cases) != expected_cases:
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
            or self.environment.input_world_sha256 is None
            or self.environment.spark_overlay_sha256 is None
            or self.environment.spark_artifact_sha256 is None
            or self.environment.runtime_mods_sha256 is None
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


def analyze_samples(  # noqa: C901, PLR0912, PLR0915 - validation is intentionally linear.
    rows: Iterable[dict[str, str]],
) -> dict[str, object]:
    """Aggregate samples without pooling experimental dimensions."""
    grouped: dict[tuple[str, str, str, int, str | None, str], list[float]] = {}
    ratio_inputs: dict[tuple[str, str, str, int, str | None, str], list[tuple[float, float]]] = {}
    for row in rows:
        try:
            metric_id = row["metric_id"]
            seed_case = row["seed_case"]
            player_case = row["player_case"]
            repetition = int(row["repetition"])
            value = float(row["value"])
            unit = row["unit"]
        except (KeyError, TypeError, ValueError) as error:
            message = "sample rows require metric_id, seed_case, player_case, repetition, and value"
            raise ValueError(message) from error
        if metric_id not in REQUIRED_METRICS:
            message = f"sample row has unknown metric_id: {metric_id}"
            raise ValueError(message)
        if unit not in SAMPLE_UNITS[metric_id]:
            message = f"sample row has invalid unit for {metric_id}: {unit}"
            raise ValueError(message)
        if seed_case not in REQUIRED_SEED_CASES:
            message = f"sample row has unknown seed_case: {seed_case}"
            raise ValueError(message)
        allowed_player_cases = REQUIRED_PLAYER_CASES | (
            {IDLE_PLAYER_CASE} if metric_id == "idle_mspt" else set[str]()
        )
        if player_case not in allowed_player_cases:
            message = f"sample row has unknown player_case: {player_case}"
            raise ValueError(message)
        if repetition <= 0 or not math.isfinite(value) or value < 0:
            message = "sample rows require positive repetition and nonnegative finite numeric value"
            raise ValueError(message)
        component = row.get("component") or None
        if metric_id in MULTI_AXIS_METRICS and component is None:
            message = f"multi-axis metric {metric_id} rows require a nonempty component"
            raise ValueError(message)
        if metric_id not in MULTI_AXIS_METRICS and component is not None:
            message = f"single-axis metric {metric_id} cannot declare a component"
            raise ValueError(message)
        group = (metric_id, seed_case, player_case, repetition, component, unit)
        if metric_id in RATIO_METRICS:
            try:
                numerator = float(row["numerator"])
                denominator = float(row["denominator"])
            except (KeyError, TypeError, ValueError) as error:
                message = f"ratio metric {metric_id} requires numerator and denominator"
                raise ValueError(message) from error
            if (
                not math.isfinite(numerator)
                or not math.isfinite(denominator)
                or numerator < 0
                or denominator <= 0
                or (metric_id in PROPORTION_METRICS and numerator > denominator)
            ):
                message = (
                    f"ratio metric {metric_id} requires nonnegative finite inputs, a positive "
                    "denominator, and bounded proportion operands"
                )
                raise ValueError(message)
            derived_value = numerator / denominator * RATIO_SCALES[metric_id]
            if not math.isclose(value, derived_value, rel_tol=1e-9, abs_tol=1e-12):
                message = f"ratio metric {metric_id} value does not match its operands"
                raise ValueError(message)
            value = derived_value
            ratio_inputs.setdefault(group, []).append((numerator, denominator))
        grouped.setdefault(group, []).append(value)
    if not grouped:
        message = "sample input contains no data rows"
        raise ValueError(message)
    groups: list[dict[str, object]] = []
    for group, values in sorted(grouped.items()):
        metric_id, seed_case, player_case, repetition, component, unit = group
        result_group: dict[str, object] = {
            "metric_id": metric_id,
            "seed_case": seed_case,
            "player_case": player_case,
            "repetition": repetition,
            "unit": unit,
            "statistics": _summarize(metric_id, values, ratio_inputs.get(group)),
        }
        if component is not None:
            result_group["component"] = component
        groups.append(result_group)
    return {"groups": groups}


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
        ratio_inputs = sorted(ratio_inputs)
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
