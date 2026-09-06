from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue

UNUSED_POOLS = {
    "integrated_villages:airship_village/farmhouse",
    "integrated_villages:airship_village/fletcher",
    "integrated_villages:airship_village/leatherworker",
    "integrated_villages:airship_village/villager_random",
    "integrated_villages:cabin_village/house/armorer_bottom",
    "integrated_villages:cabin_village/house/butcher",
    "integrated_villages:cabin_village/mobs/villager",
    "integrated_villages:cabin_village/mobs/villager_guard",
    "integrated_villages:cabin_village/mobs/villager_random",
    "integrated_villages:cabin_village/path/intersection4_bottom",
    "integrated_villages:kutcha_village/house/fletcher_bottom",
    "integrated_villages:kutcha_village/house/library",
    "integrated_villages:kutcha_village/path/bell",
    "integrated_villages:marketstead_village/deco/farm1_bottom",
    "integrated_villages:marketstead_village/deco/farm2_bottom",
    "integrated_villages:marketstead_village/deco/farm3_bottom",
    "integrated_villages:marketstead_village/deco/pen1_bottom",
    "integrated_villages:marketstead_village/deco/pen2_bottom",
    "integrated_villages:marketstead_village/deco/pen3_bottom",
    "integrated_villages:marketstead_village/house/stables_bottom",
    "integrated_villages:marketstead_village/mobs/villager_guard",
    "integrated_villages:marketstead_village/path/intersection3_bottom",
    "integrated_villages:mediterranean_village/mobs/irons_priest",
    "integrated_villages:mediterranean_village/mobs/pig",
    "integrated_villages:mediterranean_village/mobs/sheep",
    "integrated_villages:mediterranean_village/path/bell",
    "integrated_villages:mediterranean_village/path/light_left",
    "integrated_villages:mediterranean_village/path/light_right",
    "integrated_villages:minka_village/mobs/irons_priest",
    "integrated_villages:minka_village/mobs/villager_guard",
    "integrated_villages:mossy_mounds/house/armorer",
    "integrated_villages:mossy_mounds/house/cleric",
    "integrated_villages:mossy_mounds/house/house",
    "integrated_villages:oasis_village/house/basichouse4_bottom",
    "integrated_villages:oasis_village/house/library",
    "integrated_villages:oasis_village/mobs/villager_guard",
    "integrated_villages:pirate_village/house/farmhouse",
    "integrated_villages:pirate_village/market/market_stall_sawmill_bottom",
    "integrated_villages:pirate_village/ship/ship",
    "integrated_villages:pirate_village/villager_random",
    "integrated_villages:swamp_village/mobs/irons_priest",
    "integrated_villages:swamp_village/mobs/swamp_village_pig",
    "integrated_villages:swamp_village/mobs/swamp_village_sheep",
    "integrated_villages:tavern_village/hay",
    "integrated_villages:tavern_village/irons_priest",
    "integrated_villages:tavern_village/light_left",
    "integrated_villages:tavern_village/market/market_stall_ballooon_bottom",
    "integrated_villages:tavern_village/market/market_stall_sawmill_bottom",
    "integrated_villages:tavern_village/path_end",
    "integrated_villages:tavern_village/villager_random",
    "integrated_villages:tavern_village/well/waystone_bottom",
}

