from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_amendments_provider_membership() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "amendments-1.21-2.0.15-neoforge.jar")
    assert source.sha256 == "e44e67d5c2eb5a73ee8ca3d1e9099ed20ccbf8167022bc407df8434b1bf362b5"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 252
        data = {n for n in files if n.startswith("data/")}
        assets = {n for n in files if n.startswith("assets/")}
        assert Counter("/".join(n.split("/")[:3]) for n in data) == {
            "data/amendments/blueprint": 3, "data/amendments/damage_type": 1,
            "data/amendments/loot_table": 2, "data/amendments/moonlight": 1,
            "data/amendments/recipe": 3, "data/amendments/tags": 14,
            "data/apotheosis/enchanting_stat": 5, "data/create/tags": 2,
            "data/lychee/tags": 1, "data/minecraft/tags": 14, "data/quark/tags": 1,
            "data/supplementaries/tags": 5}
        assert Counter("/".join(n.split("/")[:3]) for n in assets) == {
            "assets/amendments/blockstates": 34, "assets/amendments/lang": 19,
            "assets/amendments/models": 74, "assets/amendments/particles": 6,
            "assets/amendments/sounds": 4, "assets/amendments/sounds.json": 1,
            "assets/amendments/textures": 186, "assets/minecraft/blockstates": 5,
            "assets/minecraft/models": 3, "assets/minecraft/textures": 3,
            "assets/supplementaries/dynamiclights": 21, "assets/supplementaries/lucent_data": 21,
            "assets/supplementaries/ryoamiclights": 20}
        assert files - classes - data - assets == {
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg", "META-INF/neoforge.mods.toml",
            "amendments-common-refmap.json", "amendments-common.mixins.json",
            "amendments.mixins.json", "icon.png", "pack.mcmeta"}
        entries = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert entries == {"net/mehvahdjukaar/amendments/neoforge/AmendmentsForge.class"}
        expected = set(entries)
        for name, count, client_count in (
            ("amendments-common.mixins.json", 37, 8), ("amendments.mixins.json", 2, 3),
        ):
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            assert not config.get("server")
            hooks = cast("list[str]", config["mixins"])
            assert len(hooks) == count
            assert len(cast("list[str]", config["client"])) == client_count
            package = cast("str", config["package"])
            expected.update((package + "." + n).replace(".", "/") + ".class" for n in hooks)
            expected.add(cast("str", config["plugin"]).replace(".", "/") + ".class")
        for name in data:
            if "/blueprint/" in name:
                definition = cast("dict[str, object]", json.loads(archive.read(name)))
                assert definition["structures"] in {
                    "#amendments:add_potion_cauldron", "#minecraft:village"}
                repaletter = cast("dict[str, object]", definition["repaletter"])
                assert repaletter["type"] == "amendments:blockstate_replace"
                assert repaletter["replaces_block"] in {
                    "minecraft:cauldron", "minecraft:water_cauldron"}
        captured: set[str] = set()
        for label, digest in (
            ("amendments-provider",
             "84c1363924e5567df372406b5fb56053e327b690d7a11a243a58d8e3c0b72b6b"),
            ("amendments-startup",
             "f861ebbe6b01e0593fab776764dc771e6c8f0fadd14dedfc75f067508630d59c"),
            ("amendments-block-replacement",
             "fd304f7b1fe85d565256a827dadd1566f1b83e93d6c84a69c22d312e7c575f50"),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                captured.add(row["class"])
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                assert row["disassembly_sha256"] == hashlib.sha256(
                    (directory / row["disassembly"]).read_bytes()).hexdigest()
        assert expected <= captured
        assert len(captured) == 48
