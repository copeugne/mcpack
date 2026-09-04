from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

import pytest

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_resource_selection import LITHOSTITCHED, select_resources

if TYPE_CHECKING:
    from pydantic import JsonValue

VANILLA = "minecraft-server-1.21.1.jar!/META-INF/versions/1.21.1/server-1.21.1.jar"


def resource(archive: str, path: str) -> dict[str, JsonValue]:
    return {"archive": archive, "path": path, "sha256": "a" * 64, "document": {}}


@pytest.mark.parametrize("enabled", [True, False])
def test_overlay_selection_retains_overridden_or_disabled_source(enabled: bool) -> None:
    base = resource(VANILLA, "data/minecraft/structure/shipwreck/full.nbt")
    overlay = resource(
        LITHOSTITCHED, "overlay.breaks_seed_parity/data/minecraft/structure/shipwreck/full.nbt"
    )
    selected, excluded = select_resources(
        [base, overlay],
        "structure",
        enabled_packs=["vanilla", "mod_data"],
        lithostitched_overlay=enabled,
    )
    assert selected["minecraft:shipwreck/full"] == (overlay if enabled else base)
    assert len(excluded) == 1


def test_known_pool_override_uses_mod_priority() -> None:
    path = "data/minecraft/worldgen/template_pool/trial_chambers/chamber/entrance_cap.json"
    base = resource(VANILLA, path)
    replacement = resource(LITHOSTITCHED, path)
    selected, excluded = select_resources(
        [base, replacement],
        "worldgen/template_pool",
        enabled_packs=["vanilla", "mod_data"],
        lithostitched_overlay=True,
    )
    assert selected["minecraft:trial_chambers/chamber/entrance_cap"] == replacement
    assert len(excluded) == 1
    with pytest.raises(ValueError, match="priority"):
        _ = select_resources(
            [base, replacement],
            "worldgen/template_pool",
            enabled_packs=["mod_data", "vanilla"],
            lithostitched_overlay=True,
        )


def test_unrecognized_collision_cannot_be_resolved_by_file_order() -> None:
    path = "data/example/worldgen/structure/tower.json"
    with pytest.raises(ValueError, match="unresolved competing"):
        _ = select_resources(
            [resource("first.jar", path), resource("second.jar", path)],
            "worldgen/structure",
            enabled_packs=["vanilla", "mod_data"],
            lithostitched_overlay=True,
        )


def test_frozen_pool_selection_matches_runtime_and_resolves_template_overlays() -> None:
    root = Path(__file__).resolve().parents[2]
    raw = (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd"
    )
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    context_raw = (root / "evidence/item-8/runtime/registry-r1/world-context.json").read_bytes()
    assert hashlib.sha256(context_raw).hexdigest() == (
        "0615a2dcdeb2120a467648df95f69aa9f1ef53e8989ae8c2191028d6f5c1aca2"
    )
    context = cast("dict[str, JsonValue]", json.loads(context_raw))
    packs = cast("dict[str, JsonValue]", context["DataPacks"])
    enabled = cast("list[str]", packs["Enabled"])
    config = (root / "evidence/item-6/frozen/config/lithostitched.json").read_bytes()
    assert hashlib.sha256(config).hexdigest() == (
        "d8a63933ec4757186a594debea59dd35724a0a895fe601b324f96217c28312df"
    )
    assert b'"breaks_seed_parity": true' in config
    selected, excluded = select_resources(
        cast("list[JsonValue]", catalog["resources"]),
        "worldgen/template_pool",
        enabled_packs=enabled,
        lithostitched_overlay=True,
    )
    registry_path = (
        root
        / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_template_pool.txt"
    )
    assert hashlib.sha256(registry_path.read_bytes()).hexdigest() == (
        "f73eb1d4fe59db17130ef0ac9c7269bee7bcb0305d79272f6ba1292a500a51e2"
    )
    assert set(selected) == set(read_registry(registry_path))
    assert len(excluded) == 1
    raw_templates = (root / "evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw_templates).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705"
    )
    templates = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw_templates)))
    selected_templates, excluded_templates = select_resources(
        cast("list[JsonValue]", templates["resources"]),
        "structure",
        enabled_packs=enabled,
        lithostitched_overlay=True,
    )
    assert len(selected_templates) == 12078
    assert len(excluded_templates) == 281
    reasons = [cast("dict[str, JsonValue]", row)["reason"] for row in excluded_templates]
    assert reasons.count("overridden by mod_data") == 278
    assert reasons.count("unresolved non-root pack prefix") == 3