UNUSED_TEMPLATES = {
    "integrated_villages:airship_village/mobs/airship_village_villager_baby",
    "integrated_villages:airship_village/mobs/airship_village_villager_nitwit",
    "integrated_villages:cabin_village/house/cabin_village_armorer_bottom",
    "integrated_villages:cabin_village/house/cabin_village_fisherman_lecturn1",
    "integrated_villages:cabin_village/house/cabin_village_fisherman_lecturn2",
    "integrated_villages:cabin_village/house/cabin_village_fisherman_lecturn3",
    "integrated_villages:cabin_village/house/cabin_village_fisherman_lecturn4",
    "integrated_villages:cabin_village/house/cabin_village_fisherman_lecturn5",
    "integrated_villages:cabin_village/house/cabin_village_fisherman_lecturn6",
    "integrated_villages:cabin_village/house/cabin_village_fisherman_lecturn7",
    "integrated_villages:cabin_village/house/cabin_village_toolsmith_bottom",
    "integrated_villages:cabin_village/mobs/cabin_village_villager_guard",
    "integrated_villages:cabin_village/path/cabin_village_intersection4",
    "integrated_villages:cabin_village/path/cabin_village_intersection4_bottom",
    "integrated_villages:clockwork_village/mobs/clockwork_village_villager_priest",
    "integrated_villages:kutcha_village/house/kutcha_village_fletcher",
    "integrated_villages:kutcha_village/house/kutcha_village_fletcher_bottom",
    "integrated_villages:kutcha_village/mobs/kutcha_village_nitwit",
    "integrated_villages:kutcha_village/path/kutcha_village_path_cactus",
    "integrated_villages:kutcha_village/path/kutcha_village_path_carrots",
    "integrated_villages:kutcha_village/path/kutcha_village_path_wheat",
    "integrated_villages:marketstead_village/deco/marketstead_village_farm1_bottom",
    "integrated_villages:marketstead_village/deco/marketstead_village_farm2_bottom",
    "integrated_villages:marketstead_village/deco/marketstead_village_farm3_bottom",
    "integrated_villages:marketstead_village/deco/marketstead_village_pen1_bottom",
    "integrated_villages:marketstead_village/deco/marketstead_village_pen2_bottom",
    "integrated_villages:marketstead_village/deco/marketstead_village_pen3_bottom",
    "integrated_villages:marketstead_village/house/marketstead_village_stables_bottom",
    "integrated_villages:marketstead_village/mobs/marketstead_village_nitwit",
    "integrated_villages:marketstead_village/mobs/marketstead_village_villager_guard",
    "integrated_villages:marketstead_village/path/marketstead_village_intersection3_bottom",
    "integrated_villages:mediterranean_village/house/mediterranean_village_bakery_lets_do",
    "integrated_villages:mediterranean_village/mobs/mediterranean_village_irons_priest",
    "integrated_villages:mediterranean_village/mobs/mediterranean_village_pig",
    "integrated_villages:mediterranean_village/mobs/mediterranean_village_sheep",
    "integrated_villages:mediterranean_village/path/mediterranean_village_bell",
    "integrated_villages:mediterranean_village/path/mediterranean_village_light_left",
    "integrated_villages:mediterranean_village/path/mediterranean_village_light_right",
    "integrated_villages:minka_village/mobs/minka_village_irons_priest",
    "integrated_villages:minka_village/mobs/minka_village_villager_guard",
    "integrated_villages:mossy_mounds/path/mossy_mounds_path_large7",
    "integrated_villages:oasis_village/house/oasis_village_basichouse4_bottom",
    "integrated_villages:oasis_village/mobs/oasis_village_nitwit",
    "integrated_villages:oasis_village/mobs/oasis_village_villager_guard",
    "integrated_villages:oasis_village/path/oasis_village_path_house_large3",
    "integrated_villages:pirate_village/market/pirate_village_market_stall_sawmill",
    "integrated_villages:pirate_village/market/pirate_village_market_stall_sawmill_bottom",
    "integrated_villages:pirate_village/mobs/pirate_village_villager_baby",
    "integrated_villages:pirate_village/mobs/pirate_village_villager_nitwit",
    "integrated_villages:swamp_village/deco/swamp_village_lantern_oak",
    "integrated_villages:swamp_village/deco/swamp_village_lantern_spruce",
    "integrated_villages:swamp_village/deco/swamp_village_shop_farmersdelight",
    "integrated_villages:swamp_village/mobs/swamp_village_irons_priest",
    "integrated_villages:swamp_village/mobs/swamp_village_nitwit",
    "integrated_villages:swamp_village/mobs/swamp_village_pig",
    "integrated_villages:swamp_village/mobs/swamp_village_sheep",
    "integrated_villages:swamp_village/path/path_tc",
    "integrated_villages:swamp_village/swamp_village_post_stone",
    "integrated_villages:tavern_village/house/tavern_village_tavern",
    "integrated_villages:tavern_village/market/tavern_village_market_stall_balloon",
    "integrated_villages:tavern_village/market/tavern_village_market_stall_balloon_bottom",
    "integrated_villages:tavern_village/market/tavern_village_market_stall_sawmill",
    "integrated_villages:tavern_village/market/tavern_village_market_stall_sawmill_bottom",
    "integrated_villages:tavern_village/mobs/tavern_village_irons_priest",
    "integrated_villages:tavern_village/mobs/tavern_village_villager_baby",
    "integrated_villages:tavern_village/mobs/tavern_village_villager_nitwit",
    "integrated_villages:tavern_village/path/tavern_village_hay",
    "integrated_villages:tavern_village/path/tavern_village_light_left",
    "integrated_villages:tavern_village/path/tavern_village_path_end1",
    "integrated_villages:tavern_village/path/tavern_village_path_end2",
    "integrated_villages:tavern_village/path/tavern_village_path_market4",
    "integrated_villages:tavern_village/tavern/tavern_village_tavern_bottom",
    "integrated_villages:tavern_village/well/tavern_village_waystone",
    "integrated_villages:tavern_village/well/tavern_village_waystone_bottom",
}

