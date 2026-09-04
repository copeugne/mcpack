"""Descriptor-bound publication helpers for Item 7 archives."""

from __future__ import annotations

import gzip
import hashlib
import os
import secrets
import tarfile
from contextlib import suppress
from dataclasses import dataclass
from typing import TYPE_CHECKING, Final

from .item7_archive_io import OpenedFile, duplicate_stream

if TYPE_CHECKING:
    from pathlib import Path

_ATTEMPTS: Final = 32


class UnsafePublicationError(ValueError):
    """An output directory stopped naming its pinned filesystem identity."""


@dataclass(frozen=True, slots=True)
class TemporaryFile:
    """A temporary regular file pinned with its owning directory."""

    directory: int
    name: str
    descriptor: int


@dataclass(frozen=True, slots=True)
class Publication:
    """One descriptor-bound temporary file and its requested final path."""

    temporary: TemporaryFile
    name: str
    parent: Path


@dataclass(frozen=True, slots=True)
class TarIdentity:
    """Content identity read back from one generated tar member."""

    name: str
    size: int
    sha256: str


def build_tar(directory: int, files: tuple[OpenedFile, ...]) -> TemporaryFile:
    """Build a deterministic tar stream without returning to a pathname."""
    temporary = _create_temporary(directory)
    try:
        with (
            os.fdopen(os.dup(temporary.descriptor), "wb") as stream,
            gzip.GzipFile(fileobj=stream, mode="wb", filename="", mtime=0) as compressed,
            tarfile.open(fileobj=compressed, mode="w|", format=tarfile.PAX_FORMAT) as bundle,
        ):
            for opened in files:
                info = tarfile.TarInfo(opened.relative_path)
                info.size = opened.size_bytes
                info.mode = 0o644
                info.mtime = 0
                with duplicate_stream(opened.descriptor) as source:
                    bundle.addfile(info, source)
    except Exception:
        close_temporary(temporary)
        raise
    else:
        return temporary


def stage_bytes(directory: int, body: bytes) -> TemporaryFile:
    """Write bytes to a descriptor-bound temporary file."""
    temporary = _create_temporary(directory)
    try:
        with os.fdopen(os.dup(temporary.descriptor), "wb") as stream:
            _ = stream.write(body)
    except Exception:
        close_temporary(temporary)
        raise
    else:
        return temporary


def read_inventory(temporary: TemporaryFile) -> tuple[TarIdentity, ...]:
    """Read every generated tar member through the pinned descriptor."""
    identities: list[TarIdentity] = []
    with (
        duplicate_stream(temporary.descriptor) as archive_stream,
        tarfile.open(fileobj=archive_stream, mode="r:gz") as bundle,
    ):
        for member in bundle.getmembers():
            source = bundle.extractfile(member)
            if source is None:
                message = f"generated archive member is not regular: {member.name}"
                raise ValueError(message)
            with source:
                digest = hashlib.sha256()
                while block := source.read(1024 * 1024):
                    digest.update(block)
            identities.append(TarIdentity(member.name, member.size, digest.hexdigest()))
    return tuple(identities)


def publish_pair(archive: Publication, manifest: Publication) -> None:
    """Link both outputs only while their pinned parents keep their names."""
    _require_named_parent(archive.temporary.directory, archive.parent)
    _require_named_parent(manifest.temporary.directory, manifest.parent)
    os.link(
        manifest.temporary.name,
        manifest.name,
        src_dir_fd=manifest.temporary.directory,
        dst_dir_fd=manifest.temporary.directory,
        follow_symlinks=False,
    )
    try:
        os.link(
            archive.temporary.name,
            archive.name,
            src_dir_fd=archive.temporary.directory,
            dst_dir_fd=archive.temporary.directory,
            follow_symlinks=False,
        )
        _require_named_parent(archive.temporary.directory, archive.parent)
        _require_named_parent(manifest.temporary.directory, manifest.parent)
    except Exception:
        _unlink_if_identity(
            manifest.temporary.directory,
            manifest.name,
            manifest.temporary.descriptor,
        )
        _unlink_if_identity(
            archive.temporary.directory,
            archive.name,
            archive.temporary.descriptor,
        )
        raise


def close_temporary(temporary: TemporaryFile) -> None:
    """Close and unlink one descriptor-bound temporary file."""
    try:
        _unlink_if_present(temporary.directory, temporary.name)
    finally:
        os.close(temporary.descriptor)
        os.close(temporary.directory)


def _create_temporary(directory: int) -> TemporaryFile:
    owned_directory = os.dup(directory)
    try:
        return _allocate_temporary(owned_directory)
    except Exception:
        os.close(owned_directory)
        raise


def _allocate_temporary(directory: int) -> TemporaryFile:
    for _ in range(_ATTEMPTS):
        name = f".item7-{secrets.token_hex(16)}"
        try:
            descriptor = os.open(
                name,
                os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_CLOEXEC,
                0o600,
                dir_fd=directory,
            )
        except FileExistsError:
            continue
        return TemporaryFile(directory=directory, name=name, descriptor=descriptor)
    message = "could not allocate an archive temporary file"
    raise FileExistsError(message)


def _require_named_parent(descriptor: int, path: Path) -> None:
    try:
        actual = path.stat(follow_symlinks=False)
    except OSError as error:
        raise UnsafePublicationError(path) from error
    expected = os.fstat(descriptor)
    if (actual.st_dev, actual.st_ino) != (expected.st_dev, expected.st_ino):
        raise UnsafePublicationError(path)


def _unlink_if_present(directory: int, name: str) -> None:
    with suppress(FileNotFoundError):
        os.unlink(name, dir_fd=directory)


def _unlink_if_identity(directory: int, name: str, descriptor: int) -> None:
    try:
        published = os.stat(name, dir_fd=directory, follow_symlinks=False)
    except FileNotFoundError:
        return
    temporary = os.fstat(descriptor)
    if (published.st_dev, published.st_ino) == (temporary.st_dev, temporary.st_ino):
        os.unlink(name, dir_fd=directory)
