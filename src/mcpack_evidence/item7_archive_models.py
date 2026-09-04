"""Typed evidence identities for Item 7 raw archives."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path, PurePosixPath
from typing import ClassVar, Literal, Self, final, override

from pydantic import BaseModel, ConfigDict, Field, model_validator


@dataclass(frozen=True, slots=True)
class ArchiveRequest:
    """Inputs for one raw-evidence archive publication."""

    root: Path
    archive: Path
    manifest: Path
    revision: str


@dataclass(frozen=True, slots=True)
class RestoreRequest:
    """Inputs for one verified archive restoration."""

    archive: Path
    manifest: Path
    target: Path
    receipt: Path


@final
class ArchiveValidationError(ValueError):
    """A violated archive or manifest integrity invariant."""

    def __init__(self, issue: ArchiveIssue, path: str | Path | None = None) -> None:
        """Preserve the closed issue and optional affected path."""
        self.issue: ArchiveIssue = issue
        self.path: str | Path | None = path
        super().__init__(str(self))

    @override
    def __str__(self) -> str:
        return self.issue.value if self.path is None else f"{self.issue.value}: {self.path}"


class ArchiveIssue(StrEnum):
    """Closed reasons an archive operation can reject evidence."""

    NONBLANK_IDENTITY = "revision and archive name must be nonblank and trimmed"
    ARCHIVE_NAME = "archive name must be a basename ending in .tar.gz"
    MANIFEST_PATHS = "manifest paths must be sorted and unique"
    MANIFEST_COUNT = "manifest file count does not match files"
    MANIFEST_SIZE = "manifest total size does not match files"
    SOURCE_SYMLINK = "source contains a symlink"
    NONREGULAR = "entry is not regular"
    ARCHIVE_SIZE = "archive size does not match manifest"
    ARCHIVE_HASH = "archive SHA-256 does not match manifest"
    MEMBERS_MISMATCH = "archive members do not exactly match manifest"
    RESTORED_SIZE = "restored size mismatch"
    RESTORED_HASH = "restored SHA-256 mismatch"
    UNSAFE_PATH = "unsafe relative path"


class _EvidenceModel(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)


class FileIdentity(_EvidenceModel):
    """Content identity for one archived regular file."""

    relative_path: str
    size_bytes: int = Field(ge=0)
    sha256: str = Field(pattern=r"^[0-9a-f]{64}$")


class ArchiveManifest(_EvidenceModel):
    """Immutable identity and contents of one external Item 7 archive."""

    schema_version: Literal["item7-raw-evidence-archive-v1"] = "item7-raw-evidence-archive-v1"
    revision: str = Field(min_length=1)
    archive_name: str
    archive_size_bytes: int = Field(ge=0)
    archive_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    file_count: int = Field(ge=0)
    total_size_bytes: int = Field(ge=0)
    files: tuple[FileIdentity, ...]

    @model_validator(mode="after")
    def _validate_inventory(self) -> Self:
        if not self.revision.strip() or self.revision != self.revision.strip():
            raise ArchiveValidationError(ArchiveIssue.NONBLANK_IDENTITY)
        archive_name = self.archive_name
        if Path(archive_name).name != archive_name or not archive_name.endswith(".tar.gz"):
            raise ArchiveValidationError(ArchiveIssue.ARCHIVE_NAME)
        paths = tuple(row.relative_path for row in self.files)
        for path in paths:
            _ = require_relative_path(path)
        if paths != tuple(sorted(paths)) or len(paths) != len(set(paths)):
            raise ArchiveValidationError(ArchiveIssue.MANIFEST_PATHS)
        if self.file_count != len(self.files):
            raise ArchiveValidationError(ArchiveIssue.MANIFEST_COUNT)
        if self.total_size_bytes != sum(row.size_bytes for row in self.files):
            raise ArchiveValidationError(ArchiveIssue.MANIFEST_SIZE)
        return self


class RestoreReceipt(_EvidenceModel):
    """Proof that an archive was verified before restoration."""

    schema_version: Literal["item7-raw-evidence-restore-v1"] = "item7-raw-evidence-restore-v1"
    revision: str
    archive_name: str
    archive_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    manifest_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    restored_target: str
    file_count: int = Field(ge=0)
    total_size_bytes: int = Field(ge=0)
    verified: Literal[True]


def require_relative_path(value: str) -> str:
    """Reject unsafe or non-canonical archive member paths."""
    candidate = PurePosixPath(value)
    if any((not value, candidate.is_absolute(), ".." in candidate.parts, value != str(candidate))):
        raise ArchiveValidationError(ArchiveIssue.UNSAFE_PATH, value)
    return value
