from __future__ import annotations

import gzip
import hashlib
import json
import re
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_nether_fossil_single_template_content_and_dimensions() -> None:
    root = Path("evidence/item-8/sources/vanilla-nether-fossil-code")
    raw = (root / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "611e91bd71be08103760e8cd78339d1f904655941601f37214db08dd6a31b44e"
    )
    code: dict[str, str] = {}
    for entry in cast("list[dict[str, str]]", json.loads(raw)):
        payload = (root / entry["disassembly"]).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == entry["disassembly_sha256"]
        code[entry["class"].rsplit("/", 1)[1]] = payload.decode()
    references = cast("list[str]", re.findall(
        r"// String (nether_fossils/fossil_\d+)", code["NetherFossilPieces.class"]
    ))
    assert references == [f"nether_fossils/fossil_{i}" for i in range(1, 15)]
    raw = Path("evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705"
    )
    catalog = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(raw)))
    templates = [row for row in catalog["resources"]
                 if str(row["path"]).startswith("data/minecraft/structure/nether_fossils/")]
    assert len(templates) == 14
    documents = {"minecraft:" + str(row["path"]).removeprefix(
        "data/minecraft/structure/"
    ).removesuffix(".nbt"): cast("dict[str, JsonValue]", row["document"]) for row in templates}
    assert set(documents) == {"minecraft:" + ref for ref in references}
    for doc in documents.values():
        assert doc["entities"] == doc["block_entities"] == []
        palettes = cast("list[list[dict[str, JsonValue]]]", doc.get("palettes") or [doc["palette"]])
        assert {str(state["Name"]) for palette in palettes for state in palette} == {
            "minecraft:air", "minecraft:bone_block"
        }
    decisions = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()
    ))
    group = next(
        row for row in decisions["groups"] if row["family_id"] == "minecraft:nether_fossil"
    )
    variant = cast("dict[str, dict[str, JsonValue]]", group["variants"])["minecraft:nether_fossil"]
    assert variant["vanilla_code_template_ids"] == ["minecraft:" + ref for ref in references]
    assert variant["missing_components"] == []
    attrs = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    sizes = {key: cast("list[int]", doc["size"]) for key, doc in documents.items()}
    assert attrs["approximate_footprint"]["nominal_xz_by_template_blocks"] == {
        key: [size[0], size[2]] for key, size in sizes.items()
    }
    assert attrs["approximate_vertical_size"]["nominal_y_by_template_blocks"] == {
        key: size[1] for key, size in sizes.items()
    }
    assert attrs["mob_source"]["authored_entity_ids"] == []
    assert attrs["generated_spawners"]["vanilla_template_spawner_block_types"] == []
    assert attrs["loot_table_source"]["vanilla_assigned_tables"] == []
    for source, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256(Path(source).read_bytes()).hexdigest() == digest
