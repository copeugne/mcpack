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


def test_creating_space_packaged_component_partition() -> None:
    # Complements the existing root decisions with all packaged component membership.
    # Does not assert closure of executable generation or disconnected-template consumers.
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("creatingspace-"))
    assert source.sha256 == "a02eb4c17201f2add8343ebe7b4476890ae9b59a7f5af7e0309f6e00b9c65866"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    features: dict[str, str] = {}
    carvers: dict[str, str] = {}
    biome_carvers: dict[str, JsonValue] = {}
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 1645
        for name in names:
            for category, identifiers in groups.items():
                found = resource_identity(
                    name, category, ".nbt" if category == "structure" else ".json"
                )
                if found:
                    identifiers.add(found[0])
            found = resource_identity(name, "worldgen/configured_feature")
            if found:
                data = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
                features[found[0]] = cast("str", data["type"])
            found = resource_identity(name, "worldgen/configured_carver")
            if found:
                data = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
                carvers[found[0]] = cast("str", data["type"])
            found = resource_identity(name, "worldgen/biome")
            if found:
                data = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
                biome_carvers[found[0]] = data["carvers"]
    roots = groups["worldgen/structure"]
    assert roots == {
        "creatingspace:mars/underground_outpost_1", "creatingspace:moon/abandoned_outpost",
        "creatingspace:moon/crashed_rocket", "creatingspace:moon/crashed_ship",
    }
    assert tuple(len(v) for v in groups.values()) == (4, 5, 6)
    assert features == {
        "creatingspace:mars/nickel_sulfate_geode": "minecraft:geode",
        "creatingspace:moon/aluminum_ore": "minecraft:ore",
        "creatingspace:moon/cobalt_ore": "minecraft:ore",
        "creatingspace:moon/nickel_ore": "minecraft:ore",
        "creatingspace:nickel_overworld_replacement": "minecraft:ore",
    }
    assert carvers == {
        "creatingspace:mars_cave": "minecraft:cave",
        "creatingspace:moon_cave": "minecraft:cave",
        "creatingspace:moon_crater": "creatingspace:crater",
    }
    assert biome_carvers == {
        "creatingspace:mars_cave": {"air": "creatingspace:mars_cave"},
        "creatingspace:mars_plains": {"air": "creatingspace:mars_cave"},
        "creatingspace:moon_cave": {"air": ["creatingspace:moon_crater"]},
        "creatingspace:moon_plains": {"air": ["creatingspace:moon_crater"]},
        "creatingspace:space": {},
        "creatingspace:venus": {"air": ["minecraft:canyon"]},
        "creatingspace:venus_hellground": {"air": ["minecraft:canyon"]},
    }
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    reached_pools = {p for r in roots for p in cast("list[str]", traces[r]["pools"])}
    reached_templates = {t for r in roots for t in cast("list[str]", traces[r]["templates"])}
    assert groups["worldgen/template_pool"] <= reached_pools
    assert groups["structure"] - reached_templates == {"creatingspace:moon/abandoned_outpost"}
    assert reached_templates - groups["structure"] == {
        "minecraft:bastion/bridge/legs/leg_0", "minecraft:bastion/bridge/legs/leg_1",
    }
    assert reached_pools - groups["worldgen/template_pool"] == {
        "minecraft:bastion/bridge/legs", "minecraft:empty",
    }
    for root in roots:
        assert traces[root]["missing"] == []
        assert traces[root]["unresolved_elements"] == []


