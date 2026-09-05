from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_seven_seas_scope_preserves_missing_component() -> None:
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar"
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/seven-seas-entry")
    identities = cast(
        "list[dict[str, str]]", json.loads((directory / "identities.json").read_bytes())
    )
    assert len(identities) == 1
    identity = identities[0]
    assert (
        hashlib.sha256((directory / identity["disassembly"]).read_bytes()).hexdigest()
        == (identity["disassembly_sha256"])
    )
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    with ZipFile(source.path) as archive:
        assert (
            hashlib.sha256(archive.read(identity["class"])).hexdigest() == identity["class_sha256"]
        )
        names = archive.namelist()
        assert len(names) == len(set(names))
        assert {n for n in names if n.endswith(".class")} == {identity["class"]}
        metadata = {
            "META-INF/MANIFEST.MF",
            "META-INF/neoforge.mods.toml",
            "pack.mcmeta",
            "wda_seven_seas.png",
            identity["class"],
        }
        for name in names:
            if name.endswith("/") or name in metadata:
                continue
            assert name.startswith("data/dungeons_arise_seven_seas/")
            assert name.endswith((".json", ".nbt"))
            assert name.split("/")[2] in {"structure", "worldgen", "loot_table", "tags"}
            if "/worldgen/" in name and "/tags/" not in name:
                assert name.split("/")[3] in {"structure", "structure_set", "template_pool"}
            for kind, identifiers in groups.items():
                found = resource_identity(name, kind, ".nbt" if kind == "structure" else ".json")
                if found:
                    identifiers.add(found[0])
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    doc = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    structures = cast("dict[str, dict[str, JsonValue]]", doc["structures"])
    roots = groups["worldgen/structure"]
    assert roots <= structures.keys()
    reached_pools = {p for r in roots for p in cast("list[str]", structures[r]["pools"])}
    reached_templates = {t for r in roots for t in cast("list[str]", structures[r]["templates"])}
    assert groups["worldgen/template_pool"] <= reached_pools
    assert groups["structure"] <= reached_templates
    assert all(structures[r]["unresolved_elements"] == [] for r in roots)
    missing = {r: structures[r]["missing"] for r in roots if structures[r]["missing"]}
    assert missing == {
        "dungeons_arise_seven_seas:small_yacht": [
            {
                "kind": "template",
                "id": "dungeons_arise_seven_seas:small_yacht/small_yacht_spawner_3",
            }
        ]
    }
    assert tuple(len(groups[k]) for k in groups) == (5, 10, 36)
