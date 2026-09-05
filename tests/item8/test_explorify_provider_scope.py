from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_explorify_full_archive_candidate_boundary() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "Explorify v1.6.5.mod.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    metadata = {
        "META-INF/mods.toml",
        "META-INF/neoforge.mods.toml",
        "fabric.mod.json",
        "pack.mcmeta",
        "pack.png",
    }
    templates: set[str] = set()
    pools: set[str] = set()
    roots: set[str] = set()
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        files = {n for n in names if not n.endswith("/")}
        assert len(files) == 477
        for path in sorted(files - metadata):
            if path.endswith(".nbt"):
                assert path.startswith(("data/explorify/structure/", "data/explorify/structures/"))
                if "/structures/" in path:
                    assert archive.read(path) == archive.read(
                        path.replace("/structures/", "/structure/")
                    )
                else:
                    templates.add(
                        "explorify:" + path.removeprefix("data/explorify/structure/")[:-4]
                    )
                continue
            assert path.endswith(".json")
            doc = cast("dict[str, JsonValue]", json.loads(archive.read(path)))
            if path.startswith("data/explorify/worldgen/"):
                kind = path.split("/")[3]
                assert kind in {"structure", "structure_set", "template_pool", "processor_list"}
                identifier = "explorify:" + "/".join(path.split("/")[4:])[:-5]
                if kind == "structure":
                    assert doc["type"] == "minecraft:jigsaw"
                    roots.add(identifier)
                if kind == "template_pool":
                    pools.add(identifier)
            else:
                assert path.startswith(
                    (
                        "data/explorify/tags/worldgen/biome/",
                        "data/explorify/loot_table/",
                        "data/explorify/loot_tables/",
                        "data/cristellib/structure_configs/",
                        "f15/data/explorify/worldgen/processor_list/",
                        "f41/data/explorify/loot_tables/",
                    )
                ), path
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    trace = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    structures = cast("dict[str, dict[str, JsonValue]]", trace["structures"])
    assert roots <= structures.keys()
    assert all(structures[r]["missing"] == [] for r in roots)
    assert all(structures[r]["unresolved_elements"] == [] for r in roots)
    reached_pools = {p for r in roots for p in cast("list[str]", structures[r]["pools"])}
    reached_templates = {t for r in roots for t in cast("list[str]", structures[r]["templates"])}
    disconnected_pools = {
        f"explorify:watchtower/{v}/{p}"
        for v in ("plains", "savanna", "taiga")
        for p in ("base_plate", "feature_plate", "features", "tower")
    }
    disconnected_pools.add("explorify:bastion_spiral/bridge_end")
    disconnected_templates = {
        f"explorify:watchtower/{v}/{p}"
        for v in ("plains", "savanna", "taiga")
        for p in (
            "base_plate/whole",
            "feature_plate/whole",
            "tower/whole",
            "features/campfire",
            "features/coal_pile",
            "features/hay_pile",
            "features/logs",
            "features/resource_pile",
        )
    }
    disconnected_templates.update(
        "explorify:" + p
        for p in (
            "bastion_spiral/bridge/long",
            "bastion_spiral/bridge/whole",
            "bastion_spiral/bridge_end/whole",
            "campsite/tent/09",
            "campsite/tent/10",
            "tavern/back/06",
        )
    )
    assert pools - reached_pools == disconnected_pools
    assert templates - reached_templates == disconnected_templates
    assert (len(roots), len(pools), len(templates)) == (23, 57, 165)
