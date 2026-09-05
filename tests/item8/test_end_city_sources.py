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


def test_end_city_generator_templates_and_markers() -> None:
    root = Path("evidence/item-8/sources/vanilla-end-city-code")
    raw = (root / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "ca7cb2c777ad0fc638e28cded50a78ab048ca26ad243eeb564fa72be7cac943c"
    )
    identities = cast("list[dict[str, str]]", json.loads(raw))
    generators = {"EndCityPieces.class", *(f"EndCityPieces${n}.class" for n in range(1, 5))}
    referenced: set[str] = set()
    for entry in identities:
        code = (root / entry["disassembly"]).read_bytes()
        assert hashlib.sha256(code).hexdigest() == entry["disassembly_sha256"]
        if entry["class"].rsplit("/", 1)[1] in generators:
            referenced.update(re.findall(r"// String (\S+)", code.decode()))
    assert len(referenced) == 19
    raw = Path("evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705"
    )
    catalog = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(raw)))
    prefix = "data/minecraft/structure/end_city/"
    templates: dict[str, dict[str, JsonValue]] = {}
    for row in catalog["resources"]:
        path = str(row["path"])
        if path.startswith(prefix):
            name = path.removeprefix(prefix).removesuffix(".nbt")
            assert name not in templates
            templates[name] = cast("dict[str, JsonValue]", row["document"])
    assert referenced <= templates.keys()
    assert templates.keys() - referenced == {"tower_floor"}
    markers: dict[str, dict[str, int]] = {}
    for name in sorted(referenced):
        document = templates[name]
        assert document["entities"] == []
        blocks = cast("list[dict[str, JsonValue]]", document["block_entities"])
        counts: Counter[str] = Counter()
        for block in blocks:
            nbt = cast("dict[str, JsonValue]", block["nbt"])
            assert nbt.get("id") not in {"minecraft:mob_spawner", "minecraft:trial_spawner"}
            if nbt.get("id") == "minecraft:structure_block":
                assert nbt["mode"] == "DATA"
                counts[str(nbt["metadata"])] += 1
        if counts:
            markers[name] = dict(counts)
    assert markers == {
        "base_floor": {"Sentry": 2},
        "fat_tower_middle": {"Sentry": 4},
        "fat_tower_top": {"Chest": 2},
        "second_floor_2": {"Sentry": 1},
        "ship": {"Sentry": 3, "Chest": 2, "Elytra": 1},
        "third_floor_2": {"Sentry": 2, "Chest": 1},
        "tower_top": {"Sentry": 1},
    }
