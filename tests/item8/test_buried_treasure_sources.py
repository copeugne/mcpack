from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_buried_treasure_direct_piece_source_binding() -> None:
    code: dict[str, str] = {}
    for directory, digest in {
        "vanilla-buried-treasure-code":
            "a3ee21e981a4c041695e894ba4c5ef8221ac720283870f2e71f9cb41b0a5bd4f",
        "vanilla-end-city-code":
            "ca7cb2c777ad0fc638e28cded50a78ab048ca26ad243eeb564fa72be7cac943c",
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
    group = next(r for r in decisions["groups"] if r["family_id"] == "minecraft:buried_treasure")
    variant = cast("dict[str, dict[str, JsonValue]]", group["variants"])[
        "minecraft:buried_treasure"
    ]
    assert variant["missing_components"] == variant["vanilla_code_template_ids"] == []
    piece = code[str(variant["vanilla_code_piece_class"])]
    assert "BuiltInLootTables.BURIED_TREASURE:" in piece
    assert "StructureTemplate" not in piece
    attrs = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    tables = cast("list[str]", attrs["loot_table_source"]["vanilla_assigned_tables"])
    assert tables == ["minecraft:chests/buried_treasure"]
    constants = code["net/minecraft/world/level/storage/loot/BuiltInLootTables.class"]
    assert "// String " + tables[0].removeprefix("minecraft:") in constants
    # The successful support match excludes DOWN from the air/liquid infill branch.
    # Retain the center plus the other possible direct write targets; this is an
    # envelope, not a claim that all positions change in a generated world.
    targets = [(0, 0, 0), (-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0)]
    spans = [max(p[axis] for p in targets) - min(p[axis] for p in targets) + 1
             for axis in range(3)]
    assert attrs["approximate_footprint"]["chest_target_xz_blocks"] == [1, 1]
    assert attrs["approximate_footprint"]["direct_write_envelope_xz_blocks"] == [spans[0], spans[2]]
    assert attrs["approximate_vertical_size"]["chest_target_blocks"] == 1
    assert attrs["approximate_vertical_size"]["direct_write_envelope_blocks"] == spans[1]
    assert attrs["mob_source"]["authored_entity_ids"] == []
    assert attrs["generated_spawners"]["vanilla_spawner_block_types"] == []
    assert cast("dict[str, JsonValue]", variant["definition"])["spawn_overrides"] == {}
    for source, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256(Path(source).read_bytes()).hexdigest() == digest
