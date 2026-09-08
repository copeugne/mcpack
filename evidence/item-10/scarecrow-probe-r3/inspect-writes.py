"""Inspect retained scarecrow or BOP write coordinates, not general occurrences."""
# ruff: noqa: INP001

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

from tools.manage_item4_environment import _world_backup_lock
from tools.validate_item10_trace import validate_feature_trace, validate_trace

from mcpack_evidence.item7_anvil import decode_region_payloads
from mcpack_evidence.item7_nbt import _packed, decode_compound_nbt

urn = sys.argv[1:] == ["--urn-r1"]
spike = sys.argv[1:] == ["--spike-r1"]
monster = sys.argv[1:] == ["--monster-r1"]
bop = sys.argv[1:] == ["--bop-r1"]
feature_mode = bop or monster or spike or urn
if sys.argv[1:] and not feature_mode:
    detail = "Supported inspection modes are --bop-r1, --monster-r1, --spike-r1 and --urn-r1"
    raise ValueError(detail)
if feature_mode:
    diagnostic = (
        "urn-pilot-r1"
        if urn
        else "nether-spike-pilot-r1"
        if spike
        else "monster-box-pilot-r1"
        if monster
        else "bop-fixture-r1"
    )
    raw = Path("evidence/raw/item10") / (diagnostic + "-custody") / "restored"
    world = raw.parent / "restored-world/world"
    trace = raw / "trace.jsonl"
    validated = validate_feature_trace(
        raw, mode="urn" if urn else "spike" if spike else "monster" if monster else "bop"
    )
    manifest_path = raw / "world-backup.json"
    archive_path = Path("evidence/item-10") / diagnostic / "archive-manifest.json"
    manifest_member = "world-backup.json"
    dimension = "minecraft:overworld" if monster else "minecraft:the_end"
    region_dir = "region" if monster else "DIM1/region"
else:
    world = Path("evidence/raw/item10/probe-pair-r3-custody/world-scarecrow-probe-r3/world")
    trace = Path("evidence/item-10/scarecrow-probe-r3/trace.jsonl")
    validated = validate_trace(trace)
    manifest_path = Path("evidence/raw/item10/scarecrow-probe-r3/world-backup.json")
    archive_path = trace.with_name("archive-manifest.json")
    manifest_member = "scarecrow-probe-r3/world-backup.json"
    dimension = "minecraft:overworld"
    region_dir = "region"
manifest_bytes = manifest_path.read_bytes()
archive = json.loads(archive_path.read_text())
member = [row for row in archive["files"] if row["relative_path"] == manifest_member]
if (
    len(member) != 1
    or len(manifest_bytes) != member[0]["size_bytes"]
    or hashlib.sha256(manifest_bytes).hexdigest() != member[0]["sha256"]
):
    detail = "World manifest differs from the retained archive"
    raise ValueError(detail)
world_files = {row["path"]: row["sha256"] for row in json.loads(manifest_bytes)["world_files"]}
trace_bytes = trace.read_bytes()
if hashlib.sha256(trace_bytes).hexdigest() != validated["sha256"]:
    detail = "Trace changed after identity validation"
    raise ValueError(detail)
rows = [json.loads(line) for line in trace_bytes.splitlines()]
dimensions = {row["attempt"]: row["dimension"] for row in rows if row["kind"] == "begin"}
writes = [row for row in rows if row["kind"] == "write"]
dimension_dirs = {dimension: region_dir}
if spike or urn:
    dimension_dirs = {
        "minecraft:overworld": "region",
        "minecraft:the_nether": "DIM-1/region",
        "minecraft:the_end": "DIM1/region",
    }
