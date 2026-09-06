from __future__ import annotations

import gzip
import hashlib
import json
import re
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_desert_temple_provider_payload_and_components() -> None:  # noqa: C901, PLR0912, PLR0915
    # Keep the single frozen payload and its graph partition in one assertion path.
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("YungsBetterDesertTemples-")
    )
    assert source.sha256 == "2c3191ad447092cc7873a06e92f16bd3e2ff9dc31e93268b8893d06dd89e1fd6"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    classes: set[str] = set()
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 323
        for folder, digest in (
            ("desert-temple-suppression",
             "20a9cee456cc7df91632272752f855c9c972bc860d0155c267ea9067f6bb26f6"),
            ("desert-temple-provider",
             "b64f030b80004ea67adeecadf91809f2f82e40526fa2fbe91905d9a2f53e66f2"),
        ):
            directory = Path("evidence/item-8/sources") / folder
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            identities = cast("list[dict[str, str]]", json.loads(raw))
            for row in identities:
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class"] not in classes
                classes.add(row["class"])
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert (
                    hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                    == row["disassembly_sha256"]
                )
        assert len(classes) == 30
        all_classes = {n for n in names if n.endswith(".class")}
        assert len(all_classes) == 62
        prefix = "com/yungnickyoung/minecraft/betterdeserttemples/"
        for name in all_classes - classes:
            assert name.startswith((prefix + "config/", prefix + "module/ConfigModule",
                                    prefix + "world/processor/", prefix + "entity/IPharaohData",
                                    prefix + "world/ArmorStandChances",
                                    prefix + "world/ItemFrameChances")), name
            for marker in (b"EventBusSubscriber;", b"Lnet/neoforged/fml/common/Mod;",
                           b"Lorg/spongepowered/asm/mixin/Mixin;", b"YungAutoRegister;"):
                assert marker not in archive.read(name), (name, marker)
        processor_module = prefix + "module/StructureProcessorModule.class"
        processor_text = ""
        for name in ("module.StructureProcessorModule", "services.NeoForgeProcessorProvider"):
            processor_text += (
                Path("evidence/item-8/sources/desert-temple-provider") / source.name / (
                    "com.yungnickyoung.minecraft.betterdeserttemples." + name + ".txt"
                )
            ).read_text()
        processor_classes = {n + ".class" for n in cast("list[str]", re.findall(
            r"// Field ([^ :]+)\.CODEC:", processor_text
        ))}
        assert len(processor_classes) == 26
        assert {n for n in all_classes if "/world/processor/" in n} == processor_classes
        mixins = cast("dict[str, list[str]]", json.loads(
            archive.read("betterdeserttemples.mixins.json")
        ))
        assert {prefix + "mixin/" + n.replace(".", "/") + ".class"
                for n in mixins["mixins"]} <= classes
        services = "com.yungnickyoung.minecraft.betterdeserttemples.services."
        for interface, implementation in (
            ("IModulesLoader", "NeoForgeModulesLoader"),
            ("IPlatformHelper", "NeoForgePlatformHelper"),
            ("IProcessorProvider", "NeoForgeProcessorProvider"),
        ):
            assert archive.read("META-INF/services/" + services + interface).decode().strip() == (
                services + implementation
            )
        for name in names:
            if name in all_classes | {
                "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "pack.mcmeta",
                "betterdeserttemples.mixins.json", "LICENSE_YungsBetterDesertTemples",
                "catalogue_background.png", "catalogue_icon.png", "icon.png", "logo.png",
                "META-INF/services/" + services + "IModulesLoader",
                "META-INF/services/" + services + "IPlatformHelper",
                "META-INF/services/" + services + "IProcessorProvider",
            }:
                continue
            if name.startswith("assets/betterdeserttemples/lang/"):
                assert name.endswith(".json"), name
                continue
            assert name.startswith((
                "data/betterdeserttemples/",
                "data/yungsapi/tags/", "data/morevillagers/tags/",
            )), name
            assert name.endswith((".json", ".nbt")), name
            assert name.split("/")[2] in {
                "worldgen", "structure", "tags", "loot_table", "advancement",
            }, name
            if name.split("/")[2] == "worldgen":
                assert name.split("/")[3] in {
                    "structure", "structure_set", "template_pool", "processor_list",
                }, name
            for kind, ids in groups.items():
                found = resource_identity(name, kind, ".nbt" if kind == "structure" else ".json")
                if found:
                    ids.add(found[0])
        processor_types: set[str] = set()
        for name in names:
            if "/worldgen/processor_list/" not in name:
                continue
            data = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(archive.read(name)))
            processor_types.update(cast("str", p["processor_type"]) for p in data["processors"])
        assert len(processor_types) == 27
        assert "minecraft:rule" in processor_types
        for identifier in processor_types - {"minecraft:rule"}:
            assert identifier.startswith("betterdeserttemples:")
            assert identifier.split(":")[1].encode() in archive.read(processor_module)
        for tag in ("applies_mining_fatigue", "better_desert_temples"):
            value = cast("dict[str, JsonValue]", json.loads(archive.read(
                f"data/betterdeserttemples/tags/worldgen/structure/{tag}.json"
            )))
            assert value == {"replace": False, "values": ["betterdeserttemples:desert_temple"]}
    assert groups["worldgen/structure"] == {"betterdeserttemples:desert_temple"}
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert groups["worldgen/structure"] == {
        r for r in registry if r.startswith("betterdeserttemples:")
    }
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    trace = traces["betterdeserttemples:desert_temple"]
    assert trace["missing"] == []
    assert trace["unresolved_elements"] == []
    assert len(groups["worldgen/template_pool"]) == 28
    assert groups["worldgen/template_pool"] | {"minecraft:empty"} == set(
        cast("list[str]", trace["pools"])
    )
    assert len(groups["structure"]) == 198
    assert groups["structure"] - set(cast("list[str]", trace["templates"])) == {
        "betterdeserttemples:hall_room/crushing_corridor",
    }
