"""Inspect accepted Item 13 inputs and enumerate the unchanged canonical population."""

# pyright: standard
# ruff: noqa: D103, EM101, TRY003, INP001, E501, T201, PLR2004
from __future__ import annotations

import hashlib
import json
import shutil
import time
from collections import Counter

from tools.analyze_route_opportunities import ROOT, accepted_inputs, read_bound, verify_world
from tools.manage_item4_environment import _world_backup_lock

from mcpack_evidence.item7_archive_models import ArchiveManifest

# These localized designs still warrant topology inspection because their accepted
# descriptions identify built interiors, vertical access, arena objectives or mixed scale.
ADDITIONAL = {
    "adorabuild_structures:blackstone_bastion",
    "adorabuild_structures:blackstone_bastion_towers",
    "adorabuild_structures:buried_sand_castle",
    "adorabuild_structures:crimson_hall",
    "adorabuild_structures:dark_oak_mansion",
    "adorabuild_structures:end_house",
    "adorabuild_structures:end_raised_house",
    "adorabuild_structures:end_ship",
    "adorabuild_structures:end_temple",
    "adorabuild_structures:nether_fortress",
    "adorabuild_structures:nether_fortress_courtyard",
    "adorabuild_structures:nether_fortress_wart_house",
    "adorabuild_structures:nether_temple",
    "adorabuild_structures:ocean_temple",
    "adorabuild_structures:prison",
    "adorabuild_structures:sand_pyramid",
    "adorabuild_structures:watercraft",
    "aether:gold_dungeon",
    "betterdungeons:small_dungeon",
    "ctov:pillager_outpost",
    "minecraft:ocean_ruin",
    "minecraft:pillager_outpost",
    "repurposed_structures:outpost",
    "repurposed_structures:pyramid",
    "repurposed_structures:shipwreck",
    "repurposed_structures:temple",
    "terralith:desert_outpost",
    "terralith:underground/frosted_dungeon",
    "dungeons_arise:coliseum",
    "dungeons_arise_seven_seas:small_yacht",
    "explorations:jungle_temple",
    "explorations:slime_cave",
    "explorify:badlands_pyramid",
    "explorify:mausoleum",
    "explorify:ruins",
    "idas:nexus",
    "mes:enderkeep_courtyard",
    "mns:circle_ruin",
    "mns:giant_skull",
    "mns:medium_house",
    "mss:castle_ruin",
    "mss:castle_tower",
    "mss:mushroom",
    "mss:small_deepslate_house",
    "mss:small_tower",
    "mvs:mine_with_campsite",
    "mvs:small_pillager_tower",
    "integrated_villages:village",
    "repurposed_structures:village",
    "idas:brickhouse",
    "idas:castle",
    "idas:farmhouse",
}


def main() -> None:  # noqa: C901 - one bounded input inspection
    started = time.monotonic()
    inventory_path = ROOT / "evidence/item-8/inventory.json"
    inventory = json.loads(
        read_bound(
            inventory_path, "4f7853b7b6531f99d3f0592b2129291d2e0cf24b4ad5d1381b3883dbdcfbc52d"
        )
    )
    classifications = {}
    for line in (
        read_bound(
            ROOT / "evidence/item-9/classification.md",
            "dc78d81691401bad9fc646f1fe790b14bbf1341f595db5e6cbec9a4f1111b710",
        )
        .decode()
        .splitlines()
    ):
        parts = [part.strip() for part in line.split("|")]
        if len(parts) == 9 and parts[1] in inventory["families"]:
            classifications[parts[1]] = parts[2:8]
    if (
        set(classifications) != set(inventory["families"])
        or not classifications.keys() >= ADDITIONAL
    ):
        raise ValueError("canonical classification or supplemental population mismatch")
    worlds = []
    occurrences = {}
    for name, identity in sorted(accepted_inputs().items()):
        custody = ROOT / "evidence/raw/item10" / f"{name}-custody"
        manifest = ArchiveManifest.model_validate_json(
            read_bound(ROOT / "evidence/item-10" / name / "archive-manifest.json")
        )
        entry = next(row for row in manifest.files if row.relative_path == "world-backup.json")
        backup = json.loads(read_bound(custody / "restored-local/world-backup.json", entry.sha256))
        if backup["archive_sha256"] != next(
            row.sha256 for row in manifest.files if row.relative_path == "world.tar.gz"
        ):
            raise ValueError("nested archive identity mismatch")
        with _world_backup_lock(custody / "restored-world/world"):
            verify_world(custody / "restored-world/world", backup["world_files"])
        raw = read_bound(
            ROOT / "evidence/raw/item10" / f"{name}-analysis/all-strata.json",
            identity["input_sha256"],
        )
        census = json.loads(raw)
        for data in census["strata"].values():
            for row in data["classification"]["occurrences"]:
                family = row["family_id"]
                occurrences.setdefault(family, Counter())[
                    (
                        row.get("registry_id", "nonregistry"),
                        data["dimension"],
                        "baseline" if name.endswith("-baseline") else "omit-Sparse",
                    )
                ] += 1
        worlds.append(
            {
                "world": name,
                "world_files": len(backup["world_files"]),
                "world_bytes": sum(row["size_bytes"] for row in backup["world_files"]),
                "census_bytes": len(raw),
                "census_sha256": identity["input_sha256"],
                "status": "PASS",
            }
        )
    rows = []
    for family, data in sorted(inventory["families"].items()):
        role, confidence, flags, _groups, rationale, ambiguity = classifications[family]
        reasons = []
        if role in {"T2", "T3", "T4"}:
            reasons.append("provisional dungeon, expedition or world objective")
        if {"S", "O"} & set(flags.split(",")):
            reasons.append("existing shallow-form or oversized concern requires inspection")
        if family in ADDITIONAL:
            reasons.append(
                "localized or mixed design warrants interior, vertical, arena or hostile-variant inspection"
            )
        rows.append(
            {
                "family_id": family,
                "included": bool(reasons),
                "reason": "; ".join(reasons)
                if reasons
                else "localized non-dungeon interaction, ambient formation or civilian venue without established dungeon-scale variant in accepted evidence",
                "role": role,
                "confidence": confidence,
                "classification_rationale": rationale,
                "ambiguity": ambiguity,
                "dimension_evidence": data["dimension"],
                "registry_roots": data.get("structure_ids", []),
                "variant_evidence": f"evidence/item-8/inventory.json#/families/{family}/grouping_decision",
                "occurrences": [
                    {"root": k[0], "dimension": k[1], "arm": k[2], "count": v}
                    for k, v in sorted(occurrences.get(family, {}).items())
                ],
            }
        )
    result = {
        "status": "INTAKE ONLY; not topology or quality measurement",
        "families": rows,
        "worlds": worlds,
        "included": sum(row["included"] for row in rows),
        "excluded": sum(not row["included"] for row in rows),
    }
    output = ROOT / "evidence/item-13/intake.json"
    with output.open("x") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(
        json.dumps(
            {
                "families": len(rows),
                "included": result["included"],
                "excluded": result["excluded"],
                "included_with_no_item10_occurrence": sum(
                    row["included"] and not row["occurrences"] for row in rows
                ),
                "world_bytes": sum(row["world_bytes"] for row in worlds),
                "census_bytes": sum(row["census_bytes"] for row in worlds),
                "elapsed_seconds": time.monotonic() - started,
                "free_bytes": shutil.disk_usage(ROOT).free,
                "output_bytes": output.stat().st_size,
                "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
            }
        )
    )


if __name__ == "__main__":
    main()
