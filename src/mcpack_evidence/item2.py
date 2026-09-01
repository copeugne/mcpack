"""Item 2 pristine-baseline evidence contract."""

from __future__ import annotations

import hashlib
from pathlib import PurePosixPath
from typing import TYPE_CHECKING, ClassVar

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from pathlib import Path


class ArtifactRecord(BaseModel):
    """One immutable file identity in a frozen baseline."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    path: str = Field(min_length=1)
    size_bytes: int = Field(ge=0)
    sha256: str = Field(pattern=r"^[0-9a-f]{64}$")


class BaselineManifest(BaseModel):
    """Boundary-parsed identity of a reconstructable Item 2 baseline."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    schema_version: str
    minecraft: str
    neoforge: str
    java_vendor: str
    java_version: str
    enabled_artifacts: tuple[str, ...]
    disabled_artifacts: tuple[str, ...]
    directories: tuple[str, ...]
    files: tuple[ArtifactRecord, ...]


class BaselineIdentity(BaseModel):
    """Pinned platform and artifact state used to build a baseline manifest."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    minecraft: str
    neoforge: str
    java_vendor: str
    java_version: str
    enabled_artifacts: tuple[str, ...]
    disabled_artifacts: tuple[str, ...]


class EvidenceIssue(BaseModel):
    """One deterministic reason an Item 2 evidence tree is unacceptable."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    code: str
    path: str
    detail: str


def _is_safe_relative_path(path: str) -> bool:
    candidate = PurePosixPath(path)
    return not candidate.is_absolute() and ".." not in candidate.parts and path != "."


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as artifact:
        while chunk := artifact.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def build_baseline_manifest(
    baseline_root: Path,
    identity: BaselineIdentity,
) -> BaselineManifest:
    """Build a stable identity manifest for a stopped baseline tree."""
    directories = tuple(
        path.relative_to(baseline_root).as_posix()
        for path in sorted(baseline_root.rglob("*"))
        if path.is_dir()
    )
    files = tuple(
        ArtifactRecord(
            path=path.relative_to(baseline_root).as_posix(),
            size_bytes=path.stat().st_size,
            sha256=_sha256_file(path),
        )
        for path in sorted(baseline_root.rglob("*"))
        if path.is_file()
    )
    return BaselineManifest(
        schema_version="item2-baseline-v1",
        minecraft=identity.minecraft,
        neoforge=identity.neoforge,
        java_vendor=identity.java_vendor,
        java_version=identity.java_version,
        enabled_artifacts=identity.enabled_artifacts,
        disabled_artifacts=identity.disabled_artifacts,
        directories=directories,
        files=files,
    )


def _validate_manifest_files(
    records: tuple[ArtifactRecord, ...],
    baseline_root: Path,
) -> tuple[tuple[EvidenceIssue, ...], set[str]]:
    issues: list[EvidenceIssue] = []
    expected_files: set[str] = set()
    for record in records:
        if not _is_safe_relative_path(record.path):
            issues.append(
                EvidenceIssue(
                    code="unsafe_path",
                    path=record.path,
                    detail="manifest path must remain inside the baseline root",
                )
            )
            continue
        expected_files.add(record.path)
        artifact_path = baseline_root / record.path
        if not artifact_path.is_file():
            issues.append(
                EvidenceIssue(
                    code="missing_file",
                    path=record.path,
                    detail="manifest path is absent",
                )
            )
            continue

        actual_size = artifact_path.stat().st_size
        if actual_size != record.size_bytes:
            issues.append(
                EvidenceIssue(
                    code="size_mismatch",
                    path=record.path,
                    detail=f"expected {record.size_bytes} bytes, found {actual_size}",
                )
            )

        actual_sha256 = _sha256_file(artifact_path)
        if actual_sha256 != record.sha256:
            issues.append(
                EvidenceIssue(
                    code="sha256_mismatch",
                    path=record.path,
                    detail=f"expected {record.sha256}, found {actual_sha256}",
                )
            )

    return tuple(issues), expected_files


def _validate_manifest_directories(
    directories: tuple[str, ...],
    baseline_root: Path,
) -> tuple[tuple[EvidenceIssue, ...], set[str]]:
    issues: list[EvidenceIssue] = []
    expected_directories: set[str] = set()
    for directory in directories:
        if not _is_safe_relative_path(directory):
            issues.append(
                EvidenceIssue(
                    code="unsafe_path",
                    path=directory,
                    detail="manifest directory must remain inside the baseline root",
                )
            )
            continue
        expected_directories.add(directory)
        if not (baseline_root / directory).is_dir():
            issues.append(
                EvidenceIssue(
                    code="missing_directory",
                    path=directory,
                    detail="manifest directory is absent",
                )
            )

    return tuple(issues), expected_directories


def _unexpected_tree_entries(
    baseline_root: Path,
    expected_files: set[str],
    expected_directories: set[str],
) -> tuple[EvidenceIssue, ...]:
    issues: list[EvidenceIssue] = []
    actual_files = {
        path.relative_to(baseline_root).as_posix()
        for path in baseline_root.rglob("*")
        if path.is_file()
    }
    issues.extend(
        EvidenceIssue(code="unexpected_file", path=path, detail="file is not in the manifest")
        for path in sorted(actual_files - expected_files)
    )

    actual_directories = {
        path.relative_to(baseline_root).as_posix()
        for path in baseline_root.rglob("*")
        if path.is_dir()
    }
    issues.extend(
        EvidenceIssue(
            code="unexpected_directory",
            path=path,
            detail="directory is not in the manifest",
        )
        for path in sorted(actual_directories - expected_directories)
    )
    return tuple(issues)


def validate_baseline_evidence(
    manifest_path: Path,
    baseline_root: Path,
) -> tuple[EvidenceIssue, ...]:
    """Validate a baseline tree against its machine-readable manifest."""
    manifest = BaselineManifest.model_validate_json(manifest_path.read_text(encoding="utf-8"))
    file_issues, expected_files = _validate_manifest_files(manifest.files, baseline_root)
    directory_issues, expected_directories = _validate_manifest_directories(
        manifest.directories,
        baseline_root,
    )
    issues = [*file_issues, *directory_issues]
    issues.extend(
        _unexpected_tree_entries(
            baseline_root,
            expected_files,
            expected_directories,
        )
    )
    return tuple(issues)
