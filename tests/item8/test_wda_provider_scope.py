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


def test_wda_full_payload_and_candidate_components() -> None:  # noqa: C901, PLR0915
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "DungeonsArise-1.21.1-2.1.68-release.jar"
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/wda-provider-scope")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "1878d9890c8dbb9dae7b3edb7e07b760b1e59f0cb560519ef9b257ec79135d5f"
    )
    identities = cast("list[dict[str, str]]", json.loads(raw))
    classes = {i["class"] for i in identities}
    assert len(classes) == 6
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    functions: set[str] = set()
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        assert {n for n in names if n.endswith(".class")} == classes
        for identity in identities:
            payload = archive.read(identity["class"])
            assert hashlib.sha256(payload).hexdigest() == identity["class_sha256"]
            assert b"EventBusSubscriber" not in payload
            assert (b"Lnet/neoforged/fml/common/Mod;" in payload) == (
                identity["class"] == "net/aurelj/dungeons_arise/DungeonsAriseMain.class"
            )
            assert (
                hashlib.sha256((directory / identity["disassembly"]).read_bytes()).hexdigest()
                == (identity["disassembly_sha256"])
            )
        for name in names:
            if name.endswith("/") or name in classes | {
                "META-INF/MANIFEST.MF",
                "META-INF/neoforge.mods.toml",
                "pack.mcmeta",
                "wda_logo.png",
            }:
                continue
            if name.startswith("assets/dungeons_arise/lang/"):
                assert name.endswith(".json")
                continue
            assert name.startswith(("data/dungeons_arise/", "data/minecraft/tags/")), name
            kind = name.split("/")[2]
            assert kind in {
                "advancement",
                "enchantment",
                "function",
                "loot_table",
                "predicate",
                "structure",
                "tags",
                "worldgen",
            }, name
            if kind == "function":
                assert name.endswith(".mcfunction")
                functions.add(Path(name).stem)
                for line in archive.read(name).decode().splitlines():
                    assert line.startswith(
                        (
                            "particle ",
                            "playsound ",
                            "execute as @p at @s anchored eyes run particle ",
                            "data merge entity @s {NoGravity:1b}",
                        )
                    ) or line == (
                        "execute as @e[limit=5,sort=nearest,distance=0..4,"
                        "predicate=!dungeons_arise:ignores_ensnaring] at @s "
                        "run summon evoker_fangs ~ ~ ~"
                    )
                continue
            assert name.endswith((".json", ".nbt"))
            if kind == "worldgen":
                category = name.split("/")[3]
                assert category in {"structure", "structure_set", "template_pool", "processor_list"}
                doc = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
                if category == "structure":
                    assert doc["type"] == "minecraft:jigsaw"
                if category == "processor_list":
                    processors = cast("list[dict[str, JsonValue]]", doc["processors"])
                    assert all(p["processor_type"] == "minecraft:rule" for p in processors)
            for category, identifiers in groups.items():
                found = resource_identity(
                    name, category, ".nbt" if category == "structure" else ".json"
                )
                if found:
                    identifiers.add(found[0])
    assert functions == {
        "discharge_ready",
        "discharge_thunder",
        "ensnaring_fangs",
        "purification_particles",
        "voltaic_arrows",
        "voltaic_arrows_impact_particles",
    }
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
        "dungeons_arise:" + p
        for p in (
            "fortified/illager_castle/illager_castle_corridor",
            "fortified/illager_castle/illager_castle_start",
            "fortified/illager_castle/illager_castle_tower",
            "fortified/illager_hall/illager_hall_bridges",
            "fortified/illager_hall/illager_hall_start",
            "fortified/illager_hall/illager_hall_tower_parts",
            "fortified/illager_hall/illager_hall_towers",
            "fungi/mushroom_village_old/mushroom_village_houses",
            "fungi/mushroom_village_old/mushroom_village_spawners",
            "fungi/mushroom_village_old/mushroom_village_streets",
            "jungle/jungle_tree_house/jungle_tree_house_start",
            "prairie/wishing_well/wishing_well_main_no_effects",
        )
    }
    disconnected = {
        "bandit_village/bandit_village_deco_13",
        "bandit_village/bandit_village_street_1",
        "foundry/foundry_corridor_pedestal_4",
        "foundry/foundry_corridor_terminator_0",
        "greenwood_pub/greenwood_pub_furniture_1",
        "greenwood_pub/greenwood_pub_hallway_1",
        "greenwood_towers/greenwood_towers_part_0",
        "greenwood_towers/greenwood_towers_part_1",
        "illager_castle/illager_castle_base_0",
        "illager_castle/illager_castle_corridor_part_0",
        "illager_castle/illager_castle_corridor_part_1",
        "illager_castle/illager_castle_corridor_part_1b",
        "illager_castle/illager_castle_corridor_part_2",
        "illager_castle/illager_castle_corridor_part_2b",
        "illager_castle/illager_castle_roof_0",
        "illager_castle/illager_castle_tower_part_0",
        "illager_hall/illager_hall_bridge_0",
        "illager_hall/illager_hall_tower_main_part_0",
        "illager_hall/illager_hall_tower_part_0",
        "illager_hall/illager_hall_tower_roof_part_0",
        "merchant_campsite/merchant_campsite_tent_4",
        "mining_complex/mining_complex_lush_7",
        "mining_complex/mining_complex_mine_terminator_5",
        "shiraz_palace/shiraz_palace_husk_elite_0",
        "thornborn_towers/thornborn_towers_hanging_bridge_3_medium_terminator",
        "wishing_well/wishing_well_0_no_effects",
    }
    disconnected.update(f"mushroom_village_old/mushroom_village_house_{i}" for i in range(18))
    disconnected.update(
        f"mushroom_village_old/mushroom_village_coloured_street_{i}" for i in range(4)
    )
    disconnected.update(
        "mushroom_village_old/mushroom_village_" + p
        for p in (
            "piglin_brute_0",
            "piglin_brute_1",
            "piglin_brute_2",
            "piglin_brute_3_mounted",
            "piglin_crossbow_0",
            "piglin_crossbow_1_mounted",
        )
    )
    assert groups["structure"] - reached_templates == {"dungeons_arise:" + p for p in disconnected}
    assert all(structures[r]["unresolved_elements"] == [] for r in roots)
    assert {r for r in roots if structures[r]["missing"]} == {
        "dungeons_arise:" + r
        for r in ("foundry", "thornborn_towers", "bandit_village", "mechanical_nest")
    }
    assert tuple(len(groups[k]) for k in groups) == (40, 166, 877)
