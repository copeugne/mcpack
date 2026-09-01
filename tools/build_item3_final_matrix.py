#!/usr/bin/env python3
"""Merge Item 3 primary, static, overlap, and runtime evidence into final dispositions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

RUNTIME_DISABLED = {
    "sable-neoforge-1.21.1-2.0.1.jar": (
        "post-ready GameTest activity prevented clean command processing"
    ),
    "create-aeronautics-bundled-1.21.1-1.3.0.jar": "requires disabled Sable runtime",
    "everycomp-1.21-2.11.44-neoforge.jar": "default watchdog terminated creative-tab construction",
}
DEPENDENCY_QUARANTINED = {
    "simplymore-forge-1.2.3.jar": "requires SimplyTooltips, which is server-unsupported upstream",
}


def main() -> None:
    """Build the final matrix from explicit input evidence paths."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--static", type=Path, required=True)
    parser.add_argument("--retained-static", type=Path, required=True)
    parser.add_argument("--overlap", type=Path, required=True)
    parser.add_argument("--retained", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = _by_filename(_load(args.source)["candidates"])
    static = _by_filename(_load(args.static)["candidates"])
    retained_static = _by_filename(_load(args.retained_static)["candidates"])
    overlap = _load(args.overlap)
    retained = set(args.retained.read_text(encoding="utf-8").splitlines())
    overlap_by_candidate = _overlap_by_candidate(overlap)
    rows = [
        _row(
            filename,
            source[filename],
            retained_static[filename] if filename in retained else static[filename],
            overlap_by_candidate,
            retained,
        )
        for filename in sorted(source)
    ]
    result = {
        "schema_version": "item3-final-compatibility-matrix-v1",
        "target": {
            "minecraft": "1.21.1",
            "neoforge": "21.1.249",
            "physical_side": "dedicated_server",
        },
        "candidate_count": len(rows),
        "rows": rows,
        "limitations": [
            "Retained means dedicated-server admission, not client-join or gameplay proof.",
            (
                "Publisher side labels supplement but do not replace packaged metadata "
                "and runtime evidence."
            ),
            (
                "Item 4 and later own deterministic environment, gameplay, world-generation, "
                "and performance validation."
            ),
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    _ = args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")


def _row(
    filename: str,
    source: dict[str, Any],
    static: dict[str, Any],
    overlaps: dict[str, list[str]],
    retained: set[str],
) -> dict[str, Any]:
    project = source["project"]
    disposition, rationale, confidence = _disposition(filename, project, static, retained)
    hazards = list(static["hazard_flags"])
    lower = filename.casefold()
    if "forge" in lower and "neoforge" not in lower:
        hazards.append("forge_label_under_neoforge")
    if "1.21.x" in lower or ("1.21.1" not in lower and "1.21" in lower):
        hazards.append("broad_or_other_point_release_filename")
    hazards.extend(overlaps.get(filename, []))
    return {
        "candidate_filename": filename,
        "platform": source["platform"],
        "project_id": source["project"]["project_id"],
        "version_id": source["version"]["version_id"],
        "version_number": source["version"]["version_number"],
        "artifact": source["artifact"],
        "declared_game_versions": source["declared"]["game_versions"],
        "declared_loaders": source["declared"]["loaders"],
        "publisher_environment": {
            "client": project["client_side"],
            "server": project["server_side"],
        },
        "physical_side_classification": _side(project),
        "active_metadata_paths": static["active_metadata_paths"],
        "inactive_metadata_paths": static["inactive_metadata_paths"],
        "provided_mods": static["provided_mods"],
        "loader_checks": static["loader_checks"],
        "minecraft_checks": static["minecraft_checks"],
        "neoforge_checks": static["neoforge_checks"],
        "dependency_checks": static["dependency_checks"],
        "hazard_flags": sorted(set(hazards)),
        "static_status": static["static_status"],
        "final_disposition": disposition,
        "rationale": rationale,
        "confidence": confidence,
        "runtime_evidence": "evidence/item-3/runtime/runtime-cluster-evidence.json"
        if filename in retained or filename in RUNTIME_DISABLED
        else None,
        "limitations": static["missing_runtime_evidence"]
        if filename not in retained and filename not in RUNTIME_DISABLED
        else [],
    }


def _disposition(  # noqa: PLR0911
    filename: str, project: dict[str, Any], static: dict[str, Any], retained: set[str]
) -> tuple[str, str, str]:
    if filename in retained:
        return (
            "retained_server",
            (
                "exact static checks pass and the 136-candidate server cluster passed "
                "first boot and restart"
            ),
            "high",
        )
    if filename in RUNTIME_DISABLED:
        return "disabled_runtime_failure", RUNTIME_DISABLED[filename], "high"
    if filename in DEPENDENCY_QUARANTINED:
        return "quarantined_dependency", DEPENDENCY_QUARANTINED[filename], "high"
    if static["static_status"] == "incompatible":
        return "quarantined_static_failure", "required dependency closure fails", "high"
    if project["server_side"] == "unsupported":
        return (
            "disabled_client_only",
            "publisher marks the exact version unsupported on servers",
            "high",
        )
    if filename.endswith(".disabled"):
        return (
            "disabled_inventory_state",
            "candidate was supplied disabled and is unnecessary on the dedicated server",
            "high",
        )
    return (
        "disabled_not_required_on_server",
        "server-optional or unknown candidate is not required by the retained dependency closure",
        "medium",
    )


def _side(project: dict[str, Any]) -> str:
    client, server = project["client_side"], project["server_side"]
    if server == "unsupported":
        return "client_only"
    if client == "unsupported":
        return "server_only"
    if server == "required":
        return "shared_or_server_required"
    return "optional_or_unknown"


def _overlap_by_candidate(report: dict[str, Any]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for group in report["coordinate_groups"]:
        for occurrence in group["occurrences"]:
            result.setdefault(occurrence["candidate_filename"], []).extend(
                f"embedded_{classification}:{group['identifier']}"
                for classification in group["classifications"]
            )
    for collision in report["mod_id_collisions"]:
        for provider in collision["providers"]:
            candidate = provider.split(":", 1)[1].split("!/", 1)[0]
            result.setdefault(candidate, []).append(
                f"nested_mod_id_collision:{collision['mod_id']}"
            )
    return result


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _by_filename(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {row["candidate_filename"]: row for row in rows}


if __name__ == "__main__":
    main()
