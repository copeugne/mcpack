from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_create_generation_payload_and_captured_boundaries() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "create-1.21.1-6.0.10.jar")
    assert source.sha256 == "ef87fe5709f1ba1f5b8bb20a2925b5afb4669e178fd6d8bf10c167759eefe37a"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/create-generation-boundaries")
    raw = (directory / "identities.json").read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == "7fb69a735eb1ffd0ada39ca9d1950120cf5fa87b142dc3e9814fab7ab9b5a5fe"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    assert len(rows) == 4
    with ZipFile(source.path) as archive:
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert (
                hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                == row["disassembly_sha256"]
            )
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 11753
        assert Counter(n.split("/")[2] for n in names if n.startswith("data/")) == {
            "recipe": 1884,
            "advancement": 1150,
            "loot_table": 640,
            "tags": 183,
            "structure": 67,
            "create": 25,
            "damage_type": 9,
            "worldgen": 6,
            "data_maps": 4,
            "neoforge": 3,
            "enchantment": 2,
            "curios": 1,
        }
        templates = {n for n in names if n.endswith(".nbt")}
        tests = {n for n in templates if n.startswith("data/create/structure/gametest/")}
        ponder = {n for n in templates if n.startswith("assets/create/ponder/")}
        assert len(tests) == 67
        assert len(ponder) == 178
        assert templates == tests | ponder
        features = {"zinc_ore", "striated_ores_overworld", "striated_ores_nether"}
        assert {n for n in names if n.startswith("data/") and "/worldgen/" in n} == {
            f"data/create/worldgen/{kind}/{feature}.json"
            for kind in ("configured_feature", "placed_feature")
            for feature in features
        }
        assert {n for n in names if n.startswith("data/") and "/biome_modifier/" in n} == {
            f"data/create/neoforge/biome_modifier/{feature}.json" for feature in features
        }
        for feature in features:
            configured = cast(
                "dict[str, object]",
                json.loads(archive.read(f"data/create/worldgen/configured_feature/{feature}.json")),
            )
            assert configured["type"] == (
                "minecraft:ore" if feature == "zinc_ore" else "create:layered_ore"
            )
            placed = cast(
                "dict[str, object]",
                json.loads(archive.read(f"data/create/worldgen/placed_feature/{feature}.json")),
            )
            assert placed["feature"] == f"create:{feature}"
            assert cast("list[dict[str, object]]", placed["placement"])[-1] == {
                "type": "create:config_filter"
            }
            modifier = cast(
                "dict[str, object]",
                json.loads(archive.read(f"data/create/neoforge/biome_modifier/{feature}.json")),
            )
            assert modifier == {
                "type": "neoforge:add_features",
                "features": f"create:{feature}",
                "step": "underground_ores",
                "biomes": "#minecraft:is_nether"
                if feature.endswith("nether")
                else "#minecraft:is_overworld",
            }
