from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_explorations_payload_and_component_partition() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("explorations-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/explorations-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "7889daf6336c190cec169bc57eac369ebf863eb4c72e2b7895341aa12b4e9b8f"
    )
    identities = cast("list[dict[str, str]]", json.loads(raw))
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 201
        classes = {row["class"] for row in identities}
        assert len(classes) == 33
        assert classes == {n for n in names if n.endswith(".class")}
        for row in identities:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            disassembly = (directory / row["disassembly"]).read_bytes()
            assert hashlib.sha256(disassembly).hexdigest() == row["disassembly_sha256"]
        service_prefix = "META-INF/services/com.tristankechlo.explorations."
        services = {
            service_prefix + "registration.RegistrationProvider$Factory":
                "com.tristankechlo.explorations.NeoforgeRegistrationFactory",
            service_prefix + "platform.IPlatformHelper":
                "com.tristankechlo.explorations.NeoforgePlatformHelper",
        }
        for name, implementation in services.items():
            assert archive.read(name).decode().strip() == implementation
            assert implementation.replace(".", "/") + ".class" in classes
        data_files = {n for n in names if n.startswith("data/explorations/")}
        assert set(names) - classes - data_files == set(services) | {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "pack.mcmeta",
            "pack.png", "LICENSE", "explorations.mixins.json",
        }
        assert Counter("/".join(n.split("/")[2:4]) if "/worldgen/" in n
                       or "/neoforge/" in n else n.split("/")[2]
                       for n in data_files) == {
            "tags/worldgen": 20, "tags": 1, "loot_table": 16, "structure": 55,
            "worldgen/structure": 10, "worldgen/structure_set": 10,
            "worldgen/template_pool": 15, "worldgen/configured_feature": 11,
            "worldgen/placed_feature": 10, "worldgen/processor_list": 2,
            "neoforge/biome_modifier": 10,
        }
        assert all(n.endswith(".nbt") if n.startswith("data/explorations/structure/")
                   else n.endswith(".json") for n in data_files)
        components = {
            kind: {found[0] for n in names if (found := resource_identity(n, kind, extension))}
            for kind, extension in (
                ("worldgen/structure", ".json"), ("worldgen/template_pool", ".json"),
                ("structure", ".nbt"),
            )
        }
        assert b"village/\x01/houses" in archive.read(
            "com/tristankechlo/explorations/config/types/VillageType.class"
        )
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    traces = cast("dict[str, dict[str, dict[str, JsonValue]]]",
                  json.loads(gzip.decompress(raw)))["structures"]
    roots = components["worldgen/structure"]
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert roots == {r for r in registry if r.startswith("explorations:")}
    assert roots - traces.keys() == {"explorations:slime_cave"}
    traced = roots & traces.keys()
    assert components["worldgen/template_pool"] <= {
        p for r in traced for p in cast("list[str]", traces[r]["pools"])
    }
    assert components["structure"] - {
        t for r in traced for t in cast("list[str]", traces[r]["templates"])
    } == {
        "explorations:slime_cave", "explorations:statues/statue_1",
        "explorations:statues/statue_2", "explorations:statues/statue_3",
        "explorations:statues/statue_4", "explorations:underground_temple/intersections/corner",
    }
    assert {r: traces[r]["missing"] for r in traced if traces[r]["missing"]} == {
        "explorations:underground_temple": [
            {"id": "explorations:underground_temple/intrusions/corner", "kind": "template"},
            {"id": "explorations:underground_temple/rooms/small_hall_down", "kind": "template"},
        ],
    }
    assert all(not traces[r]["unresolved_elements"] for r in traced)


