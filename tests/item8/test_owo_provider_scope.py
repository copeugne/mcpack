from __future__ import annotations

import hashlib
import json
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_owo_provider_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "owo-lib-neoforge-0.12.15.5-beta.1+1.21.jar")
    assert source.sha256 == "de6ed336bd80154b7241a7b3276694befc1c94550add8bcdfe7f82e5172fd13d"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        entries = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in entries if n.endswith(".class")}
        assert len(classes) == 492
        assert not any(n.startswith("data/") or n.endswith(".nbt") for n in entries)
        assert {n for n in entries if n.startswith("META-INF/services/")} == {
            "META-INF/services/javax.annotation.processing.Processor"}
        processor = archive.read("META-INF/services/javax.annotation.processing.Processor")
        assert processor.decode().strip() == "io.wispforest.owo.config.ConfigAP"
        expected = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert len(expected) == 2
        expected.add("io/wispforest/owo/config/ConfigAP.class")
        assert {n for n in entries if n.endswith(".mixins.json")} == {"owo.mixins.json"}
        config = cast("dict[str, object]", json.loads(archive.read("owo.mixins.json")))
        assert not config.get("plugin")
        assert len(cast("list[str]", config["client"])) == 45
        assert len(cast("list[str]", config["mixins"])) == 40
        assert config["server"] == ["MainMixin"]
        package = cast("str", config["package"])
        expected.update((package + "." + n).replace(".", "/") + ".class"
                        for n in [*cast("list[str]", config["mixins"]), "MainMixin"])
        captured: set[str] = set()
        for label, digest in (
            ("owo-entries",
             "5d4ac5b95e8047ffd23ff305976f9001d14d3bd6b3f3abe45bb7f1cbf9f0903d"),
            ("owo-common-hooks",
             "aedab40031f96c7dcb8d27baa79d6bfec800133f1f92339f581c0b1d5d2d30f1"),
            ("owo-delegates",
             "4a3c3c2463c3903b37c3d5c3a17b1b48651924523a5f8a62050897b0ae36f7dd"),
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
        assert len(captured) == 50


def test_owo_nested_payloads() -> None:
    sources = retained_sources(Path.cwd())
    source = next(s for s in sources if s.name == "owo-lib-neoforge-0.12.15.5-beta.1+1.21.jar")
    fabric = next(s for s in sources if s.name == "forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    assert hashlib.sha256(fabric.path.read_bytes()).hexdigest() == fabric.sha256
    members = {
        "endec-0.1.8.1.jar": 112, "fabric-api-base-0.4.42+d1308dedd1.jar": 17,
        "gson-0.1.5.1.jar": 10, "jankson-0.1.5.1.jar": 10,
        "jankson-1.2.2.jar": 42, "netty-0.1.4.1.jar": 6,
    }
    with ZipFile(source.path) as outer:
        assert {n for n in outer.namelist() if n.endswith(".jar")} == {
            "META-INF/jars/" + n for n in members}
        for member, count in members.items():
            with ZipFile(BytesIO(outer.read("META-INF/jars/" + member))) as nested:
                files = {n for n in nested.namelist() if not n.endswith("/")}
                classes = {n for n in files if n.endswith(".class")}
                assert len(classes) == count
                assert not any(n.startswith(("data/", "META-INF/services/")) for n in files)
                assert not any(n.endswith((".nbt", ".jar", ".mixins.json")) for n in files)
                if member.startswith("fabric-api-base-"):
                    with ZipFile(fabric.path) as other_outer:
                        other_raw = other_outer.read(
                            "META-INF/jars/fabric-api-base-0.4.42+d1308ded19.jar")
                    with ZipFile(BytesIO(other_raw)) as other:
                        assert {n: nested.read(n) for n in classes} == {
                            n: other.read(n) for n in other.namelist() if n.endswith(".class")}
                else:
                    assert not any(b"net/minecraft/" in nested.read(n) for n in classes)
                    assert not any(m in nested.read(n) for n in classes for m in (
                        b"Lnet/neoforged/fml/common/Mod;",
                        b"Lnet/neoforged/fml/common/EventBusSubscriber;"))
