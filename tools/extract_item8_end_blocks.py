"""Project central-End block evidence from the retained ordinary run-a world."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item7_anvil import (
    _chunk_payload,  # pyright: ignore[reportPrivateUsage]
    _slots,  # pyright: ignore[reportPrivateUsage]
)
from mcpack_evidence.item7_nbt import (
    _packed,  # pyright: ignore[reportPrivateUsage]
    decode_compound_nbt,
)

if TYPE_CHECKING:
    from pydantic import JsonValue

MANIFEST = Path("evidence/item-7/archive/r14/run-a-worlds-manifest.json")
MANIFEST_SHA256 = "731a0c421d3c228b3875716c4b5f06e1e040e96e4851e8b1c0fe62ceff2e19e8"


def section_counts(section: dict[str, JsonValue]) -> dict[str, int]:
    """Decode actual palette use, rather than counting unused palette entries."""
    states = cast("dict[str, JsonValue]", section["block_states"])
    palette = cast("list[dict[str, JsonValue]]", states["palette"])
    if not palette:
        message = "empty block palette"
        raise ValueError(message)
    if len(palette) == 1:
        indices = (0,) * 4096
    else:
        values = tuple(cast("list[int]", states["data"]))
        indices = _packed(values, 4096, max(4, (len(palette) - 1).bit_length()))
    if any(index >= len(palette) for index in indices):
        message = "block palette index is out of range"
        raise ValueError(message)
    return dict(sorted(Counter(str(palette[index]["Name"]) for index in indices).items()))


def main() -> None:
    """Read four archived regions and retain only chunks covering X/Z -64..63."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--restored-run-a", type=Path, required=True)
    _ = parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root, output = cast("Path", args.restored_run_a), cast("Path", args.output)
    raw = MANIFEST.read_bytes()
    if hashlib.sha256(raw).hexdigest() != MANIFEST_SHA256:
        message = "retained run-a world manifest changed"
        raise ValueError(message)
    manifest = cast("dict[str, JsonValue]", json.loads(raw))
    files = cast("list[dict[str, JsonValue]]", manifest["files"])
    identities = {str(row["relative_path"]): row for row in files}
    inputs: list[JsonValue] = []
    chunks: list[JsonValue] = []
    for rx, rz in ((-1, -1), (-1, 0), (0, -1), (0, 0)):
        relative = f"run-a-ordinary/world/DIM1/region/r.{rx}.{rz}.mca"
        path = root / relative
        identity = identities[relative]
        if (path.stat().st_size != identity["size_bytes"]
                or hashlib.sha256(path.read_bytes()).hexdigest() != identity["sha256"]):
            message = f"archived region identity mismatch: {relative}"
            raise ValueError(message)
        inputs.append(identity)
        with path.open("rb") as stream:
            for slot in _slots(path, stream):
                x, z = rx * 32 + slot.index % 32, rz * 32 + slot.index // 32
                if not (-4 <= x <= 3 and -4 <= z <= 3):  # noqa: PLR2004 - fixed survey box.
                    continue
                payload, _, external = _chunk_payload(path, stream, slot)
                if external:
                    message = "external chunk needs its own manifest binding"
                    raise ValueError(message)
                chunk = decode_compound_nbt(payload)
                if (chunk["xPos"], chunk["zPos"]) != (x, z):
                    message = "chunk coordinates disagree with region slot"
                    raise ValueError(message)
                sections = cast("list[dict[str, JsonValue]]", chunk["sections"])
                entities = cast("list[dict[str, JsonValue]]", chunk["block_entities"])
                chunks.append({
                    "region": relative, "slot": slot.index, "chunk_x": x, "chunk_z": z,
                    "status": chunk["Status"], "data_version": chunk["DataVersion"],
                    "sections": cast("JsonValue", [
                        {"y": section["Y"], "block_counts": section_counts(section)}
                        for section in sections if "block_states" in section
                    ]),
                    "block_entities": [
                        {key: entity[key] for key in ("id", "x", "y", "z")}
                        for entity in entities
                    ],
                })
    result = {
        "manifest": str(MANIFEST), "manifest_sha256": MANIFEST_SHA256, "inputs": inputs,
        "scope": "central End, seed 42 run-a, X/Z -64..63; counts are not family attribution",
        "chunks": chunks,
    }
    with output.open("x", encoding="utf-8") as stream:
        _ = stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
