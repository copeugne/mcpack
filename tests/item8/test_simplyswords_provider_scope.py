from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_simplyswords_provider_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "simplyswords-neoforge-1.63.0-1.21.1.jar")
    assert source.sha256 == "4619dcf1501fc82c1a52acd4c88a466436f5c1d7d2bccc0932912a12b0bc5198"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        entries = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in entries if n.endswith(".class")}
        assert len(classes) == 286
        assert not any(n.endswith((".nbt", ".jar")) for n in entries)
        assert not any(n.startswith("META-INF/services/") for n in entries)
        assert Counter("/".join(n.split("/")[:3]) for n in entries
                       if n.startswith("data/")) == {
            "data/c/tags": 4, "data/levelz/item": 358, "data/minecraft/tags": 6,
            "data/mythicmetals/tags": 27, "data/simplyswords/advancement": 47,
            "data/simplyswords/disabled_recipes": 317, "data/simplyswords/loot_tables": 1,
            "data/simplyswords/patchouli_books": 1, "data/simplyswords/recipe": 375,
            "data/simplyswords/recipes": 1, "data/simplyswords/safeload_recipes": 2,
            "data/simplyswords/tags": 55, "data/simplyswords/weapon_attributes": 420}
        automatic = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert automatic == {
            "net/sweenus/simplyswords/neoforge/SimplySwordsForge.class",
            "net/sweenus/simplyswords/neoforge/client/SimplySwordsClientForge.class"}
        expected = set(automatic)
        assert {n for n in entries if n.endswith(".mixins.json")} == {
            "simplyswords-common.mixins.json", "simplyswords.mixins.json"}
        for name in ("simplyswords-common.mixins.json", "simplyswords.mixins.json"):
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            assert not config.get("plugin")
            assert not config.get("server")
            hooks = cast("list[str]", config["mixins"])
            assert len(hooks) == (4 if name == "simplyswords-common.mixins.json" else 0)
            package = cast("str", config["package"])
            expected.update((package + "." + n).replace(".", "/") + ".class" for n in hooks)
        captured: set[str] = set()
        for label, digest in (
            ("simplyswords-entries",
             "3dfcec4b5d6d6978a0ecd4e7ac17effacc71008592940006b42c2d408ee40bb4"),
            ("simplyswords-startup",
             "17ec45c9e55db05245359455f3095ef76371a92b7a2a346fda4dc47dcbeae5c8"),
            ("simplyswords-content-delegates",
             "fff0b8605559f05fb254ebed2018fc99eae5ea6575ed138584260234779d5017"),
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
        assert len(captured) == 11
