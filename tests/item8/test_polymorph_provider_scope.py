from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_polymorph_membership_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "polymorph-neoforge-1.1.0+1.21.1.jar")
    assert source.sha256 == "bec8118978adeb052de9c4eaf9a595830621d82515a764f32f9c8a4dd52ab94b"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    prefix = "com/illusivesoulworks/polymorph/"
    entry = prefix + "PolymorphNeoForgeMod.class"
    services = {"META-INF/services/com.illusivesoulworks.polymorph.platform.services." + n
                for n in ("IClientPlatform", "IIntegrationPlatform", "IPlatform")}
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 98
        assert files - classes == services | {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "polymorph_icon.png",
            "polymorph.mixins.json", "polymorph-compatibility.neoforge.mixins.json",
            "polymorph-compatibility.mixins.json", "pack.mcmeta", "LICENSE", "COPYING",
            "COPYING.LESSER", "README.md", "CHANGELOG.md",
            *(f"assets/polymorph/lang/{n}.json" for n in (
                "ru_ru", "hr_hr", "zh_tw", "uk_ua", "zh_cn", "ko_kr", "es_es", "de_ch",
                "fr_fr", "de_at", "es_mx", "it_it", "pt_br", "en_us", "de_de", "tr_tr")),
            *(f"assets/polymorph/textures/gui/sprites/{n}{suffix}.png"
              for n in ("selector_button", "output_button", "current_output")
              for suffix in ("", "_highlighted"))}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert {c["config"] for c in cast("list[dict[str, str]]", metadata["mixins"])} == {
            "polymorph.mixins.json", "polymorph-compatibility.mixins.json",
            "polymorph-compatibility.neoforge.mixins.json"}
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == {entry}
        expected = {entry} | {prefix + n + ".class" for n in (
            "PolymorphCommonMod", "common/PolymorphNeoForgeCapabilities",
            "common/CommonEventsListener", "common/network/ServerPayloadHandler",
            "common/integration/PolymorphIntegrations", "common/PolymorphCommonEvents",
            "common/integration/fastbench/FastBenchModule", "common/util/BlockEntityTicker")}
        for name in services:
            expected.add(archive.read(name).decode().strip().replace(".", "/") + ".class")
        for name, count in (
            ("polymorph.mixins.json", 15), ("polymorph-compatibility.mixins.json", 3),
            ("polymorph-compatibility.neoforge.mixins.json", 2),
        ):
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            hooks = cast("list[str]", config["mixins"])
            assert len(hooks) == count
            assert not config.get("server")
            package = cast("str", config["package"])
            expected.update((package + "." + n).replace(".", "/") + ".class" for n in hooks)
            if "plugin" in config:
                assert config["plugin"] == (
                    "com.illusivesoulworks.polymorph.mixin.IntegratedMixinPlugin")
                expected.add(prefix + "mixin/IntegratedMixinPlugin.class")
        captured: set[str] = set()
        for label, digest in (
            ("polymorph-provider",
             "859c8ec69e6a3db415b633697ab588e0f874b69a69cfaca6440743e5ca07476a"),
            ("polymorph-startup",
             "207ccce94b3e276463b7659307cc80a4e1c15b122e6f4e86d56ff6c3ab107e05"),
            ("polymorph-events",
             "a37f284baa4eff32985d132cc896d54c53141bb0b8e4cd916792fe9a49275a49"),
            ("polymorph-ticker",
             "4c2aec52aa80a246dfbaf8db7c24aebc2cd91c8de42cce63cc76cd5d3ca66602"),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            rows = cast("list[dict[str, str]]", json.loads(raw))
            for row in rows:
                captured.add(row["class"])
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                assert row["disassembly_sha256"] == hashlib.sha256(
                    (directory / row["disassembly"]).read_bytes()).hexdigest()
        assert captured == expected
