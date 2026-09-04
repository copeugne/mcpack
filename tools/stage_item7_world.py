"""Stage Item 7 raw evidence with locked, independent world copies."""

from __future__ import annotations

import argparse
import errno
import fcntl
import shutil
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING, Final, final

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
    if mode == "core":
        _reject_forbidden(raw)
        _ = shutil.copytree(raw, output, copy_function=shutil.copy2, symlinks=True)
    else:
        output.mkdir(parents=True)
        names = _instance_names(mode)
        for name in names:
            copy_world_boundary(project / "instances/item7" / name, output / name / "world")
    _reject_forbidden(output)
    files = tuple(path for path in output.rglob("*") if path.is_file())
    return len(files), sum(path.stat().st_size for path in files)


def copy_world_boundary(instance: Path, destination: Path) -> None:
    """Copy the declared stopped-world boundary while holding its record lock."""
    world = instance / "world"
    with _world_lock(world):
        destination.mkdir(parents=True)
        for relative in WORLD_FILES:
            source = world / relative
            if source.is_symlink():
                message = f"stage source contains a symlink: {source}"
                raise StageError(message)
            if source.is_file():
                _ = shutil.copy2(source, destination / relative)
        for relative in WORLD_DIRECTORIES:
            source = world / relative
            if source.is_dir():
                _reject_forbidden(source)
                _ = shutil.copytree(
                    source,
                    destination / relative,
                    copy_function=shutil.copy2,
                    symlinks=True,
                )


@contextmanager
def _world_lock(world: Path) -> Generator[None]:
    lock_path = world / "session.lock"
    if lock_path.is_symlink() or not lock_path.is_file():
        message = f"world session lock is missing or unsafe: {lock_path}"
        raise StageError(message)
    with lock_path.open("r+b") as lock:
        try:
            fcntl.lockf(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as error:
            if error.errno in {errno.EACCES, errno.EAGAIN}:
                message = f"world is active: {world}"
                raise StageError(message) from error
            raise
        try:
            yield
        finally:
            fcntl.lockf(lock, fcntl.LOCK_UN)


def _instance_names(mode: str) -> tuple[str, ...]:
    if mode == "run-a-worlds":
        return tuple(f"run-a-{role}" for role in RUN_ROLES)
    if mode == "run-b-worlds":
        return tuple(f"run-b-{role}" for role in RUN_ROLES)
    return AUXILIARY_INSTANCES


def _reject_forbidden(root: Path) -> None:
    for path in root.rglob("*"):
        if path.is_symlink():
            message = f"stage source contains a symlink: {path}"
            raise StageError(message)
        if path.is_file() and (path.suffix == ".jar" or path.name == "session.lock"):
            message = f"forbidden runtime file entered the stage: {path}"
            raise StageError(message)


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
