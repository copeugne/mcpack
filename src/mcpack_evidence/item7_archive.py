"""Item 7 raw-evidence archive boundary."""

from __future__ import annotations

import hashlib
import os
import shutil
import tarfile
import tempfile
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path, PurePosixPath
from typing import ClassVar, Literal, Self, final, override

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .item7_archive_io import (
    UnsafeFilesystemError,
    duplicate_stream,
    open_directory,
    open_regular,
    open_tree,
    sha256_descriptor,
)
from .item7_archive_publish import (
    Publication,
    UnsafePublicationError,
    build_tar,
    close_temporary,
    publish_pair,
    read_inventory,
    stage_bytes,
)


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

    def __init__(self, issue: _ArchiveIssue, path: str | Path | None = None) -> None:
        """Preserve the closed issue and optional affected path."""
        self.issue: _ArchiveIssue = issue
        self.path: str | Path | None = path
        super().__init__(str(self))

    @override
    def __str__(self) -> str:
        return self.issue.value if self.path is None else f"{self.issue.value}: {self.path}"


class _ArchiveIssue(StrEnum):
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
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")


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
            raise ArchiveValidationError(_ArchiveIssue.NONBLANK_IDENTITY)
        archive_name = self.archive_name
        if Path(archive_name).name != archive_name or not archive_name.endswith(".tar.gz"):
            raise ArchiveValidationError(_ArchiveIssue.ARCHIVE_NAME)
        paths = tuple(row.relative_path for row in self.files)
        for path in paths:
            _ = _require_relative_path(path)
        if paths != tuple(sorted(paths)) or len(paths) != len(set(paths)):
            raise ArchiveValidationError(_ArchiveIssue.MANIFEST_PATHS)
        if self.file_count != len(self.files):
            raise ArchiveValidationError(_ArchiveIssue.MANIFEST_COUNT)
        if self.total_size_bytes != sum(row.size_bytes for row in self.files):
            raise ArchiveValidationError(_ArchiveIssue.MANIFEST_SIZE)
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


def create_archive(request: ArchiveRequest) -> ArchiveManifest:
    """Create a deterministic archive and publish its content manifest."""
    request.archive.parent.mkdir(parents=True, exist_ok=True)
    request.manifest.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    manifest_temporary = None
    try:
        with (
            open_directory(request.archive.parent) as archive_parent,
            open_directory(request.manifest.parent) as manifest_parent,
            open_tree(request.root) as files,
        ):
            temporary = build_tar(archive_parent, files)
            identities = tuple(
                FileIdentity(
                    relative_path=row.name,
                    size_bytes=row.size,
                    sha256=row.sha256,
                )
                for row in read_inventory(temporary)
            )
            metadata = os.fstat(temporary.descriptor)
            manifest = ArchiveManifest(
                revision=request.revision,
                archive_name=request.archive.name,
                archive_size_bytes=metadata.st_size,
                archive_sha256=sha256_descriptor(temporary.descriptor),
                file_count=len(identities),
                total_size_bytes=sum(row.size_bytes for row in identities),
                files=identities,
            )
            manifest_body = (manifest.model_dump_json(indent=2) + "\n").encode()
            manifest_temporary = stage_bytes(manifest_parent, manifest_body)
            publish_pair(
                Publication(temporary, request.archive.name, request.archive.parent),
                Publication(manifest_temporary, request.manifest.name, request.manifest.parent),
            )
    except UnsafeFilesystemError as error:
        raise ArchiveValidationError(_ArchiveIssue.SOURCE_SYMLINK, request.root) from error
    except UnsafePublicationError as error:
        raise ArchiveValidationError(_ArchiveIssue.UNSAFE_PATH) from error
    except (FileNotFoundError, NotADirectoryError) as error:
        message = f"raw evidence root is not a directory: {request.root}"
        raise NotADirectoryError(message) from error
    finally:
        if temporary is not None:
            close_temporary(temporary)
        if manifest_temporary is not None:
            close_temporary(manifest_temporary)
    return manifest


