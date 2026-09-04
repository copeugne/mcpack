"""Bind stopped Item 7 worlds to decoded chunk and fixed-selection evidence."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import BinaryIO, Literal, NoReturn

from mcpack_evidence.item7_anvil import RegionContext, decode_region
from mcpack_evidence.item7_selections import (
    CONTROL_SELECTIONS,
    PILOT_SELECTIONS,
    RUN_SELECTIONS,
    WorldgenSelection,
)
from mcpack_evidence.item7_world_inventory import (
    Dimension,
    RegionInput,
    WorldManifestError,
    external_rows,
    inventory_external,
    inventory_regions,
    sha256_file,
)

__all__ = ("ManifestMode", "WorldManifest", "WorldManifestError", "build_world_manifest")

type ManifestMode = Literal["control", "pilot", "run"]
type ChunkKey = tuple[Dimension, int, int]


@dataclass(frozen=True, slots=True)
class WorldManifest:
    """One emitted manifest result for programmatic callers."""

    record_count: int
    decoded_sha256: str


@dataclass(slots=True)
class _State:
    observed: list[set[ChunkKey]]
    seen: set[ChunkKey]
    extras: list[ChunkKey]
    external: dict[str, ChunkKey]
    region_counts: dict[str, int]
    external_rows: list[dict[str, object]]
    sha256: str


def _fail(issue: str, subject: object) -> NoReturn:
    raise WorldManifestError(issue, str(subject))


def _geometry(
    selections: tuple[WorldgenSelection, ...],
) -> tuple[dict[ChunkKey, int], tuple[set[ChunkKey], ...]]:
    owners: dict[ChunkKey, int] = {}
    expected: list[set[ChunkKey]] = []
    for index, selection in enumerate(selections):
        center_x, center_z = selection.center_x // 16, selection.center_z // 16
        radius = selection.radius_chunks
        coordinates: set[ChunkKey] = {
            (selection.dimension, x, z)
            for x in range(center_x - radius, center_x + radius + 1)
            for z in range(center_z - radius, center_z + radius + 1)
        }
        if owners.keys() & coordinates:
            _fail("fixed selections overlap", selection.label)
        owners.update((coordinate, index) for coordinate in coordinates)
        expected.append(coordinates)
    return owners, tuple(expected)


def _decode(
    world: Path,
    regions: tuple[RegionInput, ...],
    owners: dict[ChunkKey, int],
    observed: list[set[ChunkKey]],
    stream: BinaryIO,
) -> _State:
    state = _State(observed, set(), [], {}, {}, [], "")
    digest = hashlib.sha256()
    for region in regions:
        count = 0
        context = RegionContext(region.dimension, region.relative, region.min_y, region.height)
        for record in decode_region(region.path, context):
            key: ChunkKey = (region.dimension, record.chunk_x, record.chunk_z)
            if key in state.seen:
                _fail("duplicate decoded chunk", key)
            state.seen.add(key)
            line = (record.model_dump_json() + "\n").encode()
            _ = stream.write(line)
            digest.update(line)
            count += 1
            owner = owners.get(key)
            if owner is None:
                state.extras.append(key)
            elif not record.full or record.status != "minecraft:full":
                _fail("selected chunk is not minecraft:full", key)
            else:
                state.observed[owner].add(key)
            if record.external:
                name = f"c.{record.chunk_x}.{record.chunk_z}.mcc"
                state.external[region.path.with_name(name).relative_to(world).as_posix()] = key
        state.region_counts[region.relative] = count
    state.sha256 = digest.hexdigest()
    return state


def _payload(
    mode: ManifestMode,
    decoded: tuple[str, int],
    selections: tuple[WorldgenSelection, ...],
    regions: tuple[RegionInput, ...],
    state: _State,
) -> dict[str, object]:
    region_fields = (
        "path",
        "dimension",
        "region_x",
        "region_z",
        "size_bytes",
        "sha256",
        "zero_byte_placeholder",
        "decoded_chunk_count",
    )
    selection_fields = (
        "label",
        "dimension",
        "center_block_x",
        "center_block_z",
        "radius_chunks",
        "expected_chunk_count",
        "observed_chunk_count",
    )
    return {
        "schema_version": "item7-world-manifest-v1",
        "mode": mode,
        "regions": [
            dict(
                zip(
                    region_fields,
                    (
                        row.relative,
                        row.dimension,
                        row.region_x,
                        row.region_z,
                        row.size,
                        row.sha256,
                        row.size == 0,
                        state.region_counts[row.relative],
                    ),
                    strict=True,
                )
            )
            for row in regions
        ],
        "external_chunks": state.external_rows,
        "selections": [
            dict(
                zip(
                    selection_fields,
                    (
                        row.label,
                        row.dimension,
                        row.center_x,
                        row.center_z,
                        row.radius_chunks,
                        row.expected_chunk_count,
                        len(state.observed[index]),
                    ),
                    strict=True,
                )
            )
            for index, row in enumerate(selections)
        ],
        "extra_chunks": [
            {"dimension": row[0], "chunk_x": row[1], "chunk_z": row[2]}
            for row in sorted(state.extras)
        ],
        "decoded": dict(
            zip(
                ("path", "size_bytes", "sha256", "record_count"),
                (decoded[0], decoded[1], state.sha256, len(state.seen)),
                strict=True,
            )
        ),
    }


def build_world_manifest(
    world: Path, manifest_path: Path, decoded_path: Path, *, mode: ManifestMode
) -> WorldManifest:
    """Decode a stopped world and atomically emit its strict evidence identities."""
    if world.is_symlink() or not world.is_dir():
        _fail("world is not a real directory", world)
    if manifest_path.parent.resolve() != decoded_path.parent.resolve():
        _fail("outputs do not share one evidence directory", decoded_path)
    if manifest_path.resolve() == decoded_path.resolve():
        _fail("manifest and decoded output are the same path", decoded_path)
    selections = {
        "control": CONTROL_SELECTIONS,
        "pilot": PILOT_SELECTIONS,
        "run": RUN_SELECTIONS,
    }[mode]
    owners, expected = _geometry(selections)
    regions, external = inventory_regions(world), inventory_external(world)
    decoded_path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix=f".{decoded_path.name}.", dir=decoded_path.parent)
    temporary, manifest_temporary = Path(name), None
    try:
        with os.fdopen(descriptor, "wb") as stream:
            state = _decode(world, regions, owners, [set() for _ in selections], stream)
        for index, coordinates in enumerate(expected):
            missing = sorted(coordinates - state.observed[index])
            if missing:
                issue = f"missing selected chunk for {selections[index].label}"
                _fail(issue, missing[0])
        for region in regions:
            if region.size != region.path.stat().st_size or region.sha256 != sha256_file(
                region.path
            ):
                _fail("region changed while decoding", region.relative)
        state.external_rows = external_rows(external, state.external)
        decoded = (decoded_path.name, temporary.stat().st_size)
        payload = _payload(mode, decoded, selections, regions, state)
        descriptor, name = tempfile.mkstemp(
            prefix=f".{manifest_path.name}.", dir=manifest_path.parent
        )
        manifest_temporary = Path(name)
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            _ = stream.write(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        _ = temporary.replace(decoded_path)
        _ = manifest_temporary.replace(manifest_path)
    except Exception:
        temporary.unlink(missing_ok=True)
        if manifest_temporary is not None:
            manifest_temporary.unlink(missing_ok=True)
        raise
    return WorldManifest(len(state.seen), state.sha256)
