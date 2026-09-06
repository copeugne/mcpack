from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_puzzles_lib_membership_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "PuzzlesLib-v21.1.52-1.21.1-NeoForge.jar")
    assert source.sha256 == "00069866c4c6bb67ee5192d1b425d46e6a1601dc598e61bd10b67ba5fa8b029c"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    prefix = "fuzs/puzzleslib/"
    entries = {prefix + "neoforge/impl/PuzzlesLibNeoForge.class",
               prefix + "neoforge/impl/client/PuzzlesLibNeoForgeClient.class"}
    services = {"META-INF/services/fuzs.puzzleslib." + n for n in (
        "api.core.v1.ModLoaderEnvironment", "impl.client.core.proxy.ClientProxyImpl",
        "impl.core.proxy.ProxyImpl")}
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 951
        assert files - classes == services | {
            "META-INF/MANIFEST.MF", "CHANGELOG.md", "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml", "mod_banner.png", "mod_logo.png", "pack.mcmeta",
            "puzzleslib.common.mixins.json", "puzzleslib.common.refmap.json",
            "puzzleslib.neoforge.mixins.json", "puzzleslib.neoforge.refmap.json"}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert {c["config"] for c in cast("list[dict[str, str]]", metadata["mixins"])} == {
            "puzzleslib.common.mixins.json", "puzzleslib.neoforge.mixins.json"}
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == entries
        expected = entries | {prefix + n + ".class" for n in (
            "impl/PuzzlesLib", "impl/PuzzlesLibMod", "impl/core/proxy/ProxyImpl",
            "neoforge/impl/core/NeoForgeProxy",
            "neoforge/impl/event/NeoForgeEventInvokerRegistryImpl")}
        for name in services:
            expected.add(archive.read(name).decode().strip().replace(".", "/") + ".class")
        for label, count, client_count, server_count in (
            ("common", 3, 3, 2), ("neoforge", 10, 2, 0),
        ):
            config = cast("dict[str, object]",
                          json.loads(archive.read(f"puzzleslib.{label}.mixins.json")))
            common = cast("list[str]", config["mixins"])
            server = cast("list[str]", config.get("server", []))
            assert (len(common), len(cast("list[str]", config["client"])), len(server)) == (
                count, client_count, server_count)
            package = cast("str", config["package"])
            expected.update((package + "." + n).replace(".", "/") + ".class"
                            for n in common + server)
            expected.add(cast("str", config["plugin"]).replace(".", "/") + ".class")
        captured: set[str] = set()
        for label, digest in (
            ("puzzles-lib-provider",
             "c78df917ecd4e021c8aa397744fc270c2769e4408f94cf2eb8b404af0f6e07df"),
            ("puzzles-lib-startup",
             "76e803aeacdd3c17a5ddb4bdcc6e7aba430ba189902f46876d6b1647182ccf4e"),
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
