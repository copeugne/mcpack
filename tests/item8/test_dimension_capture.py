from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from tools.build_item8_inventory import main as build_inventory

from mcpack_evidence.item8_registry import read_registry

if TYPE_CHECKING:
    import pytest
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


def test_inventory_dimension_join_covers_every_frozen_root(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    output = tmp_path / "inventory.json"
    monkeypatch.setattr("sys.argv", ["build_item8_inventory", "--output", str(output)])
    build_inventory()
    inventory = cast("dict[str, JsonValue]", json.loads(output.read_bytes()))
    families = cast("dict[str, dict[str, JsonValue]]", inventory["families"])
    memberships: dict[str, JsonValue] = {}
    for family in families.values():
        dimension = cast("dict[str, JsonValue]", family["dimension"])
        by_root = cast("dict[str, JsonValue]", dimension["biome_compatible_by_structure"])
        assert by_root.keys() == set(cast("list[str]", family["structure_ids"]))
        assert not memberships.keys() & by_root.keys()
        memberships.update(by_root)
        possible = {dim for value in by_root.values() if isinstance(value, list)
                    for dim in cast("list[str]", value)}
        assert set(cast("list[str]", dimension["observed"])) <= possible
    assert set(memberships) == set(read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )))
    assert {root for root, value in memberships.items() if isinstance(value, str)} == {
        "idas:lumber_camp/lumber_camp_bopmahogany",
        "idas:lumber_camp/lumber_camp_bygmahogany",
        "idas:lumber_camp/lumber_camp_bygredwood",
    }
    assert {root for root, value in memberships.items() if value == []} == {
        "deep_aether:altar_camp", "deep_aether:campfire", "deep_aether:combiner_corridor",
        "dungeons_arise:mining_system", "idas:desert_camp/desert_camp_bygwindswept",
        "terralith:underground/witch_hut", "towns_and_towers:exclusives/pillager_outpost_nilotic",
        "towns_and_towers:exclusives/village_nilotic", "towns_and_towers:exclusives/village_piglin",
    }
    assert inventory["status"] == "INCOMPLETE"
