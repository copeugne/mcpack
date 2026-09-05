from __future__ import annotations

import gzip
import hashlib
import json
import tomllib
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_resource_selection import mod_conditions_match, runtime_mod_ids

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_ctov_frozen_callback_selection_uses_existing_roots() -> None:
    directory = Path("evidence/item-8/sources/ctov-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "892790797564491473c7bf42d1e92f182cdb640721aa5e00c9a9b9c044de489e"
    )
    for identity in cast("list[dict[str, str]]", json.loads(raw)):
        assert hashlib.sha256((directory / identity["disassembly"]).read_bytes()).hexdigest() == (
            identity["disassembly_sha256"]
        )
    config_raw = Path("evidence/item-6/frozen/config/ctov-common.toml").read_bytes()
    assert hashlib.sha256(config_raw).hexdigest() == (
        "0c2bfe4c04c4f7136c4f924b66dc291c36efdb3ed9d47634872701fbe76f28c6"
    )
    config = tomllib.loads(config_raw.decode())
    structures = cast("dict[str, JsonValue]", config["structures"])
    villages = cast("list[str]", structures["enabledVillages"])
    assert len(villages) == len(set(villages)) == 21
    assert all(structures[name] is True for name in (
        "generatesmallVillage", "generatemediumVillage", "generatelargeVillage",
        "generatePillagerOutpost",
    ))
    assert config["weights"] == {
        "smallVillageWeight": 10, "mediumVillageWeight": 4,
        "largeVillageWeight": 1, "PillagerOutpostWeight": 1,
    }
    # The captured callback uses this literal outpost list, not its unused
    # enabledpillageroutpost wrapper. This proves callback selection, not every
    # possible other provider's structure-set modification or observed placement.
    outposts = (
        "beach", "dark_forest", "desert", "jungle", "badlands", "mountain",
        "plains", "savanna", "snowy", "swamp", "taiga",
    )
    selected = {
        f"ctov:{size}/village_{v}" for size in ("small", "medium", "large") for v in villages
    } | {f"ctov:pillager_outpost_{v}" for v in outposts}
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    roots = {r for r in registry if r.startswith("ctov:")}
    assert len(roots) == 78
    assert len(selected) == 74
    assert selected <= roots
    assert roots - selected == {
        "ctov:pillager_outpost_mesa", "ctov:small/village_underground",
        "ctov:medium/village_underground", "ctov:large/village_underground",
    }


def test_ctov_modifier_conditions_select_only_existing_component_integrations() -> None:
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd"
    )
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    rows = [r for r in cast("list[dict[str, JsonValue]]", catalog["resources"])
            if r["archive"] == "[Neoforge]ctov-3.6.3.jar"
            and "/lithostitched/worldgen_modifier/" in str(r["path"])]
    assert len(rows) == 1019
    log = Path("evidence/raw/item8/registry-r1/debug.log").read_bytes()
    assert hashlib.sha256(log).hexdigest() == (
        "e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b"
    )
    mods = set(runtime_mod_ids(log.decode()))
    selected: list[dict[str, JsonValue]] = []
    for row in rows:
        data = cast("dict[str, JsonValue]", row["document"])
        assert data["type"] == "lithostitched:add_template_pool_elements"
        if mod_conditions_match(data.get("neoforge:conditions", []), mods):
            selected.append(row)
    assert Counter(str(r["path"]).split("/")[4] for r in selected) == {
        "chefsdelight": 21, "farmersdelight": 21, "village_taverns": 21,
    }
    assert len(rows) - len(selected) == 956
