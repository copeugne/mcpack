from __future__ import annotations

import gzip
import hashlib
import json
import re
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_igloo_components_content_and_nominal_assembly() -> None:
    root = Path("evidence/item-8/sources/vanilla-igloo-code")
    raw = (root / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "5104752aa5eb795053f75e8d62731b7ea7d79af1f9cacfdccfe2e55f9336838e"
    )
    code: dict[str, str] = {}
    for entry in cast("list[dict[str, str]]", json.loads(raw)):
        payload = (root / entry["disassembly"]).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == entry["disassembly_sha256"]
        code[entry["class"].rsplit("/", 1)[1]] = payload.decode()
    components = set(cast("list[str]", re.findall(
        r"// String (igloo/\S+)", code["IglooPieces.class"]
    )))
    assert components == {"igloo/top", "igloo/middle", "igloo/bottom"}
    raw = Path("evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705"
    )
    catalog = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(raw)))
    templates = [row for row in catalog["resources"]
                 if str(row["path"]).startswith("data/minecraft/structure/igloo/")]
    assert len(templates) == 3
    documents = {str(row["path"]).rsplit("/", 1)[1].removesuffix(".nbt"):
                 cast("dict[str, JsonValue]", row["document"]) for row in templates}
    assert {"igloo/" + name for name in documents} == components
    assert {name: doc["size"] for name, doc in documents.items()} == {
        "top": [7, 5, 8], "middle": [3, 3, 3], "bottom": [7, 6, 9]
    }
    for name, doc in documents.items():
        entities = cast("list[dict[str, JsonValue]]", doc["entities"])
        assert [cast("dict[str, JsonValue]", entity["nbt"])["id"] for entity in entities] == (
            ["minecraft:villager", "minecraft:zombie_villager"] if name == "bottom" else []
        )
        palettes = cast("list[list[dict[str, JsonValue]]]", doc.get("palettes") or [doc["palette"]])
        assert {str(state["Name"]) for palette in palettes for state in palette}.isdisjoint(
            {"minecraft:spawner", "minecraft:trial_spawner"}
        )
    blocks = cast("list[dict[str, JsonValue]]", documents["bottom"]["block_entities"])
    by_id = {str(cast("dict[str, JsonValue]", block["nbt"])["id"]): block for block in blocks}
    assert len(by_id) == len(blocks) == 4
    marker = cast("dict[str, JsonValue]", by_id["minecraft:structure_block"]["nbt"])
    assert (marker["mode"], marker["metadata"]) == ("DATA", "chest")
    assert by_id["minecraft:structure_block"]["pos"] == [1, 2, 6]
    assert by_id["minecraft:chest"]["pos"] == [1, 1, 6]
    assert cast("dict[str, JsonValue]", by_id["minecraft:brewing_stand"]["nbt"])["Items"] == [
        {"Slot": 1, "components": {"minecraft:potion_contents": {"potion": "minecraft:weakness"}},
         "count": 1, "id": "minecraft:splash_potion"}
    ]
    decisions = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()
    ))
    group = next(row for row in decisions["groups"] if row["family_id"] == "minecraft:igloo")
    variant = cast("dict[str, dict[str, JsonValue]]", group["variants"])["minecraft:igloo"]
    assert variant["vanilla_code_template_ids"] == sorted("minecraft:" + x for x in components)
    assert variant["missing_components"] == []
    attrs = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    assert attrs["mob_source"]["authored_entity_ids"] == [
        "minecraft:villager", "minecraft:zombie_villager"
    ]
    # Source offsets and pivots align all components to the same horizontal pivot
    # and height sample. Union the unrotated template envelopes, not piece counts.
    top = cast("list[int]", documents["top"]["size"])
    bottom = cast("list[int]", documents["bottom"]["size"])
    assert attrs["approximate_footprint"]["without_basement_xz_blocks"] == [top[0], top[2]]
    assert attrs["approximate_footprint"]["with_basement_xz_blocks"] == [
        max(top[0], bottom[0]), max(top[2], bottom[2] - 2) + 2
    ]
    assert attrs["approximate_vertical_size"]["without_basement_blocks"] == top[1]
    assert attrs["approximate_vertical_size"]["with_basement_options_blocks"] == [
        top[1] + 3 + 3 * n for n in range(4, 12)
    ]
    for source, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256(Path(source).read_bytes()).hexdigest() == digest
