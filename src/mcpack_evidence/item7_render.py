"""Deterministic SVG elevation and structure-placement views for Item 7."""

from __future__ import annotations

import html
import json
import shutil
import tempfile
from pathlib import Path
from typing import TYPE_CHECKING, Final, Literal

from mcpack_evidence.item7_render_input import (
    RenderChunk,
    RenderInput,
    RenderInputError,
    RenderMetadata,
    parse_input,
    sha256,
)
from mcpack_evidence.item7_render_svg import section_svg, topdown_svg

RENDERER_VERSION: Final = "item7-offline-render-v1"
_BIOME_INDEX_MESSAGE: Final = "decoded biome section has an invalid palette index"

if TYPE_CHECKING:
    from collections.abc import Iterable

__all__ = ("RenderInputError", "RenderMetadata", "render_jsonl")


def render_jsonl(
    chunks_path: Path,
    output: Path,
    metadata: RenderMetadata,
    *,
    expected_chunks_sha256: str | None = None,
) -> None:
    """Render strict decoded JSONL into an atomic, hash-listed offline gallery."""
    render_input = parse_input(chunks_path, metadata, expected_chunks_sha256)
    if output.exists() or output.is_symlink():
        message = f"render output already exists: {output}"
        raise FileExistsError(message)
    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{output.name}.render-", dir=output.parent))
    try:
        artifacts = _render_artifacts(render_input)
        for name, content in artifacts.items():
            _ = (staging / name).write_text(content, encoding="utf-8")
        hashes = {name: sha256(staging / name) for name in sorted(artifacts)}
        manifest = {
            "schema_version": RENDERER_VERSION,
            "metadata": _metadata_document(render_input),
            "artifact_hashes": hashes,
        }
        _ = (staging / "manifest.json").write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        _ = staging.replace(output)
    finally:
        if staging.exists():
            shutil.rmtree(staging)


def _render_artifacts(render_input: RenderInput) -> dict[str, str]:
    metadata = render_input.metadata
    return {
        "cross-section-x.svg": _render_section(metadata, render_input.chunks, "x"),
        "cross-section-z.svg": _render_section(metadata, render_input.chunks, "z"),
        "index.html": _render_gallery(metadata, render_input.chunks_sha256),
        "topdown.svg": _render_topdown(metadata, render_input.chunks),
    }


def _render_topdown(metadata: RenderMetadata, chunks: tuple[RenderChunk, ...]) -> str:
    minimum_x, minimum_z, width, height = _bounds(chunks)
    paths: dict[tuple[str, str, str], list[str]] = {}
    for chunk in chunks:
        for index, surface in enumerate(chunk.world_surface):
            local_x, local_z = index % 16, index // 16
            water_candidate = chunk.ocean_floor[index] < surface
            colour = _water_colour(surface) if water_candidate else _elevation_colour(surface)
            key = (
                "water-candidate" if water_candidate else "land",
                colour,
                _biome(chunk, index),
            )
            x = chunk.chunk_x * 16 + local_x - minimum_x
            z = chunk.chunk_z * 16 + local_z - minimum_z
            paths.setdefault(key, []).append(f"M{x} {z}h1v1h-1z")
    layers = "".join(
        _layer(kind, colour, biome, commands)
        for (kind, colour, biome), commands in sorted(paths.items())
    )
    boxes = "".join(_boxes(chunk, minimum_x, minimum_z) for chunk in chunks)
    return topdown_svg(metadata, (minimum_x, minimum_z, width, height), layers, boxes)


def _render_section(
    metadata: RenderMetadata,
    chunks: tuple[RenderChunk, ...],
    axis: Literal["x", "z"],
) -> str:
    minimum_x, minimum_z, width, height = _bounds(chunks)
    points = tuple(_section_points(chunks, axis))
    origin = minimum_x if axis == "x" else minimum_z
    slice_coordinate = minimum_z + height // 2 if axis == "x" else minimum_x + width // 2
    return section_svg(metadata, axis, points, origin, slice_coordinate)


def _bounds(chunks: tuple[RenderChunk, ...]) -> tuple[int, int, int, int]:
    chunk_xs, chunk_zs = [chunk.chunk_x for chunk in chunks], [chunk.chunk_z for chunk in chunks]
    minimum_x, minimum_z = min(chunk_xs) * 16, min(chunk_zs) * 16
    width, height = (
        (max(chunk_xs) - min(chunk_xs) + 1) * 16,
        (max(chunk_zs) - min(chunk_zs) + 1) * 16,
    )
    return minimum_x, minimum_z, width, height


