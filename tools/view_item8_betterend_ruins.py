"""Write fixed BetterEnd ruin voxel diagrams for canonical design inspection."""

from __future__ import annotations

import argparse
import gzip
import hashlib
from html import escape
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item7_nbt import decode_compound_nbt
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def diagram(raw: bytes, title: str, origin_x: int, origin_y: int) -> str:
    """Project occupied block cells; preserve material names in SVG tooltips."""
    root = decode_compound_nbt(gzip.decompress(raw))
    palette = cast("list[dict[str, JsonValue]]", root["palette"])
    blocks = cast("list[dict[str, JsonValue]]", root["blocks"])
    result = [f'<text x="{origin_x}" y="{origin_y}" font-size="14">{escape(title)}</text>']
    sx, sy, sz = cast("list[int]", root["size"])
    step = min(12, 240 / (sx + sz), 180 / (sy + (sx + sz) / 2))
    cells: list[tuple[int, int, int, str]] = []
    for block in blocks:
        x, y, z = cast("list[int]", block["pos"])
        name = str(palette[cast("int", block["state"])]["Name"])
        if name not in {"minecraft:air", "minecraft:cave_air", "minecraft:structure_void"}:
            cells.append((x, y, z, name))
    for x, y, z, name in sorted(cells, key=lambda cell: (sum(cell[:3]), cell[1])):
        px = origin_x + 110 + (x - z) * step
        py = origin_y + 180 + (x + z) * step / 2 - y * step
        # Green is a visual hint only, not a membership classifier.
        plant = any(word in name for word in ("leaves", "moss", "vine", "grass", "flower"))
        colors = ("#81a98b", "#486c51", "#608169") if plant else (
            "#aac5e4", "#4e7099", "#7595ba")
        faces = (
            ((px, py - step), (px + step, py - step / 2), (px, py), (px - step, py - step / 2)),
            ((px - step, py - step / 2), (px, py), (px, py + step), (px - step, py + step / 2)),
            ((px, py), (px + step, py - step / 2), (px + step, py + step / 2), (px, py + step)),
        )
        for color, face in zip(colors, faces, strict=True):
            points = " ".join(f"{a},{b}" for a, b in face)
            result.append("".join((f'<polygon points="{points}" fill="{color}" stroke="#34495e" ',
                          f'stroke-width="0.2"><title>{escape(name)}',
                          f" ({x},{y},{z})</title></polygon>")))
    return "\n".join(result)


def main() -> None:
    """Render only the six known biome ruin sets from the frozen archive."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--output", type=Path, required=True)
    output = cast("Path", parser.parse_args().output)
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "BetterEnd-21.0.31.jar")
    if hashlib.sha256(source.path.read_bytes()).hexdigest() != source.sha256:
        message = "BetterEnd archive identity mismatch"
        raise ValueError(message)
    output.mkdir(parents=True, exist_ok=False)
    with ZipFile(source.path) as archive:
        for biome, count in {
            "blossoming_spires": 8, "chorus_forest": 8, "foggy_mushroomland": 3,
            "lantern_woods": 2, "shadow_forest": 8, "umbrella_jungle": 6,
        }.items():
            pieces: list[str] = []
            for index in range(count):
                name = f"ruins_{index + 1}"
                raw = archive.read(f"data/betterend/structure/biome/{biome}/{name}.nbt")
                pieces.append(diagram(raw, name, 20 + index % 2 * 300, 35 + index // 2 * 300))
            height = ((count + 1) // 2) * 300
            svg = "".join((
                f'<svg xmlns="http://www.w3.org/2000/svg" width="620" height="{height}">',
                   '<rect width="100%" height="100%" fill="white"/>',
                   "\n".join(pieces), "</svg>"))
            _ = (output / f"{biome}.svg").write_text(svg + "\n")


if __name__ == "__main__":
    main()
