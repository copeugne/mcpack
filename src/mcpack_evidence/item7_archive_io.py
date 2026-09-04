"""Descriptor-safe filesystem access for Item 7 archives."""

from __future__ import annotations

import errno
import gzip
import hashlib
import os
import stat
import tarfile
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator
    from typing import BinaryIO


@dataclass(frozen=True, slots=True)
class OpenedFile:
    """A regular file held open at one stable filesystem identity."""

    relative_path: str
    descriptor: int
    size_bytes: int


class UnsafeFilesystemError(ValueError):
    """A path crossed a symlink or nonregular filesystem entry."""

    def __init__(self, issue: _FilesystemIssue, path: object) -> None:
        """Preserve the closed issue and affected path component."""
        super().__init__(f"{issue.value}: {path}")


class _FilesystemIssue(StrEnum):
    NONREGULAR = "entry is not regular"
    UNSAFE_ENTRY = "unsafe directory entry"
    SYMLINK = "source contains a symlink"
    UNSAFE_DIRECTORY = "directory path is unsafe"


@contextmanager
def open_regular(path: Path) -> Generator[tuple[int, os.stat_result]]:
    """Open one regular file without following any path-component symlink."""
    parent = _open_directory(path.parent)
    descriptor = -1
    try:
        descriptor = _open_at(parent, path.name)
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise UnsafeFilesystemError(_FilesystemIssue.NONREGULAR, path)
        yield descriptor, metadata
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        os.close(parent)


@contextmanager
def open_tree(root: Path) -> Generator[tuple[OpenedFile, ...]]:
    """Open and pin every regular file below a symlink-free directory tree."""
    root_descriptor = _open_directory(root)
    files: list[OpenedFile] = []
    try:
        _walk(root_descriptor, PurePosixPath(), files)
        files.sort(key=lambda row: row.relative_path)
        yield tuple(files)
    finally:
        for opened in files:
            os.close(opened.descriptor)
        os.close(root_descriptor)


def duplicate_stream(descriptor: int) -> BinaryIO:
    """Return a binary stream over a duplicate of a pinned descriptor."""
    _ = os.lseek(descriptor, 0, os.SEEK_SET)
    return os.fdopen(os.dup(descriptor), "rb")


def build_tar(archive: Path, files: tuple[OpenedFile, ...]) -> Path:
    """Build a deterministic tar stream from pinned file descriptors."""
    with tempfile.NamedTemporaryFile(dir=archive.parent, delete=False) as stream:
        temporary = Path(stream.name)
        with (
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
    return temporary


def sha256_descriptor(descriptor: int) -> str:
    """Hash the complete bytes of one pinned descriptor."""
    with duplicate_stream(descriptor) as stream:
        digest = hashlib.sha256()
        while block := stream.read(1024 * 1024):
            digest.update(block)
        return digest.hexdigest()


def _walk(directory: int, prefix: PurePosixPath, files: list[OpenedFile]) -> None:
    for name in sorted(os.listdir(directory)):
        if name in {"", ".", ".."} or "/" in name:
            raise UnsafeFilesystemError(_FilesystemIssue.UNSAFE_ENTRY, name)
        relative = prefix / name
        metadata = os.stat(name, dir_fd=directory, follow_symlinks=False)
        if stat.S_ISLNK(metadata.st_mode):
            raise UnsafeFilesystemError(_FilesystemIssue.SYMLINK, relative)
        descriptor = _open_at(directory, name)
        opened_metadata = os.fstat(descriptor)
        if stat.S_ISDIR(opened_metadata.st_mode):
            try:
                _walk(descriptor, relative, files)
            finally:
                os.close(descriptor)
            continue
        if not stat.S_ISREG(opened_metadata.st_mode):
            os.close(descriptor)
            raise UnsafeFilesystemError(_FilesystemIssue.NONREGULAR, relative)
        if name == "session.lock":
            os.close(descriptor)
            continue
        files.append(
            OpenedFile(
                relative_path=relative.as_posix(),
                descriptor=descriptor,
                size_bytes=opened_metadata.st_size,
            )
        )


def _open_directory(path: Path) -> int:
    absolute = path.absolute()
    descriptor = os.open("/", os.O_RDONLY | os.O_DIRECTORY | os.O_CLOEXEC)
    try:
        for component in absolute.parts[1:]:
            next_descriptor = os.open(
                component,
                os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
                dir_fd=descriptor,
            )
            os.close(descriptor)
            descriptor = next_descriptor
    except OSError as error:
        os.close(descriptor)
        if error.errno in {errno.ELOOP, errno.ENOTDIR}:
            raise UnsafeFilesystemError(_FilesystemIssue.UNSAFE_DIRECTORY, path) from error
        raise
    return descriptor


def _open_at(directory: int, name: str) -> int:
    try:
        return os.open(
            name,
            os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW | os.O_CLOEXEC,
            dir_fd=directory,
        )
    except OSError as error:
        if error.errno == errno.ELOOP:
            raise UnsafeFilesystemError(_FilesystemIssue.SYMLINK, name) from error
        raise
