"""Read accepted worlds for the predeclared Item 12 discoverability assessment."""

# pyright: standard
# ruff: noqa: D103, EM101, EM102, TRY003, PLR2004
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
from array import array
from collections import Counter
from pathlib import Path
from typing import Any, cast

from tools.analyze_route_opportunities import (
    MISSING,
    ROOT,
    accepted_inputs,
    candidates,
    height_at,
    read_bound,
    verify_world,
)
from tools.manage_item4_environment import _world_backup_lock

from mcpack_evidence.item6_json import parse_strict_json
from mcpack_evidence.item7_anvil import RegionContext, decode_region_payloads
from mcpack_evidence.item7_archive_io import open_directory, open_regular
from mcpack_evidence.item7_archive_models import ArchiveManifest

FIELDS = ("WORLD_SURFACE", "MOTION_BLOCKING_NO_LEAVES")
OFFSETS = ((64, 0), (45, 45), (0, 64), (-45, 45), (-64, 0), (-45, -45), (0, -64), (45, -45))
PROTOCOL = ROOT / "evidence/item-12/protocol.md"


def geometry(world: Path) -> dict[str, array[int]]:
    """Decode only two existing saved heightmaps, without reprocessing routes."""
    maps = {name: array("h", [MISSING]) * (1024 * 1024) for name in FIELDS}
    seen = set()
    for rx in (-1, 0):
        for rz in (-1, 0):
            relative = f"region/r.{rx}.{rz}.mca"
            context = RegionContext("minecraft:overworld", relative, -64, 384)
            for record, _ in decode_region_payloads(world / relative, context):
                key = record.chunk_x, record.chunk_z
                if key in seen or not record.full:
                    raise ValueError(f"duplicate or incomplete selected chunk: {key}")
                seen.add(key)
                fields = {row.name: row.values for row in record.heightmaps}
                if len(fields) != len(record.heightmaps) or not set(FIELDS) <= fields.keys():
                    raise ValueError(f"missing or duplicate heightmap: {key}")
                for z in range(16):
                    start = (record.chunk_z * 16 + z + 512) * 1024 + record.chunk_x * 16 + 512
                    for name in FIELDS:
                        maps[name][start : start + 16] = array(
                            "h", fields[name][z * 16 : z * 16 + 16]
                        )
    if len(seen) != 4096:
        raise ValueError("incomplete selected world denominator")
    return maps


def select_cases(census: dict[str, Any]) -> list[dict[str, Any]]:
    """Select before visibility inspection, keeping every family's full count."""
    rows = candidates(census)
    counts = Counter(row["family_id"] for row in rows)
    boxes = {(r["registry_id"], r["chunk_x"], r["chunk_z"]): r for r in census["occurrence_biomes"]}
    selected = {}
    for row in sorted(
        rows,
        key=lambda r: (hashlib.sha256(r["location_id"].encode()).hexdigest(), r["location_id"]),
    ):
        family = row["family_id"]
        if family in selected:
            continue
        entry = boxes.get((row.get("registry_id"), row["chunk_x"], row["chunk_z"]))
        row["envelope"] = entry["envelope"] if entry else None
        row["biome"] = entry["biome"] if entry else row.get("biome")
        row["family_count"] = counts[family]
        row["density_chunks"] = census["full_chunks"]
        selected[family] = row
    return [selected[key] for key in sorted(selected)]


def ray(heights: array[int], eye: list[float], target: list[float]) -> dict[str, Any]:
    steps = max(1, math.ceil(math.hypot(target[0] - eye[0], target[2] - eye[2])))
    for i in range(1, steps + 1):
        t = i / steps
        p = [eye[j] + t * (target[j] - eye[j]) for j in range(3)]
        x, z = math.floor(p[0]), math.floor(p[2])
        height = height_at(heights, x, z)
        if height is None:
            return {"status": "UNKNOWN", "at": [x, z], "reason": "missing_height"}
        if p[1] < height + 1:
            return {"status": "OCCLUDED", "at": [x, z], "height": height, "ray_y": p[1]}
    return {"status": "CLEAR"}


