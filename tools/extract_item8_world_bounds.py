"""Extract Item 7 bounds with uv run -m tools.extract_item8_world_bounds."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item7_nbt_models import ChunkRecord
from mcpack_evidence.item8_world_bounds import observed_bounds

if TYPE_CHECKING:
    from pydantic import JsonValue

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "evidence/item-7/archive/r14/core-manifest.json"
MANIFEST_SHA256 = "669b6b0c3294e051169059fb349366e7d74fec73859432a26983916a96b29b19"
SEEDS = {
    "ordinary": 42,
    "mountainous": 6671238423019257953,
    "ocean-heavy": 95920844204830198,
    "biome-diverse": -3503646078644842058,
}


def main() -> None:
    """Bind eight retained decoded streams to the delivered raw archive manifest."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--core", type=Path, required=True)
    _ = parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    core, output = cast("Path", args.core), cast("Path", args.output)
    raw_manifest = (ROOT / MANIFEST).read_bytes()
    if hashlib.sha256(raw_manifest).hexdigest() != MANIFEST_SHA256:
        message = "Item 7 archive manifest identity changed"
        raise ValueError(message)
    manifest = cast("dict[str, JsonValue]", json.loads(raw_manifest))
    files = cast("list[dict[str, JsonValue]]", manifest["files"])
    identities = {str(row["relative_path"]): row for row in files}
    inputs: list[JsonValue] = []
    observations: list[JsonValue] = []
    for run in ("run-a", "run-b"):
        for label, seed in SEEDS.items():
            relative = f"{run}/{label}/chunks.jsonl"
            source = core / relative
            identity = identities[relative]
            with source.open("rb") as stream:
                digest = hashlib.file_digest(stream, "sha256").hexdigest()
            if digest != identity["sha256"] or source.stat().st_size != identity["size_bytes"]:
                message = f"restored Item 7 decoded source mismatch: {relative}"
                raise ValueError(message)
            inputs.append(identity)
            with source.open("rb") as stream:
                for number, raw in enumerate(stream, 1):
                    record = ChunkRecord.model_validate_json(raw)
                    for observation in observed_bounds(record):
                        row = cast("dict[str, JsonValue]", observation)
                        row.update(source=relative, line=number, run=run, seed=seed)
                        observations.append(row)
    result: dict[str, JsonValue] = {
        "manifest": MANIFEST,
        "manifest_sha256": MANIFEST_SHA256,
        "inputs": inputs,
        "scope": "piece envelopes of saved starts; chunk status retained; not occupied volume",
        "observations": observations,
    }
    payload = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode()
    with output.open("xb") as stream:
        _ = stream.write(gzip.compress(payload, mtime=0))
    print(f"Retained {len(observations)} start observations from {len(inputs)} decoded sources")


if __name__ == "__main__":
    main()
