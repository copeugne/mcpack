from __future__ import annotations

import hashlib
import json
import re
import tomllib
from pathlib import Path
from typing import TYPE_CHECKING, cast

import pytest

if TYPE_CHECKING:
    from pydantic import JsonValue


@pytest.mark.parametrize(("family", "directory", "structure_type", "setting"), [
    ("desert_pyramid", "desert-temple", "DESERT_PYRAMID",
     ("betterdeserttemples", "YUNG's Better Desert Temples", "Disable Vanilla Pyramids",
      "disableVanillaPyramids")),
    ("fortress", "fortress", "FORTRESS",
     ("betterfortresses", "YUNG's Better Nether Fortresses", "Disable Vanilla Nether Fortresses",
      "disableVanillaFortresses")),
    ("jungle_pyramid", "jungle-temple", "JUNGLE_TEMPLE",
     ("betterjungletemples", "YUNG's Better Jungle Temples", "Disable Vanilla Jungle Temples",
      "disableVanillaJungleTemples")),
    ("monument", "monument", "OCEAN_MONUMENT",
     ("betteroceanmonuments", "YUNG's Better Ocean Monuments", "Disable Vanilla Ocean Monuments",
      "disableVanillaMonuments")),
    ("stronghold", "stronghold", "STRONGHOLD", None),
    ("swamp_hut", "witch-hut", "SWAMP_HUT",
     ("betterwitchhuts", "YUNG's Better Witch Huts", "Disable Vanilla Witch Huts",
      "disableVanillaWitchHuts")),
])
def test_yung_normal_generation_suppression(
    family: str, directory: str, structure_type: str,
    setting: tuple[str, str, str, str] | None,
) -> None:
    decisions = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()
    ))
    group = next(g for g in decisions["groups"] if g["family_id"] == "minecraft:" + family)
    for source, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256(Path(source).read_bytes()).hexdigest() == digest
    root = Path("evidence/item-8/sources") / (directory + "-suppression")
    entries = cast("list[dict[str, str]]", json.loads((root / "identities.json").read_bytes()))
    code: dict[str, str] = {}
    for entry in entries:
        raw = (root / entry["disassembly"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == entry["disassembly_sha256"]
        code[entry["class"].rsplit("/", 1)[1]] = raw.decode()
    hook_name = next(k for k in code if k.startswith("DisableVanilla"))
    hook = code[hook_name]
    assert 'method=["tryGenerateStructure"]' in hook
    assert 'value="HEAD"' in hook
    assert "cancellable=true" in hook
    assert "value=[class Lnet/minecraft/world/level/chunk/ChunkGenerator;]" in hook
    assert f"StructureType.{structure_type}:" in hook
    assert re.search(r"iconst_0\n[^\n]+Boolean.valueOf:[^\n]+\n[^\n]+setReturnValue:", hook)
    metadata = cast("dict[str, dict[str, str]]", json.loads(
        (root / entries[0]["archive"] / "mixin-metadata.json").read_bytes()
    ))
    for member in metadata.values():
        assert hashlib.sha256(member["text"].encode()).hexdigest() == member["sha256"]
    name = next(k for k in metadata if k.endswith(".mixins.json"))
    mixins = cast("dict[str, JsonValue]", json.loads(metadata[name]["text"]))
    assert mixins["required"] is True
    assert hook_name.removesuffix(".class") in cast("list[str]", mixins["mixins"])
    assert name in metadata["META-INF/neoforge.mods.toml"]["text"]
    if setting is not None:
        mod, section, label, field = setting
        config = tomllib.loads(Path(
            f"evidence/item-6/frozen/config/{mod}-neoforge-1_21.toml"
        ).read_text())
        assert config[section]["General"][label] is True
        assert f"ConfigModule$General.{field}:Z" in hook
        binding = code["ConfigModuleNeoForge.class"]
        assert f"ConfigModule$General.{field}:Z" in binding
        assert "Boolean.booleanValue:()Z" in binding
        assert any(f"// String {label}\n" in text for text in code.values())
    else:
        assert "CONFIG:" not in hook
    variant = cast("dict[str, dict[str, JsonValue]]", group["variants"])["minecraft:" + family]
    assert cast("dict[str, JsonValue]", variant["normal_generation"])["status"] == "SUPPRESSED"
