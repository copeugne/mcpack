from __future__ import annotations

import hashlib
import json
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_regions_unexplored_complete_payload_and_json5_boundary() -> None:
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("regions-unexplored-")
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 8077
        assert Counter("classes" if n.endswith(".class") else n.split("/")[0] for n in names) == {
            "classes": 349,
            "assets": 4408,
            "data": 3267,
            ".cache": 14,
            "META-INF": 5,
            "overlay.painted_planks": 16,
            "overlay.birch_aspen_trees": 6,
            "overlay.oak_taller_trees": 4,
            "overlay.taiga_pine_trees": 2,
            "overlay.common_grass_sprouts": 1,
            "overlay.forest_fancy_oaks": 1,
            "pack.mcmeta": 1,
            "pack.png": 1,
            "regions_unexplored.mixins.json": 1,
            "regions_unexplored.neoforge.mixins.json": 1,
        }
        assert Counter(n.split("/")[2] for n in names if n.startswith("data/")) == {
            "loot_table": 798,
            "worldgen": 771,
            "advancement": 638,
            "recipe": 622,
            "tags": 335,
            "lithostitched": 90,
            "wolf_variant": 9,
            "damage_type": 2,
            "data_maps": 1,
            "structure": 1,
        }
        assert {n for n in names if n.startswith("META-INF/")} == {
            "META-INF/MANIFEST.MF",
            "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml",
            "META-INF/jarjar/metadata.json",
            "META-INF/jars/json5-java-3.0.0.jar",
        }
        raw = archive.read("META-INF/jars/json5-java-3.0.0.jar")
        assert hashlib.sha256(raw).hexdigest() == (
            "2e0f73784e6bc4c755e52d485f628d110d397f079d58b118658b903be9aa0533"
        )
        assert {
            n for n in names if n.endswith(".class") and b"de/marhali/json5/" in archive.read(n)
        } == {
            "net/regions_unexplored/config/RUConfigHandler.class",
            "net/regions_unexplored/config/json5/Json5Ops.class",
            "net/regions_unexplored/config/json5/Json5Ops$1.class",
            "net/regions_unexplored/config/json5/Json5Ops$ArrayBuilder.class",
            "net/regions_unexplored/config/json5/Json5Ops$Json5RecordBuilder.class",
        }
    with ZipFile(BytesIO(raw)) as library:
        names = [n for n in library.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 29
        classes = [n for n in names if n.endswith(".class")]
        assert len(classes) == 28
        assert set(names) - set(classes) == {"META-INF/MANIFEST.MF"}
        assert all(n.startswith("de/marhali/json5/") for n in classes)
        assert not any(
            marker in library.read(n)
            for n in classes
            for marker in (
                b"Lnet/neoforged/fml/common/Mod;",
                b"Lnet/neoforged/fml/common/EventBusSubscriber;",
                b"net/minecraft/",
                b"net/neoforged/",
            )
        )


def test_regions_unexplored_overlay_resource_roles() -> None:
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("regions-unexplored-")
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if n.startswith("overlay.") and not n.endswith("/")]
        assert len(names) == 30
        assert all(n.endswith(".json") for n in names)
        roles = {
            "painted_planks": (16, "minecraft:crafting_shaped"),
            "birch_aspen_trees": (6, "minecraft:tree"),
            "oak_taller_trees": (4, "minecraft:tree"),
            "taiga_pine_trees": (2, "minecraft:tree"),
            "common_grass_sprouts": (1, "minecraft:random_patch"),
            "forest_fancy_oaks": (1, "minecraft:random_selector"),
        }
        for name, (count, kind) in roles.items():
            prefix = "overlay." + name + "/"
            selected = [n for n in names if n.startswith(prefix)]
            assert len(selected) == count
            resource_prefix = (
                "data/regions_unexplored/recipe/"
                if name == "painted_planks"
                else "data/minecraft/worldgen/configured_feature/"
            )
            assert all(n.startswith(prefix + resource_prefix) for n in selected)
            assert {json.loads(archive.read(n))["type"] for n in selected} == {kind}
        pack = cast("dict[str, dict[str, object]]", json.loads(archive.read("pack.mcmeta")))
        entries = cast("list[dict[str, object]]", pack["neoforge:overlays"]["entries"])
        assert len(entries) == 6
        assert {e["directory"] for e in entries} == {"overlay." + n for n in roles}
        for entry in entries:
            name = str(entry["directory"]).removeprefix("overlay.")
            assert entry["neoforge:conditions"] == [
                {
                    "type": "regions_unexplored:config",
                    "key": name if name == "painted_planks" else "vanilla_changes/" + name,
                }
            ]
            assert entry["formats"] == [1, 999]


def test_regions_unexplored_registered_tree_component_sources() -> None:
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("regions-unexplored-")
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    captured: set[str] = set()
    with ZipFile(source.path) as archive:
        for label, digest in (
            (
                "regions-unexplored-tree-components",
                "c0e8750b46dd656807e33cc3906aa98fd736da650cc01cdd0754cc94ec63f243",
            ),
            (
                "regions-unexplored-log-decorator",
                "7656c29c7f0b77b5827cbb01b082d2509f800a7cac87e342ec47bc6785bdc77d",
            ),
            (
                "regions-unexplored-ground-decorator",
                "2b459bc6975a0ddffe6826ea332312ef7f78e0d31354d165d455f3d127f03544",
            ),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert (
                    hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                    == (row["disassembly_sha256"])
                )
                captured.add(row["class"])
        tree_classes = {
            n
            for n in archive.namelist()
            if n.endswith(".class")
            and n.startswith("net/regions_unexplored/worldgen/")
            and any(part in n for part in ("/trunkplacer/", "/foliageplacer/", "/treedecorator/"))
        }
        assert len(tree_classes) == 21
        assert tree_classes <= captured
        neoforge = cast(
            "dict[str, object]", json.loads(archive.read("regions_unexplored.neoforge.mixins.json"))
        )
        assert all(neoforge[k] == [] for k in ("mixins", "client", "server"))
        assert "plugin" not in neoforge
