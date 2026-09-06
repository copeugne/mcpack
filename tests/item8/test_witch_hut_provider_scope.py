from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_witch_hut_provider_payload_and_components() -> None:  # noqa: PLR0915
    # Keep the single frozen payload and its graph partition in one assertion path.
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("YungsBetterWitchHuts-")
    )
    assert source.sha256 == "888b1e6d1ada21982a75abfb4afb040c9bc2cc68777ec5fcd1199b978e3d4f8d"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    classes: set[str] = set()
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 54
        for folder, digest in (
            ("witch-hut-suppression",
             "b76bb19b6c7552b13b7b07b350826c84774a492932639636e87ed4bffa525c9a"),
            ("witch-hut-provider",
             "a5945737834c9c643fa966de790d0e63f40c1d4df9b301b4856ffb66e1c9e098"),
        ):
            directory = Path("evidence/item-8/sources") / folder
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            identities = cast("list[dict[str, str]]", json.loads(raw))
            for row in identities:
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class"] not in classes
                classes.add(row["class"])
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert (
                    hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                    == row["disassembly_sha256"]
                )
        assert len(classes) == 20
        assert classes == {n for n in names if n.endswith(".class")}
        services = "com.yungnickyoung.minecraft.betterwitchhuts.services."
        for interface, implementation in (
            ("IModulesLoader", "NeoForgeModulesLoader"),
            ("IPlatformHelper", "NeoForgePlatformHelper"),
        ):
            assert archive.read("META-INF/services/" + services + interface).decode().strip() == (
                services + implementation
            )
        for name in names:
            if name in classes | {
                "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "pack.mcmeta",
                "betterwitchhuts.mixins.json", "LICENSE_YungsBetterWitchHuts",
                "catalogue_background.png", "catalogue_icon.png", "icon.png", "logo.png",
                "META-INF/services/" + services + "IModulesLoader",
                "META-INF/services/" + services + "IPlatformHelper",
            }:
                continue
            if name.startswith("assets/betterwitchhuts/lang/"):
                assert name.endswith(".json"), name
                continue
            assert name.startswith((
                "data/betterwitchhuts/", "data/minecraft/tags/", "data/morevillagers/tags/",
            )), name
            assert name.endswith((".json", ".nbt")), name
            assert name.split("/")[2] in {"worldgen", "structure", "tags", "loot_table"}, name
            if name.split("/")[2] == "worldgen":
                assert name.split("/")[3] in {
                    "structure", "structure_set", "template_pool", "processor_list",
                }, name
            for kind, ids in groups.items():
                found = resource_identity(name, kind, ".nbt" if kind == "structure" else ".json")
                if found:
                    ids.add(found[0])
        processor_ids = (
            "leg_processor", "fence_leg_processor", "witch_circle_processor",
            "brewing_stand_processor", "potted_mushroom_processor",
        )
        assert json.loads(archive.read(
            "data/betterwitchhuts/worldgen/processor_list/main.json"
        )) == {
            "processors": [{"processor_type": "betterwitchhuts:" + p} for p in processor_ids]
        }
    assert groups["worldgen/structure"] == {
        "betterwitchhuts:witch_circle", "betterwitchhuts:witch_hut",
    }
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert groups["worldgen/structure"] == {
        r for r in registry if r.startswith("betterwitchhuts:")
    }
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    selected = [traces[r] for r in groups["worldgen/structure"]]
    assert groups["worldgen/template_pool"] == {
        "betterwitchhuts:starts", "betterwitchhuts:circles", "betterwitchhuts:mobs",
    }
    assert groups["worldgen/template_pool"] | {"minecraft:empty"} == {
        p for t in selected for p in cast("list[str]", t["pools"])
    }
    assert groups["structure"] == {
        "betterwitchhuts:" + n for n in (
            "witch", "cat", "witch_circle", "witch_hut_double", "witch_hut_lg", "witch_hut_sm",
        )
    }
    assert groups["structure"] == {
        n for t in selected for n in cast("list[str]", t["templates"])
    }
    assert all(t["missing"] == [] for t in selected)
    assert all(t["unresolved_elements"] == [] for t in selected)
