from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_bookshelf_membership_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "bookshelf-neoforge-1.21.1-21.1.81.jar")
    assert source.sha256 == "19e88d40da2b6a114c2b808f7fb469d96e66a5379df0a8a43fcb7834498b3e76"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    prefix = "net/darkhax/bookshelf/"
    entry = prefix + "neoforge/impl/NeoForgeMod.class"
    services = {"META-INF/services/net.darkhax.bookshelf.common.api." + n for n in (
        "network.INetworkHandler", "registry.ContentProvider", "util.IGameplayHelper",
        "util.IRenderHelper", "util.IPlatformHelper")}
    tags = {"data/bookshelf/tags/item/creative_tab/minecraft/" + n + ".json" for n in (
        "functional_blocks", "ingredients", "colored_blocks", "food_and_drinks",
        "building_blocks", "combat", "redstone_blocks", "spawn_eggs", "natural_blocks",
        "op_blocks", "tools_and_utilities")}
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 173
        assert files - classes == services | tags | {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "pack.mcmeta",
            "bookshelf.neoforge.mixins.json", "bookshelf.mixins.json",
            "logo_bookshelf.png", "license_bookshelf.txt",
            "data/bookshelf/damage_type/fake_player.json",
            "data/bookshelf/tags/damage_type/fake_player.json",
            *(f"assets/bookshelf/lang/{lang}.json" for lang in (
                "ja_jp", "en_us", "es_ar", "zh_cn", "pt_br"))}
        for name in tags:
            assert json.loads(archive.read(name)) == {"values": []}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert {c["config"] for c in cast("list[dict[str, str]]", metadata["mixins"])} == {
            "bookshelf.mixins.json", "bookshelf.neoforge.mixins.json"}
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == {entry}
        expected = {entry, prefix + "common/impl/BookshelfMod.class",
                    prefix + "common/api/registry/ContentProvider.class"}
        for name in services:
            expected.add(archive.read(name).decode().strip().replace(".", "/") + ".class")
        for name, count, client_count in (
            ("bookshelf.mixins.json", 27, 7), ("bookshelf.neoforge.mixins.json", 0, 1),
        ):
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            hooks = cast("list[str]", config["mixins"])
            assert (len(hooks), len(cast("list[str]", config["client"]))) == (count, client_count)
            assert not any(config.get(k) for k in ("server", "plugin"))
            package = cast("str", config["package"])
            expected.update((package + "." + n).replace(".", "/") + ".class" for n in hooks)
        captured: set[str] = set()
        for label, digest in (
            ("bookshelf-provider",
             "efb66653932f676f95a91b5cc61a660ce9278fef0d0375e6431983136e0354c2"),
            ("bookshelf-startup",
             "5dd211d3d7a55d6f8fbb16ce18b92b1827db2f63b1bbe18aa3911a7f8b4baf82"),
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
