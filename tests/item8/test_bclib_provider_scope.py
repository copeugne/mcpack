from __future__ import annotations

import hashlib
import json
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_bclib_membership_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "bclib-21.0.24.jar")
    assert source.sha256 == "a7efd02dd3409dbac9c8455c5ed4fa4ca340e2af1c39f211038198dfa1c92093"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 627
        assert Counter(n.split("/")[2] for n in files if n.startswith("assets/bclib/")) == {
            "lang": 8, "patterns": 52, "textures": 6, "models": 23, "blockstates": 4,
            "materialmaps": 1, "materials": 1, "betterx.png": 1, "header.png": 1,
            "icon.png": 1, "iconpixelated.png": 1, "icon_betterend.png": 1,
            "icon_betternether.png": 1, "icon_bright.png": 1, "icon_updater.png": 1}
        assert {n for n in files if n.startswith("data/")} == {
            "data/bclib/config/recipes.json",
            "data/bclib/tags/block/bonemeal/source/netherrack.json",
            *("data/bclib/tags/block/bonemeal/target/" + n + ".json"
              for n in ("end_stone", "netherrack", "obsidian"))}
        assert files - classes - {n for n in files if n.startswith(("assets/", "data/"))} == {
            "LICENSE", "LICENSE.ASSETS", "META-INF/MANIFEST.MF",
            "META-INF/accesstransformer.cfg", "META-INF/jarjar/metadata.json",
            "META-INF/jarjar/mixinextras-neoforge-0.5.0.jar", "META-INF/neoforge.mods.toml",
            "bclib.mixins.client.json", "bclib.mixins.common.json", "bclib.refmap.json",
            "ui.mixins.client.json"}
        automatic = {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert len(automatic) == 9
        common = cast("dict[str, object]", json.loads(archive.read("bclib.mixins.common.json")))
        assert len(cast("list[str]", common["mixins"])) == 35
        assert not common.get("plugin")
        assert not common.get("server")
        expected = automatic | {
            (cast("str", common["package"]) + "." + n).replace(".", "/") + ".class"
            for n in cast("list[str]", common["mixins"])}
        for label, count in (("bclib.mixins.client.json", 13), ("ui.mixins.client.json", 0)):
            config = cast("dict[str, object]", json.loads(archive.read(label)))
            assert len(cast("list[str]", config["client"])) == count
            assert not any(config.get(k) for k in ("plugin", "mixins", "server"))
        captured: set[str] = set()
        for label, digest in (
            ("bclib-integration-dispatch",
             "d085183016dd793119d9f8bbab449fbbc791851dce4ea8244e18da2e9aa4af2c"),
            ("bclib-generation-entry",
             "6e3641e3a2aa875328b5db7a2af8374c61e8e3f15075ca6e71fa95c8d3c90365"),
            ("bclib-provider-entry",
             "92b75f9b0a82c47cfbc2be5f2fe3606e4894ba90b8d5fe922e30af908eb4b56a"),
            ("bclib-post-init",
             "655110f279def6342e06afd6adbabd856a66474899d3e38ae20d18ee3e9266ad"),
            ("bclib-common-hooks",
             "909cc6737418099310e6cabfedcc22048e089b2fc1c386946ff00847f7e9447f"),
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
        assert len(captured) == 50


def test_bclib_nested_mixinextras_membership() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "bclib-21.0.24.jar")
    nested = "META-INF/jarjar/mixinextras-neoforge-0.5.0.jar"
    with ZipFile(source.path) as parent:
        payload = parent.read(nested)
    digest = "9c617719248f8b89847348fc7ea5e705739c147ae5e172551264d225bc9f2507"
    assert hashlib.sha256(payload).hexdigest() == digest
    with ZipFile(BytesIO(payload)) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 503
        assert files - classes == {
            "META-INF/MANIFEST.MF", "mixinextras.init.mixins.json", "LICENSE_MixinExtras",
            "META-INF/services/javax.annotation.processing.Processor"}
        assert not any(b"net/minecraft/" in archive.read(n) for n in classes)
        config = cast("dict[str, object]", json.loads(archive.read("mixinextras.init.mixins.json")))
        assert not any(config.get(k) for k in ("mixins", "client", "server"))
        directory = Path("evidence/item-8/sources/bclib-mixinextras-entry")
        raw = (directory / "identities.json").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == (
            "0a86d854b1de84af1cbffd2c9e1dd4ff1a47a9ff01197773667b9fdae2a1490a")
        rows = cast("list[dict[str, str]]", json.loads(raw))
        assert len(rows) == 1
        row = rows[0]
        assert row["class"] == cast("str", config["plugin"]).replace(".", "/") + ".class"
        assert row["archive"] == source.name + "!/" + nested
        assert row["archive_sha256"] == digest
        assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
        assert row["disassembly_sha256"] == hashlib.sha256(
            (directory / row["disassembly"]).read_bytes()).hexdigest()
