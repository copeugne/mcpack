from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources


def test_end_island_provider_entries_and_payload() -> None:
    # Bind reused entry evidence and the bounded remainder in one archive check.
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("YungsBetterEndIsland-")
    )
    assert source.sha256 == "8005f1ea798d09fc05dad07a21ed1f393a523a718197cdbd37b1ce6d9a17e4a4"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    captured: set[str] = set()
    manifests = (
        ("better-end-island-platform-gateway",
         "6d6944ae221e62182308d1ac3cdcc10a9b028d98bb0e2fa0d72e910cd366b48a"),
        ("better-end-island-processors",
         "dfeb5a2586c4b82b3e0e6eb5712149d1ab8adfc6689cc7ece108490a2b7d9b95"),
        ("better-end-island-configuration",
         "56c0b14dfb0f0a11156acd745548cb01085bce05ed965bbc38bdbeae19fed3cb"),
        ("better-end-island-generator-dependencies",
         "8c3ce129b5cdde84f33f705a24735cff5c219462b9b0a5db494b927c21d3ca3e"),
        ("better-end-island-exit-portal",
         "c33781ceaf0c25c60be92da62653f8fe73afbdc83b6248066bedd7ad2b61dcbd"),
        ("better-end-island-activation",
         "65c8b9e69ad267dced5a68b6035808345da4d67193d919e1760028ccf8ec399a"),
        ("better-end-island-spike-podium",
         "edd47178444d8218268335284bbe3ae1b394d4249c22b02ad85208caa2d63c52"),
        ("end-island-provider",
         "0db009720863b6d44792a50e2f39f0adc418cc90a11e486c9d28343235cb9be2"),
    )
    with ZipFile(source.path) as archive:
        names = {n for n in archive.namelist() if not n.endswith("/")}
        assert len(names) == 101
        for folder, digest in manifests:
            base = Path("evidence/item-8/sources") / folder
            raw = (base / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert hashlib.sha256((base / row["disassembly"]).read_bytes()).hexdigest() == (
                    row["disassembly_sha256"]
                )
                captured.add(row["class"])
        prefix = "com/yungnickyoung/minecraft/betterendisland/"
        classes = {n for n in names if n.endswith(".class")}
        assert len(classes) == 45
        assert classes - captured == {prefix + n + ".class" for n in (
            "services/IPlatformHelper", "world/DragonRespawnStage$1",
            "world/DragonRespawnStage$2", "world/DragonRespawnStage$4", "world/ExtraFightData",
            "world/IBetterDragonFight", "world/IEndSpike", "world/IPrimaryLevelData",
            "world/util/EndCrystalUtils", "world/util/EndSpikeUtils",
        )}
        # These remaining internal types are reached by captured fight code; none
        # declares a loader, event subscriber, mixin or YUNG module entry.
        for name in classes - captured:
            raw = archive.read(name)
            for annotation in (
                b"Lnet/neoforged/fml/common/Mod;", b"EventBusSubscriber;",
                b"Lorg/spongepowered/asm/mixin/Mixin;", b"YungAutoRegister;",
            ):
                assert annotation not in raw, (name, annotation)
        mixins = cast(
            "dict[str, list[str]]", json.loads(archive.read("betterendisland.mixins.json"))
        )
        assert {prefix + "mixin/" + n.replace(".", "/") + ".class"
                for n in mixins["mixins"]} <= captured
        services = "com.yungnickyoung.minecraft.betterendisland.services."
        for interface, implementation in (
            ("IModulesLoader", "NeoForgeModulesLoader"),
            ("IPlatformHelper", "NeoForgePlatformHelper"),
        ):
            assert archive.read("META-INF/services/" + services + interface).decode().strip() == (
                services + implementation
            )
        other = names - classes
        templates = {n for n in other if n.startswith("data/betterendisland/structure/")}
        assert len(templates) == 41
        assert all(n.endswith(".nbt") for n in templates)
        for name in other - templates:
            if name.startswith(("assets/betterendisland/lang/", "data/betterendisland/tags/",
                                "data/minecraft/tags/")):
                assert name.endswith(".json"), name
            else:
                assert name in {
                    "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "pack.mcmeta",
                    "betterendisland.mixins.json", "catalogue_background.png", "catalogue_icon.png",
                    "icon.png", "logo.png", "LICENSE_YungsBetterEndIsland",
                    "META-INF/services/" + services + "IModulesLoader",
                    "META-INF/services/" + services + "IPlatformHelper",
                }, name
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert not {r for r in registry if r.startswith("betterendisland:")}
