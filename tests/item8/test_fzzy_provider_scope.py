from __future__ import annotations

import hashlib
import json
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_fzzy_provider_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "fzzy_config-0.7.6+1.21+neoforge.jar")
    assert source.sha256 == "4e5cc1438087b0bc0276969e88b9ad0bdf2bcc60d6caf5fe79e18947d7a29050"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        entries = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in entries if n.endswith(".class")}
        assert len(classes) == 755
        assert not any(n.startswith(("data/", "META-INF/services/")) for n in entries)
        assert not any(n.endswith((".nbt", ".mixins.json")) for n in entries)
        nested = {
            "META-INF/jars/jankson-1.2.3.jar": (
                "7a71dd9c4ac20cea37ce19c35c4aeda15385a40f31836b0058ff18f9e9554aad", 42),
            "META-INF/jars/tomlkt-jvm-0.3.7.jar": (
                "c996b2dee0bf7be1d9d962e944d13510331092cf5687fddcc0523aba4eadfe4f", 139),
        }
        assert {n for n in entries if n.endswith(".jar")} == set(nested)
        for name, (digest, count) in nested.items():
            raw_nested = archive.read(name)
            assert hashlib.sha256(raw_nested).hexdigest() == digest
            with ZipFile(BytesIO(raw_nested)) as library:
                files = {n for n in library.namelist() if not n.endswith("/")}
                library_classes = {n for n in files if n.endswith(".class")}
                assert len(library_classes) == count
                assert all(n.startswith("META-INF/") for n in files - library_classes)
                assert not any(n.startswith("META-INF/services/") for n in files)
                assert not any(b"net/minecraft/" in library.read(n) for n in library_classes)
        expected = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert expected == {
            "me/fzzyhmstrs/fzzy_config/FzzyConfigNeoForge.class",
            "me/fzzyhmstrs/fzzy_config/FzzyConfigNeoForgeClient.class"}
        captured: set[str] = set()
        for label, digest in (
            ("fzzy-provider",
             "a5d373218b1ed79fd349e2f329c911da42358bae5f67636bf2bdb5b859d12811"),
            ("fzzy-delegates",
             "99281fc1128f2e399175b18e758391429143a955706256519cb1e79acaa595a8"),
            ("fzzy-registrations",
             "9ba43a7c31efdd79947956bc6c9ff1ed7e3f249b4a5a98f94728d8ed4cd691eb"),
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
        assert len(captured) == 8
