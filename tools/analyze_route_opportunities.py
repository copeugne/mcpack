"""Read accepted Item 10 worlds for the predeclared Item 11 route analysis."""

# pyright: standard
# ruff: noqa: D103, EM101, EM102, TRY003, PLR2004
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import math
import statistics
from array import array
from pathlib import Path
from typing import Any, cast

from tools.analyze_structure_density import category_occurrences, saved_block_at
from tools.manage_item4_environment import _backup_paths, _world_backup_lock

from mcpack_evidence.item6_json import parse_strict_json
from mcpack_evidence.item7_anvil import RegionContext, decode_region_payloads
from mcpack_evidence.item7_archive_io import (
    duplicate_stream,
    open_directory,
    open_regular,
    sha256_descriptor,
)
from mcpack_evidence.item7_archive_models import ArchiveManifest
from mcpack_evidence.item7_nbt import decode_compound_nbt

ROOT = Path(__file__).resolve().parents[1]
ROUTES = {
    "east-south": (-384, -256, 1, 0),
    "east-north": (-384, 256, 1, 0),
    "south-west": (-256, -384, 0, 1),
    "south-east": (256, -384, 0, 1),
}
SPEEDS = {"walking": (4, 3, 5), "horse": (7, 5, 9), "boat": (8, 6, 10)}
RADII = (32, 64, 96)
WINDOWS = (256, 512, 768)
MISSING = -32768


def read_bound(path: Path, expected: str | None = None) -> bytes:
    with open_regular(path) as (fd, _), duplicate_stream(fd) as stream:
        data = stream.read()
    if expected is not None and hashlib.sha256(data).hexdigest() != expected:
        raise ValueError(f"input identity mismatch: {path}")
    return data


def accepted_inputs() -> dict[str, Any]:
    return cast(
        "dict[str, Any]",
        parse_strict_json(
            gzip.decompress(
                read_bound(ROOT / "evidence/item-10/accepted-biome-comparisons.json.gz")
            )
        ),
    )


def verify_world(world: Path, manifest: list[dict[str, Any]]) -> None:
    expected = {row["path"]: (row["size_bytes"], row["sha256"]) for row in manifest}
    if len(expected) != len(manifest):
        raise ValueError("duplicate world inventory member")
    # POSIX locks are released if this process closes ANY descriptor for session.lock.
    # Reuse the existing backup enumeration, which excludes that path before opening it.
    actual = {}
    with open_directory(world):
        for path in _backup_paths(world):
            if path.is_symlink():
                raise ValueError(f"world inventory contains a symlink: {path}")
            if path.is_dir():
                continue
            with open_regular(path) as (descriptor, metadata):
                actual[path.relative_to(world).as_posix()] = (
                    metadata.st_size,
                    sha256_descriptor(descriptor),
                )
    if actual != expected:
        raise ValueError("restored world differs from complete accepted inventory")


def point(route: tuple[int, int, int, int], distance: int) -> tuple[int, int]:
    x, z, dx, dz = route
    return x + dx * distance, z + dz * distance


def height_at(heights: array[int], x: int, z: int) -> int | None:
    if not (-512 <= x < 512 and -512 <= z < 512):
        return None
    value = heights[(z + 512) * 1024 + x + 512]
    return None if value == MISSING else value


