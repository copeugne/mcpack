from __future__ import annotations

import hashlib
import json
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_kff_payload_boundary() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "kotlinforforge-5.11.0-all.jar")
    assert source.sha256 == "ac827b62ce8fe71760208671b4a694e3ccd35049075f9406a751cffb5a5c9779"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    counts = {
        "kotlin-reflect-2.3.0.jar": 2215, "kotlin-stdlib-2.3.0.jar": 978,
        "kotlin-stdlib-jdk7-2.3.0.jar": 1, "kotlin-stdlib-jdk8-2.3.0.jar": 1,
        "kotlinx-coroutines-core-jvm-1.10.2.jar": 834,
        "kotlinx-coroutines-jdk8-1.10.2.jar": 1,
        "kotlinx-serialization-core-jvm-1.9.0.jar": 229,
        "kotlinx-serialization-json-jvm-1.9.0.jar": 137,
        "thedarkcolour.kfflang-5.11.0.jar": 19,
        "thedarkcolour.kfflib-5.11.0.jar": 46,
        "thedarkcolour.kffmod-5.11.0.jar": 2,
    }
    with ZipFile(source.path) as outer:
        files = {n for n in outer.namelist() if not n.endswith("/")}
        assert files == {"META-INF/jarjar/" + n for n in counts} | {
            "META-INF/MANIFEST.MF", "META-INF/jarjar/metadata.json"}
        for name, count in counts.items():
            with ZipFile(BytesIO(outer.read("META-INF/jarjar/" + name))) as archive:
                entries = {n for n in archive.namelist() if not n.endswith("/")}
                classes = {n for n in entries if n.endswith(".class")}
                assert len(classes) == count
                assert not any(n.startswith("data/") for n in entries)
                assert not any(n.endswith((".nbt", ".jar", ".mixins.json")) for n in entries)
                services = {n for n in entries if n.startswith("META-INF/services/")}
                if name.startswith("kotlin-reflect-"):
                    assert len(services) == 3
                    assert all(n.startswith("META-INF/services/kotlin.reflect.") for n in services)
                    assert all(archive.read(n).decode().startswith("kotlin.reflect.")
                               for n in services)
                elif name.startswith("thedarkcolour.kfflang-"):
                    assert services == {
                        "META-INF/services/net.neoforged.neoforgespi.language.IModLanguageLoader",
                        "META-INF/services/net.minecraftforge.forgespi.language.IModLanguageProvider"}
                else:
                    assert not services
                if not name.startswith("thedarkcolour."):
                    assert not any(b"net/minecraft/" in archive.read(n) for n in classes)
                if name.startswith("thedarkcolour.kfflib-"):
                    assert all(n.startswith("META-INF/") for n in entries - classes)
                    assert not any(m in archive.read(n) for n in classes for m in (
                        b"Lnet/neoforged/fml/common/Mod;",
                        b"Lnet/neoforged/fml/common/EventBusSubscriber;"))


def test_kff_entry_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "kotlinforforge-5.11.0-all.jar")
    with ZipFile(source.path) as outer:
        for member, digest, label, manifest, count in (
            ("thedarkcolour.kfflang-5.11.0.jar",
             "0ecb6b4e3c7101439f386712c073fd2d9c31b75dc3e7aeffdb130c0517b22a72",
             "kff-language", "7aa167a9ab8cb42d77871c7149d8455c2cf9837aeb7c85c1a787d8cf888a0c5e", 4),
            ("thedarkcolour.kffmod-5.11.0.jar",
             "61cf0d7962977ba28ad3cd14e609f4c5d8c3dae880c01598a17c76ad0ee0f9a4",
             "kff-mod", "66a33c92310269a68c6939921fa997abd7b5b366dc3730b278a44e0139c786d2", 2),
        ):
            nested_path = "META-INF/jarjar/" + member
            raw_nested = outer.read(nested_path)
            assert hashlib.sha256(raw_nested).hexdigest() == digest
            with ZipFile(BytesIO(raw_nested)) as archive:
                directory = Path("evidence/item-8/sources") / label
                raw = (directory / "identities.json").read_bytes()
                assert hashlib.sha256(raw).hexdigest() == manifest
                expected_files = {directory / "identities.json", directory / "README.md"}
                captured: set[str] = set()
                for row in cast("list[dict[str, str]]", json.loads(raw)):
                    captured.add(row["class"])
                    assert row["archive"] == source.name + "!/" + nested_path
                    assert row["archive_sha256"] == digest
                    class_hash = hashlib.sha256(archive.read(row["class"])).hexdigest()
                    assert row["class_sha256"] == class_hash
                    target = directory / row["disassembly"]
                    assert target.resolve().is_relative_to(directory.resolve())
                    assert hashlib.sha256(target.read_bytes()).hexdigest() == row[
                        "disassembly_sha256"]
                    expected_files.add(target)
                assert len(captured) == count
                assert {p for p in directory.rglob("*") if p.is_file()} == expected_files
                services = {n for n in archive.namelist()
                            if n.startswith("META-INF/services/") and not n.endswith("/")}
                for name in services:
                    entry = archive.read(name).decode().strip().replace(".", "/") + ".class"
                    assert entry in captured
                if label == "kff-mod":
                    assert captured == {n for n in archive.namelist() if n.endswith(".class")}
