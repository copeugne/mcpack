"""Item 7 raw-evidence archive boundary."""

from __future__ import annotations

import os

from .item7_archive_io import (
    UnsafeFilesystemError,
    open_directory,
    open_tree,
    sha256_descriptor,
)
from .item7_archive_models import (
    ArchiveIssue,
    ArchiveManifest,
    ArchiveRequest,
    ArchiveValidationError,
    FileIdentity,
    RestoreReceipt,
    RestoreRequest,
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
from .item7_archive_restore import restore_archive

__all__ = (
    "ArchiveManifest",
    "ArchiveRequest",
    "ArchiveValidationError",
    "FileIdentity",
    "RestoreReceipt",
    "RestoreRequest",
    "create_archive",
    "restore_archive",
)


def create_archive(request: ArchiveRequest) -> ArchiveManifest:
    """Create a deterministic archive and publish its content manifest."""
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
        raise ArchiveValidationError(ArchiveIssue.SOURCE_SYMLINK, request.root) from error
    except UnsafePublicationError as error:
        raise ArchiveValidationError(ArchiveIssue.UNSAFE_PATH) from error
    except (FileNotFoundError, NotADirectoryError) as error:
        message = "archive source and output parents must be existing directories"
        raise NotADirectoryError(message) from error
    finally:
        if temporary is not None:
            close_temporary(temporary)
        if manifest_temporary is not None:
            close_temporary(manifest_temporary)
    return manifest
