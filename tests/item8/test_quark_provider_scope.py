from __future__ import annotations

import hashlib
import json
import tomllib
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue

SOURCES = (
    ("quark-biolith-provider",
     "c8990b7cdc842caf2f85e84e28ecdb16d1b72dfc6ab51f43150d14c761c49d0f"),
    ("quark-end-generators",
     "b780ea6da20e3207872d0aee601a859382b6f3fc30db7b9a0f0383b2c1e4480a"),
    ("quark-end-registration",
     "ccc7e76f93036a8ec46d3add67ac29116e24205d72c14d461a511d9ee02c9581"),
    ("quark-fallen-log-decor",
     "a8f031439bb9ef6b14cb9f117fb56390717332c907a7cce4f9e9cbe8a67254b3"),
    ("quark-landmark-encounter-generators",
     "9e85bdd251270a20b8922c12a2b3567a9ffa18920426b94b1fec4bd1e9965971"),
    ("quark-monster-box-behavior",
     "9ce1a6e746759357630f45fcd135c126df48f38f4951d5fa0932144b3788e79b"),
    ("quark-monster-box-bindings",
     "e8b2cf605a2c485da43a062cf0a37128491fb085d92d46f54a3c694eff4a28ae"),
    ("quark-nether-spikes",
     "5c80fe8dba773400a3cd3fd42309d5b374499a9f7ff5c12e22c51c8c87a3ce4f"),
    ("quark-provider-entries",
     "46024fc051bacf39814edca480d0bf72a26ad8f1f7839b50536d13bd93910a0d"),
    ("quark-spawner-replacement",
     "f98c7135cebbc6868cc86ddb249f99cfff8eca8a3bbb7d802c5c8ff61434bb7e"),
    ("quark-spire-config-annotations",
     "44640d8c6411c058fa06ad6ed8e4633a58424b4987e464a43b18fd9dc6eb7449"),
    ("quark-stone-clusters",
     "10a0d8183bb99276dde2a57cd1cdbe2dc680da5ee4666fb44e48c880740d4acb"),
    ("quark-underground-base",
     "4c91291f1917aca25e977b0bc5b98f2d13d59a55d2f8e6ab0cc7221f1549800e"),
    ("quark-underground-context",
     "8b6f0f3e19d441cb110c27e52594be6dca879f8fc7f7573a3f5c2558a24da0e8"),
    ("quark-underground-fill",
     "f73c06f31d3b43e56c89b47eef22797689b18e96935d573c4bd45ab31ed22e43"),
    ("quark-underground-styles",
     "65b30aa6da55b5b00cb91a375f674b1bd0bba4b4b35cddb0810bfdd48d885d1f"),
    ("quark-vegetation",
     "c4de657bb4ec684bbb94f4433bac81022b3d2d8f2cb1311fb98c2ded8cb5c57a"),
    ("quark-world-category",
     "5157d8b0b79f4da07faa2bcc284869e8d58c673bd9c2a1a0d0993d575f546f62"),
)


