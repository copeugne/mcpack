# IDAS ruined well assessment

Nine remaining entries for two connected components. Existing catalogs and
processor inspection suffice; no new runtime or measurement system.

## mob_source

Main has no authored entities; bottom declares only Create super glue, which is not a mob. Neither template has unresolved entity compounds, physical spawners or generation markers. Both select ticking-only waterlogging_fix_processor, with no mob NBT injection. Environmental spawning remains possible.

## loot_table_source

Neither component has literal loot-table references; selected ticking-only processor assigns no loot NBT. Absence of loot-table references does not prove that fixed contents or salvage are absent. Glue and source furnishings do not establish operating machinery or measured reward yield.

## generated_spawners

No ordinary or trial spawner blocks or generation markers in either template. Selected ticking-only processor introduces no spawner source. Create glue is not a spawner or an enemy.

## authored_or_natural_enemies

No authored mob or spawner-based enemy source. Empty root spawn_overrides declares no family-specific natural override; ordinary environmental spawning remains separate. This does not guarantee every generated well is safe.

## intended_hostility

Ruined well with connected lower section and no authored hostile mob or spawner source. It provides an exploration feature without a hostile dungeon claim, an Item9 tier or assumed operating machinery.

## visual_discoverability

Surface-associated well supplies a local architectural cue; the lower section need not be visible from outside. Nominal18 by23 horizontal and27 vertical extents include lower geometry and padding, not measured sightlines or an exposed silhouette. Terrain and vegetation can obscure parts.

## underground_surface_classification

Surface-associated well with attached lower component. Root generic_structure projects WORLD_SURFACE_WG offset0,size3,beard_thin adaptation,terrain range10/radius1,biome radius1,ignore_waterlogging. Both pools rigid. Nominal bottom origin is twelve blocks below main; actual terrain burial and successful complete placement are unmeasured.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Under data/idas/structure/ruined_well/, ruined_well.nbt is18,15,23 with down_east
aligned connector at17,0,22; ruined_well_bottom.nbt is18,12,23 with up_east aligned
connector at17,11,22. Both name/target idas:ruined_well_bottom. Adjacent connection
gives bottom origin0,-12,0 relative to main0,0,0. Inclusive union x0..17,z0..22,
y-12..14 gives18 by23 horizontal and27 vertical. This is nominal complete
reference geometry, not measured burial or guaranteed lower placement.
Corresponding worldgen/template_pool/ruined_well resources each contain one
rigid element and empty fallback. Trace has no missing components or unresolved
elements. Both select waterlogging_fix_processor; reuse the pinned ticking-only
processor inspection in idas-desert-market-assessment/README.md. It schedules
eligible dispenser/dropper ticks without entity or container-loot NBT injection.

The complete template-content trace retains only bottom super glue as authored
entity data, without mobs, spawners, markers or literal loot-table references.
No machinery-operation or reward-yield experiment is required to inventory these
sources. Fixed content and salvage absence are not inferred from missing tables.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-ruined-well-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only ruined_well and input identity may change.
Final integration, acceptance and PR/review/main remain open.
