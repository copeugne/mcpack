from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

import pytest

from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


@pytest.mark.parametrize("name", [
    "lootintegration_townsandtowers-1.3.jar",
    "lootintegration_wda-1.8.jar",
    "lootintegrations_ctov-1.4.jar",
    "lootintegrations_integrated-1.5.jar",
    "lootintegrations_moog-2.0.jar",
    "lootintegrations_vanilla-1.6.jar",
    "lootintegrations_yungs-1.5.jar",
])
def test_complete_loot_addon_payload_has_no_structure_contribution(name: str) -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == name)
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    metadata = {"META-INF/MANIFEST.MF", "META-INF/mods.toml",
                "META-INF/neoforge.mods.toml", "fabric.mod.json", "pack.mcmeta"}
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        files = {n for n in names if not n.endswith("/")}
        assert metadata <= files
        payload = files - metadata
        assert payload
        assert all(PurePosixPath(n).parent == PurePosixPath("data/lootintegrations/loot")
                   and n.endswith(".json") for n in payload)
        # Exhaustive file accounting above excludes classes, nested archives,
        # templates, services, mixins, scripts and generation resource files.
        descriptor = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert descriptor["modLoader"] == "lowcodefml"
        for path in payload:
            document = cast("dict[str, JsonValue]", json.loads(archive.read(path)))
            assert set(document) == {
                "loot_table", "max_result_itemcount", "integrated_loot_tables"}
            assert isinstance(document["loot_table"], str)
            assert isinstance(document["integrated_loot_tables"], dict)
            assert all(isinstance(key, str) and isinstance(weight, int)
                       for key, weight in document["integrated_loot_tables"].items())
