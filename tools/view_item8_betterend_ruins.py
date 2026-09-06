"""Write fixed template voxel diagrams for canonical design inspection."""

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


def diagram(raw: bytes, title: str, origin_x: int, origin_y: int, *, exposed: bool = False) -> str:
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
    occupied: set[tuple[int, int, int]] = {(x, y, z) for x, y, z, _ in cells} if exposed else set()
    for x, y, z, name in sorted(cells, key=lambda cell: (sum(cell[:3]), cell[1])):
        if exposed and all(p in occupied for p in ((x + 1, y, z), (x, y + 1, z), (x, y, z + 1))):
            continue
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
    """Render fixed BetterEnd or Soaring sets from their frozen archive."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--output", type=Path, required=True)
    _ = parser.add_argument("--soaring", action="store_true")
    args = parser.parse_args()
    output = cast("Path", args.output)
    soaring = cast("bool", args.soaring)
    archive_name = "MoogsSoaringStructures-1.21-2.1.2.jar" if soaring else "BetterEnd-21.0.31.jar"
    source = next(s for s in retained_sources(Path.cwd()) if s.name == archive_name)
    if hashlib.sha256(source.path.read_bytes()).hexdigest() != source.sha256:
        message = f"Archive identity mismatch: {archive_name}"
        raise ValueError(message)
    output.mkdir(parents=True, exist_ok=False)
    with ZipFile(source.path) as archive:
        sheets = {
            biome: [f"biome/{biome}/ruins_{i + 1}" for i in range(count)]
            for biome, count in {
                "blossoming_spires": 8, "chorus_forest": 8, "foggy_mushroomland": 3,
                "lantern_woods": 2, "shadow_forest": 8, "umbrella_jungle": 6,
            }.items()
        }
        if soaring:
            sheets = {
                "houses": ["calcite_house", "diorite_house", "small_deepslate_house",
                           "small_oak_house", "spruce_huts", "white_house"],
                "towers": ["castle_ruin", "castle_tower", "large_tower", "small_tower"],
                "landscapes": ["frozen_pond", "muddy_water_hole", "small_pond", "jungle",
                               "leaf_hollow", "mangrove"],
                "islands": ["mushroom", "palm_island", "red_sand", "taiga", "volcano"],
                "monuments": ["desert_pyramid", "desert_pyramid_side", "desert_pyramid_top",
                              "desert_well", "nether_portal"],
            }
        namespace = "mss" if soaring else "betterend"
        for biome, names in sheets.items():
            count = len(names)
            pieces: list[str] = []
            for index, name in enumerate(names):
                raw = archive.read(f"data/{namespace}/structure/{name}.nbt")
                title = name if soaring else name.rsplit("/", 1)[1]
                pieces.append(diagram(raw, title, 20 + index % 2 * 300,
                                      35 + index // 2 * 300, exposed=soaring))
            height = ((count + 1) // 2) * 300
            svg = "".join((
                f'<svg xmlns="http://www.w3.org/2000/svg" width="620" height="{height}">',
                   '<rect width="100%" height="100%" fill="white"/>',
                   "\n".join(pieces), "</svg>"))
            _ = (output / f"{biome}.svg").write_text(svg + "\n")


if __name__ == "__main__":
    main()
