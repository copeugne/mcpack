"""Stage Item 7 raw evidence with locked, independent world copies."""

from __future__ import annotations

import argparse
import errno
import fcntl
import shutil
import tempfile
from contextlib import contextmanager
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Final, final

from mcpack_evidence.item7_archive_io import (
    OpenedFile,
    UnsafeFilesystemError,
    duplicate_stream,
    open_directory,
    open_regular_at,
    open_tree,
    open_tree_at,
)

if TYPE_CHECKING:
    from collections.abc import Generator, Sequence

RUN_ROLES: Final = ("ordinary", "mountainous", "ocean-heavy", "biome-diverse")
AUXILIARY_INSTANCES: Final = (
    "control-ordinary",
    "control-ordinary-failed-marker",
    "gap-a-ordinary",
    "gap-a-ordinary-rejected-config-contract",
    "gap-b-ordinary",
    "pilot-characterization",
    "pilot-tracked-ordinary",
    "pilot-tracked-ordinary-success",
)
WORLD_FILES: Final = ("level.dat", "level.dat_old")
WORLD_DIRECTORIES: Final = ("region", "DIM-1/region", "DIM1/region")
MODES: Final = ("core", "run-a-worlds", "run-b-worlds", "auxiliary-worlds")


class StageError(ValueError):
    """The requested raw-evidence stage is unsafe or incomplete."""


@final
class _Namespace(argparse.Namespace):
    def __init__(self) -> None:
        """Supply typed placeholders that argparse replaces with required values."""
        super().__init__()
        self.mode = ""
        self.project = Path()
        self.raw = Path()
        self.output = Path()


def stage(mode: str, project: Path, raw: Path, output: Path) -> tuple[int, int]:
    """Create one Item 7 stage and return its file count and byte size."""
    if mode not in MODES:
        message = f"unknown stage mode: {mode}"
        raise StageError(message)
    if not project.is_dir() or not raw.is_dir() or output.exists() or output.is_symlink():
        message = "project and raw roots must exist, and output must be absent"
        raise StageError(message)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".item7-stage-", dir=output.parent))
    try:
        if mode == "core":
            with open_tree(raw) as files:
                _copy_opened_files(files, temporary)
        else:
            for name in _instance_names(mode):
                destination = temporary / name / "world"
                copy_world_boundary(project / "instances/item7" / name, destination)
        _ = temporary.rename(output)
    except UnsafeFilesystemError as error:
        raise StageError(str(error)) from error
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
    files = tuple(path for path in output.rglob("*") if path.is_file())
    return len(files), sum(path.stat().st_size for path in files)


def copy_world_boundary(instance: Path, destination: Path) -> None:
    """Copy the declared stopped-world boundary while holding its record lock."""
    world = instance / "world"
    if destination.exists() or destination.is_symlink():
        message = f"stage destination already exists: {destination}"
        raise StageError(message)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".item7-world-", dir=destination.parent))
    try:
        _copy_locked_world(world, temporary)
        _ = temporary.rename(destination)
    except UnsafeFilesystemError as error:
        raise StageError(str(error)) from error
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)


def _copy_locked_world(world: Path, destination: Path) -> None:
    with open_directory(world) as world_descriptor:
        lock_path = PurePosixPath("session.lock")
        try:
            lock_context = open_regular_at(world_descriptor, lock_path, writable=True)
            with lock_context as (lock_descriptor, _):
                _copy_under_lock(world_descriptor, lock_descriptor, destination)
        except FileNotFoundError as error:
            message = f"world session lock is missing or unsafe: {world / lock_path}"
            raise StageError(message) from error


def _copy_under_lock(directory: int, lock: int, destination: Path) -> None:
    with _record_lock(lock):
        for value in WORLD_FILES:
            relative = PurePosixPath(value)
            try:
                with open_regular_at(directory, relative) as (descriptor, metadata):
                    _copy_descriptor(descriptor, metadata.st_size, relative, destination)
            except FileNotFoundError:
                continue
        for value in WORLD_DIRECTORIES:
            relative = PurePosixPath(value)
            try:
                with open_tree_at(directory, relative) as files:
                    _copy_opened_files(files, destination)
            except FileNotFoundError:
                continue


@contextmanager
def _record_lock(descriptor: int) -> Generator[None]:
    try:
        fcntl.lockf(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError as error:
        if error.errno in {errno.EACCES, errno.EAGAIN}:
            message = "world is active"
            raise StageError(message) from error
        raise
    try:
        yield
    finally:
        fcntl.lockf(descriptor, fcntl.LOCK_UN)


def _copy_opened_files(files: tuple[OpenedFile, ...], destination: Path) -> None:
    for opened in files:
        relative = PurePosixPath(opened.relative_path)
        _require_allowed(relative)
        _copy_descriptor(opened.descriptor, opened.size_bytes, relative, destination)


def _copy_descriptor(descriptor: int, size: int, relative: PurePosixPath, root: Path) -> None:
    target = root / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    with duplicate_stream(descriptor) as source, target.open("xb") as output:
        _ = shutil.copyfileobj(source, output)
    if target.stat().st_size != size:
        message = f"source changed while staging: {relative}"
        raise StageError(message)


def _require_allowed(relative: PurePosixPath) -> None:
    if relative.suffix == ".jar" or relative.name == "session.lock":
        message = f"forbidden runtime file entered the stage: {relative}"
        raise StageError(message)


def _instance_names(mode: str) -> tuple[str, ...]:
    if mode == "run-a-worlds":
        return tuple(f"run-a-{role}" for role in RUN_ROLES)
    if mode == "run-b-worlds":
        return tuple(f"run-b-{role}" for role in RUN_ROLES)
    return AUXILIARY_INSTANCES


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("mode", choices=MODES)
    _ = parser.add_argument("project", type=Path)
    _ = parser.add_argument("raw", type=Path)
    _ = parser.add_argument("output", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Stage the requested evidence boundary."""
    options = build_parser().parse_args(argv, namespace=_Namespace())
    count, size = stage(options.mode, options.project, options.raw, options.output)
    print(f"staged {count} files using {size} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
