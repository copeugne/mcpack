"""Link runtime IDs to packaged sources with uv run -m tools.build_item8_structure_inputs."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_biomes import structure_biomes
from mcpack_evidence.item8_inventory import biome_tag_inputs, size_variant_groups, structure_inputs
from mcpack_evidence.item8_registry import read_registry

if TYPE_CHECKING:
    from pydantic import JsonValue

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = "evidence/item-8/sources/packaged-json-redacted.json.gz"
SOURCE_SHA256 = "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd"
REGISTRY_PATH = (
    "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
)
REGISTRY_SHA256 = "9d245430730173e9ce5304317a7476e7ecd4267d208b25a16a0d7b2cf3f16941"
BIOMES_PATH = "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_biome.txt"
BIOMES_SHA256 = "0970c5296980495640901e3ba7fd44fa90e97da4774900368fa924a263446713"


def main() -> None:
    """Read the delivered source identities and write the deterministic relationship index."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--output", type=Path, required=True)
    output = cast("Path", parser.parse_args().output)
    inputs = {
        SOURCE_PATH: SOURCE_SHA256,
        REGISTRY_PATH: REGISTRY_SHA256,
        BIOMES_PATH: BIOMES_SHA256,
    }
    for relative, digest in inputs.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            message = f"source identity mismatch: {relative}"
            raise ValueError(message)
    catalog = cast(
        "dict[str, JsonValue]", json.loads(gzip.decompress((ROOT / SOURCE_PATH).read_bytes()))
    )
    resources = catalog["resources"]
    if not isinstance(resources, list):
        message = "packaged source catalog has no resources list"
        raise TypeError(message)
    registry = read_registry(ROOT / REGISTRY_PATH)
    result = structure_inputs(registry, resources)
    result["size_variant_groups"] = size_variant_groups(registry, resources)
    tags = biome_tag_inputs(resources)
    result["biome_tags"] = tags
    constraints = structure_biomes(
        registry, resources, tags, frozenset(read_registry(ROOT / BIOMES_PATH))
    )
    result["structure_biomes"] = constraints
    result["inputs"] = dict(inputs)
    with output.open("x", encoding="utf-8") as stream:
        _ = stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    resolved = sum(
        isinstance(row, dict) and row["biomes"] is not None for row in constraints.values()
    )
    print(f"Packaged biome constraints: {resolved} resolved of {len(constraints)} registry IDs")


if __name__ == "__main__":
    main()
