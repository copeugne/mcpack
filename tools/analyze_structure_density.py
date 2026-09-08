"""Count registry starts directly from a complete rectangle of stopped-world chunks."""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
from pathlib import Path
from typing import cast

from tools.manage_item4_environment import _world_backup_lock

from mcpack_evidence.item7_anvil import decode_region_payloads, world_regions
from mcpack_evidence.item7_nbt import decode_compound_nbt


def spatial_summary(
    occurrences: list[dict[str, str | int]], bounds: tuple[int, int, int, int]
) -> dict[str, object]:
    """Describe fixed-grid density and boundary-censored start-chunk distances."""
    min_x, max_x, min_z, max_z = bounds
    points = [(16 * int(row["chunk_x"]) + 8, 16 * int(row["chunk_z"]) + 8) for row in occurrences]
    neighbors = []
    for index, (x, z) in enumerate(points):
        boundary = min(x - 16 * min_x, 16 * (max_x + 1) - x, z - 16 * min_z, 16 * (max_z + 1) - z)
        distance = min(
            (math.dist((x, z), other) for i, other in enumerate(points) if i != index), default=None
        )
        exact = distance is not None and distance <= boundary
        neighbors.append(
            {
                **occurrences[index],
                "nearest_observed_blocks": distance,
                "boundary_distance_blocks": boundary,
                "boundary_censored": not exact,
                "nearest_distance_lower_bound_blocks": distance if exact else boundary,
            }
        )
    cells = []
    counts = collections.Counter(
        (int(row["chunk_x"]) // 16, int(row["chunk_z"]) // 16) for row in occurrences
    )
    for cell_z in range(min_z // 16, max_z // 16 + 1):
        for cell_x in range(min_x // 16, max_x // 16 + 1):
            x0, x1 = max(min_x, cell_x * 16), min(max_x, cell_x * 16 + 15)
            z0, z1 = max(min_z, cell_z * 16), min(max_z, cell_z * 16 + 15)
            cells.append(
                {
                    "bounds_chunks": [x0, x1, z0, z1],
                    "full_chunks": (x1 - x0 + 1) * (z1 - z0 + 1),
                    "count": counts[cell_x, cell_z],
                }
            )
    full_cell_chunks = 16 * 16
    full_cells = [cell for cell in cells if cell["full_chunks"] == full_cell_chunks]
    cell_counts = [cell["count"] for cell in full_cells]
    mean = sum(cell_counts) / len(cell_counts) if cell_counts else None
    dispersion = (
        sum((count - mean) ** 2 for count in cell_counts) / len(cell_counts) / mean
        if mean
        else None
    )
    # Maximal all-zero rectangle on the fully observed 16-chunk grid.
    empty = {
        (cell["bounds_chunks"][0] // 16, cell["bounds_chunks"][2] // 16)
        for cell in full_cells
        if cell["count"] == 0
    }
    best_area, best_bounds = 0, None
    for top in range(min_z // 16, max_z // 16 + 1):
        eligible = set(range(min_x // 16, max_x // 16 + 1))
        for bottom in range(top, max_z // 16 + 1):
            eligible &= {x for x in eligible if (x, bottom) in empty}
            left = None
            for right in range(min_x // 16, max_x // 16 + 2):
                if right in eligible:
                    left = right if left is None else left
                    continue
                if left is not None:
                    area = (right - left) * (bottom - top + 1) * 256
                    rectangle = [left * 16, right * 16 - 1, top * 16, (bottom + 1) * 16 - 1]
                    if area > best_area or (area == best_area and rectangle < best_bounds):
                        best_area, best_bounds = area, rectangle
                    left = None
    distances = [row["nearest_observed_blocks"] for row in neighbors]
    return {
        "coordinate_convention": "horizontal centers of authoritative start chunks, in blocks",
        "nearest_neighbors": neighbors,
        "mean_nearest_observed_blocks": (
            sum(distances) / len(distances) if len(distances) > 1 else None
        ),
        "mean_nearest_neighbor_blocks": (
            sum(distances) / len(distances)
            if distances and all(not row["boundary_censored"] for row in neighbors)
            else None
        ),
        "mean_rule": "null if no observations or any boundary-censored neighbor; no dropped cases",
        "grid_cell_side_chunks": 16,
        "cells": cells,
        "full_cell_count": len(full_cells),
        "full_cell_variance_over_mean": dispersion,
        "full_cell_zero_fraction": len(empty) / len(full_cells) if full_cells else None,
        "largest_empty_full_cell_rectangle": {
            "area_chunks": best_area,
            "bounds_chunks": best_bounds,
        },
    }


def classify_census(result: dict[str, object]) -> dict[str, object]:
    """Join measured starts to the exact accepted inventory and provisional matrix."""
    repository = Path(__file__).resolve().parents[1]
    identities = {
        "evidence/item-8/inventory.json": (
            "4f7853b7b6531f99d3f0592b2129291d2e0cf24b4ad5d1381b3883dbdcfbc52d"
        ),
        "evidence/item-9/classification.md": (
            "dc78d81691401bad9fc646f1fe790b14bbf1341f595db5e6cbec9a4f1111b710"
        ),
    }
    contents = {}
    for name, expected in identities.items():
        contents[name] = (repository / name).read_bytes()
        if hashlib.sha256(contents[name]).hexdigest() != expected:
            detail = f"accepted classification input identity changed: {name}"
            raise ValueError(detail)
    inventory = json.loads(contents["evidence/item-8/inventory.json"])
    family_by_root = {
        root: family
        for family, data in inventory["families"].items()
        for root in data["structure_ids"]
    }
    # Reuse the accepted Item 9 table format. Exact hashes bind its reviewed coverage.
    rows = [
        [cell.strip() for cell in line.split("|")[1:-1]]
        for line in contents["evidence/item-9/classification.md"].decode().splitlines()
        if line.startswith("|")
    ][2:]
    classifications = {row[0]: row[1:] for row in rows}
    occurrences = cast("list[dict[str, str | int]]", result["occurrences"])
    full_chunks = cast("int", result["full_chunks"])
    annotated = []
    counts = dict.fromkeys(("T0", "C", "T1", "T2", "T3", "T4"), 0)
    for occurrence in occurrences:
        root = occurrence["registry_id"]
        if root not in family_by_root:
            detail = f"observed registry start is outside accepted active families: {root}"
            raise ValueError(detail)
        family = family_by_root[root]
        role, confidence, flags, groups, rationale, ambiguity = classifications[family]
        annotated.append(
            {
                **occurrence,
                "family_id": family,
                "role": role,
                "confidence": confidence,
                "flags": flags,
                "comparison_groups": groups.split(","),
                "rationale": rationale,
                "ambiguity": ambiguity,
            }
        )
        counts[role] += 1
    return {
        "scope": "registry occurrences by provisional family role; not observed combat",
        "input_sha256": identities,
        "occurrences": annotated,
        "exclusive_roles": {
            role: {"count": count, "per_1000_chunks": 1000 * count / full_chunks}
            for role, count in counts.items()
        },
    }


def start_origins(payload: bytes, chunk: tuple[int, int]) -> list[dict[str, str | int]]:
    """Require the stored start coordinates rather than infer them from a log row."""
    root = decode_compound_nbt(payload)
    starts = root.get("structures", {}).get("starts", {})
    result = []
    for identifier, start in sorted(starts.items()):
        if start["id"] == "INVALID":
            continue
        origin = (start.get("ChunkX"), start.get("ChunkZ"))
        if any(type(value) is not int for value in origin) or origin != chunk:
            detail = f"start {identifier} has missing or inconsistent authoritative chunk: {origin}"
            raise ValueError(detail)
        if start["id"] != identifier:
            detail = f"start key/id mismatch: {identifier}, {start['id']}"
            raise ValueError(detail)
        result.append({"registry_id": identifier, "chunk_x": origin[0], "chunk_z": origin[1]})
    return result


def census(
    world: Path,
    dimension: str,
    bounds: tuple[int, int, int, int],
    geometry: dict[str, tuple[int, int]],
) -> dict[str, object]:
    """Reject incomplete coverage and retain the actual denominator and occurrences."""
    min_x, max_x, min_z, max_z = bounds
    if min_x > max_x or min_z > max_z:
        detail = "bounds must be inclusive ordered min-x max-x min-z max-z"
        raise ValueError(detail)
    expected = (max_x - min_x + 1) * (max_z - min_z + 1)
    seen = set()
    occurrences = []
    inputs = []
    for path, context in world_regions(world, dimension_geometry=geometry):
        if context.dimension != dimension:
            continue
        before = hashlib.sha256(path.read_bytes()).hexdigest()
        external_inputs = {}
        for record, payload in decode_region_payloads(path, context):
            x, z = record.chunk_x, record.chunk_z
            if record.external:
                external_path = path.with_name(f"c.{x}.{z}.mcc")
                external_inputs[external_path.relative_to(world).as_posix()] = hashlib.sha256(
                    external_path.read_bytes()
                ).hexdigest()
            if not (min_x <= x <= max_x and min_z <= z <= max_z):
                continue
            if record.status != "minecraft:full" or (x, z) in seen:
                detail = f"selected chunk is incomplete or duplicated: {dimension} {x},{z}"
                raise ValueError(detail)
            seen.add((x, z))
            occurrences.extend(start_origins(payload, (x, z)))
        if hashlib.sha256(path.read_bytes()).hexdigest() != before:
            detail = f"region changed during census: {path}"
            raise ValueError(detail)
        inputs.append({"path": context.relative_path, "sha256": before})
        inputs.extend(
            {"path": name, "sha256": digest} for name, digest in sorted(external_inputs.items())
        )
    if len(seen) != expected:
        detail = f"incomplete selected coverage: {len(seen)} of {expected} full chunks"
        raise ValueError(detail)
    counts = collections.Counter(row["registry_id"] for row in occurrences)
    return {
        "scope": "registry starts only; not all-family density or observed combat",
        "dimension": dimension,
        "bounds_chunks": bounds,
        "full_chunks": len(seen),
        "total_starts": len(occurrences),
        "starts_per_1000_chunks": 1000 * len(occurrences) / len(seen),
        "registry_counts": dict(sorted(counts.items())),
        "occurrences": sorted(
            occurrences, key=lambda row: (row["registry_id"], row["chunk_x"], row["chunk_z"])
        ),
        "anvil_inputs": inputs,
    }


def main() -> None:
    """Run an offline census while holding the existing Java-compatible world lock."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("world", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--dimension", required=True)
    parser.add_argument("--bounds", type=int, nargs=4, required=True)
    parser.add_argument("--dimension-geometry", type=Path)
    parser.add_argument("--classify", action="store_true", help="join accepted Item 8/9 inputs")
    parser.add_argument("--spatial", action="store_true", help="add classified spatial summaries")
    args = parser.parse_args()
    if args.output.exists() or args.output.resolve().is_relative_to(args.world.resolve()):
        parser.error("output must be new and outside the input world")
    geometry = json.loads(args.dimension_geometry.read_text()) if args.dimension_geometry else {}
    with _world_backup_lock(args.world):
        result = census(args.world, args.dimension, tuple(args.bounds), geometry)
    if args.classify or args.spatial:
        result["classification"] = classify_census(result)
    if args.spatial:
        rows = result["classification"]["occurrences"]
        result["spatial"] = {
            role: spatial_summary(
                [row for row in rows if role == "all_registry" or row["role"] == role],
                tuple(args.bounds),
            )
            for role in ("all_registry", "T0", "C", "T1", "T2", "T3", "T4")
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
