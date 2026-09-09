"""Render exact saved block slices for manual small-dungeon topology inspection."""

# pyright: standard
# ruff: noqa: D103, EM101, TRY003, INP001, E501
from __future__ import annotations

import argparse
import gzip
import hashlib
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def state_at(case, x, y, z):  # noqa: ANN001, ANN201
    b = case["bounds"]
    if not (b[0] <= x <= b[3] and b[1] <= y <= b[4] and b[2] <= z <= b[5]):
        raise ValueError("coordinate outside retained voxel extraction")
    index = ((y - b[1]) * (b[5] - b[2] + 1) + z - b[2]) * (b[3] - b[0] + 1) + x - b[0]
    return case["palette"][case["blocks_yzx"][index]]


def appearance(name):  # noqa: ANN001, ANN201, PLR0911
    if name in {"minecraft:air", "minecraft:cave_air"}:
        return "#ffffff", ""
    if name == "minecraft:spawner":
        return "#dc4040", "S"
    if name == "minecraft:chest":
        return "#f2b644", "C"
    if name == "minecraft:barrel":
        return "#da9031", "B"
    if name == "minecraft:water":
        return "#3da4dc", "W"
    if name.endswith(("vein", "lichen")):
        return "#a8d8b0", "v"
    if name == "minecraft:chain":
        return "#ad99bb", "|"
    if name.endswith(("skull", "banner", "furnace", "jukebox", "crafting_table")):
        return "#b792c2", "P"
    if name.endswith(("stairs", "slab")):
        return "#6d8ca0", "h"
    return "#89908d", ""


