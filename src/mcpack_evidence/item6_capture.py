"""Item 6 configuration capture boundary."""

from __future__ import annotations

import shutil
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


def capture(instance: Path, output: Path) -> None:
    """Copy configuration-bearing paths without altering the source instance."""
    if output.exists():
        message = f"output already exists: {output}"
        raise FileExistsError(message)
    output.mkdir(parents=True)
    sources = {
        instance / "config": output / "config",
        instance / "defaultconfigs": output / "defaultconfigs",
        instance / "world" / "serverconfig": output / "world-serverconfig",
    }
    for source, target in sources.items():
        if source.is_dir():
            _ = shutil.copytree(source, target)
    _ = shutil.copy2(instance / "server.properties", output / "server.properties")
