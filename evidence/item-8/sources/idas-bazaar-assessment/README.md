# IDAS bazaar assessment

Nine remaining entries for nine connected market components. Existing catalogs
and processor inspection suffice; no new runtime or measurement system.

## mob_source

Villagers occur in pieces2,3,4,5,7,8,9; llama in1. Guard references in1,2,3,6,7,9 and cockroach in7 depend on absent GuardVillagers/AlexsMobs, so they are not confirmed inhabitants. Seats,frames and armor stand are non-mob entities. Twenty-six ID-less records across3,4,7,8,9 are empty NBT compounds (6,1,4,3,12). Preserve raw paths without invented identities. Selected ticking-only processor supplies no mob NBT injection.

## loot_table_source

Defined idas:chests/bazaar/bazaar is referenced by all pieces except center5; defined idas:chests/bazaar/bazaar_food additionally occurs in9. No literal bazaar_tools reference occurs despite a packaged definition. Selected ticking-only processor assigns no loot NBT. Source ownership is not measured reward yield or operating market machinery.

## generated_spawners

No ordinary/trial spawner blocks or generation markers across the nine connected templates. Selected waterlogging_fix_processor only schedules eligible ticks and introduces no spawner source.

## authored_or_natural_enemies

Villagers and llama are civilian/animal declarations, not an authored hostile roster. Absent-provider guards/cockroach and empty entity records do not establish generated enemies. Empty root spawn_overrides declares no family-specific natural override; environmental spawning remains separate.

## intended_hostility

Large connected market assembly with civilian and animal declarations, furnishings and two literal loot sources. No authored hostile mob or spawner source identified. Preserve optional-provider limitations without assigning an Item9 tier or claiming every generated site is safe.

## visual_discoverability

Broad nine-section market provides architectural cues across a nominal115 by112 footprint and31 height. These are complete layout extents including padding, not measured sightlines or exposed silhouette. Buildings, terrain and vegetation may obscure internal approaches.

## underground_surface_classification

Surface-associated market. Root generic_structure projects WORLD_SURFACE_WG offset0,size9,terrain range10/radius3,biome radius1,ignore_waterlogging; custom enhanced adaptation declares beards/carves,kernel size35/distance35. All components rigid. Adjacent pieces start one block above center5 in nominal geometry; actual burial and terrain alteration are unmeasured.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Templates data/idas/structure/bazaar/bazaar1..9.nbt have sizes respectively
48,30,48;21,30,48;46,30,48;46,30,17;21,31,17;48,30,17;48,30,47;21,30,47;46,30,47.
Center5 west0,30,8 joins4 east45,29,8; east20,30,8 joins6 west0,29,8;
north10,30,0 joins2 south10,29,47; south10,30,16 joins8 north10,29,0.
Adjacent aligned connectors produce origins4=-46,1,0;6=21,1,0;2=0,1,-48;
8=0,1,17 relative to center0,0,0. Piece2 east20,29,47 joins1 west0,29,47 and
west0,29,47 joins3 east45,29,47; piece8 east20,29,0 joins7 west0,29,0 and
west0,29,0 joins9 east45,29,0. Thus corners1,3,7,9 have origins21,1,-48;
-46,1,-48;21,1,17;-46,1,17. Names/targets match numbered components.
Inclusive union x-46..68,z-48..63,y0..30 gives115 by112 horizontal and31 vertical.
Nominal complete layout is not guaranteed observed placement. Every corresponding
pool has one rigid element; trace has no missing components or unresolved elements.

All select waterlogging_fix_processor. Reuse the pinned ticking-only inspection
in idas-desert-market-assessment; it adds no entity or container-loot NBT.
The two referenced bazaar/bazaar_food tables have packaged definitions. The
additional bazaar_tools definition alone does not establish a source in this family.
No physical spawners or structure-generation markers occur. Empty entity compounds
are preserved at the exact paths in mob_source.unresolved_authored_entities;
direct template inspection verifies all26 are empty dictionaries. Runtime Mod List
identity in idas-ruins-of-the-deep-assessment establishes absence of GuardVillagers
and AlexsMobs. No optional reference is promoted to confirmed population.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-bazaar-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only bazaar and input identity may change.
Final integration, acceptance and PR/review/main remain open.
