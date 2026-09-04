"""Create visible, self-identifying SVG frames for Item 7 evidence."""

from __future__ import annotations

import html
import json
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from mcpack_evidence.item7_render_input import RenderMetadata

_BACKGROUND = "#101820"
_FOREGROUND = "#f4f7f9"
_MUTED = "#b7c3ca"
_GRADIENT = (
    '<defs><linearGradient id="elevation-gradient">'
    '<stop offset="0" stop-color="#607d46"/>'
    '<stop offset="1" stop-color="#d6d39a"/></linearGradient></defs>'
)


def topdown_svg(
    metadata: RenderMetadata,
    bounds: tuple[int, int, int, int],
    layers: str,
    boxes: str,
) -> str:
    """Frame one derived terrain map with visible provenance and legend."""
    minimum_x, minimum_z, width, height = bounds
    canvas_width = max(width, 720)
    header, footer = 100, 134
    offset_x = (canvas_width - width) // 2
    description = (
        "<desc>Derived elevation and placement view. Fill color encodes saved WORLD_SURFACE "
        "elevation, except blue cells where OCEAN_FLOOR is below WORLD_SURFACE. Biome IDs "
        "are metadata only and do not drive fill color. Red outlines are saved structure "
        "bounds.</desc>"
    )
    legend_y = header + height + 34
    content = "".join(
        (
            description,
            _header(metadata, "Top-down derived elevation and placement view"),
            "".join(
                (
                    f'<defs><clipPath id="map-boundary"><rect width="{width}" height="{height}"/>',
                    "</clipPath></defs>",
                )
            ),
            f'<g clip-path="url(#map-boundary)" transform="translate({offset_x} {header})">',
            f'<g class="terrain">{layers}</g><g class="structures">{boxes}</g></g>',
            "".join(
                (
                    f'<text class="orientation" x="{canvas_width - 24}" y="{header + 24}" ',
                    'text-anchor="end">North (-Z) ↑</text>',
                )
            ),
            f'<g class="legend" transform="translate(24 {legend_y})">',
            '<rect class="elevation-key" x="0" y="0" width="96" height="16"/>',
            '<text x="104" y="13">Elevation color</text>',
            '<rect class="water-key" x="258" y="0" width="20" height="16"/>',
            '<text x="286" y="13">Water candidate</text>',
            '<rect class="structure-key" x="466" y="0" width="20" height="16"/>',
            '<text x="494" y="13">Structure bounds</text>',
            "".join(
                (
                    f'<text class="muted" x="0" y="42">Block extent: X {minimum_x} to ',
                    f"{minimum_x + width - 1}; Z {minimum_z} to ",
                    f"{minimum_z + height - 1}</text>",
                )
            ),
            '<text class="muted" x="0" y="66">Resolution: 1 map cell = 1 block.</text>',
            '<text class="muted" x="0" y="90">Biome IDs are metadata, not a color encoding.</text>',
            "</g>",
        )
    )
    return _document(
        metadata,
        canvas_width,
        header + height + footer,
        "top-down derived elevation and placement view",
        content,
    )


def section_svg(
    metadata: RenderMetadata,
    axis: Literal["x", "z"],
    points: tuple[tuple[int, int], ...],
    origin: int,
    slice_coordinate: int,
) -> str:
    """Frame one heightmap profile with visible scale, units, and limitations."""
    surfaces = tuple(surface for _, surface in points)
    minimum_y, maximum_y = min(surfaces), max(surfaces)
    plot_width, plot_height = 900, 360
    left, top = 86, 116
    canvas_width, canvas_height = left + plot_width + 38, top + plot_height + 118
    horizontal = "X" if axis == "x" else "Z"
    slice_axis = "Z" if axis == "x" else "X"
    last_coordinate = max(coordinate for coordinate, _ in points)
    x_scale = plot_width / max(last_coordinate, 1)
    y_span = max(maximum_y - minimum_y, 1)

    def profile_point(coordinate: int, surface: int) -> str:
        x_value = left + coordinate * x_scale
        y_value = top + (maximum_y - surface) * plot_height / y_span
        return f"{x_value:.2f},{y_value:.2f}"

    profile = " ".join(profile_point(coordinate, surface) for coordinate, surface in points)
    flat_note = (
        "".join(
            (
                f'<text class="muted" x="{left + 12}" y="{top + 28}">',
                f"Flat stored heightmap profile at Y={minimum_y}.</text>",
            )
        )
        if minimum_y == maximum_y
        else ""
    )
    content = "".join(
        (
            "".join(
                (
                    f"<desc>Heightmap-derived surface profile along block {horizontal}. ",
                    "No block-column samples are present.</desc>",
                )
            ),
            _header(metadata, f"Orthogonal elevation cross-section along block {horizontal}"),
            "".join(
                (
                    f'<rect class="plot" x="{left}" y="{top}" ',
                    f'width="{plot_width}" height="{plot_height}"/>',
                )
            ),
            "".join(
                (
                    f'<line class="axis" x1="{left}" y1="{top + plot_height}" ',
                    f'x2="{left + plot_width}" y2="{top + plot_height}"/>',
                )
            ),
            f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{top + plot_height}"/>',
            f'<polyline class="surface-profile" points="{profile}"/>',
            flat_note,
            f'<text x="{left}" y="{top + plot_height + 24}">{origin}</text>',
            "".join(
                (
                    f'<text x="{left + plot_width}" y="{top + plot_height + 24}" ',
                    'text-anchor="end">',
                    f"{origin + last_coordinate}</text>",
                )
            ),
            f'<text x="{left - 12}" y="{top + plot_height}" text-anchor="end">{minimum_y}</text>',
            f'<text x="{left - 12}" y="{top + 12}" text-anchor="end">{maximum_y}</text>',
            "".join(
                (
                    f'<text class="axis-label" x="{left + plot_width / 2}" ',
                    f'y="{canvas_height - 58}" ',
                    f'text-anchor="middle">Horizontal coordinate (block {horizontal})</text>',
                )
            ),
            "".join(
                (
                    f'<text class="axis-label" x="22" y="{top + plot_height / 2}" ',
                    f'text-anchor="middle" transform="rotate(-90 22 {top + plot_height / 2})">',
                    "Elevation (blocks)</text>",
                )
            ),
            "".join(
                (
                    f'<text class="muted" x="{left}" y="{canvas_height - 28}">Slice at block ',
                    f"{slice_axis}={slice_coordinate}. Heightmap-derived only; ",
                    "no block-column samples.</text>",
                )
            ),
        )
    )
    document = _document(metadata, canvas_width, canvas_height, "elevation cross-section", content)
    return document.replace("<svg ", f'<svg data-axis="{axis}" data-block-accurate="false" ', 1)


