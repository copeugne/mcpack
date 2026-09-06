from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_moonlight_provider_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "moonlight-neoforge-1.21.1-3.0.17.jar")
    assert source.sha256 == "41bbe274c689ef4229892b6e46da57d27dce34a40fe7e2de0c230cd0e2bc0e98"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        entries = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in entries if n.endswith(".class")}
        assert len(classes) == 684
        assert not any(n.endswith((".jar", ".nbt")) for n in entries)
        assert not any(n.startswith("META-INF/services/") for n in entries)
        assert Counter("/".join(n.split("/")[:3]) for n in entries
                       if n.startswith("data/")) == {
            "data/moonlight/moonlight": 19, "data/moonlight/color_sets": 5,
            "data/minecraft/tags": 3, "data/c/tags": 1, "data/moonlight/tags": 1}
        custom = {n for n in entries if n.startswith("data/moonlight/moonlight/")}
        assert len([n for n in custom if "/soft_fluid/" in n]) == 17
        assert {n for n in custom if "/soft_fluid/" not in n} == {
            "data/moonlight/moonlight/token.json",
            "data/moonlight/moonlight/map_marker/generic_structure.json"}
        assert json.loads(archive.read(
            "data/moonlight/moonlight/map_marker/generic_structure.json")) == {}
        expected = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert len(expected) == 2
        configs = {n for n in entries if n.endswith(".mixins.json")}
        assert configs == {"moonlight-common.mixins.json", "moonlight.mixins.json"}
        hooks: set[str] = set()
        for name in configs:
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            assert not config.get("server")
            package = cast("str", config["package"])
            hooks.update((package + "." + n).replace(".", "/") + ".class"
                         for n in cast("list[str]", config["mixins"]))
            if name == "moonlight-common.mixins.json":
                assert config["plugin"] == "net.mehvahdjukaar.moonlight.core.mixins.MixinPlugin"
                expected.add(cast("str", config["plugin"]).replace(".", "/") + ".class")
                assert len(cast("list[str]", config["client"])) == 11
            else:
                assert not config.get("plugin")
                assert len(cast("list[str]", config["client"])) == 7
        assert len(hooks) == 43
        expected.update(hooks)
        captured: set[str] = set()
        for label, digest in (
            ("moonlight-entries",
             "8e3ae9145da3c936b9cb3c38f238ee73b9c215419e6ff52cfd0e213d5ffd9751"),
            ("moonlight-common-hooks",
             "e110a8843fa506d7ebea72c4c231d30993dfaff40aeff4b138cd8a32d241f312"),
            ("moonlight-platform-hooks",
             "a6866cc98941df5676b89ccd4c7d87103bef79c06f6bc96b54493e88011e478f"),
            ("moonlight-startup",
             "a0c685bc98b853a98b61d9f06f79fefb8832c34d6f3d9303a3a77e898f4bfbb1"),
            ("moonlight-generation-delegates",
             "eee5815a67288e010a4d111e5ce759515d13604db6de351e9474be933fb7f3e0"),
            ("moonlight-dynamic-registration",
             "b409463d0d9db29ee765d36879c987e68f26d744b066a0f8f58976bd0d9e05b9"),
            ("supplementaries-shared-plugin",
             "05fbc861b5d5a7e0290ac0bdcd10d29ae1afd2410c7833b97f5fd560a9640e75"),
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
        assert len(captured) == 56
