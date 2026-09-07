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


def test_ocean_monument_provider_payload_and_components() -> None:  # noqa: PLR0915
    # Keep the single frozen payload and its graph partition in one assertion path.
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("YungsBetterOceanMonuments-")
    )
    assert source.sha256 == "cdcf8fe0e08c75261048d43c6ed4898972d23e096dd04a2524c136f06416ab02"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    classes: set[str] = set()
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 122
        for folder, digest in (
            ("monument-suppression",
             "ac148bb2b65821f70b7402c9681844a378bcc3918f57d6076d670af78a53b53d"),
            ("ocean-monument-provider",
             "8eea5e78334604ab4ff0f9e02bdf127030a4a5bc07a418bc9461ff835c03bab2"),
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
        assert len(classes) == 28
        assert classes == {n for n in names if n.endswith(".class")}
        services = "com.yungnickyoung.minecraft.betteroceanmonuments.services."
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
                "betteroceanmonuments.mixins.json", "LICENSE_YungsBetterOceanMonuments",
                "catalogue_background.png", "catalogue_icon.png", "icon.png", "logo.png",
                "META-INF/services/" + services + "IModulesLoader",
                "META-INF/services/" + services + "IPlatformHelper",
            }:
                continue
            if name.startswith("assets/betteroceanmonuments/lang/"):
                assert name.endswith(".json"), name
                continue
            assert name.startswith((
                "data/betteroceanmonuments/", "data/minecraft/tags/",
                "data/yungsapi/tags/",
            )), name
            assert name.endswith((".json", ".nbt")), name
            assert name.split("/")[2] in {
                "worldgen", "structure", "tags", "loot_table",
            }, name
            if name.split("/")[2] == "worldgen":
                assert name.split("/")[3] in {
                    "structure", "structure_set", "template_pool", "processor_list",
                }, name
            for kind, ids in groups.items():
                found = resource_identity(name, kind, ".nbt" if kind == "structure" else ".json")
                if found:
                    ids.add(found[0])
        processor_data = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(archive.read(
            "data/betteroceanmonuments/worldgen/processor_list/main.json"
        )))
        assert {cast("str", p["processor_type"]) for p in processor_data["processors"]} == {
            "betteroceanmonuments:" + n for n in (
                "random_prismarine_slab_decoration_processor",
                "random_dark_prismarine_slab_decoration_processor", "sand_gravel_processor",
                "random_oxidization_processor", "structure_void_processor", "air_processor",
                "waterlog_processor", "seagrass_processor", "random_sponge_processor",
                "leg_processor",
            )
        }
        assert json.loads(archive.read(
            "data/betteroceanmonuments/tags/worldgen/structure/better_ocean_monuments.json"
        )) == {"replace": False, "values": ["betteroceanmonuments:ocean_monument"]}
    assert groups["worldgen/structure"] == {"betteroceanmonuments:ocean_monument"}
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert groups["worldgen/structure"] == {
        r for r in registry if r.startswith("betteroceanmonuments:")
    }
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    trace = traces["betteroceanmonuments:ocean_monument"]
    assert len(groups["worldgen/template_pool"]) == 13
    assert groups["worldgen/template_pool"] | {"minecraft:empty"} == set(
        cast("list[str]", trace["pools"])
    )
    assert len(groups["structure"]) == 59
    assert groups["structure"] - set(cast("list[str]", trace["templates"])) == {
        "betteroceanmonuments:kelp/seagrass", "betteroceanmonuments:kelp/seagrass_tall",
    }
    assert trace["missing"] == []
    assert trace["unresolved_elements"] == []
