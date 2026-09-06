from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_jungle_temple_provider_payload_and_components() -> None:  # noqa: C901, PLR0915
    # Keep the single frozen payload and its graph partition in one assertion path.
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("YungsBetterJungleTemples-")
    )
    assert source.sha256 == "a0d57b78c7a1891796f342b1f09c214bc27bedf0a3a894f029dfdb2db9f813d0"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    classes: set[str] = set()
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 203
        for folder, digest in (
            ("jungle-temple-suppression",
             "40fa52b38f8b195be2e65b9f3846312b32024f5825c064ac703b8ba31a6d8611"),
            ("jungle-temple-provider",
             "c58f507bc5d0896b3f5fd6238d7ab9b3a79ce4ff4408417e896c041d6ce0c027"),
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
        assert len(classes) == 32
        assert classes == {n for n in names if n.endswith(".class")}
        services = "com.yungnickyoung.minecraft.betterjungletemples.services."
        for interface, implementation in (
            ("IModulesLoader", "NeoForgeModulesLoader"),
            ("IPlatformHelper", "NeoForgePlatformHelper"),
            ("IProcessorProvider", "NeoForgeProcessorProvider"),
        ):
            assert archive.read("META-INF/services/" + services + interface).decode().strip() == (
                services + implementation
            )
        for name in names:
            if name in classes | {
                "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "pack.mcmeta",
                "betterjungletemples.mixins.json", "LICENSE_YungsBetterJungleTemples",
                "catalogue_background.png", "catalogue_icon.png", "icon.png", "logo.png",
                "META-INF/services/" + services + "IModulesLoader",
                "META-INF/services/" + services + "IPlatformHelper",
                "META-INF/services/" + services + "IProcessorProvider",
            }:
                continue
            if name.startswith("assets/betterjungletemples/lang/"):
                assert name.endswith(".json"), name
                continue
            assert name.startswith((
                "data/betterjungletemples/",
                "data/yungsapi/tags/", "data/morevillagers/tags/",
            )), name
            assert name.endswith((".json", ".nbt")), name
            assert name.split("/")[2] in {
                "worldgen", "structure", "tags", "loot_table",
            }, name
            if name.split("/")[2] == "worldgen":
                assert name.split("/")[3] in {
                    "structure", "structure_set", "template_pool", "processor_list",
                }, name
            for kind, ids in groups.items():
                found = resource_identity(name, kind, ".nbt" if kind == "structure" else ".json")
                if found:
                    ids.add(found[0])
        for processor_list in ("main", "main_waterlog"):
            processor_data = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(archive.read(
                f"data/betterjungletemples/worldgen/processor_list/{processor_list}.json"
            )))
            expected = {
                "empty_dispenser_processor", "fireball_dispenser_processor",
                "cave_vine_decoration_processor", "torch_processor", "item_frame_processor",
                "block_replace_processor", "pillar_processor",
            }
            if processor_list == "main":
                expected.add("blast_furnace_processor")
            assert {cast("str", p["processor_type"]) for p in processor_data["processors"]} == {
                "betterjungletemples:" + n for n in expected
            }
    assert groups["worldgen/structure"] == {"betterjungletemples:jungle_temple"}
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert groups["worldgen/structure"] == {
        r for r in registry if r.startswith("betterjungletemples:")
    }
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    trace = traces["betterjungletemples:jungle_temple"]
    assert len(groups["worldgen/template_pool"]) == 17
    assert groups["worldgen/template_pool"] | {"minecraft:empty"} == set(
        cast("list[str]", trace["pools"])
    )
    assert len(groups["structure"]) == 127
    assert groups["structure"] - set(cast("list[str]", trace["templates"])) == {
        "betterjungletemples:props/prop_table_0",
        "betterjungletemples:props/prop_table_1",
    }
    assert trace["missing"] == []
    assert trace["unresolved_elements"] == []
