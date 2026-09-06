from __future__ import annotations

import hashlib
import json
import tomllib
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_mca_membership_payload_and_building_recognition() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "mca-neoforge-7.7.11+1.21.1.jar")
    assert source.sha256 == "8d569c0ae870e1fe098a7270f240780aa588f328512f64ffa0a6d74a886fc59f"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assets = {n for n in files if n.startswith("assets/")}
        data = {n for n in files if n.startswith("data/")}
        assert (len(classes), len(assets), len(data)) == (543, 2034, 770)
        assert files - classes - assets - data == {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "mca.mixins.json",
            "hotswap-agent.properties", "icon.png", "pack.mcmeta", "LICENSE_Minecraft Comes Alive",
        }
        assert Counter(n.split("/")[2] for n in data) == {
            "recipe": 226, "advancement": 221, "gifts": 112, "mca_names": 110,
            "loot_tables": 26, "building_types": 26, "dialogues": 19, "tags": 19,
            "skins": 6, "tasks": 5,
        }
        assert Counter(n.split("/")[2] for n in assets) == {
            "skins": 1324, "models": 280, "textures": 166, "lang": 129, "sounds": 99,
            "blockstates": 15, "api": 14, "shaders": 4, "particles": 2, "sounds.json": 1,
        }
        assert not any(n.endswith((".jar", ".nbt")) for n in files)
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert metadata["mixins"] == [{"config": "mca.mixins.json"}]
        mixin = cast("dict[str, object]", json.loads(archive.read("mca.mixins.json")))
        assert not mixin.get("plugin")
        assert not mixin.get("server")
        hooks = {"net/conczin/mca/mixin/" + n + ".class"
                 for n in cast("list[str]", mixin["mixins"])}
        assert len(hooks) == 21
        assert len(cast("list[str]", mixin["client"])) == 8
        entries = {"net/conczin/mca/neoforge/CommonNeoForge.class",
                   "net/conczin/mca/neoforge/ClientNeoForge.class"}
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == entries
        for label, digest, expected in (
            ("mca-provider", "d57838eeff0a970043dd26410cff0ac901fd70bbc498446b510366b0a88b77e1",
             hooks | entries | {"net/conczin/mca/" + n + ".class" for n in (
                 "network/c2s/DestinyMessage", "server/world/data/Village",
                 "server/world/data/VillageManager", "util/BlockBoxExtended", "util/WorldUtils",
             )}),
            ("mca-building-recognition",
             "06481eae75ce8b701dd96d45455a5d0ea74f24c56a180018bc101dc7334433cf",
             {"net/conczin/mca/" + n + ".class" for n in (
                 "resources/BuildingTypes", "resources/data/BuildingType",
                 "server/world/data/Building",
             )}),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            rows = cast("list[dict[str, str]]", json.loads(raw))
            assert {row["class"] for row in rows} == expected
            for row in rows:
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class_sha256"] == hashlib.sha256(
                    archive.read(row["class"])).hexdigest()
                assert row["disassembly_sha256"] == hashlib.sha256(
                    (directory / row["disassembly"]).read_bytes()).hexdigest()
        for name in sorted(n for n in data if "/building_types/" in n):
            definition = cast("dict[str, object]", json.loads(archive.read(name)))
            assert set(definition) <= {
                "color", "visible", "priority", "blocks", "iconU", "iconV", "icon",
                "margin", "noBeds", "grouped", "mergeRange",
            }
            blocks = cast("dict[str, int]", definition["blocks"])
            assert all(isinstance(key, str) and type(value) is int and value > 0
                       for key, value in blocks.items())
