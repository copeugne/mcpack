from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_curios_provider_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "curios-neoforge-9.5.1+1.21.1.jar")
    assert source.sha256 == "a45df2125c26219974aba7507ffc9afe7b83acc941a386af3faacb1cc0056fde"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        entries = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in entries if n.endswith(".class")}
        assert len(classes) == 152
        assert not any(n.endswith((".jar", ".nbt")) for n in entries)
        assert {n for n in entries if n.startswith("data/")} == {
            "data/curios/curios/slots/" + name + ".json" for name in (
                "back", "belt", "body", "bracelet", "charm", "curio", "hands", "head",
                "necklace", "ring")}
        services = {n for n in entries if n.startswith("META-INF/services/")}
        assert services == {
            "META-INF/services/top.theillusivec4.curios.platform.services.ICuriosPlatform"}
        expected = {archive.read(n).decode().strip().replace(".", "/") + ".class"
                    for n in services}
        assert expected == {"top/theillusivec4/curios/platform/NeoForgeCurios.class"}
        automatic = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert len(automatic) == 2
        expected.update(automatic)
        configs = {n for n in entries if n.endswith(".mixins.json")}
        assert configs == {"curios.mixins.json", "curios.neoforge.mixins.json"}
        hooks: set[str] = set()
        for name in configs:
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            assert not config.get("plugin")
            assert not config.get("server")
            assert not config.get("client")
            package = cast("str", config["package"])
            hooks.update((package + "." + n).replace(".", "/") + ".class"
                         for n in cast("list[str]", config["mixins"]))
        assert len(hooks) == 13
        expected.update(hooks)
        captured: set[str] = set()
        for label, digest in (
            ("curios-provider",
             "e1d8df4787a575099d1181f4519104940bc0d87e29d46c1fb236c3e7129b0270"),
            ("curios-delegates",
             "adeafdb6ec29b32e3832bbc4f091eecbe55996415ac6dac88e67cc8c8e41f6a9"),
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
        assert len(captured) == 24
