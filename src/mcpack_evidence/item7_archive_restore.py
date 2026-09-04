"""Verified restoration for Item 7 raw-evidence archives."""

from __future__ import annotations

import hashlib
import tarfile
from pathlib import Path, PurePosixPath

from .item7_archive_io import (
    UnsafeFilesystemError,
    duplicate_stream,
    open_directory,
    open_regular,
    open_tree_at,
    sha256_descriptor,
)
from .item7_archive_models import (
    ArchiveIssue,
    ArchiveManifest,
    ArchiveValidationError,
    FileIdentity,
    RestoreReceipt,
    RestoreRequest,
    require_relative_path,
)
from .item7_archive_publish import (
    Publication,
    UnsafePublicationError,
    close_temporary,
    publish_one,
    stage_bytes,
)
from .item7_stage_output import StageOutputError, StagingTree, staging_tree


def restore_archive(request: RestoreRequest) -> RestoreReceipt:
    """Verify an archive against its manifest and restore to an absent target."""
    _require_absent(request.target)
    _require_absent(request.receipt)
    receipt_temporary = None
    try:
        with (
            open_regular(request.manifest) as (manifest_descriptor, _),
            duplicate_stream(manifest_descriptor) as manifest_stream,
        ):
            manifest_bytes = manifest_stream.read()
        manifest = ArchiveManifest.model_validate_json(manifest_bytes)
        with (
            open_regular(request.archive) as (archive_descriptor, archive_metadata),
            open_directory(request.receipt.parent) as receipt_parent,
            staging_tree(request.target) as destination,
        ):
            if request.archive.name != manifest.archive_name:
                raise ArchiveValidationError(ArchiveIssue.ARCHIVE_NAME)
            if archive_metadata.st_size != manifest.archive_size_bytes:
                raise ArchiveValidationError(ArchiveIssue.ARCHIVE_SIZE)
            if sha256_descriptor(archive_descriptor) != manifest.archive_sha256:
                raise ArchiveValidationError(ArchiveIssue.ARCHIVE_HASH)
            with (
                duplicate_stream(archive_descriptor) as archive_stream,
                tarfile.open(fileobj=archive_stream, mode="r:gz") as bundle,
            ):
                _verify_and_extract(bundle, manifest, destination)
            _verify_restored_tree(destination, manifest)
            destination.publish()
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
            receipt_temporary = stage_bytes(
                receipt_parent,
                (receipt.model_dump_json(indent=2) + "\n").encode(),
            )
            publish_one(
                Publication(receipt_temporary, request.receipt.name, request.receipt.parent),
                destination.require_named,
            )
    except UnsafeFilesystemError as error:
        raise ArchiveValidationError(ArchiveIssue.UNSAFE_PATH) from error
    except (StageOutputError, UnsafePublicationError) as error:
        raise ArchiveValidationError(ArchiveIssue.UNSAFE_PATH) from error
    finally:
        if receipt_temporary is not None:
            close_temporary(receipt_temporary)
    return receipt


def _verify_and_extract(
    bundle: tarfile.TarFile,
    manifest: ArchiveManifest,
    staging: StagingTree,
) -> None:
    members = bundle.getmembers()
    for member in members:
        _ = require_relative_path(member.name)
        if not member.isfile():
            raise ArchiveValidationError(ArchiveIssue.NONREGULAR, member.name)
    expected_paths = tuple(identity.relative_path for identity in manifest.files)
    if tuple(member.name for member in members) != expected_paths:
        raise ArchiveValidationError(ArchiveIssue.MEMBERS_MISMATCH)
    for identity in manifest.files:
        member = bundle.getmember(identity.relative_path)
        source = bundle.extractfile(member)
        if source is None:
            raise ArchiveValidationError(ArchiveIssue.NONREGULAR, member.name)
        with source:
            staging.write(PurePosixPath(identity.relative_path), source, identity.size_bytes)


def _verify_restored_tree(staging: StagingTree, manifest: ArchiveManifest) -> None:
    with open_tree_at(staging.root_descriptor, PurePosixPath()) as files:
        restored = tuple(
            FileIdentity(
                relative_path=row.relative_path,
                size_bytes=row.size_bytes,
                sha256=sha256_descriptor(row.descriptor),
            )
            for row in files
        )
    if restored == manifest.files:
        return
    for expected, actual in zip(manifest.files, restored, strict=False):
        if expected != actual:
            detail = f"expected {expected.model_dump()} but restored {actual.model_dump()}"
            raise ArchiveValidationError(ArchiveIssue.RESTORED_HASH, detail)
    detail = f"expected {len(manifest.files)} files but restored {len(restored)}"
    raise ArchiveValidationError(ArchiveIssue.RESTORED_HASH, detail)


def _require_absent(path: Path) -> None:
    if path.exists() or path.is_symlink():
        message = f"destination already exists: {path}"
        raise FileExistsError(message)
