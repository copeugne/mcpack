from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_glitchcore_membership_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "GlitchCore-neoforge-1.21.1-2.1.0.2.jar")
    assert source.sha256 == "59d2a3fb3d6877e43018fd6a2b199d526074a864276a5f49091409a1cdc62fae"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 80
        assert files - classes == {
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml", "glitchcore_icon_small.png",
            "glitchcore.mixins.json", "glitchcore.neoforge.mixins.json",
            "glitchcore.accesswidener", "glitchcore_logo.png", "pack.mcmeta",
        }
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        declarations = cast("list[dict[str, str]]", metadata["mixins"])
        assert {r["config"] for r in declarations} == {
            "glitchcore.mixins.json", "glitchcore.neoforge.mixins.json"}
        hooks: set[str] = set()
        for name, count in (("glitchcore.mixins.json", 3),
                            ("glitchcore.neoforge.mixins.json", 5)):
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            assert not config.get("plugin")
            assert not config.get("server")
            declared = cast("list[str]", config["mixins"])
            assert len(declared) == count
            assert len(cast("list[str]", config["client"])) == 2
            prefix = cast("str", config["package"]).replace(".", "/")
            hooks.update(prefix + "/" + n.replace(".", "/") + ".class" for n in declared)
        entries = {"glitchcore/neoforge/GlitchCoreNeoForge.class"} | {
            "glitchcore/neoforge/handlers/" + n + "EventHandler.class" for n in (
                "Colors", "Interaction", "LevelRender", "RegisterCommands",
                "RegisterParticleProviders", "Registry", "TagsUpdated", "Tick",
                "ToolModification", "Tooltip", "VillagerTrades",
            )}
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == entries
        for label, digest, expected in (
            ("glitchcore-provider",
             "491a475ee26288951ffdac1e0e66dd7cd94cef92bd94193fd2f80a61dd9ed609",
             entries | hooks),
            ("glitchcore-init",
             "fe4eab4820bf598f4c279b41fba270159e389a15a6778e6a3c9da2073245c64a",
             {"glitchcore/core/GlitchCore.class"}),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            rows = cast("list[dict[str, str]]", json.loads(raw))
            assert {r["class"] for r in rows} == expected
            for row in rows:
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class_sha256"] == hashlib.sha256(
                    archive.read(row["class"])).hexdigest()
                assert row["disassembly_sha256"] == hashlib.sha256(
                    (directory / row["disassembly"]).read_bytes()).hexdigest()
