"""Inspect accepted Item 13 inputs and enumerate the unchanged canonical population."""

# pyright: standard
# ruff: noqa: D103, EM101, TRY003, INP001, E501, T201, PLR2004
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import time
from collections import Counter
from pathlib import Path

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


def prior_geometry(inventory):  # noqa: ANN201, ANN001, C901
    """Locate existing saved starts without mistaking envelopes for full geometry."""
    roots = {
        root: family
        for family, record in inventory["families"].items()
        for root in record.get("structure_ids", [])
    }
    found = {}
    for path in sorted((ROOT / "evidence/item-8/raw-custody").glob("*-manifest.json")):
        manifest_raw = read_bound(path)
        manifest = ArchiveManifest.model_validate_json(manifest_raw)
        entries = {row.relative_path: row for row in manifest.files}
        if "chunks.jsonl" not in entries:
            continue
        receipt_path = path.with_name(path.name.replace("-manifest.json", "-local-restore.json"))
        receipt = json.loads(read_bound(receipt_path))
        if receipt["manifest_sha256"] != hashlib.sha256(manifest_raw).hexdigest():
            raise ValueError("prior restore receipt does not match manifest")
        relative = Path(receipt["restored_target"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("prior restore target escapes repository")
        restored = ROOT / relative
        run = json.loads(read_bound(restored / "run.json", entries["run.json"].sha256))
        preflight = run["preflight"]
        if (
            preflight["retained_runtime_sha256"]
            != "4062d6179218916c703269f113663b1e078adebbf6d43a691e692d972e07ac50"
            or preflight["frozen_manifest_sha256"]
            != "2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f"
            or preflight["config_audit_sha256"]
            != "181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd"
        ):
            raise ValueError("prior capture differs from frozen input identity")
        raw = read_bound(restored / "chunks.jsonl", entries["chunks.jsonl"].sha256)
        complete = set()
        candidates = []
        for line_number, line in enumerate(raw.splitlines(), 1):
            chunk = json.loads(line)
            if chunk["full"]:
                complete.add((chunk["dimension"], chunk["chunk_x"], chunk["chunk_z"]))
            for start in chunk["structure_starts"]:
                root = start["structure_id"]
                if root not in roots or not start["boxes"]:
                    continue
                boxes = [box["bounds"] for box in start["boxes"]]
                envelope = [min(box[i] for box in boxes) for i in range(3)] + [
                    max(box[i] for box in boxes) for i in range(3, 6)
                ]
                candidates.append(
                    {
                        "family_id": roots[root],
                        "root": root,
                        "dimension": chunk["dimension"],
                        "start_chunk": [chunk["chunk_x"], chunk["chunk_z"]],
                        "start_full": chunk["full"],
                        "envelope": envelope,
                        "archive_manifest": path.relative_to(ROOT).as_posix(),
                        "decoded_line": line_number,
                        "decoded_sha256": entries["chunks.jsonl"].sha256,
                        "seed": preflight["seed"],
                    }
                )
        for candidate in candidates:
            box = candidate["envelope"]
            required = {
                (candidate["dimension"], x, z)
                for x in range(box[0] // 16, box[3] // 16 + 1)
                for z in range(box[2] // 16, box[5] // 16 + 1)
            }
            candidate["envelope_chunks"] = len(required)
            candidate["full_envelope_chunks"] = len(required & complete)
            candidate["adequacy"] = (
                "candidate for block inspection"
                if required <= complete
                else "incomplete saved envelope; cannot close topology"
            )
            family = candidate.pop("family_id")
            key = (candidate["root"], candidate["dimension"])
            by_root = found.setdefault(family, {})
            previous = by_root.get(key)
            # This is an availability index, not quality-based sample selection.
            # The raw candidate population stays in the already retained streams.
            if previous is None or (
                candidate["full_envelope_chunks"] / candidate["envelope_chunks"],
                candidate["start_full"],
            ) > (
                previous["full_envelope_chunks"] / previous["envelope_chunks"],
                previous["start_full"],
            ):
                by_root[key] = candidate
    return {family: [rows[key] for key in sorted(rows)] for family, rows in found.items()}


def main() -> None:  # noqa: C901 - one bounded input inspection
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "evidence/item-13/intake.json")
    args = parser.parse_args()
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
    prior = prior_geometry(inventory)
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
        pointer_key = family.replace("~", "~0").replace("/", "~1")
        variant_pointer = f"/families/{pointer_key}/grouping_decision"
        if "grouping_decision" not in data:
            contribution = data["contribution_id"].replace("~", "~0").replace("/", "~1")
            variant_pointer = f"/non_registry_content/contributions/{contribution}"
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
                "prior_world_candidates": prior.get(family, []),
                "variant_evidence": f"evidence/item-8/inventory.json#{variant_pointer}",
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
    output = args.output
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
