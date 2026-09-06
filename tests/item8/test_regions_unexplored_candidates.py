from __future__ import annotations

import gzip
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources


def test_regions_unexplored_packaged_component_boundary() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "regions-unexplored-0.6.1-neoforge-21.1.jar")
    assert source.sha256 == "8eac74e63ba6bc9c3aea459adcdeba58d7918d296d0775c6f51777fe2ee1967a"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert not any(n.startswith("regions_unexplored:") for n in registry)
    with ZipFile(source.path) as archive:
        names = {n for n in archive.namelist() if not n.endswith("/")}
        assert len(names) == 8077
        prefix = "data/regions_unexplored/worldgen/"
        assert Counter(n.removeprefix(prefix).split("/")[0]
                       for n in names if n.startswith(prefix)) == {
            "configured_feature": 386, "placed_feature": 287, "biome": 78,
            "processor_list": 10, "noise": 5, "density_function": 1, "template_pool": 1,
        }
        assert {n for n in names if n.endswith(".nbt")} == {
            "data/regions_unexplored/structure/trial_chambers/ashen.nbt",
        }
        assert not any("/worldgen/structure/" in n or "/worldgen/structure_set/" in n
                       for n in names)
        assert json.loads(archive.read(prefix + "template_pool/trial_chambers/ashen.json")) == {
            "elements": [{"element": {
                "element_type": "minecraft:single_pool_element",
                "location": "regions_unexplored:trial_chambers/ashen",
                "processors": {"processors": []}, "projection": "rigid",
            }, "weight": 1}], "fallback": "minecraft:empty",
        }
        assert json.loads(archive.read(
            "data/lithostitched/tags/worldgen/template_pool/trial_spawner/melee.json"
        )) == {"values": ["regions_unexplored:trial_chambers/ashen"]}
        base = Path("evidence/item-8/sources/regions-unexplored-provider")
        raw = (base / "identities.json").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == (
            "cb7185024530c1b77bbf71dbf9ccefb2ba1acf505688896a1803f0a4240a4894"
        )
        captured: set[str] = set()
        for row in cast("list[dict[str, str]]", json.loads(raw)):
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((base / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
            captured.add(row["class"])
        entries = {n for n in names if n.endswith(".class") and any(
            marker in archive.read(n) for marker in (
                b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
            )
        )}
        assert len(entries) == 3
        assert entries <= captured
        mixins = cast("dict[str, object]", json.loads(
            archive.read("regions_unexplored.mixins.json")
        ))
        common = {"net/regions_unexplored/mixin/" + n.replace(".", "/") + ".class"
                  for n in cast("list[str]", mixins["mixins"])}
        assert len(common) == 9
        assert common <= captured


def test_regions_unexplored_feature_candidates_and_sources() -> None:
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd"
    )
    catalog = cast("dict[str, list[dict[str, object]]]", json.loads(gzip.decompress(raw)))
    rows = {str(r["path"]): cast("dict[str, object]", r["document"])
            for r in catalog["resources"]
            if r["archive"] == "regions-unexplored-0.6.1-neoforge-21.1.jar"}
    variants = {p.rsplit("/", 1)[1].removesuffix(".json"): d
                for p, d in rows.items() if "/configured_feature/" in p
                and d.get("type") == "regions_unexplored:fallen_tree"}
    assert set(variants) == {"larch", "maple", "oak", "pine", "silver_birch", "snow_pine"}
    placed = {p.rsplit("/", 1)[1].removesuffix(".json"): d["feature"]
              for p, d in rows.items()
              if p.startswith("data/regions_unexplored/worldgen/placed_feature/tree/fallen/")}
    assert placed == {name: "regions_unexplored:tree/fallen/" + config for name, config in (
        ("larch", "larch"), ("maple", "maple"), ("oak_dense", "oak"), ("oak_sparse", "oak"),
        ("pine", "pine"), ("pine_on_dirt", "pine"), ("pine_on_snow", "snow_pine"),
        ("silver_birch", "silver_birch"),
    )}
    consumers = {
        p.rsplit("/", 1)[1].removesuffix(".json"): [n for group in
            cast("list[list[str]]", d["features"]) for n in group if ":tree/fallen/" in n]
        for p, d in rows.items() if p.startswith("data/regions_unexplored/worldgen/biome/")
    }
    assert {k: v for k, v in consumers.items() if v} == {
        biome: ["regions_unexplored:tree/fallen/" + name]
        for name, biomes in (
            ("larch", ("boreal_taiga", "cold_boreal_taiga", "golden_boreal_taiga",
                       "old_growth_boreal_taiga", "old_growth_golden_boreal_taiga")),
            ("oak_sparse", ("cold_deciduous_forest",)),
            ("oak_dense", ("deciduous_forest", "fen", "old_growth_forest")),
            ("pine_on_dirt", ("frozen_pine_taiga", "mountains", "pine_slopes", "pine_taiga")),
            ("pine_on_snow", ("icy_heights",)),
            ("maple", ("maple_forest", "temperate_grove", "windswept_maple_forest")),
            ("silver_birch", ("silver_birch_forest",)), ("pine", ("towering_cliffs",)),
        ) for biome in biomes
    }
    for name, minimum, maximum, log in (
        ("larch", 7, 12, "regions_unexplored:larch_log"),
        ("maple", 6, 8, "regions_unexplored:maple_log"),
        ("oak", 6, 8, "minecraft:oak_log"),
        ("pine", 7, 12, "regions_unexplored:pine_log"),
        ("silver_birch", 6, 10, "regions_unexplored:silver_birch_log"),
        ("snow_pine", 7, 12, "regions_unexplored:stripped_pine_log"),
    ):
        config = cast("dict[str, object]", variants[name]["config"])
        assert config["log_length"] == {
            "type": "minecraft:uniform", "min_inclusive": minimum, "max_inclusive": maximum,
        }
        assert config["stump_decorators"] == []
        provider = cast("dict[str, object]", config["trunk_provider"])
        assert provider["type"] == "minecraft:simple_state_provider"
        assert cast("dict[str, object]", provider["state"])["Name"] == log
        assert all(d["type"] == "regions_unexplored:attached_to_logs"
                   for d in cast("list[dict[str, object]]", config["log_decorators"]))
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "regions-unexplored-0.6.1-neoforge-21.1.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    captured: set[str] = set()
    with ZipFile(source.path) as archive:
        for directory, digest in (
            ("regions-unexplored-generation-delegates",
             "b779daaf84f5a04384246079c6ada082941188e6319cb4c8835bfe6dad089770"),
            ("regions-unexplored-log-decorator",
             "7656c29c7f0b77b5827cbb01b082d2509f800a7cac87e342ec47bc6785bdc77d"),
            ("regions-unexplored-terrain-features",
             "408438fe5484a1798d6487f12725cd3becac5c315a0d99dc585163177a2d474c"),
            ("regions-unexplored-redstone-writer",
             "31143f1076e6d08d7280dd918331ce67087d07626cfe25778608398c26827bdd"),
            ("regions-unexplored-vegetation-features",
             "6e77e0aab7c6f999e08de37eca0fdf8417b07377823cd848bae016e50cdc1bb6"),
            ("regions-unexplored-feature-code",
             "d27de44a59aedb2dd41e12dcc0f35db1328207314c8cbe59dae6120de5b9953b"),
        ):
            base = Path("evidence/item-8/sources") / directory
            raw = (base / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                assert row["archive"] == source.name
                captured.add(row["class"].removesuffix(".class"))
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert hashlib.sha256((base / row["disassembly"]).read_bytes()).hexdigest() == (
                    row["disassembly_sha256"]
                )
    registration = (
        Path("evidence/item-8/sources/regions-unexplored-feature-code")
        / "regions-unexplored-0.6.1-neoforge-21.1.jar"
        / "net.regions_unexplored.registry.RUFeatureTypes.txt"
    ).read_text()
    implementations = set(re.findall(
        r"// class (net/regions_unexplored/[^\s]+Feature)", registration
    ))
    assert len(implementations) == 53
    assert implementations <= captured
