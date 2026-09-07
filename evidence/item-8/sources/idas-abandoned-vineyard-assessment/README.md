# IDAS abandoned vineyard assessment

Nine remaining entries for one two-component family. Direct immutable template
inspection and connector derivation reuse the existing brickhouse assessment
pattern. No new runtime, renderer or measurement system.

## mob_source

Main template authors only minecraft:item; bottom has no authored entities. Neither has unresolved entity records, spawners or generation markers. Both select the ticking-only waterlogging_fix_processor, which supplies no mob injection. An item entity is not a mob or enemy. Ordinary environmental spawning remains possible.

## loot_table_source

Neither template contains literal loot-table references, and the selected ticking-only processor assigns no loot NBT. Preserved stove, cabinet, basket, barrel and berry-sack contents remain fixed source contents; absence of loot tables does not prove empty storage. No grape/wine system, machinery operation or reward yield is inferred.

## generated_spawners

No physical ordinary or trial spawners and no structure generation markers in either connected template. The selected waterlogging_fix_processor only schedules eligible dispenser/dropper ticks; it does not add spawners. No generated spawner source is identified in this assembly.

## authored_or_natural_enemies

No authored enemy or spawner source. The sole authored item entity is not an enemy. Empty root spawn_overrides declares no family-specific natural override; ordinary environmental spawning may still occur. This is not a guarantee that every generated site is safe.

## intended_hostility

Abandoned food-storage building with no authored hostile entities or spawners in the connected source assembly. Its contents support a noncombat discovery/salvage role without assigning an Item9 category, measured reward value or invented grape/wine progression.

## visual_discoverability

Surface-associated building provides an architectural cue; the attached bottom component need not be visible from outside. Nominal envelope includes padding and below-main geometry, not a measured silhouette, visible-entry guarantee or sightline distance. Vegetation and terrain may obscure the site.

## underground_surface_classification

Surface-associated main building with an attached lower component. Root projects WORLD_SURFACE_WG offset0,size3,beard_thin adaptation,terrain range10/radius1,biome radius1,ignore_waterlogging. Both components use rigid projection. Nominal lower origin is seven blocks below the main origin; actual burial relative to terrain is not measured.

## Approximate geometry and evidence

The family evidence map binds templates-redacted, pool-traces-content and packaged
JSON catalogs. data/idas/structure/abandoned_vineyard/abandoned_vineyard.nbt has
size24,13,22. Its jigsaw at23,0,21 has orientation down_east, joint aligned, and
name/target idas:abandoned_vineyard_bottom. The bottom template in the same
directory has size24,7,22 and matching up_east connector at23,6,21. With main
origin0,0,0, adjacent connection places the bottom origin at0,-7,0. Thus x0..23,
z0..21,y-7..12 yields24 by22 horizontal and20 vertical. These are nominal complete
assembly dimensions, not observed placement or terrain burial. Quarter rotations
exchange horizontal axes; rejected placement may omit a component.

Both corresponding worldgen/template_pool/abandoned_vineyard definitions have one
rigid element, empty fallback and waterlogging_fix_processor. No missing pool
components or unresolved pool elements. Reuse the exact ticking processor
inspection in idas-desert-market-assessment/README.md. It schedules eligible ticks
without assigning entity or container-loot NBT. Full template contents and the
family rationale retain food-storage furnishings; no operational machinery or
empty-storage claim follows from absent loot-table references.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-abandoned-vineyard-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only abandoned_vineyard and input identity may change.
Final integration, acceptance and PR/review/main remain open.
