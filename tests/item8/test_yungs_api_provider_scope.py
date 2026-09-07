from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_yungs_api_provider_payload_and_entries() -> None:
    # Bound the shared provider; do not re-audit consuming structure generators.
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("YungsApi-"))
    assert source.sha256 == "08e1d21690d3213a4c62de6b6cf79f3527afb2e72e0cad0e1848d46eb8f682ca"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    prefix = "com/yungnickyoung/minecraft/yungsapi/"
    captured: set[str] = set()
    with ZipFile(source.path) as archive:
        names = {n for n in archive.namelist() if not n.endswith("/")}
        assert len(names) == 197
        classes = {n for n in names if n.endswith(".class")}
        assert len(classes) == 179
        for directory, digest, count in (
            ("yungs-api-provider",
             "29215d7f2b0ca237ee8ec41dd0a7e5248dd20591d8c85cd96bf64a29574eedcf", 43),
            ("pool-codecs", "4f1484523b4f3dea5154273eaaffea2459eb8a158af4d39dafcc0ca966a1bb98", 2),
        ):
            base = Path("evidence/item-8/sources") / directory
            raw = (base / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            rows = [r for r in cast("list[dict[str, str]]", json.loads(raw))
                    if r["archive"] == source.name]
            assert len(rows) == count
            for row in rows:
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert hashlib.sha256((base / row["disassembly"]).read_bytes()).hexdigest() == (
                    row["disassembly_sha256"]
                )
                assert row["class"] not in captured
                captured.add(row["class"])
        tags = {"data/yungsapi/tags/worldgen/structure/" + n + ".json" for n in (
            "remove_basalt_columns_feature_in", "remove_delta_feature_in",
            "remove_magma_feature_in", "remove_vines_feature_in",
        )}
        service = "com.yungnickyoung.minecraft.yungsapi.services."
        services = {"META-INF/services/" + service + "I" + n for n in (
            "AutoRegisterHelper", "BlockEntityTypeHelper", "ParticleTypeHelper", "PlatformHelper",
        )}
        assert names - classes == tags | services | {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "pack.mcmeta",
            "catalogue_background.png", "catalogue_icon.png", "icon.png", "logo.png",
            "yungsapi.mixins.json", "yungsapi_neoforge.mixins.json", "LICENSE_YungsApi",
        }
        for name in tags:
            assert json.loads(archive.read(name)) == {"replace": False, "values": []}
        for name in services:
            interface = name.split(service)[1]
            expected = service + "NeoForge" + interface[1:]
            assert archive.read(name).decode().strip() == expected
            assert expected.replace(".", "/") + ".class" in captured
        for name, count in (("yungsapi.mixins.json", 15), ("yungsapi_neoforge.mixins.json", 1)):
            doc = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
            mixins = cast("list[str]", doc["mixins"])
            assert len(mixins) == count
            assert not doc.get("client")
            assert {prefix + "mixin/" + m.replace(".", "/") + ".class"
                    for m in mixins} <= captured
            if name == "yungsapi.mixins.json":
                assert doc["plugin"] == "com.yungnickyoung.minecraft.yungsapi.YungsApiMixinPlugin"
            else:
                assert "plugin" not in doc
        assert prefix + "mixin/MinecraftServerMixin.class" not in classes
        assert {n for n in classes if b"Lnet/neoforged/fml/common/Mod;" in archive.read(n)} == {
            prefix + "YungsApiNeoForge.class",
        }
        assert not {n for n in classes if b"EventBusSubscriber;" in archive.read(n)}
        assert all(n.startswith(prefix) for n in classes)
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert not {r for r in registry if r.startswith("yungsapi:")}
