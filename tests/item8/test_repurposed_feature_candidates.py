from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue

DUNGEONS = (
    "badlands", "dark_forest", "deep", "desert", "end", "icy", "jungle", "mushroom",
    "nether", "ocean_cold", "ocean_frozen", "ocean_lukewarm", "ocean_neutral", "ocean_warm",
    "snow", "swamp",
)
WELLS = ("badlands", "cherry", "forest", "mossy_stone", "mushroom", "nether", "snow")


def test_repurposed_nonregistry_nbt_candidates() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name.startswith("repurposed_structures-"))
    assert source.sha256 == "aeb473f0a0a0632cea089377cdd9f66c42cf6f97557fd32c368ac40635285dd2"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    expected = {"dungeons/" + n: "nbt_dungeon" for n in DUNGEONS} | {
        "wells/" + n: "nbt_feature" for n in WELLS
    }
    prefix = "data/repurposed_structures/worldgen/"
    with ZipFile(source.path) as archive:
        configs = {
            n.removeprefix(prefix + "configured_feature/").removesuffix(".json"):
            cast("dict[str, JsonValue]", json.loads(archive.read(n)))
            for n in archive.namelist()
            if n.startswith(prefix + "configured_feature/") and n.endswith(".json")
        }
        selected = {k: d for k, d in configs.items() if d["type"] in {
            "repurposed_structures:nbt_dungeon", "repurposed_structures:nbt_feature",
        }}
        assert set(selected) == set(expected)
        for candidate, kind in expected.items():
            assert selected[candidate]["type"] == "repurposed_structures:" + kind
            config = cast("dict[str, JsonValue]", selected[candidate]["config"])
            entries = cast("list[dict[str, JsonValue]]", config[
                "dungeon_nbt_entries" if kind == "nbt_dungeon" else "nbt_entries"
            ])
            assert entries
            for entry in entries:
                namespace, path = cast("str", entry["resourcelocation"]).split(":", 1)
                assert f"data/{namespace}/structure/{path}.nbt" in archive.namelist()
            placed = cast("dict[str, JsonValue]", json.loads(archive.read(
                prefix + "placed_feature/" + candidate + ".json"
            )))
            assert placed["feature"] == "repurposed_structures:" + candidate
            modifier = cast("dict[str, JsonValue]", json.loads(archive.read(
                "data/repurposed_structures/neoforge/biome_modifier/" + candidate + ".json"
            )))
            assert modifier["feature"] == "repurposed_structures:" + candidate
            assert modifier["type"] in {
                "repurposed_structures:additions_modifier",
                "repurposed_structures:additions_temperature_modifier",
            }


def test_repurposed_existing_graph_partition() -> None:
    # Partition existing evidence; outside a graph does not mean unused or a new family.
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name.startswith("repurposed_structures-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == (
        "aeb473f0a0a0632cea089377cdd9f66c42cf6f97557fd32c368ac40635285dd2"
    )
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = {k: v for k, v in cast(
        "dict[str, dict[str, JsonValue]]", document["structures"]
    ).items() if k.startswith("repurposed_structures:")}
    assert len(traces) == 95
    with ZipFile(source.path) as archive:
        groups = {
            kind: {identity[0] for name in archive.namelist()
                   if (identity := resource_identity(name, kind, extension)) is not None}
            for kind, extension in (
                ("worldgen/structure", ".json"), ("worldgen/template_pool", ".json"),
                ("structure", ".nbt"),
            )
        }
    assert len(groups["worldgen/structure"]) == 107
    assert groups["worldgen/structure"] - traces.keys() == {
        "repurposed_structures:mansion_" + n for n in (
            "birch", "desert", "jungle", "mangrove", "oak", "savanna", "snowy", "taiga",
        )
    } | {"repurposed_structures:monument_" + n for n in ("desert", "icy", "jungle", "nether")}
    for kind, field, total, outside_counts in (
        ("worldgen/template_pool", "pools", 1099,
         {"mansions": 416, "monuments": 80, "cities": 2, "villages": 5}),
        ("structure", "templates", 3162, {
            "mansions": 597, "monuments": 92, "dungeons": 36, "wells": 7,
            "ancient_cities": 3, "bastions": 5, "mineshafts": 16,
            "strongholds": 2, "villages": 27,
        }),
    ):
        assert len(groups[kind]) == total
        reached = {r for t in traces.values() for r in cast("list[str]", t[field])}
        outside = groups[kind] - reached
        assert Counter(n.split(":", 1)[1].split("/", 1)[0] for n in outside) == outside_counts
    assert all(t["missing"] == [] for t in traces.values())
    assert all(t["unresolved_elements"] == [] for t in traces.values())


