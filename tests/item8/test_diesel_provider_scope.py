from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_diesel_provider_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "createdieselgenerators-1.21.1-1.3.15.jar")
    assert source.sha256 == "56ef1d574278fc311f1ffa223dbd613077b899354a18d01ae8dca2578a4e2990"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        entries = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in entries if n.endswith(".class")}
        assert len(classes) == 239
        assert not any(n.startswith("META-INF/services/") for n in entries)
        nested = "META-INF/jarjar/sable-companion-common-1.21.1-1.6.0.jar"
        assert {n for n in entries if n.endswith(".jar")} == {nested}
        assert hashlib.sha256(archive.read(nested)).hexdigest() == (
            "873633e35046e3761b277ff8a1ecad0d55d9a3014fa81a0b084c9aecba1f3bed")
        assert Counter("/".join(n.split("/")[:3]) for n in entries if n.startswith("data/")) == {
            "data/c/tags": 8,
            "data/create/tags": 3,
            "data/createdieselgenerators/advancement": 1,
            "data/createdieselgenerators/createdieselgenerators": 5,
            "data/createdieselgenerators/loot_table": 43,
            "data/createdieselgenerators/recipe": 137,
            "data/createdieselgenerators/tags": 5,
            "data/farmersdelight/tags": 1,
            "data/immersiveengineering/tags": 3,
            "data/minecraft/tags": 6,
        }
        templates = {n for n in entries if n.endswith(".nbt")}
        assert len(templates) == 10
        assert all(n.startswith("assets/createdieselgenerators/ponder/") for n in templates)
        expected = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert len(expected) == 3
        assert {n for n in entries if n.endswith(".mixins.json")} == {
            "createdieselgenerators.mixins.json"}
        config = cast("dict[str, object]",
                      json.loads(archive.read("createdieselgenerators.mixins.json")))
        assert not config.get("server")
        assert not config.get("plugin")
        hooks = cast("list[str]", config["mixins"])
        assert len(hooks) == 12
        assert len(cast("list[str]", config["client"])) == 3
        package = cast("str", config["package"])
        expected.update((package + "." + n).replace(".", "/") + ".class" for n in hooks)
        captured: set[str] = set()
        for label, digest in (
            ("diesel-provider",
             "ae941c8805f0a988eed4218a8d7f230e477dae513494e5c18ac2384b96d439d3"),
            ("diesel-registrations",
             "db8380aed38b40f546def69b980f7b9a6b7d47d9783007ea4d770585cbdca398"),
            ("diesel-commands",
             "18d94d199156976c9ac9dbb8cebd5287c99dcee31ff272b70e10c861aecbb522"),
            ("diesel-oil-data",
             "3a526470b2149eb8a87fde6003b6cc7f44134f996c65ad542538115d132960c0"),
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
        assert len(captured) == 32
