from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_collective_membership_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "collective-1.21.1-8.25.jar")
    assert source.sha256 == "f66daf378f7a6747ac3b8e601d62ff571fc9f7f2d11b9fb6fae69de33b39f62e"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    prefix = "com/natamus/collective/"
    common = "com/natamus/collective_common_neoforge/"
    entries = {prefix + "CollectiveNeoForge.class",
               prefix + "neoforge/events/RegisterCollectiveNeoForgeEvents.class"}
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 567
        services = {f"META-INF/services/com.natamus.collective_common_{loader}.services.helpers."
                    + helper + "Helper" for loader in ("forge", "fabric", "neoforge")
                    for helper in ("RegisterKeyMapping", "ToolFunctions", "Teleport", "ModLoader",
                                   "ClientUtils", "RegisterBlock", "BlockTags", "EventTrigger",
                                   "RegisterItem")}
        data = {"data/collective/json/" + n + ".json": keys for n, keys in (
            ("area_names", {"area_names"}), ("entity_names", {"female_names", "male_names"}),
            ("linger_messages", {"linger_messages"}))}
        assert files - classes == services | set(data) | {
            "collective_forge.mixins.json", "collective_fabric.crop.mixins.json",
            "collective_fabric.mixins.json", "collective_fabric.refmap.json",
            "collective_neoforge.mixins.json", "collective.accesswidener", "fabric.mod.json",
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg", "META-INF/mods.toml",
            "META-INF/neoforge.mods.toml", "icon.png", "pack.mcmeta",
            "assets/collective/lang/en_us.json"}
        for name, keys in data.items():
            document = cast("dict[str, list[str]]", json.loads(archive.read(name)))
            assert set(document) == keys
            assert all(isinstance(v, list) and all(isinstance(s, str) for s in v)
                       for v in document.values())
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert metadata["mixins"] == [{"config": "collective_neoforge.mixins.json"}]
        config = cast("dict[str, object]",
                      json.loads(archive.read("collective_neoforge.mixins.json")))
        assert config["package"] == "com.natamus.collective.neoforge.mixin"
        assert config["plugin"] == (
            "com.natamus.collective.neoforge.mixin.plugin.NeoForgeMixinConfigPlugin")
        assert set(cast("list[str]", config["mixins"])) == {
            "BaseSpawnerMixin", "BlockEntityMixin", "BoneMealItemMixin", "PrimaryLevelDataMixin"}
        assert len(cast("list[str]", config["client"])) == 5
        assert not config["server"]
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == entries
        expected = entries | {
            prefix + "neoforge/mixin/plugin/NeoForgeMixinConfigPlugin.class",
            prefix + "neoforge/networking/NeoForgeNetworkHandler.class"}
        expected.update(prefix + "neoforge/mixin/" + n + ".class"
                        for n in cast("list[str]", config["mixins"]))
        expected.update(common + n + ".class" for n in (
            "CollectiveCommon", "events/CollectiveEvents", "config/GenerateJSONFiles",
            "config/LoadJSONFiles", "data/GlobalVariables", "data/Constants",
            "implementations/networking/NetworkSetup", "check/RegisterMod"))
        for name in services:
            implementation = archive.read(name).decode().strip().replace(".", "/") + ".class"
            assert implementation in classes
            if "_neoforge." in name:
                expected.add(implementation)
        captured: set[str] = set()
        for label, digest in (
            ("provider", "54dc3bdb078a2638a1c0368bd5883e4d5721bb2e24f5f94ed37cfa5ca86e576e"),
            ("services", "be2d268ae5cce33d21ff9bbb098f7669de1d870882c31e070c2d4034836eef8d"),
            ("init", "aebbe9220eb37a9142a499b1b3a817fa83e76c846586983a3627c91a1eb6138f"),
            ("mixin-plugin", "17633f917be4a00d30225d1efbb2f7b7a2e7ccd5237e3db2e1a5d4fa623b3e14"),
        ):
            directory = Path("evidence/item-8/sources") / ("collective-" + label)
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                captured.add(row["class"])
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                assert row["disassembly_sha256"] == hashlib.sha256(
                    (directory / row["disassembly"]).read_bytes()).hexdigest()
        assert captured == expected
