from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_integrated_api_membership_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "integrated_api-1.7.3+1.21.1-neoforge.jar")
    assert source.sha256 == "81bffee0e09dce9160376c36c3f38b26af4470393ecf7b2d6fdc3fa5c40593ec"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/integrated-api-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "fa79c4ec7cb6bc0ec4b3c537a36d1ef725a89189d1cc4ae1762fbf5a39310f5e")
    rows = cast("list[dict[str, str]]", json.loads(raw))
    assert len(rows) == 30
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        data = {n for n in files if n.startswith("data/")}
        assert len(classes) == 206
        assert len(data) == 51
        assert files - classes - data == {
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml", "integrated_api-common-refmap.json",
            "integrated_api-common.mixins.json", "integrated_api-neoforge.mixins.json",
            "pack.mcmeta", "assets/integrated_api/integrated_api_logo.png",
        }
        biome_tags = {n for n in data if n.startswith(
            "data/integrated_api/tags/worldgen/biome/collections/") and n.endswith(".json")}
        assert len(biome_tags) == 48
        assert data - biome_tags == {
            "data/integrated_api/tags/worldgen/feature/skippable_features.json",
            "data/integrated_api/tags/worldgen/structure/disabled_structures.json",
            "data/integrated_api/tags/worldgen/structure/unskippable_structures.json",
        }
        for name in data - biome_tags:
            assert json.loads(archive.read(name)) == {"replace": False, "values": []}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert metadata["mixins"] == [
            {"config": "integrated_api-neoforge.mixins.json"},
            {"config": "integrated_api-common.mixins.json"},
        ]
        hooks: set[str] = set()
        for name, count, clients in (
            ("integrated_api-common.mixins.json", 26, 2),
            ("integrated_api-neoforge.mixins.json", 1, 0),
        ):
            mixin = cast("dict[str, object]", json.loads(archive.read(name)))
            assert not mixin.get("plugin")
            assert not mixin.get("server")
            declared = cast("list[str]", mixin["mixins"])
            assert len(declared) == count
            assert len(cast("list[str]", mixin["client"])) == clients
            prefix = cast("str", mixin["package"]).replace(".", "/")
            hooks.update(prefix + "/" + n.replace(".", "/") + ".class" for n in declared)
        entries = {"com/craisinlord/integrated_api/" + n + ".class" for n in (
            "neoforge/IntegratedAPINeoforge", "datagen/StructureNbtUpdaterDatagen",
        )}
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == entries
        assert {r["class"] for r in rows} == hooks | entries | {
            "com/craisinlord/integrated_api/IntegratedAPI.class"}
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
            assert row["disassembly_sha256"] == hashlib.sha256(
                (directory / row["disassembly"]).read_bytes()).hexdigest()
