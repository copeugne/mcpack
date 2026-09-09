"""Enumerate accepted baseline starts and budget targeted Item 13 inspection."""

# pyright: standard
# ruff: noqa: D103, EM101, TRY003, INP001, T201, PLR2004, ANN201
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from tools.analyze_route_opportunities import ROOT, accepted_inputs, read_bound

from mcpack_evidence.item7_archive_models import ArchiveManifest


def enumerate_candidates():  # noqa: C901, PLR0912
    intake_raw = read_bound(ROOT / "evidence/item-13/intake.json")
    included = {row["family_id"] for row in json.loads(intake_raw)["families"] if row["included"]}
    candidates = {}
    worlds = {}
    for name, identity in sorted(accepted_inputs().items()):
        if not name.endswith("-baseline"):
            continue
        manifest_raw = read_bound(ROOT / "evidence/item-10" / name / "archive-manifest.json")
        manifest = ArchiveManifest.model_validate_json(manifest_raw)
        entry = next(r for r in manifest.files if r.relative_path == "world-backup.json")
        backup = json.loads(
            read_bound(
                ROOT / "evidence/raw/item10" / f"{name}-custody/restored-local/world-backup.json",
                entry.sha256,
            )
        )
        if backup["archive_sha256"] != next(
            r.sha256 for r in manifest.files if r.relative_path == "world.tar.gz"
        ):
            raise ValueError("nested world archive identity mismatch")
        files = {r["path"]: r for r in backup["world_files"]}
        if len(files) != len(backup["world_files"]):
            raise ValueError("duplicate backup inventory path")
        census = json.loads(
            read_bound(
                ROOT / "evidence/raw/item10" / f"{name}-analysis/all-strata.json",
                identity["input_sha256"],
            )
        )
        needed_regions = set()
        start_regions = set()
        for stratum, scope in sorted(census["strata"].items()):
            boxes = {}
            for row in scope["occurrence_biomes"]:
                key = row["registry_id"], row["chunk_x"], row["chunk_z"]
                if key in boxes:
                    raise ValueError("duplicate occurrence geometry")
                boxes[key] = row
            directories = {str(Path(r["path"]).parent) for r in scope["anvil_inputs"]}
            for row in scope["classification"]["occurrences"]:
                if row["family_id"] not in included or "registry_id" not in row:
                    continue
                if len(directories) != 1:
                    raise ValueError("ambiguous dimension region directory")
                directory = next(iter(directories))
                key = row["registry_id"], row["chunk_x"], row["chunk_z"]
                geometry = boxes[key]
                envelope = geometry["envelope"]
                if len(envelope) != 6 or any(envelope[i] > envelope[i + 3] for i in range(3)):
                    raise ValueError("invalid saved envelope")
                bounds = [v - 3 if i < 3 else v + 3 for i, v in enumerate(envelope)]
                regions = sorted(
                    {
                        f"{directory}/r.{x // 32}.{z // 32}.mca"
                        for x in range(bounds[0] // 16, bounds[3] // 16 + 1)
                        for z in range(bounds[2] // 16, bounds[5] // 16 + 1)
                    }
                )
                start_region = f"{directory}/r.{key[1] // 32}.{key[2] // 32}.mca"
                start_regions.add(start_region)
                needed_regions.update(regions)
                case_id = f"{name}|{scope['dimension']}|{key[0]}|{key[1]}|{key[2]}"
                case = {
                    "id": case_id,
                    "world": name,
                    "dimension": scope["dimension"],
                    "seed_role": name.removeprefix("full-").rsplit("-r", 1)[0],
                    "family_id": row["family_id"],
                    "root": key[0],
                    "chunk_x": key[1],
                    "chunk_z": key[2],
                    "envelope": envelope,
                    "piece_bounds_sha256": hashlib.sha256(
                        json.dumps(geometry["piece_bounds"], separators=(",", ":")).encode()
                    ).hexdigest(),
                    "bounds": bounds,
                    "voxel_count": (bounds[3] - bounds[0] + 1)
                    * (bounds[4] - bounds[1] + 1)
                    * (bounds[5] - bounds[2] + 1),
                    "start_region": start_region,
                    "envelope_regions": regions,
                    "missing_region_inventory": [p for p in regions if p not in files],
                    "census_sha256": identity["input_sha256"],
                }
                if case_id in candidates:
                    previous = {k: v for k, v in candidates[case_id].items() if k != "strata"}
                    if previous != case:
                        raise ValueError("contradictory cross-frame start metadata")
                    candidates[case_id]["strata"].append(stratum)
                else:
                    candidates[case_id] = {**case, "strata": [stratum]}
        worlds[name] = {
            "archive_manifest_sha256": hashlib.sha256(manifest_raw).hexdigest(),
            "world_backup_sha256": entry.sha256,
            "start_regions": sorted(start_regions),
            "start_region_bytes": sum(files[p]["size_bytes"] for p in start_regions),
            "envelope_regions": [files[p] for p in sorted(needed_regions) if p in files],
            "missing_region_inventory": sorted(needed_regions - files.keys()),
            "envelope_region_bytes": sum(
                files[p]["size_bytes"] for p in needed_regions if p in files
            ),
        }
    rows = [candidates[k] for k in sorted(candidates)]
    return {
        "status": "CANDIDATES ONLY; saved membership and full chunk coverage pending",
        "intake_sha256": hashlib.sha256(intake_raw).hexdigest(),
        "worlds": worlds,
        "candidates": rows,
        "summary": {
            "candidates": len(rows),
            "families": len({r["family_id"] for r in rows}),
            "roots": len({r["root"] for r in rows}),
            "envelope_voxels_before_selection": sum(r["voxel_count"] for r in rows),
            "unique_start_region_bytes": sum(w["start_region_bytes"] for w in worlds.values()),
            "unique_envelope_region_bytes": sum(
                w["envelope_region_bytes"] for w in worlds.values()
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = enumerate_candidates()
    raw = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if len(raw) > 10 * 1024 * 1024:
        raise ValueError("candidate output exceeds predeclared budget")
    args.output.write_bytes(raw)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
