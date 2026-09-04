"""Exact expected contents for the three Item 7 world archives."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path  # noqa: TC003
from typing import TYPE_CHECKING, ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item7_archive import ArchiveManifest, FileIdentity
from mcpack_evidence.item7_archive_io import open_tree, sha256_descriptor
from mcpack_evidence.item7_completion_io import fail, identity, strict_model, write_atomic

if TYPE_CHECKING:
    from mcpack_evidence.item7_completion_models import ArtifactIdentity

_WORLD_ARCHIVE_COUNT: Final = 3


class _Strict(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)


class WorldArchiveContents(_Strict):
    """One world archive's complete expected file inventory."""

    archive_name: str
    files: tuple[FileIdentity, ...]


class WorldArchiveInventory(_Strict):
    """Exact expected inventories for all non-core Item 7 archives."""

    schema_version: Literal["item7-world-archive-inventory-v1"]
    archives: tuple[WorldArchiveContents, ...]


@dataclass(frozen=True, slots=True)
class WorldArchiveSource:
    """One descriptor-safe source tree and its intended archive name."""

    root: Path
    archive_name: str


def build_world_archive_inventory(
    sources: tuple[WorldArchiveSource, WorldArchiveSource, WorldArchiveSource],
) -> WorldArchiveInventory:
    """Inventory three isolated world stages without trusting archive manifests."""
    archives: list[WorldArchiveContents] = []
    for source in sources:
        with open_tree(source.root) as opened:
            files = tuple(
                FileIdentity(
                    relative_path=row.relative_path,
                    size_bytes=row.size_bytes,
                    sha256=sha256_descriptor(row.descriptor),
                )
                for row in opened
            )
        archives.append(WorldArchiveContents(archive_name=source.archive_name, files=files))
    return WorldArchiveInventory(
        schema_version="item7-world-archive-inventory-v1",
        archives=tuple(archives),
    )


def write_world_archive_inventory(
    output: Path,
    sources: tuple[WorldArchiveSource, WorldArchiveSource, WorldArchiveSource],
) -> WorldArchiveInventory:
    """Build and atomically write the expected world archive inventory."""
    report = build_world_archive_inventory(sources)
    write_atomic(output, report)
    return report


def validate_world_archive_inventory(
    path: Path, manifests: tuple[ArchiveManifest, ...]
) -> ArtifactIdentity:
    """Require every world archive byte identity exactly once."""
    report = strict_model(path, WorldArchiveInventory)
    expected_names = tuple(row.archive_name for row in report.archives)
    if (
        len(report.archives) != _WORLD_ARCHIVE_COUNT
        or len(set(expected_names)) != _WORLD_ARCHIVE_COUNT
        or any(not row.files for row in report.archives)
    ):
        fail("world archive inventory", path)
    by_name = {row.archive_name: row for row in manifests}
    if len(by_name) != len(manifests) or set(expected_names) - by_name.keys():
        fail("world archive inventory", path)
    unexplained = set(by_name) - set(expected_names)
    if len(unexplained) != 1 or "-core-" not in unexplained.pop():
        fail("world archive inventory", path)
    for expected in report.archives:
        if by_name[expected.archive_name].files != expected.files:
            fail("world archive inventory", expected.archive_name)
    return identity(path, "world-archive-inventory.json")