def test_repurposed_residual_component_links() -> None:  # noqa: PLR0915
    """Distinguish template consumers from equal-named pools and count limits."""
    raw = Path("evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705"
    )
    catalog = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(raw)))
    templates = {identity[0]: cast("dict[str, JsonValue]", r["document"])
                 for r in catalog["resources"]
                 if (identity := resource_identity(str(r["path"]), "structure", ".nbt"))
                 and identity[0].startswith("repurposed_structures:")}
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name.startswith("repurposed_structures-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == (
        "aeb473f0a0a0632cea089377cdd9f66c42cf6f97557fd32c368ac40635285dd2"
    )
    prefix = "data/repurposed_structures/"
    namespace = "repurposed_structures:"
    with ZipFile(source.path) as archive:
        documents = {n: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
                     for n in archive.namelist()
                     if n.startswith(prefix + "worldgen/") and n.endswith(".json")}
        for variant in ("nether", "overworld"):
            path = prefix + f"worldgen/template_pool/cities/{variant}/no_stair_room.json"
            document = documents[path]
            assert document["fallback"] == namespace + f"cities/{variant}/no_stair_room"
            elements = cast("list[dict[str, JsonValue]]", document["elements"])
            assert {str(cast("dict[str, JsonValue]", e["element"])["location"])
                    for e in elements} == {
                namespace + f"cities/{variant}/" + n
                for n in ("large_room_ns", "medium_room_ns", "tiny_room_ns", "bridge_end")
            }
        tree_features = {
            "cherry": namespace + "cherry_bees_05", "giant_taiga": "minecraft:mega_pine_checked",
            "mountains": "minecraft:pine", "swamp": namespace + "swamp_tree_checked",
        }
        for variant, feature in tree_features.items():
            document = documents[prefix + f"worldgen/template_pool/villages/{variant}/trees.json"]
            assert document["fallback"] == "minecraft:empty"
            assert document["elements"] == [{"weight": 1, "element": {
                "element_type": "minecraft:feature_pool_element", "feature": feature,
                "projection": "rigid",
            }}]
        path = prefix + "worldgen/template_pool/villages/giant_taiga/zombie/terminators.json"
        document = documents[path]
        assert document["fallback"] == "minecraft:empty"
        entries = cast("list[dict[str, JsonValue]]", document["elements"])
        assert {str(cast("dict[str, JsonValue]", e["element"])["location"])
                for e in entries} == {
            namespace + f"villages/giant_taiga/terminators/terminator_0{i}" for i in range(1, 5)
        }
        minecarts = {n: d for n, d in documents.items()
                     if d.get("type") == namespace + "mineshaft_minecarts"}
        assert len(minecarts) == 16
        for document in minecarts.values():
            config = cast("dict[str, JsonValue]", document["config"])
            template = templates[str(config["minecart_nbt_file"])]
            assert template["size"] == [1, 1, 1]
            entities = cast("list[dict[str, JsonValue]]", template["entities"])
            assert len(entities) == 1
            entity = cast("dict[str, JsonValue]", entities[0]["nbt"])
            assert entity["id"] == "minecraft:chest_minecart"
        # A matching pool ID is not a reference to the same-named NBT file.
        locations = {str(cast("dict[str, JsonValue]", e["element"]).get("location"))
                     for n, d in documents.items() if "/template_pool/" in n
                     for e in cast("list[dict[str, JsonValue]]", d["elements"])}
        for variant in ("end", "nether", "ocean"):
            key = namespace + f"ancient_cities/{variant}/city_center/walls/bottom_right_corner"
            assert key in templates
            assert key not in locations
            assert {key + "_1", key + "_2"} <= locations
        for variant in ("end", "nether"):
            key = namespace + f"strongholds/{variant}/crossing"
            assert key in templates
            assert key not in locations
            start = templates[namespace + f"strongholds/{variant}/start_stairs"]
            blocks = cast("list[dict[str, JsonValue]]", start["block_entities"])
            assert any(cast("dict[str, JsonValue]", b["nbt"]).get("pool") == key
                       for b in blocks)
            counts = cast("dict[str, JsonValue]", json.loads(archive.read(
                prefix + f"rs_pieces_spawn_counts/stronghold_{variant}.json"
            )))
            limits = cast("list[dict[str, JsonValue]]", counts["pieces_spawn_counts"])
            assert next(e for e in limits if e["nbt_piece_name"] == key) == {
                "nbt_piece_name": key, "never_spawn_more_than_this_many": 7,
            }
        raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == (
            "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
        )
        graph = cast("dict[str, dict[str, dict[str, JsonValue]]]",
                     json.loads(gzip.decompress(raw)))["structures"]
        reached = {str(t) for key, trace in graph.items() if key.startswith(namespace)
                   for t in cast("list[str]", trace["templates"])}
        remaining = {k for k in templates if k not in reached
                     and k.split(":", 1)[1].split("/", 1)[0] in {"bastions", "villages"}}
        assert len(remaining) == 32
        assert remaining.isdisjoint(locations)
        entrance = templates[namespace + "bastions/underground/bridge/starting_pieces/entrance"]
        blocks = cast("list[dict[str, JsonValue]]", entrance["block_entities"])
        assert any(cast("dict[str, JsonValue]", b["nbt"]).get("pool") ==
                   namespace + "bastions/underground/mobs/skeleton_horse" for b in blocks)
        for key in remaining:
            parts = key.split(":", 1)[1].split("/")
            if parts[0] == "bastions":
                assert parts[:3] == ["bastions", "underground", "mobs"]
                template = templates[key]
                palette = cast("list[dict[str, JsonValue]]", template["palette"])
                assert {str(p["Name"]) for p in palette} == {"minecraft:air", "minecraft:jigsaw"}
                entities = cast("list[dict[str, JsonValue]]", template["entities"])
                assert len(entities) == 1
                entity = cast("dict[str, JsonValue]", entities[0]["nbt"])
                assert entity["id"] in {"minecraft:skeleton", "minecraft:skeleton_horse"}
            else:
                assert prefix + f"worldgen/structure/village_{parts[1]}.json" in documents
                assert any(p in {"houses", "streets", "villagers", "mobs"} for p in parts[2:])


