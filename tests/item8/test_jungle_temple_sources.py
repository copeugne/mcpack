from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_jungle_temple_binding_dimensions_and_container_paths() -> None:
    decisions = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()
    ))
    group = next(g for g in decisions["groups"] if g["family_id"] == "minecraft:jungle_pyramid")
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
    piece = code["JungleTemplePiece.class"]
    bootstrap = code["JungleTempleStructure.class"].split("BootstrapMethods:")[1]
    assert (
        'REF_newInvokeSpecial net/minecraft/world/level/levelgen/structure/structures/'
        'JungleTemplePiece."<init>":(Lnet/minecraft/util/RandomSource;II)V'
    ) in bootstrap.split("\n  1:")[0]
    assert "SinglePieceStructure$PieceConstructor.construct:" in code["SinglePieceStructure.class"]
    variant = cast("dict[str, dict[str, JsonValue]]", group["variants"])["minecraft:jungle_pyramid"]
    assert variant["missing_components"] == variant["vanilla_code_template_ids"] == []
    assert str(variant["vanilla_code_piece_class"]).endswith("/JungleTemplePiece.class")
    ints = [int(v) for v in cast("list[str]", re.findall(
        r"bipush\s+(\d+)", piece.split(
            "JungleTemplePiece(net.minecraft.util.RandomSource, int, int);"
        )[1].split("  public ")[0]
    ))]
    assert ints == [64, 12, 10, 15]
    attrs = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    assert attrs["approximate_footprint"]["nominal_piece_xz_blocks"] == [ints[1], ints[3]]
    assert attrs["approximate_vertical_size"]["nominal_piece_height_blocks"] == ints[2]
    for helper, flags in (
        ("createChest", ["placedMainChest", "placedHiddenChest"]),
        ("createDispenser", ["placedTrap1", "placedTrap2"]),
    ):
        found = re.findall(rf"Method {helper}:[^\n]+\n[^\n]+// Field (\w+):Z", piece)
        assert found == flags
    assert attrs["loot_table_source"]["vanilla_assigned_tables"] == [
        "minecraft:chests/jungle_temple", "minecraft:chests/jungle_temple_dispenser"
    ]
    for constant, path in (
        ("JUNGLE_TEMPLE", "chests/jungle_temple"),
        ("JUNGLE_TEMPLE_DISPENSER", "chests/jungle_temple_dispenser"),
    ):
        assert re.search(rf"// String {path}\n[^\n]+\n[^\n]+// Field {constant}:",
                         code["BuiltInLootTables.class"])
        assert f"BuiltInLootTables.{constant}:" in piece
    assert "net/minecraft/world/entity/EntityType." not in piece
    assert attrs["mob_source"]["authored_entity_ids"] == []
    assert attrs["generated_spawners"]["vanilla_spawner_block_types"] == []
    assert not re.search(r"Blocks\.(?:SPAWNER|TRIAL_SPAWNER):", piece)
