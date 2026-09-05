"""Assemble the working family inventory with uv run -m tools.build_item8_inventory."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_templates import spawner_entity_sources

if TYPE_CHECKING:
    from pydantic import JsonValue

ROOT = Path(__file__).resolve().parents[1]
SOURCES = "evidence/item-8/sources/structure-inputs.json"
TRACES = "evidence/item-8/sources/pool-traces-content.json.gz"
BOUNDS = "evidence/item-8/sources/world-bounds.json.gz"
DECISIONS = "evidence/item-8/family-decisions.json"
REGISTRY = "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
DIMENSION_BIOMES = "evidence/item-8/runtime/dimension-r3/dimension-biomes.json"
INPUTS = {
    SOURCES: "fcd9e53c1802b8ab2f03785baacce7a032ae525446f24e1172dbdeee868367ef",
    TRACES: "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5",
    BOUNDS: "fd8ebda1d1778b51c312cb98734248ce8c8ead623b201d79943df05ff36f169b",
    DECISIONS: "70c5eb1359d86e22045d9a34d3d5816cabdfc3449d7f481b6156c590328e5d81",
    REGISTRY: "9d245430730173e9ce5304317a7476e7ecd4267d208b25a16a0d7b2cf3f16941",
    DIMENSION_BIOMES: "08fa8185cd2c3f54b5255b2e8f86946c4b37ed471fb1991d0f82c835ffe20c7c",
}


def _spawner_sources(
    templates: list[str], template_contents: dict[str, dict[str, JsonValue]]
) -> dict[str, JsonValue]:
    spawner_sources: dict[tuple[str, str, str], set[str]] = {}
    unresolved_spawners: dict[str, list[JsonValue]] = {}
    for template in templates:
        for block in cast(
            "list[dict[str, JsonValue]]", template_contents[template]["spawner_blocks"]
        ):
            nbt = cast("dict[str, JsonValue]", block["nbt"])
            block_id = cast("str | None", block.get("block_id"))
            for source in spawner_entity_sources(nbt, block_id=block_id):
                if "entity_id" in source:
                    source_key = (
                        str(nbt.get("id", block_id)), str(source["mode"]), str(source["entity_id"])
                    )
                    spawner_sources.setdefault(source_key, set()).add(template)
                else:
                    unresolved_spawners.setdefault(template, []).append(
                        {"block_path": block["path"], **source}
                    )
    return {
        "packaged_entity_sources": cast(
            "JsonValue",
            [
                {
                    "spawner_id": kind,
                    "mode": mode,
                    "entity_id": entity,
                    "templates": sorted(owners),
                }
                for (kind, mode, entity), owners in sorted(spawner_sources.items())
            ],
        ),
        "unresolved_sources": cast("JsonValue", unresolved_spawners),
        "generation_marker_templates": [
            template for template in templates if template_contents[template]["generation_markers"]
        ],
    }


def assemble(  # noqa: C901, PLR0913, PLR0917 - keep explicit evidence joins in one assembly pass.
    registry: tuple[str, ...],
    decisions: list[dict[str, JsonValue]],
    sources: dict[str, JsonValue],
    traces: dict[str, JsonValue],
    bounds: dict[str, JsonValue],
    dimension_biomes: dict[str, list[str]],
) -> dict[str, JsonValue]:
    """Join resolved groups without treating unassigned IDs or unknown attributes as complete."""
    families: dict[str, JsonValue] = {}
    assigned: set[str] = set()
    constraints = cast("dict[str, JsonValue]", sources["structure_biomes"])
    pool_traces = cast("dict[str, dict[str, JsonValue]]", traces["structures"])
    custom = cast("dict[str, JsonValue]", traces["untraced_structures"])
    template_contents = cast("dict[str, dict[str, JsonValue]]", traces["template_contents"])
    observations = cast("list[dict[str, JsonValue]]", bounds["observations"])
    for decision in decisions:
        family = str(decision["family_id"])
        members = cast("list[str]", decision["structure_ids"])
        if family in families or not members or len(members) != len(set(members)):
            message = f"duplicate family or invalid member list: {family}"
            raise ValueError(message)
        if set(members) - set(registry) or assigned.intersection(members):
            message = f"unregistered or multiply assigned structure: {family}"
            raise ValueError(message)
        assigned.update(members)
        templates = sorted(
            {
                template
                for member in members
                if member in pool_traces
                for template in cast("list[str]", pool_traces[member]["templates"])
            }
        )
        world_rows = [
            index for index, row in enumerate(observations) if row["structure_id"] in members
        ]
        dimensions = sorted({str(observations[index]["dimension"]) for index in world_rows})
        compatible_dimensions: dict[str, JsonValue] = {}
        for member in members:
            constraint = cast("dict[str, JsonValue]", constraints[member])
            biomes = cast("list[str] | None", constraint.get("biomes"))
            if (
                biomes is None
                or constraint.get("missing_required")
                or constraint.get("unresolved_tags")
            ):
                compatible_dimensions[member] = "UNKNOWN: biome constraints are unresolved"
            else:
                compatible_dimensions[member] = cast(
                    "JsonValue", sorted(
                        dimension for dimension, possible in dimension_biomes.items()
                        if set(biomes).intersection(possible)
                    )
                )
        observed_sizes = [
            cast("list[int]", observations[index]["size_xyz"])
            for index in world_rows
            if observations[index]["chunk_full"] is True
        ]
        geometry_basis = (
            "Saved-piece envelopes from linked world_observations with chunk_full=true. "
            "Approximate layout extents in blocks, including air and piece padding. "
            "Full start chunks do not prove all component chunks were populated. "
            "Observed samples only, not family-wide bounds or occupied geometry."
        )
        loot_sources: dict[tuple[str, str], list[str]] = {}
        authored_sources: dict[str, list[str]] = {}
        for template in templates:
            entities = cast(
                "list[dict[str, JsonValue]]", template_contents[template]["authored_entities"]
            )
            for entity in entities:
                entity_owners = authored_sources.setdefault(str(entity["id"]), [])
                if template not in entity_owners:
                    entity_owners.append(template)
            references = cast(
                "list[dict[str, JsonValue]]", template_contents[template]["loot_references"]
            )
            for reference in references:
                key = (
                    str(reference["path"]).rsplit("/", 1)[-1],
                    json.dumps(reference["value"], sort_keys=True),
                )
                owners = loot_sources.setdefault(key, [])
                if template not in owners:
                    owners.append(template)
        content: dict[str, JsonValue] = {
            "artifact": TRACES,
            "template_ids": cast("JsonValue", templates),
            "custom_generation": {member: custom[member] for member in members if member in custom},
            "status": "packaged possibilities; effective generation and injections unresolved",
        }
        family_row: dict[str, JsonValue] = {
            "name": decision["name"],
            "structure_ids": cast("JsonValue", members),
            "grouping_decision": decision,
            "status": "INCOMPLETE",
            "dimension": {
                "observed": cast("JsonValue", dimensions),
                "biome_compatible_by_structure": compatible_dimensions,
                "artifact": DIMENSION_BIOMES,
                "eligibility": (
                    "Biome overlap only. Structure-set selection, custom-generator "
                    "conditions and effective structure constraints remain to be reconciled. "
                    "An empty match is not an observed generation failure."
                ),
            },
            "biome_constraints": {member: constraints[member] for member in members},
            "approximate_footprint": (
                {
                    "observed_envelope_xz_blocks": cast(
                        "JsonValue",
                        [list(pair) for pair in sorted({(s[0], s[2]) for s in observed_sizes})],
                    ),
                    "basis": geometry_basis,
                }
                if observed_sizes
                else "UNKNOWN: no retained full-start-chunk envelope observation"
            ),
            "approximate_vertical_size": (
                {
                    "observed_envelope_y_blocks": cast(
                        "JsonValue", sorted({s[1] for s in observed_sizes})
                    ),
                    "basis": geometry_basis,
                }
                if observed_sizes
                else "UNKNOWN: no retained full-start-chunk envelope observation"
            ),
            "intended_hostility": "UNKNOWN",
            "mob_source": {
                **content,
                "packaged_authored_entity_templates": cast(
                    "JsonValue", dict(sorted(authored_sources.items()))
                ),
                "unresolved_authored_entities": {
                    template: template_contents[template]["unresolved_entities"]
                    for template in templates
                    if template_contents[template]["unresolved_entities"]
                },
                "authored_entity_scope": (
                    "Base IDs of template entities and passengers, including non-mob entities. "
                    "Not a hostile-enemy classification or spawned population."
                ),
                "fields": [
                    "authored_entities",
                    "spawner_blocks",
                    "generation_markers",
                    "unresolved_entities",
                ],
            },
            "loot_table_source": {
                **content,
                "fields": ["loot_references"],
                "packaged_references": [
                    {
                        "field": field,
                        "value": cast("JsonValue", json.loads(value)),
                        "templates": cast("JsonValue", owners),
                    }
                    for (field, value), owners in sorted(loot_sources.items())
                ],
            },
            "generated_spawners": {
                **content,
                "fields": ["spawner_blocks", "generation_markers"],
                **_spawner_sources(templates, template_contents),
                "source_scope": (
                    "Explicit base entity IDs from initial data and positive-weight potentials. "
                    "Not generated counts, passenger attribution or effective processor results. "
                    "Generation markers require separate interpretation."
                ),
            },
            "authored_or_natural_enemies": (
                "UNKNOWN: requires generation and natural-spawn disposition"
            ),
            "visual_discoverability": "UNKNOWN",
            "underground_surface_classification": "UNKNOWN",
            "world_observations": {
                "artifact": BOUNDS,
                "observation_indexes": cast("JsonValue", world_rows),
            },
            "pool_trace_ids": [member for member in members if member in pool_traces],
        }
        attributes = cast("dict[str, JsonValue]", decision.get("attributes", {}))
        protected = {
            "name",
            "structure_ids",
            "grouping_decision",
            "status",
            "world_observations",
            "pool_trace_ids",
        }
        if attributes.keys() - family_row.keys() or attributes.keys() & protected:
            message = f"unknown or protected family attribute: {family}"
            raise ValueError(message)
        family_row.update(attributes)
        families[family] = family_row
    return {
        "status": "INCOMPLETE",
        "scope": (
            "Working family inventory. Group relationships, provider coverage and attributes "
            "remain unresolved. Not a canonical total or exit-gate pass."
        ),
        "families": families,
        "unassigned_registry_ids": cast("JsonValue", sorted(set(registry) - assigned)),
        "non_registry_content": (
            "UNKNOWN: feature structures and injected village buildings need explicit relationships"
        ),
    }


def main() -> None:
    """Bind the delivered source files and write the reviewable working inventory."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--output", type=Path, required=True)
    output = cast("Path", parser.parse_args().output)
    documents: dict[str, dict[str, JsonValue]] = {}
    for relative, digest in INPUTS.items():
        raw = (ROOT / relative).read_bytes()
        if hashlib.sha256(raw).hexdigest() != digest:
            message = f"inventory source identity mismatch: {relative}"
            raise ValueError(message)
        if relative != REGISTRY:
            documents[relative] = cast(
                "dict[str, JsonValue]",
                json.loads(gzip.decompress(raw) if relative.endswith(".gz") else raw),
            )
    result = assemble(
        read_registry(ROOT / REGISTRY),
        cast("list[dict[str, JsonValue]]", documents[DECISIONS]["groups"]),
        documents[SOURCES],
        documents[TRACES],
        documents[BOUNDS],
        cast("dict[str, list[str]]", documents[DIMENSION_BIOMES]),
    )
    result["non_registry_content"] = documents[DECISIONS]["non_registry_content"]
    result["inputs"] = dict(INPUTS)
    with output.open("x", encoding="utf-8") as stream:
        _ = stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("Working inventory written; completion remains unproven")


if __name__ == "__main__":
    main()