def _visible_identity(metadata: RenderMetadata) -> str:
    return (
        f"Run: {metadata.run_id} | Seed role: {metadata.seed_role} | Seed: {metadata.seed} | "
        f"Selection: {metadata.selection} | Dimension: {metadata.dimension}"
    )


def _header(metadata: RenderMetadata, subtitle: str) -> str:
    return "".join(
        (
            "".join(
                (
                    f'<text class="title" x="24" y="26">Run: {html.escape(metadata.run_id)} | ',
                    f"Seed role: {html.escape(metadata.seed_role)} | ",
                    f"Seed: {html.escape(metadata.seed)}</text>",
                )
            ),
            "".join(
                (
                    '<text class="title" x="24" y="50">Selection: ',
                    f"{html.escape(metadata.selection)} | ",
                    f"Dimension: {html.escape(metadata.dimension)}</text>",
                )
            ),
            f'<text class="subtitle" x="24" y="76">{html.escape(subtitle)}</text>',
        )
    )


def _document(metadata: RenderMetadata, width: int, height: int, label: str, content: str) -> str:
    identity = _visible_identity(metadata)
    hashes = html.escape(json.dumps(dict(sorted(metadata.region_hashes.items())), sort_keys=True))
    attributes = " ".join(
        (
            'xmlns="http://www.w3.org/2000/svg"',
            'role="img"',
            f'aria-label="{html.escape(label)}"',
            f'data-run-id="{html.escape(metadata.run_id)}"',
            f'data-seed-role="{html.escape(metadata.seed_role)}"',
            f'data-seed="{html.escape(metadata.seed)}"',
            f'data-selection="{html.escape(metadata.selection)}"',
            f'data-dimension="{html.escape(metadata.dimension)}"',
            f'data-input-region-hashes="{hashes}"',
            f'viewBox="0 0 {width} {height}"',
        )
    )
    style = "".join(
        (
            f".background{{fill:{_BACKGROUND}}}.plot{{fill:#17242d;stroke:#61737f}}",
            f"text{{fill:{_FOREGROUND};font-family:system-ui,sans-serif;font-size:14px}}",
            ".title{font-size:16px;font-weight:700}.subtitle,.axis-label{font-size:15px}",
            f".muted{{fill:{_MUTED}}}.orientation{{font-weight:700}}",
            ".structure{fill:none;stroke:#ff003c;stroke-width:1}.surface-profile{fill:none;stroke:#ffffff;stroke-width:2}",
            ".axis{stroke:#9fb0ba;stroke-width:1}.water-key{fill:#1c80d8}",
            ".structure-key{fill:none;stroke:#ff003c;stroke-width:2}",
            ".elevation-key{fill:url(#elevation-gradient)}",
        )
    )
    return "".join(
        (
            '<?xml version="1.0" encoding="UTF-8"?>\n',
            f"<svg {attributes}><title>{html.escape(identity)}</title>",
            _GRADIENT,
            f"<style>{style}</style>",
            f'<rect class="background" x="0" y="0" width="{width}" height="{height}"/>',
            f"{content}</svg>\n",
        )
    )
