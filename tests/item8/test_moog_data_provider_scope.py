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
    ("MoogsVoyagerStructures-1.21-5.0.11.jar", "mvs", (129, 149, 327, 92)),
    ("MoogsNetherStructures-1.21-3.0.0-alpha.2.jar", "mns", (52, 168, 459, 171)),
])
def test_complete_moog_data_scope(  # noqa: C901, PLR0912, PLR0915 - explicit archive cases.
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
            if namespace == "mns" and name_in_archive.startswith("data/moogs_structures/"):
                assert name_in_archive in {
                    "data/moogs_structures/tags/worldgen/structure/no_basalt.json",
                    "data/moogs_structures/tags/worldgen/structure/no_delta.json"}
                continue
            assert path.parts[:2] == ("data", namespace), name_in_archive
            if path.parts[2] == "structure":
                assert path.suffix == ".nbt"
                templates.add(namespace + ":" + "/".join(path.parts[3:])[:-4])
                continue
            assert path.suffix == ".json"
            document = cast("dict[str, JsonValue]", json.loads(archive.read(name_in_archive)))
            if path.parts[2] == "worldgen":
                assert path.parts[3] in {
                    "structure", "structure_set", "template_pool", "processor_list"}
                if path.parts[3] == "structure":
                    roots.add(namespace + ":" + "/".join(path.parts[4:])[:-5])
                    assert isinstance(document["start_pool"], str)
                if path.parts[3] == "processor_list":
                    allowed = {"minecraft:rule"} if namespace == "mvs" else {
                        "moogs_structures:pillar_processor",
                        "moogs_structures:spawner_randomizing_processor",
                        "moogs_structures:trial_spawner_randomizing_processor",
                        "moogs_structures:vault_randomizing_processor",
                        "moogs_structures:equip_armor_stand_processor"}
                    assert namespace in {"mvs", "mns"}
                    assert all(p["processor_type"] in allowed for p in
                               cast("list[dict[str, JsonValue]]", document["processors"]))
            elif path.parts[2] == "tags":
                assert path.parts[3:5] == ("worldgen", "biome")
            else:
                assert path.parts[2] in {"loot_table", "trial_spawner"}
                if path.parts[2] == "trial_spawner":
                    assert namespace == "mns"
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
    assert all(structures[root]["missing"] == [] for root in roots)
    assert all(structures[root]["unresolved_elements"] == [] for root in roots)
    reached_pools = {p for root in roots for p in
                     cast("list[str]", structures[root]["pools"])}
    reached_templates = {t for root in roots for t in
                         cast("list[str]", structures[root]["templates"])}
    disconnected_pools: set[str] = set()
    if namespace == "mns":
        disconnected_pools = {"mns:" + suffix for suffix in (
            "dragon_arena/lower_14", "mega_arenas/mobs/arena_bowman",
            "mega_arenas/mobs/ember_sentinel", "mega_arenas/mobs/pit_vanguard",
            "mega_fortress/crossings/small/small_crossing_2_east",
            "mega_fortress/crossings/small/small_crossing_2_north",
            "mega_fortress/crossings/small/small_crossing_2_south",
            "mega_fortress/crossings/small/small_crossing_2_west",
            "mega_fortress/mobs/blaze_sentinel", "mega_fortress/mobs/fortress_guard",
            "mega_fortress/start/start_crossing_north", "very_small_nether_brick_start_pool",
        )}
    assert {cast("str", link["id"]) for link in links} - reached_pools == disconnected_pools
    excluded_by_version = {cast("str", edge["id"]) for link in links for edge in
                           cast("list[dict[str, JsonValue]]", link["edges"])
                           if edge["kind"] == "template" and edge.get("selected") is False}
    disconnected: set[str] = set()
    if namespace == "mvs":
        disconnected = {"mvs:" + suffix for suffix in (
            "animals/cat_black", "animals/cat_british_shorthair", "animals/cat_calico",
            "animals/cat_jellie", "animals/cat_persian", "animals/cat_ragdoll",
            "animals/cat_red", "animals/cat_siamese", "animals/cat_tabby",
            "animals/cat_tuxedo", "animals/cat_white", "animals/cows_1",
            "animals/horses_1", "animals/horses_2", "animals/horses_3", "animals/horses_4",
            "animals/horses_5", "animals/mule", "animals/pigs_1", "animals/sheep_1",
            "animals/sheep_2", "armor_stand/armor_stand_1", "armor_stand/armor_stand_2",
            "armor_stand/armor_stand_3", "armor_stand/armor_stand_4", "cathedral/cathedral_start",
            "cathedral/corridors/corridor_8", "houses/medium_igloo_2",
            "houses/medium_igloo_2_lower", "mineshaft/barrels_1", "mineshaft/barrels_2",
            "mineshaft/barrels_3", "mineshaft/barrels_4", "mineshaft/cart_1", "mineshaft/cart_2",
            "mineshaft/cart_3", "mineshaft/dead_end_1", "mineshaft/logs_1", "mineshaft/logs_2",
            "mineshaft/round_staircase_3", "mineshaft/stable",
        )}
        all_pool_references = {cast("str", edge["id"]) for link in links for edge in
                               cast("list[dict[str, JsonValue]]", link["edges"])
                               if edge["kind"] == "template"}
        assert templates - all_pool_references == disconnected
    if namespace == "mns":
        disconnected = {"mns:" + suffix for suffix in (
            "dragon_arena/lower_14", "large_arena/v1_21_4/l2", "large_arena/v1_21_4/r2",
            "large_arena/v1_21_5/l2", "large_arena/v1_21_5/r2", "large_arena/v1_21_9/l2",
            "large_arena/v1_21_9/r2", "mega_fortress/corridors/roofed_long_straight_2",
            "ruins/very_small_nether_brick_1",
        )}
    assert templates - reached_templates - excluded_by_version == disconnected
    assert (len(roots), len(links), len(templates), len(templates - reached_templates)) == counts
