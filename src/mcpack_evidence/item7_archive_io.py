"""Descriptor-safe filesystem access for Item 7 archives."""

from __future__ import annotations

import errno
import hashlib
import os
import stat
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
    HARDLINK = "source contains a hardlink"
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
        _require_regular(metadata, path)
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


@contextmanager
def open_directory(path: Path) -> Generator[int]:
    """Open and pin a symlink-free directory path."""
    descriptor = _open_directory(path)
    try:
        yield descriptor
    finally:
        os.close(descriptor)


@contextmanager
def open_regular_at(
    directory: int, relative: PurePosixPath, *, writable: bool = False
) -> Generator[tuple[int, os.stat_result]]:
    """Open one relative regular file below a pinned directory."""
    parent = _open_relative_directory(directory, relative.parts[:-1])
    descriptor = -1
    try:
        descriptor = _open_at(parent, relative.name, writable=writable)
        metadata = os.fstat(descriptor)
        _require_regular(metadata, relative)
        yield descriptor, metadata
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        os.close(parent)


@contextmanager
def open_tree_at(directory: int, relative: PurePosixPath) -> Generator[tuple[OpenedFile, ...]]:
    """Open and pin a relative subtree below a pinned directory."""
    root_descriptor = _open_relative_directory(directory, relative.parts)
    files: list[OpenedFile] = []
    try:
        _walk(root_descriptor, relative, files)
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


def sha256_descriptor(descriptor: int) -> str:
    """Hash the complete bytes of one pinned descriptor."""
    with duplicate_stream(descriptor) as stream:
        digest = hashlib.sha256()
        while block := stream.read(1024 * 1024):
            digest.update(block)
        return digest.hexdigest()


def _walk(directory: int, prefix: PurePosixPath, files: list[OpenedFile]) -> None:
    _ = os.lseek(directory, 0, os.SEEK_SET)
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
        if opened_metadata.st_nlink != 1:
            os.close(descriptor)
            raise UnsafeFilesystemError(_FilesystemIssue.HARDLINK, relative)
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


def _open_relative_directory(directory: int, parts: tuple[str, ...]) -> int:
    descriptor = os.dup(directory)
    try:
        for component in parts:
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
            raise UnsafeFilesystemError(_FilesystemIssue.UNSAFE_DIRECTORY, parts) from error
        raise
    return descriptor


def _open_at(directory: int, name: str, *, writable: bool = False) -> int:
    try:
        return os.open(
            name,
            (os.O_RDWR if writable else os.O_RDONLY) | os.O_NONBLOCK | os.O_NOFOLLOW | os.O_CLOEXEC,
            dir_fd=directory,
        )
    except OSError as error:
        if error.errno == errno.ELOOP:
            raise UnsafeFilesystemError(_FilesystemIssue.SYMLINK, name) from error
        raise


def _require_regular(metadata: os.stat_result, path: object) -> None:
    if not stat.S_ISREG(metadata.st_mode):
        raise UnsafeFilesystemError(_FilesystemIssue.NONREGULAR, path)
    if metadata.st_nlink != 1:
        raise UnsafeFilesystemError(_FilesystemIssue.HARDLINK, path)
