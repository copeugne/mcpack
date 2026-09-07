# IDAS desert ruins assessment

Nine remaining entries for two connected components. Existing catalogs and
processor inspection suffice; no new runtime or measurement system.

## mob_source

Neither component declares authored entities, unresolved entity compounds, physical spawners or generation markers. Both select ticking-only waterlogging_fix_processor, with no mob NBT injection. Ordinary environmental spawning remains possible.

## loot_table_source

Neither component contains literal loot-table references; selected ticking-only processor assigns no loot NBT. This does not establish empty fixed containers or absent salvage. Reward yield is not measured.

## generated_spawners

No ordinary/trial spawner blocks or generation markers in either connected template. Selected ticking-only processor introduces no spawner source.

## authored_or_natural_enemies

No authored entity or spawner-based enemy source. Empty root spawn_overrides declares no family-specific natural override; environmental spawning remains separate. No guarantee that every generated ruin is safe.

## intended_hostility

Small desert ruin with connected lower section and no authored hostile mob or spawner source. Inventoried as an exploration feature without assuming a hostile dungeon, Item9 tier or reward quantity.

## visual_discoverability

Surface-associated ruin provides a local architectural cue; the lower component can remain concealed. Nominal14 by15 footprint and21 height include lower geometry and padding, not measured exposed silhouette or sightlines. Terrain may obscure the site.

## underground_surface_classification

Surface-associated desert ruin with attached lower component. Root generic_structure projects WORLD_SURFACE_WG offset0,size3,beard_thin adaptation,terrain range10/radius1,biome radius1,ignore_waterlogging. Both pools rigid. Nominal lower origin twelve blocks below main is not measured burial relative to terrain.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Under data/idas/structure/desert_ruins/, desert_ruins.nbt is14,9,15 with down_east
aligned connector13,0,14; desert_ruins_bottom.nbt is14,12,15 with up_east aligned
connector13,11,14. Both name/target idas:desert_ruins_bottom. Adjacent connection
yields bottom origin0,-12,0 relative to main0,0,0. Inclusive union x0..13,z0..14,
y-12..8 gives14 by15 horizontal and21 vertical. These are nominal complete layout
dimensions, not observed burial or guaranteed placement. Corresponding pools
have one rigid element each. Trace has no missing components or unresolved elements.

Both select waterlogging_fix_processor. Reuse the pinned ticking-only inspection
in idas-desert-market-assessment/README.md; it schedules eligible dispenser/dropper
ticks without assigning entity or container-loot NBT. Complete template-content
trace has no entities,spawners,markers or literal loot references. Fixed-content
or salvage absence is not inferred from absent tables. No population, yield or
sightline measurement is required to inventory these source declarations.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-desert-ruins-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only desert_ruins and input identity may change.
Final integration, acceptance and PR/review/main remain open.