def test_repurposed_complete_feature_type_partition() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name.startswith("repurposed_structures-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == (
        "aeb473f0a0a0632cea089377cdd9f66c42cf6f97557fd32c368ac40635285dd2"
    )
    folder = Path("evidence/item-8/sources/repurposed-feature-roles")
    raw = (folder / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "4e90a8ed5ea83a2db56830de2cd50d5dc2c5ed1149eb0d0ad06477eed7409230"
    )
    identities = cast("list[dict[str, str]]", json.loads(raw))
    with ZipFile(source.path) as archive:
        feature_prefix = "com/telepathicgrunt/repurposedstructures/world/features/"
        feature_classes = {n for n in archive.namelist() if n.endswith(".class")
                           and n.startswith(feature_prefix)
                           and "/configs/" not in n}
        assert feature_classes - {i["class"] for i in identities} == {
            "com/telepathicgrunt/repurposedstructures/world/features/NbtDungeon.class",
            "com/telepathicgrunt/repurposedstructures/world/features/NbtFeature.class",
        }
        assert len(identities) == 31
        for identity in identities:
            assert identity["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(identity["class"])).hexdigest() == (
                identity["class_sha256"]
            )
            assert hashlib.sha256((folder / identity["disassembly"]).read_bytes()).hexdigest() == (
                identity["disassembly_sha256"]
            )
        configs = {n: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
                   for n in archive.namelist() if n.endswith(".json")
                   and n.startswith("data/repurposed_structures/worldgen/configured_feature/")}
        assert len(configs) == 136
        expected = {"minecraft:" + k: v for k, v in {
            "block_pile": 1, "coral_claw": 1, "coral_tree": 2,
            "no_bonemeal_flower": 1, "random_patch": 3, "tree": 2,
        }.items()} | {"repurposed_structures:" + k: v for k, v in {
            "configurable_coral_claw": 1, "configurable_coral_mushroom": 1,
            "configurable_coral_tree": 1, "drowned_with_armor": 1,
            "mineshaft_minecarts": 16, "mineshaft_supports": 31, "nbt_dungeon": 16,
            "nbt_feature": 7, "ocean_temperature_random_selector": 1,
            "post_process_connecting_blocks": 1, "shulker_mob": 1,
            "simple_block_with_fluid_tick": 2, "skeleton": 6, "skeleton_horseman": 2,
            "structure_breakage": 1, "structure_chains": 1, "structure_chorus": 2,
            "structure_crimson_plants": 3, "structure_end_rod_chains": 1, "structure_fire": 4,
            "structure_flowers": 1, "structure_grass": 1, "structure_netherwart": 1,
            "structure_powder_snow": 1, "structure_seagrass": 4, "structure_vine_breakage": 1,
            "structure_vines": 9, "structure_vines_and_leaves": 1, "structure_warped_plants": 3,
            "underwater_block_pile": 4, "wither_skeleton_with_bow": 1,
        }.items()}
        assert Counter(str(d["type"]) for d in configs.values()) == expected
        selector = next(d for d in configs.values()
                        if d["type"] == "repurposed_structures:ocean_temperature_random_selector")
        assert selector["config"] == {
            temperature + "_features": ["repurposed_structures:villages/" + prefix + shape
                                         for shape in ("tree", "claw", "mushroom")]
            for temperature, prefix in (("warm", "coral_"), ("cold", "dead_coral_"))
        }
