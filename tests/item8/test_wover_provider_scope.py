from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_wover_provider_membership() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "worldweaver-21.0.24.jar")
    assert source.sha256 == "cd1a1c247a4870479a64a5ad837a0f42ebfadfcd1507131284eec05a4a6af51e"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 794
        configs = {n for n in files if ".mixins." in n and n.endswith(".json")}
        assert len(configs) == 25
        service = "META-INF/services/org.betterx.wover.core.api.registry.DatapackRegistryEntrypoint"
        assets = {n for n in files if n.startswith("assets/")}
        assert Counter("/".join(n.split("/")[:3]) for n in assets) == {
            "assets/wover/lang": 3, "assets/wover/models": 1,
            "assets/wover-generator/lang": 2, "assets/wover-preset/lang": 2,
            "assets/wover-ui/lang": 2,
            **{"assets/wover/" + n + ".png": 1 for n in (
                "betterx", "header", "icon", "icon2", "icon_bclib", "icon_betterend",
                "icon_betternether", "icon_updater")},
            **{"assets/wover-" + n + "/icon.png": 1 for n in ("core", "events", "surface")}}
        assert files - classes - assets - configs == {
            "LICENSE", "LICENSE-worldweaver", "META-INF/MANIFEST.MF",
            "META-INF/accesstransformer.cfg", "META-INF/neoforge.mods.toml", service,
            "data/wover/worldgen/noise_settings/amplified_nether.json"}
        entries = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert len(entries) == 7
        services = {n.replace(".", "/") + ".class"
                    for n in archive.read(service).decode().splitlines()}
        assert len(services) == 6
        hooks: set[str] = set()
        client_count = 0
        for name in configs:
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            assert not config.get("plugin")
            assert not config.get("server")
            package = cast("str", config["package"])
            hooks.update((package + "." + n).replace(".", "/") + ".class"
                         for n in cast("list[str]", config.get("mixins", [])))
            client_count += len(cast("list[str]", config.get("client", [])))
        assert len(hooks) == 45
        assert client_count == 10
        captured: set[str] = set()
        for label, digest in (
            ("wover-provider-entry",
             "7537c04a2b8eb8e4ddbbd4e01d44c44f30412abede90a2da78660ee7576eaeea"),
            ("wover-module-startup",
             "f2a9d6f8299314df097c55d483033b066a430dc8ef108bcf87afa20acb7c50dc"),
            ("wover-listener-targets",
             "73e67c1b9e5d6563d6884c6c01b80cdf06faf10728a31e6cd138c8d42733e2b3"),
            ("wover-registration-targets",
             "49c08adb298ff6d87ee15167b56c956274b7b043b1d79f62455cbf697f0602aa"),
            ("wover-common-hooks",
             "4cd9101a82b4be679faa5f0e691a0f6fd095bb6f8c4d9542ab2de3b23f173fb2"),
            ("wover-bootstrap-boundaries",
             "901508185dd2583e0a22de2eb10e017b8a241ba262781803c158d43a0fa5e1be"),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                captured.add(row["class"])
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                assert row["disassembly_sha256"] == hashlib.sha256(
                    (directory / row["disassembly"]).read_bytes()).hexdigest()
        assert entries | services | hooks <= captured
        assert len(captured) == 91
