"""Cross-surface acceptance checks for Item 7 completion."""

from __future__ import annotations

from pathlib import Path  # noqa: TC003
from typing import ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict, JsonValue

from mcpack_evidence.item7_archive import ArchiveManifest, RestoreReceipt
from mcpack_evidence.item7_completion_io import fail, identity, sha256_file, strict_model
from mcpack_evidence.item7_completion_models import ArtifactIdentity  # noqa: TC001
from mcpack_evidence.item7_gap import GAP_TARGETS, GapLifecycleReceipt
from mcpack_evidence.item7_runtime import PreflightReceipt  # noqa: TC001
from mcpack_evidence.item7_world_archive_inventory import validate_world_archive_inventory

_ARCHIVE_COUNT: Final = 4


class _Strict(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)


class _GapReceipt(_Strict):
    schema_version: Literal["item7-gap-run-v1"]
    preflight: PreflightReceipt
    lifecycle: GapLifecycleReceipt
    configuration: dict[str, JsonValue]
    rejection_reason: None


def validate_gaps(raw_root: Path) -> tuple[ArtifactIdentity, ...]:
    """Require both fresh targeted runs to reproduce the same four coordinates."""
    receipts: list[tuple[Path, _GapReceipt]] = []
    expected = tuple(target.structure for target in GAP_TARGETS)
    for run_id in ("gap-a", "gap-b"):
        path = raw_root / run_id / "ordinary" / "run-receipt.json"
        receipt = strict_model(path, _GapReceipt)
        lifecycle = receipt.lifecycle
        if (
            receipt.preflight.seed_role != "ordinary"
            or receipt.preflight.seed != "42"
            or tuple(row.structure for row in lifecycle.located_targets) != expected
            or tuple(lifecycle.completed_targets) != expected
            or not all(
                (
                    lifecycle.ready,
                    lifecycle.save_all_flush,
                    lifecycle.clean_stop,
                    lifecycle.return_code == 0,
                    not lifecycle.process_group_killed,
                    lifecycle.rejection_reason is None,
                )
            )
        ):
            fail("targeted gap lifecycle", path)
        receipts.append((path, receipt))
    coordinates = [
        tuple((row.structure, row.x, row.z) for row in receipt.lifecycle.located_targets)
        for _path, receipt in receipts
    ]
    if coordinates[0] != coordinates[1]:
        fail("targeted gap coordinate reproducibility", raw_root)
    return tuple(
        identity(path, f"{path.parts[-3]}/ordinary/run-receipt.json") for path, _ in receipts
    )


def validate_archives(
    manifests: tuple[Path, ...],
    receipts: tuple[Path, ...],
    required: tuple[ArtifactIdentity, ...],
    world_inventory: Path,
) -> tuple[ArtifactIdentity, ...]:
    """Bind four immutable archive manifests to four verified restore receipts."""
    if len(manifests) != _ARCHIVE_COUNT or len(receipts) != _ARCHIVE_COUNT:
        fail("archive pair count", len(manifests))
    output: list[ArtifactIdentity] = []
    names: set[str] = set()
    archived: dict[str, list[tuple[str, int]]] = {}
    parsed_manifests: list[ArchiveManifest] = []
    for index, (manifest_path, receipt_path) in enumerate(zip(manifests, receipts, strict=True)):
        manifest = strict_model(manifest_path, ArchiveManifest)
        parsed_manifests.append(manifest)
        receipt = strict_model(receipt_path, RestoreReceipt)
        if (
            receipt.archive_name != manifest.archive_name
            or receipt.archive_sha256 != manifest.archive_sha256
            or receipt.manifest_sha256 != sha256_file(manifest_path)
            or receipt.revision != manifest.revision
            or receipt.file_count != manifest.file_count
            or receipt.total_size_bytes != manifest.total_size_bytes
            or manifest.archive_name in names
        ):
            fail("archive restore identity", manifest_path)
        names.add(manifest.archive_name)
        for row in manifest.files:
            archived.setdefault(row.relative_path, []).append((row.sha256, row.size_bytes))
        output.extend(
            (
                identity(manifest_path, f"archive/archive-{index + 1}-manifest.json"),
                identity(receipt_path, f"archive/archive-{index + 1}-restore.json"),
            )
        )
    for artifact in required:
        if archived.get(artifact.path) != [(artifact.sha256, artifact.size_bytes)]:
            fail("archive cross-input identity", artifact.path)
    output.append(validate_world_archive_inventory(world_inventory, tuple(parsed_manifests)))
    return tuple(output)