def test_creating_space_entry_source_coverage() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("creatingspace-"))
    directory = Path("evidence/item-8/sources/creating-space-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "eba1da2e07326fc6b3f57060d05bc7130695911a5fc118be589e2e09a1a515c4"
    )
    identities = cast("list[dict[str, str]]", json.loads(raw))
    captured = {row["class"] for row in identities}
    assert len(captured) == len(identities) == 39
    arrival_directory = Path("evidence/item-8/sources/creating-space-arrival")
    raw = (arrival_directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "04e25ddcbb7b1105bcf0d27eb83c605dda16a97ec4d683d829f94d74e97da0e1"
    )
    arrival = cast("list[dict[str, str]]", json.loads(raw))
    assert [row["class"] for row in arrival] == [
        "com/rae/creatingspace/content/rocket/CustomTeleporter.class",
    ]
    delegate_directory = Path("evidence/item-8/sources/creating-space-common-delegates")
    raw = (delegate_directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "452f56f08a577286fe894d2e692aa26b73e67dda6027274c318fcb30c7c7145e"
    )
    delegates = cast("list[dict[str, str]]", json.loads(raw))
    assert len(delegates) == 4
    with ZipFile(source.path) as archive:
        annotated = {
            n for n in archive.namelist() if n.endswith(".class") and any(
                annotation in archive.read(n) for annotation in (
                    b"Lnet/neoforged/fml/common/Mod;",
                    b"Lnet/neoforged/fml/common/EventBusSubscriber;",
                )
            )
        }
        mixin = cast("dict[str, JsonValue]", json.loads(archive.read("creatingspace.mixins.json")))
        declared = {
            (str(mixin["package"]) + "." + name).replace(".", "/") + ".class"
            for key in ("mixins", "client", "server")
            for name in cast("list[str]", mixin.get(key, []))
        }
        declared.add(str(mixin["plugin"]).replace(".", "/") + ".class")
        assert len(annotated) == 13
        assert len(declared) == 20
        for capture_directory, rows in (
            (directory, identities), (arrival_directory, arrival), (delegate_directory, delegates),
        ):
            for row in rows:
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                disassembly = (capture_directory / row["disassembly"]).read_bytes()
                assert hashlib.sha256(disassembly).hexdigest() == row["disassembly_sha256"]
    raw = Path("evidence/item-8/sources/generation-code-references.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "95b9991457704f4cf710b09456a82db78c2dcdd79544212c77d8f31d64c8883f"
    )
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    referenced = {
        str(row["path"]) for row in cast("list[dict[str, JsonValue]]", catalog["resources"])
        if row["archive"] == source.name
    }
    assert len(referenced) == 6
    assert captured == annotated | declared | referenced


def test_creating_space_remaining_payload_partition() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("creatingspace-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in names if n.endswith(".class")}
        assert len(classes) == 342
        assert all(n.startswith("com/rae/creatingspace/") for n in classes)
        assert not any(b"abandoned_outpost" in archive.read(n) for n in classes)
        assets = {n for n in names if n.startswith("assets/")}
        data = {n for n in names if n.startswith("data/")}
        caches = {n for n in names if n.startswith(".cache/")}
        assert len(caches) == 10
        assert names - classes - assets - data - caches == {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml",
            "creatingspace.mixins.json", "logo.png", "pack.mcmeta",
        }
        assert Counter(n.split("/")[2] for n in assets) == {
            "blockstates": 51, "lang": 7, "models": 284, "particles": 1, "ponder": 5,
            "sounds": 1, "sounds.json": 1, "textures": 325, "atlases": 1,
        }
        assert all(n.endswith((".json", ".png", ".ogg", ".nbt", ".mcmeta")) for n in assets)
        assert {n for n in assets if n.endswith(".nbt")} == {
            "assets/creatingspace/ponder/catalyst_carrier/chemical.nbt",
            "assets/creatingspace/ponder/chemical_synthesizer/chemical_synthesizer.nbt",
            "assets/creatingspace/ponder/mechanical_electrolyzer/electrolysis.nbt",
            "assets/creatingspace/ponder/rocket/rocket_building.nbt",
            "assets/creatingspace/ponder/rocket_generator/setup.nbt",
        }
        assert Counter(n.split("/")[2] for n in data) == {
            "tags": 108, "advancement": 104, "advancements": 2, "creatingspace": 19,
            "creatingspace_utilities": 1, "damage_type": 1, "dimension": 6,
            "dimension_type": 6, "loot_table": 52, "neoforge": 2, "recipe": 249,
            "structure": 6, "worldgen": 55, "data_maps": 1,
        }
        assert all(n.endswith(".nbt" if n.split("/")[2] == "structure" else ".json") for n in data)
