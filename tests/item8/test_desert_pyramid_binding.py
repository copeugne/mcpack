from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_desert_pyramid_callback_binds_the_frozen_piece() -> None:
    root = Path("evidence/item-8/sources/vanilla-desert-pyramid-binding-code")
    raw = (root / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "f83997815e0225442cdcd1819b3b7b1c210c8296da1b22191c7bba31df5e3b1c"
    )
    entries = cast("list[dict[str, str]]", json.loads(raw))
    code: dict[str, str] = {}
    for entry in entries:
        payload = (root / entry["disassembly"]).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == entry["disassembly_sha256"]
        code[entry["class"].rsplit("/", 1)[1]] = payload.decode()
    original = Path("evidence/item-8/sources/vanilla-desert-pyramid-code/identities.json")
    assert hashlib.sha256(original.read_bytes()).hexdigest() == (
        "89770d3b09f15c47e801b2889bf431d3f5e823c047cc8025c1fd433932e405d9"
    )
    previous = cast("list[dict[str, str]]", json.loads(original.read_bytes()))
    structure = next(e for e in entries if e["class"].endswith("/DesertPyramidStructure.class"))
    old = next(e for e in previous if e["class"] == structure["class"])
    assert structure["class_sha256"] == old["class_sha256"]
    assert structure["archive_sha256"] == old["archive_sha256"]
    bootstrap = code["DesertPyramidStructure.class"].split("BootstrapMethods:", 1)[1]
    first = bootstrap.split("\n  1:", 1)[0]
    assert (
        'REF_newInvokeSpecial net/minecraft/world/level/levelgen/structure/structures/'
        'DesertPyramidPiece."<init>":(Lnet/minecraft/util/RandomSource;II)V'
    ) in first
    assert "InvokeDynamic #0:construct:" in code["DesertPyramidStructure.class"]
    assert "SinglePieceStructure$PieceConstructor.construct:" in code["SinglePieceStructure.class"]


def test_desert_pyramid_content_and_loot_paths() -> None:
    decisions = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()
    ))
    group = next(g for g in decisions["groups"] if g["family_id"] == "minecraft:desert_pyramid")
    code: dict[str, str] = {}
    for source, digest in cast("dict[str, str]", group["evidence"]).items():
        raw = Path(source).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        if not source.endswith("/identities.json"):
            continue
        for entry in cast("list[dict[str, str]]", json.loads(raw)):
            payload = (Path(source).parent / entry["disassembly"]).read_bytes()
            assert hashlib.sha256(payload).hexdigest() == entry["disassembly_sha256"]
            code[entry["class"].rsplit("/", 1)[1]] = payload.decode()
    piece = code["DesertPyramidPiece.class"]
    structure = code["DesertPyramidStructure.class"]
    variant = cast("dict[str, dict[str, JsonValue]]", group["variants"])["minecraft:desert_pyramid"]
    assert variant["missing_components"] == variant["vanilla_code_template_ids"] == []
    assert str(variant["vanilla_code_piece_class"]).endswith("/DesertPyramidPiece.class")
    blocks = set(cast("list[str]", re.findall(
        r"Field net/minecraft/world/level/block/Blocks\.([A-Z_]+):", piece + structure
    )))
    assert {"TNT", "STONE_PRESSURE_PLATE", "SUSPICIOUS_SAND"} <= blocks
    assert not {"SPAWNER", "TRIAL_SPAWNER"} & blocks
    assert "net/minecraft/world/entity/EntityType." not in piece + structure
    assert re.search(r"Method createChest:[^\n]+\n\s*3651: bastore", piece)
    attrs = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    assert attrs["mob_source"]["authored_entity_ids"] == []
    assert attrs["generated_spawners"]["vanilla_spawner_block_types"] == []
    tables = attrs["loot_table_source"]["vanilla_assigned_tables"]
    assert tables == ["minecraft:archaeology/desert_pyramid", "minecraft:chests/desert_pyramid"]
    builtin = code["BuiltInLootTables.class"]
    for constant, path in (
        ("DESERT_PYRAMID", "chests/desert_pyramid"),
        ("DESERT_PYRAMID_ARCHAEOLOGY", "archaeology/desert_pyramid"),
    ):
        assert re.search(
            rf"// String {path}\n[^\n]+\n[^\n]+// Field {constant}:", builtin
        )
        assert f"BuiltInLootTables.{constant}:" in piece + structure
