from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_resource_selection import mod_conditions_match, runtime_mod_ids
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_ctov_payload_and_disconnected_components() -> None:  # noqa: PLR0915
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "[Neoforge]ctov-3.6.3.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/ctov-provider")
    identities = cast("list[dict[str, str]]", json.loads(
        (directory / "identities.json").read_bytes()
    ))
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        assert {n for n in names if n.endswith(".class")} == {r["class"] for r in identities}
        assert len(identities) == 12
        for row in identities:
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
        files = [n for n in names if not n.endswith(("/", ".class"))]
        # Bundled payload contents and entry disassemblies have separate focused checks.
        counts = Counter(
            "/".join(n.split("/")[:4]) if n.startswith("data/") and "/worldgen/" in n
            else "/".join(n.split("/")[:3]) if n.startswith(("assets/", "data/"))
            else n.split("/")[0] for n in files
        )
        assert counts == {
            "META-INF": 2, "assets/ctov/lang": 7, "assets/ctov/pack.png": 1,
            "ctov-common.mixins.json": 1, "ctov.mixins.json": 1, "ctov.accesswidener": 1,
            "ctov-extended-mushrooms": 7, "ctov-savage-and-ravage-add-on": 12,
            "data/ctov/lithostitched": 1021, "data/ctov/loot_table": 12,
            "data/ctov/structure": 2093, "data/ctov/structure_icons.json": 1,
            "data/ctov/tags/worldgen": 28, "data/ctov/worldgen/placed_feature": 1,
            "data/ctov/worldgen/processor_list": 281, "data/ctov/worldgen/structure": 78,
            "data/ctov/worldgen/structure_set": 1, "data/ctov/worldgen/template_pool": 174,
            "data/minecraft/tags/worldgen": 1, "data/monobank/loot_tables": 7,
            "data/monobank/structures": 14, "data/monobank/worldgen/template_pool": 7,
            "data/wares/loot_tables": 35, "pack.mcmeta": 1,
        }
        for name in files:
            for kind, identifiers in groups.items():
                found = resource_identity(name, kind, ".nbt" if kind == "structure" else ".json")
                if found and not found[1]:
                    identifiers.add(found[0])
        flower = cast("dict[str, JsonValue]", json.loads(archive.read(
            "data/ctov/worldgen/placed_feature/village_flowers.json"
        )))
        assert flower["feature"] == "minecraft:flower_flower_forest"
        underground = cast("dict[str, JsonValue]", json.loads(archive.read(
            "data/ctov/worldgen/structure_set/underground_village.txt"
        )))
        entries = cast("list[dict[str, str]]", underground["structures"])
        assert {e["structure"] for e in entries} == {
            f"ctov:{size}/village_underground" for size in ("small", "medium", "large")
        }
    assert tuple(len(v) for v in groups.values()) == (78, 181, 2093)
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    roots = groups["worldgen/structure"]
    assert roots <= traces.keys()
    assert sum(bool(traces[r]["missing"]) for r in roots) == 27
    assert not any(traces[r]["unresolved_elements"] for r in roots)
    pools = {p for r in roots for p in cast("list[str]", traces[r]["pools"])}
    assert groups["worldgen/template_pool"] - pools == {
        *(f"ctov:village/common/{p}" for p in (
            "bees", "flowers", "pet", "pet_aquatic", "villager/desert", "villager/plain",
            "villager/savanna", "villager/snow", "villager/taiga",
            "waystone/mossy", "waystone/sand",
        )), "ctov:village/mesa_fortified/tree",
        *(f"monobank:village/monobank/{v}" for v in (
            "badlands", "beach", "dark_forest", "jungle", "mountain", "mushroom", "swamp",
        )),
    }
    outside = groups["structure"] - {
        t for r in roots for t in cast("list[str]", traces[r]["templates"])
    }
    assert len(outside) == 1133
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    mods = set(runtime_mod_ids(Path("evidence/raw/item8/registry-r1/debug.log").read_text()))
    references: dict[bool, set[str]] = {True: set(), False: set()}
    for resource in cast("list[dict[str, JsonValue]]", catalog["resources"]):
        if resource["archive"] != source.name or "/lithostitched/worldgen_modifier/" not in str(
            resource["path"]
        ):
            continue
        data = cast("dict[str, JsonValue]", resource["document"])
        active = mod_conditions_match(data.get("neoforge:conditions", []), mods)
        for entry in cast("list[dict[str, JsonValue]]", data["elements"]):
            element = cast("dict[str, JsonValue]", entry["element"])
            # Reference accounting only. No simulation of these placement constraints.
            while element["element_type"] in {"lithostitched:limited", "lithostitched:guaranteed"}:
                element = cast("dict[str, JsonValue]", element["delegate"])
            assert element["element_type"] == "minecraft:single_pool_element"
            references[active].add(str(element["location"]))
    assert not outside & references[True]
    assert len(outside & references[False]) == 1005
    residual = outside - references[False]
    assert len(residual) == 128
    assert Counter(
        p.split("/")[2] if p.startswith("ctov:village/") else p.split("/")[-1]
        for p in residual
    ) == {
        "animals": 44, "jobsite": 56, "deco": 3, "allay_cage": 8, "tree": 5,
        "target": 1, "roads": 7, "house": 3, "bees": 1,
    }
