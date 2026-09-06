from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_create_generation_payload_and_captured_boundaries() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "create-1.21.1-6.0.10.jar")
    assert source.sha256 == "ef87fe5709f1ba1f5b8bb20a2925b5afb4669e178fd6d8bf10c167759eefe37a"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/create-generation-boundaries")
    raw = (directory / "identities.json").read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == "7fb69a735eb1ffd0ada39ca9d1950120cf5fa87b142dc3e9814fab7ab9b5a5fe"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    assert len(rows) == 4
    with ZipFile(source.path) as archive:
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert (
                hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                == row["disassembly_sha256"]
            )
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 11753
        assert Counter(n.split("/")[2] for n in names if n.startswith("data/")) == {
            "recipe": 1884,
            "advancement": 1150,
            "loot_table": 640,
            "tags": 183,
            "structure": 67,
            "create": 25,
            "damage_type": 9,
            "worldgen": 6,
            "data_maps": 4,
            "neoforge": 3,
            "enchantment": 2,
            "curios": 1,
        }
        templates = {n for n in names if n.endswith(".nbt")}
        tests = {n for n in templates if n.startswith("data/create/structure/gametest/")}
        ponder = {n for n in templates if n.startswith("assets/create/ponder/")}
        assert len(tests) == 67
        assert len(ponder) == 178
        assert templates == tests | ponder
        features = {"zinc_ore", "striated_ores_overworld", "striated_ores_nether"}
        assert {n for n in names if n.startswith("data/") and "/worldgen/" in n} == {
            f"data/create/worldgen/{kind}/{feature}.json"
            for kind in ("configured_feature", "placed_feature")
            for feature in features
        }
        assert {n for n in names if n.startswith("data/") and "/biome_modifier/" in n} == {
            f"data/create/neoforge/biome_modifier/{feature}.json" for feature in features
        }
        for feature in features:
            configured = cast(
                "dict[str, object]",
                json.loads(archive.read(f"data/create/worldgen/configured_feature/{feature}.json")),
            )
            assert configured["type"] == (
                "minecraft:ore" if feature == "zinc_ore" else "create:layered_ore"
            )
            placed = cast(
                "dict[str, object]",
                json.loads(archive.read(f"data/create/worldgen/placed_feature/{feature}.json")),
            )
            assert placed["feature"] == f"create:{feature}"
            assert cast("list[dict[str, object]]", placed["placement"])[-1] == {
                "type": "create:config_filter"
            }
            modifier = cast(
                "dict[str, object]",
                json.loads(archive.read(f"data/create/neoforge/biome_modifier/{feature}.json")),
            )
            assert modifier == {
                "type": "neoforge:add_features",
                "features": f"create:{feature}",
                "step": "underground_ores",
                "biomes": "#minecraft:is_nether"
                if feature.endswith("nether")
                else "#minecraft:is_overworld",
            }


def test_create_entry_and_template_consumer_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "create-1.21.1-6.0.10.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/create-entry-template-consumers")
    raw = (directory / "identities.json").read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == "151d5db9de69c37bd56cb596da59fe227f4f750b77a873cae8c0459b7d4738d5"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    assert {row["class"] for row in rows} == {
        "com/simibubi/create/Create.class",
        "com/simibubi/create/AllStructureProcessorTypes.class",
        "com/simibubi/create/foundation/mixin/CreateMixinPlugin.class",
        "com/simibubi/create/infrastructure/gametest/CreateTestFunction.class",
    }
    with ZipFile(source.path) as archive:
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert (
                hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                == row["disassembly_sha256"]
            )


def test_create_common_schematic_and_dynamic_data_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "create-1.21.1-6.0.10.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        for label, digest, count in (
            (
                "create-common-schematics",
                "740e8c093ef2e861d14015498e1c1c53cbab297810e68997f8dd6bec65441b8c",
                5,
            ),
            (
                "create-dynamic-data",
                "48b9e6ce6979db0df0ea0003fffcfa95545336480a694270ff952993b1c3c70c",
                1,
            ),
            (
                "create-dynamic-recipe-serializer",
                "3bfb8d0f3a362eec0930be85992d6ee2470bf3aa40b1621748ec7c78061b7292",
                1,
            ),
            (
                "create-common-mixins",
                "e7941906291f7bfe6f15b3989e4db734cb57c0aec9e2ac55f370bd4cd2be7193",
                43,
            ),
            (
                "create-remaining-entries",
                "3428176fa46ad9d0a07e89f9f7c1748b8bea6154e793ad07bc7e251dbf8fbafb",
                55,
            ),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            rows = cast("list[dict[str, str]]", json.loads(raw))
            assert len(rows) == count
            for row in rows:
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert (
                    hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                    == row["disassembly_sha256"]
                )


