"""Inventory stopped-world Anvil inputs without following filesystem links."""

from __future__ import annotations

import hashlib
import re
import stat
from dataclasses import dataclass
from pathlib import Path
from typing import Final, Literal, NoReturn, final, override

type Dimension = Literal["minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"]
type ChunkKey = tuple[Dimension, int, int]
type ExternalInput = tuple[Path, int, str]

_REGION_NAME: Final = re.compile(r"^r\.(-?\d+)\.(-?\d+)\.mca$")
_DIMENSIONS: Final[tuple[tuple[Path, Dimension, int, int], ...]] = (
    (Path("region"), "minecraft:overworld", -64, 384),
    (Path("DIM-1/region"), "minecraft:the_nether", 0, 256),
    (Path("DIM1/region"), "minecraft:the_end", 0, 256),
)


@final
@dataclass(frozen=True, slots=True)
class WorldManifestError(Exception):
    """A stopped-world inventory or fixed-selection invariant failed."""

    issue: str
    subject: str

    @override
    def __str__(self) -> str:
        return f"{self.issue}: {self.subject}"


@dataclass(frozen=True, slots=True)
class RegionInput:
    """One hash-bound region file plus its decoder geometry."""

    path: Path
    relative: str
    dimension: Dimension
    region_x: int
    region_z: int
    min_y: int
    height: int
    size: int
    sha256: str


def _fail(issue: str, subject: object) -> NoReturn:
    raise WorldManifestError(issue, str(subject))


def sha256_file(path: Path) -> str:
    """Return the streaming SHA-256 identity of one evidence file."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def _files(directory: Path, suffix: str) -> tuple[Path, ...]:
    rows: list[Path] = []
    for path in directory.rglob("*"):
        if path.is_symlink():
            _fail("symlink in region evidence tree", path)
        if not path.name.endswith(suffix):
            continue
        if not stat.S_ISREG(path.stat(follow_symlinks=False).st_mode):
            _fail("evidence input is not a regular non-symlink file", path)
        rows.append(path)
    return tuple(sorted(rows))


def inventory_regions(world: Path) -> tuple[RegionInput, ...]:
    """Inventory every supported-dimension MCA file, including empty placeholders."""
    rows: list[RegionInput] = []
    coordinates: set[ChunkKey] = set()
    for relative_dir, dimension, min_y, height in _DIMENSIONS:
        directory = world / relative_dir
        if not directory.exists():
            continue
        if directory.is_symlink() or not directory.is_dir():
            _fail("region path is not a real directory", directory)
        for path in _files(directory, ".mca"):
            match = _REGION_NAME.fullmatch(path.name)
            if match is None:
                _fail("invalid region filename", path)
            key: ChunkKey = (dimension, int(match[1]), int(match[2]))
            if key in coordinates:
                _fail("duplicate region coordinates", key)
            coordinates.add(key)
            rows.append(
                RegionInput(
                    path,
                    path.relative_to(world).as_posix(),
                    dimension,
                    key[1],
                    key[2],
                    min_y,
                    height,
                    path.stat().st_size,
                    sha256_file(path),
                )
            )
    return tuple(sorted(rows, key=lambda row: row.relative))


def inventory_external(world: Path) -> dict[str, ExternalInput]:
    """Inventory every MCC file before decoding can consume it."""
    rows: dict[str, ExternalInput] = {}
    for relative_dir, _, _, _ in _DIMENSIONS:
        directory = world / relative_dir
        if directory.is_dir() and not directory.is_symlink():
            for path in _files(directory, ".mcc"):
                rows[path.relative_to(world).as_posix()] = (
                    path,
                    path.stat().st_size,
                    sha256_file(path),
                )
    return rows


def external_rows(
    inputs: dict[str, ExternalInput], expected: dict[str, ChunkKey]
) -> list[dict[str, object]]:
    """Bind referenced external chunks to the stable pre-decode inventory."""
    if inputs.keys() != expected.keys():
        _fail(
            "external inventory disagrees with Anvil slots", sorted(inputs.keys() ^ expected.keys())
        )
    rows: list[dict[str, object]] = []
    for name, (path, size, sha256) in sorted(inputs.items()):
        if path.stat().st_size != size or sha256_file(path) != sha256:
            _fail("external chunk changed while decoding", name)
        dimension, chunk_x, chunk_z = expected[name]
        rows.append(
            dict(
                zip(
                    ("path", "dimension", "chunk_x", "chunk_z", "size_bytes", "sha256"),
                    (name, dimension, chunk_x, chunk_z, size, sha256),
                    strict=True,
                )
            )
        )
    return rows
