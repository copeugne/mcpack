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


def test_lithostitched_payload_and_declared_hooks() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("lithostitched-"))
    assert source.sha256 == "d367ea1885486755dd8a162b8bb28404a35155e9fd34eba03108991363b6c70a"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    manifests = {
        "lithostitched-alias-code": (
            "eea3af78139809c0a2452a0027bfe83fac321380574b3a10ba3d8dcc16c1691b"
        ),
        "lithostitched-biome-injector-code": (
            "b48129fffa046624fb15e6381edb678001d491c4be8ddcd03e2c5ec440f8afaa"
        ),
        "lithostitched-feature-modifier-code": (
            "b7138be0cec7822f8e4fb19c6c9175e3ac1ba7ab174cb58015c34be488b9aaa1"
        ),
        "lithostitched-platform-modifier-code": (
            "b9705872460fd2c8aac838cfc70780fc4085700ab1aaa92b9ca66fb4ba3f52d5"
        ),
        "lithostitched-pool-additions-code": (
            "f3aecd612d8fdfe23649887ea70032cdc4fc5b0db00276ae3c0e718bdadf0a75"
        ),
        "lithostitched-pool-compilation-code": (
            "c69e16e8ae53df5fa0d817126b3b62d739e7780292576c1891e3084054ee556e"
        ),
        "lithostitched-processor-registration-code": (
            "803ac1e2b0d9992d51c5e5246db7ff88683fe0f7de21ec6f4e9881d240da991f"
        ),
        "lithostitched-provider-entry": (
            "86a0259a201e3198d49e62e81834e93e8aff50ea14ca7d93703a02c99cade3c8"
        ),
        "lithostitched-provider-hooks": (
            "7b4524568318a99cc4fc77d5ac4d8c23c125cc492d5c3045ae6347f3d170a8c2"
        ),
        "lithostitched-random-block-code": (
            "03ae09f76ee50c52058b4cb0818fab9ab2a2ffbe458676a3a4020f9bed127c8d"
        ),
        "lithostitched-street-processor-code": (
            "b813d2393bfb7ff410451e5cee65a6036187abe438405bb2a1d9cd00e5f5cafc"
        ),
        "lithostitched-surface-lifecycle-code": (
            "ed1f626e586466a933457e0bc18859254fc483cd062e4c359d58f6e8aa084885"
        ),
        "pool-codecs": "4f1484523b4f3dea5154273eaaffea2459eb8a158af4d39dafcc0ca966a1bb98",
    }
    captured: set[str] = set()
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 445
        assert Counter("classes" if n.endswith(".class") else n.split("/")[0] for n in names) == {
            "classes": 339,
            "data": 77,
            "overlay.breaks_seed_parity": 20,
            "META-INF": 3,
            "idea.json": 1,
            "pack.mcmeta": 1,
            "pack.png": 1,
            "lithostitched.mixins.json": 1,
            "lithostitched.21.1.mixins.json": 1,
            "lithostitched.neoforge.mixins.json": 1,
        }
        assert {n for n in names if n.startswith("META-INF/")} == {
            "META-INF/MANIFEST.MF",
            "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml",
        }
        for label, digest in manifests.items():
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            rows = cast("list[dict[str, str]]", json.loads(raw))
            selected = [r for r in rows if r["archive"] == source.name]
            assert selected
            for row in selected:
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert (
                    hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                    == (row["disassembly_sha256"])
                )
                captured.add(row["class"])
        assert {
            n
            for n in names
            if n.endswith(".class")
            and any(
                tag in archive.read(n)
                for tag in (
                    b"Lnet/neoforged/fml/common/Mod;",
                    b"Lnet/neoforged/fml/common/EventBusSubscriber;",
                )
            )
        } == {"dev/worldgen/lithostitched/LithostitchedNeoforge.class"}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        entries = cast("list[dict[str, str]]", metadata["mixins"])
        assert {m["config"] for m in entries} == {
            "lithostitched.mixins.json",
            "lithostitched.21.1.mixins.json",
            "lithostitched.neoforge.mixins.json",
        }
        hooks: set[str] = set()
        for entry in entries:
            mixin = cast("dict[str, JsonValue]", json.loads(archive.read(entry["config"])))
            assert not mixin.get("plugin")
            package = cast("str", mixin["package"]).replace(".", "/")
            for name in cast("list[str]", mixin["mixins"]) + cast(
                "list[str]", mixin.get("server", [])
            ):
                hooks.add(package + "/" + name.replace(".", "/") + ".class")
        assert len(hooks) == 55
        assert hooks <= captured