def render_slices(source, output, *, layers: list[int] | None = None) -> None:  # noqa: ANN001
    raw = source.read_bytes()
    doc = json.loads(gzip.decompress(raw))
    if len(doc["cases"]) != 1:
        raise ValueError("slice sheet requires exactly one retained case")
    case = doc["cases"][0]
    bounds = case["bounds"]
    ys = list(range(case["envelope"][1], case["envelope"][4] + 1))
    if layers is not None:
        if not layers or len(set(layers)) != len(layers) or any(y not in ys for y in layers):
            raise ValueError("selected layers must be unique heights within the saved envelope")
        ys = layers
    cell = 12
    width = (bounds[3] - bounds[0] + 1) * cell + 30
    height = (bounds[5] - bounds[2] + 1) * cell + 40
    canvas_width = 4 * width + 20
    header_height = 115 if layers is None else 130
    canvas_height = ((len(ys) + 3) // 4) * height + header_height
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_width}" height="{canvas_height}">',
        '<rect width="100%" height="100%" fill="#f5f3ec"/>',
        '<g font-family="DejaVu Sans, sans-serif">',
        f'<text x="10" y="24" font-size="17">Saved slices: {html.escape(case["root"])}</text>',
        '<text x="10" y="45" font-size="12">X right, Z down. White air; grey other blocks; h slab/stair; D door; T trapdoor; G gate; F fire. Not collision shapes.</text>',
        f'<text x="10" y="64" font-size="11">Raw SHA-256: {hashlib.sha256(raw).hexdigest()}</text>',
    ]
    parts.extend(
        [
            f'<text x="10" y="80" font-size="12">Selected layers only: {", ".join(map(str, ys))}</text>'
        ]
        if layers is not None
        else []
    )
    for panel, y in enumerate(ys):
        px, py = 10 + (panel % 4) * width, header_height - 20 + (panel // 4) * height
        parts.append(
            f'<text x="{px}" y="{py - 8}" font-size="12">Y={y}; X={bounds[0]}..{bounds[3]}, Z={bounds[2]}..{bounds[5]}</text>'
        )
        for z in range(bounds[2], bounds[5] + 1):
            for x in range(bounds[0], bounds[3] + 1):
                state = state_at(case, x, y, z)
                name = state["Name"]
                fill, letter = appearance(name)
                for suffix, color, marker in (
                    ("trapdoor", "#a2c49d", "T"),
                    ("_door", "#78b690", "D"),
                    ("fence_gate", "#c9b682", "G"),
                    (":fire", "#ff832e", "F"),
                ):
                    if name.endswith(suffix):
                        fill, letter = color, marker
                        break
                sx, sy = px + (x - bounds[0]) * cell, py + (z - bounds[2]) * cell
                title = html.escape(f"{x},{y},{z}: " + json.dumps(state, sort_keys=True))
                parts.append(
                    f'<rect x="{sx}" y="{sy}" width="{cell}" height="{cell}" fill="{fill}" stroke="#c6c9c7" stroke-width="0.3"><title>{title}</title></rect>'
                )
                if letter:
                    parts.append(f'<text x="{sx + 2}" y="{sy + 10}" font-size="9">{letter}</text>')
    parts.append("</g></svg>")
    output.write_text("\n".join(parts) + "\n")


def main() -> None:
    doc = json.loads(gzip.decompress((ROOT / "pilot/observations.json.gz").read_bytes()))
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1650" height="810" viewBox="0 0 1650 810">',
        '<rect width="1650" height="810" fill="#f5f3ec"/>',
        '<g font-family="DejaVu Sans, sans-serif">',
        '<text x="20" y="30" font-size="21">Item 13: exact saved block plans and centre section</text>',
        '<text x="20" y="54" font-size="13">White: air. Grey: solid/ore. C: chest, B: barrel, S: spawner, W: water, P: prop, h: slab/stair, v: vein/lichen.</text>',
    ]
    for row, c in enumerate(doc["cases"]):
        e = c["envelope"]
        base_y = 93 + row * 355
        parts.append(
            f'<text x="20" y="{base_y}" font-size="17">{html.escape(c["world"])}: envelope {e}, planes show X right / Z down</text>'
        )
        specs = [("floor", e[1]), ("feet", e[1] + 1), ("head", e[1] + 2), ("upper", e[1] + 4)]
        for col, (label, y) in enumerate(specs):
            px = 20 + col * 325
            py = base_y + 38
            parts.append(
                f'<text x="{px}" y="{py - 10}" font-size="13">{label} Y={y}, X={c["bounds"][0]}..{c["bounds"][3]}, Z={c["bounds"][2]}..{c["bounds"][5]}</text>'
            )
            for iz, z in enumerate(range(c["bounds"][2], c["bounds"][5] + 1)):
                for ix, x in enumerate(range(c["bounds"][0], c["bounds"][3] + 1)):
                    fill, letter = appearance(state_at(c, x, y, z)["Name"])
                    sx = px + ix * 17
                    sy = py + iz * 17
                    parts.append(
                        f'<rect x="{sx}" y="{sy}" width="17" height="17" fill="{fill}" stroke="#c6c9c7" stroke-width="0.4"/>'
                    )
                    if letter:
                        parts.append(
                            f'<text x="{sx + 4}" y="{sy + 13}" font-size="11">{letter}</text>'
                        )
            bx, bz = px + 3 * 17, py + 3 * 17
            bw, bh = (e[3] - e[0] + 1) * 17, (e[5] - e[2] + 1) * 17
            for xx, yy, ww, hh in (
                (bx, bz, bw, 2),
                (bx, bz + bh - 2, bw, 2),
                (bx, bz, 2, bh),
                (bx + bw - 2, bz, 2, bh),
            ):
                parts.append(f'<rect x="{xx}" y="{yy}" width="{ww}" height="{hh}" fill="#e16521"/>')

        px = 1320
        py = base_y + 38
        z = (e[2] + e[5]) // 2
        parts.append(
            f'<text x="{px}" y="{py - 10}" font-size="13">X/Y section at Z={z}, Y up</text>'
        )
        for iy, y in enumerate(range(c["bounds"][4], c["bounds"][1] - 1, -1)):
            for ix, x in enumerate(range(c["bounds"][0], c["bounds"][3] + 1)):
                fill, letter = appearance(state_at(c, x, y, z)["Name"])
                sx = px + ix * 17
                sy = py + iy * 17
                parts.append(
                    f'<rect x="{sx}" y="{sy}" width="17" height="17" fill="{fill}" stroke="#c6c9c7" stroke-width="0.4"/>'
                )
                if letter:
                    parts.append(f'<text x="{sx + 4}" y="{sy + 13}" font-size="11">{letter}</text>')
    parts += [
        '<text x="20" y="790" font-size="13">Orange: saved envelope. These are block diagrams, not player-view renders. Solids are not automatically hazards or inaccessible rooms.</text>',
        "</g></svg>",
    ]
    (ROOT / "pilot/block-plans.svg").write_text("\n".join(parts) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--layers", type=int, nargs="+", help="explicit envelope Y layers to render"
    )
    args = parser.parse_args()
    if args.input:
        if args.output is None:
            raise ValueError("slice rendering requires an output path")
        render_slices(args.input, args.output, layers=args.layers)
    else:
        if args.layers is not None:
            raise ValueError("layer selection requires a slice input")
        main()