ROOTS = {
    "integrated_villages:airship_village",
    "integrated_villages:cabin_village",
    "integrated_villages:clockwork_village",
    "integrated_villages:kutcha_village",
    "integrated_villages:marketstead_village",
    "integrated_villages:mediterranean_village",
    "integrated_villages:mossy_mounds",
    "integrated_villages:oasis_village",
    "integrated_villages:pirate_village",
    "integrated_villages:quark/minka_village",
    "integrated_villages:sunken_village",
    "integrated_villages:tavern_village",
}

MISSING = {
    "integrated_villages:cabin_village": [
        {"id": "integrated_villages:cabin_village/house/fisherman_lecturn", "kind": "pool"},
        {"id": "integrated_villages:cabin_village/villager_random", "kind": "pool"},
        {
            "id": "integrated_villages:cabin_village/house/cabin_village_farmhouse1",
            "kind": "template",
        },
    ],
    "integrated_villages:kutcha_village": [
        {
            "id": "integrated_villages:kutcha_village/mobs/kutcha_village_villager_nitwit",
            "kind": "template",
        }
    ],
    "integrated_villages:marketstead_village": [
        {"id": "integrated_villages:cabin_village/deco/farm1_bottom", "kind": "pool"},
        {"id": "integrated_villages:cabin_village/deco/farm2_bottom", "kind": "pool"},
        {"id": "integrated_villages:cabin_village/deco/farm3_bottom", "kind": "pool"},
        {"id": "integrated_villages:cabin_village/deco/pen1_bottom", "kind": "pool"},
        {"id": "integrated_villages:cabin_village/deco/pen2_bottom", "kind": "pool"},
        {"id": "integrated_villages:cabin_village/deco/pen3_bottom", "kind": "pool"},
        {"id": "integrated_villages:cabin_village/house/stables_bottom", "kind": "pool"},
        {
            "id": (
                "integrated_villages:marketstead_village/mobs/"
                "marketstead_village_villager_nitwit"
            ),
            "kind": "template",
        },
    ],
    "integrated_villages:oasis_village": [
        {
            "id": "integrated_villages:oasis_village/mobs/oasis_village_villager_nitwit",
            "kind": "template",
        }
    ],
    "integrated_villages:pirate_village": [
        {"id": "integrated_villages:pirate_village/path", "kind": "pool"}
    ],
    "integrated_villages:quark/minka_village": [
        {
            "id": "integrated_villages:oasis_village/mobs/oasis_village_villager_nitwit",
            "kind": "template",
        }
    ],
    "integrated_villages:sunken_village": [
        {"id": "integrated_villages:swamp_village/swamp_village_irons_priest", "kind": "pool"},
        {
            "id": "integrated_villages:swamp_village/mobs/swamp_village_villager_nitwit",
            "kind": "template",
        },
    ],
}


