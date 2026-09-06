from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_yigd_provider_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "youre-in-grave-danger-neoforge-2.0.13.jar")
    assert source.sha256 == "dd2142a3c6a9d5b990ab36220be482f7aa9f528755f93b8fef8996f509ddcda2"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        entries = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in entries if n.endswith(".class")}
        assert len(classes) == 142
        assert not any(n.endswith((".nbt", ".jar")) for n in entries)
        assert not any(n.startswith("META-INF/services/") for n in entries)
        assert Counter("/".join(n.split("/")[:3]) for n in entries
                       if n.startswith("data/")) == {
            "data/botania/tags": 1, "data/c/tags": 1, "data/ftbchunks/tags": 2,
            "data/inventorytabs/tags": 1, "data/minecraft/tags": 5,
            "data/twilightforest/tags": 1, "data/yigd/custom": 3,
            "data/yigd/enchantment": 2, "data/yigd/loot_table": 1,
            "data/yigd/recipes": 1, "data/yigd/tags": 11}
        graveyard = cast("dict[str, object]", json.loads(
            archive.read("data/yigd/custom/graveyard.json")))
        assert graveyard["coordinates"] == []
        areas = cast("dict[str, object]", json.loads(
            archive.read("data/yigd/custom/grave_areas.json")))
        assert areas["values"] == []
        assert "data/yigd/loot_table/blocks/grave.json" in entries
        automatic = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert automatic == {
            "com/b1n_ry/yigd/Yigd.class", "com/b1n_ry/yigd/client/YigdClient.class"}
        expected = set(automatic)
        assert {n for n in entries if n.endswith(".mixins.json")} == {"yigd.mixins.json"}
        config = cast("dict[str, object]", json.loads(archive.read("yigd.mixins.json")))
        assert not config.get("plugin")
        hooks = cast("list[str]", config["mixins"])
        server_hooks = cast("list[str]", config["server"])
        assert len(hooks) == 4
        assert server_hooks == ["DedicatedServerMixin"]
        package = cast("str", config["package"])
        expected.update((package + "." + n).replace(".", "/") + ".class"
                        for n in [*hooks, *server_hooks])
        captured: set[str] = set()
        for label, digest in (
            ("yigd-entries",
             "b394f2d7ad375315dcc45058385b7a87f61e3271938bf8b2f0903f8e5ee2a5fe"),
            ("yigd-delegates",
             "08214afb2c7f64e433c24feff30c9d7e910aff9ce5bc4dc0c83b1e9fa4723174"),
            ("yigd-resources",
             "e4ded8871588e2161f81da4bf58624c3ccacd60a223a03b1f5b3aca6c701ec77"),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            expected_files = {directory / "identities.json", directory / "README.md"}
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                captured.add(row["class"])
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                target = directory / row["disassembly"]
                assert target.resolve().is_relative_to(directory.resolve())
                assert hashlib.sha256(target.read_bytes()).hexdigest() == row["disassembly_sha256"]
                expected_files.add(target)
            assert {p for p in directory.rglob("*") if p.is_file()} == expected_files
        assert expected <= captured
        assert len(captured) == 13
