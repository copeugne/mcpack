"""Controlled-run and analysis acceptance checks for Item 7 completion."""

from __future__ import annotations

from pathlib import Path  # noqa: TC003
from typing import ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item7_analysis import analyze_jsonl
from mcpack_evidence.item7_analysis_models import ANOMALY_SPECS, AnalysisIdentity, WorldAnalysis
from mcpack_evidence.item7_completion_io import (
    fail,
    identity,
    portable_path,
    sha256_file,
    strict_model,
)
from mcpack_evidence.item7_completion_models import ArtifactIdentity  # noqa: TC001
from mcpack_evidence.item7_config import ConfigCaptureReceipt  # noqa: TC001
from mcpack_evidence.item7_repeat import RepeatWorldManifest
from mcpack_evidence.item7_selection_extract import SelectionReceipt

_ROLES: Final = (
    ("ordinary", "42"),
    ("mountainous", "6671238423019257953"),
    ("ocean-heavy", "95920844204830198"),
    ("biome-diverse", "-3503646078644842058"),
)
_SELECTIONS: Final = (
    ("overworld", "minecraft:overworld", 0, 0, 31, 3969),
    ("nether", "minecraft:the_nether", 0, 0, 15, 961),
    ("end-central", "minecraft:the_end", 0, 0, 15, 961),
    ("end-outer", "minecraft:the_end", 1536, 0, 15, 961),
)
_ANALYSIS_COUNT: Final = 16
_BASE_CONFIG_COUNT: Final = 228
_RUN_ARTIFACT_COUNT: Final = 96
_ANOMALY_KEYS: Final = tuple(spec.key for spec in ANOMALY_SPECS)


