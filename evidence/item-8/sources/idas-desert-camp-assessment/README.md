# IDAS desert camp assessment

Nine entries integrated for one family/four independent template variants.
Each template is11 by4 by12 in x,y,z blocks. Approximate sizes use that nominal
envelope without a new runtime capture or claim of observed terrain extent.

## mob_source

Four independent templates contain no authored entities, unresolved entity compounds or generation markers. Their selected waterlogging_fix_processor only schedules dispenser/dropper ticks; it does not introduce entities. Seats and machinery blocks are not evidence of live operators or working machinery.

## loot_table_source

No literal loot-table references in the four templates. Selected ticking processor appends no loot NBT. Preserved sacks and other fixed contents are not thereby declared empty, and ordinary harvestable materials remain distinct from loot-table sources.

## generated_spawners

No ordinary or trial spawner blocks or generation markers in any variant. Selected ticking processor does not create spawners. This does not exclude ordinary environmental spawning.

## authored_or_natural_enemies

No authored entity or spawner source; all four roots have empty spawn_overrides. No family-specific natural enemy rule is declared, while ordinary environmental spawning remains possible. Empty windswept biome overlap is eligibility evidence, not an enemy or generation-failure observation.

## intended_hostility

Small open camp/worksite design with campfire, sack, seat and saw/hand-crank arrangement. No identified authored hostile encounter source. Neither the worksite furnishings nor absent spawners establish safe conditions or functioning machinery.

## visual_discoverability

Low open worksite, campfire and scattered equipment provide local cues against desert ground. Material and vegetation substitutions remain variants. Four-block template height is not a reliable distant landmark; no measured sightline or discovery distance.

## underground_surface_classification

Surface worksite intent for all four generic_structure roots: WORLD_SURFACE_WG projection, offset0, size1, beard_thin and biome radius1. Red adds terrain range10/radius1. The windswept variant has no captured possible-biome overlap, as already recorded. Template size does not establish final terrain relief or foundation burial.

## Evidence and limits

All four pool graphs have no missing or unresolved components and select
idas:waterlogging_fix_processor. Its only processor schedules dispenser/dropper
ticks and preserves incoming block info; reuse the exact class inspection in
idas-desert-market-assessment. There is no entity or loot injection in this path.

Hash-bound templates and pool trace retain the dimensions and empty entity,
loot-reference and spawner fields. Existing idas-variant-views and family
rationale retain the low worksite design, campfire, sack, seat and saw arrangement.
The integrated dimension assessment already distinguishes the windswept variant's
empty possible-biome overlap from the three other variants. No failed generation
experiment, working machinery or empty fixed inventory is inferred.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-desert-camp-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only desert_camp and input identity may change.
No new runtime, renderer or measurement system. Final integration, acceptance
and PR/review/main remain open.