def restore_archive(request: RestoreRequest) -> RestoreReceipt:
    """Verify an archive against its manifest and restore to an absent target."""
    _require_absent(request.target)
    _require_absent(request.receipt)
    try:
        with (
            open_regular(request.manifest) as (manifest_descriptor, _),
            duplicate_stream(manifest_descriptor) as manifest_stream,
        ):
            manifest_bytes = manifest_stream.read()
        manifest = ArchiveManifest.model_validate_json(manifest_bytes)
        with open_regular(request.archive) as (archive_descriptor, archive_metadata):
            if request.archive.name != manifest.archive_name:
                raise ArchiveValidationError(_ArchiveIssue.ARCHIVE_NAME)
            if archive_metadata.st_size != manifest.archive_size_bytes:
                raise ArchiveValidationError(_ArchiveIssue.ARCHIVE_SIZE)
            if sha256_descriptor(archive_descriptor) != manifest.archive_sha256:
                raise ArchiveValidationError(_ArchiveIssue.ARCHIVE_HASH)
            request.target.parent.mkdir(parents=True, exist_ok=True)
            staging = Path(tempfile.mkdtemp(dir=request.target.parent))
            try:
                with (
                    duplicate_stream(archive_descriptor) as archive_stream,
                    tarfile.open(fileobj=archive_stream, mode="r:gz") as bundle,
                ):
                    _verify_and_extract(bundle, manifest, staging)
                _ = shutil.copytree(staging, request.target)
            finally:
                if staging.exists():
                    _ = shutil.rmtree(staging)
    except UnsafeFilesystemError as error:
        raise ArchiveValidationError(_ArchiveIssue.UNSAFE_PATH) from error
    receipt = RestoreReceipt(
        revision=manifest.revision,
        archive_name=manifest.archive_name,
        archive_sha256=manifest.archive_sha256,
        manifest_sha256=hashlib.sha256(manifest_bytes).hexdigest(),
        restored_target=request.target.as_posix(),
        file_count=manifest.file_count,
        total_size_bytes=manifest.total_size_bytes,
        verified=True,
    )
    receipt_temporary = _stage_text(request.receipt, receipt.model_dump_json(indent=2) + "\n")
    os.link(receipt_temporary, request.receipt)
    receipt_temporary.unlink()
    return receipt


def _verify_and_extract(bundle: tarfile.TarFile, manifest: ArchiveManifest, staging: Path) -> None:
    members = bundle.getmembers()
    for member in members:
        _ = _require_relative_path(member.name)
        if not member.isfile():
            raise ArchiveValidationError(_ArchiveIssue.NONREGULAR, member.name)
    expected_paths = tuple(identity.relative_path for identity in manifest.files)
    if tuple(member.name for member in members) != expected_paths:
        raise ArchiveValidationError(_ArchiveIssue.MEMBERS_MISMATCH)
    for identity in manifest.files:
        member = bundle.getmember(identity.relative_path)
        source = bundle.extractfile(member)
        if source is None:
            raise ArchiveValidationError(_ArchiveIssue.NONREGULAR, member.name)
        destination = staging / identity.relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        with source, destination.open("wb") as output:
            _ = shutil.copyfileobj(source, output)
        if destination.stat().st_size != identity.size_bytes:
            raise ArchiveValidationError(_ArchiveIssue.RESTORED_SIZE, identity.relative_path)
        if _sha256(destination) != identity.sha256:
            raise ArchiveValidationError(_ArchiveIssue.RESTORED_HASH, identity.relative_path)


def _stage_text(path: Path, body: str) -> Path:
    with tempfile.NamedTemporaryFile("wb", prefix=".", dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        _ = stream.write(body.encode("utf-8"))
    return temporary


def _require_relative_path(value: str) -> str:
    candidate = PurePosixPath(value)
    if any((not value, candidate.is_absolute(), ".." in candidate.parts, value != str(candidate))):
        raise ArchiveValidationError(_ArchiveIssue.UNSAFE_PATH, value)
    return value


def _require_absent(path: Path) -> None:
    if path.exists() or path.is_symlink():
        message = f"destination already exists: {path}"
        raise FileExistsError(message)


def _sha256(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()
