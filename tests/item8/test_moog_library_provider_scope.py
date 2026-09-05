from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_moog_library_entry_routes_and_full_resource_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("moogs_structures-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    prefix = "com/finndog/moogs_structures/"
    captured: set[str] = set()
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        for name in (
            "pool-codecs", "moog-generator-code", "moog-nether-generator-code",
            "moog-provider-entries", "moog-provider-callbacks", "moog-declared-mixins",
            "moog-direct-boundaries", "moog-registration-boundaries",
        ):
            directory = Path("evidence/item-8/sources") / name
            identities = cast(
                "list[dict[str, str]]", json.loads((directory / "identities.json").read_bytes())
            )
            for identity in identities:
                if identity["archive"] != source.name:
                    continue
                assert identity["archive_sha256"] == source.sha256
                captured.add(identity["class"])
                assert (
                    hashlib.sha256(archive.read(identity["class"])).hexdigest()
                    == identity["class_sha256"]
                )
                assert (
                    hashlib.sha256((directory / identity["disassembly"]).read_bytes()).hexdigest()
                    == identity["disassembly_sha256"]
                )
        files = {n for n in names if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        # Source interpretation follows these loader/subscriber entries, not a
        # zero-hit worldgen keyword search or an assertion about every helper.
        entries = {
            n for n in classes if any(marker in archive.read(n) for marker in (
                b"EventBusSubscriber", b"SubscribeEvent", b"fml/common/Mod;",
            ))
        }
        assert entries == {
            prefix + "neoforge/MoogsStructuresNeoforge.class",
            prefix + "datagen/StructureNbtUpdaterDatagen.class",
        }
        assert entries <= captured
        service = "META-INF/services/com.finndog.moogs_structures.platform.IRegistryPlatform"
        implementation = (
            "com.finndog.moogs_structures.modinit.registry.neoforge.ResourcefulRegistriesImpl"
        )
        assert archive.read(service).decode().strip() == implementation
        assert implementation.replace(".", "/") + ".class" in captured
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        configs = {
            entry["config"] for entry in cast("list[dict[str, str]]", metadata["mixins"])
        }
        assert configs == {
            "moogs_structures-common.mixins.json", "moogs_structures-neoforge.mixins.json",
        }
        mixins: set[str] = set()
        for config in configs:
            data = cast("dict[str, object]", json.loads(archive.read(config)))
            assert "plugin" not in data
            for side in ("mixins", "client", "server"):
                mixins.update(
                    (cast("str", data["package"]) + "." + n).replace(".", "/") + ".class"
                    for n in cast("list[str]", data.get(side, []))
                )
        assert len(mixins) == 16
        assert mixins <= captured
        assert files - classes == configs | {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", service,
            "META-INF/accesstransformer.cfg", "moogs_structures.accesswidener",
            "pack.mcmeta", "assets/moogs_structures/icon.png", "LICENSE_Moog's Structure Lib",
        }
        # These only expose classes. No generation entry or resource is added.
        assert archive.read("META-INF/accesstransformer.cfg").decode().splitlines() == [
            "public net.minecraft.world.entity.npc.VillagerTrades$TreasureMapForEmeralds",
            "public net.minecraft.server.packs.resources.FallbackResourceManager$PackEntry",
        ]
        pack_entry = "net/minecraft/server/packs/resources/FallbackResourceManager$PackEntry"
        assert archive.read("moogs_structures.accesswidener").decode().splitlines() == [
            "accessWidener v1 named",
            "accessible class net/minecraft/world/entity/npc/VillagerTrades$TreasureMapForEmeralds",
            f"accessible class {pack_entry}",
        ]
