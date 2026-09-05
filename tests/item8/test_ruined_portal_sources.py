from __future__ import annotations

import gzip
import hashlib
import json
import re
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_ruined_portal_components_chests_and_empty_pool_metadata() -> None:
    root = Path("evidence/item-8/sources/vanilla-ruined-portal-code")
    raw = (root / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "c5cde03aa864cfadf9b167a01e4cd90d2193ba6e67b5c5b0a4edaff56ef93f79"
    )
    code: dict[str, str] = {}
    for entry in cast("list[dict[str, str]]", json.loads(raw)):
        payload = (root / entry["disassembly"]).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == entry["disassembly_sha256"]
        code[entry["class"].rsplit("/", 1)[1]] = payload.decode()
    references = cast("list[str]", re.findall(
        r"// String (ruined_portal/\S+)", code["RuinedPortalStructure.class"]
    ))
    assert references == [f"ruined_portal/portal_{i}" for i in range(1, 11)] + [
        f"ruined_portal/giant_portal_{i}" for i in range(1, 4)
    ]
    raw = Path("evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705"
    )
    catalog = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(raw)))
    rows = [r for r in catalog["resources"]
            if str(r["path"]).startswith("data/minecraft/structure/ruined_portal/")]
    assert len(rows) == 13
    assert {str(r["path"]).removeprefix("data/minecraft/structure/").removesuffix(".nbt")
            for r in rows} == set(references)
    jigsaws: dict[str, JsonValue] = {}
    for row in rows:
        doc = cast("dict[str, JsonValue]", row["document"])
        assert doc["entities"] == []
        palettes = cast("list[list[dict[str, JsonValue]]]", doc.get("palettes") or [doc["palette"]])
        assert {str(s["Name"]) for palette in palettes for s in palette}.isdisjoint(
            {"minecraft:spawner", "minecraft:trial_spawner"}
        )
        blocks = cast("list[dict[str, JsonValue]]", doc["block_entities"])
        chests = 0
        for block in blocks:
            nbt = cast("dict[str, JsonValue]", block["nbt"])
            if nbt["id"] == "minecraft:chest":
                assert nbt["LootTable"] == "minecraft:chests/ruined_portal"
                chests += 1
            else:
                assert nbt["id"] == "minecraft:jigsaw"
                assert nbt["name"] == nbt["pool"] == nbt["target"] == "minecraft:empty"
                name = str(row["path"]).rsplit("/", 1)[1]
                assert name not in jigsaws
                jigsaws[name] = nbt["final_state"]
        assert chests == 1
    assert jigsaws == {f"portal_{i}.nbt": "minecraft:air" if i == 3 else "minecraft:netherrack"
                       for i in range(1, 6)}
    decisions = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()
    ))
    group = next(r for r in decisions["groups"] if r["family_id"] == "minecraft:ruined_portal")
    variants = cast("dict[str, dict[str, JsonValue]]", group["variants"])
    assert len(variants) == 7
    attrs = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    placements = cast("dict[str, JsonValue]", attrs[
        "underground_surface_classification"
    ]["placement_modes_by_structure"])
    for key, variant in variants.items():
        assert variant["vanilla_code_template_ids"] == sorted("minecraft:" + r for r in references)
        assert variant["missing_components"] == []
        definition = cast("dict[str, JsonValue]", variant["definition"])
        setups = cast("list[dict[str, JsonValue]]", definition["setups"])
        assert placements[key] == sorted({str(setup["placement"]) for setup in setups})
        assert definition["spawn_overrides"] == {}
    assert attrs["mob_source"]["authored_entity_ids"] == []
    assert attrs["generated_spawners"]["vanilla_template_spawner_block_types"] == []
    assert attrs["loot_table_source"]["packaged_tables"] == ["minecraft:chests/ruined_portal"]
    for source, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256(Path(source).read_bytes()).hexdigest() == digest
