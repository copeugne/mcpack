from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

import pytest

from mcpack_evidence.item8_pool_links import pool_links
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


@pytest.mark.parametrize(("name", "namespace", "counts"), [
    ("MoogsEndStructures-1.21-2.0.3.jar", "mes", (25, 57, 67, 1)),
    ("MoogsSoaringStructures-1.21-2.1.2.jar", "mss", (35, 91, 99, 8)),
])
def test_complete_moog_data_scope(
    name: str, namespace: str, counts: tuple[int, int, int, int],
) -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == name)
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    metadata = {"META-INF/MANIFEST.MF", "META-INF/mods.toml", "META-INF/neoforge.mods.toml",
                "fabric.mod.json", "quilt.mod.json", "pack.mcmeta",
                f"assets/{namespace}/lang/en_us.json", f"assets/{namespace}/icon.png"}
    resources: list[JsonValue] = []
    templates: set[str] = set()
    roots: set[str] = set()
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        for name_in_archive in names:
            if name_in_archive.endswith("/") or name_in_archive in metadata:
                continue
            path = PurePosixPath(name_in_archive)
            assert path.parts[:2] == ("data", namespace), name_in_archive
            if path.parts[2] == "structure":
                assert path.suffix == ".nbt"
                templates.add(namespace + ":" + "/".join(path.parts[3:])[:-4])
                continue
            assert path.suffix == ".json"
            document = cast("dict[str, JsonValue]", json.loads(archive.read(name_in_archive)))
            if path.parts[2] == "worldgen":
                assert path.parts[3] in {"structure", "structure_set", "template_pool"}
                if path.parts[3] == "structure":
                    roots.add(namespace + ":" + "/".join(path.parts[4:])[:-5])
                    assert isinstance(document["start_pool"], str)
            elif path.parts[2] == "tags":
                assert path.parts[3:5] == ("worldgen", "biome")
            else:
                assert path.parts[2] == "loot_table"
            resources.append({"archive": source.name, "path": name_in_archive,
                              "sha256": hashlib.sha256(archive.read(name_in_archive)).hexdigest(),
                              "document": document})
    links = cast("list[dict[str, JsonValue]]", pool_links(resources))
    assert all(link["unresolved_elements"] == [] for link in links)
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5")
    trace = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    structures = cast("dict[str, dict[str, JsonValue]]", trace["structures"])
    assert roots <= structures.keys()
    reached_pools = {p for root in roots for p in
                     cast("list[str]", structures[root]["pools"])}
    reached_templates = {t for root in roots for t in
                         cast("list[str]", structures[root]["templates"])}
    assert {cast("str", link["id"]) for link in links} <= reached_pools
    excluded_by_version = {cast("str", edge["id"]) for link in links for edge in
                           cast("list[dict[str, JsonValue]]", link["edges"])
                           if edge["kind"] == "template" and edge.get("selected") is False}
    assert templates - reached_templates <= excluded_by_version
    assert (len(roots), len(links), len(templates), len(templates - reached_templates)) == counts