def _section_points(
    chunks: tuple[RenderChunk, ...], axis: Literal["x", "z"]
) -> Iterable[tuple[int, int]]:
    minimum_x, minimum_z, width, height = _bounds(chunks)
    cross = minimum_z + height // 2 if axis == "x" else minimum_x + width // 2
    points: list[tuple[int, int]] = []
    for chunk in chunks:
        for index, surface in enumerate(chunk.world_surface):
            local_x, local_z = index % 16, index // 16
            world_x, world_z = chunk.chunk_x * 16 + local_x, chunk.chunk_z * 16 + local_z
            selected = world_z == cross if axis == "x" else world_x == cross
            if selected:
                coordinate = world_x - minimum_x if axis == "x" else world_z - minimum_z
                points.append((coordinate, surface))
    return tuple(sorted(points))


def _biome(chunk: RenderChunk, index: int) -> str:
    surface = chunk.world_surface[index] - 1
    section_y = surface // 16
    section = next((row for row in chunk.biome_sections if row.section_y == section_y), None)
    if section is None:
        return "unknown"
    local_x, local_z, local_y = index % 16, index // 16, surface % 16
    palette_index = (local_y // 4) * 16 + (local_z // 4) * 4 + local_x // 4
    index_value = section.indices[palette_index]
    if index_value < 0 or index_value >= len(section.palette):
        raise RenderInputError(_BIOME_INDEX_MESSAGE)
    return section.palette[index_value]


def _layer(kind: str, colour: str, biome: str, commands: list[str]) -> str:
    path = "".join(commands)
    return "".join(
        (
            f'<g class="{kind}" data-biome="{html.escape(biome)}" fill="{colour}">',
            f'<path d="{path}"/></g>',
        )
    )


def _boxes(chunk: RenderChunk, minimum_x: int, minimum_z: int) -> str:
    return "".join(
        _box(start.structure_id, box.bounds, minimum_x, minimum_z)
        for start in chunk.structures
        for box in start.boxes
    )


def _box(
    identifier: str, bounds: tuple[int, int, int, int, int, int], minimum_x: int, minimum_z: int
) -> str:
    x, z = bounds[0] - minimum_x, bounds[2] - minimum_z
    width, height = bounds[3] - bounds[0] + 1, bounds[5] - bounds[2] + 1
    provider = identifier.partition(":")[0]
    return "".join(
        (
            f'<rect class="structure" data-provider="{html.escape(provider)}" ',
            f'data-id="{html.escape(identifier)}" x="{x}" ',
            f'y="{z}" width="{width}" height="{height}"/>',
        )
    )


def _elevation_colour(surface: int) -> str:
    red = max(24, min(220, 96 + surface // 3))
    green = max(32, min(220, 118 + surface // 4))
    blue = max(24, min(180, 62 + surface // 8))
    return f"#{red:02x}{green:02x}{blue:02x}"


def _water_colour(surface: int) -> str:
    depth_tone = max(48, min(184, 192 - surface // 2))
    return f"#1c{depth_tone:02x}d8"


def _metadata_document(render_input: RenderInput) -> dict[str, str | dict[str, str]]:
    return {
        "run_id": render_input.metadata.run_id,
        "seed_role": render_input.metadata.seed_role,
        "seed": render_input.metadata.seed,
        "dimension": render_input.metadata.dimension,
        "selection": render_input.metadata.selection,
        "input_region_hashes": dict(sorted(render_input.metadata.region_hashes.items())),
        "chunks_sha256": render_input.chunks_sha256,
    }


def _render_gallery(metadata: RenderMetadata, chunks_sha256: str) -> str:
    title = (
        f"Item 7 inspection: {metadata.run_id}, seed role {metadata.seed_role}, seed "
        f"{metadata.seed}, selection {metadata.selection}, {metadata.dimension}"
    )
    rows = "".join(
        f'<li><a href="{name}">{label}</a></li>'
        for name, label in (
            ("topdown.svg", "Top-down elevation and placement"),
            ("cross-section-x.svg", "X elevation cross-section"),
            ("cross-section-z.svg", "Z elevation cross-section"),
        )
    )
    limitation = (
        "<p>These are derived elevation and placement views. "
        "No block-accurate rendering claim is made.</p>"
    )
    return "".join(
        (
            '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>',
            f"{html.escape(title)}</title></head><body><h1>{html.escape(title)}</h1>",
            "".join(
                (
                    f"<p>Seed role: {html.escape(metadata.seed_role)}. Selection: ",
                    f"{html.escape(metadata.selection)}.</p>",
                )
            ),
            f"<p>Decoded JSONL SHA-256: {chunks_sha256}</p><ul>{rows}</ul>",
            limitation,
            "</body></html>\n",
        )
    )
