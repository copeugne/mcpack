from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import cast
from zipfile import ZipFile

import pytest

from mcpack_evidence.item8_sources import retained_sources


@pytest.mark.parametrize(("archive_identity", "entry", "extras", "configs", "captures"), [
    (("prickle-neoforge-1.21.1-21.1.11.jar", 47,
     "ccf46c442ed3c7fe41ad056f0940560829ec4dd88360985dfacd78f4614eb167"),
     "net/darkhax/pricklemc/neoforge/impl/NeoForgeMod.class",
     {"license_prickle.txt", "logo_prickle.png", "pack.mcmeta",
      "META-INF/services/net.darkhax.pricklemc.common.api.config.property.IDefaultPropertyAdapters",
      "META-INF/services/net.darkhax.pricklemc.common.api.util.IPlatformHelper"},
     {"prickle.mixins.json": (0, 0), "prickle.neoforge.mixins.json": (0, 0)},
     {"prickle-provider": "d74e45ef3f358e66f265369bb421d84e372521a0c2ba2e5b9e99080ce7a108e5",
      "prickle-init": "44697e75f75482b14fbef985cc910ebecf26fd0e15fbdbbcc2b829bb54a5f3d6"}),
    (("resourcefulconfig-neoforge-1.21-3.0.11.jar", 186,
     "25b4f3502d25c535004acd4a9420272fff01d2f1e2df352239fec93fdab005d4"),
     "com/teamresourceful/resourcefulconfig/neoforge/ResourcefulConfigNeoForge.class",
     {"resourcefulconfig-common-refmap.json",
      "META-INF/services/com.teamresourceful.resourcefulconfig.api.loader.ConfigParser"},
     {"resourcefulconfig.mixins.json": (3, 1)},
     {"resourcefulconfig-provider":
      "f1d2c276dedab09562346f4dec4afdb7039c9b056602aa31e263c1ce0c47a021"}),
])
def test_config_library_membership_payload(
    archive_identity: tuple[str, int, str], entry: str, extras: set[str],
    configs: dict[str, tuple[int, int]], captures: dict[str, str],
) -> None:
    name, count, digest = archive_identity
    source = next(s for s in retained_sources(Path.cwd()) if s.name == name)
    assert source.sha256 == digest
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == digest
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assets = {n for n in files if n.startswith("assets/")}
        assert len(classes) == count
        assert len(assets) == (35 if name.startswith("resourcefulconfig-") else 0)
        assert all(n.startswith("assets/resourcefulconfig/") and
                   n.endswith((".png", ".png.mcmeta", ".json")) for n in assets)
        assert files - classes - assets == extras | set(configs) | {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml"}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        declarations = cast("list[dict[str, str]]", metadata["mixins"])
        assert {r["config"] for r in declarations} == set(configs)
        expected = {entry}
        for filename, (common, client) in configs.items():
            config = cast("dict[str, object]", json.loads(archive.read(filename)))
            assert not config.get("plugin")
            assert not config.get("server")
            members = cast("list[str]", config.get("mixins", []))
            assert len(members) == common
            assert len(cast("list[str]", config.get("client", []))) == client
            prefix = cast("str", config["package"]).replace(".", "/")
            expected.update(prefix + "/" + n.replace(".", "/") + ".class" for n in members)
        for filename in extras:
            if filename.startswith("META-INF/services/"):
                expected.add(archive.read(filename).decode().strip().replace(".", "/") + ".class")
        if name.startswith("prickle-"):
            expected.add("net/darkhax/pricklemc/common/impl/PrickleMod.class")
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == {entry}
        captured: set[str] = set()
        for label, identity in captures.items():
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == identity
            rows = cast("list[dict[str, str]]", json.loads(raw))
            for row in rows:
                captured.add(row["class"])
                assert row["archive"] == source.name
                assert row["archive_sha256"] == digest
                assert row["class_sha256"] == hashlib.sha256(
                    archive.read(row["class"])).hexdigest()
                assert row["disassembly_sha256"] == hashlib.sha256(
                    (directory / row["disassembly"]).read_bytes()).hexdigest()
        assert captured == expected
