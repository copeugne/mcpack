"""Count registry starts directly from a complete rectangle of stopped-world chunks."""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
from pathlib import Path
from typing import TYPE_CHECKING, cast

from tools.manage_item4_environment import _world_backup_lock

from mcpack_evidence.item7_anvil import decode_region_payloads, world_regions
from mcpack_evidence.item7_nbt import decode_compound_nbt

if TYPE_CHECKING:
    from mcpack_evidence.item7_nbt_models import ChunkRecord


def chunk_biome_column(record: ChunkRecord, min_y: int, height: int) -> dict[int, str]:
    """Read each saved quart-height biome at local block X=8, Z=8."""
    sections = {section.section_y: section for section in record.biome_sections}
    if len(sections) != len(record.biome_sections):
        detail = f"duplicate biome section at chunk {record.chunk_x},{record.chunk_z}"
        raise ValueError(detail)
    column = {}
    section_quarts = 4**3
    for section_y in range(min_y // 16, (min_y + height) // 16):
        section = sections.get(section_y)
        if (
            section is None
            or len(section.indices) != section_quarts
            or any(not 0 <= index < len(section.palette) for index in section.indices)
        ):
            detail = (
                f"missing or invalid biome section {section_y} at {record.chunk_x},{record.chunk_z}"
            )
            raise ValueError(detail)
        for local_quart_y in range(4):
            # Minecraft palette order is X + 4*Z + 16*Y; X=Z=2 in quart coordinates.
            column[section_y * 4 + local_quart_y] = section.palette[
                section.indices[2 + 4 * 2 + 16 * local_quart_y]
            ]
    return column


def occurrence_biomes(record: ChunkRecord, column: dict[int, str]) -> list[dict[str, object]]:
    """Attribute starts at chunk center and the midpoint of their complete piece envelope."""
    rows = []
    for start in record.structure_starts:
        if start.start_id == "INVALID":
            continue
        boxes = [box.bounds for box in start.boxes]
        if any(box[axis] > box[axis + 3] for box in boxes for axis in range(3)):
            detail = "inverted structure piece bounds"
            raise ValueError(detail)
        envelope = (
            [min(box[i] for box in boxes) for i in range(3)]
            + [max(box[i] for box in boxes) for i in range(3, 6)]
            if boxes
            else None
        )
        anchor_y = (envelope[1] + envelope[4]) // 2 if envelope else None
        quart_y = anchor_y // 4 if anchor_y is not None else None
        biome = column.get(quart_y) if quart_y is not None else None
        rows.append(
            {
                "registry_id": start.structure_id,
                "chunk_x": record.chunk_x,
                "chunk_z": record.chunk_z,
                "piece_bounds": boxes,
                "envelope": envelope,
                "anchor_x": 16 * record.chunk_x + 8,
                "anchor_y": anchor_y,
                "anchor_z": 16 * record.chunk_z + 8,
                "quart_y": quart_y,
                "biome": biome,
                "unavailable_reason": (
                    "no stored piece bounds"
                    if not boxes
                    else "anchor outside stored biome height"
                    if biome is None
                    else None
                ),
            }
        )
    return rows


def generation_digest(payload: bytes) -> str:
    """Hash the predeclared generation projection without tick or entity movement state."""
    root = decode_compound_nbt(payload)
    projection = {
        "sections": sorted(
            (
                {key: row[key] for key in ("Y", "block_states", "biomes") if key in row}
                for row in root["sections"]
            ),
            key=lambda row: row["Y"],
        ),
        "block_entities": sorted(
            root.get("block_entities", []), key=lambda row: (row["x"], row["y"], row["z"])
        ),
        "structures": root["structures"],
    }
    encoded = json.dumps(projection, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(encoded.encode()).hexdigest()


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


def census(  # noqa: C901, PLR0913 - keep optional metrics in the existing single census pass.
    world: Path,
    dimension: str,
    bounds: tuple[int, int, int, int],
    geometry: dict[str, tuple[int, int]],
    *,
    include_biomes: bool = False,
    include_generation: bool = False,
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
    biome_counts = collections.Counter()
    attributed_biomes = []
    generation = []
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
            if include_biomes:
                column = chunk_biome_column(record, context.min_y, context.build_height)
                biome_counts.update(column.items())
                attributed_biomes.extend(occurrence_biomes(record, column))
            occurrences.extend(start_origins(payload, (x, z)))
            generation.extend(
                [{"chunk_x": x, "chunk_z": z, "sha256": generation_digest(payload)}]
                if include_generation
                else []
            )
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
    result = {
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
    exposure = {
        "scope": "saved chunk-center column biomes; separate quart-height denominators",
        "local_block_xz": [8, 8],
        "rows": [
            {"quart_y": quart_y, "biome": biome, "full_chunks": count}
            for (quart_y, biome), count in sorted(biome_counts.items())
        ],
    }
    return (
        result
        | (
            {"biome_exposure": exposure, "occurrence_biomes": attributed_biomes}
            if include_biomes
            else {}
        )
        | (
            {
                "generation_content": sorted(
                    generation, key=lambda row: (row["chunk_x"], row["chunk_z"])
                )
            }
            if include_generation
            else {}
        )
    )


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
    parser.add_argument(
        "--biomes", action="store_true", help="retain biome exposure by quart height"
    )
    parser.add_argument("--generation", action="store_true", help="hash declared generated content")
    args = parser.parse_args()
    if args.output.exists() or args.output.resolve().is_relative_to(args.world.resolve()):
        parser.error("output must be new and outside the input world")
    geometry = json.loads(args.dimension_geometry.read_text()) if args.dimension_geometry else {}
    with _world_backup_lock(args.world):
        result = census(
            args.world,
            args.dimension,
            tuple(args.bounds),
            geometry,
            include_biomes=args.biomes,
            include_generation=args.generation,
        )
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
