# IDAS desert dig site assessment

Nine remaining entries for two connected components. Reuse the shared dig-site
processor assessment; no new runtime or measurement system.

## mob_source

Both components declare villagers,guardvillagers:guard and Create seats. GuardVillagers is absent from the frozen runtime, so guards are not confirmed inhabitants; seats are non-mob entities. Eight main entity records have empty NBT compounds and no recoverable identity. No spawners or generation markers. Selected dig_site_processor applies archaeology loot rules and dispenser ticking, with no mob NBT injection.

## loot_table_source

Three defined literal idas:chests/dig_site/ sources: dig_site_desert and dig_site_tools in main, dig_site_treasure in bottom. Shared dig_site_processor conditionally assigns defined idas:archeology/suspicious_sand_dig_site and idas:archeology/suspicious_gravel_dig_site using modern append_loot modifiers on matching suspicious blocks, each probability1. Reuse the dig-site processor assessment; conditional assignments are distinct from literal references and not measured yields.

## generated_spawners

Neither component has ordinary/trial spawner blocks or generation markers. Selected processor has archaeology loot rules and dispenser ticking only; no generated spawner source identified. Seats are not spawners.

## authored_or_natural_enemies

Villagers provide civilian sources; absent-provider guards do not establish generated enemies or inhabitants. Seats are non-mob data and empty records supply no identity. Empty root spawn_overrides declares no family-specific natural override; environmental spawning remains separate.

## intended_hostility

Desert excavation compound with tall tower, framed worksite and lower excavation layer, civilian declarations and chest/archaeology sources. No authored hostile mob or spawner source identified. No Item9 tier, universally safe site or measured excavation reward claimed.

## visual_discoverability

Tower and framed surface worksite provide architectural cues; lower excavation can remain hidden. Nominal38 by48 footprint and43 height include lower geometry and padding, not a measured exposed silhouette or sightline. Terrain can obscure access.

## underground_surface_classification

Surface-associated desert worksite with lower excavation component. Root generic_structure projects WORLD_SURFACE_WG offset0,size2,fixed rotation,terrain range12/radius1,biome radius1,ignore_waterlogging,enhanced adaptation none. Main element separately declares custom beards/carves,kernel size20/distance25. Both rigid; nominal bottom origin ten blocks below main does not measure actual burial or terrain alteration.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Root idas:dig_site/dig_site_desert differs from family idas:desert_dig_site.
Under data/idas/structure/dig_site/, dig_site_desert.nbt has size38,33,48 and
down_east aligned connector37,0,0; dig_site_desert_bottom.nbt has size38,10,47 and
up_east aligned connector37,9,0. Both name/target idas:bottom. Adjacent connection
yields bottom origin0,-10,0 relative to main0,0,0. Inclusive union x0..37,z0..47,
y-10..32 gives38 by48 horizontal and43 vertical. These are nominal complete
layout dimensions, not observed burial or guaranteed placement. Corresponding
pool resources each have one rigid element and empty fallback. Trace has no
missing components or unresolved pool elements. Ordinary dig-site stables are
not attached here, despite sharing the packaged directory and processor.

Both select dig_site_processor. Reuse idas-dig-site-assessment/README.md for
exact modern append_loot rules, their two defined archaeology tables and the
pinned ticking processor inspection. Literal main desert/tools and bottom
treasure definitions exist under data/idas/loot_table/chests/dig_site/.
Main element terrain kernel size20/distance25 remains separate from root none.

Main /entities/12,17,19,21,23,25,27,32/nbt are empty dictionaries. Preserve those
raw paths without inventing mobs. GuardVillagers absence is established by the
runtime Mod List identity in idas-ruins-of-the-deep-assessment. No spawners or
structure-generation markers occur. No population, machinery-operation or
reward-yield measurement is needed to inventory these source declarations.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-desert-dig-site-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only desert_dig_site and input identity may change.
Final integration, acceptance and PR/review/main remain open.
