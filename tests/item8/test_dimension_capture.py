from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_registry import read_registry

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_dimension_capture_preserves_stack_and_registry_identity() -> None:
    root = Path("evidence/item-8/runtime")
    baseline = cast(
        "dict[str, JsonValue]", json.loads((root / "registry-r1/capture.json").read_bytes())
    )
    accepted = cast(
        "dict[str, JsonValue]", json.loads((root / "dimension-r3/capture.json").read_bytes())
    )
    assert accepted["rejection_reason"] is None
    assert accepted["preflight"] == baseline["preflight"]
    assert accepted["registries"] == baseline["registries"]
    lifecycle = cast("dict[str, JsonValue]", accepted["lifecycle"])
    assert lifecycle["ready"] is lifecycle["save_all_flush"] is lifecycle["clean_stop"] is True
    assert lifecycle["return_code"] == 0
    assert lifecycle["process_group_killed"] is False
    for attempt in ("dimension-r1", "dimension-r2"):
        rejected = cast(
            "dict[str, JsonValue]", json.loads((root / attempt / "capture.json").read_bytes())
        )
        assert rejected["preflight"] == baseline["preflight"]
        failure = cast("dict[str, JsonValue]", rejected["lifecycle"])
        assert failure["clean_stop"] is False
        assert failure["process_group_killed"] is True
        assert rejected["rejection_reason"]
    raw = (root / "dimension-r3/dimension-biomes.json").read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == accepted["dimension_biomes_sha256"]
        == ("08fa8185cd2c3f54b5255b2e8f86946c4b37ed471fb1991d0f82c835ffe20c7c")
    )
    dimensions = cast("dict[str, list[str]]", json.loads(raw))
    context = cast(
        "dict[str, dict[str, JsonValue]]",
        json.loads((root / "registry-r1/world-context.json").read_bytes()),
    )
    assert (
        dimensions.keys()
        == cast("dict[str, JsonValue]", context["WorldGenSettings"]["dimensions"]).keys()
    )
    registered = set(
        read_registry(root / "registry-r1/dumps/registry/minecraft/worldgen_biome.txt")
    )
    for biomes in dimensions.values():
        assert biomes
        assert biomes == sorted(set(biomes))
        assert set(biomes) <= registered
    assert {name: len(biomes) for name, biomes in dimensions.items()} == {
        "aether:the_aether": 13,
        "creatingspace:earth_orbit": 1,
        "creatingspace:mars": 2,
        "creatingspace:mars_orbit": 1,
        "creatingspace:moon_orbit": 1,
        "creatingspace:the_moon": 2,
        "creatingspace:venus": 2,
        "minecraft:overworld": 272,
        "minecraft:the_end": 29,
        "minecraft:the_nether": 14,
    }
    probe = cast("dict[str, str]", accepted["dimension_probe"])
    assert (
        hashlib.sha256(Path("tools/Item8DimensionProbe.java").read_bytes()).hexdigest()
        == probe["source_sha256"]
    )
    assert (
        hashlib.sha256(Path("tools/Item8DimensionProbe.mf").read_bytes()).hexdigest()
        == probe["manifest_sha256"]
    )
