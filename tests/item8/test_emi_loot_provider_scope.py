from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_emi_loot_membership_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "emi_loot-0.7.9+1.21+neoforge.jar")
    assert source.sha256 == "a89805cdcb2e11734624d7239112643ee6b8f95e6b71b3a720530df6a5c18980"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    prefix = "fzzyhmstrs/emi_loot/"
    entries = {prefix + "neoforge/EMILootNeoForge.class", *(prefix + "neoforge/events/" + n
               + ".class" for n in (
                   "EMILootGameEvents", "EMILootClientGameEvents", "EMILootClientModEvents"))}
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 209
        assets = {n for n in files if n.startswith("assets/")}
        assert len(assets) == 90
        assert all((n.startswith("assets/emi_loot/textures/gui/") and n.endswith(".png"))
                   or n in {"assets/emi/category/properties/emi_loot_categories.json",
                            "assets/emi_loot/entity_fixers/vanilla_mob_fixers.json",
                            *(f"assets/emi_loot/lang/{lang}.json" for lang in (
                                "en_us", "es_mx", "ru_ru", "zh_cn"))} for n in assets)
        data = {f"data/minecraft/direct_drops/entities/{n}.json" for n in (
            "creeper", "drowned", "evoker", "husk", "piglin", "piglin_brute", "pillager",
            "skeleton", "stray", "vindicator", "wither", "wither_skeleton", "zombie",
            "zombie_villager", "zombified_piglin")}
        assert files - classes - assets == data | {
            "data/emi_loot/emi_loot_data/table_exclusions.json", "META-INF/MANIFEST.MF",
            "META-INF/accesstransformer.cfg", "META-INF/neoforge.mods.toml",
            "emi_loot-xplat-refmap.json", "emi_loot.accesswidener", "emi_loot.mixins.json",
            "icon.png"}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert metadata["mixins"] == [{"config": "emi_loot.mixins.json"}]
        config = cast("dict[str, object]", json.loads(archive.read("emi_loot.mixins.json")))
        assert config["package"] == "fzzyhmstrs.emi_loot.mixins"
        assert not any(config.get(k) for k in ("plugin", "server", "client"))
        hooks = {prefix + "mixins/" + n + ".class"
                 for n in cast("list[str]", config["mixins"])}
        assert len(hooks) == 40
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == entries
        expected = entries | hooks | {prefix + n + ".class" for n in (
            "EMILoot", "neoforge/EMILootAgnosNeoForge", "server/ServerResourceData",
            "server/LootBuilder", "parser/LootTableParser")}
        captured: set[str] = set()
        for label, digest in (
            ("emi-loot-provider",
             "30d1b35994e3b901231cf0a42e4830a1e851e8e8dbf2801164b656ca15cc5196"),
            ("emi-loot-parser",
             "f7964ccca52ce3e55ab0da2082ef43bf55f047b021ce0af3c7501cecb3ba592b"),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            rows = cast("list[dict[str, str]]", json.loads(raw))
            for row in rows:
                captured.add(row["class"])
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                text = (directory / row["disassembly"]).read_bytes()
                assert row["disassembly_sha256"] == hashlib.sha256(text).hexdigest()
                if row["class"].endswith("Accessor.class"):
                    body = text.decode().split("\n{", 1)[1].split("\n}", 1)[0]
                    assert "org.spongepowered.asm.mixin.gen.Accessor" in body or (
                        "org.spongepowered.asm.mixin.gen.Invoker" in body)
                    assert "org.spongepowered.asm.mixin.injection" not in body
                    if "LootContextTypesAccessor" not in row["class"]:
                        assert "Code:" not in body
                    else:
                        assert "java/lang/UnsupportedOperationException" in body
        assert captured == expected
