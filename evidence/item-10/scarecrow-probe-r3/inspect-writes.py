"""Inspect the retained r3 write coordinates, not a general occurrence validator."""

import hashlib
import json
from pathlib import Path

from tools.manage_item4_environment import _world_backup_lock
from tools.validate_item10_trace import validate_trace

from mcpack_evidence.item7_anvil import decode_region_payloads
from mcpack_evidence.item7_nbt import _packed, decode_compound_nbt

world = Path("evidence/raw/item10/probe-pair-r3-custody/world-scarecrow-probe-r3/world")
trace = Path("evidence/item-10/scarecrow-probe-r3/trace.jsonl")
validate_trace(trace)
manifest_path = Path("evidence/raw/item10/scarecrow-probe-r3/world-backup.json")
manifest_bytes = manifest_path.read_bytes()
archive = json.loads(trace.with_name("archive-manifest.json").read_text())
member = [
    row
    for row in archive["files"]
    if row["relative_path"] == "scarecrow-probe-r3/world-backup.json"
]
if (
    len(member) != 1
    or len(manifest_bytes) != member[0]["size_bytes"]
    or hashlib.sha256(manifest_bytes).hexdigest() != member[0]["sha256"]
):
    detail = "World manifest differs from the retained archive"
    raise ValueError(detail)
world_files = {row["path"]: row["sha256"] for row in json.loads(manifest_bytes)["world_files"]}
rows = [json.loads(line) for line in trace.read_text().splitlines()]
dimensions = {row["attempt"]: row["dimension"] for row in rows if row["kind"] == "begin"}
writes = [row for row in rows if row["kind"] == "write"]
chunks = {(row["position"][0] // 16, row["position"][2] // 16) for row in writes}
regions = {(x // 32, z // 32) for x, z in chunks}
retained = {}
inputs = []
with _world_backup_lock(world):
    for x, z in sorted(regions):
        path = world / "region" / f"r.{x}.{z}.mca"
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
            if (record.chunk_x, record.chunk_z) in chunks:
                retained[record.chunk_x, record.chunk_z] = decode_compound_nbt(payload)
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            detail = f"Region changed during inspection: {relative}"
            raise ValueError(detail)
    observations = []
    for row in writes:
        if dimensions[row["attempt"]] != "minecraft:overworld":
            detail = "This bounded inspection expects only r3 Overworld writes"
            raise ValueError(detail)
        x, y, z = row["position"]
        chunk = retained[x // 16, z // 16]
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
                "position": row["position"],
                "recorded_state": row["state"],
                "saved_state": state,
                "same_block_id": row["state"].split("}")[0] == "Block{" + state["Name"],
            }
        )
print(  # noqa: T201
    json.dumps(
        {
            "scope": "r3 coordinate corroboration only; not probe noninterference",
            "trace_sha256": hashlib.sha256(trace.read_bytes()).hexdigest(),
            "anvil_inputs": inputs,
            "observations": observations,
        },
        indent=2,
    )
)
expected_writes = 30
if len(observations) != expected_writes or not all(row["same_block_id"] for row in observations):
    detail = "Retained r3 corroboration requires all 30 recorded block IDs to match"
    raise ValueError(detail)
