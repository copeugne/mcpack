"""Final deterministic Item 7 completion acceptance boundary."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Final

from mcpack_evidence.item7_completion_io import (
    CompletionError,
    identity,
    sha256_file,
    write_atomic,
)
from mcpack_evidence.item7_completion_models import ArtifactIdentity, CompletionReport
from mcpack_evidence.item7_completion_other import (
    validate_archives,
    validate_control,
    validate_gaps,
    validate_warnings,
)
from mcpack_evidence.item7_completion_provider_visual import (
    validate_provider_disposition,
    validate_visual_evidence,
)
from mcpack_evidence.item7_completion_publication import validate_publication
from mcpack_evidence.item7_completion_repeat import validate_repeat
from mcpack_evidence.item7_completion_runs import validate_runs
from mcpack_evidence.item7_protocol import load_protocol
from mcpack_evidence.item7_restrictions import validate_restriction_audit

if TYPE_CHECKING:
    from pathlib import Path

_ANOMALY_ROWS: Final = 192


@dataclass(frozen=True, slots=True)
class CompletionInputs:
    """Every independently produced surface required by the exit gate."""

    raw_root: Path
    protocol: Path
    provider_catalog: Path
    provider_coverage: Path
    provider_disposition: Path
    restriction_audit: Path
    world_archive_inventory: Path
    repeat_comparison: Path
    warning_audit: Path
    warning_disposition: Path
    control_comparison: Path
    visual_manifest: Path
    visual_reviews: tuple[Path, Path]
    archive_manifests: tuple[Path, Path, Path, Path]
    restore_receipts: tuple[Path, Path, Path, Path]
    publication: Path
    output: Path


def build_completion(inputs: CompletionInputs) -> CompletionReport:
    """Validate every Item 7 boundary and atomically publish PASS."""
    _ = load_protocol(inputs.protocol)
    protocol_sha = sha256_file(inputs.protocol)
    artifacts = [identity(inputs.protocol, "protocol/worldgen-audit-v1.json")]
    raw_artifacts: list[ArtifactIdentity] = []
    run_artifacts, anomaly_rows = validate_runs(inputs.raw_root, protocol_sha)
    if anomaly_rows != _ANOMALY_ROWS:
        issue = "analysis anomaly accounting"
        raise CompletionError(issue, str(anomaly_rows))
    artifacts.extend(run_artifacts)
    raw_artifacts.extend(run_artifacts)
    repeat = validate_repeat(inputs.repeat_comparison, protocol_sha)
    warning_artifacts = validate_warnings(inputs.warning_audit, inputs.warning_disposition)
    artifacts.append(repeat)
    artifacts.extend(warning_artifacts)
    raw_artifacts.append(repeat)
    raw_artifacts.extend(warning_artifacts)
    provider = validate_provider_disposition(
        inputs.provider_catalog,
        inputs.provider_disposition,
        inputs.provider_coverage,
        raw_root=inputs.raw_root,
    )
    _ = validate_restriction_audit(inputs.restriction_audit, sha256_file(inputs.provider_catalog))
    artifacts.extend(
        (
            identity(inputs.provider_catalog, "provider-catalog.json"),
            identity(inputs.restriction_audit, "biome-restriction-audit.json"),
            identity(inputs.provider_coverage, "run-a/provider-coverage.json"),
            identity(inputs.provider_disposition, "provider-disposition.json"),
        )
    )
    raw_artifacts.extend(artifacts[-2:])
    provider_evidence = tuple(
        identity(inputs.raw_root / path, path)
        for path in (
            "run-a/mountainous/minecraft-latest.log",
            "gap-a/ordinary/chunks.jsonl",
            "gap-a/ordinary/gap-minecraft-latest.log",
            "gap-b/ordinary/chunks.jsonl",
            "gap-b/ordinary/gap-minecraft-latest.log",
        )
    )
    artifacts.extend(provider_evidence)
    raw_artifacts.extend(provider_evidence)
    control = validate_control(inputs.control_comparison, inputs.repeat_comparison)
    gaps = validate_gaps(inputs.raw_root)
    artifacts.append(control)
    artifacts.extend(gaps)
    raw_artifacts.append(control)
    raw_artifacts.extend(gaps)
    visual = validate_visual_evidence(inputs.visual_manifest, inputs.visual_reviews)
    visual_manifest = identity(inputs.visual_manifest, "visual-qa/captures/capture-manifest.tsv")
    artifacts.append(visual_manifest)
    raw_artifacts.append(visual_manifest)
    artifacts.extend(identity(path, f"visual/{path.name}") for path in inputs.visual_reviews)
    artifacts.extend(
        validate_archives(
            inputs.archive_manifests,
            inputs.restore_receipts,
            tuple(raw_artifacts),
            inputs.world_archive_inventory,
        )
    )
    publication, release_url = validate_publication(inputs.publication, inputs.archive_manifests)
    artifacts.append(publication)
    paths = tuple(row.path for row in artifacts)
    if len(paths) != len(set(paths)):
        issue = "duplicate completion artifact path"
        raise CompletionError(issue, "artifacts")
    report = CompletionReport(
        artifacts=tuple(sorted(artifacts, key=lambda row: row.path)),
        anomaly_rows=_ANOMALY_ROWS,
        provider_summary=provider,
        control_disposition="not_attributable_due_to_measured_stack_nondeterminism",
        visual_summary=visual,
        archive_release_url=release_url,
        limitations=(
            "Generated semantics differ across independent fresh runs; causal provider is UNKNOWN.",
            (
                "Offline renders are derived elevation and placement views, "
                "not block-accurate client renders."
            ),
            "Warning and provider unknowns remain preserved with explicit downstream dispositions.",
        ),
    )
    write_atomic(inputs.output, report)
    return report


__all__ = (
    "CompletionError",
    "CompletionInputs",
    "build_completion",
    "validate_provider_disposition",
    "validate_visual_evidence",
)
