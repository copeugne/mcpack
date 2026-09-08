"""Count registry starts directly from a complete rectangle of stopped-world chunks."""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
from pathlib import Path

from tools.manage_item4_environment import _world_backup_lock

from mcpack_evidence.item7_anvil import decode_region_payloads, world_regions
from mcpack_evidence.item7_nbt import decode_compound_nbt


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
    args = parser.parse_args()
    if args.output.exists() or args.output.resolve().is_relative_to(args.world.resolve()):
        parser.error("output must be new and outside the input world")
    geometry = json.loads(args.dimension_geometry.read_text()) if args.dimension_geometry else {}
    with _world_backup_lock(args.world):
        result = census(args.world, args.dimension, tuple(args.bounds), geometry)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
