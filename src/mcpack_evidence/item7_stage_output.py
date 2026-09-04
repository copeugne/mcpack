"""Descriptor-bound output trees for Item 7 evidence staging."""

from __future__ import annotations

import ctypes
import errno
import os
import secrets
import shutil
import stat
from contextlib import contextmanager, suppress
from dataclasses import dataclass
from typing import TYPE_CHECKING, Final, cast

from .item7_archive_io import open_directory

if TYPE_CHECKING:
    from collections.abc import Generator
    from pathlib import Path, PurePosixPath
    from typing import IO, Protocol

    class _RenameAt2(Protocol):
        argtypes: list[object]
        restype: object

        def __call__(
            self,
            source_directory: int,
            source: bytes,
            target_directory: int,
            target: bytes,
            flags: int,
            /,
        ) -> int: ...


_ATTEMPTS: Final = 32
_RENAME_NOREPLACE: Final = 1


class StageOutputError(ValueError):
    """A stage output stopped naming its pinned filesystem identity."""


@dataclass(slots=True)
class StagingTree:
    """An unpublished output tree owned through pinned directory descriptors."""

    parent_path: Path
    target_name: str
    parent_descriptor: int
    root_descriptor: int
    temporary_name: str
    published: bool = False

    def write(self, relative: PurePosixPath, source: IO[bytes], size: int) -> None:
        """Write one regular file below the pinned output root."""
        parts = _relative_parts(relative)
        parent = _create_directories(self.root_descriptor, parts[:-1])
        descriptor = -1
        try:
            descriptor = os.open(
                parts[-1],
                os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC,
                0o600,
                dir_fd=parent,
            )
            with os.fdopen(descriptor, "wb") as output:
                descriptor = -1
                _ = shutil.copyfileobj(source, output)
                output.flush()
                metadata = os.fstat(output.fileno())
            if metadata.st_size != size:
                message = f"source changed while staging: {relative}"
                raise StageOutputError(message)
        finally:
            if descriptor >= 0:
                os.close(descriptor)
            os.close(parent)

    def publish(self) -> None:
        """Publish the complete tree without replacing an existing target."""
        self.require_named()
        _rename_noreplace(
            self.parent_descriptor,
            self.temporary_name,
            self.target_name,
        )
        self.temporary_name = self.target_name
        self.require_named()
        self.published = True

    def require_named(self) -> None:
        """Require the pinned parent and tree to retain their approved names."""
        _require_named_directory(self.parent_descriptor, self.parent_path)
        _require_named_tree(
            self.parent_descriptor,
            self.temporary_name,
            self.root_descriptor,
        )

    def close(self) -> None:
        """Close the pinned tree and remove unpublished process-owned output."""
        try:
            if not self.published:
                _clear_tree(self.root_descriptor)
                _remove_named_tree(
                    self.parent_descriptor,
                    self.temporary_name,
                    self.root_descriptor,
                )
        finally:
            os.close(self.root_descriptor)


@contextmanager
def staging_tree(target: Path) -> Generator[StagingTree]:
    """Create an unpublished tree below the pinned parent of an absent target."""
    if not target.name:
        message = f"stage output must name a directory: {target}"
        raise StageOutputError(message)
    with open_directory(target.parent) as parent:
        name, root = _create_tree(parent)
        tree = StagingTree(target.parent, target.name, parent, root, name)
        try:
            yield tree
        finally:
            tree.close()


def _create_tree(parent: int) -> tuple[str, int]:
    for _ in range(_ATTEMPTS):
        name = f".item7-stage-{secrets.token_hex(16)}"
        try:
            os.mkdir(name, mode=0o700, dir_fd=parent)
        except FileExistsError:
            continue
        try:
            descriptor = os.open(
                name,
                os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
                dir_fd=parent,
            )
        except Exception:
            os.rmdir(name, dir_fd=parent)
            raise
        return name, descriptor
    message = "could not allocate an evidence staging directory"
    raise FileExistsError(message)


def _relative_parts(relative: PurePosixPath) -> tuple[str, ...]:
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        message = f"unsafe stage output path: {relative}"
        raise StageOutputError(message)
    return relative.parts


def _create_directories(root: int, parts: tuple[str, ...]) -> int:
    descriptor = os.dup(root)
    try:
        for part in parts:
            with suppress(FileExistsError):
                os.mkdir(part, mode=0o700, dir_fd=descriptor)
            child = os.open(
                part,
                os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
                dir_fd=descriptor,
            )
            os.close(descriptor)
            descriptor = child
    except Exception:
        os.close(descriptor)
        raise
    return descriptor


def _require_named_directory(descriptor: int, path: Path) -> None:
    message = f"stage output parent changed: {path}"
    try:
        actual = path.stat(follow_symlinks=False)
    except OSError as error:
        raise StageOutputError(message) from error
    expected = os.fstat(descriptor)
    if (actual.st_dev, actual.st_ino) != (expected.st_dev, expected.st_ino):
        raise StageOutputError(message)


def _require_named_tree(parent: int, name: str, descriptor: int) -> None:
    message = "stage temporary directory changed"
    try:
        actual = os.stat(name, dir_fd=parent, follow_symlinks=False)
    except OSError as error:
        raise StageOutputError(message) from error
    expected = os.fstat(descriptor)
    if not stat.S_ISDIR(actual.st_mode) or (
        actual.st_dev,
        actual.st_ino,
    ) != (expected.st_dev, expected.st_ino):
        raise StageOutputError(message)


def _rename_noreplace(parent: int, source: str, target: str) -> None:
    rename = _load_renameat2()
    _ = ctypes.set_errno(0)
    result = rename(
        parent,
        os.fsencode(source),
        parent,
        os.fsencode(target),
        _RENAME_NOREPLACE,
    )
    if result == 0:
        return
    error_number = ctypes.get_errno()
    if error_number == errno.EEXIST:
        raise FileExistsError(error_number, os.strerror(error_number), target)
    raise OSError(error_number, os.strerror(error_number), target)


def _load_renameat2() -> _RenameAt2:
    library = ctypes.CDLL(None, use_errno=True)
    rename = cast("_RenameAt2", cast("object", library.renameat2))
    rename.argtypes = [
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_uint,
    ]
    rename.restype = ctypes.c_int
    return rename


def _clear_tree(directory: int) -> None:
    _ = os.lseek(directory, 0, os.SEEK_SET)
    for name in os.listdir(directory):
        metadata = os.stat(name, dir_fd=directory, follow_symlinks=False)
        if stat.S_ISDIR(metadata.st_mode):
            child = os.open(
                name,
                os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
                dir_fd=directory,
            )
            try:
                _clear_tree(child)
            finally:
                os.close(child)
            os.rmdir(name, dir_fd=directory)
        else:
            os.unlink(name, dir_fd=directory)


def _remove_named_tree(parent: int, name: str, root: int) -> None:
    try:
        named = os.stat(name, dir_fd=parent, follow_symlinks=False)
    except FileNotFoundError:
        return
    opened = os.fstat(root)
    if stat.S_ISDIR(named.st_mode) and (named.st_dev, named.st_ino) == (
        opened.st_dev,
        opened.st_ino,
    ):
        os.rmdir(name, dir_fd=parent)
