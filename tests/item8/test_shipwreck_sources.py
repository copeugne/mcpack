from __future__ import annotations

import gzip
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_shipwreck_templates_sizes_and_markers() -> None:
    root = Path("evidence/item-8/sources/vanilla-shipwreck-code")
    raw = (root / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "313d8031a873de27b39ca5fa8fed9ab1ea1f3694fc56db8afcd7127a3e4415b8"
    )
    code: dict[str, str] = {}
    for entry in cast("list[dict[str, str]]", json.loads(raw)):
        payload = (root / entry["disassembly"]).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == entry["disassembly_sha256"]
        code[entry["class"].rsplit("/", 1)[1]] = payload.decode()
    initializer = code["ShipwreckPieces.class"].split("static {};")[1]
    beached, ocean = re.split(r"putstatic.*Field STRUCTURE_LOCATION_BEACHED:.*", initializer)
    beach_ids = cast("list[str]", re.findall(r"// String (shipwreck/\S+)", beached))
    ocean_ids = cast("list[str]", re.findall(r"// String (shipwreck/\S+)", ocean))
    assert len(beach_ids) == len(set(beach_ids)) == 11
    assert len(ocean_ids) == len(set(ocean_ids)) == 20
    assert set(beach_ids) <= set(ocean_ids)
    raw = Path("evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705"
    )
    catalog = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(raw)))
    templates = [row for row in catalog["resources"]
                 if str(row["path"]).startswith("data/minecraft/structure/shipwreck/")]
    assert len(templates) == len(ocean_ids)
    assert {str(row["path"]).removeprefix("data/minecraft/structure/").removesuffix(".nbt")
            for row in templates} == set(ocean_ids)
    sizes = [cast("list[int]", cast("dict[str, JsonValue]", row["document"])["size"])
             for row in templates]
    for row in templates:
        name = str(row["path"]).rsplit("/", 1)[1].removesuffix(".nbt").removesuffix("_degraded")
        document = cast("dict[str, JsonValue]", row["document"])
        expected_size = {
            "rightsideup_backhalf": [9, 9, 16], "rightsideup_fronthalf": [9, 9, 24],
            "rightsideup_full": [9, 9, 28], "sideways_backhalf": [9, 9, 17],
            "sideways_fronthalf": [9, 9, 24], "sideways_full": [9, 9, 28],
            "upsidedown_backhalf": [9, 9, 16], "upsidedown_fronthalf": [9, 9, 22],
            "upsidedown_full": [9, 9, 28], "with_mast": [9, 21, 28],
        }[name]
        assert document["size"] == expected_size
        assert document["entities"] == []
        palettes = cast("list[list[dict[str, JsonValue]]]",
                        document.get("palettes") or [document["palette"]])
        states = cast("dict[str, int]", document["state_counts"])
        block_types = {str(palette[int(index)]["Name"]) for palette in palettes
                       for index, count in states.items() if count}
        assert block_types.isdisjoint({"minecraft:spawner", "minecraft:trial_spawner"})
        blocks = cast("list[dict[str, JsonValue]]", document["block_entities"])
        markers = Counter(str(cast("dict[str, JsonValue]", block["nbt"])["metadata"])
                          for block in blocks
                          if cast("dict[str, JsonValue]", block["nbt"]).get("id")
                          == "minecraft:structure_block")
        expected_markers = {"supply_chest", "map_chest", "treasure_chest"}
        if name.endswith("backhalf"):
            expected_markers = {"map_chest", "treasure_chest"}
        elif name.endswith("fronthalf"):
            expected_markers = {"supply_chest"}
            if name == "upsidedown_fronthalf":
                expected_markers.add("map_chest")
        assert markers == Counter(dict.fromkeys(expected_markers, 1))
    decisions = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()
    ))
    group = next(row for row in decisions["groups"] if row["family_id"] == "minecraft:shipwreck")
    variants = cast("dict[str, dict[str, JsonValue]]", group["variants"])
    for identifier, candidates in (
        ("minecraft:shipwreck", ocean_ids), ("minecraft:shipwreck_beached", beach_ids)
    ):
        assert variants[identifier]["vanilla_code_template_ids"] == [
            "minecraft:" + candidate for candidate in candidates
        ]
        assert variants[identifier]["missing_components"] == []
    attrs = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    assert {size[0] for size in sizes} == {
        cast("int", attrs["approximate_footprint"]["nominal_width_blocks"])
    }
    assert sorted({size[2] for size in sizes}) == (
        attrs["approximate_footprint"]["nominal_length_options_blocks"]
    )
    assert sorted({size[1] for size in sizes}) == (
        attrs["approximate_vertical_size"]["nominal_height_options_blocks"]
    )
    for source, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256(Path(source).read_bytes()).hexdigest() == digest
