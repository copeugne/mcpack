from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_ctov_bundled_packs_and_misnamed_modifiers_are_components() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "[Neoforge]ctov-3.6.3.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        prefix = "ctov-extended-mushrooms/"
        zipped = prefix + "ctov-extended-mushrooms-v1.zip"
        raw = archive.read(zipped)
        assert hashlib.sha256(raw).hexdigest() == (
            "4a79860229a4d678c4b5567d12456ae9078476c62052c7df6c474771d5823223"
        )
        processors = {
            f"data/ctov/worldgen/processor_list/village/mushroom/{name}.json"
            for name in ("house", "house_glow", "house_honey", "house_poison", "house_slime")
        }
        with ZipFile(io.BytesIO(raw)) as nested:
            files = {n for n in nested.namelist() if not n.endswith("/")}
            assert files == processors | {"pack.mcmeta"}
            for name in files:
                loose = "data/pack.mcmeta" if name == "pack.mcmeta" else name
                assert nested.read(name) == archive.read(prefix + loose)
            for name in processors:
                document = cast("dict[str, JsonValue]", json.loads(nested.read(name)))
                assert set(document) == {"processors"}
                assert {
                    p["processor_type"]
                    for p in cast("list[dict[str, str]]", document["processors"])
                } <= {"lithostitched:block_swap", "lithostitched:apply_random"}
        assert {n for n in archive.namelist() if n.startswith(prefix) and not n.endswith("/")} == {
            zipped, prefix + "data/pack.mcmeta", *(prefix + n for n in processors),
        }
        prefix = "ctov-savage-and-ravage-add-on/"
        expected = {
            prefix + f"data/ctov/structures/pillager_outpost/{v}/base_plate.nbt"
            for v in (
                "badlands", "beach", "dark_forest", "desert", "jungle", "mountain",
                "plains", "savanna", "snowy", "swamp", "taiga",
            )
        } | {prefix + "pack.mcmeta"}
        files = {n for n in archive.namelist() if n.startswith(prefix) and not n.endswith("/")}
        assert files == expected
        # These are structure-set references, not independent root definitions.
        registry = read_registry(Path(
            "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
        ))
        for filename, target, count in (
            ("pillager_outpost", "minecraft:pillager_outposts", 11),
            ("village", "minecraft:villages", 63),
        ):
            name = f"data/ctov/lithostitched/worldgen_modifier/ctov/{filename}.jso"
            document = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
            assert set(document) == {"type", "structure_sets", "entries"}
            assert document["type"] == "lithostitched:add_structure_set_entries"
            assert document["structure_sets"] == target
            entries = cast("list[dict[str, JsonValue]]", document["entries"])
            assert len(entries) == count
            assert len({str(e["structure"]) for e in entries}) == count
            assert all(e["structure"] in registry and e["weight"] == 1 for e in entries)
