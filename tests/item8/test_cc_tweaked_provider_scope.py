from __future__ import annotations

import hashlib
import json
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_cc_tweaked_provider_membership() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "cc-tweaked-1.21.1-forge-1.119.0.jar")
    assert source.sha256 == "169e2fe0445e320562c0568baa4c796a69a3464a0a5e902c484be1be3e326a0b"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 1190
        assert not any(n.endswith(".nbt") for n in files)
        assert Counter("/".join(n.split("/")[:3]) for n in files if n.startswith("data/")) == {
            "data/computercraft/lua": 220, "data/computercraft/recipe": 75,
            "data/computercraft/advancement": 70, "data/computercraft/tags": 18,
            "data/computercraft/loot_table": 17, "data/computercraft/computercraft": 8,
            "data/minecraft/computercraft": 6, "data/minecraft/tags": 5, "data/create/tags": 1}
        assert {n for n in files if n.endswith(".jar")} == {
            "META-INF/jarjar/cobalt-0.9.9.jar", "META-INF/jarjar/jzlib-1.1.3.jar"}
        for member, count in (("cobalt-0.9.9.jar", 187), ("jzlib-1.1.3.jar", 26)):
            with ZipFile(BytesIO(archive.read("META-INF/jarjar/" + member))) as library:
                entries = {n for n in library.namelist() if not n.endswith("/")}
                code = {n for n in entries if n.endswith(".class")}
                assert len(code) == count
                assert not any(b"net/minecraft/" in library.read(n) for n in code)
                assert all(n.startswith("META-INF/") for n in entries - code)
                assert not any(n.startswith("META-INF/services/") for n in entries)
        services = {n for n in files if n.startswith("META-INF/services/")}
        assert len(services) == 6
        providers = {archive.read(n).decode().strip().replace(".", "/") + ".class"
                     for n in services}
        clients = {
            "dan200/computercraft/client/integration/IrisShaderMod.class",
            "dan200/computercraft/client/platform/ClientPlatformHelperImpl.class",
            "dan200/computercraft/client/platform/ClientNetworkContextImpl.class"}
        assert clients <= providers
        expected = providers - clients
        expected.update(n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;")))
        for name, count in (("computercraft.forge.mixins.json", 1),
                            ("computercraft.mixins.json", 3),
                            ("computercraft-client.forge.mixins.json", 0)):
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            assert not config.get("plugin")
            assert not config.get("server")
            hooks = cast("list[str]", config.get("mixins", []))
            assert len(hooks) == count
            package = cast("str", config["package"])
            expected.update((package + "." + n).replace(".", "/") + ".class" for n in hooks)
        captured: set[str] = set()
        for label, digest in (
            ("cc-tweaked-provider",
             "eb5f29f53bff4cb1e977a4c2f35c4c1e0b4c70a582f2c77acd4a072b1b4327ab"),
            ("cc-tweaked-startup",
             "86915681e8cb6ccb41a0cecf9c444fc9c15a8f1a20c23df146a0429acfb2fb26"),
            ("cc-tweaked-registry-lifecycle",
             "3ea31124fc41a1706c6e2c8c656446b18c4047ffff2677d25b1133ed9313b815"),
            ("cc-tweaked-client-entries",
             "c0ed967d981853b4d4d2254cfec2babaab165dd5fc263ab385ab2c8612eb0ad4"),
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
                assert row["disassembly_sha256"] == hashlib.sha256(target.read_bytes()).hexdigest()
                expected_files.add(target)
                if label == "cc-tweaked-client-entries":
                    assert (
                        "value=[Lnet/neoforged/api/distmarker/Dist;.CLIENT]" in target.read_text()
                    )
            assert {p for p in directory.rglob("*") if p.is_file()} == expected_files
        assert expected <= captured
        assert len(captured) == 31