def test_quark_sources_and_payload() -> None:  # noqa: PLR0915
    # One frozen provider with its actual bundled library and existing source captures.
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "Quark-4.1-480.jar")
    assert source.sha256 == "989c465df2e4cb9f602840c2eec143358bf11462cc19dc0b0c7c9f17449e75a5"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 9367
        assert Counter(n.split("/")[0] for n in names) == {
            "META-INF": 7, "org": 903, "aurelienribon": 64, "assets": 4479,
            "resourcepacks": 285, "datapacks": 44, "data": 3580, "proxypack.png": 1,
            "quark.mixins.json": 1, "quark_integrations.mixins.json": 1,
            "pack.mcmeta": 1, "proxypack.mcmeta": 1,
        }
        assert all(n.endswith(".class") for n in names
                   if n.startswith(("org/", "aurelienribon/")))
        assert not [n for n in names if n.endswith((".nbt", ".mcfunction"))]
        data_types = Counter("/".join(n.split("/")[:3]) for n in names if n.startswith("data/"))
        assert data_types == {
            "data/quark/tags": 96, "data/quark/loot_table": 788, "data/quark/worldgen": 15,
            "data/quark/recipe": 1503, "data/quark/damage_type": 1,
            "data/quark/advancement": 988, "data/quark/loot_modifiers": 18,
            "data/quark/readme.md": 1, "data/quark/jukebox_song": 9,
            "data/minecraft/tags": 88, "data/neoforge/loot_modifiers": 1, "data/c/tags": 72,
        }
        assert all("/assets/" in n or n.endswith(("/pack.mcmeta", "/pack.png"))
                   for n in names if n.startswith("resourcepacks/"))
        optional_worldgen = {n for n in names if n.startswith("datapacks/")
                             and "/worldgen/" in n}
        optional_root = "datapacks/quark_vdo_vanilla_stone_clusters/data/minecraft/worldgen/"
        assert optional_worldgen == {
            optional_root + "configured_feature/ore_" + stone + ".json"
            for stone in ("granite", "andesite", "diorite")
        }
        assert all("/tags/" in n or n in optional_worldgen or n.endswith("/pack.mcmeta")
                   for n in names if n.startswith("datapacks/"))
        nested_path = "META-INF/jarjar/biolith-neoforge-3.0.10.jar"
        raw = archive.read(nested_path)
        nested_sha = "7f5c86757c61f56c7dccf602b44a2c17ba08d32d7e88cb531cbcd0c7b4789eab"
        assert hashlib.sha256(raw).hexdigest() == nested_sha
        captured: set[str] = set()
        with ZipFile(BytesIO(raw)) as nested:
            nested_names = {n for n in nested.namelist() if not n.endswith("/")}
            assert len(nested_names) == 106
            classes = {n for n in nested_names if n.endswith(".class")}
            assert len(classes) == 95
            assert nested_names - classes == {
                "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg",
                "META-INF/neoforge.mods.toml", "assets/biolith/icon.png",
                "assets/biolith/lang/en_us.json", "assets/biolith/logo.png",
                "biolith-common-common-refmap.json", "biolith.mixins.json",
                "biolith.neoforge.mixins.json", "pack.mcmeta",
                "META-INF/services/com.terraformersmc.biolith.impl.platform.services.PlatformHelper",
            }
            for directory, digest in SOURCES:
                base = Path("evidence/item-8/sources") / directory
                manifest = (base / "identities.json").read_bytes()
                assert hashlib.sha256(manifest).hexdigest() == digest
                for row in cast("list[dict[str, str]]", json.loads(manifest)):
                    if not row["archive"].startswith(source.name):
                        continue
                    is_nested = row["archive"] == source.name + "!/" + nested_path
                    assert row["archive"] == source.name or is_nested
                    jar = nested if is_nested else archive
                    assert row["archive_sha256"] == (nested_sha if is_nested else source.sha256)
                    assert hashlib.sha256(jar.read(row["class"])).hexdigest() == row["class_sha256"]
                    assert hashlib.sha256((base / row["disassembly"]).read_bytes()).hexdigest() == (
                        row["disassembly_sha256"]
                    )
                    captured.add(row["class"])
            for name, count in (("biolith.mixins.json", 12), ("biolith.neoforge.mixins.json", 3)):
                doc = cast("dict[str, JsonValue]", json.loads(nested.read(name)))
                entries = cast("list[str]", doc["mixins"])
                assert len(entries) == count
                assert {"com/terraformersmc/biolith/impl/mixin/" + n + ".class"
                        for n in entries} <= captured
        prefix = "org/violetmoon/quark/content/world/"
        assert {n for n in names if n.startswith(prefix + "gen/")
                and n.endswith(".class")} <= captured
        assert {n for n in names if n.startswith(prefix + "module/") and n.endswith(".class")
                and "$" not in n} <= captured
        assert {n for n in names if n.startswith(prefix + "feature/")
                and n.endswith(".class")} <= captured
        worldgen = "data/quark/worldgen/"
        documents = {
            n.removeprefix(worldgen): cast("dict[str, JsonValue]", json.loads(archive.read(n)))
            for n in names if n.startswith(worldgen)
        }
        assert Counter(n.split("/")[0] for n in documents) == {
            "configured_feature": 6, "placed_feature": 8, "biome": 1,
        }
        assert {cast("str", d["type"]) for n, d in documents.items()
                if n.startswith("configured_feature/")} == {
            "minecraft:tree",
        }
        assert all(json.loads(archive.read(n))["type"] == "minecraft:ore"
                   for n in optional_worldgen)
    config = cast("dict[str, dict[str, JsonValue]]", tomllib.loads(Path(
        "evidence/item-6/frozen/config/quark-common.toml"
    ).read_text()))
    assert config["experimental"]["Spawner Replacer"] is False
    assert config["experimental"]["Vanilla Stone Clusters"] is False
    assert hashlib.sha256(Path(
        "evidence/item-6/frozen/config/quark-common.toml"
    ).read_bytes()).hexdigest() == (
        "94bfff490eea33f9bb105fae298606c4708ddb8af2f3df8630cc0f0ac7e85327"
    )


def test_quark_canonical_membership() -> None:
    decisions = cast("dict[str, JsonValue]", json.loads(Path(
        "evidence/item-8/family-decisions.json"
    ).read_text()))
    content = cast("dict[str, JsonValue]", decisions["non_registry_content"])
    contributions = cast("dict[str, dict[str, JsonValue]]", content["contributions"])
    selected = {k: v for k, v in contributions.items() if k.startswith("quark:")}
    included = {"quark:" + n for n in (
        "spiral_spire", "fairy_ring", "monster_box", "nether_obsidian_spike",
    )}
    excluded = {"quark:" + n for n in (
        "fallen_log", "underground_styles", "vegetation", "stone_generation",
    )}
    assert set(selected) == included | excluded
    families: list[str] = []
    for key, row in selected.items():
        members = cast("list[dict[str, JsonValue]]", row["families"])
        if key in included:
            assert row["membership_decision"] == "INCLUDE_ONE_FAMILY"
            assert len(members) == 1
            assert members[0]["family"] == key
            families.append(str(members[0]["family"]))
        else:
            assert members == []
            assert all(str(d["decision"]).endswith("NOT_ADDITIONAL_FAMILY")
                       for d in cast("list[dict[str, JsonValue]]", row["dispositions"]))
    assert len(families) == len(set(families)) == 4
    log = selected["quark:fallen_log"]
    assert cast("dict[str, JsonValue]", log["excluded_design"])["candidate_id"] == (
        "quark:fallen_log"
    )
    # These contributions do not duplicate a runtime structure-root group.
    assert not any(str(root).startswith("quark:")
                   for group in cast("list[dict[str, JsonValue]]", decisions["groups"])
                   for root in cast("list[str]", group["structure_ids"]))