class _RunReceipt(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    schema_version: Literal["item7-worldgen-run-v1"]
    preflight: _Preflight
    lifecycle: _Lifecycle
    configuration: ConfigCaptureReceipt
    rejection_reason: None


class _Preflight(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    schema_version: Literal["item7-worldgen-preflight-v1"]
    seed_role: str
    seed: str
    java_version: Literal["Temurin-21.0.12.1+1-LTS"]
    retained_candidate_count: Literal[136]
    instrumented_candidate_count: Literal[137]
    retained_runtime_sha256: str
    instrumented_runtime_sha256: str
    retained_manifest_sha256: Literal[
        "78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb"
    ]
    frozen_manifest_sha256: Literal[
        "2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f"
    ]
    config_audit_sha256: Literal["181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd"]
    seed_suite_sha256: Literal["de5e5e89bd04b6f75dac4eab2e84524956f46faa91660b5315c8eade269d39ae"]
    chunky_sha256: Literal["d72f235cf1f56f2c374f52c00bdda5034524b28142305a84cfc123a3f92ad274"]


class _Selection(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    label: str
    dimension: str
    center_x: int
    center_z: int
    radius_chunks: int
    expected_chunk_count: int


class _Lifecycle(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    schema_version: Literal["item7-worldgen-lifecycle-v1"]
    ready: bool
    generation_finished: bool
    save_all_flush: bool
    clean_stop: bool
    return_code: int
    commands: tuple[str, ...]
    selections: tuple[_Selection, ...]
    completed_selection_labels: tuple[str, ...]
    log: str
    minecraft_log: str
    duration_seconds: float
    process_group_killed: bool
    rejection_reason: None


def validate_runs(raw_root: Path, protocol_sha256: str) -> tuple[tuple[ArtifactIdentity, ...], int]:
    """Validate all eight clean runs and all 16 Run A analysis reports."""
    artifacts: list[ArtifactIdentity] = []
    analysis_count = 0
    for run_id in ("run-a", "run-b"):
        for role, seed in _ROLES:
            root = raw_root / run_id / role
            receipt_path = root / "run-receipt.json"
            manifest_path = root / "world-manifest.json"
            receipt = strict_model(receipt_path, _RunReceipt)
            manifest = strict_model(manifest_path, RepeatWorldManifest)
            _validate_run(receipt, role, seed)
            _validate_manifest(root, manifest)
            artifacts.extend(
                (
                    identity(receipt_path, f"{run_id}/{role}/run-receipt.json"),
                    identity(manifest_path, f"{run_id}/{role}/world-manifest.json"),
                )
            )
            for label, dimension, center_x, center_z, radius, count in _SELECTIONS:
                selected = root / "selections" / f"{label}.jsonl"
                selected_receipt_path = selected.with_suffix(".jsonl.receipt.json")
                selected_receipt = strict_model(selected_receipt_path, SelectionReceipt)
                _validate_selection(
                    selected,
                    selected_receipt,
                    manifest_path,
                    protocol_sha256,
                    (label, dimension, center_x, center_z, radius, count),
                )
                artifacts.extend(
                    (
                        identity(selected, f"{run_id}/{role}/selections/{label}.jsonl"),
                        identity(
                            selected_receipt_path,
                            f"{run_id}/{role}/selections/{label}.jsonl.receipt.json",
                        ),
                    )
                )
                if run_id == "run-a":
                    analysis_path = root / "analysis" / f"{label}.json"
                    analysis = strict_model(analysis_path, WorldAnalysis)
                    rebuilt = analyze_jsonl(
                        selected,
                        AnalysisIdentity(run_id, role, label, dimension),
                        selected_receipt.selected.sha256,
                    )
                    keys = tuple(row.key for row in analysis.anomalies)
                    statuses = {row.status for row in analysis.anomalies}
                    if (
                        analysis.input_sha256 != selected_receipt.selected.sha256
                        or (
                            analysis.run_id,
                            analysis.seed_role,
                            analysis.selection,
                            analysis.dimension,
                        )
                        != (run_id, role, label, dimension)
                        or keys != _ANOMALY_KEYS
                        or not statuses <= {"observed", "method-limited", "unresolved"}
                        or analysis != rebuilt
                    ):
                        fail("analysis identity or anomaly accounting", analysis_path)
                    artifacts.append(
                        identity(analysis_path, f"{run_id}/{role}/analysis/{label}.json")
                    )
                    analysis_count += 1
    if len(artifacts) != _RUN_ARTIFACT_COUNT or analysis_count != _ANALYSIS_COUNT:
        fail("run artifact accounting", len(artifacts))
    return tuple(artifacts), analysis_count * len(_ANOMALY_KEYS)


def _validate_run(receipt: _RunReceipt, role: str, seed: str) -> None:
    preflight, lifecycle = receipt.preflight, receipt.lifecycle
    selections = tuple(
        (
            row.label,
            row.dimension,
            row.center_x,
            row.center_z,
            row.radius_chunks,
            row.expected_chunk_count,
        )
        for row in lifecycle.selections
    )
    if (
        (preflight.seed_role, preflight.seed) != (role, seed)
        or selections != _SELECTIONS
        or tuple(lifecycle.completed_selection_labels) != tuple(row[0] for row in _SELECTIONS)
        or not all(
            (
                lifecycle.ready,
                lifecycle.generation_finished,
                lifecycle.save_all_flush,
                lifecycle.clean_stop,
                lifecycle.return_code == 0,
                not lifecycle.process_group_killed,
                lifecycle.rejection_reason is None,
            )
        )
        or receipt.configuration.base_file_count != _BASE_CONFIG_COUNT
    ):
        fail("controlled run boundary", f"{role}/{seed}")


def _validate_manifest(root: Path, manifest: RepeatWorldManifest) -> None:
    expected = tuple(
        (row[0], row[1], row[2], row[3], row[4], row[5], row[5]) for row in _SELECTIONS
    )
    observed = tuple(
        (
            row.label,
            row.dimension,
            row.center_block_x,
            row.center_block_z,
            row.radius_chunks,
            row.expected_chunk_count,
            row.observed_chunk_count,
        )
        for row in manifest.selections
    )
    decoded = root / portable_path(manifest.decoded.path)
    try:
        _ = decoded.resolve().relative_to(root.resolve())
    except ValueError:
        fail("decoded path escapes run root", decoded)
    if (
        observed != expected
        or manifest.external_chunks
        or decoded.stat().st_size != manifest.decoded.size_bytes
        or sha256_file(decoded) != manifest.decoded.sha256
    ):
        fail("stopped world manifest boundary", root)


def _validate_selection(
    selected: Path,
    receipt: SelectionReceipt,
    manifest_path: Path,
    protocol_sha256: str,
    expected: tuple[str, str, int, int, int, int],
) -> None:
    row = receipt.selection
    actual = (
        row.label,
        row.dimension,
        row.center_block_x,
        row.center_block_z,
        row.radius_chunks,
        row.expected_chunk_count,
    )
    if (
        actual != expected
        or row.observed_chunk_count != expected[5]
        or receipt.selected.record_count != expected[5]
        or receipt.selected.sha256 != sha256_file(selected)
        or receipt.selected.size_bytes != selected.stat().st_size
        or receipt.protocol.sha256 != protocol_sha256
        or receipt.world_manifest.sha256 != sha256_file(manifest_path)
    ):
        fail("selection extract identity", selected)
