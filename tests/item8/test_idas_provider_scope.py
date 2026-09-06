from __future__ import annotations

import gzip
import hashlib
import json
import tomllib
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue

UNUSED_POOLS = {
    "idas:archmages_tower/archmages_tower2",
    "idas:bophauntedhouse",
    "idas:castle/villager",
    "idas:desert_camp/desert_camp_black",
    "idas:desert_pyramid/all",
    "idas:desert_pyramid/villager",
    "idas:enchantingtower/ars_enchantingtower",
    "idas:haunted_manor/if_haunted_manor1",
    "idas:haunted_manor/if_haunted_manor2",
    "idas:haunted_manor/if_haunted_manor3",
    "idas:haunted_manor/if_haunted_manor4",
    "idas:hauntedhouse",
    "idas:labyrinth/bopfloor1",
    "idas:labyrinth/bopfloor2",
    "idas:labyrinth/boplabyrinth_entrance",
    "idas:labyrinth/boplabyrinth_entrance2",
    "idas:labyrinth/if_floor1",
    "idas:labyrinth/if_floor2",
    "idas:labyrinth/if_labyrinth_entrance",
    "idas:labyrinth/if_labyrinth_entrance2",
    "idas:labyrinth/if_tomb",
}

UNUSED_TEMPLATES = {
    "idas:animal_den/bear_den",
    "idas:archmages_tower/archmages_tower2",
    "idas:desert_camp/desert_camp_black",
    "idas:desert_pyramid/desert_pyramid_cave1",
    "idas:desert_pyramid/desert_pyramid_cave2",
    "idas:desert_pyramid/desert_pyramid_villager",
    "idas:enchantingtowers/ars_blueenchantingtower",
    "idas:enchantingtowers/ars_redenchantingtower",
    "idas:haunted_manor/if_haunted_manor1",
    "idas:haunted_manor/if_haunted_manor2",
    "idas:haunted_manor/if_haunted_manor3",
    "idas:haunted_manor/if_haunted_manor4",
    "idas:labyrinth/bopfloor1",
    "idas:labyrinth/bopfloor2",
    "idas:labyrinth/boplabyrinth_entrance",
    "idas:labyrinth/boplabyrinth_entrance2",
    "idas:labyrinth/if_floor1",
    "idas:labyrinth/if_floor2",
    "idas:labyrinth/if_labyrinth_entrance",
    "idas:labyrinth/if_labyrinth_entrance2",
    "idas:labyrinth/if_tomb",
    "idas:labyrinth/test",
    "idas:pillager_camp/pillager_camp1",
}

MISSING = {
    "idas:ancient_mines": [{"id": "idas:ancient_mines/ancient_mines_entrance2", "kind": "pool"}],
    "idas:desert_pyramid": [{"id": "idas:desert_pyramid/desert_pyramid_villager", "kind": "pool"}],
    "idas:iceandfire/dread_citadel": [
        {"id": "idas:dread_citadel/dread_citadel12", "kind": "pool"},
        {"id": "idas:dread_citadel/dread_citadel5", "kind": "pool"},
    ],
}


