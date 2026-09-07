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


def test_fortress_provider_payload_and_components() -> None:  # noqa: PLR0915
    # Keep the single frozen payload and its graph partition in one assertion path.
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("YungsBetterNetherFortresses-")
    )
    assert source.sha256 == "5450a64a7036237f449496837e08f3e5b3aa1d7974a10df43944172def75d8ff"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    classes: set[str] = set()
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 244
        for folder, digest in (
            ("fortress-suppression",
             "100e268d617b82cd28a20aa2adbdff2eef29976b3a60bf8627337e2f1ada9bb4"),
            ("fortress-provider",
             "3dfe3d5fc9c799adcff26bc710001126477a9f8d712b227bed501f3612835598"),
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
        assert len(classes) == 26
        assert classes == {n for n in names if n.endswith(".class")}
        services = "com.yungnickyoung.minecraft.betterfortresses.services."
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
                "betterfortresses.mixins.json", "LICENSE_YungsBetterNetherFortresses",
                "catalogue_background.png", "catalogue_icon.png", "icon.png", "logo.png",
                "META-INF/services/" + services + "IModulesLoader",
                "META-INF/services/" + services + "IPlatformHelper",
                "META-INF/services/" + services + "IProcessorProvider",
            }:
                continue
            if name.startswith("assets/betterfortresses/lang/"):
                assert name.endswith(".json"), name
                continue
            assert name.startswith((
                "data/betterfortresses/", "data/minecraft/advancement/",
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
        processor_data = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(archive.read(
            "data/betterfortresses/worldgen/processor_list/main.json"
        )))
        assert {cast("str", p["processor_type"]) for p in processor_data["processors"]} == {
            "betterfortresses:" + n for n in (
                "stair_pillar_processor", "item_frame_processor", "bridge_arch_processor",
                "nether_wart_processor", "red_sandstone_stairs_processor", "pillar_processor",
                "liquid_block_processor",
            )
        } | {"minecraft:rule"}
    assert groups["worldgen/structure"] == {"betterfortresses:fortress"}
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert groups["worldgen/structure"] == {
        r for r in registry if r.startswith("betterfortresses:")
    }
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    trace = traces["betterfortresses:fortress"]
    assert len(groups["worldgen/template_pool"]) == 15
    assert groups["worldgen/template_pool"] | {"minecraft:empty"} == set(
        cast("list[str]", trace["pools"])
    )
    assert len(groups["structure"]) == 169
    assert groups["structure"] - set(cast("list[str]", trace["templates"])) == {
        "betterfortresses:battle_bridge/battle_bridge_straight_bothsides",
        "betterfortresses:battle_bridge/battle_bridge_straight_oneside",
        "betterfortresses:bridge/blaze_stairs_broken_0",
        "betterfortresses:bridge/blaze_stairs_broken_1",
        "betterfortresses:bridge/blaze_stairs_broken_2",
        "betterfortresses:bridge/blaze_stairs_broken_3",
        "betterfortresses:bridge/blaze_stairs_broken_4",
        "betterfortresses:bridge/bridge_junction_2_covered",
        "betterfortresses:bridge/bridge_junction_3_covered",
        "betterfortresses:bridge/bridge_junction_4_covered",
        "betterfortresses:bridge/bridge_pillar_beacon_lit",
        "betterfortresses:bridge/bridge_pillar_beacon_unlit",
        "betterfortresses:bridge/bridge_pillar_covered",
        "betterfortresses:bridge/bridge_pillar_shelter",
        "betterfortresses:halls/hall_4_",
        "betterfortresses:halls/prop/hall_prop_desk",
        "betterfortresses:keep/tower/tower_stairs_back_left",
        "betterfortresses:keep/tower/tower_stairs_back_right",
        "betterfortresses:keep/tower/tower_stairs_front_left",
        "betterfortresses:keep/tower/tower_stairs_front_right",
    }
    assert trace["missing"] == [{"id": "betterfortresses:halls/hall_4", "kind": "template"}]
    assert trace["unresolved_elements"] == []
