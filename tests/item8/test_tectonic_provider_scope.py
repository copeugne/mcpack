from __future__ import annotations

import hashlib
import json
import tomllib
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_tectonic_provider_payload_and_generation_entries() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("tectonic-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    prefix = "dev/worldgen/tectonic/"
    captured: set[str] = set()
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 310
        classes = {n for n in names if n.endswith(".class")}
        assert len(classes) == 57
        for name, digest in (
            ("tectonic-provider",
             "b807dc5f98fab2557300678fb3b69e5504fef767f1c84ab160590924452fafd9"),
            ("tectonic-config-selection",
             "cf630dfe5cf8b8ff093d293db9cdd0a259eb1050a1f43f30dedf8d8f5d3951c4"),
        ):
            directory = Path("evidence/item-8/sources") / name
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                captured.add(row["class"])
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == (
                    row["class_sha256"]
                )
                disassembly = (directory / row["disassembly"]).read_bytes()
                assert hashlib.sha256(disassembly).hexdigest() == row["disassembly_sha256"]
        assert len(captured) == 31
        assert all(n.startswith((prefix + "client/", prefix + "config/state/"))
                   for n in classes - captured)
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"fml/common/Mod;", b"EventBusSubscriber", b"SubscribeEvent",
        ))} == {prefix + "TectonicNeoforge.class", prefix + "TectonicNeoforgeClient.class"}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        mixins = {r["config"] for r in cast("list[dict[str, str]]", metadata["mixins"])}
        assert mixins == {"tectonic.mixins.json", "tectonic.21.1.mixins.json"}
        declared: set[str] = set()
        for name in mixins:
            document = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
            assert "plugin" not in document
            for side in ("mixins", "client", "server"):
                declared.update(
                    (str(document["package"]) + "." + n).replace(".", "/") + ".class"
                    for n in cast("list[str]", document.get(side, []))
                )
        assert len(declared) == 13
        assert declared <= captured
        assert {n for n in classes if "/mixin/" in n} - declared == {
            prefix + "mixin/WorldCarverMixin.class"
        }
        resources = {n for n in names if n.startswith("resourcepacks/tectonic/")}
        assert len(resources) == 245
        assert set(names) - classes - resources == mixins | {
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml", "assets/tectonic/lang/en_us.json",
            "pack.mcmeta", "pack.png",
        }
        assert archive.read("META-INF/accesstransformer.cfg") == b""
        assert Counter("/".join(n.split("/data/")[1].split("/")[1:3])
                       for n in resources if "/data/" in n) == {
            "worldgen/density_function": 164, "worldgen/noise": 38,
            "worldgen/placed_feature": 17, "lithostitched/worldgen_modifier": 6,
            "worldgen/configured_carver": 5, "worldgen/noise_settings": 3,
            "worldgen/configured_feature": 3, "tags/block": 1, "tags/worldgen": 1,
        }
        assert all(n.endswith(".json") if "/data/" in n
                   else n.endswith(("/pack.mcmeta", "/pack.png")) for n in resources)


def test_tectonic_named_lantern_candidate_and_frozen_selection() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("tectonic-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    raw = Path("evidence/item-6/frozen/config/tectonic.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "fe51e529faafe17609b060f25d2cd87c0db5571c98e306a09f9335d4b54546fa"
    )
    config = cast("dict[str, dict[str, JsonValue]]", json.loads(raw))
    assert config["general"]["mod_enabled"] is True
    assert config["continents"]["river_lanterns"] is True
    assert config["continents"]["river_ice"] is False
    assert config["caves"]["carvers_enabled"] is True
    assert config["caves"]["ore_fix"] is False
    assert config["global_terrain"]["ultrasmooth"] is False
    assert config["oceans"]["monument_offset"] == -30
    with ZipFile(source.path) as archive:
        data = {n: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
                for n in archive.namelist() if n.endswith((".json", ".mcmeta"))}
    base = "resourcepacks/tectonic/"
    overlays = cast("dict[str, list[dict[str, JsonValue]]]", data[base + "pack.mcmeta"]["overlays"])
    assert [(o["directory"], o["formats"]) for o in overlays["entries"]] == [
        ("overlay.mod", [1, 999]), ("overlay.1_21_9_mod", [82, 999]),
        ("overlay.1_21_9", [82, 999]),
    ]
    modifier_path = base + "overlay.mod/data/tectonic/lithostitched/worldgen_modifier/"
    assert data[modifier_path + "underground_river/lanterns.json"] == {
        "predicate": {"type": "tectonic:config", "key": "river_lanterns"},
        "type": "lithostitched:add_features", "biomes": "#minecraft:is_overworld",
        "features": "tectonic:underground_river/lanterns", "step": "vegetal_decoration",
    }
    feature_path = base + "data/tectonic/worldgen/"
    lantern = data[feature_path + "configured_feature/underground_river/lanterns.json"]
    assert lantern["type"] == "minecraft:block_column"
    column = cast("dict[str, JsonValue]", lantern["config"])
    assert column["direction"] == "down"
    assert column["prioritize_tip"] is True
    layers = cast("list[dict[str, JsonValue]]", column["layers"])
    assert [cast("dict[str, dict[str, str]]", layer["provider"])["state"]["Name"]
            for layer in layers] == ["minecraft:chain", "minecraft:lantern"]
    assert layers[0]["height"] == {
        "type": "minecraft:uniform", "min_inclusive": 2, "max_inclusive": 8,
        "value": {"min_inclusive": 2, "max_inclusive": 8},
    }
    assert layers[1]["height"] == 1
    assert data[feature_path + "placed_feature/underground_river/lanterns.json"]["feature"] == (
        "tectonic:underground_river/lanterns"
    )
    assert data[feature_path + "configured_feature/underground_river/ice.json"] == {
        "type": "minecraft:simple_block", "config": {"to_place": {
            "type": "minecraft:simple_state_provider", "state": {"Name": "minecraft:ice"},
        }},
    }
    assert data[feature_path + "placed_feature/underground_river/lichen.json"]["feature"] == (
        "minecraft:glow_lichen"
    )