def test_lithostitched_template_lists_are_existing_vanilla_components() -> None:
    sources = retained_sources(Path.cwd())
    source = next(s for s in sources if s.name.startswith("lithostitched-"))
    minecraft = next(s for s in sources if s.name == "minecraft-server-1.21.1.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    assert hashlib.sha256(minecraft.path.read_bytes()).hexdigest() == minecraft.sha256
    assert minecraft.nested_archive is not None
    with ZipFile(minecraft.path) as outer:
        vanilla_bytes = outer.read(minecraft.nested_archive)
    with ZipFile(source.path) as archive, ZipFile(BytesIO(vanilla_bytes)) as vanilla:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        prefix = "data/lithostitched/lithostitched/template_list/"
        lists = {
            n.removeprefix(prefix): cast("list[str]", json.loads(archive.read(n)))
            for n in names
            if n.startswith(prefix)
        }
        assert len(lists) == 26
        groups: dict[str, set[str]] = {}
        for name, choices in lists.items():
            group = name.split("/")[0].removesuffix(".json")
            groups.setdefault(group, set()).update(choices)
            for choice in choices:
                assert choice.startswith("minecraft:")
                assert (
                    "data/minecraft/structure/" + choice.removeprefix("minecraft:") + ".nbt"
                    in vanilla.namelist()
                )
        assert {g: len(v) for g, v in groups.items()} == {
            "nether_fossil": 14,
            "ruined_portal": 13,
            "shipwreck": 20,
            "woodland_mansion": 50,
        }
        overlays = {
            n.removeprefix("overlay.breaks_seed_parity/data/minecraft/structure/").removesuffix(
                ".nbt"
            )
            for n in names
            if n.startswith("overlay.breaks_seed_parity/")
        }
        assert overlays == {v.removeprefix("minecraft:") for v in groups["shipwreck"]}
        pack = cast("dict[str, JsonValue]", json.loads(archive.read("pack.mcmeta")))
        assert cast("dict[str, JsonValue]", pack["neoforge:overlays"])["entries"] == [
            {
                "directory": "overlay.breaks_seed_parity",
                "formats": [48, 99],
                "min_format": 48,
                "max_format": 99,
                "neoforge:conditions": [{"type": "lithostitched:breaks_seed_parity"}],
            }
        ]
        for n in names:
            if n.startswith("data/lithostitched/tags/worldgen/template_pool/"):
                for pool in cast("list[str]", json.loads(archive.read(n))["values"]):
                    assert (
                        "data/" + pool.replace(":", "/worldgen/template_pool/") + ".json"
                        in vanilla.namelist()
                    )
        assert "data/minecraft/worldgen/structure/trial_chambers.json" in vanilla.namelist()


def test_lithostitched_remaining_data_roles() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("lithostitched-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if n.startswith("data/") and not n.endswith("/")]
        assert all(n.endswith(".json") for n in names)
        assert Counter("/".join(n.split("/")[2:4]) for n in names) == {
            "lithostitched/template_list": 26,
            "worldgen/processor_list": 23,
            "tags/worldgen": 13,
            "worldgen/density_function": 5,
            "lithostitched/fast_noise_config": 3,
            "lithostitched/region": 3,
            "lithostitched/worldgen_modifier": 2,
            "worldgen/noise": 1,
            "worldgen/template_pool": 1,
        }
        modifiers = {
            Path(n).stem: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
            for n in names
            if "/lithostitched/worldgen_modifier/" in n
        }
        assert modifiers["compile_raw_templates"] == {
            "type": "lithostitched:internal/compile_raw_templates"
        }
        alias = modifiers["set_trial_chambers_pool_aliases"]
        assert alias["type"] == "lithostitched:set_pool_aliases"
        assert alias["structures"] == "minecraft:trial_chambers"
        assert alias["append"] is False
        assert {
            p
            for group in cast("list[dict[str, list[str]]]", alias["pool_aliases"])
            for p in group["pools"]
        } == {
            "#lithostitched:trial_spawner/" + n
            for n in ("ranged", "slow_ranged", "melee", "small_melee")
        }
        processors = [
            p
            for n in names
            if n.startswith("data/lithostitched/worldgen/processor_list/")
            for p in cast("list[dict[str, JsonValue]]", json.loads(archive.read(n))["processors"])
        ]
        assert Counter(cast("str", p["processor_type"]) for p in processors) == {
            "lithostitched:block_swap": 8,
            "lithostitched:apply_random": 1,
        }
        pool = cast(
            "dict[str, JsonValue]",
            json.loads(
                archive.read(
                    "data/minecraft/worldgen/template_pool/trial_chambers/chamber/entrance_cap.json"
                )
            ),
        )
        assert pool["fallback"] == "minecraft:empty"
        assert pool["elements"] == [
            {
                "weight": 1,
                "element": {
                    "element_type": "minecraft:single_pool_element",
                    "location": "minecraft:trial_chambers/chamber/entrance_cap",
                    "processors": "minecraft:trial_chambers_copper_bulb_degradation",
                    "projection": "rigid",
                },
            }
        ]
