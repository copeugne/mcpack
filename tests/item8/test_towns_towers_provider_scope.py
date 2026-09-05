from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_resource_selection import runtime_mod_ids
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_towns_towers_full_archive_and_disconnected_resources() -> None:
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "t_and_t-neoforge-fabric-1.13.9+1.21.1.jar"
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/towns-towers-entry")
    identities = cast(
        "list[dict[str, str]]", json.loads((directory / "identities.json").read_bytes())
    )
    classes = {i["class"] for i in identities}
    assert len(classes) == 3
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    patch_prefix = "resources/t_and_t_waystones_patch/"
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        assert {n for n in names if n.endswith(".class")} == classes
        for identity in identities:
            assert (
                hashlib.sha256(archive.read(identity["class"])).hexdigest()
                == identity["class_sha256"]
            )
            raw = (directory / identity["disassembly"]).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == identity["disassembly_sha256"]
        patch = {
            patch_prefix
            + "data/kaisyn/structure/village/modded/waystones/waystone_"
            + variant
            + ".nbt"
            for variant in ("default", "desert", "mossy")
        }
        metadata = {
            "CHANGELOG.txt",
            "CREDITS.txt",
            "LICENSE",
            "fabric.mod.json",
            "pack.png",
            "META-INF/MANIFEST.MF",
            "META-INF/neoforge.mods.toml",
            patch_prefix + "pack.png",
            patch_prefix + "pack.mcmeta",
        }
        for name in names:
            if name.endswith("/") or name in classes | patch | metadata:
                continue
            assert name.startswith("data/")
            assert name.endswith((".json", ".nbt"))
            assert name.split("/")[1] in {"kaisyn", "towns_and_towers", "minecraft", "cristellib"}
            kind = name.split("/")[2]
            assert kind in {
                "worldgen",
                "structure",
                "tags",
                "loot_table",
                "structure_config",
                "data_pack",
            }
            if kind == "worldgen":
                assert name.split("/")[3] in {
                    "structure",
                    "structure_set",
                    "template_pool",
                    "processor_list",
                }
            for kind, identifiers in groups.items():
                found = resource_identity(name, kind, ".nbt" if kind == "structure" else ".json")
                if found:
                    identifiers.add(found[0])
        assert {n for n in names if n.startswith(patch_prefix) and n.endswith(".nbt")} == patch
        declaration = cast(
            "dict[str, JsonValue]",
            json.loads(archive.read("data/cristellib/data_pack/load_waystone_patch_pack.json")),
        )
        assert declaration["location"] == "t_and_t:resources/t_and_t_waystones_patch"
        assert declaration["condition"] == {"type": "mod_loaded", "modid": "waystones"}
    log = Path("evidence/raw/item8/registry-r1/debug.log").read_bytes()
    assert hashlib.sha256(log).hexdigest() == (
        "e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b"
    )
    assert "waystones" not in runtime_mod_ids(log.decode())
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    doc = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    structures = cast("dict[str, dict[str, JsonValue]]", doc["structures"])
    roots = groups["worldgen/structure"]
    assert roots <= structures.keys()
    reached_pools = {p for r in roots for p in cast("list[str]", structures[r]["pools"])}
    reached_templates = {t for r in roots for t in cast("list[str]", structures[r]["templates"])}
    assert groups["worldgen/template_pool"] - reached_pools == {
        "kaisyn:" + p
        for p in (
            "village/grove_villager_outpost/decor",
            "village/modded/waystones/waystone_desert",
            "village/modded/waystones/waystone_mossy",
        )
    }
    assert groups["structure"] - reached_templates == {
        "kaisyn:" + p
        for p in (
            "outpost/camps/savanna_plateau/side/tower_pieces/savanna_plateau_tower_piece_1",
            "village/badlands_pueblo/houses/badlands_medium_house_2_r",
            "village/beach_lighthouse/villagers/lighthouse_master",
            "village/exclusives/iberian/terminators/terminator_04",
            "village/exclusives/iberian/terminators/terminator_05",
            "village/exclusives/iberian/terminators/terminator_06",
            "village/exclusives/mediterranean/houses/corner/med_small_garden_1",
            "village/exclusives/mediterranean/houses/corner/med_small_stall_1",
            "village/exclusives/mediterranean/villagers/bishop",
            "village/exclusives/nilotic/houses/nilotic_large_house_1",
            "village/exclusives/nilotic/houses/nilotic_leatherworker_and_shepherd_1",
            "village/exclusives/nilotic/houses/nilotic_mason_1",
            "village/exclusives/piglin/houses/piglin_skul_tent_1",
            "village/exclusives/rustic/professions_misc/rustic_empty_piece_1",
            "village/grove_villager_outpost/grove_table_1",
            "village/modded/waystones/waystone_desert",
            "village/modded/waystones/waystone_mossy",
            "village/sparse_jungle_polynesian/villagers/village_chief",
            "village/swamp_boat/streets/corssroad_03",
            "village/swamp_boat/streets/corssroad_04",
            "village/swamp_boat/streets/corssroad_05",
            "village/swamp_boat/streets/straight_03",
            "village/wooded_badlands_tipi/houses/large_huts/wooded_badlands_large_hut_green_1",
        )
    }
    assert all(structures[r]["unresolved_elements"] == [] for r in roots)
    assert {r for r in roots if structures[r]["missing"]} == {
        "towns_and_towers:" + r
        for r in (
            "village_meadow",
            "village_swamp",
            "exclusives/village_nilotic",
            "village_sparse_jungle",
            "pillager_outpost_savanna_plateau",
            "exclusives/pillager_outpost_nilotic",
            "exclusives/village_mediterranean",
            "village_beach",
        )
    }
    assert tuple(len(groups[k]) for k in groups) == (60, 187, 837)
