from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_totem_packaged_consumer_is_outside_captured_dimension_biomes() -> None:
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd")
    catalog = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(raw)))
    references = {str(r["path"]): r for r in catalog["resources"]
                  if "deep_aether:totem" in json.dumps(r["document"])}
    assert len(references) == sum(
        "deep_aether:totem" in json.dumps(r["document"]) for r in catalog["resources"])
    assert set(references) == {
        "data/deep_aether/worldgen/biome/sacred_lands.json",
        "data/deep_aether/worldgen/configured_feature/totem.json",
        "data/deep_aether/worldgen/placed_feature/totem.json",
    }
    assert all(r["archive"] == "deep_aether-1.21.1-1.1.5.1.jar"
               for r in references.values())
    biome = cast("dict[str, JsonValue]",
                 references["data/deep_aether/worldgen/biome/sacred_lands.json"]["document"])
    features = cast("list[list[str]]", biome["features"])
    assert "deep_aether:totem" in features[4]
    raw = Path("evidence/item-8/runtime/dimension-r3/dimension-biomes.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "08fa8185cd2c3f54b5255b2e8f86946c4b37ed471fb1991d0f82c835ffe20c7c")
    dimensions = cast("dict[str, list[str]]", json.loads(raw))
    assert dimensions
    assert all("deep_aether:sacred_lands" not in biomes for biomes in dimensions.values())
