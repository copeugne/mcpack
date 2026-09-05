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


@pytest.mark.parametrize("entry", [
    "doors", "fences", "lights", "paintings", "paths", "roofs", "stairs", "trapdoors", "windows",
])
def test_macaw_entry_and_full_packaged_resource_scope(entry: str) -> None:
    directory = Path(f"evidence/item-8/sources/macaw-{entry}-entry")
    identities = cast("list[dict[str, str]]", json.loads(
        (directory / "identities.json").read_bytes()))
    assert len(identities) == 1
    identity = identities[0]
    source = next(s for s in retained_sources(Path.cwd()) if s.name == identity["archive"])
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    assert identity["archive_sha256"] == source.sha256
    assert hashlib.sha256((directory / identity["disassembly"]).read_bytes()).hexdigest() == (
        identity["disassembly_sha256"])
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        assert hashlib.sha256(archive.read(identity["class"])).hexdigest() == (
            identity["class_sha256"])
        descriptor = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert set(descriptor) == {"modLoader", "loaderVersion", "license", "logoFile", "mods"}
        assert descriptor["modLoader"] == "javafml"
        metadata = {"META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "pack.mcmeta",
                    descriptor["logoFile"]}
        entry_points: set[str] = set()
        for name in names:
            if name.endswith("/") or name in metadata:
                continue
            path = PurePosixPath(name)
            if name.endswith(".class"):
                raw = archive.read(name)
                if b"Lnet/neoforged/fml/common/Mod;" in raw:
                    entry_points.add(name)
                assert b"Lnet/neoforged/fml/common/EventBusSubscriber;" not in raw
                assert b"net/neoforged/neoforge/common/NeoForge" not in raw
            elif name.startswith("assets/"):
                assert path.suffix in {".json", ".png", ".mcmeta", ".ogg"}
            else:
                assert name.startswith("data/"), name
                assert path.suffix == ".json", name
                kind = path.parts[2]
                assert kind in {"advancement", "loot_table", "recipe", "tags", "painting_variant"}
                if kind == "tags":
                    assert path.parts[3] in {"block", "blocks", "item", "painting_variant"}
                document = cast("JsonValue", json.loads(archive.read(name)))
                assert isinstance(document, dict)
        assert entry_points == {identity["class"]}
