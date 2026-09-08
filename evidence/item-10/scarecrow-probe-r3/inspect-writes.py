"""Inspect the retained r3 write coordinates, not a general occurrence validator."""

import hashlib
import json
from pathlib import Path

from tools.manage_item4_environment import _world_backup_lock

from mcpack_evidence.item7_anvil import decode_region_payloads
from mcpack_evidence.item7_nbt import _packed, decode_compound_nbt

world = Path("evidence/raw/item10/probe-pair-r3-custody/world-scarecrow-probe-r3/world")
trace = Path("evidence/item-10/scarecrow-probe-r3/trace.jsonl")
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
        inputs.append({"path": path.relative_to(world).as_posix(),
                       "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        for record, payload in decode_region_payloads(path):
            if (record.chunk_x, record.chunk_z) in chunks:
                retained[record.chunk_x, record.chunk_z] = decode_compound_nbt(payload)
    observations = []
    for row in writes:
        if dimensions[row["attempt"]] != "minecraft:overworld":
            raise ValueError("This bounded inspection expects only r3 Overworld writes")
        x, y, z = row["position"]
        chunk = retained[x // 16, z // 16]
        section = next(part for part in chunk["sections"] if part["Y"] == y // 16)
        states = section["block_states"]
        palette = states["palette"]
        indices = ((0,) * 4096 if len(palette) == 1 else
                   _packed(tuple(states["data"]), 4096, max(4, (len(palette) - 1).bit_length())))
        state = palette[indices[x % 16 + 16 * (z % 16) + 256 * (y % 16)]]
        observations.append({"attempt": row["attempt"], "position": row["position"],
                             "recorded_state": row["state"], "saved_state": state,
                             "same_block_id": row["state"].split("}")[0] == "Block{" + state["Name"]})
print(json.dumps({"scope": "r3 coordinate corroboration only; not probe noninterference",
                  "trace_sha256": hashlib.sha256(trace.read_bytes()).hexdigest(),
                  "anvil_inputs": inputs, "observations": observations}, indent=2))
