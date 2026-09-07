from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_terrablender_membership_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "TerraBlender-neoforge-1.21.1-4.1.0.8.jar")
    assert source.sha256 == "0c49b5ef447a7f09100e9a210888a7347fbda0aa75322063991f6063b25fe3f9"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 63
        assert files - classes == {
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml", "pack.mcmeta", "tb_icon.png", "tb_logo.png",
            "terrablender.accesswidener", "terrablender.mixins.json",
            "terrablender_neoforge.mixins.json",
            "data/terrablender/tags/dimension_type/nether_regions.json",
            "data/terrablender/tags/dimension_type/overworld_regions.json",
            "data/terrablender/worldgen/biome/deferred_placeholder.json",
            *(f"assets/terrablender/lang/{locale}.json" for locale in (
                "de_de", "en_gb", "en_us", "pt_br", "ru_ru", "sv_se", "tr_tr", "uk_ua")),
        }
        for name, dimension in (("nether", "the_nether"), ("overworld", "overworld")):
            assert json.loads(archive.read(
                f"data/terrablender/tags/dimension_type/{name}_regions.json")) == {
                    "replace": False, "values": [f"minecraft:{dimension}"]}
        biome = cast("dict[str, object]", json.loads(archive.read(
            "data/terrablender/worldgen/biome/deferred_placeholder.json")))
        assert biome["features"] == []
        assert biome["carvers"] == {}
        assert all(v == [] for v in cast("dict[str, object]", biome["spawners"]).values())
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        declarations = cast("list[dict[str, str]]", metadata["mixins"])
        assert {r["config"] for r in declarations} == {
            "terrablender.mixins.json", "terrablender_neoforge.mixins.json"}
        hooks: set[str] = set()
        for name, count, clients in (("terrablender.mixins.json", 10, 1),
                                     ("terrablender_neoforge.mixins.json", 0, 0)):
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            assert not config.get("plugin")
            assert not config.get("server")
            declared = cast("list[str]", config["mixins"])
            assert len(declared) == count
            assert len(cast("list[str]", config["client"])) == clients
            hooks.update("terrablender/mixin/" + n + ".class" for n in declared)
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == {"terrablender/core/TerraBlenderNeoForge.class"}
        for label, digest, expected in (
            ("terrablender-provider",
             "9b97ec0fcf96fdafc905d63d11397ef8caf502f9930d32ac7a470e86977c7875",
             hooks | {"terrablender/" + n + ".class" for n in (
                 "core/TerraBlender", "core/TerraBlenderNeoForge",
                 "handler/InitializationHandler")}),
            ("terrablender-level-init",
             "53230a431dda07c58b9c5be768a13002a9bcc40d4e846bda2346a3578747b8ab",
             {"terrablender/util/LevelUtils.class"}),
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
