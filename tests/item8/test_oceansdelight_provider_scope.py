from __future__ import annotations

import hashlib
import json
import tomllib
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_oceansdelight_full_payload_is_food_and_existing_mob_loot() -> None:
    directory = Path("evidence/item-8/sources/oceansdelight-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "db7a1ce1a12229d00abefb1eacf24bb3b5a28f824e6b86746855e1c943458c48"
    )
    identities = cast("list[dict[str, str]]", json.loads(raw))
    source = next(s for s in retained_sources(Path.cwd()) if s.name == identities[0]["archive"])
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        classes = {r["class"] for r in identities}
        assert len(classes) == len(identities) == 15
        assert {n for n in names if n.endswith(".class")} == classes
        for row in identities:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        assert {c for c in classes if b"Lnet/neoforged/fml/common/Mod;" in archive.read(c)} == {
            "com/scouter/oceansdelight/OceansDelight.class",
        }
        assert {
            c for c in classes
            if b"Lnet/neoforged/fml/common/EventBusSubscriber;" in archive.read(c)
        } == {"com/scouter/oceansdelight/datagen/DataGenerators.class"}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert set(metadata) == {"modLoader", "loaderVersion", "license", "mods", "dependencies"}
        assert metadata["modLoader"] == "javafml"
        files = [n for n in names if not n.endswith(("/", ".class"))]
        assert Counter(
            "/".join(n.split("/")[:3]) if n.startswith(("assets/", "data/"))
            else n.split("/")[0] for n in files
        ) == {
            "META-INF": 2, "oceans_delight_logo.png": 1, ".cache": 5,
            "assets/oceansdelight/blockstates": 1, "assets/oceansdelight/lang": 7,
            "assets/oceansdelight/models": 32, "assets/oceansdelight/textures": 27,
            "data/diet/tags": 4, "data/farmersdelight/loot_modifiers": 4,
            "data/minecraft/tags": 1, "data/neoforge/loot_modifiers": 1,
            "data/oceansdelight/advancement": 27, "data/oceansdelight/recipe": 31,
        }
        recipe_types: Counter[str] = Counter()
        for name in files:
            if name.startswith("assets/"):
                assert name.endswith((".json", ".png"))
            if not name.startswith("data/"):
                continue
            assert name.endswith(".json")
            data = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
            if "/recipe/" in name:
                recipe_types[str(data["type"])] += 1
            elif "/advancement/" in name:
                rewards = cast("dict[str, JsonValue]", data["rewards"])
                assert set(rewards) == {"recipes"}
            elif "/tags/" in name:
                assert set(data) <= {"replace", "values"}
                assert "/tags/items/" in name or name == (
                    "data/minecraft/tags/block/mineable/pickaxe.json"
                )
        assert recipe_types == {
            "minecraft:crafting_shapeless": 7, "minecraft:smelting": 5,
            "minecraft:campfire_cooking": 5, "minecraft:smoking": 5,
            "farmersdelight:cooking": 5, "farmersdelight:cutting": 4,
        }
        modifiers = {
            "cut_elder_guardian": ("elder_guardian", "elder_guardian_slab"),
            "cut_tentacles_glow_squid": ("glow_squid", "tentacles"),
            "cut_tentacles_squid": ("squid", "tentacles"),
            "guardian_drop": ("guardian", "guardian"),
        }
        global_list = cast("dict[str, JsonValue]", json.loads(archive.read(
            "data/neoforge/loot_modifiers/global_loot_modifiers.json"
        )))
        assert global_list == {
            "replace": False, "entries": [
                "farmersdelight:cut_elder_guardian", "farmersdelight:cut_tentacles_squid",
                "farmersdelight:cut_tentacles_glow_squid", "farmersdelight:guardian_drop",
            ],
        }
        for name, (entity, item) in modifiers.items():
            data = cast("dict[str, JsonValue]", json.loads(archive.read(
                f"data/farmersdelight/loot_modifiers/{name}.json"
            )))
            conditions: list[JsonValue] = []
            if name.startswith("cut_"):
                conditions.append({
                    "condition": "minecraft:entity_properties", "entity": "attacker",
                    "predicate": {"equipment": {
                        "mainhand": {"items": "#farmersdelight:tools/knives"},
                    }},
                })
            conditions.append({
                "condition": "minecraft:entity_properties", "entity": "this",
                "predicate": {"type": f"minecraft:{entity}"},
            })
            assert data == {
                "type": "farmersdelight:add_item", "item": f"oceansdelight:{item}",
                "conditions": conditions,
            }
