# IDAS enchanting tower assessment

Seven remaining entries are integrated for one family and three alternatives.
Prior idas-existing-geometry-assessment already integrated the11 by26 by11
single-template dimensions. No new runtime, measurement or tooling is needed.

## mob_source

Three active rigid template alternatives, red/orange/blue, each author minecraft:villager. No unresolved template entities, generation markers or missing components. All select minecraft:empty processors. Existing ModAdaptiveStructure evidence and absent ars_nouveau retain the default pool, not the inactive compatibility templates. Source declarations are not measured populations.

## loot_table_source

All three active alternatives reference the defined idas:chests/enchantingtower/enchantingtower_basic, enchantingtower_library and enchantingtower_top tables. Empty processors add no table source. Separate *_ars definitions are not selected by these active templates. Stored furnishings and loot-table references do not establish reward quantities or tested interactions.

## generated_spawners

No ordinary or trial spawner blocks or generation markers in the three active templates. Empty processors introduce no spawner source. This is an absence of authored spawners, not a guarantee that natural mobs cannot spawn.

## authored_or_natural_enemies

Authored villagers are the only identified template entities. No authored hostile entity or physical spawner in the selected alternatives; root spawn_overrides is empty, so no family-specific natural override is declared. Ordinary environmental spawning remains possible.

## intended_hostility

Furnished loot-bearing tower with authored villagers and no identified authored hostile encounter source. Its name and inactive Ars compatibility do not establish a wizard enemy or spell-progression system. Natural danger is not excluded; no combat intensity or Item9 tier is assigned.

## visual_discoverability

Narrow freestanding tower form with upper furnished rooms, contrasting material/flower alternatives and26-block template height provides a vertical architectural cue. Surrounding terrain and vegetation may obscure it. No measured sightline, visible entrance guarantee or real-client discovery claim.

## underground_surface_classification

Surface-associated tower: active mod_adaptive_structure root projects to WORLD_SURFACE_WG with start offset0, size1, beard_thin adaptation and biome radius1. Packaged search_for_highest_land flag is preserved in the root without treating it as a measured placement result. Rigid single-template dimensions do not establish actual foundation burial or site relief.

## Evidence and limits

The preserved pool idas:enchantingtower/enchantingtower assigns each active
integrated_api_single_pool_element weight1, rigid projection and minecraft:empty
processors, with empty fallback. The complete trace has three templates and no
missing or unresolved elements. The existing family decision binds the verified
ModAdaptiveStructure selection evidence: ars_nouveau is absent, so the default
pool remains active. This does not reactivate optional compatibility templates.

All three literal table definitions exist in the packaged JSON catalog. The
canonical inventory retains exact references and template mappings. Prior
full-template inspection recorded furnace columns, barrels, upper beds, brewing
and differing furnishings. Neither those furnishings nor the structure name
proves operating machinery, hostile wizards or tested gameplay.

This assessment reuses the family decision's existing hash-bound catalogs and
provider evidence. No population, reward-yield or sightline experiment is added.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-enchanting-tower-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only enchantingtower and input identity may change.
Final integration, acceptance and PR/review/main remain open.
