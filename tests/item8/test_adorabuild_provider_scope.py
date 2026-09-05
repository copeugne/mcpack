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


def test_adorabuild_full_payload_and_all_root_components() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("adorabuild-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/adorabuild-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "446d2811b3bd46642a1ae419f030e7d78b24fa061eb12c8e37f2702b086f038d"
    )
    identities = cast("list[dict[str, str]]", json.loads(raw))
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    types: Counter[str] = Counter()
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        classes = {row["class"] for row in identities}
        assert len(classes) == 7
        assert {n for n in names if n.endswith(".class")} == classes
        for identity in identities:
            assert identity["archive"] == source.name
            assert identity["archive_sha256"] == source.sha256
            assert (
                hashlib.sha256(archive.read(identity["class"])).hexdigest()
                == identity["class_sha256"]
            )
            assert (
                hashlib.sha256((directory / identity["disassembly"]).read_bytes()).hexdigest()
                == identity["disassembly_sha256"]
            )
        for name in names:
            if name.endswith("/") or name in classes | {
                "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "pack.mcmeta", "logo.png",
                "assets/adorabuild_structures/icon.png",
                "assets/adorabuild_structures/textures/adorabuild.png",
            }:
                continue
            if name.startswith("assets/adorabuild_structures/lang/"):
                assert name.endswith(".json"), name
                continue
            assert name.startswith("data/adorabuild_structures/"), name
            assert name.endswith((".json", ".nbt")), name
            kind = name.split("/")[2]
            assert kind in {"worldgen", "structure", "tags", "loot_table", "advancement"}, name
            if kind == "worldgen":
                category = name.split("/")[3]
                assert category in {
                    "structure", "structure_set", "template_pool", "processor_list",
                }, name
                if category == "structure":
                    data = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
                    types[cast("str", data["type"])] += 1
                if category == "processor_list":
                    data = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
                    assert all(
                        p["processor_type"] == "minecraft:rule"
                        for p in cast("list[dict[str, JsonValue]]", data["processors"])
                    )
            for category, identifiers in groups.items():
                found = resource_identity(
                    name, category, ".nbt" if category == "structure" else ".json"
                )
                if found:
                    identifiers.add(found[0])
    assert types == {
        "minecraft:jigsaw": 69,
        "adorabuild_structures:end_jigsaw_structure": 16,
        "adorabuild_structures:nether_jigsaw_structure": 14,
        "adorabuild_structures:overworld_jigsaw_structure": 7,
    }
    assert tuple(len(v) for v in groups.values()) == (106, 110, 121)
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    roots = groups["worldgen/structure"]
    assert roots <= traces.keys()
    assert groups["worldgen/template_pool"] <= {
        p for r in roots for p in cast("list[str]", traces[r]["pools"])
    }
    assert groups["structure"] <= {
        t for r in roots for t in cast("list[str]", traces[r]["templates"])
    }
    assert {r: traces[r]["missing"] for r in roots if traces[r]["missing"]} == {
        "adorabuild_structures:basalt_chambers_large_1": [
            {"id": "minecraft:basalt_chambers/chambers", "kind": "pool"},
        ],
    }
