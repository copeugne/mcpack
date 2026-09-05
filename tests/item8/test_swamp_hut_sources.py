from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_swamp_hut_direct_content_dimensions_and_spawn_candidates() -> None:
    code: dict[str, str] = {}
    for directory, digest in {
        "vanilla-swamp-hut-code":
            "504b9d418376e547f229aca14b3d91e8b60fa0e2e4fe84f733dfa1cfc376bb5e",
        "vanilla-scattered-feature-code":
            "62d64cfdb219f8424e9cbac0b6bb3aa683c773a8969ecf93fd558f6195a3b8e7",
    }.items():
        root = Path("evidence/item-8/sources") / directory
        raw = (root / "identities.json").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        for entry in cast("list[dict[str, str]]", json.loads(raw)):
            payload = (root / entry["disassembly"]).read_bytes()
            assert hashlib.sha256(payload).hexdigest() == entry["disassembly_sha256"]
            code[entry["class"]] = payload.decode()
    decisions = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()
    ))
    group = next(r for r in decisions["groups"] if r["family_id"] == "minecraft:swamp_hut")
    variant = cast("dict[str, dict[str, JsonValue]]", group["variants"])["minecraft:swamp_hut"]
    assert variant["missing_components"] == variant["vanilla_code_template_ids"] == []
    piece = code[str(variant["vanilla_code_piece_class"])]
    constructor = piece.split("  public ")[1]
    ints = [int(v) for v in cast("list[str]", re.findall(r"bipush\s+(\d+)", constructor))]
    assert ints == [64, 7, 7, 9]
    attrs = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    assert attrs["approximate_footprint"]["nominal_piece_xz_blocks"] == [ints[1], ints[3]]
    assert attrs["approximate_vertical_size"]["nominal_piece_height_blocks"] == ints[2]
    entities = sorted("minecraft:" + v.lower() for v in set(cast(
        "list[str]", re.findall(r"Field net/minecraft/world/entity/EntityType\.([A-Z_]+):", piece)
    )))
    assert entities == attrs["mob_source"]["authored_entity_ids"] == [
        "minecraft:cat", "minecraft:witch"
    ]
    blocks = set(cast("list[str]", re.findall(
        r"Field net/minecraft/world/level/block/Blocks\.([A-Z_]+):", piece
    )))
    assert blocks == {"AIR", "CAULDRON", "CRAFTING_TABLE", "OAK_FENCE", "OAK_LOG",
                      "POTTED_RED_MUSHROOM", "SPRUCE_PLANKS", "SPRUCE_STAIRS"}
    definition = cast("dict[str, JsonValue]", variant["definition"])
    overrides = cast("dict[str, dict[str, JsonValue]]", definition["spawn_overrides"])
    assert attrs["mob_source"]["natural_spawn_overrides"] == overrides
    assert set(overrides) == {"creature", "monster"}
    for category, entity in (("creature", "minecraft:cat"), ("monster", "minecraft:witch")):
        assert overrides[category] == {
            "bounding_box": "piece",
            "spawns": [{"type": entity, "weight": 1, "minCount": 1, "maxCount": 1}]
        }
    assert attrs["loot_table_source"]["vanilla_assigned_tables"] == []
    assert attrs["generated_spawners"]["vanilla_spawner_block_types"] == []
    for source, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256(Path(source).read_bytes()).hexdigest() == digest
