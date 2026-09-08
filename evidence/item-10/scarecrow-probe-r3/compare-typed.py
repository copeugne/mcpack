"""Compare the eight retained r3 typed reader outputs and preserve their full vectors."""

import gzip
import hashlib
import json
from pathlib import Path

source = Path("evidence/raw/item10/probe-pair-r3-typed")
destination = Path("evidence/item-10/scarecrow-probe-r3")
bundle_path = destination / "typed-comparison.json.gz"
summary_path = destination / "typed-comparison.json"
if bundle_path.exists() or summary_path.exists():
    detail = "Typed comparison outputs must be absent"
    raise ValueError(detail)
selections = {
    "overworld": ("minecraft:overworld", [-31, 31, -31, 31]),
    "nether": ("minecraft:the_nether", [-15, 15, -15, 15]),
    "end-central": ("minecraft:the_end", [-15, 15, -15, 15]),
    "end-outer": ("minecraft:the_end", [81, 111, -15, 15]),
}
archive = json.loads((destination / "archive-manifest.json").read_text())
world_files = {}
for member in ("probe", "control"):
    relative = f"scarecrow-{member}-r3/world-backup.json"
    payload = (Path("evidence/raw/item10") / relative).read_bytes()
    retained = [row for row in archive["files"] if row["relative_path"] == relative]
    if (
        len(retained) != 1
        or len(payload) != retained[0]["size_bytes"]
        or hashlib.sha256(payload).hexdigest() != retained[0]["sha256"]
    ):
        detail = f"World manifest differs from retained archive: {member}"
        raise ValueError(detail)
    world_files[member] = {row["path"]: row["sha256"] for row in json.loads(payload)["world_files"]}
inputs, input_hashes, comparisons = {}, {}, []
for label, (dimension, bounds) in selections.items():
    coordinates = {
        (x, z) for x in range(bounds[0], bounds[1] + 1) for z in range(bounds[2], bounds[3] + 1)
    }
    members = []
    for member in ("probe", "control"):
        name = f"{member}-{label}.json"
        payload = (source / name).read_bytes()
        data = json.loads(payload)
        directory = {
            "minecraft:overworld": "region",
            "minecraft:the_nether": "DIM-1/region",
            "minecraft:the_end": "DIM1/region",
        }[dimension]
        expected_inputs = {
            path: digest
            for path, digest in world_files[member].items()
            if Path(path).parent.as_posix() == directory and Path(path).suffix in (".mca", ".mcc")
        }
        observed_inputs = {row["path"]: row["sha256"] for row in data["anvil_inputs"]}
        if (
            not expected_inputs
            or observed_inputs != expected_inputs
            or len(observed_inputs) != len(data["anvil_inputs"])
        ):
            detail = f"Region inputs differ from retained world manifest: {name}"
            raise ValueError(detail)
        vectors = data["generation_content"]
        indexed = {(row["chunk_x"], row["chunk_z"]): row["sha256"] for row in vectors}
        if (
            data["generation_encoding"] != "typed-nbt-v2"
            or data["dimension"] != dimension
            or data["bounds_chunks"] != bounds
            or data["full_chunks"] != len(coordinates)
            or len(vectors) != len(coordinates)
            or set(indexed) != coordinates
        ):
            detail = f"Wrong encoding or incomplete declared frame: {name}"
            raise ValueError(detail)
        inputs[name] = data
        input_hashes[name] = hashlib.sha256(payload).hexdigest()
        members.append(indexed)
    mismatches = sorted(
        position for position in coordinates if members[0][position] != members[1][position]
    )
    comparisons.append(
        {
            "selection": label,
            "dimension": dimension,
            "bounds_chunks": bounds,
            "chunks": len(coordinates),
            "mismatch_count": len(mismatches),
            "mismatch_coordinates": mismatches,
        }
    )
bundle = {"generation_encoding": "typed-nbt-v2", "inputs": inputs, "comparisons": comparisons}
payload = json.dumps(bundle, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
compressed = gzip.compress(payload, mtime=0)
with bundle_path.open("xb") as stream:
    stream.write(compressed)
summary = {
    "generation_encoding": "typed-nbt-v2",
    "input_sha256": input_hashes,
    "bundle_sha256": hashlib.sha256(compressed).hexdigest(),
    "uncompressed_sha256": hashlib.sha256(payload).hexdigest(),
    "bundle_size_bytes": len(compressed),
    "comparisons": [
        {key: value for key, value in row.items() if key != "mismatch_coordinates"}
        for row in comparisons
    ],
}
with summary_path.open("x") as stream:
    json.dump(summary, stream, indent=2)
    stream.write("\n")