def test_create_remaining_declared_entry_inventory() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "create-1.21.1-6.0.10.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        annotated = {
            n
            for n in archive.namelist()
            if n.endswith(".class")
            and any(
                marker in archive.read(n)
                for marker in (
                    b"Lnet/neoforged/fml/common/Mod;",
                    b"Lnet/neoforged/fml/common/EventBusSubscriber;",
                )
            )
        }
        assert len(annotated) == 58
        config = cast("dict[str, object]", json.loads(archive.read("create.mixins.json")))
        prefix = cast("str", config["package"]).replace(".", "/") + "/"
        common = {
            prefix + n.replace(".", "/") + ".class" for n in cast("list[str]", config["mixins"])
        }
        assert len(common) == 43
        assert not annotated & common
        assert common <= set(archive.namelist())
        rows = cast(
            "list[dict[str, str]]",
            json.loads(
                Path("evidence/item-8/sources/create-common-mixins/identities.json").read_text()
            ),
        )
        assert {row["class"] for row in rows} == common
        directory = Path("evidence/item-8/sources/create-remaining-entries")
        entries = cast(
            "list[dict[str, str]]", json.loads((directory / "identities.json").read_text())
        )
        previously_captured = {
            "com/simibubi/create/Create.class",
            "com/simibubi/create/foundation/events/CommonEvents.class",
            "com/simibubi/create/foundation/events/CommonEvents$ModBusEvents.class",
            "com/simibubi/create/infrastructure/gametest/CreateGameTests.class",
        }
        assert {row["class"] for row in entries} == (annotated - previously_captured) | {
            "com/simibubi/create/api/registry/CreateBuiltInRegistries.class"
        }
        client_subscribers: set[str] = set()
        for row in entries:
            text = (directory / row["disassembly"]).read_text()
            annotation = re.search(
                r"net.neoforged.fml.common.EventBusSubscriber\(\n(.*?)\n    \)", text, re.DOTALL
            )
            if annotation and "Dist;.CLIENT" in annotation[1]:
                client_subscribers.add(row["class"])
        assert len(client_subscribers) == 17
        client = (directory / source.name / "com.simibubi.create.CreateClient.txt").read_text()
        assert 'value="create"\n      dist=[Lnet/neoforged/api/distmarker/Dist;.CLIENT]' in client


def test_create_flywheel_and_registrate_membership() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "create-1.21.1-6.0.10.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as parent:
        for member, digest, count in (
            (
                "META-INF/jarjar/flywheel-neoforge-1.21.1-1.0.6.jar",
                "31dda15c205eb596d3b3449ef03f6af7363a6cd35b3da4bfe916b304f9e5337e",
                636,
            ),
            (
                "META-INF/jarjar/Registrate-MC1.21-1.3.0+67.jar",
                "510f4041c41739f1d8ea8850ab8364d3e3a5fada8529beed5d9f479e2523db52",
                89,
            ),
        ):
            raw = parent.read(member)
            assert hashlib.sha256(raw).hexdigest() == digest
            with ZipFile(BytesIO(raw)) as archive:
                names = [n for n in archive.namelist() if not n.endswith("/")]
                assert len(names) == len(set(names)) == count
                annotated = {
                    n
                    for n in names
                    if n.endswith(".class")
                    and any(
                        t in archive.read(n)
                        for t in (
                            b"Lnet/neoforged/fml/common/Mod;",
                            b"Lnet/neoforged/fml/common/EventBusSubscriber;",
                        )
                    )
                }
                if "Registrate-" in member:
                    assert not annotated
                    assert set(names) == {"META-INF/MANIFEST.MF"} | {
                        n
                        for n in names
                        if n.startswith("com/tterrag/registrate/") and n.endswith(".class")
                    }
                    assert archive.read("META-INF/MANIFEST.MF").decode().splitlines() == [
                        "Manifest-Version: 1.0",
                        "FMLModType: GAMELIBRARY",
                        "",
                    ]
                    continue
                assert Counter(
                    "classes" if n.endswith(".class") else n.split("/")[0] for n in names
                ) == {
                    "classes": 555,
                    "assets": 71,
                    "META-INF": 3,
                    "backend-flywheel.refmap.json": 1,
                    "flywheel.refmap.json": 1,
                    "flywheel.backend.mixins.json": 1,
                    "flywheel.impl.mixins.json": 1,
                    "flywheel.impl.neoforge.mixins.json": 1,
                    "logo.png": 1,
                    "pack.mcmeta": 1,
                }
                assert {n for n in names if n.startswith("META-INF/")} == {
                    "META-INF/MANIFEST.MF",
                    "META-INF/LICENSE.md",
                    "META-INF/neoforge.mods.toml",
                }
                assert annotated == {"dev/engine_room/flywheel/impl/FlywheelNeoForge.class"}
                for filename in (
                    "flywheel.backend.mixins.json",
                    "flywheel.impl.mixins.json",
                    "flywheel.impl.neoforge.mixins.json",
                ):
                    config = cast("dict[str, object]", json.loads(archive.read(filename)))
                    assert config["client"]
                    assert not any(config.get(k) for k in ("mixins", "server", "plugin"))
                directory = Path("evidence/item-8/sources/create-flywheel-entry")
                identities = (directory / "identities.json").read_bytes()
                assert (
                    hashlib.sha256(identities).hexdigest()
                    == "08dd1db3d78aa87730567c551d4a33a2bdcf0081eb35560fa522a544b49f37be"
                )
                rows = cast("list[dict[str, str]]", json.loads(identities))
                assert len(rows) == 1
                row = rows[0]
                assert row["archive"] == source.name + "!/" + member
                assert row["archive_sha256"] == digest
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                disassembly = (directory / row["disassembly"]).read_bytes()
                assert hashlib.sha256(disassembly).hexdigest() == row["disassembly_sha256"]
                assert "dist=[Lnet/neoforged/api/distmarker/Dist;.CLIENT]" in disassembly.decode()
