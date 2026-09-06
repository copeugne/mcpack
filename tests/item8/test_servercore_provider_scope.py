from __future__ import annotations

import hashlib
import json
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_servercore_provider_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "servercore-neoforge-1.5.17+1.21.1.jar")
    assert source.sha256 == "5d3b3ac3fc61ef304af929cec2637481eed211fc694d6074258e02abbcfe3467"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        entries = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in entries if n.endswith(".class")}
        assert len(classes) == 692
        assert not any(n.startswith("data/") or n.endswith(".nbt") for n in entries)
        services = {n for n in entries if n.startswith("META-INF/services/")}
        assert len(services) == 4
        expected = {archive.read(n).decode().strip().replace(".", "/") + ".class"
                    for n in services}
        automatic = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert automatic == {"me/wesley1808/servercore/neoforge/common/ServerCoreNeoForge.class"}
        expected.update(automatic)
        assert {n for n in entries if n.endswith(".mixins.json")} == {
            "servercore.common.mixins.json"}
        config = cast("dict[str, object]", json.loads(
            archive.read("servercore.common.mixins.json")))
        assert not config.get("client")
        assert not config.get("server")
        assert config["plugin"] == "me.wesley1808.servercore.mixin.ServerCoreMixinPlugin"
        expected.add(cast("str", config["plugin"]).replace(".", "/") + ".class")
        hooks = cast("list[str]", config["mixins"])
        assert len(hooks) == 60
        package = cast("str", config["package"])
        expected.update((package + "." + n).replace(".", "/") + ".class" for n in hooks)
        nested_counts = {
            "META-INF/jars/dazzleconf-core-1.3.0-M2.jar": 119,
            "META-INF/jars/dazzleconf-ext-snakeyaml-1.3.0-M2.jar": 16,
            "META-INF/jars/snakeyaml-2.6.jar": 237}
        assert {n for n in entries if n.endswith(".jar")} == set(nested_counts)
        for name, count in nested_counts.items():
            with ZipFile(BytesIO(archive.read(name))) as nested:
                files = {n for n in nested.namelist() if not n.endswith("/")}
                library_classes = {n for n in files if n.endswith(".class")}
                assert len(library_classes) == count
                assert not any(n.startswith(("data/", "META-INF/services/")) for n in files)
                assert not any(n.endswith((".jar", ".nbt", ".mixins.json")) for n in files)
                assert not any(b"net/minecraft/" in nested.read(n) for n in library_classes)
        captured: set[str] = set()
        for label, digest in (
            ("servercore-entries",
             "a6d8b88a096224c94e16092de36f70c5b082333b7d8200511480e1df81abae51"),
            ("servercore-feature-hooks",
             "431aac7308956b597f7ed103bc0ffa51ee84864516501e54f14e8ec3370bfb24"),
            ("servercore-optimization-hooks",
             "4c0b0255eb5ea4a2aad601ccd9f918168803c331a1954bb97eb62efd75a9944e"),
            ("servercore-lifecycle",
             "a56b6cd495a2513f8dc23e0982526a9eb85cb18866260821059dc66ea7de8c4c"),
            ("servercore-dynamic-settings",
             "89ca2250b255166ddc1e54c4628d33b97b7de6e65a756f45e4b72acc173cfa16"),
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
        assert len(captured) == 70
