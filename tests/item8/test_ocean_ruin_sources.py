from __future__ import annotations

import gzip
import hashlib
import json
import re
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_ocean_ruin_templates_markers_and_source_assignments() -> None:
    code: dict[str, str] = {}
    for directory, digest in {
        "vanilla-ocean-ruin-code":
            "966f0fe1112562cc35c718bad64a241c2ef4dd8ad7331f9afd4a77b7da155382",
        "vanilla-end-city-code":
            "ca7cb2c777ad0fc638e28cded50a78ab048ca26ad243eeb564fa72be7cac943c",
    }.items():
        root = Path("evidence/item-8/sources") / directory
        raw = (root / "identities.json").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        for entry in cast("list[dict[str, str]]", json.loads(raw)):
            payload = (root / entry["disassembly"]).read_bytes()
            assert hashlib.sha256(payload).hexdigest() == entry["disassembly_sha256"]
            code[entry["class"].rsplit("/", 1)[1]] = payload.decode()
    references = cast("list[str]", re.findall(
        r"// String (underwater_ruin/\S+)", code["OceanRuinPieces.class"]
    ))
    assert len(references) == len(set(references)) == 48
    raw = Path("evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705"
    )
    catalog = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(raw)))
    templates = [row for row in catalog["resources"]
                 if str(row["path"]).startswith("data/minecraft/structure/underwater_ruin/")]
    assert len(templates) == 48
    assert {str(row["path"]).removeprefix("data/minecraft/structure/").removesuffix(".nbt")
            for row in templates} == set(references)
    for row in templates:
        doc = cast("dict[str, JsonValue]", row["document"])
        assert doc["entities"] == []
        assert doc["size"] == ([16, 16, 16] if "/big_" in str(row["path"]) else [6, 7, 7])
        palettes = cast("list[list[dict[str, JsonValue]]]", doc.get("palettes") or [doc["palette"]])
        assert {str(s["Name"]) for palette in palettes for s in palette}.isdisjoint(
            {"minecraft:spawner", "minecraft:trial_spawner"}
        )
        blocks = cast("list[dict[str, JsonValue]]", doc["block_entities"])
        assert blocks
        for block in blocks:
            nbt = cast("dict[str, JsonValue]", block["nbt"])
            assert nbt["id"] == "minecraft:structure_block"
            assert nbt["mode"] == "DATA"
            assert nbt["metadata"] in ("chest", "drowned")
    decisions = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()
    ))
    group = next(row for row in decisions["groups"] if row["family_id"] == "minecraft:ocean_ruin")
    variants = cast("dict[str, dict[str, JsonValue]]", group["variants"])
    for temperature, expected_count in (("cold", 36), ("warm", 12)):
        variant = variants["minecraft:ocean_ruin_" + temperature]
        expected = sorted("minecraft:" + r for r in references
                          if ("warm" in r) == (temperature == "warm"))
        assert len(expected) == expected_count
        assert variant["vanilla_code_template_ids"] == expected
        assert variant["missing_components"] == []
    attrs = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    assert attrs["mob_source"]["authored_entity_ids"] == ["minecraft:drowned"]
    assert attrs["generated_spawners"]["vanilla_template_spawner_block_types"] == []
    loot = attrs["loot_table_source"]
    for field in ("chest_tables_by_size", "archaeology_tables_by_temperature"):
        for table in cast("dict[str, str]", loot[field]).values():
            assert (
                "// String " + table.removeprefix("minecraft:") in code["BuiltInLootTables.class"]
            )
    for source, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256(Path(source).read_bytes()).hexdigest() == digest
