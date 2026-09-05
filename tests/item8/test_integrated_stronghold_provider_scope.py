from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_integrated_stronghold_full_payload_and_component_dispositions() -> None:
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("integrated_stronghold-")
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/integrated-stronghold-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "0044580a6b6f71c9b32c8d385d539779c7b0b2ad22d4c21bf1a5bfbbf2785d5b"
    )
    identities = cast("list[dict[str, str]]", json.loads(raw))
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        classes = {row["class"] for row in identities}
        assert len(classes) == 9
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
                "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "pack.mcmeta",
                "integrated_stronghold-common.mixins.json",
                "integrated_stronghold-common-refmap.json",
            }:
                continue
            if name.startswith("assets/integrated_stronghold/"):
                assert name.endswith((".png", ".json", ".ogg")), name
                continue
            assert name.startswith((
                "data/integrated_stronghold/", "data/minecraft/tags/",
                "data/minecraft/advancement/", "data/integrated_api/tags/",
            )), name
            assert name.endswith((".json", ".nbt")), name
            kind = name.split("/")[2]
            assert kind in {
                "worldgen", "structure", "tags", "loot_table", "jukebox_song",
                "recipe", "advancement", "integrated_structure_spawners",
            }, name
            if kind == "worldgen":
                assert name.split("/")[3] in {
                    "structure", "structure_set", "template_pool", "processor_list",
                }, name
            for category, identifiers in groups.items():
                found = resource_identity(
                    name, category, ".nbt" if category == "structure" else ".json"
                )
                if found:
                    identifiers.add(found[0])
        eye_tag = cast("dict[str, JsonValue]", json.loads(archive.read(
            "data/minecraft/tags/worldgen/structure/eye_of_ender_located.json"
        )))
        assert eye_tag == {"replace": True, "values": ["integrated_stronghold:stronghold"]}
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    trace = traces["integrated_stronghold:stronghold"]
    assert groups["worldgen/structure"] == {"integrated_stronghold:stronghold"}
    assert len(groups["worldgen/template_pool"]) == 44
    assert groups["worldgen/template_pool"] | {"minecraft:empty"} == set(
        cast("list[str]", trace["pools"])
    )
    assert len(groups["structure"]) == 61
    assert groups["structure"] - set(cast("list[str]", trace["templates"])) == {
        "integrated_stronghold:portal_room/portal_room_endrem",
        "integrated_stronghold:small_room/armory_left",
        "integrated_stronghold:small_room/armory_right",
    }
    assert trace["missing"] == [
        {"id": "integrated_stronghold:small_room/small_armory_left", "kind": "template"},
        {"id": "integrated_stronghold:small_room/small_armory_right", "kind": "template"},
    ]
