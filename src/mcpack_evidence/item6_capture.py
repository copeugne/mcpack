"""Item 6 configuration capture boundary."""

from __future__ import annotations

import shutil
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from pathlib import Path


_DIRECTORIES: Final = ("config", "defaultconfigs", "world", "world/serverconfig")


class CaptureValidationError(ValueError):
    """Raised when an Item 6 capture source violates its filesystem contract."""


def capture(instance: Path, output: Path) -> None:
    """Copy configuration-bearing paths without altering the source instance."""
    if output.exists():
        message = f"output already exists: {output}"
        raise FileExistsError(message)
    _require_directory(instance, "instance")
    sources = tuple(instance / relative for relative in _DIRECTORIES)
    for source, relative in zip(sources, _DIRECTORIES, strict=True):
        _require_directory(source, relative)
    properties = instance / "server.properties"
    _require_regular_file(properties, "server.properties")

    output.mkdir(parents=True)
    for source, target in (
        (instance / "config", output / "config"),
        (instance / "defaultconfigs", output / "defaultconfigs"),
        (instance / "world" / "serverconfig", output / "world-serverconfig"),
    ):
        _ = shutil.copytree(source, target)
    _ = shutil.copy2(properties, output / "server.properties")


def _require_directory(path: Path, name: str) -> None:
    """Require one real, non-symlink source directory."""
    if path.is_symlink() or not path.is_dir():
        message = f"required directory must be a real non-symlink directory: {name}"
        raise CaptureValidationError(message)


def _require_regular_file(path: Path, name: str) -> None:
    """Require one real, non-symlink source file."""
    if path.is_symlink() or not path.is_file():
        message = f"required regular non-symlink file is invalid: {name}"
        raise CaptureValidationError(message)