def test_explorations_features_and_frozen_statue_consumers() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("explorations-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        data = {n: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
                for n in archive.namelist() if n.startswith("data/") and n.endswith(".json")}
    base = "data/explorations/"
    variants = {"acacia", "bamboo", "birch", "cherry", "dark_oak", "jungle",
                "mangrove", "oak", "spruce"}
    decisions = cast("dict[str, JsonValue]", json.loads(Path(
        "evidence/item-8/family-decisions.json").read_bytes()))
    content = cast("dict[str, JsonValue]", decisions["non_registry_content"])
    contributions = cast("dict[str, dict[str, JsonValue]]", content["contributions"])
    scarecrow = contributions["explorations:scarecrow"]
    variant_ids = sorted("explorations:scarecrow_" + name for name in variants)
    assert scarecrow["configured_features"] == scarecrow["placed_features"] == variant_ids
    assert scarecrow["selector"] == "explorations:scarecrow"
    for path, digest in cast("dict[str, str]", scarecrow["evidence"]).items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest
    registry = Path("evidence/item-8/runtime/registry-r1/dumps/registry/minecraft")
    assert set(variant_ids) | {"explorations:scarecrow"} <= set(read_registry(
        registry / "worldgen_configured_feature.txt"))
    assert set(variant_ids) <= set(read_registry(registry / "worldgen_placed_feature.txt"))
    configured = base + "worldgen/configured_feature/"
    assert {n.removeprefix(configured).removesuffix(".json") for n in data
            if n.startswith(configured)} == {
        "scarecrow_" + name for name in variants
    } | {"scarecrow", "large_mushroom"}
    selector = data[configured + "scarecrow.json"]
    assert selector["type"] == "minecraft:simple_random_selector"
    selection = cast("dict[str, list[dict[str, JsonValue]]]", selector["config"])
    assert {str(f["feature"]) for f in selection["features"]} == {
        "explorations:scarecrow_" + name for name in variants
    }
    for name in variants:
        assert data[configured + f"scarecrow_{name}.json"]["type"] == "explorations:scarecrow"
        assert data[base + f"worldgen/placed_feature/scarecrow_{name}.json"]["feature"] == (
            "explorations:scarecrow_" + name
        )
        assert data[base + f"neoforge/biome_modifier/scarecrow_{name}.json"] == {
            "type": "neoforge:add_features",
            "biomes": "#explorations:has_feature/scarecrow/" + name,
            "features": "explorations:scarecrow_" + name, "step": "vegetal_decoration",
        }
        assert base + f"tags/worldgen/biome/has_feature/scarecrow/{name}.json" in data
    mushroom = data[configured + "large_mushroom.json"]
    assert mushroom["type"] == "minecraft:tree"
    config = cast("dict[str, JsonValue]", mushroom["config"])
    assert config["decorators"] == [{
        "type": "explorations:lantern", "probability": 0.9,
        "lantern_count": {"type": "minecraft:uniform",
                          "value": {"min_inclusive": 2, "max_inclusive": 3}},
        "chain_length": {"type": "minecraft:uniform",
                         "value": {"min_inclusive": 1, "max_inclusive": 2}},
    }]
    assert data[base + "worldgen/placed_feature/large_mushroom.json"]["feature"] == (
        "explorations:large_mushroom"
    )
    assert data[base + "neoforge/biome_modifier/large_mushroom.json"] == {
        "type": "neoforge:add_features", "biomes": "#explorations:has_feature/large_mushroom",
        "features": "explorations:large_mushroom", "step": "vegetal_decoration",
    }
    raw = Path("evidence/item-6/frozen/config/explorations.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "00f272a0018d06c3b73b70da85f6fb85c05cc9bd0b2558d2d5d57e9f4e185d09"
    )
    statues = cast("dict[str, dict[str, list[dict[str, JsonValue]]]]", json.loads(raw))["statues"]
    assert set(statues) == {"plains", "savanna", "snowy", "taiga"}
    for village, weight in (("plains", 2), ("savanna", 2), ("snowy", 3), ("taiga", 4)):
        assert statues[village] == [
            {"location": f"explorations:statues/statue_{i}", "weight": weight}
            for i in range(1, 5)
        ]
