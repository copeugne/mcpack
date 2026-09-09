"""Extract the predeclared small-dungeon representative from accepted worlds."""

# pyright: standard
# ruff: noqa: D103, EM101, EM102, TRY003, INP001, PLR2004, T201
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import shutil
import time
from pathlib import Path
from typing import Any, cast

from tools.analyze_route_opportunities import ROOT, accepted_inputs, read_bound, verify_world
from tools.analyze_structure_density import saved_block_at
from tools.manage_item4_environment import _world_backup_lock

from mcpack_evidence.item7_anvil import RegionContext, decode_region_payloads
from mcpack_evidence.item7_archive_models import ArchiveManifest
from mcpack_evidence.item7_nbt import decode_compound_nbt

FAMILY = "betterdungeons:small_dungeon"
PROTOCOL = ROOT / "evidence/item-13/protocol.md"


def select():  # noqa: ANN201
    candidates = []
    for name, identity in sorted(accepted_inputs().items()):
        if not name.endswith("-baseline"):
            continue
        raw = read_bound(
            ROOT / "evidence/raw/item10" / f"{name}-analysis/all-strata.json",
            identity["input_sha256"],
        )
        census = json.loads(raw)["strata"]["overworld"]
        boxes = {
            (r["registry_id"], r["chunk_x"], r["chunk_z"]): r["envelope"]
            for r in census["occurrence_biomes"]
        }
        for row in census["classification"]["occurrences"]:
            if row["family_id"] != FAMILY:
                continue
            key = f"{name}|overworld|{row['registry_id']}|{row['chunk_x']}|{row['chunk_z']}"
            candidates.append(
                {
                    "id": key,
                    "world": name,
                    "seed_role": name.removeprefix("full-").rsplit("-r", 1)[0],
                    "root": row["registry_id"],
                    "chunk_x": row["chunk_x"],
                    "chunk_z": row["chunk_z"],
                    "envelope": boxes[(row["registry_id"], row["chunk_x"], row["chunk_z"])],
                    "census_sha256": identity["input_sha256"],
                }
            )
    ordered = sorted(
        candidates, key=lambda row: (hashlib.sha256(row["id"].encode()).hexdigest(), row["id"])
    )
    chosen = []
    for row in ordered:
        if row["seed_role"] not in {c["seed_role"] for c in chosen}:
            chosen.append(row)
        if len(chosen) == 2:
            break
    if len(chosen) != 2:
        raise ValueError("two distinct-seed baseline representatives unavailable")
    return chosen, len(candidates)