def test_idas_payload_and_component_dispositions() -> None:  # noqa: C901, PLR0915
    # One frozen archive and its complete component partition form the scope assertion.
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("idas-"))
    assert source.sha256 == "7f5031dd90ae0b32d7fe5c6c47c877cac1eb95a178bc78d196cb24c17ce82522"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    classes: set[str] = set()
    roots: dict[str, dict[str, JsonValue]] = {}
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 967
        for folder, digest in (
            (
                "idas-suppression",
                "d6b5776443ad0f76f42e94d3e54fa497dbdea94fd6eef096ee3595c3a48be376",
            ),
            ("idas-provider", "b3c57a302eacff4c8a957037fa610e7480d0d5a29d0715eeedea159d27cc20fe"),
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
        assert len(classes) == 21
        assert classes == {n for n in names if n.endswith(".class")}
        for name in names:
            if name in classes | {
                "META-INF/MANIFEST.MF",
                "META-INF/neoforge.mods.toml",
                "pack.mcmeta",
                "idas-common.mixins.json",
                "idas-common-refmap.json",
            }:
                continue
            if name.startswith("assets/idas/"):
                assert name.endswith((".png", ".json", ".ogg")), name
                continue
            assert name.startswith(
                (
                    "data/idas/",
                    "data/integrated_api/tags/",
                    "data/minecraft/tags/",
                    "data/supplementaries/tags/",
                )
            ), name
            assert name.endswith((".nbt", ".json")), name
            kind = name.split("/")[2]
            assert kind in {
                "worldgen",
                "structure",
                "loot_table",
                "tags",
                "advancement",
                "integrated_structure_spawners",
                "jukebox_song",
                "recipe",
            }, name
            if kind == "worldgen":
                assert name.split("/")[3] in {
                    "structure",
                    "structure_set",
                    "template_pool",
                    "processor_list",
                }, name
            for category, ids in groups.items():
                found = resource_identity(
                    name, category, ".nbt" if category == "structure" else ".json"
                )
                if found:
                    ids.add(found[0])
                    if category == "worldgen/structure":
                        roots[found[0]] = cast(
                            "dict[str, JsonValue]", json.loads(archive.read(name))
                        )
        assert {
            k: (v["change_pool_mods"], v["new_pool"])
            for k, v in roots.items()
            if v["type"] == "integrated_api:mod_adaptive_structure"
        } == {
            "idas:enchantingtower": ("ars_nouveau", "idas:enchantingtower/ars_enchantingtower"),
            "idas:haunted_manor": ("iceandfire", "idas:haunted_manor/if_haunted_manor1"),
            "idas:labyrinth": ("iceandfire", "idas:labyrinth/if_labyrinth_entrance"),
        }
        assert {
            k: v["required_mods"]
            for k, v in roots.items()
            if v["type"] == "integrated_api:optional_dependency_structure"
        } == {
            "idas:ars_nouveau/archmages_tower": "ars_nouveau",
            "idas:iceandfire/dread_citadel": "iceandfire",
            "idas:iceandfire/sirens_cove": "iceandfire",
        }
        assert all(
            cast("str", v["type"])
            in {
                "integrated_api:generic_structure",
                "integrated_api:mod_adaptive_structure",
                "integrated_api:optional_dependency_structure",
                "integrated_api:nether_structure",
                "integrated_api:over_lava_nether_structure",
            }
            for v in roots.values()
        )
        spawners = [n for n in names if "/integrated_structure_spawners/" in n]
        assert len(spawners) == 18
        for name in spawners:
            data = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(archive.read(name)))
            assert set(data) == {"mobs"}
            assert all(set(mob) == {"name", "weight"} for mob in data["mobs"])
        assert json.loads(
            archive.read("data/idas/tags/worldgen/structure/applies_mining_fatigue.json")
        ) == {"replace": False, "values": ["idas:labyrinth"]}
    registry = read_registry(
        Path("evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt")
    )
    assert groups["worldgen/structure"] == {r for r in registry if r.startswith("idas:")}
    assert len(roots) == 84
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    structures = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    traces = {k: structures[k] for k in roots}
    assert len(groups["worldgen/template_pool"]) == 214
    assert len(groups["structure"]) == 259
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


def test_idas_labyrinth_existing_encounter_hooks() -> None:
    config = Path("evidence/item-6/frozen/config/idas-neoforge-1_21.toml")
    assert hashlib.sha256(config.read_bytes()).hexdigest() == (
        "7c81cad8f7fe70cb4538c76023f39bf17b8d3d65226ae71084e61844d7aa34d4"
    )
    assert tomllib.loads(config.read_text())["IDAS"]["General"]["Apply Mining Fatigue"] is True
    directory = Path("evidence/item-8/sources/idas-provider/idas-1.13.7+1.21.1-neoforge.jar")
    tick = (directory / "com.craisinlord.idas.mixins.ServerPlayerTickMixin.txt").read_text()
    death = (directory / "com.craisinlord.idas.mixins.LabyrinthBossKilledMixin.txt").read_text()
    level = (directory / "com.craisinlord.idas.mixins.ServerLevelMixin.txt").read_text()
    assert "ConfigModule$General.applyMiningFatigue:Z" in tick
    assert "ServerPlayerGameMode.isSurvival:()Z" in tick
    assert "stateCache.isCleared:" in tick
    assert "MobEffects.DIG_SLOWDOWN:" in tick
    assert "getStructureWithPieceAt:" in tick
    assert "stateCache.setCleared:" in death
    assert "Pharaoh of the Labyrinth" in death
    assert "IDASTags.APPLIES_MINING_FATIGUE:" in death
    assert "getDimensionPath:" in level
    assert "class com/craisinlord/idas/state/stateCache" in level
