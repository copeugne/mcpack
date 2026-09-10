"""Compare the four declared r5 placements with a hash-verified stopped restore."""

# pyright: standard
# ruff: noqa: D103, EM101, EM102, TRY003, INP001, T201
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from typing import Any, cast

from tools.analyze_route_opportunities import ROOT, read_bound, verify_world
from tools.analyze_structure_density import saved_block_section
from tools.manage_item4_environment import _world_backup_lock

from mcpack_evidence.item7_anvil import RegionContext, decode_region_payloads
from mcpack_evidence.item7_nbt import decode_compound_nbt


def verify(world: Path, backup_path: Path) -> dict[str, Any]:  # noqa: C901, PLR0912
    backup_hash = "cf6d6b5fc690fbceab9941ad1b0bc4b4a74d192e4ae1597469e4b5a9039836d1"
    backup = json.loads(read_bound(backup_path, backup_hash))
    raw = gzip.decompress(read_bound(Path(__file__).with_name("r5-temple-variants.json.gz")))
    if (
        hashlib.sha256(raw).hexdigest()
        != "b3e1a088879bf6fd02039c2768e3d40912abfb18012fe11d199038629a326093"
    ):
        raise ValueError("r5 projection identity mismatch")
    cases = json.loads(raw)["cases"]
    needed = {
        (x, z)
        for case in cases
        for x in range(case["bounds"][0] // 16, case["bounds"][3] // 16 + 1)
        for z in range(case["bounds"][2] // 16, case["bounds"][5] // 16 + 1)
    }
    chunks = {}
    rows = []
    with _world_backup_lock(world):
        verify_world(world, backup["world_files"])
        for rx, rz in sorted({(x // 32, z // 32) for x, z in needed}):
            relative = f"DIM-1/region/r.{rx}.{rz}.mca"
            for record, payload in decode_region_payloads(
                world / relative, RegionContext("minecraft:the_nether", relative, 0, 256)
            ):
                key = record.chunk_x, record.chunk_z
                if key not in needed:
                    continue
                if key in chunks or not record.full:
                    raise ValueError(f"Duplicate or incomplete chunk: {key}")
                chunks[key] = cast("dict[str, Any]", decode_compound_nbt(payload))
        if set(chunks) != needed:
            raise ValueError("Missing saved chunks")
        for case in cases:
            bounds = case["bounds"]
            sections = {}
            for cx, cz in needed:
                for sy in range(bounds[1] // 16, bounds[4] // 16 + 1):
                    section = saved_block_section(chunks[(cx, cz)], sy)
                    if section is None:
                        raise ValueError(f"Missing saved section: {(cx, sy, cz)}")
                    sections[(cx, sy, cz)] = section
            differences = []
            central = None
            index = 0
            center = [
                (case["envelope"][0] + case["envelope"][3]) // 2,
                164,
                (case["envelope"][2] + case["envelope"][5]) // 2,
            ]
            for y in range(bounds[1], bounds[4] + 1):
                for z in range(bounds[2], bounds[5] + 1):
                    for x in range(bounds[0], bounds[3] + 1):
                        palette, indices = sections[(x // 16, y // 16, z // 16)]
                        state = palette[indices[x % 16 + 16 * (z % 16) + 256 * (y % 16)]]
                        immediate = case["palette"][case["blocks_yzx"][index]]
                        if state != immediate:
                            differences.append(
                                {"position": [x, y, z], "immediate": immediate, "saved": state}
                            )
                        if [x, y, z] == center:
                            central = state
                        index += 1
            if index != len(case["blocks_yzx"]) or central is None:
                raise ValueError("Incomplete saved comparison")
            if central["Name"] != case["observed_central_material"]:
                raise ValueError("Saved central material differs")
            rows.append(
                {
                    "root": case["root"],
                    "origin": case["origin"],
                    "cells": index,
                    "saved_central": central,
                    "differences": differences,
                }
            )
        verify_world(world, backup["world_files"])
    return {"world_backup_sha256": backup_hash, "cases": rows}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("world", type=Path)
    parser.add_argument(
        "--backup",
        type=Path,
        default=ROOT / "evidence/raw/item13/temple-r5-custody/world-backup.json",
    )
    args = parser.parse_args()
    print(json.dumps(verify(args.world, args.backup), indent=2))