def extract_geometry(  # noqa: C901 - one existing-decoder pass over the fixed region
    world: Path,
) -> tuple[array[int], dict[tuple[int, int], dict[str, Any]]]:
    """Reuse the accepted decoder and palette lookup; retain all needed top cells."""
    heights = array("h", [MISSING]) * (1024 * 1024)
    needed: set[tuple[int, int]] = set()
    for route in ROUTES.values():
        for distance in range(769):
            x, z = point(route, distance)
            needed.update((x + dx, z + dz) for dx in (-1, 0, 1) for dz in (-1, 0, 1))
    by_chunk: dict[tuple[int, int], list[tuple[int, int]]] = {}
    for x, z in sorted(needed):
        by_chunk.setdefault((x // 16, z // 16), []).append((x, z))
    tops = {}
    seen = set()
    for rx in (-1, 0):
        for rz in (-1, 0):
            relative = f"region/r.{rx}.{rz}.mca"
            context = RegionContext("minecraft:overworld", relative, -64, 384)
            for record, payload in decode_region_payloads(world / relative, context):
                key = record.chunk_x, record.chunk_z
                if key in seen or not record.full:
                    raise ValueError(f"duplicate or nonfull selected chunk: {key}")
                seen.add(key)
                maps = {row.name: row.values for row in record.heightmaps}
                if len(maps) != len(record.heightmaps) or "WORLD_SURFACE" not in maps:
                    raise ValueError(f"missing or duplicate heightmaps: {key}")
                surface = maps["WORLD_SURFACE"]
                for z in range(16):
                    start = (record.chunk_z * 16 + z + 512) * 1024 + record.chunk_x * 16 + 512
                    heights[start : start + 16] = array("h", surface[z * 16 : z * 16 + 16])
                if key in by_chunk:
                    chunk = decode_compound_nbt(payload)
                    for x, z in by_chunk[key]:
                        y = surface[(z % 16) * 16 + x % 16]
                        state = saved_block_at(chunk, (x, y, z))
                        tops[(x, z)] = {"x": x, "z": z, "height": y, "state": state}
    if len(seen) != 4096 or len(tops) != len(needed):
        raise ValueError("incomplete route geometry denominator")
    return heights, tops


def candidates(census: dict[str, Any]) -> list[dict[str, Any]]:
    boxes = {
        (r["registry_id"], r["chunk_x"], r["chunk_z"]): r["envelope"]
        for r in census["occurrence_biomes"]
    }
    rows = []
    for source in census["classification"]["occurrences"]:
        row = dict(source)
        x = row.get("anchor_x", row["chunk_x"] * 16 + 8)
        z = row.get("anchor_z", row["chunk_z"] * 16 + 8)
        if "registry_id" in row:
            box = boxes.get((row["registry_id"], row["chunk_x"], row["chunk_z"]))
            target = [(box[0] + box[3]) / 2, box[4] + 1, (box[2] + box[5]) / 2] if box else None
        else:
            target = [x, row["anchor_y"] + 1, z] if row.get("anchor_y") is not None else None
        row.update(anchor_x=x, anchor_z=z, target=target)
        row["location_id"] = (
            f"{row['registry_id']}@{row['chunk_x']},{row['chunk_z']}"
            if "registry_id" in row
            else f"nonregistry:{row['candidate_id']}"
        )
        rows.append(row)
    if len({r["location_id"] for r in rows}) != len(rows):
        raise ValueError("duplicate accepted location identity")
    return sorted(rows, key=lambda r: (r["family_id"], r["location_id"]))


def ray(heights: array[int], eye_x: int, eye_z: int, target: list[float] | None) -> str:
    surface = height_at(heights, eye_x, eye_z)
    if target is None or surface is None:
        return "UNKNOWN"
    x, y, z = target
    steps = max(1, math.ceil(math.hypot(x - eye_x, z - eye_z)))
    eye_y = surface + 2.62
    for step in range(1, steps + 1):
        f = step / steps
        h = height_at(
            heights, math.floor(eye_x + (x - eye_x) * f), math.floor(eye_z + (z - eye_z) * f)
        )
        if h is None:
            return "UNKNOWN"
        if eye_y + (y - eye_y) * f <= h + 1:
            return "OCCLUDED"
    return "RAY_CLEAR"


def route_observations(
    route: tuple[int, int, int, int], rows: list[dict[str, Any]], heights: array[int]
) -> list[dict[str, Any]]:
    observations = []
    sx, sz, dx, dz = route
    for row in rows:
        projection = min(768, max(0, (row["anchor_x"] - sx) * dx + (row["anchor_z"] - sz) * dz))
        px, pz = point(route, projection)
        lateral = math.hypot(row["anchor_x"] - px, row["anchor_z"] - pz)
        rays = []
        for distance in range(4, 768, 8):
            x, z = point(route, distance)
            target = row["target"]
            # Missing targets retain unknown tests within the anchor radius.
            tx, tz = (target[0], target[2]) if target else (row["anchor_x"], row["anchor_z"])
            separation = math.hypot(tx - x, tz - z)
            if separation <= 96:
                rays.append(
                    {
                        "distance": distance,
                        "target_distance": separation,
                        "result": ray(heights, x, z, target),
                    }
                )
        if lateral <= 96 or rays:
            observations.append(
                {**row, "projection": projection, "adjacent_distance": lateral, "rays": rays}
            )
    return observations


def model_transport(
    route: tuple[int, int, int, int], mode: str, tops: dict[tuple[int, int], dict[str, Any]]
) -> dict[str, Any]:
    failures = []
    lengths = [0.0]
    for distance in range(769):
        x, z = point(route, distance)
        top = tops[(x, z)]
        state = top["state"]
        name = state.get("Name") if state else None
        reasons = []
        if name is None:
            reasons.append("UNKNOWN_TOP_BLOCK")
        elif mode != "boat" and name in (
            "minecraft:water",
            "minecraft:lava",
            "minecraft:air",
            "minecraft:cave_air",
            "minecraft:void_air",
        ):
            reasons.append("NO_DRY_SUPPORT")
        elif mode == "boat":
            neighbors = [tops[(x + dx, z + dz)] for dx in (-1, 0, 1) for dz in (-1, 0, 1)]
            if any(t["state"] is None for t in neighbors):
                reasons.append("UNKNOWN_WATER_NEIGHBORHOOD")
            if any(
                t["state"] is not None
                and (t["state"].get("Name") != "minecraft:water" or t["height"] != top["height"])
                for t in neighbors
            ):
                reasons.append("NO_LEVEL_3X3_WATER")
        if distance:
            prior = tops[point(route, distance - 1)]
            delta = top["height"] - prior["height"]
            lengths.append(lengths[-1] + (1 if mode == "boat" else math.hypot(1, delta)))
            if abs(delta) > (0 if mode == "boat" else 1):
                reasons.append("HEIGHT_STEP_EXCEEDS_CAPABILITY")
        if reasons:
            failures.append({"distance": distance, "reasons": reasons})
    known = any(any(not r.startswith("UNKNOWN") for r in f["reasons"]) for f in failures)
    prefix = max(0, failures[0]["distance"] - 1) if failures else 768
    return {
        "status": "INFEASIBLE" if known else "UNKNOWN" if failures else "MODEL_FEASIBLE",
        "failures": failures,
        "reachable_prefix": prefix,
        "cumulative_cost_distance": lengths,
    }


def distribution(values: list[float]) -> dict[str, Any]:
    if not values:
        return {"n": 0, "median": None, "min": None, "max": None, "iqr": None}
    quarters = (
        statistics.quantiles(values, n=4, method="inclusive")
        if len(values) > 1
        else [values[0]] * 3
    )
    return {
        "n": len(values),
        "median": statistics.median(values),
        "min": min(values),
        "max": max(values),
        "iqr": quarters[2] - quarters[0],
    }


def event_summary(events: list[tuple[float, str, str]], window: int) -> dict[str, Any]:
    events = sorted(events)
    gaps = [b[0] - a[0] for a, b in itertools.pairwise(events)]
    boundaries = [events[0][0], window - events[-1][0]] if events else [window]
    seen = {}
    repeats = []
    for distance, family, identity in events:
        if family in seen:
            repeats.append(
                {
                    "family": family,
                    "location_id": identity,
                    "distance": distance,
                    "interval": distance - seen[family],
                }
            )
        seen[family] = distance
    return {
        "events": events,
        "count": len(events),
        "unique_families": len(seen),
        "gaps": gaps,
        "gap_distribution": distribution(gaps),
        "censored_boundary_gaps": boundaries,
        "maximum_empty_interval": max(gaps + boundaries),
        "repeats": repeats,
        "repeat_count": len(repeats),
        "first_repeat_distance": repeats[0]["distance"] if repeats else None,
        "no_repeat_right_censored_at": None if repeats else window,
        "repeat_interval_distribution": distribution([r["interval"] for r in repeats]),
    }


def costs(distance: float, mode: str) -> dict[str, float]:
    central, slow, fast = SPEEDS[mode]
    return {
        "central_seconds": distance / central,
        "min_seconds": distance / fast,
        "max_seconds": distance / slow,
    }


def summarize_route(
    observations: list[dict[str, Any]], transport: dict[str, Any]
) -> list[dict[str, Any]]:
    summaries = []
    visibility_categories = cast(
        "dict[str, list[dict[str, Any]]]",
        category_occurrences(observations, total_name="all_locations"),
    )
    for radius in RADII:
        for window in WINDOWS:
            adjacent = [
                r
                for r in observations
                if r["adjacent_distance"] <= radius
                and (r["projection"] < window or r["projection"] == window == 768)
            ]
            adjacent_categories = cast(
                "dict[str, list[dict[str, Any]]]",
                category_occurrences(adjacent, total_name="all_locations"),
            )
            for category, rows in visibility_categories.items():
                events = [
                    (r["projection"], r["family_id"], r["location_id"])
                    for r in adjacent_categories[category]
                ]
                visible = []
                stations = set()
                unknown = set()
                for row in rows:
                    hits = [
                        r["distance"]
                        for r in row["rays"]
                        if r["distance"] < window
                        and r["target_distance"] <= radius
                        and r["result"] == "RAY_CLEAR"
                    ]
                    unknown.update(
                        r["distance"]
                        for r in row["rays"]
                        if r["distance"] < window
                        and r["target_distance"] <= radius
                        and r["result"] == "UNKNOWN"
                    )
                    stations.update(hits)
                    if hits:
                        visible.append((min(hits), row["family_id"], row["location_id"]))
                adjacent_summary = event_summary(events, window)
                visible_summary = event_summary(visible, window)
                modes = {}
                for mode, model in transport.items():
                    prefix = min(window, model["reachable_prefix"])
                    length = model["cumulative_cost_distance"][window]
                    modes[mode] = {
                        "reachable_prefix": prefix,
                        "unconstrained_cost": costs(length, mode),
                        "completed_cost": costs(length, mode) if prefix == window else None,
                        "prefix_cost": costs(model["cumulative_cost_distance"][prefix], mode),
                        "prefix_covered_blocks": sum(8 for d in stations if d + 4 <= prefix),
                        "prefix_denominator_blocks": prefix,
                        "unconstrained_adjacent_repeat_interval_times": [
                            costs(
                                model["cumulative_cost_distance"][int(r["distance"])]
                                - model["cumulative_cost_distance"][
                                    int(r["distance"] - r["interval"])
                                ],
                                mode,
                            )
                            for r in adjacent_summary["repeats"]
                        ],
                        "unconstrained_repeat_interval_times": [
                            costs(
                                model["cumulative_cost_distance"][int(b)]
                                - model["cumulative_cost_distance"][int(b - interval)],
                                mode,
                            )
                            for b, interval in [
                                (r["distance"], r["interval"]) for r in visible_summary["repeats"]
                            ]
                        ],
                    }
                summaries.append(
                    {
                        "radius": radius,
                        "window": window,
                        "category": category,
                        "adjacent": adjacent_summary,
                        "geometric_visible": visible_summary,
                        "covered_blocks": 8 * len(stations),
                        "denominator_blocks": window,
                        "coverage_fraction": 8 * len(stations) / window,
                        "unknown_only_blocks": 8 * len(unknown - stations),
                        "modes": modes,
                    }
                )
    return summaries


def analyze(name: str, raw_root: Path) -> dict[str, Any]:
    accepted = accepted_inputs()
    if name not in accepted:
        raise ValueError("world is not in the sixteen accepted inputs")
    evidence = ROOT / "evidence/item-10" / name
    custody = raw_root / (name + "-custody")
    world = custody / "restored-world/world"
    manifest_raw = read_bound(evidence / "archive-manifest.json")
    manifest = ArchiveManifest.model_validate_json(manifest_raw)
    backup_identity = next(r for r in manifest.files if r.relative_path == "world-backup.json")
    backup_raw = read_bound(custody / "restored-local/world-backup.json", backup_identity.sha256)
    backup = cast("dict[str, Any]", parse_strict_json(backup_raw))
    world_archive = next(r for r in manifest.files if r.relative_path == "world.tar.gz")
    if backup["archive_sha256"] != world_archive.sha256:
        raise ValueError("nested world archive identity mismatch")
    source = read_bound(
        raw_root / (name + "-analysis") / "all-strata.json", accepted[name]["input_sha256"]
    )
    census = cast("dict[str, Any]", parse_strict_json(source))["strata"]["overworld"]
    if census["bounds_chunks"] != [-32, 31, -32, 31] or census["full_chunks"] != 4096:
        raise ValueError("accepted Overworld geometry differs from route protocol")
    # Check existing safe filesystem primitives before the lock helper touches its path.
    with open_directory(world):
        if (world / "session.lock").exists() or (world / "session.lock").is_symlink():
            with open_regular(world / "session.lock"):
                _ = None
    with _world_backup_lock(world):
        verify_world(world, backup["world_files"])
        heights, tops = extract_geometry(world)
        rows = candidates(census)
        routes = {}
        for label, geometry in ROUTES.items():
            observations = route_observations(geometry, rows, heights)
            transport = {mode: model_transport(geometry, mode, tops) for mode in SPEEDS}
            routes[label] = {
                "start": point(geometry, 0),
                "end": point(geometry, 768),
                "observations": observations,
                "transport": transport,
                "summaries": summarize_route(observations, transport),
            }
        verify_world(world, backup["world_files"])
    return {
        "protocol": "item11-routes-v2",
        "world": name,
        "inputs": {
            "analysis_sha256": hashlib.sha256(read_bound(Path(__file__))).hexdigest(),
            "archive_manifest_sha256": hashlib.sha256(manifest_raw).hexdigest(),
            "world_backup_sha256": backup_identity.sha256,
            "census_sha256": accepted[name]["input_sha256"],
            "protocol_sha256": hashlib.sha256(
                read_bound(ROOT / "evidence/item-11/protocol.md")
            ).hexdigest(),
        },
        "placement_categories": census["classification"]["categories"],
        "top_cells": [tops[key] for key in sorted(tops)],
        "routes": routes,
        "human_metrics": "NOT MEASURED",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True)
    parser.add_argument("--raw-root", type=Path, default=ROOT / "evidence/raw/item10")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.output.is_symlink():
        raise ValueError("output must be absent; preserve earlier results")
    result = analyze(args.name, args.raw_root)
    data = (
        json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False).encode() + b"\n"
    )
    with args.output.open("xb") as output:
        output.write(gzip.compress(data, mtime=0))
    print(
        json.dumps(
            {
                "world": args.name,
                "output_bytes": args.output.stat().st_size,
                "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
            }
        )
    )


if __name__ == "__main__":
    main()
