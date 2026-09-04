"""Extract safe pack/dimension metadata with uv run -m tools.extract_item8_world_context."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item7_nbt import decode_compound_nbt

if TYPE_CHECKING:
    from pydantic import JsonValue

ROOT = Path(__file__).resolve().parents[1]


def world_context(raw: bytes) -> dict[str, JsonValue]:
    """Select worldgen fields without publishing players or unrelated operational metadata."""
    data = decode_compound_nbt(gzip.decompress(raw)).get("Data")
    if not isinstance(data, dict):
        message = "level.dat has no Data compound"
        raise TypeError(message)
    generation = data.get("WorldGenSettings")
    packs = data.get("DataPacks")
    version = data.get("Version")
    if (
        not isinstance(generation, dict)
        or generation.get("seed") != 42  # noqa: PLR2004 - frozen ordinary seed.
        or not isinstance(packs, dict)
        or not isinstance(version, dict)
        or version.get("Name") != "1.21.1"
    ):
        message = "world metadata does not match the ordinary-seed frozen registry capture"
        raise ValueError(message)
    return {
        "level_dat_sha256": hashlib.sha256(raw).hexdigest(),
        "DataVersion": data.get("DataVersion"),
        "Version": version,
        "DataPacks": packs,
        "WorldGenSettings": generation,
    }


def main() -> None:
    """Extract from the stopped Item 8 registry instance and record the source identity."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--level", type=Path, required=True)
    _ = parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = cast("Path", args.level)
    output = cast("Path", args.output)
    result = world_context(source.read_bytes())
    capture = ROOT / "evidence/item-8/runtime/registry-r1/capture.json"
    result["registry_capture_sha256"] = hashlib.sha256(capture.read_bytes()).hexdigest()
    with output.open("x", encoding="utf-8") as stream:
        _ = stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
