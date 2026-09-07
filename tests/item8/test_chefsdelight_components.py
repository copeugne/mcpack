from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_resource_selection import select_resources
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_full_provider_archive_matches_inspected_code_and_components() -> None:
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "chefsdelight-1.0.5-neoforge-1.21.1.jar"
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    classes: set[str] = set()
    with ZipFile(source.path) as archive:
        for folder in ("chefsdelight-villages", "chefsdelight-provider-entries"):
            directory = Path("evidence/item-8/sources") / folder
            identities = cast(
                "list[dict[str, str]]", json.loads((directory / "identities.json").read_bytes())
            )
            for identity in identities:
                assert identity["archive_sha256"] == source.sha256
                assert (
                    hashlib.sha256(archive.read(identity["class"])).hexdigest()
                    == (identity["class_sha256"])
                )
                assert (
                    hashlib.sha256((directory / identity["disassembly"]).read_bytes()).hexdigest()
                    == (identity["disassembly_sha256"])
                )
                classes.add(identity["class"])
        names = archive.namelist()
        assert len(names) == len(set(names))
        assert {n for n in names if n.endswith(".class")} == classes
        assert len(classes) == 6
        templates = {
            f"data/chefsdelight/structure/{v}_{role}_house.nbt"
            for v in ("plains", "desert", "taiga", "savanna", "snowy")
            for role in ("chef", "cook")
        }
        metadata = {
            "META-INF/MANIFEST.MF",
            "META-INF/neoforge.mods.toml",
            "META-INF/accesstransformer.cfg",
            "icon.png",
            "logo.png",
        }
        other_data = {
            "data/chefsdelight/loot_table/chests/cooker.json",
            "data/minecraft/tags/point_of_interest_type/acquirable_job_site.json",
        }
        for name in names:
            if name.endswith("/") or name in classes | templates | metadata | other_data:
                continue
            assert name.startswith("assets/chefsdelight/")
            assert name.endswith((".png", ".json"))
        pool_class = "net.minecraft.world.level.levelgen.structure.pools.StructureTemplatePool"
        assert archive.read("META-INF/accesstransformer.cfg").decode().strip() == (
            f"public {pool_class} templates  # templates"
        )


def test_injected_house_content() -> None:
    raw = Path("evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705")
    catalog = cast("dict[str, list[JsonValue]]", json.loads(gzip.decompress(raw)))
    selected, _ = select_resources(catalog["resources"], "structure",
                                  enabled_packs=["vanilla", "mod_data"],
                                  lithostitched_overlay=True)
    for variant in ("plains", "desert", "taiga", "savanna", "snowy"):
        for role in ("cook", "chef"):
            key = f"chefsdelight:{variant}_{role}_house"
            row = selected[key]
            assert row["archive"] == "chefsdelight-1.0.5-neoforge-1.21.1.jar"
            doc = cast("dict[str, JsonValue]", row["document"])
            assert doc["entities"] == []
            nbts = [cast("dict[str, JsonValue]", block["nbt"]) for block in
                    cast("list[dict[str, JsonValue]]", doc["block_entities"])]
            assert {cast("str", nbt["LootTable"]) for nbt in nbts if "LootTable" in nbt} == {
                "chefsdelight:chests/cooker"}
            assert not any(nbt["id"] in ("minecraft:mob_spawner", "minecraft:spawner",
                                         "minecraft:trial_spawner") for nbt in nbts)
            pools = [nbt["pool"] for nbt in nbts if nbt["id"] == "minecraft:jigsaw"]
            expected = ["minecraft:empty"]
            if role == "cook" and variant in ("plains", "desert", "taiga"):
                expected = ["minecraft:village/plains/streets"]
            if role == "cook" and variant == "snowy":
                expected.append("minecraft:village/snowy/villagers")
            assert pools == expected
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd")
    catalog = cast("dict[str, list[JsonValue]]", json.loads(gzip.decompress(raw)))
    loot, _ = select_resources(catalog["resources"], "loot_table",
                              enabled_packs=["vanilla", "mod_data"],
                              lithostitched_overlay=True)
    assert "chefsdelight:chests/cooker" in loot
