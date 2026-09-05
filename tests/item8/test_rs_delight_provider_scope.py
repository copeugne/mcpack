from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_rs_delight_all_resources_are_existing_village_components() -> None:
    name = "repurposed_structures_farmers_delight_compat_v7.jar"
    source = next(s for s in retained_sources(Path.cwd()) if s.name == name)
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    variants = {"badlands", "bamboo", "birch", "cherry", "dark_forest", "giant_taiga",
                "jungle", "mountains", "mushroom", "oak", "ocean", "swamp"}
    root = "data/farmersdelight/"
    additions = {f"{root}rs_pool_additions/villages/{v}/houses.json" for v in variants}
    limits = {f"{root}rs_pieces_spawn_counts/village_{v}.json" for v in variants}
    templates = {f"farmersdelight:villages/{v}/houses/compost_pile_1" for v in variants}
    templates.add("farmersdelight:villages/mushroom/houses/mushroom_farm")
    processor_root = "data/repurposed_structures/worldgen/processor_list/villages"
    processors = {f"{processor_root}/{v}/crop_randomizer.json"
                  for v in variants - {"mushroom", "ocean"}}
    processors.add(f"{processor_root}/mushroom/mushroom_randomizer.json")
    template_paths = {"data/" + t.replace(":", "/structure/") + ".nbt" for t in templates}
    metadata = {"META-INF/neoforge.mods.toml", "fabric.mod.json", "pack.mcmeta"}
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        assert {n for n in names if not n.endswith("/")} == (
            metadata | additions | limits | processors | template_paths)
        descriptor = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert descriptor["modLoader"] == "lowcodefml"
        referenced: set[str] = set()
        limited: set[str] = set()
        for variant in sorted(variants):
            addition = cast("dict[str, JsonValue]", json.loads(archive.read(
                f"{root}rs_pool_additions/villages/{variant}/houses.json")))
            assert addition["target_pool"] == f"repurposed_structures:villages/{variant}/houses"
            for entry in cast("list[dict[str, JsonValue]]", addition["elements"]):
                element = cast("dict[str, JsonValue]", entry["element"])
                referenced.add(cast("str", element["location"]))
            limit = cast("dict[str, JsonValue]", json.loads(archive.read(
                f"{root}rs_pieces_spawn_counts/village_{variant}.json")))
            assert limit["target_structure"] == f"repurposed_structures:village_{variant}"
            for piece in cast("list[dict[str, JsonValue]]", limit["pieces_spawn_counts"]):
                limited.add(cast("str", piece["nbt_piece_name"]))
        assert referenced == templates
        assert limited == templates
        for path in processors:
            document = cast("dict[str, JsonValue]", json.loads(archive.read(path)))
            assert {cast("str", p["processor_type"]) for p in
                    cast("list[dict[str, JsonValue]]", document["processors"])} == {
                        "minecraft:rule"}
    registry_dir = Path("evidence/item-8/runtime/registry-r1/dumps/registry/minecraft")
    registry = (registry_dir / "worldgen_structure.txt").read_bytes()
    assert hashlib.sha256(registry).hexdigest() == (
        "9d245430730173e9ce5304317a7476e7ecd4267d208b25a16a0d7b2cf3f16941")
    for variant in variants:
        assert f"repurposed_structures:village_{variant}" in registry.decode().splitlines()
