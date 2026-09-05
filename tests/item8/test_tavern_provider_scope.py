from __future__ import annotations

import hashlib
import json
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_tavern_parent_and_nested_provider_scope() -> None:
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "village_taverns-neoforge-1.1.5+1.21.1.jar"
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    nested_name = "META-INF/jars/tiny-config-3.1.0-neoforge.jar"
    with ZipFile(source.path) as parent:
        nested_raw = parent.read(nested_name)
        nested_sha = hashlib.sha256(nested_raw).hexdigest()
        assert nested_sha == "1587ed9848881e7b677da5b8c85e0f35719315eb5f6571592d31840cf1421f63"
        classes: set[str] = set()
        with ZipFile(BytesIO(nested_raw)) as nested:
            for folder in (
                "tavern-provider-entries",
                "tavern-registration-scope",
                "tavern-remaining-entries",
                "tiny-config-entry",
            ):
                directory = Path("evidence/item-8/sources") / folder
                identities = cast(
                    "list[dict[str, str]]", json.loads((directory / "identities.json").read_bytes())
                )
                archive = nested if folder == "tiny-config-entry" else parent
                for identity in identities:
                    assert identity["archive_sha256"] == (
                        nested_sha if archive is nested else source.sha256
                    )
                    assert (
                        hashlib.sha256(archive.read(identity["class"])).hexdigest()
                        == (identity["class_sha256"])
                    )
                    raw = (directory / identity["disassembly"]).read_bytes()
                    assert hashlib.sha256(raw).hexdigest() == identity["disassembly_sha256"]
                    if archive is parent:
                        classes.add(identity["class"])
            metadata = {
                "META-INF/MANIFEST.MF",
                "META-INF/neoforge.mods.toml",
                "logo.png",
                "META-INF/architectury-loom-nesting-metadata.json",
                "tiny_config.mixins.json",
            }
            entries: set[str] = set()
            for name in nested.namelist():
                if name.endswith("/") or name in metadata:
                    continue
                assert name.endswith(".class"), name
                raw = nested.read(name)
                if b"Lnet/neoforged/fml/common/Mod;" in raw:
                    entries.add(name)
                assert b"Lnet/neoforged/fml/common/EventBusSubscriber;" not in raw
            assert entries == {"net/tiny_config/neoforge/ExampleModNeoForge.class"}
            mixins = cast(
                "dict[str, JsonValue]", json.loads(nested.read("tiny_config.mixins.json"))
            )
            assert mixins["mixins"] == []
            assert mixins["client"] == []
        assert len(classes) == 15
        names = parent.namelist()
        assert len(names) == len(set(names))
        assert {n for n in names if n.endswith(".class")} == classes
        variants = ("desert", "plains", "savanna", "snowy", "taiga")
        templates = {f"data/village_taverns/structure/village/{v}/tavern.nbt" for v in variants}
        additions = {
            f"data/village_taverns/lithostitched/worldgen_modifier/village/{v}.json"
            for v in variants
        }
        metadata = {
            "META-INF/MANIFEST.MF",
            "META-INF/neoforge.mods.toml",
            nested_name,
            "META-INF/jarjar/metadata.json",
            "icon.png",
            "village_taverns.mixins.json",
            "village_taverns-common-common-refmap.json",
        }
        other_data = {
            "data/minecraft/tags/point_of_interest_type/acquirable_job_site.json",
            "data/village_taverns/loot_table/blocks/barrel.json",
            "data/village_taverns/loot_table/chests/tavern.json",
            "data/village_taverns/recipe/rune_crafting_altar.json",
        }
        for name in names:
            if (
                name.endswith("/")
                or name in classes | templates | additions | metadata | other_data
            ):
                continue
            assert name.startswith("assets/village_taverns/")
            assert name.endswith((".png", ".json", ".png.mcmeta"))
        for variant in variants:
            path = f"data/village_taverns/lithostitched/worldgen_modifier/village/{variant}.json"
            doc = cast("dict[str, JsonValue]", json.loads(parent.read(path)))
            assert doc["type"] == "lithostitched:add_template_pool_elements"
            assert doc["template_pools"] == [f"minecraft:village/{variant}/houses"]
            assert doc["elements"] == [
                {
                    "weight": 5,
                    "element": {
                        "element_type": "lithostitched:limited",
                        "limit": 1,
                        "delegate": {
                            "element_type": "minecraft:single_pool_element",
                            "projection": "rigid",
                            "processors": "minecraft:empty",
                            "location": f"village_taverns:village/{variant}/tavern",
                        },
                    },
                }
            ]
