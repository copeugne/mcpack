"""Inspect selected saved start NBT using the accepted stopped-world reader."""

# pyright: standard
# ruff: noqa: D103, EM101, TRY003, INP001, T201, PLR2004, ANN201, ANN001
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import resource
import time
from pathlib import Path

from tools.analyze_route_opportunities import ROOT, read_bound, verify_world
from tools.manage_item4_environment import _world_backup_lock

from mcpack_evidence.item7_anvil import decode_region_payloads, world_regions
from mcpack_evidence.item7_nbt import decode_compound_nbt


def inspect(name, relative):  # noqa: C901, PLR0912
    candidate_raw = read_bound(ROOT / "evidence/item-13/candidates.json")
    index = json.loads(candidate_raw)
    identity = index["worlds"][name]
    cases = [
        r
        for r in index["candidates"]
        if r["world"] == name and (relative is None or r["start_region"] == relative)
    ]
    if not cases:
        raise ValueError("selection must identify populated candidate regions")
    selected = {p for c in cases for p in [c["start_region"], *c["envelope_regions"]]}
    if any(Path(p).is_absolute() or ".." in Path(p).parts for p in selected):
        raise ValueError("region path escapes accepted world")
    geometry_raw = read_bound(ROOT / "evidence/item-10/dimension-geometry.json")
    geometry = json.loads(geometry_raw)
    custody = ROOT / "evidence/raw/item10" / f"{name}-custody"
    backup = json.loads(
        read_bound(custody / "restored-local/world-backup.json", identity["world_backup_sha256"])
    )
    world = custody / "restored-world/world"
    rows = {}
    statuses = {}
    wanted = {}
    for case in cases:
        key = case["dimension"], case["chunk_x"], case["chunk_z"]
        wanted.setdefault(key, []).append(case)
    with _world_backup_lock(world):
        verify_world(world, backup["world_files"])
        regions = {
            ctx.relative_path: (path, ctx)
            for path, ctx in world_regions(world, dimension_geometry=geometry)
        }
        for region in sorted(selected):
            if region not in regions:
                continue  # Missing regions become explicit per-candidate chunk gaps below.
            path, context = regions[region]
            for record, payload in decode_region_payloads(path, context):
                key = context.dimension, record.chunk_x, record.chunk_z
                if key in statuses:
                    raise ValueError("duplicate saved chunk identity")
                statuses[key] = record.status
                if key not in wanted:
                    continue
                chunk = decode_compound_nbt(payload)
                structures = chunk.get("structures", {})
                if not isinstance(structures, dict):
                    raise TypeError("saved structures tag is not a compound")
                starts = structures.get("starts", {})
                if not isinstance(starts, dict):
                    raise TypeError("saved starts tag is not a compound")
                for case in wanted[key]:
                    raw_start = starts.get(case["root"])
                    if raw_start is not None and (
                        not isinstance(raw_start, dict)
                        or raw_start.get("id") != case["root"]
                        or (raw_start.get("ChunkX"), raw_start.get("ChunkZ")) != key[1:]
                    ):
                        raise ValueError("saved start identity disagrees with candidate")
                    rows[case["id"]] = {
                        "id": case["id"],
                        "chunk_status": record.status,
                        "status": "SAVED"
                        if record.full and raw_start is not None
                        else "INCOMPLETE",
                        "start_nbt": raw_start,
                        "chunk_payload_sha256": hashlib.sha256(payload).hexdigest(),
                    }
        verify_world(world, backup["world_files"])
    for case in cases:
        row = rows.setdefault(case["id"], {"id": case["id"], "status": "MISSING_START_CHUNK"})
        bounds = case["bounds"]
        needed = [
            (case["dimension"], x, z)
            for x in range(bounds[0] // 16, bounds[3] // 16 + 1)
            for z in range(bounds[2] // 16, bounds[5] // 16 + 1)
        ]
        row["required_chunks"] = len(needed)
        row["incomplete_chunks"] = [
            [x, z, statuses.get((dim, x, z), "MISSING")]
            for dim, x, z in needed
            if statuses.get((dim, x, z)) != "minecraft:full"
        ]
    return {
        "candidate_sha256": hashlib.sha256(candidate_raw).hexdigest(),
        "producer_sha256": hashlib.sha256(read_bound(Path(__file__))).hexdigest(),
        "dimension_geometry_sha256": hashlib.sha256(geometry_raw).hexdigest(),
        "world": name,
        "regions": sorted(selected),
        "world_backup_sha256": identity["world_backup_sha256"],
        "chunk_statuses": [[*key, status] for key, status in sorted(statuses.items())],
        "starts": [rows[k] for k in sorted(rows)],
        "scope": (
            "Saved start metadata and chunk completeness; "
            "playable topology and gameplay NOT MEASURED"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--world", required=True)
    parser.add_argument("--region", help="restrict starts; default all candidates in this world")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.output.is_symlink():
        raise ValueError("preserve existing inspection output")
    begun = time.monotonic()
    result = inspect(args.world, args.region)
    raw = gzip.compress(
        (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode(), mtime=0
    )
    with args.output.open("xb") as stream:
        stream.write(raw)
    elapsed = time.monotonic() - begun
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(
        json.dumps(
            {
                "elapsed_seconds": elapsed,
                "peak_rss_kib": peak,
                "bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "starts": len(result["starts"]),
            }
        )
    )
    if elapsed > 360 or peak > 1536 * 1024 or len(raw) > 10 * 1024**2:
        raise ValueError("inspection exceeded world batch budget; retained output is not accepted")


if __name__ == "__main__":
    main()
