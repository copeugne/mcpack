from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources


def test_regions_unexplored_packaged_component_boundary() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "regions-unexplored-0.6.1-neoforge-21.1.jar")
    assert source.sha256 == "8eac74e63ba6bc9c3aea459adcdeba58d7918d296d0775c6f51777fe2ee1967a"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert not any(n.startswith("regions_unexplored:") for n in registry)
    with ZipFile(source.path) as archive:
        names = {n for n in archive.namelist() if not n.endswith("/")}
        assert len(names) == 8077
        prefix = "data/regions_unexplored/worldgen/"
        assert Counter(n.removeprefix(prefix).split("/")[0]
                       for n in names if n.startswith(prefix)) == {
            "configured_feature": 386, "placed_feature": 287, "biome": 78,
            "processor_list": 10, "noise": 5, "density_function": 1, "template_pool": 1,
        }
        assert {n for n in names if n.endswith(".nbt")} == {
            "data/regions_unexplored/structure/trial_chambers/ashen.nbt",
        }
        assert not any("/worldgen/structure/" in n or "/worldgen/structure_set/" in n
                       for n in names)
        assert json.loads(archive.read(prefix + "template_pool/trial_chambers/ashen.json")) == {
            "elements": [{"element": {
                "element_type": "minecraft:single_pool_element",
                "location": "regions_unexplored:trial_chambers/ashen",
                "processors": {"processors": []}, "projection": "rigid",
            }, "weight": 1}], "fallback": "minecraft:empty",
        }
        assert json.loads(archive.read(
            "data/lithostitched/tags/worldgen/template_pool/trial_spawner/melee.json"
        )) == {"values": ["regions_unexplored:trial_chambers/ashen"]}
        base = Path("evidence/item-8/sources/regions-unexplored-provider")
        raw = (base / "identities.json").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == (
            "cb7185024530c1b77bbf71dbf9ccefb2ba1acf505688896a1803f0a4240a4894"
        )
        captured: set[str] = set()
        for row in cast("list[dict[str, str]]", json.loads(raw)):
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((base / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
            captured.add(row["class"])
        entries = {n for n in names if n.endswith(".class") and any(
            marker in archive.read(n) for marker in (
                b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
            )
        )}
        assert len(entries) == 3
        assert entries <= captured
        mixins = cast("dict[str, object]", json.loads(
            archive.read("regions_unexplored.mixins.json")
        ))
        common = {"net/regions_unexplored/mixin/" + n.replace(".", "/") + ".class"
                  for n in cast("list[str]", mixins["mixins"])}
        assert len(common) == 9
        assert common <= captured
