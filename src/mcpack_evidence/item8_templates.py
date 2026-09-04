"""Decode template attributes without treating pieces as assembled structures."""

from __future__ import annotations

import gzip
from collections import Counter
from typing import TYPE_CHECKING

from .item7_nbt import decode_compound_nbt

if TYPE_CHECKING:
    from pydantic import JsonValue


def template_summary(raw: bytes) -> dict[str, JsonValue]:
    """Preserve geometry, palettes, authored entities and block entity data."""
    payload = gzip.decompress(raw) if raw.startswith(b"\x1f\x8b") else raw
    root = decode_compound_nbt(payload)
    size = root.get("size")
    blocks = root.get("blocks")
    if (
        not isinstance(size, list)
        or len(size) != 3  # noqa: PLR2004 - Minecraft template XYZ dimensions.
        or any(type(value) is not int or value < 0 for value in size)
        or not isinstance(blocks, list)
    ):
        message = "template is missing valid size or blocks"
        raise ValueError(message)
    state_counts: Counter[int] = Counter()
    block_entities: list[JsonValue] = []
    for block in blocks:
        if not isinstance(block, dict) or type(block.get("state")) is not int:
            message = "template block has no integer state"
            raise ValueError(message)
        state = block["state"]
        assert isinstance(state, int)  # noqa: S101 - narrowed by explicit validation above.
        state_counts[state] += 1
        if "nbt" in block:
            block_entities.append(block)
    return {
        "size": size,
        "data_version": root.get("DataVersion"),
        "palette": root.get("palette"),
        "palettes": root.get("palettes"),
        "state_counts": {str(key): count for key, count in sorted(state_counts.items())},
        "block_entities": block_entities,
        "entities": root.get("entities"),
    }
