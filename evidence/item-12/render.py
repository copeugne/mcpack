"""Render retained Item 12 technical sections, never simulated player screenshots."""

# pyright: standard
# ruff: noqa: D103, INP001, E501
# Long lines are literal SVG markup; the renderer has one fixed panel pass.
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from html import escape
from pathlib import Path


def render(path: Path) -> str:  # noqa: C901, PLR0912 - fixed two-axis technical gallery.
    raw = path.read_bytes()
    data = json.loads(gzip.decompress(raw))
    cases = data["cases"]
    output = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{160 + len(cases) * 280}" viewBox="0 0 1200 {160 + len(cases) * 280}">',
        '<rect width="100%" height="100%" fill="#fff"/>',
        '<g font-family="sans-serif" font-size="13" fill="#17232f">',
        f'<text x="24" y="28">{escape(data["world"])} | Item 12 saved heightmap sections</text>',
        f'<text x="24" y="52">Result SHA-256: {hashlib.sha256(raw).hexdigest()}</text>',
        '<text x="24" y="76">Blue: WORLD_SURFACE. Green: MOTION_BLOCKING_NO_LEAVES. Red: saved envelope (air/padding included).</text>',
        '<text x="24" y="100">Technical placement context only. No cave interiors, textures, entrance positions or human recognition shown.</text>',
        '<text x="24" y="124">Horizontal axis: world X or Z blocks, increasing right. Vertical axis: world Y blocks. Missing samples leave gaps.</text>',
    ]
    for index, case in enumerate(cases):
        y0 = 160 + index * 280
        output.append(
            f'<text x="24" y="{y0}">{escape(case["family_id"])} | {escape(case["location_id"])} | biome: {escape(str(case["biome"]))}</text>'
        )
        obs = case["observation"]
        if "profiles" not in obs:
            output.append(f'<text x="24" y="{y0 + 30}">UNKNOWN: missing target geometry</text>')
            continue
        box = case["envelope"]
        for col, axis in enumerate(("x", "z")):
            profile = obs["profiles"][axis]
            coord = 0 if axis == "x" else 1
            lo, hi = profile[0]["coordinate"][coord], profile[-1]["coordinate"][coord]
            values = [
                r[n]
                for r in profile
                for n in ("WORLD_SURFACE", "MOTION_BLOCKING_NO_LEAVES")
                if r[n] is not None
            ]
            if box:
                values.extend([box[1], box[4]])
            elif case["target"]:
                values.append(case["target"][1] - 1)
            low, high = min(values, default=-64) - 10, max(values, default=64) + 10
            x0 = 60 + col * 590

            def xp(v: float, origin: float = x0, lower: float = lo) -> float:
                return origin + (v - lower) / 128 * 480

            def yp(v: float, origin: float = y0, lower: float = low, upper: float = high) -> float:
                return origin + 210 - (v - lower) / (upper - lower) * 160

            output.append(
                f'<rect x="{x0}" y="{y0 + 50}" width="480" height="160" fill="#f4f6f8" stroke="#aaa"/>'
            )
            if box:
                left, right = max(lo, box[coord * 2]), min(hi, box[coord * 2 + 3])
                # X uses bounds 0/3; Z uses bounds 2/5.
                if right >= left:
                    output.append(
                        f'<rect x="{xp(left):.2f}" y="{yp(box[4]):.2f}" width="{max(1, xp(right) - xp(left)):.2f}" height="{max(1, yp(box[1]) - yp(box[4])):.2f}" fill="#fa5252" fill-opacity="0.15" stroke="#c92a2a"/>'
                    )
            if not box and case["target"]:
                point = case["target"]
                output.append(
                    f'<circle cx="{xp(point[coord * 2]):.2f}" cy="{yp(point[1] - 1):.2f}" r="3" fill="#c92a2a"/>'
                )
            for name, color in [
                ("WORLD_SURFACE", "#1971c2"),
                ("MOTION_BLOCKING_NO_LEAVES", "#2b8a3e"),
            ]:
                segment = []
                for row in [*profile, {name: None}]:
                    if row[name] is None:
                        if segment:
                            output.append(
                                f'<polyline points="{" ".join(segment)}" stroke="{color}" fill="none" stroke-width="2"/>'
                            )
                        segment = []
                    else:
                        segment.append(f"{xp(row['coordinate'][coord]):.2f},{yp(row[name]):.2f}")
            output.extend(
                [
                    f'<text x="{x0}" y="{y0 + 235}">{axis.upper()}: {lo} to {hi}; fixed {"Z" if axis == "x" else "X"}={profile[0]["coordinate"][1 - coord]}</text>',
                    f'<text x="{x0}" y="{y0 + 40}">Y {low} to {high}</text>',
                ]
            )
    return "\n".join([*output, "</g></svg>"]) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    with args.output.open("x") as stream:
        stream.write(render(args.result))


if __name__ == "__main__":
    main()
