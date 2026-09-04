"""Link runtime IDs to packaged sources with uv run -m tools.build_item8_structure_inputs."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_inventory import structure_inputs
from mcpack_evidence.item8_registry import read_registry

if TYPE_CHECKING:
    from pydantic import JsonValue

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = "evidence/item-8/sources/packaged-json.json.gz"
SOURCE_SHA256 = "c7ea06de3f7cd2dedaead5c6f9ac9021ebe4d03deb007bc15dc712ddfe28a5a2"
REGISTRY_PATH = (
    "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
)
REGISTRY_SHA256 = "9d245430730173e9ce5304317a7476e7ecd4267d208b25a16a0d7b2cf3f16941"


def main() -> None:
    """Read the delivered source identities and write the deterministic relationship index."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--output", type=Path, required=True)
    output = cast("Path", parser.parse_args().output)
    for relative, digest in ((SOURCE_PATH, SOURCE_SHA256), (REGISTRY_PATH, REGISTRY_SHA256)):
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
    result = structure_inputs(read_registry(ROOT / REGISTRY_PATH), resources)
    result["inputs"] = {SOURCE_PATH: SOURCE_SHA256, REGISTRY_PATH: REGISTRY_SHA256}
    with output.open("x", encoding="utf-8") as stream:
        _ = stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
