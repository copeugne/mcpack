from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

import pytest
from tools.build_item8_inventory import assemble

from mcpack_evidence.item8_inventory import resource_identity, size_variant_groups
from mcpack_evidence.item8_registry import read_registry

if TYPE_CHECKING:
    from pydantic import JsonValue


@pytest.mark.parametrize("namespace", ["integrated_villages:", "dungeons_arise:"])
def test_authored_designs_bind_roots_settings_and_missing_components(
    namespace: str,
) -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    groups = [
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if str(row["family_id"]).startswith(namespace)
    ]
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    members = [member for row in groups for member in cast("list[str]", row["structure_ids"])]
    assert len(members) == len(set(members))
    expected = {key for key in registry if key.startswith(namespace)}
    assert members
    assert set(members) == expected
    catalog = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    definitions: dict[str, dict[str, JsonValue]] = {}
    for resource in cast("list[dict[str, JsonValue]]", catalog["resources"]):
        identity = resource_identity(str(resource["path"]), "worldgen/structure")
        if identity is not None and identity[0] in members:
            assert identity[1] == ""
            assert identity[0] not in definitions
            definitions[identity[0]] = cast("dict[str, JsonValue]", resource["document"])
    assert set(definitions) == set(members)
    traces = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    structures = cast("dict[str, dict[str, JsonValue]]", traces["structures"])
    if namespace == "dungeons_arise:":
        seen: set[str] = set()
        for identifier in sorted(expected):
            templates = set(cast("list[str]", structures[identifier]["templates"]))
            assert templates
            assert not seen.intersection(templates)
            seen.update(templates)
    assert len({str(row["start_pool"]) for row in groups}) == len(groups)
    for row in groups:
        identifier = str(row["family_id"])
        assert row["structure_ids"] == [identifier]
        definition = definitions[identifier]
        assert row["start_pool"] == definition["start_pool"] == structures[identifier]["start_pool"]
        assert row["generation_settings"] == {
            key: definition[key]
            for key in (
                "type",
                "start_height",
                "project_start_to_heightmap",
                "required_mods",
                "target_biomes",
                "target_biome_radius_check_blocks",
                "cannot_spawn_in_liquid",
            )
            if key in definition
        }
        assert row["missing_components"] == structures[identifier]["missing"]
        for path, digest in cast("dict[str, str]", row["evidence"]).items():
            assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest


def test_integrated_stronghold_keeps_rooms_as_components_and_binds_spawn_override() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    groups = [
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if str(row["family_id"]).startswith("integrated_stronghold:")
    ]
    assert len(groups) == 1
    group = groups[0]
    identifier = "integrated_stronghold:stronghold"
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    assert (
        group["structure_ids"]
        == [member for member in registry if member.startswith("integrated_stronghold:")]
        == [identifier]
    )
    for path, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
    catalog = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    definitions = [
        cast("dict[str, JsonValue]", row["document"])
        for row in cast("list[dict[str, JsonValue]]", catalog["resources"])
        if row["path"] == "data/integrated_stronghold/worldgen/structure/stronghold.json"
    ]
    assert len(definitions) == 1
    definition = definitions[0]
    attributes = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    assert definition["start_pool"] == group["start_pool"]
    assert definition["spawn_overrides"] == attributes["mob_source"]["structure_spawn_override"]
    assert definition["start_height"] == {
        "type": "minecraft:uniform",
        "min_inclusive": {"absolute": 15},
        "max_inclusive": {"absolute": 15},
    }
    assert definition["step"] == "strongholds"
    traces = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    trace = cast("dict[str, dict[str, JsonValue]]", traces["structures"])[identifier]
    assert trace["start_pool"] == group["start_pool"]
    assert group["missing_components"] == [
        row["id"] for row in cast("list[dict[str, str]]", trace["missing"])
    ]