def extract(case):  # noqa: ANN001, ANN201, C901, PLR0912
    name = case["world"]
    custody = ROOT / "evidence/raw/item10" / f"{name}-custody"
    world = custody / "restored-world/world"
    manifest_raw = read_bound(ROOT / "evidence/item-10" / name / "archive-manifest.json")
    manifest = ArchiveManifest.model_validate_json(manifest_raw)
    entry = next(r for r in manifest.files if r.relative_path == "world-backup.json")
    backup = json.loads(read_bound(custody / "restored-local/world-backup.json", entry.sha256))
    if backup["archive_sha256"] != next(
        r.sha256 for r in manifest.files if r.relative_path == "world.tar.gz"
    ):
        raise ValueError("nested world archive identity mismatch")
    envelope = case["envelope"]
    bounds = [v - 3 if i < 3 else v + 3 for i, v in enumerate(envelope)]
    volume = (bounds[3] - bounds[0] + 1) * (bounds[4] - bounds[1] + 1) * (bounds[5] - bounds[2] + 1)
    if volume > 3757:
        raise ValueError(f"pilot volume budget exceeded: {volume}")
    needed = {
        (x, z)
        for x in range(bounds[0] // 16, bounds[3] // 16 + 1)
        for z in range(bounds[2] // 16, bounds[5] // 16 + 1)
    }
    chunks = {}
    heights = {}
    start = None
    with _world_backup_lock(world):
        verify_world(world, backup["world_files"])
        for rx, rz in sorted({(x // 32, z // 32) for x, z in needed}):
            relative = f"region/r.{rx}.{rz}.mca"
            for record, payload in decode_region_payloads(
                world / relative, RegionContext("minecraft:overworld", relative, -64, 384)
            ):
                key = record.chunk_x, record.chunk_z
                if key not in needed:
                    continue
                if key in chunks or not record.full:
                    raise ValueError(f"duplicate or incomplete pilot chunk: {key}")
                chunk = cast("dict[str, Any]", decode_compound_nbt(payload))
                chunks[key] = chunk
                maps = {r.name: r.values for r in record.heightmaps}
                heights[key] = maps["WORLD_SURFACE"]
                if key == (case["chunk_x"], case["chunk_z"]):
                    start = chunk["structures"]["starts"][case["root"]]
        if set(chunks) != needed or start is None:
            raise ValueError("incomplete pilot geometry")
        states = []
        block_entities = []
        for y in range(bounds[1], bounds[4] + 1):
            for z in range(bounds[2], bounds[5] + 1):
                for x in range(bounds[0], bounds[3] + 1):
                    value = saved_block_at(chunks[(x // 16, z // 16)], (x, y, z))
                    if value is None:
                        raise ValueError(f"missing pilot block section: {(x, y, z)}")
                    states.append(json.dumps(value, sort_keys=True, separators=(",", ":")))
        for chunk in chunks.values():
            block_entities.extend(
                block
                for block in chunk.get("block_entities", [])
                if all(
                    bounds[i] <= block[axis] <= bounds[i + 3]
                    for i, axis in enumerate(("x", "y", "z"))
                )
            )
        surface = [
            [x, z, heights[(x // 16, z // 16)][(z % 16) * 16 + x % 16]]
            for z in range(envelope[2], envelope[5] + 1)
            for x in range(envelope[0], envelope[3] + 1)
        ]
        verify_world(world, backup["world_files"])
    palette = sorted(set(states))
    indexes = {state: i for i, state in enumerate(palette)}
    return {
        **case,
        "world_backup_sha256": entry.sha256,
        "archive_manifest_sha256": hashlib.sha256(manifest_raw).hexdigest(),
        "bounds": bounds,
        "voxel_count": volume,
        "palette": [json.loads(state) for state in palette],
        "blocks_yzx": [indexes[state] for state in states],
        "block_entities": sorted(block_entities, key=lambda b: (b["x"], b["y"], b["z"])),
        "surface_xzy": surface,
        "start_nbt": start,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.output.is_symlink():
        raise ValueError("output must be absent; preserve previous attempts")
    if shutil.disk_usage(ROOT).free < 5 * 1024**3:
        raise ValueError("pilot free-space floor not met")
    begun = time.monotonic()
    selected, denominator = select()
    results = [extract(case) for case in selected]
    elapsed = time.monotonic() - begun
    result = {
        "protocol": "item13-quality-v1-small-dungeon",
        "protocol_sha256": hashlib.sha256(read_bound(PROTOCOL)).hexdigest(),
        "producer_sha256": hashlib.sha256(read_bound(Path(__file__))).hexdigest(),
        "eligible_baseline_occurrences": denominator,
        "cases": results,
        "human_metrics": "NOT MEASURED",
    }
    raw = gzip.compress(
        (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode(), mtime=0
    )
    with args.output.open("xb") as stream:
        stream.write(raw)
    print(
        json.dumps(
            {
                "elapsed_seconds": elapsed,
                "output_bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "selected": [row["id"] for row in results],
                "voxel_count": sum(row["voxel_count"] for row in results),
            }
        )
    )
    if elapsed > 600 or len(raw) > 1024**2:
        raise ValueError("pilot resource cap exceeded; retained result is rejected")


if __name__ == "__main__":
    main()
