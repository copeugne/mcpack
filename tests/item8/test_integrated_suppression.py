from __future__ import annotations

import hashlib
import json
import re
import tomllib
from pathlib import Path
from typing import TYPE_CHECKING, cast

import pytest

from mcpack_evidence.item8_registry import read_registry

if TYPE_CHECKING:
    from pydantic import JsonValue


@pytest.mark.parametrize(("directory", "mod", "section", "settings"), [
    ("integrated-village", "integrated_villages", "Integrated Villages",
     {"Disable Vanilla Villages": "disableVanillaVillages"}),
    ("idas", "idas", "IDAS", {"Disable Vanilla Desert Pyramid": "disableDesertPyramid",
                              "Disable Ice and Fire Structures": "disableIaFStructures"}),
])
def test_integrated_suppression_source_bindings(
    directory: str, mod: str, section: str, settings: dict[str, str],
) -> None:
    root = Path("evidence/item-8/sources") / (directory + "-suppression")
    entries = cast("list[dict[str, str]]", json.loads((root / "identities.json").read_bytes()))
    code: dict[str, str] = {}
    for entry in entries:
        raw = (root / entry["disassembly"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == entry["disassembly_sha256"]
        code[entry["class"].rsplit("/", 1)[1]] = raw.decode()
    hook_name = next(k for k in code if k.endswith("Mixin.class"))
    hook = code[hook_name]
    assert 'method=["tryGenerateStructure(' in hook
    assert 'value="HEAD"' in hook
    assert "cancellable=true" in hook
    assert "value=[class Lnet/minecraft/world/level/chunk/ChunkGenerator;]" in hook
    assert re.search(r"iconst_0\n[^\n]+Boolean.valueOf:[^\n]+\n[^\n]+setReturnValue:", hook)
    metadata = cast("dict[str, dict[str, str]]", json.loads(
        (root / entries[0]["archive"] / "mixin-metadata.json").read_bytes()
    ))
    for row in metadata.values():
        assert hashlib.sha256(row["text"].encode()).hexdigest() == row["sha256"]
    mixin_name = mod + "-common.mixins.json"
    mixins = cast("dict[str, JsonValue]", json.loads(metadata[mixin_name]["text"]))
    assert mixins["required"] is True
    assert hook_name.removesuffix(".class") in cast("list[str]", mixins["mixins"])
    assert mixin_name in metadata["META-INF/neoforge.mods.toml"]["text"]
    config = tomllib.loads(Path(
        f"evidence/item-6/frozen/config/{mod}-neoforge-1_21.toml"
    ).read_text())
    for label, field in settings.items():
        assert config[section]["General"][label] is True
        assert f"// String {label}\n" in code["ConfigGeneralNeoforge.class"]
        assert f"ConfigModule$General.{field}:Z" in hook
        assert f"ConfigModule$General.{field}:Z" in code["ConfigModuleNeoforge.class"]
        assert "Boolean.booleanValue:()Z" in code["ConfigModuleNeoforge.class"]


def test_integrated_suppression_exact_registry_scope_and_family_dispositions() -> None:
    source = Path("evidence/item-8/sources")
    village = next((source / "integrated-village-suppression").glob("*/*Mixin.txt")).read_text()
    keys = cast("list[str]", re.findall(r"// String ([^\n]+)", village.split("  static {};")[1]))
    suppressed = {k if ":" in k else "minecraft:" + k for k in keys}
    assert len(keys) == 7
    assert suppressed == {
        "minecraft:village_desert", "minecraft:village_plains", "minecraft:village_snowy",
        "minecraft:village_savanna", "minecraft:village_taiga",
        "terralith:fortified_desert_village", "terralith:fortified_village",
    }
    assert "ResourceLocation.tryParse:" in village
    assert "Holder.unwrapKey:" in village
    assert "Set.contains:" in village
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert suppressed <= set(registry)
    idas = next((source / "idas-suppression").glob("*/*Mixin.txt")).read_text()
    iaf_keys = cast("list[str]", re.findall(
        r"// String ([^\n]+)", idas.split("  static {};")[1]
    ))
    assert iaf_keys == ["iceandfire", "mausoleum", "iceandfire", "gorgon_temple",
                        "iceandfire", "graveyard"]
    assert not {"iceandfire:" + k for k in iaf_keys[1::2]} & set(registry)
    assert "StructureType.DESERT_PYRAMID:" in idas
    decisions = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()
    ))
    checked: set[str] = set()
    for group in decisions["groups"]:
        if group["family_id"] not in {
            "minecraft:village", "terralith:fortified_village", "minecraft:desert_pyramid"
        }:
            continue
        for path, digest in cast("dict[str, str]", group["evidence"]).items():
            assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest
        for rid, variant in cast("dict[str, dict[str, JsonValue]]", group["variants"]).items():
            disposition = cast("dict[str, JsonValue]", variant["normal_generation"])
            assert disposition["status"] == "SUPPRESSED"
            if rid == "minecraft:desert_pyramid":
                assert "disableDesertPyramid" in str(disposition["additional_suppression"])
            else:
                checked.add(rid)
    assert checked == suppressed
