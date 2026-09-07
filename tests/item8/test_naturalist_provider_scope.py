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


def test_naturalist_payload_and_source_coverage() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("naturalist-"))
    assert source.sha256 == "04616a9f136c7a8fd6f9f75e83be80af33bc54924b3ca16b0f33d19273c25e95"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/naturalist-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "2b5d4824d4dfcbd499f73366a72e001e098f794e26eb20bffa58b4e375932f2d"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    captured = {r["class"] for r in rows}
    assert len(rows) == len(captured) == 10
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 1347
        assert Counter("classes" if n.endswith(".class") else n.split("/")[0]
                       for n in names) == {
            "classes": 211, "assets": 779, "data": 265, "resourcepacks": 79,
            ".cache": 8, "META-INF": 2, "icon.png": 1, "naturalist.mixins.json": 1,
            "pack.mcmeta": 1,
        }
        assert {n for n in names if n.startswith("META-INF/")} == {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml",
        }
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        classes = {n for n in names if n.endswith(".class")}
        assert {n for n in classes if any(tag in archive.read(n) for tag in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == {"com/starfish_studios/naturalist/Naturalist.class"}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert metadata["mixins"] == [{"config": "naturalist.mixins.json"}]
        mixins = cast("dict[str, JsonValue]", json.loads(archive.read("naturalist.mixins.json")))
        common = cast("list[str]", mixins["mixins"])
        assert len(common) == 7
        assert {"com/starfish_studios/naturalist/mixin/" + n + ".class" for n in common} <= captured
        assert mixins["client"] == ["ClientLevelMixin", "ClientPacketListenerMixin"]
        assert not mixins.get("plugin")


def test_naturalist_data_has_spawn_changes_and_client_resource_pack() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("naturalist-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert all(n.endswith(".json") for n in names if n.startswith("data/"))
        assert Counter(n.split("/")[2] for n in names if n.startswith("data/")) == {
            "tags": 112, "recipe": 65, "loot_table": 50, "advancement": 33, "neoforge": 5,
        }
        assert {n.split("/")[1] for n in names if n.startswith("resourcepacks/")} == {
            "custom_spawn_eggs",
        }
        assert Counter("/".join(n.split("/")[2:5]) if "/assets/" in n else n.split("/")[-1]
                       for n in names if n.startswith("resourcepacks/")) == {
            "assets/naturalist/textures": 47, "assets/naturalist/models": 31, "pack.mcmeta": 1,
        }
        assert all(n.endswith((".json", ".png", ".mcmeta")) for n in names
                   if n.startswith("resourcepacks/"))
        prefix = "data/naturalist/neoforge/"
        assert {n.removeprefix(prefix) for n in names if n.startswith(prefix)} == {
            "biome_modifier/add_animals.json", "biome_modifier/remove_farm_animals_savanna.json",
            "biome_modifier/remove_farm_animals_swamp.json",
            "biome_modifier/remove_forest_pigs.json",
            "data_maps/item/compostables.json",
        }
        assert json.loads(archive.read(prefix + "biome_modifier/add_animals.json")) == {
            "type": "naturalist:add_animals",
        }
        for name, biome, entities in (
            ("remove_farm_animals_savanna", "#minecraft:is_savanna",
             ["sheep", "pig", "chicken", "cow"]),
            ("remove_farm_animals_swamp", "#c:is_swamp", ["sheep", "pig", "chicken", "cow"]),
            ("remove_forest_pigs", "#minecraft:is_forest", ["pig"]),
        ):
            assert json.loads(archive.read(prefix + f"biome_modifier/{name}.json")) == {
                "type": "neoforge:remove_spawns", "biomes": biome,
                "entity_types": ["minecraft:" + entity for entity in entities],
            }
