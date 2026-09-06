from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_architectury_membership_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "architectury-13.0.8-neoforge.jar")
    assert source.sha256 == "5ec578f814e8cca87aeffa6e424032e78d9ea5ea6b603dd834c2dc13c31141ee"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    prefix = "dev/architectury/"
    entry = prefix + "neoforge/ArchitecturyNeoForge.class"
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 382
        assert files - classes == {
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml", "icon.png", "pack.mcmeta",
            "architectury-common-refmap.json", "architectury-common.mixins.json",
            "architectury.mixins.json"}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert {c["config"] for c in cast("list[dict[str, str]]", metadata["mixins"])} == {
            "architectury-common.mixins.json", "architectury.mixins.json"}
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == {entry}
        expected = {entry} | {prefix + n + ".class" for n in (
            "event/EventHandler", "event/forge/EventHandlerImpl",
            "event/forge/EventHandlerImplCommon",
            "event/forge/EventHandlerImplCommon$ModBasedEventHandler",
            "event/forge/EventHandlerImplServer",
            "event/forge/EventHandlerImplServer$ModBasedEventHandler",
            "registry/level/biome/forge/BiomeModificationsImpl",
            "registry/level/biome/forge/BiomeModificationsImpl$BiomeModifierImpl",
            "networking/SpawnEntityPacket")}
        for name, count, client_count in (
            ("architectury-common.mixins.json", 9, 0), ("architectury.mixins.json", 8, 3),
        ):
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            hooks = cast("list[str]", config["mixins"])
            assert (len(hooks), len(cast("list[str]", config["client"]))) == (count, client_count)
            assert not config.get("server")
            package = cast("str", config["package"])
            expected.update((package + "." + n).replace(".", "/") + ".class" for n in hooks)
            if "plugin" in config:
                expected.add(cast("str", config["plugin"]).replace(".", "/") + ".class")
        captured: set[str] = set()
        for label, digest in (
            ("architectury-provider",
             "74ab5cf158c0e545d102726828fd146a836d24c24010809d2aa02f3a17f672c1"),
            ("architectury-startup",
             "6cba03224fd0a49c2d65ad146c6611943639c7efb3e4b1dbd5bd6fe4968b1fe8"),
            ("architectury-spawn-packet",
             "cb2e12853d525539a7b353dbe9656a6981d22ff735cfb170e25469fc605431e0"),
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