def test_mineshaft_group_covers_its_runtime_variants_and_preserved_specialized_generator() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    decision = cast("list[dict[str, JsonValue]]", decisions["groups"])[0]
    evidence = cast("dict[str, str]", decision["evidence"])
    for path, digest in evidence.items():
        assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    members = cast("list[str]", decision["structure_ids"])
    assert len(members) == len(set(members))
    assert set(members) == {
        identifier for identifier in registry if identifier.startswith("bettermineshafts:")
    }
    raw = (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    definitions: dict[str, dict[str, JsonValue]] = {}
    for resource in cast("list[dict[str, JsonValue]]", catalog["resources"]):
        identity = resource_identity(str(resource["path"]), "worldgen/structure")
        if identity is not None and identity[0] in members:
            assert identity[1] == ""
            assert identity[0] not in definitions
            definitions[identity[0]] = cast("dict[str, JsonValue]", resource["document"])
    assert set(definitions) == set(members)
    for document in definitions.values():
        assert {
            key: value for key, value in document.items() if key not in {"biomes", "config"}
        } == {
            "type": "bettermineshafts:mineshaft",
            "spawn_overrides": {},
            "step": "underground_structures",
        }
    code_root = root / "evidence/item-8/sources/mineshafts-code"
    identities = cast(
        "list[dict[str, str]]", json.loads((code_root / "identities.json").read_bytes())
    )
    for row in identities:
        assert (
            hashlib.sha256((code_root / row["disassembly"]).read_bytes()).hexdigest()
            == row["disassembly_sha256"]
        )


def test_ctov_size_decisions_exactly_cover_source_proven_variant_groups() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    groups = [
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if str(row["family_id"]).startswith("ctov:")
    ]
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    raw = (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    proven = size_variant_groups(registry, cast("list[JsonValue]", catalog["resources"]))
    expected = {
        tuple(str(member["structure_id"]) for member in cast("list[dict[str, JsonValue]]", group))
        for group in proven
    }
    actual = [tuple(cast("list[str]", row["structure_ids"])) for row in groups]
    assert len(actual) == len(set(actual))
    assert set(actual) == expected
    members = [identifier for group in actual for identifier in group]
    assert len(members) == len(set(members))
    assert set(members) == {
        identifier
        for identifier in registry
        if identifier.startswith(("ctov:small/", "ctov:medium/", "ctov:large/"))
    }
    for row in groups:
        assert {
            identifier.split("/", 1)[1] for identifier in cast("list[str]", row["structure_ids"])
        } == {str(row["family_id"]).split(":", 1)[1]}
        for path, digest in cast("dict[str, str]", row["evidence"]).items():
            assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest


def test_working_inventory_keeps_unassigned_ids_and_rejects_double_counting() -> None:
    decision: dict[str, JsonValue] = {
        "family_id": "example:family",
        "name": "Example",
        "structure_ids": ["example:a"],
    }
    sources: dict[str, JsonValue] = {"structure_biomes": {"example:a": {"biomes": []}}}
    traces: dict[str, JsonValue] = {
        "structures": {},
        "untraced_structures": {"example:a": {"reason": "custom"}},
        "template_contents": {},
    }
    bounds: dict[str, JsonValue] = {"observations": []}
    result = assemble(("example:a", "example:b"), [decision], sources, traces, bounds)
    assert result["status"] == "INCOMPLETE"
    assert result["unassigned_registry_ids"] == ["example:b"]
    conflicting = dict(decision, family_id="example:second")
    with pytest.raises(ValueError, match="multiply assigned"):
        _ = assemble(("example:a",), [decision, conflicting], sources, traces, bounds)
    with pytest.raises(ValueError, match="unregistered"):
        _ = assemble(("example:b",), [decision], sources, traces, bounds)
    decision["attributes"] = {"intended_hostility": {"value": "hostile", "basis": "source"}}
    result = assemble(("example:a",), [decision], sources, traces, bounds)
    families = cast("dict[str, dict[str, JsonValue]]", result["families"])
    assert families["example:family"]["intended_hostility"] == {
        "value": "hostile",
        "basis": "source",
    }
    assert families["example:family"]["status"] == "INCOMPLETE"
    decision["attributes"] = {"status": "COMPLETE"}
    with pytest.raises(ValueError, match="protected family attribute"):
        _ = assemble(("example:a",), [decision], sources, traces, bounds)


def test_inventory_preserves_loot_kinds_and_rejects_missing_template_content() -> None:
    references: list[JsonValue] = [
        {"path": "/block_entities/0/nbt/LootTable", "value": "example:chest"},
        {"path": "/entities/0/nbt/DeathLootTable", "value": "example:chest"},
        {"path": "/block_entities/1/nbt/LootTable", "value": "example:chest"},
        {"path": "/block_entities/2/nbt/loot_tables_to_eject", "value": ["example:reward"]},
    ]
    decision: dict[str, JsonValue] = {
        "family_id": "example:family",
        "name": "Example",
        "structure_ids": ["example:a"],
    }
    sources: dict[str, JsonValue] = {"structure_biomes": {"example:a": {"biomes": []}}}
    contents: dict[str, JsonValue] = {
        "example:room": {
            "loot_references": references,
            "authored_entities": [
                {"id": "example:animal", "path": "/entities/0/nbt"},
                {"id": "example:animal", "path": "/entities/1/nbt"},
                {"id": "example:rider", "path": "/entities/1/nbt/Passengers/0"},
            ],
            "unresolved_entities": [{"path": "/entities/2/nbt", "reason": "missing ID"}],
        },
        "example:empty": {
            "loot_references": [],
            "authored_entities": [],
            "unresolved_entities": [],
        },
    }
    traces: dict[str, JsonValue] = {
        "structures": {"example:a": {"templates": ["example:room", "example:empty"]}},
        "untraced_structures": {},
        "template_contents": contents,
    }
    bounds: dict[str, JsonValue] = {"observations": []}
    result = assemble(("example:a",), [decision], sources, traces, bounds)
    families = cast("dict[str, dict[str, JsonValue]]", result["families"])
    loot = cast("dict[str, JsonValue]", families["example:family"]["loot_table_source"])
    mobs = cast("dict[str, JsonValue]", families["example:family"]["mob_source"])
    assert mobs["packaged_authored_entity_templates"] == {
        "example:animal": ["example:room"],
        "example:rider": ["example:room"],
    }
    assert mobs["unresolved_authored_entities"] == {
        "example:room": [{"path": "/entities/2/nbt", "reason": "missing ID"}]
    }
    assert loot["packaged_references"] == [
        {"field": "DeathLootTable", "value": "example:chest", "templates": ["example:room"]},
        {"field": "LootTable", "value": "example:chest", "templates": ["example:room"]},
        {
            "field": "loot_tables_to_eject",
            "value": ["example:reward"],
            "templates": ["example:room"],
        },
    ]
    assert (
        loot["status"] == "packaged possibilities; effective generation and injections unresolved"
    )
    assert families["example:family"]["status"] == "INCOMPLETE"
    del contents["example:room"]
    with pytest.raises(KeyError, match="example:room"):
        _ = assemble(("example:a",), [decision], sources, traces, bounds)


def test_seven_seas_groups_cover_registered_roots_without_counting_spawner_components() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    groups = [
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if str(row["family_id"]).startswith("dungeons_arise_seven_seas:")
    ]
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    raw = (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    traces = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    structures = cast("dict[str, dict[str, JsonValue]]", traces["structures"])
    templates = cast("dict[str, dict[str, JsonValue]]", traces["template_contents"])
    members = [member for row in groups for member in cast("list[str]", row["structure_ids"])]
    assert len(members) == len(set(members))
    assert set(members) == {key for key in registry if key.startswith("dungeons_arise_seven_seas:")}
    for row in groups:
        identifier = str(row["family_id"])
        assert row["structure_ids"] == [identifier]
        assert row["start_pool"] == structures[identifier]["start_pool"]
        main = str(row["main_template"])
        assert main in cast("list[str]", structures[identifier]["templates"])
        assert main in templates
        attributes = cast("dict[str, dict[str, JsonValue]]", row["attributes"])
        dimensions = cast("list[int]", templates[main]["template_size_xyz"])
        assert attributes["approximate_footprint"]["main_template_xz_blocks"] == [
            dimensions[0],
            dimensions[2],
        ]
        assert attributes["approximate_vertical_size"]["main_template_y_blocks"] == dimensions[1]
        loot = cast("list[dict[str, JsonValue]]", templates[main]["loot_references"])
        assert set(
            cast("list[str]", attributes["loot_table_source"]["packaged_container_tables"])
        ) == {str(reference["value"]) for reference in loot}
        initial_types: set[str] = set()
        potential_types: set[str] = set()
        for template in cast("list[str]", structures[identifier]["templates"]):
            for block in cast("list[dict[str, JsonValue]]", templates[template]["spawner_blocks"]):
                nbt = cast("dict[str, JsonValue]", block["nbt"])
                initial_types.add(
                    cast("dict[str, dict[str, str]]", nbt["SpawnData"])["entity"]["id"]
                )
                for potential in cast("list[dict[str, JsonValue]]", nbt["SpawnPotentials"]):
                    if cast("int", potential["weight"]) > 0:
                        potential_types.add(
                            cast("dict[str, dict[str, str]]", potential["data"])["entity"]["id"]
                        )
        assert (
            initial_types
            == potential_types
            == set(cast("list[str]", attributes["mob_source"]["authored_spawner_types"]))
        )
        assert initial_types == set(
            cast("list[str]", attributes["generated_spawners"]["authored_types"])
        )
        missing = cast("list[dict[str, str]]", structures[identifier]["missing"])
        assert attributes["generated_spawners"]["missing_components"] == [
            entry["id"] for entry in missing
        ]
        for path, digest in cast("dict[str, str]", row["evidence"]).items():
            assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