chunks = {
    (dimensions[row["attempt"]], row["position"][0] // 16, row["position"][2] // 16)
    for row in writes
}
regions = {(dim, x // 32, z // 32) for dim, x, z in chunks}
retained = {}
inputs = []
with _world_backup_lock(world):
    for dim, x, z in sorted(regions):
        path = world / dimension_dirs[dim] / f"r.{x}.{z}.mca"
        if not path.resolve().is_relative_to(world.resolve()):
            detail = "Region escapes restored world"
            raise ValueError(detail)
        relative = path.relative_to(world).as_posix()
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != world_files.get(relative):
            detail = f"Region differs from retained world: {relative}"
            raise ValueError(detail)
        inputs.append({"path": path.relative_to(world).as_posix(), "sha256": digest})
        for record, payload in decode_region_payloads(path):
            if record.external:
                detail = "Unexpected external chunk in bounded r3 corroboration"
                raise ValueError(detail)
            if (dim, record.chunk_x, record.chunk_z) in chunks:
                chunk = decode_compound_nbt(payload)
                if (chunk.get("xPos"), chunk.get("zPos")) != (record.chunk_x, record.chunk_z):
                    detail = "Stored chunk coordinates differ from region slot"
                    raise ValueError(detail)
                retained[dim, record.chunk_x, record.chunk_z] = chunk
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            detail = f"Region changed during inspection: {relative}"
            raise ValueError(detail)
    observations = []
    for row in writes:
        if dimensions[row["attempt"]] not in dimension_dirs:
            detail = "Write dimension differs from selected bounded inspection"
            raise ValueError(detail)
        x, y, z = row["position"]
        chunk = retained[dimensions[row["attempt"]], x // 16, z // 16]
        section = next(part for part in chunk["sections"] if part["Y"] == y // 16)
        states = section["block_states"]
        palette = states["palette"]
        indices = (
            (0,) * 4096
            if len(palette) == 1
            else _packed(tuple(states["data"]), 4096, max(4, (len(palette) - 1).bit_length()))
        )
        state = palette[indices[x % 16 + 16 * (z % 16) + 256 * (y % 16)]]
        observations.append(
            {
                "attempt": row["attempt"],
                **({"dimension": dimensions[row["attempt"]]} if spike or urn else {}),
                "returned": row["returned"],
                "position": row["position"],
                "recorded_state": row["state"],
                "saved_state": state,
                "chunk_status": chunk["Status"],
                "same_block_id": row["state"].split("}")[0] == "Block{" + state["Name"],
            }
        )
result = {
    "scope": "coordinate block-ID corroboration only; not full-state equality or noninterference",
    "trace_sha256": hashlib.sha256(trace_bytes).hexdigest(),
    "anvil_inputs": inputs,
}
if feature_mode:
    successful = [row for row in observations if row["returned"]]
    last = {(dimensions[row["attempt"]], *row["position"]): row for row in successful}
    attempt_counts = Counter(row["attempt"] for row in successful)
    features = {row["attempt"]: row["class"] for row in rows if row["kind"] == "feature"}
    returns = {
        row["attempt"]: row.get("returned")
        for row in rows
        if row["kind"] in {"end", "generator_end"}
    }
    result.update(
        {
            "recorded_writes": len(observations),
            "successful_writes": len(successful),
            "refused_writes": len(observations) - len(successful),
            "unique_successful_coordinates": len(last),
            "successful_write_chunk_statuses": dict(
                Counter(row["chunk_status"] for row in successful)
            ),
            "repeated_coordinate_writes": len(successful) - len(last),
            "successful_writes_matching_saved_block_id": sum(
                row["same_block_id"] for row in successful
            ),
            "last_recorded_writes_matching_saved_block_id": sum(
                row["same_block_id"] for row in last.values()
            ),
            "attempts": [
                {
                    "attempt": attempt,
                    **({"dimension": dimensions[attempt]} if spike or urn else {}),
                    "feature": features[attempt],
                    "returned": returns[attempt],
                    "successful_writes": attempt_counts[attempt],
                    "matching_saved_block_id": sum(
                        row["same_block_id"] for row in successful if row["attempt"] == attempt
                    ),
                }
                for attempt in sorted(dimensions)
            ],
            "last_recorded_write_mismatches": [
                row for row in last.values() if not row["same_block_id"]
            ],
        }
    )
    if urn:
        # The archive-bound trace retains every attempt; do not duplicate its mixed population.
        result.pop("attempts")
        parents = {
            row["attempt"]: row["placed_feature"] for row in rows if row["kind"] == "urn_parent"
        }
        urn_observations = [row for row in observations if row["attempt"] in parents]
        urn_success = [row for row in urn_observations if row["returned"]]
        coordinates = Counter(tuple(row["position"]) for row in urn_success)
        result["urn_capture"] = {
            "scope": "all captured urn writes including halo; not selected-area cache density",
            "successful_writes": len(urn_success),
            "successful_patch_attempts": len({row["attempt"] for row in urn_success}),
            "zero_successful_write_patch_attempts": len(parents)
            - len({row["attempt"] for row in urn_success}),
            "unique_successful_coordinates": len(coordinates),
            "repeated_coordinates": [
                list(pos) for pos, count in sorted(coordinates.items()) if count > 1
            ],
            "chunk_statuses": dict(Counter(row["chunk_status"] for row in urn_success)),
            "observations": [
                {**row, "parent": parents[row["attempt"]]} for row in urn_observations
            ],
        }
else:
    result["observations"] = observations
print(json.dumps(result, indent=2))  # noqa: T201
if feature_mode and result["last_recorded_write_mismatches"]:
    detail = "BOP last recorded successful writes disagree with saved block IDs"
    raise ValueError(detail)
expected_writes = 30
if not feature_mode and (
    len(observations) != expected_writes or not all(row["same_block_id"] for row in observations)
):
    detail = "Retained r3 corroboration requires all 30 recorded block IDs to match"
    raise ValueError(detail)
