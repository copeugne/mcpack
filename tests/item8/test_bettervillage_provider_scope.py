from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_bettervillage_complete_payload_uses_existing_contribution_paths() -> None:
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "bettervillage-neoforge-1.21.1-3.3.1.jar"
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/bettervillage-code")
    identities = cast(
        "list[dict[str, str]]", json.loads((directory / "identities.json").read_bytes())
    )
    classes = {i["class"] for i in identities}
    assert len(classes) == 7
    metadata = {
        "META-INF/MANIFEST.MF",
        "META-INF/accesstransformer.cfg",
        "META-INF/neoforge.mods.toml",
        "bettervillage.mixins.json",
        "pack.mcmeta",
        "changelog.md",
        "license_bettervillage.txt",
        "icon.png",
        "pack.png",
    }
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        assert {n for n in names if n.endswith(".class")} == classes
        for identity in identities:
            assert (
                hashlib.sha256(archive.read(identity["class"])).hexdigest()
                == identity["class_sha256"]
            )
            assert (
                hashlib.sha256((directory / identity["disassembly"]).read_bytes()).hexdigest()
                == identity["disassembly_sha256"]
            )
        remaining = {n for n in names if not n.endswith("/")} - classes - metadata
        templates = {
            n
            for n in remaining
            if n.startswith("data/minecraft/structure/village/") and n.endswith(".nbt")
        }
        compat = {
            n
            for n in remaining
            if n.startswith("data/bettervillage/bettervillage_compat/") and n.endswith(".json")
        }
        assert remaining == templates | compat
        assert (len(templates), len(compat)) == (246, 4)
        mixins = cast("dict[str, object]", json.loads(archive.read("bettervillage.mixins.json")))
        assert mixins["package"] == "com.jtorleonstudios.bettervillage.mixin"
        assert mixins["mixins"] == ["AbstractDecorationEntityMixin", "StructureSetMixin"]
        assert mixins["client"] == []
        assert "plugin" not in mixins
        target = "public-f net.minecraft.world.level.levelgen.structure.pools.StructureTemplatePool"
        assert archive.read("META-INF/accesstransformer.cfg").decode().splitlines() == [
            f"{target} rawTemplates",
            f"{target} templates",
        ]
