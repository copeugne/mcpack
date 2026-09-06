from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_bop_named_candidates_bind_packaged_routes_and_live_biomes() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("BiomesOPlenty-"))
    assert source.sha256 == "07f449b7766845883523ffadb8fb706ec011c1212aa378b48bea5841188f0b04"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    candidates = {"anomaly", "monolith", "bone_spine", "nether_bone_spine"}
    with ZipFile(source.path) as archive:
        data = {
            n: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
            for n in archive.namelist() if n.startswith("data/") and n.endswith(".json")
        }
        prefix = "data/biomesoplenty/worldgen/"
        for name in candidates:
            assert data[prefix + "configured_feature/" + name + ".json"] == {
                "type": "biomesoplenty:" + ("bone_spine" if name == "nether_bone_spine" else name),
                "config": {},
            }
        placed = {n: d for n, d in data.items() if n.startswith(prefix + "placed_feature/")}
        assert len(placed) == 321
        assert all(isinstance(d["feature"], str) for d in placed.values())
        assert {n.removeprefix(prefix + "placed_feature/").removesuffix(".json")
                for n, d in placed.items()
                if d["feature"] in {"biomesoplenty:" + c for c in candidates}} == {
            "anomaly", "monolith", "nether_bone_spine",
        }
        for name, chance in (("anomaly", 2), ("monolith", 4)):
            assert placed[prefix + "placed_feature/" + name + ".json"] == {
                "feature": "biomesoplenty:" + name,
                "placement": [
                    {"type": "minecraft:rarity_filter", "chance": chance},
                    {"type": "minecraft:in_square"},
                    {"type": "minecraft:heightmap", "heightmap": "MOTION_BLOCKING"},
                    {"type": "minecraft:biome"},
                ],
            }
        consumers: dict[str, set[str]] = {name: set() for name in candidates}
        for path, definition in data.items():
            if path.startswith(prefix + "biome/"):
                for stage in cast("list[list[str]]", definition["features"]):
                    for feature in stage:
                        if feature.removeprefix("biomesoplenty:") in consumers:
                            consumers[feature.removeprefix("biomesoplenty:")].add(
                                path.removeprefix(prefix + "biome/").removesuffix(".json"))
        assert consumers == {
            "anomaly": {"end_corruption"}, "monolith": {"end_corruption"},
            "nether_bone_spine": {"visceral_heap"}, "bone_spine": set(),
        }
        directory = Path("evidence/item-8/sources/bop-feature-scope")
        raw = (directory / "identities.json").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == (
            "784dbe3703e88c8720cacd937195f867735f3b13c892d755cb0aaff389f18296"
        )
        rows = cast("list[dict[str, str]]", json.loads(raw))
        assert len(rows) == 3
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
    runtime = Path("evidence/item-8/runtime/registry-r1/dumps/registry/minecraft")
    assert {"biomesoplenty:" + name for name in candidates} <= set(read_registry(
        runtime / "worldgen_configured_feature.txt"))
    assert {"biomesoplenty:" + name for name in candidates - {"bone_spine"}} <= set(read_registry(
        runtime / "worldgen_placed_feature.txt"))
    raw = Path("evidence/item-8/runtime/dimension-r3/dimension-biomes.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "08fa8185cd2c3f54b5255b2e8f86946c4b37ed471fb1991d0f82c835ffe20c7c"
    )
    dimensions = cast("dict[str, list[str]]", json.loads(raw))
    assert "biomesoplenty:end_corruption" in dimensions["minecraft:the_end"]
    assert "biomesoplenty:visceral_heap" in dimensions["minecraft:the_nether"]


def test_bop_plain_bone_spine_has_no_packaged_selector_reference() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("BiomesOPlenty-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        prefix = "data/biomesoplenty/worldgen/"
        data = {
            n: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
            for n in archive.namelist() if n.startswith("data/") and n.endswith(".json")
        }
        # Exact value search includes selectors and other packaged data, not only direct routes.
        references: set[str] = set()
        for path, definition in data.items():
            pending: list[JsonValue] = [definition]
            while pending:
                value = pending.pop()
                if isinstance(value, dict):
                    pending.extend(value.values())
                elif isinstance(value, list):
                    pending.extend(value)
                elif value == "biomesoplenty:bone_spine":
                    references.add(path)
        assert references == {
            prefix + "configured_feature/bone_spine.json",
            prefix + "configured_feature/nether_bone_spine.json",
        }
