# IDAS tinkers workshop assessment

Nine remaining entries for an eight-component chain. Existing catalogs and
processor inspection suffice; no new runtime or measurement system.

## mob_source

Entrance declares villagers and optional alexsmobs:komodo_dragon; AlexsMobs absent means no confirmed komodo inhabitant. Workshop2 directly authors Quark forgotten; workshop6 cave spiders. Glue,frames and item entities are non-mob data and do not prove operating machinery. No unresolved authored entities. Spawner sources vary by selected component processor and are assessed separately.

## loot_table_source

Five defined idas:chests/tinkers_workshop/ sources. Entrance uses tinkers_workshop_basic and tinkers_workshop_bedroom; numbered1..7 use tinkers_workshop;2..7 add tinkers_workshop_tools;7 adds tinkers_workshop_vault. Selected processors tick blocks and, in specified pieces, randomize spawners; none assigns container loot NBT. Sources do not measure reward yields or operational engineering machinery.

## generated_spawners

Ten physical ordinary spawners: workshop2 one forgotten, workshop3 two cave spiders, workshop4 two raw rocky_roller, workshop6 five mixed raw cave-spider/forgotten/centipede-head sources. Workshop2/3 use ticking-only processor and retain raw sources. Workshop4 uses tuff randomizer,6 regular randomizer; both lists select minecraft:skeleton10,quark:forgotten5, replacing raw optional-provider data. Both declare delay20,min200,max800,count4,nearby6,player range16,spawn range4,block-light0..7. Other components have none despite randomizer selection in1/7. No trial spawners or markers. Reuse pinned processor/manager semantics and fallback limitations; source counts are not successful spawn counts.

## authored_or_natural_enemies

Direct forgotten/cave spiders and component-specific ordinary spawners establish authored hostile sources. Entrance villagers are civilian; absent-provider komodo and non-mob entities remain separate. Raw optional mobs in randomized spawners are not selected outcomes. Empty root spawn_overrides declares no family-specific natural override; environmental spawning remains separate.

## intended_hostility

Entrance leads through a serial industrial workshop complex with authored hostile sources and final vault loot. No operating machinery, Item9 tier, measured encounter intensity or gating of foundational engineering behind dungeon rewards is inferred.

## visual_discoverability

Surface-associated entrance is the discovery cue for a deeper chain. Nominal63 by81 footprint and130 vertical span describe the full reference layout including padding, not visible silhouette or sightline. Most nominal geometry lies below entrance; full placement and terrain concealment remain unmeasured.

## underground_surface_classification

Surface entrance with descending connected workshop interiors. Root generic_structure projects WORLD_SURFACE_WG offset0,size8,fixed rotation,beard_thin,terrain range10/radius1,biome radius1,ignore_waterlogging. All elements rigid. Nominal last origins are93 blocks below entrance; terrain/world-height limits may reject components, so source geometry is not measured burial or complete placement.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Templates under data/idas/structure/tinkers_workshop/ have sizes entrance48,37,37;
1=13,15,36;2=22,18,37;3=38,18,38;4=22,20,38;5=25,44,15;6=38,26,40;7=15,27,23.
Each parent target matches the child name. Adjacent aligned connector pairs:
entrance down_west34,0,19 to1 up_west12,14,3;
1 down_south6,0,28 to2 up_south14,17,0;
2 down_north15,0,35 to3 up_north15,17,37;
3 north_up17,17,0 to4 south_up9,19,37;
4 west_up0,17,13 to5 east_up24,43,14;
5 east_up24,11,2 to6 west_up0,25,2;
6 south_up16,25,39 to7 north_up0,25,0.
Resulting origins appear in approximate_footprint. Inclusive union x-3..59,
z0..80,y-93..36 gives63 by81 horizontal and130 vertical. This is a nominal full
reference chain, not measured burial or guaranteed placement within world bounds.
Trace has no missing components or unresolved elements; all pool elements rigid.

Pool processor ownership is material: entrance,2,3,5 use waterlogging_fix;
1,6,7 use tinkers_workshop_processor;4 uses tinkers_workshop_tuff_processor.
The latter two declare dispenser ticking plus ordinary spawner randomization.
Their integrated_structure_spawners lists both contain skeleton10,forgotten5.
Reuse integrated-villages-provider's pinned randomizer/manager inspection and
idas-desert-market-assessment's ticking inspection. Ticking-only pieces2/3 retain
raw forgotten/cave-spider spawners; randomized4/6 do not retain optional rocky
roller/centipede as selected outcomes. Five literal loot tables are defined.
Runtime Mod List absence of AlexsMobs is recorded with exact log identity in
idas-ruins-of-the-deep-assessment. Entrance komodo is not a confirmed inhabitant.
No physical trial spawners, markers or authored ID gaps. Preserve all raw mappings.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-tinkers-workshop-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only tinkers_workshop and input identity may change.
Final integration, acceptance and PR/review/main remain open.
