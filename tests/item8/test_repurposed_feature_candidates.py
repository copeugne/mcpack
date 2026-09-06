from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue

DUNGEONS = (
    "badlands", "dark_forest", "deep", "desert", "end", "icy", "jungle", "mushroom",
    "nether", "ocean_cold", "ocean_frozen", "ocean_lukewarm", "ocean_neutral", "ocean_warm",
    "snow", "swamp",
)
WELLS = ("badlands", "cherry", "forest", "mossy_stone", "mushroom", "nether", "snow")


def test_repurposed_nonregistry_nbt_candidates() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name.startswith("repurposed_structures-"))
    assert source.sha256 == "aeb473f0a0a0632cea089377cdd9f66c42cf6f97557fd32c368ac40635285dd2"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    expected = {"dungeons/" + n: "nbt_dungeon" for n in DUNGEONS} | {
        "wells/" + n: "nbt_feature" for n in WELLS
    }
    prefix = "data/repurposed_structures/worldgen/"
    with ZipFile(source.path) as archive:
        configs = {
            n.removeprefix(prefix + "configured_feature/").removesuffix(".json"):
            cast("dict[str, JsonValue]", json.loads(archive.read(n)))
            for n in archive.namelist()
            if n.startswith(prefix + "configured_feature/") and n.endswith(".json")
        }
        selected = {k: d for k, d in configs.items() if d["type"] in {
            "repurposed_structures:nbt_dungeon", "repurposed_structures:nbt_feature",
        }}
        assert set(selected) == set(expected)
        for candidate, kind in expected.items():
            assert selected[candidate]["type"] == "repurposed_structures:" + kind
            config = cast("dict[str, JsonValue]", selected[candidate]["config"])
            entries = cast("list[dict[str, JsonValue]]", config[
                "dungeon_nbt_entries" if kind == "nbt_dungeon" else "nbt_entries"
            ])
            assert entries
            for entry in entries:
                namespace, path = cast("str", entry["resourcelocation"]).split(":", 1)
                assert f"data/{namespace}/structure/{path}.nbt" in archive.namelist()
            placed = cast("dict[str, JsonValue]", json.loads(archive.read(
                prefix + "placed_feature/" + candidate + ".json"
            )))
            assert placed["feature"] == "repurposed_structures:" + candidate
            modifier = cast("dict[str, JsonValue]", json.loads(archive.read(
                "data/repurposed_structures/neoforge/biome_modifier/" + candidate + ".json"
            )))
            assert modifier["feature"] == "repurposed_structures:" + candidate
            assert modifier["type"] in {
                "repurposed_structures:additions_modifier",
                "repurposed_structures:additions_temperature_modifier",
            }