def observe(case: dict[str, Any], maps: dict[str, array[int]]) -> dict[str, Any]:
    box = case["envelope"]
    target = case["target"]
    if target is None:
        return {"status": "UNKNOWN", "reason": "missing_target_geometry", "views": []}
    cx, cz = math.floor(target[0]), math.floor(target[2])
    targets = [target]
    if box:
        targets += [
            [x, box[4] + 1, z]
            for x, z in ((box[0], box[2]), (box[3], box[2]), (box[3], box[5]), (box[0], box[5]))
        ]
    targets = [list(p) for p in dict.fromkeys(tuple(p) for p in targets)]
    views = []
    for dx, dz in OFFSETS:
        x, z = cx + dx, cz + dz
        heights = {name: height_at(maps[name], x, z) for name in FIELDS}
        base = heights[FIELDS[1]]
        eye = [x + 0.5, base + 2.62, z + 0.5] if base is not None else None
        internal = box is not None and box[0] <= x <= box[3] and box[2] <= z <= box[5]
        outcomes = {
            name: [
                {"status": "UNKNOWN", "reason": "observer_inside_envelope"}
                if internal
                else ray(maps[name], eye, point)
                if eye
                else {"status": "UNKNOWN", "reason": "missing_eye_height"}
                for point in targets
            ]
            for name in FIELDS
        }
        views.append({"cell": [x, z], "heights": heights, "eye": eye, "rays": outcomes})
    complete = all(
        view["eye"] is not None
        and view["rays"][FIELDS[0]][0].get("reason") != "observer_inside_envelope"
        for view in views
    )
    low = min(range(8), key=lambda i: views[i]["eye"][1]) if complete else None
    high = min(range(8), key=lambda i: -views[i]["eye"][1]) if complete else None
    profiles = {}
    for axis in ("x", "z"):
        profiles[axis] = [
            {
                "coordinate": [
                    cx + delta if axis == "x" else cx,
                    cz + delta if axis == "z" else cz,
                ],
                **{
                    name: height_at(
                        maps[name],
                        cx + delta if axis == "x" else cx,
                        cz + delta if axis == "z" else cz,
                    )
                    for name in FIELDS
                },
            }
            for delta in range(-64, 65)
        ]
    return {
        "status": "MEASURED",
        "targets": targets,
        "views": views,
        "low_view": low,
        "high_view": high,
        "relief": views[high]["eye"][1] - views[low]["eye"][1]
        if low is not None and high is not None
        else None,
        "profiles": profiles,
    }


def analyze(name: str, raw_root: Path) -> dict[str, Any]:
    accepted = accepted_inputs()
    if name not in accepted:
        raise ValueError("world is not an accepted Item 10 input")
    custody = raw_root / (name + "-custody")
    world = custody / "restored-world/world"
    manifest_raw = read_bound(ROOT / "evidence/item-10" / name / "archive-manifest.json")
    manifest = ArchiveManifest.model_validate_json(manifest_raw)
    entry = next(r for r in manifest.files if r.relative_path == "world-backup.json")
    backup = cast(
        "dict[str, Any]",
        parse_strict_json(read_bound(custody / "restored-local/world-backup.json", entry.sha256)),
    )
    if backup["archive_sha256"] != next(
        r.sha256 for r in manifest.files if r.relative_path == "world.tar.gz"
    ):
        raise ValueError("nested archive identity mismatch")
    raw = read_bound(
        raw_root / (name + "-analysis/all-strata.json"), accepted[name]["input_sha256"]
    )
    census = cast("dict[str, Any]", parse_strict_json(raw))["strata"]["overworld"]
    if census["bounds_chunks"] != [-32, 31, -32, 31] or census["full_chunks"] != 4096:
        raise ValueError("unexpected Overworld frame")
    cases = select_cases(census)
    with open_directory(world):
        if (world / "session.lock").exists() or (world / "session.lock").is_symlink():
            with open_regular(world / "session.lock"):
                _ = None
    with _world_backup_lock(world):
        verify_world(world, backup["world_files"])
        maps = geometry(world)
        for case in cases:
            case["observation"] = observe(case, maps)
        verify_world(world, backup["world_files"])
    return {
        "protocol": "item12-discoverability-v3",
        "world": name,
        "inputs": {
            "census_sha256": accepted[name]["input_sha256"],
            "archive_manifest_sha256": hashlib.sha256(manifest_raw).hexdigest(),
            "world_backup_sha256": entry.sha256,
            "protocol_sha256": hashlib.sha256(read_bound(PROTOCOL)).hexdigest(),
            "producer_sha256": hashlib.sha256(read_bound(Path(__file__))).hexdigest(),
            "shared_reader_sha256": hashlib.sha256(
                read_bound(ROOT / "tools/analyze_route_opportunities.py")
            ).hexdigest(),
        },
        "cases": cases,
        "human_metrics": "NOT MEASURED",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True)
    parser.add_argument("--raw-root", type=Path, default=ROOT / "evidence/raw/item10")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.output.is_symlink():
        raise ValueError("output must be absent; preserve previous results")
    result = analyze(args.name, args.raw_root)
    encoded = (
        json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False).encode() + b"\n"
    )
    with args.output.open("xb") as stream:
        stream.write(gzip.compress(encoded, mtime=0))
    print(
        json.dumps(
            {
                "world": args.name,
                "cases": len(result["cases"]),
                "bytes": args.output.stat().st_size,
                "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
            }
        )
    )


if __name__ == "__main__":
    main()
