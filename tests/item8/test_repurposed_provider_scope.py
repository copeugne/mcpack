from __future__ import annotations

import hashlib
import json
import tomllib
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue

SOURCES = (
    ("pool-codecs",
     "4f1484523b4f3dea5154273eaaffea2459eb8a158af4d39dafcc0ca966a1bb98"),
    ("repurposed-assembly",
     "10a3a2a15d647c5c52c171034c84be9c2fc68e1fe42dd571e8a6c725a6de6746"),
    ("repurposed-datagen-entry",
     "0d2237b825ac55da59a8908beb120e562b67a58ccc3a5de1c151e1bbd980d9bf"),
    ("repurposed-feature-roles",
     "4e90a8ed5ea83a2db56830de2cd50d5dc2c5ed1149eb0d0ad06477eed7409230"),
    ("repurposed-mansion",
     "eea99d1b6d1808ab40ccb5113e510ab329c2a7eceaf630c56473345ec05825fd"),
    ("repurposed-mansion-bindings",
     "e7e337973a74886d6794c31436f892c4f1c6cc68a42429344dcc8697779e14f9"),
    ("repurposed-mansion-layout",
     "1a4fc07772f58cab7379cebd9d237b8332cfee5ef91f031a6cc84354ad8599ee"),
    ("repurposed-mansion-processors",
     "6428fc8e109a796e54586acbdbc0bc0a5526d359d5ee87bec4684f2d11653257"),
    ("repurposed-monument",
     "3e6b74fb9b31ae3758d87b1ba365090f52962ae582deb6d55dae85db29a59379"),
    ("repurposed-monument-processors",
     "d1dc51ab4782be630633659dbea1fdc396c622d0c2076532cee86ce01fcef76d"),
    ("repurposed-monument-rooms",
     "58a0a51e3c6eec5171d450ed23b7345420230e3a71e05f608d09da4dc74059d9"),
    ("repurposed-provider",
     "b41a597ff11502546a3edfac9ae59cbbc7fcc44132a6c10dc01dac43f18c69e7"),
)


def test_repurposed_provider_sources_and_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "repurposed_structures-7.5.21+1.21.1-neoforge.jar")
    assert source.sha256 == "aeb473f0a0a0632cea089377cdd9f66c42cf6f97557fd32c368ac40635285dd2"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = {n for n in archive.namelist() if not n.endswith("/")}
        assert len(names) == 5842
        classes = {n for n in names if n.endswith(".class")}
        assert len(classes) == 248
        assets = {n for n in names if n.startswith("assets/")}
        data = {n for n in names if n.startswith("data/")}
        assert len(assets) == 13
        assert all(n.endswith((".png", ".json")) for n in assets)
        assert not any(n.endswith((".jar", ".mcfunction", ".js", ".py")) for n in names)
        assert names - classes - assets - data == {
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml", "pack.mcmeta",
            "repurposed_structures-common-refmap.json",
            "repurposed_structures-common.mixins.json",
            "repurposed_structures-neoforge.mixins.json",
        }
        assert Counter("/".join(n.split("/")[:3]) for n in data) == {
            "data/repurposed_structures/structure": 3162,
            "data/repurposed_structures/worldgen": 1863,
            "data/repurposed_structures/tags": 238,
            "data/repurposed_structures/loot_table": 179,
            "data/repurposed_structures/rs_spawners": 56,
            "data/repurposed_structures/neoforge": 24,
            "data/repurposed_structures/rs_pieces_spawn_counts": 22,
            "data/repurposed_structures/advancement": 19,
            "data/minecraft/tags": 7, "data/neoforge/loot_modifiers": 1,
            "data/pneumaticcraft/tags": 1, "data/repurposed_structures/loot_modifiers": 1,
            "data/repurposed_structures/structure_map_trades": 1,
        }
        prefix = "data/repurposed_structures/worldgen/"
        assert Counter(n.removeprefix(prefix).split("/")[0]
                       for n in data if n.startswith(prefix)) == {
            "structure": 107, "structure_set": 37, "template_pool": 1099,
            "processor_list": 327, "configured_feature": 136, "placed_feature": 157,
        }
        roots = {"repurposed_structures:" + n.removeprefix(prefix + "structure/")[:-5]
                 for n in data if n.startswith(prefix + "structure/")}
        registry = read_registry(Path(
            "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
        ))
        assert roots == {k for k in registry if k.startswith("repurposed_structures:")}
        captured: set[str] = set()
        for directory, digest in SOURCES:
            base = Path("evidence/item-8/sources") / directory
            raw = (base / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                if row["archive"] != source.name:
                    continue
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert hashlib.sha256((base / row["disassembly"]).read_bytes()).hexdigest() == (
                    row["disassembly_sha256"]
                )
                captured.add(row["class"])
        mod_prefix = "com/telepathicgrunt/repurposedstructures/"
        assert {n for n in classes if n.startswith(mod_prefix + "world/structures/")
                and n.count("/") == 5 and "$" not in n} <= captured
        entries = {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))}
        assert entries == {
            mod_prefix + "datagen/StructureNbtUpdaterDatagen.class",
            mod_prefix + "neoforge/RepurposedStructuresNeoforge.class",
        }
        assert entries <= captured
        metadata = cast("dict[str, JsonValue]", tomllib.loads(
            archive.read("META-INF/neoforge.mods.toml").decode()
        ))
        assert metadata["mixins"] == [
            {"config": "repurposed_structures-neoforge.mixins.json"},
            {"config": "repurposed_structures-common.mixins.json"},
        ]
        for suffix, count in (("common", 29), ("neoforge", 1)):
            document = cast("dict[str, JsonValue]", json.loads(archive.read(
                f"repurposed_structures-{suffix}.mixins.json"
            )))
            package = str(document["package"]).replace(".", "/")
            mixins = cast("list[str]", document["mixins"])
            assert len(mixins) == count
            assert {package + "/" + n.replace(".", "/") + ".class" for n in mixins} <= captured
            assert document["client"] == (["blocks.StructureBlockScreenMixin"]
                                           if suffix == "common" else [])
            assert "plugin" not in document
