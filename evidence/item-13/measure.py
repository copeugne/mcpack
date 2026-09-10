"""Extract the predeclared small-dungeon representative from accepted worlds."""

# pyright: standard
# ruff: noqa: D103, EM101, EM102, TRY003, INP001, PLR2004, T201
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import resource
import shutil
import time
from pathlib import Path
from typing import Any, cast

from tools.analyze_route_opportunities import ROOT, accepted_inputs, read_bound, verify_world
from tools.analyze_structure_density import saved_block_section
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


def extract(case, voxel_budget=3757):  # noqa: ANN001, ANN201
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
    return {
        **extract_saved(case, world, backup, voxel_budget),
        "world_backup_sha256": entry.sha256,
        "archive_manifest_sha256": hashlib.sha256(manifest_raw).hexdigest(),
    }


def extract_saved(case, world, backup, voxel_budget, start=None):  # noqa: ANN001, ANN201, C901, PLR0912
    """Read verified saved cells for natural starts or a supplied forced start."""
    envelope = case["envelope"]
    bounds = [v - 3 if i < 3 else v + 3 for i, v in enumerate(envelope)]
    volume = (bounds[3] - bounds[0] + 1) * (bounds[4] - bounds[1] + 1) * (bounds[5] - bounds[2] + 1)
    if volume > voxel_budget:
        raise ValueError(f"pilot volume budget exceeded: {volume}")
    dimension = case.get("dimension", "minecraft:overworld")
    directory, min_y, height = {
        "minecraft:overworld": ("region", -64, 384),
        "minecraft:the_nether": ("DIM-1/region", 0, 256),
        "minecraft:the_end": ("DIM1/region", 0, 256),
    }[dimension]
    needed = {
        (x, z)
        for x in range(bounds[0] // 16, bounds[3] // 16 + 1)
        for z in range(bounds[2] // 16, bounds[5] // 16 + 1)
    }
    chunks = {}
    heights = {}
    natural_start = start is None
    with _world_backup_lock(world):
        verify_world(world, backup["world_files"])
        for rx, rz in sorted({(x // 32, z // 32) for x, z in needed}):
            relative = f"{directory}/r.{rx}.{rz}.mca"
            for record, payload in decode_region_payloads(
                world / relative, RegionContext(dimension, relative, min_y, height)
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
                if natural_start and key == (case["chunk_x"], case["chunk_z"]):
                    start = chunk["structures"]["starts"][case["root"]]
        if set(chunks) != needed or start is None:
            raise ValueError("incomplete pilot geometry")
        sections = {}
        for (cx, cz), chunk in chunks.items():
            for sy in range(bounds[1] // 16, bounds[4] // 16 + 1):
                section = saved_block_section(chunk, sy)
                if section is None:
                    raise ValueError(f"missing block section: {(cx, sy, cz)}")
                palette, indices = section
                sections[(cx, sy, cz)] = (
                    [json.dumps(value, sort_keys=True, separators=(",", ":")) for value in palette],
                    indices,
                )
        states = []
        block_entities = []
        for y in range(bounds[1], bounds[4] + 1):
            for z in range(bounds[2], bounds[5] + 1):
                for x in range(bounds[0], bounds[3] + 1):
                    palette, indices = sections[(x // 16, y // 16, z // 16)]
                    index = indices[x % 16 + 16 * (z % 16) + 256 * (y % 16)]
                    if not 0 <= index < len(palette):
                        raise ValueError("saved block palette index out of range")
                    states.append(palette[index])
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
    parser.add_argument("--fixed-root", help="one root from the fixed Moog selection")
    parser.add_argument(
        "--selection",
        type=Path,
        default=ROOT / "evidence/item-13/fixed-moog-selection.json",
        help="predeclared fixed-layout selection using the existing format",
    )
    args = parser.parse_args()
    if args.output.exists() or args.output.is_symlink():
        raise ValueError("output must be absent; preserve previous attempts")
    if shutil.disk_usage(ROOT).free < 5 * 1024**3:
        raise ValueError("pilot free-space floor not met")
    begun = time.monotonic()
    selection_sha256 = None
    if args.fixed_root:
        selection_raw = read_bound(args.selection)
        plan = json.loads(selection_raw)
        chosen = [r for r in plan["selected"] if r["root"] == args.fixed_root]
        if len(chosen) != 1:
            raise ValueError("root must identify exactly one preselected fixed instance")
        candidate_raw = read_bound(
            ROOT / "evidence/item-13/candidates.json", plan["input_sha256"]["candidates"]
        )
        selected = [
            r
            for r in json.loads(candidate_raw)["candidates"]
            if r["id"] == chosen[0]["candidate_id"]
        ]
        if len(selected) != 1 or selected[0]["bounds"] != chosen[0]["bounds"]:
            raise ValueError("selected instance or bounds disagree with candidate index")
        denominator = chosen[0]["eligible_count"]
        selection_sha256 = hashlib.sha256(selection_raw).hexdigest()
        results = [extract(selected[0], chosen[0]["voxel_count"])]
    else:
        selected, denominator = select()
        results = [extract(case) for case in selected]
    elapsed = time.monotonic() - begun
    result = {
        "protocol": "item13-fixed-blocks-v1"
        if args.fixed_root
        else "item13-quality-v1-small-dungeon",
        "protocol_sha256": hashlib.sha256(read_bound(PROTOCOL)).hexdigest(),
        "producer_sha256": hashlib.sha256(read_bound(Path(__file__))).hexdigest(),
        "eligible_baseline_occurrences": denominator,
        "cases": results,
        "human_metrics": "NOT MEASURED",
    }
    if selection_sha256 is not None:
        result["selection_sha256"] = selection_sha256
    raw = gzip.compress(
        (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode(), mtime=0
    )
    with args.output.open("xb") as stream:
        stream.write(raw)
    print(
        json.dumps(
            {
                "elapsed_seconds": elapsed,
                "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                "output_bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "selected": [row["id"] for row in results],
                "voxel_count": sum(row["voxel_count"] for row in results),
            }
        )
    )
    time_cap, size_cap = (300, 10 * 1024**2) if args.fixed_root else (600, 1024**2)
    if (
        elapsed > time_cap
        or len(raw) > size_cap
        or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 1536 * 1024
    ):
        raise ValueError("pilot resource cap exceeded; retained result is rejected")


if __name__ == "__main__":
    main()
