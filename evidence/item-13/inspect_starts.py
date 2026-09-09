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

from mcpack_evidence.item7_anvil import RegionContext, decode_region_payloads
from mcpack_evidence.item7_nbt import decode_compound_nbt


def inspect(name, relative):
    candidate_raw = read_bound(ROOT / "evidence/item-13/candidates.json")
    index = json.loads(candidate_raw)
    identity = index["worlds"][name]
    cases = [r for r in index["candidates"] if r["world"] == name and r["start_region"] == relative]
    if not cases or len({r["dimension"] for r in cases}) != 1:
        raise ValueError("selection must identify one populated dimension region")
    dimension = cases[0]["dimension"]
    geometry = {
        "minecraft:overworld": (-64, 384),
        "minecraft:the_nether": (0, 256),
        "minecraft:the_end": (0, 256),
    }
    if dimension not in geometry:
        raise ValueError("custom dimension requires its accepted geometry before inspection")
    if Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ValueError("region path escapes accepted world")
    custody = ROOT / "evidence/raw/item10" / f"{name}-custody"
    backup = json.loads(
        read_bound(custody / "restored-local/world-backup.json", identity["world_backup_sha256"])
    )
    world = custody / "restored-world/world"
    rows = []
    statuses = []
    wanted = {(r["chunk_x"], r["chunk_z"]) for r in cases}
    with _world_backup_lock(world):
        verify_world(world, backup["world_files"])
        for record, payload in decode_region_payloads(
            world / relative, RegionContext(dimension, relative, *geometry[dimension])
        ):
            statuses.append([record.chunk_x, record.chunk_z, record.status])
            if (record.chunk_x, record.chunk_z) not in wanted:
                continue
            chunk = decode_compound_nbt(payload)
            structures = chunk.get("structures", {})
            if not isinstance(structures, dict):
                raise ValueError("saved structures tag is not a compound")
            starts = structures.get("starts", {})
            if not isinstance(starts, dict):
                raise ValueError("saved starts tag is not a compound")
            for case in cases:
                if (case["chunk_x"], case["chunk_z"]) != (record.chunk_x, record.chunk_z):
                    continue
                start = starts.get(case["root"])
                rows.append(
                    {
                        "id": case["id"],
                        "chunk_status": record.status,
                        "status": "SAVED" if record.full and start is not None else "INCOMPLETE",
                        "start_nbt": start,
                        "chunk_payload_sha256": hashlib.sha256(payload).hexdigest(),
                    }
                )
        verify_world(world, backup["world_files"])
    found = {r["id"] for r in rows}
    rows.extend(
        {"id": c["id"], "status": "MISSING_START_CHUNK"} for c in cases if c["id"] not in found
    )
    return {
        "candidate_sha256": hashlib.sha256(candidate_raw).hexdigest(),
        "producer_sha256": hashlib.sha256(read_bound(Path(__file__))).hexdigest(),
        "world": name,
        "region": relative,
        "world_backup_sha256": identity["world_backup_sha256"],
        "chunk_statuses": sorted(statuses),
        "starts": sorted(rows, key=lambda r: r["id"]),
        "scope": "Saved start metadata only; playable topology and gameplay NOT MEASURED",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--world", required=True)
    parser.add_argument("--region", required=True)
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
    if elapsed > 180 or peak > 1536 * 1024 or len(raw) > 10 * 1024**2:
        raise ValueError("inspection exceeded pilot budget; retained output is not accepted")


if __name__ == "__main__":
    main()
