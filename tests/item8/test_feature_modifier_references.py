from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_resource_selection import select_resources

if TYPE_CHECKING:
    from pydantic import JsonValue


# Keep the observed feature grammar in one proof, without a new traversal framework.
def test_selected_feature_modifier_references() -> None:  # noqa: C901, PLR0915
    root = Path(__file__).resolve().parents[2]
    raw = (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd"
    )
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    resources = cast("list[JsonValue]", catalog["resources"])
    config_path = root / "evidence/item-6/frozen/config/regions_unexplored/common.json"
    config_raw = config_path.read_bytes()
    assert hashlib.sha256(config_raw).hexdigest() == (
        "300dda462e31f6f1bcce0d67308e4939d1b461a03c8cc92ba805f7ac9d1cb66c"
    )
    # This exact frozen file has standalone // comment lines, not inline comments.
    configuration = cast("dict[str, JsonValue]", json.loads("\n".join(
        line for line in config_raw.decode().splitlines() if not line.lstrip().startswith("//")
    )))
    toggles = configuration["vanilla_changes"]
    assert isinstance(toggles, dict)
    placed_sources, _ = select_resources(
        resources, "worldgen/placed_feature",
        enabled_packs=["vanilla", "mod_data"], lithostitched_overlay=True,
    )
    configured_sources, _ = select_resources(
        resources, "worldgen/configured_feature",
        enabled_packs=["vanilla", "mod_data"], lithostitched_overlay=True,
    )
    modifiers, _ = select_resources(
        resources, "lithostitched/worldgen_modifier",
        enabled_packs=["vanilla", "mod_data"], lithostitched_overlay=True,
    )
    seen: set[tuple[str, str]] = set()
    terminals: set[str] = set()
    counts: Counter[str] = Counter()

    def placed(value: JsonValue) -> None:
        if isinstance(value, str):
            key = ("placed", value)
            if key in seen:
                return
            seen.add(key)
            value = placed_sources[value]["document"]
        assert isinstance(value, dict)
        assert set(value) == {"feature", "placement"}
        configured(value["feature"])

    def configured(value: JsonValue) -> None:
        if isinstance(value, str):
            key = ("configured", value)
            if key in seen:
                return
            seen.add(key)
            value = configured_sources[value]["document"]
        assert isinstance(value, dict)
        assert set(value) == {"type", "config"}
        kind, config = value["type"], value["config"]
        assert isinstance(kind, str)
        assert isinstance(config, dict)
        if kind in {"minecraft:random_patch", "minecraft:flower"}:
            placed(config["feature"])
        elif kind in {"lithostitched:weighted_selector", "lithostitched:composite"}:
            assert isinstance(config["features"], list)
            for feature in config["features"]:
                assert isinstance(feature, dict)
                if "data" in feature:
                    assert kind == "lithostitched:weighted_selector"
                    assert set(feature) == {"data", "weight"}
                    weight = feature["weight"]
                    assert isinstance(weight, int)
                    assert weight > 0
                    placed(feature["data"])
                else:
                    placed(feature)
        elif kind == "minecraft:random_selector":
            placed(config["default"])
            assert isinstance(config["features"], list)
            for feature in config["features"]:
                assert isinstance(feature, dict)
                placed(feature["feature"])
        else:
            # These are implementation endpoints, not absence-of-content claims.
            terminals.add(kind)

    for resource in modifiers.values():
        document = resource["document"]
        assert isinstance(document, dict)
        kind = document["type"]
        if kind not in {"lithostitched:add_features", "lithostitched:remove_features"}:
            continue
        assert isinstance(kind, str)
        assert resource["archive"] == "regions-unexplored-0.6.1-neoforge-21.1.jar"
        predicate = document["predicate"]
        assert isinstance(predicate, dict)
        assert set(predicate) == {"type", "key"}
        assert predicate["type"] == "regions_unexplored:config"
        key = predicate["key"]
        assert isinstance(key, str)
        assert key.startswith("vanilla_changes/")
        assert toggles[key.removeprefix("vanilla_changes/")] is True
        counts[kind] += 1
        # Predicate truth does not prove successful placement in a generated world.
        features = document["features"]
        if isinstance(features, str):
            features = [features]
        assert isinstance(features, list)
        for feature in features:
            placed(feature)
    assert counts == {"lithostitched:add_features": 30, "lithostitched:remove_features": 4}
    assert Counter(kind for kind, _ in seen) == {"placed": 34, "configured": 41}
    assert terminals == {
        "minecraft:simple_block", "minecraft:tree", "regions_unexplored:saguaro_cactus",
        "regions_unexplored:palm_tree", "regions_unexplored:bamboo_tree",
        "regions_unexplored:giant_lily",
    }
