from __future__ import annotations

import hashlib
import json
import tomllib
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_creeper_overhaul_payload_and_spawn_only_data() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("CreeperOverhaul-"))
    assert source.sha256 == "ed83bea2826667fca80a6a8067f89fe7b97eb8b3213bbcb7f0f4e6a6898c0bc9"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 317
        classes = {n for n in names if n.endswith(".class")}
        assets = {n for n in names if n.startswith("assets/")}
        data = {n for n in names if n.startswith("data/")}
        assert (len(classes), len(assets), len(data)) == (83, 185, 42)
        assert set(names) - classes - assets - data == {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml",
            "META-INF/jarjar/metadata.json", "META-INF/jars/resourceful-cosmetics-4j-1.0.3.jar",
            "CreeperOverhaul-common-refmap.json", "creeperoverhaul-common.mixins.json",
            "creeperoverhaul.accesswidener",
        }
        assert all(n.endswith((".json", ".png", ".ogg", ".fsh", ".vsh")) for n in assets)
        assert Counter(n.split("/")[2] for n in data) == {
            "loot_table": 18, "neoforge": 17, "tags": 7,
        }
        spawn_types: Counter[str] = Counter()
        additions: set[str] = set()
        for name in data:
            assert name.endswith(".json")
            document = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
            if "/neoforge/" in name:
                assert "/neoforge/biome_modifier/" in name
                spawn_types[str(document["type"])] += 1
                if document["type"] == "neoforge:add_spawns":
                    spawner = cast("dict[str, JsonValue]", document["spawners"])
                    additions.add(str(spawner["type"]))
                else:
                    assert document["entity_types"] == ["minecraft:creeper"]
            elif "/loot_table/" in name:
                assert document["type"] in {"minecraft:entity", "minecraft:block"}
            else:
                assert "/tags/entity_type/" in name or "/tags/worldgen/biome/" in name
                assert set(document) <= {"values", "replace", "remove"}
        assert spawn_types == {"neoforge:add_spawns": 16, "neoforge:remove_spawns": 1}
        entity_loot = {
            "creeperoverhaul:" + Path(n).stem for n in data if "/loot_table/entities/" in n
        }
        assert len(additions) == 16
        assert additions == entity_loot


def test_creeper_overhaul_executable_entries() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("CreeperOverhaul-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        classes = {n for n in archive.namelist() if n.endswith(".class")}
        assert {n for n in classes if b"Lnet/neoforged/fml/common/Mod;" in archive.read(n)} == {
            "tech/thatgravyboat/creeperoverhaul/forge/CreepersForge.class",
        }
        assert not any(b"Lnet/neoforged/fml/common/EventBusSubscriber;" in archive.read(n)
                       for n in classes)
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert metadata["mixins"] == [{"config": "creeperoverhaul-common.mixins.json"}]
        mixins = cast("dict[str, JsonValue]", json.loads(
            archive.read("creeperoverhaul-common.mixins.json")
        ))
        assert mixins["mixins"] == ["IronGolemMixin", "PlayerListMixin"]
        assert mixins["client"] == ["ClientPacketListenerMixin", "LivingEntityRendererInvoker"]
        assert not mixins.get("plugin")
        captured: set[str] = set()
        for label, count, expected_sha in (
            ("creeper-overhaul-provider", 13,
             "f44ec77d75bb58eed2f2475aa44575ca4f894ee557f6ee83549a6efee6844b7c"),
            ("creeper-overhaul-login", 1,
             "abb86e8bdaf55aa9fd570fe47f21f2e30f19c50780019b3a7d4f63ee521096ec"),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == expected_sha
            rows = cast("list[dict[str, str]]", json.loads(raw))
            assert len(rows) == len({r["class"] for r in rows}) == count
            for row in rows:
                captured.add(row["class"])
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                raw = (directory / row["disassembly"]).read_bytes()
                assert hashlib.sha256(raw).hexdigest() == row["disassembly_sha256"]
        assert {
            "tech/thatgravyboat/creeperoverhaul/mixin/" + name + ".class"
            for name in cast("list[str]", mixins["mixins"])
        } <= captured


def test_creeper_overhaul_bundled_cosmetics_has_no_server_entry() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("CreeperOverhaul-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        assert {
            n for n in archive.namelist()
            if n.endswith(".class") and b"resourcefulcosmetics" in archive.read(n)
        } == {"tech/thatgravyboat/creeperoverhaul/client/cosmetics/service/CosmeticsApi.class"}
        payload = archive.read("META-INF/jars/resourceful-cosmetics-4j-1.0.3.jar")
    assert hashlib.sha256(payload).hexdigest() == (
        "ed67d9ccb8be7deb4771e08dd95be234bf63363b320531c4ed4d7531f8429b9e"
    )
    with ZipFile(BytesIO(payload)) as nested:
        names = {n for n in nested.namelist() if not n.endswith("/")}
        classes = {n for n in names if n.endswith(".class")}
        assert len(names) == 12
        assert len(classes) == 10
        assert names - classes == {
            "META-INF/MANIFEST.MF", "META-INF/architectury-loom-nesting-metadata.json",
        }
        assert nested.read("META-INF/MANIFEST.MF").decode().strip() == "Manifest-Version: 1.0"
        assert all(n.startswith("com/teamresourceful/resourcefulcosmetics/") for n in classes)
        assert not any(
            key in nested.read(name) for name in classes
            for key in (b"net/minecraft/", b"net/neoforged/", b"net/fabricmc/")
        )
