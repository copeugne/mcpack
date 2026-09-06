from __future__ import annotations

import hashlib
import json
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_create_dragons_plus_membership() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "CreateDragonsPlus-1.11.2b.jar")
    assert source.sha256 == "9b15e464465a639de9ef5a935ae9fd94ea545904517d1428bc784a4012e0a1e2"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 352
        data = {n for n in files if n.startswith("data/")}
        assets = {n for n in files if n.startswith("assets/")}
        assert Counter("/".join(n.split("/")[:3]) for n in data) == {
            "data/c/tags": 107, "data/create/tags": 2,
            "data/create_dragons_plus/advancement": 4, "data/create_dragons_plus/data_maps": 7,
            "data/create_dragons_plus/floating_materials": 1,
            "data/create_dragons_plus/loot_table": 4,
            "data/create_dragons_plus/physics_block_properties": 1,
            "data/create_dragons_plus/recipe": 119, "data/create_dragons_plus/tags": 57,
            "data/minecraft/tags": 1, "data/sable/tags": 2}
        assert Counter("/".join(n.split("/")[:3]) for n in assets) == {
            "assets/create_dragons_plus/blockstates": 56, "assets/create_dragons_plus/lang": 11,
            "assets/create_dragons_plus/models": 118, "assets/create_dragons_plus/ponder": 9,
            "assets/create_dragons_plus/textures": 19, "assets/minecraft/atlases": 1}
        configs = {n for n in files if "/" not in n and n.endswith(".mixins.json")}
        assert len(configs) == 5
        assert files - classes - data - assets - configs == {
            "META-INF/MANIFEST.MF", "icon.png", "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml", "META-INF/jarjar/metadata.json", "LICENSING.txt",
            "LICENSE.txt", "LICENSE-CREATE.txt",
            "META-INF/jarjar/conditional-mixin-neoforge-0.6.4.jar"}
        entries = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert len(entries) == 14
        hooks: set[str] = set()
        client_count = 0
        for name in configs:
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            assert config["plugin"] == "plus.dragons.createdragonsplus.mixin.CDPMixinConfigPlugin"
            assert not config.get("server")
            package = cast("str", config["package"])
            hooks.update((package + "." + n).replace(".", "/") + ".class"
                         for n in cast("list[str]", config["mixins"]))
            client_count += len(cast("list[str]", config.get("client", [])))
        assert len(hooks) == 34
        assert client_count == 1
        captured: set[str] = set()
        for label, digest in (
            ("create-dragons-plus-provider",
             "0dad0fdd4901ca6972a9e629a27c13e0331ef6a4c2efc932d46d630e44ed18a1"),
            ("create-dragons-plus-startup",
             "abf6643ffff8cb152e132dee8bc25332c43fc684352d193e38559fe3e7356c7b"),
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
        assert entries | hooks <= captured
        assert "plus/dragons/createdragonsplus/mixin/CDPMixinConfigPlugin.class" in captured
        assert len(captured) == 52


def test_create_dragons_plus_nested_membership() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "CreateDragonsPlus-1.11.2b.jar")
    name = "META-INF/jarjar/conditional-mixin-neoforge-0.6.4.jar"
    with ZipFile(source.path) as parent:
        payload = parent.read(name)
    digest = "0ae7b346d87879e81f276e6a590a6af1e723193e6eb3e94c1f71f7ab5b54d59f"
    assert hashlib.sha256(payload).hexdigest() == digest
    with ZipFile(BytesIO(payload)) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 19
        assert files - classes == {
            "META-INF/MANIFEST.MF", "LICENSE_conditional-mixin", "META-INF/neoforge.mods.toml",
            "assets/conditionalmixin/icon.png", "pack.mcmeta"}
        directory = Path("evidence/item-8/sources/create-dragons-plus-conditional")
        raw = (directory / "identities.json").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == (
            "c45e2412785aa38544e33ef491a9983cd5d4db094d26e8fcd32bf85d9b4eb14c")
        rows = cast("list[dict[str, str]]", json.loads(raw))
        assert len(rows) == 3
        captured = {r["class"] for r in rows}
        automatic = {n for n in classes if b"Lnet/neoforged/fml/common/Mod;" in archive.read(n)}
        assert len(automatic) == 1
        assert automatic <= captured
        for row in rows:
            assert row["archive"] == source.name + "!/" + name
            assert row["archive_sha256"] == digest
            assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
            assert row["disassembly_sha256"] == hashlib.sha256(
                (directory / row["disassembly"]).read_bytes()).hexdigest()
