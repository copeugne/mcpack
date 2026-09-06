from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
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


def test_repurposed_existing_graph_partition() -> None:
    # Partition existing evidence; outside a graph does not mean unused or a new family.
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name.startswith("repurposed_structures-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == (
        "aeb473f0a0a0632cea089377cdd9f66c42cf6f97557fd32c368ac40635285dd2"
    )
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = {k: v for k, v in cast(
        "dict[str, dict[str, JsonValue]]", document["structures"]
    ).items() if k.startswith("repurposed_structures:")}
    assert len(traces) == 95
    with ZipFile(source.path) as archive:
        groups = {
            kind: {identity[0] for name in archive.namelist()
                   if (identity := resource_identity(name, kind, extension)) is not None}
            for kind, extension in (
                ("worldgen/structure", ".json"), ("worldgen/template_pool", ".json"),
                ("structure", ".nbt"),
            )
        }
    assert len(groups["worldgen/structure"]) == 107
    assert groups["worldgen/structure"] - traces.keys() == {
        "repurposed_structures:mansion_" + n for n in (
            "birch", "desert", "jungle", "mangrove", "oak", "savanna", "snowy", "taiga",
        )
    } | {"repurposed_structures:monument_" + n for n in ("desert", "icy", "jungle", "nether")}
    for kind, field, total, outside_counts in (
        ("worldgen/template_pool", "pools", 1099,
         {"mansions": 416, "monuments": 80, "cities": 2, "villages": 5}),
        ("structure", "templates", 3162, {
            "mansions": 597, "monuments": 92, "dungeons": 36, "wells": 7,
            "ancient_cities": 3, "bastions": 5, "mineshafts": 16,
            "strongholds": 2, "villages": 27,
        }),
    ):
        assert len(groups[kind]) == total
        reached = {r for t in traces.values() for r in cast("list[str]", t[field])}
        outside = groups[kind] - reached
        assert Counter(n.split(":", 1)[1].split("/", 1)[0] for n in outside) == outside_counts
    assert all(t["missing"] == [] for t in traces.values())
    assert all(t["unresolved_elements"] == [] for t in traces.values())