def test_integrated_villages_payload_and_component_partition() -> None:
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("integrated_villages-")
    )
    assert source.sha256 == "b53a485828da352b1a6a24cd2796aacf5d8360632b98c7dfba295f235d41ec00"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    classes: set[str] = set()
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 1475
        for folder, digest in (
            (
                "integrated-village-suppression",
                "1e13f934a2a29c03d56bfdb610aaea5c53b28367e4a554a0ecf3abaf58942320",
            ),
            (
                "integrated-villages-provider",
                "b7edce7fe258c480a4b60ad5869b379a9501ea9f7d02e5ed287519f4122334c9",
            ),
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
                    == (row["disassembly_sha256"])
                )
        assert len(classes) == 14
        assert classes == {n for n in names if n.endswith(".class")}
        for name in names:
            if name in classes | {
                "META-INF/MANIFEST.MF",
                "META-INF/neoforge.mods.toml",
                "pack.mcmeta",
                "integrated_villages-common.mixins.json",
                "integrated_villages-common-refmap.json",
                "assets/integrated_villages/integrated_villages_logo.png",
            }:
                continue
            assert name.startswith(
                (
                    "data/integrated_villages/",
                    "data/create/tags/",
                    "data/minecraft/tags/",
                    "data/integrated_api/tags/",
                    "data/integrated_api/integrated_workstations/",
                )
            ), name
            assert name.endswith((".nbt", ".json")), name
            assert name.split("/")[2] in {
                "structure",
                "worldgen",
                "loot_table",
                "tags",
                "advancement",
                "integrated_workstations",
                "integrated_structure_spawners",
                "integrated_villages_pool_additions",
            }, name
            if name.split("/")[2] == "worldgen":
                assert name.split("/")[3] in {
                    "structure",
                    "structure_set",
                    "template_pool",
                    "processor_list",
                }, name
            for kind, identifiers in groups.items():
                found = resource_identity(name, kind, ".nbt" if kind == "structure" else ".json")
                if found:
                    identifiers.add(found[0])
        roots = {
            name: cast(
                "dict[str, JsonValue]",
                json.loads(
                    archive.read(
                        "data/integrated_villages/worldgen/structure/"
                        + name.split(":", 1)[1]
                        + ".json"
                    )
                ),
            )
            for name in ROOTS
        }
        assert {k: v["type"] for k, v in roots.items()} == {
            k: "integrated_api:"
            + (
                "optional_dependency_structure"
                if k.endswith("quark/minka_village")
                else "biome_facing_structure"
                if k.endswith("pirate_village")
                else "generic_structure"
            )
            for k in ROOTS
        }
        workstations = [n for n in names if "/integrated_workstations/" in n]
        assert len(workstations) == 12
        for name in workstations:
            data = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(archive.read(name)))
            assert set(data) == {"workstations"}
            assert all(
                set(row) == {"required_mod", "output_block", "weight"}
                for row in data["workstations"]
            )
        assert json.loads(
            archive.read("data/integrated_villages/integrated_structure_spawners/generic.json")
        ) == {
            "mobs": [
                {"name": "minecraft:zombie", "weight": 15},
                {"name": "minecraft:skeleton", "weight": 10},
            ]
        }
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    structures = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    traces = {k: structures[k] for k in ROOTS}
    assert groups["worldgen/structure"] == ROOTS
    assert len(groups["worldgen/template_pool"]) == 421
    assert len(groups["structure"]) == 754
    assert (
        groups["worldgen/template_pool"]
        - {x for t in traces.values() for x in cast("list[str]", t["pools"])}
        == UNUSED_POOLS
    )
    assert (
        groups["structure"]
        - {x for t in traces.values() for x in cast("list[str]", t["templates"])}
        == UNUSED_TEMPLATES
    )
    assert {k: t["missing"] for k, t in traces.items() if t["missing"]} == MISSING
    assert all(t["unresolved_elements"] == [] for t in traces.values())


def test_integrated_villages_legacy_addition_fields_and_consumers() -> None:
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("integrated_villages-")
    )
    with ZipFile(source.path) as archive:
        additions = [
            n
            for n in archive.namelist()
            if "/integrated_villages_pool_additions/" in n and n.endswith(".json")
        ]
        targets: dict[str, str] = {}
        for name in additions:
            data = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
            assert set(data) == {"name", "fallback", "elements"}
            entries = cast("list[dict[str, JsonValue]]", data["elements"])
            assert len(entries) == 1
            assert set(entries[0]) == {"element", "weight", "required_mod"}
            element = cast("dict[str, JsonValue]", entries[0]["element"])
            location = cast("str", element["location"])
            assert location in UNUSED_TEMPLATES
            targets[cast("str", data["name"])] = location
        assert targets == {
            "integrated_villages:mediterranean_village/bakery": (
                "integrated_villages:mediterranean_village/house/"
                "mediterranean_village_bakery_lets_do"
            ),
            "integrated_villages:pirate_village/market": (
                "integrated_villages:pirate_village/market/"
                "pirate_village_market_stall_sawmill"
            ),
            "integrated_villages:tavern_village/market": (
                "integrated_villages:tavern_village/market/"
                "tavern_village_market_stall_sawmill"
            ),
            "integrated_villages:tavern_village/well": (
                "integrated_villages:tavern_village/well/"
                "tavern_village_waystone"
            ),
        }
    directory = Path("evidence/item-8/sources/integrated-villages-provider") / source.name
    prefix = "com.craisinlord.integrated_villages.pooladditions.PoolAdditionMergerManager"
    manager = (directory / (prefix + ".txt")).read_text().split("\n{", 1)[1]
    codec = (directory / (prefix + "$AdditionalStructureTemplatePool.txt")).read_text()
    entry = (
        directory / (prefix + "$AdditionalStructureTemplatePool$ExpandedPoolEntry.txt")
    ).read_text()
    assert "// String target_pool" in manager
    assert "// String target_pool" in codec
    assert "// String condition" in codec
    assert "required_mod" not in manager + codec + entry
    assert "Field cachedMap" in manager
    assert "ifnull" in manager
