# IDAS windswept shrine assessment

Nine remaining entries for one six-component assembly. Existing catalogs and
processor inspection suffice; no new runtime or measurement system.

## mob_source

Shrine1 authors Quark glass frames and Create super glue; its bottom also authors super glue. Other components have no authored entities. These are non-mob entities, not an enemy roster. No unresolved entity compounds or physical spawners. Selected windswept_shrine_processor schedules dispenser ticks only, with no mob NBT injection.

## loot_table_source

Shrine1 alone references the defined idas:chests/windswept_shrine/windswept_shrine table. Other components have no literal loot-table references. Selected ticking-only processor assigns no loot NBT. Preserved furnishings and glue do not establish working machinery or measured reward yield.

## generated_spawners

No ordinary or trial spawner blocks in any of the six templates. Shrine1,shrine1_bottom,shrine3,shrine3_bottom each have one CORNER structure marker with empty metadata, not DATA enemy instructions. Selected processor only schedules dispenser ticks and introduces no spawner source.

## authored_or_natural_enemies

No authored mob or spawner-based enemy source. Frames and glue are non-mob entities. Empty root spawn_overrides declares no family-specific natural override; ordinary environmental spawning remains separate. Source absence does not guarantee safety at every generated site.

## intended_hostility

Connected shrine compound with furnishings and a shrine loot source, but no authored hostile mob or spawner source. This supports discovery interest without inventing a hostile encounter, operating machinery, player spell progression or an Item9 tier.

## visual_discoverability

Three connected shrine sections provide architectural cues over a broad nominal81 by54 footprint; attached bottoms need not be exposed. Nominal33 height includes lower components and padding, not a measured visible silhouette or sightline. Terrain and vegetation may conceal parts.

## underground_surface_classification

Surface-associated three-section shrine with a bottom attached to each section. Root projects WORLD_SURFACE_WG offset0,size5,fixed rotation,terrain range20/radius3,ignore_waterlogging,enhanced adaptation none. Each main pool separately declares custom beards/carves,kernel size25/distance25. All components rigid. Nominal bottom offsets are -9,-1,-9; actual burial, terrain alteration and full placement are unmeasured.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Under data/idas/structure/windswept_shrine/, shrine1 east_up jigsaw at20,3,0 joins
shrine2 west_up at0,3,0 through idas:shrine2. Shrine1 west_up at0,3,0 joins shrine3
east_up at40,3,11 through idas:shrine3. With shrine1 origin0,0,0, adjacent joints
yield shrine2 origin21,0,0 and shrine3 origin-41,0,-11. Main sizes21,24,43;
19,9,21;41,12,43 give union x-41..39,z-11..42.

Each main down_north connector at y0 joins its aligned bottom up_north at
local y8,0,8 respectively, sharing horizontal coordinates within each pair.
Bottom sizes21,9,43;19,1,21;41,9,43 produce origins0,-9,0;21,-1,0;-41,-9,-11.
Thus inclusive union y-9..23 yields81 by54 horizontal and33 vertical overall.
This is nominal complete reference geometry, not observed burial or guaranteed
full placement. All corresponding template_pool resources have one rigid element
and empty fallback; no missing components or unresolved pool elements.

worldgen/processor_list/windswept_shrine_processor.json contains only
integrated_api:tick_blocks_processor for minecraft:dispenser. Reuse the pinned
TickBlocksProcessor inspection in idas-desert-market-assessment. Main pools
separately preserve custom terrain kernels; root enhanced adaptation none does
not erase those element settings. No mob, spawner or loot NBT injection is declared.

CORNER markers with empty metadata are shrine1 /block_entities/1,
shrine1_bottom /block_entities/34, shrine3 /block_entities/60 and
shrine3_bottom /block_entities/34. These are not DATA enemy instructions.
The literal shrine loot definition exists under data/idas/loot_table/chests/
windswept_shrine/windswept_shrine.json. No machinery-operation or reward-yield
measurement is required to inventory the source.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-windswept-shrine-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only windswept_shrine and input identity may change.
Final integration, acceptance and PR/review/main remain open.
