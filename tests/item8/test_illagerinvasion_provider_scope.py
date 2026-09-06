from __future__ import annotations

import gzip
import hashlib
import json
import tomllib
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_illagerinvasion_parent_and_nested_entry_payloads() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("IllagerInvasion"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    nested_path = "META-INF/jars/extensibleenums-neoforge-21.1.1.jar"
    with ZipFile(source.path) as parent:
        nested_bytes = parent.read(nested_path)
        nested_sha = hashlib.sha256(nested_bytes).hexdigest()
        assert nested_sha == "35720e0569288b37fe59dfd3781691019d24ce1fab48623980b9d7a9b5af2e1c"
        with ZipFile(BytesIO(nested_bytes)) as nested:
            for archive, label, archive_name, digest, class_count, captured_count in (
                (parent, "provider", source.name, source.sha256, 137, 24),
                (nested, "extensible-enums", source.name + "!/" + nested_path, nested_sha, 16, 16),
            ):
                directory = Path("evidence/item-8/sources/illagerinvasion-" + label)
                raw = (directory / "identities.json").read_bytes()
                assert hashlib.sha256(raw).hexdigest() == {
                    "provider": "74b6cb2b01b81d99417d139334cf85e7629fb6fef50947d06227b864ec7574c9",
                    "extensible-enums":
                        "3ede180202e65323e4c3b9af92c03a0b81e2fff01c16562946291c0b08500d9f",
                }[label]
                identities = cast("list[dict[str, str]]", json.loads(raw))
                captured = {row["class"] for row in identities}
                assert len(captured) == captured_count
                names = [n for n in archive.namelist() if not n.endswith("/")]
                assert len(names) == len(set(names))
                classes = {n for n in names if n.endswith(".class")}
                assert len(classes) == class_count
                for row in identities:
                    assert row["archive"] == archive_name
                    assert row["archive_sha256"] == digest
                    assert hashlib.sha256(archive.read(row["class"])).hexdigest() == (
                        row["class_sha256"]
                    )
                    disassembly = (directory / row["disassembly"]).read_bytes()
                    assert hashlib.sha256(disassembly).hexdigest() == row["disassembly_sha256"]
                entries = {n for n in classes if any(k in archive.read(n) for k in (
                    b"fml/common/Mod;", b"EventBusSubscriber", b"SubscribeEvent",
                ))}
                assert len(entries) == 2
                assert entries <= captured
                metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
                mixins = {r["config"] for r in cast("list[dict[str, str]]", metadata["mixins"])}
                mod = "illagerinvasion" if label == "provider" else "extensibleenums"
                assert mixins == {mod + ".common.mixins.json", mod + ".neoforge.mixins.json"}
                declared: set[str] = set()
                for path in mixins:
                    document = cast("dict[str, JsonValue]", json.loads(archive.read(path)))
                    assert "plugin" not in document
                    for side in ("mixins", "client", "server"):
                        declared.update(
                            (str(document["package"]) + "." + n).replace(".", "/") + ".class"
                            for n in cast("list[str]", document.get(side, []))
                        )
                assert len(declared) == (6 if label == "provider" else 0)
                assert declared <= captured
                remaining = set(names) - classes - mixins
                remaining -= {
                    "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml",
                    "META-INF/accesstransformer.cfg", "pack.mcmeta", "mod_banner.png",
                    "mod_logo.png", "CHANGELOG.md", "LICENSE.md", "LICENSE-ASSETS.md",
                }
                if label == "extensible-enums":
                    assert remaining == {"META-INF/architectury-loom-nesting-metadata.json"}
                    continue
                assert len(names) == 499
                remaining -= {nested_path, "META-INF/jarjar/metadata.json",
                              "illagerinvasion.common.refmap.json"}
                assets = {n for n in remaining if n.startswith("assets/")}
                assert len(assets) == 203
                remaining -= assets
                assert all(n.startswith("data/") for n in remaining)
                assert Counter("/".join(n.split("/")[:4]) if "/worldgen/" in n
                               else "/".join(n.split("/")[:3]) for n in remaining) == {
                    "data/illagerinvasion/structure": 50, "data/minecraft/structure": 13,
                    "data/illagerinvasion/worldgen/template_pool": 25,
                    "data/illagerinvasion/worldgen/structure": 5,
                    "data/illagerinvasion/worldgen/structure_set": 5,
                    "data/illagerinvasion/loot_table": 23, "data/minecraft/tags": 7,
                    "data/illagerinvasion/tags/worldgen": 5, "data/illagerinvasion/tags": 2,
                    "data/illagerinvasion/advancement": 4, "data/illagerinvasion/recipe": 4,
                    "data/illagerinvasion/trim_material": 1, "data/numismatic-overhaul/tags": 1,
                }
                assert all(n.endswith(".nbt") if "/structure/" in n
                           and "/worldgen/" not in n else n.endswith(".json") for n in remaining)


def test_illagerinvasion_roots_mansion_replacements_and_unused_components() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("IllagerInvasion"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        components = {
            kind: {found[0] for n in archive.namelist()
                   if (found := resource_identity(n, kind, extension))}
            for kind, extension in (
                ("worldgen/structure", ".json"), ("worldgen/template_pool", ".json"),
                ("structure", ".nbt"),
            )
        }
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    traces = cast("dict[str, dict[str, dict[str, JsonValue]]]",
                  json.loads(gzip.decompress(raw)))["structures"]
    roots = components["worldgen/structure"]
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert len(roots) == 5
    assert roots == {r for r in registry if r.startswith("illagerinvasion:")}
    assert roots <= traces.keys()
    assert len(components["worldgen/template_pool"]) == 25
    assert components["worldgen/template_pool"] - {
        p for r in roots for p in cast("list[str]", traces[r]["pools"])
    } == {"illagerinvasion:mobs/pillager"}
    assert len(components["structure"]) == 63
    outside = components["structure"] - {
        t for r in roots for t in cast("list[str]", traces[r]["templates"])
    }
    assert outside == {"illagerinvasion:mobs/pillager"} | {
        "minecraft:woodland_mansion/" + name for name in (
            "1x2_a4", "1x2_a9", "1x2_b3", "1x2_c1", "1x2_c4", "1x2_c_stairs",
            "1x2_d5", "1x2_d_stairs", "2x2_a3", "2x2_b1", "2x2_b2", "2x2_b3", "2x2_b5",
        )
    }
    assert all(not traces[r]["missing"] and not traces[r]["unresolved_elements"] for r in roots)
