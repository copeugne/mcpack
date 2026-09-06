from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_accessories_provider_membership() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "accessories-neoforge-1.1.0-beta.53+1.21.1.jar")
    assert source.sha256 == "10017a3da78ea63e9ece27a1ca32f8cf490362f348778cf8cb759e7282f3beb0"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 416
        data = {n for n in files if n.startswith("data/")}
        assets = {n for n in files if n.startswith("assets/")}
        assert Counter("/".join(n.split("/")[:4]) for n in data) == {
            "data/accessories/accessories/entity": 1, "data/accessories/accessories/group": 7,
            "data/accessories/accessories/slot": 12, "data/accessories/tags/enchantment": 1,
            "data/accessories/tags/entity_type": 4, "data/accessories/tags/item": 2}
        assert Counter("/".join(n.split("/")[:3]) for n in assets) == {
            "assets/accessories/lang": 5, "assets/accessories/nine_patch_textures": 30,
            "assets/accessories/shaders": 6, "assets/accessories/textures": 90,
            "assets/minecraft/atlases": 2}
        assert files - classes - data - assets == {
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg", "META-INF/neoforge.mods.toml",
            "accessories-common-common-refmap.json", "accessories-common.mixins.json",
            "accessories-forge.mixins.json", "accessories.accesswidener", "icon.png", "pack.mcmeta",
            "schemas/custom_renderer_schema.json", "schemas/rendering_function_schema.json",
            "schemas/transformation_schema.json"}
        entries = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert len(entries) == 2
        expected = set(entries)
        for name, common_count, client_count in (
            ("accessories-common.mixins.json", 31, 31),
            ("accessories-forge.mixins.json", 1, 5),
        ):
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            assert not config.get("server")
            hooks = cast("list[str]", config["mixins"])
            assert len(hooks) == common_count
            assert len(cast("list[str]", config["client"])) == client_count
            package = cast("str", config["package"])
            expected.update((package + "." + n).replace(".", "/") + ".class" for n in hooks)
            expected.add(cast("str", config["plugin"]).replace(".", "/") + ".class")
        captured: set[str] = set()
        for label, digest in (
            ("accessories-provider",
             "93c8d040e59e2df4b2b46de805f7bb529018b99c9e275a765c6b4f5a9295a646"),
            ("accessories-startup",
             "599e8339dcb834199a136be2b53e9063cf2a62cb5560db04e9680e9e3dacbaef"),
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
        assert captured == expected | {
            "io/wispforest/accessories/Accessories.class",
            "io/wispforest/accessories/impl/AccessoriesEventHandler.class"}
