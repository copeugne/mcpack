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


def test_stronghold_provider_payload_and_components() -> None:  # noqa: C901, PLR0915
    # Keep the single frozen payload and its graph partition in one assertion path.
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("YungsBetterStrongholds-")
    )
    assert source.sha256 == "a9cab2fc01538368862365691f7d215309801aed0b390351681b6b60a1db7b58"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    classes: set[str] = set()
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 181
        for folder, digest in (
            ("stronghold-suppression",
             "56e90dc542fe8ef9a152ccaa201cfa79e2e4f629f4b9b68623a4bf9c96f7224b"),
            ("stronghold-provider",
             "3a72121dbd2da8c4b5cc66a419c0f03e0fefc7f329542cb9750e94cbae707a72"),
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
        services = "com.yungnickyoung.minecraft.betterstrongholds.services."
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
                "betterstrongholds.mixins.json", "LICENSE_YungsBetterStrongholds",
                "catalogue_background.png", "catalogue_icon.png", "icon.png", "logo.png",
                "META-INF/services/" + services + "IModulesLoader",
                "META-INF/services/" + services + "IPlatformHelper",
                "META-INF/services/" + services + "IProcessorProvider",
            }:
                continue
            if name.startswith("assets/betterstrongholds/lang/"):
                assert name.endswith(".json"), name
                continue
            assert name.startswith((
                "data/betterstrongholds/", "data/minecraft/advancement/",
                "data/minecraft/tags/",
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
        processor_files = [n for n in names if "/worldgen/processor_list/" in n]
        assert len(processor_files) == 9
        processor_ids: set[str] = set()
        for name in processor_files:
            data = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(archive.read(name)))
            processor_ids.update(cast("str", p["processor_type"]) for p in data["processors"])
        assert processor_ids == {"betterstrongholds:" + n for n in (
            "ruin_processor", "banner_processor", "ore_processor", "armorstand_processor",
            "itemframe_processor", "rare_block_processor", "redstone_processor", "leg_processor",
            "end_portal_frame_processor",
        )} | {"minecraft:rule"}
        assert json.loads(archive.read(
            "data/betterstrongholds/worldgen/structure_set/stronghold.json"
        )) == {
            "structures": [{"structure": "betterstrongholds:stronghold", "weight": 1}],
            "placement": {"salt": 596441294, "spacing": 85, "separation": 50,
                          "chunk_distance_to_first_ring": 80, "ring_chunk_thickness": 96,
                          "type": "betterstrongholds:stronghold"},
        }
    assert groups["worldgen/structure"] == {"betterstrongholds:stronghold"}
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert groups["worldgen/structure"] == {
        r for r in registry if r.startswith("betterstrongholds:")
    }
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    trace = traces["betterstrongholds:stronghold"]
    assert len(groups["worldgen/template_pool"]) == 12
    assert set(cast("list[str]", trace["pools"])) - groups["worldgen/template_pool"] == {
        "minecraft:empty",
    }
    assert groups["worldgen/template_pool"] <= set(cast("list[str]", trace["pools"]))
    assert len(groups["structure"]) == 97
    assert groups["structure"] - set(cast("list[str]", trace["templates"])) == {
        "betterstrongholds:hall_doorways/hall_doorway_2torch_soul",
        "betterstrongholds:rooms/hallway_trap_0",
        "betterstrongholds:terminators/hallway_end_new",
        "betterstrongholds:terminators/hallway_end_statue_0",
        "betterstrongholds:terminators/hallway_end_statue_0_new",
        "betterstrongholds:terminators/hallway_end_statue_1",
        "betterstrongholds:terminators/hallway_end_statue_1_new",
        "betterstrongholds:terminators/hallway_end_statue_2",
        "betterstrongholds:terminators/hallway_end_statue_2_new",
        "betterstrongholds:terminators/hallway_end_statue_3",
        "betterstrongholds:terminators/hallway_end_statue_3_new",
        "betterstrongholds:terminators/hallway_end_statue_4",
        "betterstrongholds:terminators/hallway_end_statue_4_new",
    }
    assert trace["missing"] == [{"id": "betterstrongholds:spiral_stairs", "kind": "pool"}]
    assert trace["unresolved_elements"] == []
