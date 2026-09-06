from __future__ import annotations

import hashlib
import json
import tomllib
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_cristellib_membership_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "cristellib-neoforge-1.21.1-3.1.7.jar")
    assert source.sha256 == "11e05dbc97bd3fe1790bd6361747240e314c1dbf40b590ea20cc691dc8396c38"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    prefix = "de/cristelknight/cristellib/"
    entries = {prefix + "neoforge/CristelLibNeoForge.class",
               prefix + "neoforge/client/CristelLibNeoForgeClient.class"}
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 95
        assert files - classes == {
            "META-INF/MANIFEST.MF", "LICENSE", "META-INF/neoforge.mods.toml", "pack.png",
            "META-INF/jarjar/metadata.json", "META-INF/jars/jankson-1.2.3.jar",
            "cristellib-common-1.21.1-common-refmap.json", "cristellib-common.mixins.json",
            "cristellib.mixins.json", *(f"assets/cristellib/lang/{n}.json"
                                       for n in ("en_us", "pt_br", "zh_cn"))}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert metadata["mixins"] == [{"config": "cristellib-common.mixins.json"}]
        common = cast("dict[str, object]",
                      json.loads(archive.read("cristellib-common.mixins.json")))
        assert common["mixins"] == []
        assert common["client"] == ["PackSelectionScreenMixin"]
        extra = cast("dict[str, object]", json.loads(archive.read("cristellib.mixins.json")))
        assert extra["mixins"] == ["PathPackResourcesAccessor"]
        assert extra["client"] == []
        for config in (common, extra):
            assert not any(config.get(k) for k in ("plugin", "server"))
        markers = (b"Lnet/neoforged/fml/common/Mod;",
                   b"Lnet/neoforged/fml/common/EventBusSubscriber;")
        assert {n for n in classes if any(m in archive.read(n) for m in markers)} == entries
        assert {n for n in classes if b"Lde/cristelknight/cristellib/api/CristelPlugin;"
                in archive.read(n)} == {prefix + "api/BuiltInAPI.class"}
        nested = archive.read("META-INF/jars/jankson-1.2.3.jar")
        assert hashlib.sha256(nested).hexdigest() == (
            "16bae7b779763248f5ca596e3f7f44793a635b551359233e982ee8a4072f1670")
        jarjar = cast("dict[str, list[dict[str, object]]]",
                      json.loads(archive.read("META-INF/jarjar/metadata.json")))
        assert [r["path"] for r in jarjar["jars"]] == ["META-INF/jars/jankson-1.2.3.jar"]
        with ZipFile(BytesIO(nested)) as parser:
            names = {n for n in parser.namelist() if not n.endswith("/")}
            code = {n for n in names if n.endswith(".class")}
            assert len(code) == 42
            assert all(n.startswith("blue/endless/jankson/") for n in code)
            assert names - code == {
                "META-INF/MANIFEST.MF", "META-INF/architectury-loom-nesting-metadata.json"}
            assert not any(m in parser.read(n) for n in code for m in (
                *markers, b"net/minecraft/", b"net/neoforged/", b"CristelPlugin"))
        expected = entries | {prefix + n + ".class" for n in (
            "CristelLib", "CristelLibRegistry", "autoconfig/ModFinder",
            "builtinpacks/BuiltInPackLoader", "builtinpacks/RuntimePack",
            "neoforge/PlatformHelperImpl", "neoforge/extraapiutil/APIFinder",
            "neoforge/mixin/PathPackResourcesAccessor", "StructureConfig", "util/Util",
            "data/ReadData", "StructureConfigToggle", "StructureConfigPlacement",
            "data/condition/ConditionNode", "data/condition/ConditionRegistry",
            "data/condition/conditions/ModLoadedCondition", "neoforge/ModLoadingUtilImpl",
            "api/BuiltInAPI")}
        captured: set[str] = set()
        for label, digest in (
            ("provider", "e6ef7ec929f496a08887bd704480e3523c9bb7f4fdf2c6352b712c4281fafd9e"),
            ("writers", "cf2b2a4ef6e3965343d69b694eac128f554668ec354491fb0280aa394845bd2d"),
            ("set-writers", "710a8a7a2c265c7e41b10177367ce927644e5b9d7f3cfe9bffcabeb56191ff01"),
            ("conditions", "978790f35e5af270a4b6949b6e1c80b6780b5506a129d1d2c6e202bb58484afe"),
            ("builtin", "e1a8ad79183b283beab90e8a4c6571a84f3dc7d128ea8262ecf0e6f5db2220f3"),
        ):
            directory = Path("evidence/item-8/sources") / ("cristellib-" + label)
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                captured.add(row["class"])
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                assert row["disassembly_sha256"] == hashlib.sha256(
                    (directory / row["disassembly"]).read_bytes()).hexdigest()
        assert captured == expected
