from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_yungs_extras_full_archive_has_only_known_feature_paths() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("YungsExtras-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    classes: set[str] = set()
    directories = (
        "yungs-extras-desert-code",
        "yungs-extras-registration",
        "yungs-extras-generators",
        "yungs-extras-processor-bindings",
        "yungs-extras-initialization",
        "yungs-extras-module-default",
        "yungs-extras-scope-entries",
    )
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        for name in directories:
            directory = Path("evidence/item-8/sources") / name
            identities = cast(
                "list[dict[str, str]]", json.loads((directory / "identities.json").read_bytes())
            )
            for identity in identities:
                assert identity["archive"] == source.name
                classes.add(identity["class"])
                assert (
                    hashlib.sha256(archive.read(identity["class"])).hexdigest()
                    == identity["class_sha256"]
                )
                assert (
                    hashlib.sha256((directory / identity["disassembly"]).read_bytes()).hexdigest()
                    == identity["disassembly_sha256"]
                )
        assert {n for n in names if n.endswith(".class")} == classes
        assert len(classes) == 29
        service = "com.yungnickyoung.minecraft.yungsextras.services."
        metadata = {
            "META-INF/MANIFEST.MF",
            "META-INF/neoforge.mods.toml",
            "pack.mcmeta",
            "LICENSE_YungsExtras",
            "catalogue_background.png",
            "icon.png",
            "logo.png",
        }
        for interface, impl in (
            ("IModulesLoader", "NeoForgeModulesLoader"),
            ("IPlatformHelper", "NeoForgePlatformHelper"),
        ):
            path = f"META-INF/services/{service}{interface}"
            metadata.add(path)
            assert archive.read(path).decode().strip() == service + impl
        remaining = {n for n in names if not n.endswith("/")} - classes - metadata
        groups = {
            prefix: {n for n in remaining if n.startswith(f"data/yungsextras/{prefix}/")}
            for prefix in (
                "structure",
                "worldgen/configured_feature",
                "worldgen/placed_feature",
                "tags",
                "loot_table",
                "forge/biome_modifier",
                "neoforge/biome_modifier",
            )
        }
        assert remaining == set().union(*groups.values())
        assert tuple(len(v) for v in groups.values()) == (62, 62, 62, 3, 3, 3, 3)
        assert all(n.endswith(".nbt") for n in groups["structure"])
        assert all(n.endswith(".json") for n in remaining - groups["structure"])
