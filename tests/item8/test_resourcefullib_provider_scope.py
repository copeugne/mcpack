from __future__ import annotations

import hashlib
import json
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_resourcefullib_provider_membership() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "resourcefullib-neoforge-1.21-3.0.12.jar")
    assert source.sha256 == "5e36f2c69de008dc5795f730c84ab767688f15c810944b585485349a0c911261"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        entries = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in entries if n.endswith(".class")}
        assert len(classes) == 222
        assert not any(n.startswith(("data/", "META-INF/services/")) or n.endswith(".nbt")
                       for n in entries)
        assert {n for n in entries if n.endswith(".jar")} == {
            "META-INF/jars/bytecodecs-1.1.2.jar", "META-INF/jars/yabn-1.0.3.jar"}
        for member, count in (("bytecodecs-1.1.2.jar", 54), ("yabn-1.0.3.jar", 26)):
            with ZipFile(BytesIO(archive.read("META-INF/jars/" + member))) as nested:
                files = {n for n in nested.namelist() if not n.endswith("/")}
                code = {n for n in files if n.endswith(".class")}
                assert len(code) == count
                assert files - code == {"META-INF/MANIFEST.MF"}
                assert not any(b"net/minecraft/" in nested.read(n) for n in code)
        expected = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert expected == {
            "com/teamresourceful/resourcefullib/neoforge/ResourcefulLibNeoForge.class"}
        assert {n for n in entries if n.endswith(".mixins.json")} == {"resourcefullib.mixins.json"}
        config = cast("dict[str, object]", json.loads(archive.read("resourcefullib.mixins.json")))
        assert not config.get("plugin")
        assert not config.get("server")
        assert not config.get("client")
        assert config["mixins"] == ["ResourcefulFlowingFluidMixin"]
        package = cast("str", config["package"])
        expected.add(package.replace(".", "/") + "/ResourcefulFlowingFluidMixin.class")
        captured: set[str] = set()
        for label, digest in (
            ("resourcefullib-provider",
             "9ff04ca7c852f6db9ddff805d56a56c3a0978a2c681e8ebdb1267ffeb3d2af9f"),
            ("resourcefullib-startup",
             "4f0c368751adf3de24c46be01bac5bebcfabe62347c6ddc9f5617fd0f66f1ac9"),
            ("resourcefullib-storage",
             "46287b67e6639ab6c2221f5ef5cab188c0ee46182920254ca63a84ab5353aa7a"),
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
        assert len(captured) == 6
