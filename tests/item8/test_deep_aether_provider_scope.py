from __future__ import annotations

import hashlib
import io
import json
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources

SOURCES = (
    ("deep-aether-totem-scope",
     "a4a20f4109769622d01ebc02d5324d2ff55b6cc10aefde39e15132e377a3865d"),
    ("deep-aether-provider",
     "71c441da5bd3213d84b0ce9f1f38f098979d158b3f16146397428b99e958d5c4"),
    ("deep-aether-aeroblender",
     "414711e4c35a498420ead8f3a7de80e7e7b8feb15909a19fb2dcebdba6ef5dc7"),
    ("deep-aether-biome-setup",
     "d0c5ae38827b28d5db0048c2f5da5603e116a8c070991d1ab198b610af2a126f"),
)


def test_deep_aether_provider_sources_and_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "deep_aether-1.21.1-1.1.5.1.jar")
    assert source.sha256 == "0f55ad970715bb933344e785b2c35a7354dfba25ffd426c0b68921d08bbe0ce5"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = {n for n in archive.namelist() if not n.endswith("/")}
        assert Counter(n.split("/")[0] for n in names) == {
            "assets": 1989, "data": 1483, "io": 375, "packs": 265, ".cache": 14,
            "META-INF": 7, "deep_aether.mixins.json": 1, "deep_aether.png": 1,
            "pack.mcmeta": 1,
        }
        assert Counter(n.split("/")[2] for n in names if n.startswith("data/")) == {
            "recipe": 377, "advancement": 377, "loot_table": 318, "tags": 233,
            "worldgen": 132, "structure": 15, "neoforge": 10, "loot_modifiers": 9,
            "jukebox_song": 7, "trim_material": 3, "enchantment": 1, "data_maps": 1,
        }
        packs = {n for n in names if n.startswith("packs/")}
        assert Counter(n.split("/data/", 1)[1].split("/")[1]
                       for n in packs if "/data/" in n) == {
            "recipe": 86, "advancement": 49, "recipes": 2,
        }
        assert all("/data/" in n or "/assets/" in n
                   or n.endswith(("/pack.mcmeta", "/pack.png")) for n in packs)
        assert not any(n.startswith("META-INF/services/")
                       or n.endswith((".mcfunction", ".js", ".lua", ".py")) for n in names)
        captured: set[str] = set()
        nested_captured: set[str] = set()
        for directory, digest in SOURCES:
            base = Path("evidence/item-8/sources") / directory
            raw = (base / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                if row["archive"] == source.name:
                    assert row["archive_sha256"] == source.sha256
                    payload = archive.read(row["class"])
                    captured.add(row["class"])
                else:
                    assert row["archive"] == (
                        source.name + "!/META-INF/jarjar/aeroblender-1.21.1-1.0.0-neoforge.jar"
                    )
                    nested = archive.read(row["archive"].split("!/", 1)[1])
                    assert hashlib.sha256(nested).hexdigest() == row["archive_sha256"]
                    with ZipFile(io.BytesIO(nested)) as library:
                        payload = library.read(row["class"])
                    nested_captured.add(row["class"])
                assert hashlib.sha256(payload).hexdigest() == row["class_sha256"]
                assert hashlib.sha256((base / row["disassembly"]).read_bytes()).hexdigest() == (
                    row["disassembly_sha256"]
                )
        classes = {n for n in names if n.endswith(".class")}
        assert len(classes) == 375
        entries = {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))}
        assert len(entries) == 14
        assert entries <= captured
        mixins = cast("dict[str, object]", json.loads(archive.read("deep_aether.mixins.json")))
        common = {"io/github/razordevs/deep_aether/mixin/" + n.replace(".", "/") + ".class"
                  for n in cast("list[str]", mixins["mixins"])}
        assert len(common) == 11
        assert common <= captured
        with ZipFile(io.BytesIO(archive.read(
            "META-INF/jarjar/aeroblender-1.21.1-1.0.0-neoforge.jar"
        ))) as library:
            nested_names = {n for n in library.namelist() if not n.endswith("/")}
            assert len(nested_captured) == 14
            assert nested_names == nested_captured | {
                "io/github/razordevs/aeroblender/AeroBlenderConfig.class",
                "io/github/razordevs/aeroblender/AeroBlenderConfig$Common.class",
                "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg",
                "META-INF/neoforge.mods.toml", "pack.mcmeta", "aeroblender.mixins.json",
                "data/aeroblender/worldgen/density_function/depth.json",
                "data/aeroblender/worldgen/noise/temperature.json",
                "data/aether/worldgen/noise_settings/skylands.json",
                "data/terrablender/tags/dimension_type/aether_regions.json",
            }
