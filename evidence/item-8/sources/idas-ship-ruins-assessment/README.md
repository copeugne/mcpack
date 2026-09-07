# IDAS detached ship ruins assessment

Nine entries integrated for one family/two independent wreckage alternatives.
Exact template sizes are8 by6 by9 and12 by5 by12 in x,y,z. Nominal dimensions
need no new runtime capture; these are not two joined ship components.

## mob_source

Two independent wreckage templates have no authored entities, unresolved entity compounds or generation markers. The selected sunken_ship_processor randomizes existing SpawnerBlock inputs; neither template supplies one. A processor list name is not an authored enemy source here.

## loot_table_source

Both alternatives reference defined idas:chests/sunken_ship/sunken_ship_supply and idas:chests/sunken_ship/sunken_ship_treasure. Selected spawner processor does not append container loot. Shared tables do not merge these detached wreckage alternatives with the separate long-hull ship family; source references are not measured rewards.

## generated_spawners

No ordinary or trial spawner blocks or generation markers in either template. Selected Integrated API spawner_randomizing_processor acts on SpawnerBlock inputs and does not turn unrelated wreckage blocks into spawners. Its idas:sunken_ship list is therefore not evidence of a spawner encounter in these templates.

## authored_or_natural_enemies

No authored entities or spawners; root spawn_overrides is empty. No family-specific authored encounter or natural override is identified. Ordinary ocean/environmental spawning remains possible; absent template enemies do not guarantee a safe site.

## intended_hostility

Small submerged wreckage/cache design with supply and treasure loot but no identified authored hostile encounter source. Underwater access is an environmental constraint; no measured combat intensity, successful guard population or difficulty tier is assigned.

## visual_discoverability

Detached wreckage and loot-bearing barrels provide local seabed cues, distinct from the larger mast/deck hull family. Water, terrain and debris can obscure the small structures. No surface marker, visibility distance or guaranteed visible cache is established.

## underground_surface_classification

Seabed/submerged intent: generic_structure root uses OCEAN_FLOOR_WG, LOWEST_CORNER, offset0, apply_waterlogging, size1, beard_box and biome radius1. These are placement inputs, not measured water depth, burial fraction or final terrain extent.

## Evidence

The complete pool trace has no missing or unresolved components. Both templates
select idas:sunken_ship_processor. It contains only Integrated API's ordinary
spawner randomizer; reuse integrated-villages-provider content assessment and
its exact processor_inspection identities. The inspected SpawnerBlock input
check is essential: neither ruins template contains such a block, so the
processor's presence is not evidence of an enemy or a generated spawner.

Both literal supply/treasure definitions exist in the preserved packaged JSON
catalog. Hash-bound template contents retain barrels and exact references.
Prior family comparison distinguishes the detached debris from the separate
ship hull variants; shared loot is not a family alias. Existing world samples
remain separate from the nominal template geometry accepted here.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-ship-ruins-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only sunken_ship/sunken_ship_ruins and input identity
may change. No new runtime, renderer or measurement system. Final integration,
acceptance and PR/review/main remain open.
