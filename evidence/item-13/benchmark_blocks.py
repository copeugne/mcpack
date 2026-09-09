"""Compare point and section decoding on identical synthetic saved palette data."""

# ruff: noqa: INP001, T201
import json
import time

from tests.item7.anvil_support import packed_values
from tools.analyze_structure_density import saved_block_at, saved_block_section

values = tuple(index % 2 for index in range(4096))
palette = [{"Name": "minecraft:air"}, {"Name": "minecraft:stone"}]
chunk = {
    "xPos": 0,
    "zPos": 0,
    "sections": [
        {
            "Y": 0,
            "block_states": {
                "palette": palette,
                "data": packed_values(values, 4),
            },
        }
    ],
}
begun = time.perf_counter()
points = [saved_block_at(chunk, (i % 16, i // 256, (i // 16) % 16)) for i in range(4096)]
point_seconds = time.perf_counter() - begun
begun = time.perf_counter()
section = saved_block_section(chunk, 0)
if section is None:
    message = "synthetic saved section unexpectedly absent"
    raise ValueError(message)
bulk = [section[0][index] for index in section[1]]
section_seconds = time.perf_counter() - begun
if points != bulk:
    message = "bulk and point block identities disagree"
    raise ValueError(message)
print(
    json.dumps(
        {
            "blocks": len(points),
            "point_seconds": point_seconds,
            "section_seconds": section_seconds,
            "identical_states": True,
        },
        sort_keys=True,
    )
)
