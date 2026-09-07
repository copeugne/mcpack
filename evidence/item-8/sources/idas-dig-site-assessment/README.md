# IDAS dig site assessment

Nine remaining entries for four connected components. Existing catalogs suffice;
no new runtime or measurement system. Root ID is idas:dig_site/dig_site.

## mob_source

Main and bottom declare villagers and guardvillagers:guard; stable and stable-bottom declare horses. Main also authors item entities. GuardVillagers is absent from the frozen runtime, so guard declarations are not confirmed inhabitants. Items are non-mob data. No unresolved entity compounds or physical spawners. Selected processor applies archaeology loot modifiers and dispenser ticking, without mob NBT injection.

## loot_table_source

Three defined literal idas:chests/dig_site/ tables: dig_site in main/bottom, dig_site_tools and dig_site_treasure in bottom. Neither stable component has literal loot references. Selected dig_site_processor additionally uses modern minecraft:append_loot modifiers: suspicious sand matches receive defined idas:archeology/suspicious_sand_dig_site, suspicious gravel matches receive defined idas:archeology/suspicious_gravel_dig_site, each probability1. These conditional processor sources remain distinct from literal references; realized yield is unmeasured.

## generated_spawners

No ordinary or trial spawner blocks in the four components. Main /block_entities/182 and bottom /block_entities/62 are CORNER markers with empty metadata, not DATA enemy instructions. Selected processor contains archaeology loot rules and dispenser ticking only; no spawner source identified.

## authored_or_natural_enemies

Villagers and horses supply civilian/animal sources, not a hostile enemy roster. Absent-provider guards do not establish generated inhabitants; item entities are not enemies. Empty root spawn_overrides declares no family-specific natural override; environmental spawning remains separate.

## intended_hostility

Excavation work area with connected lower section and stables, civilian declarations and chest/archaeology loot sources. No authored hostile mob or spawner source is identified. No Item9 tier, guaranteed safe site or measured excavation reward is claimed.

## visual_discoverability

Roofed excavation work area and attached stables provide surface architectural cues; lower excavation sections can remain concealed. Nominal42 by39 footprint and21 height include bottom geometry and padding, not measured sightlines or exposed silhouette. Terrain and vegetation may obscure access.

## underground_surface_classification

Surface-associated work area/stables with lower components. Root generic_structure projects WORLD_SURFACE_WG offset0,size4,fixed rotation,terrain range12/radius1,biome radius1,ignore_waterlogging,enhanced adaptation none. Main element separately declares custom beards/carves,kernel size20/distance35; stable uses size15/distance20. All rigid. Nominal bottom offsets -9 and-1 do not measure actual burial or terrain alteration.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Under data/idas/structure/dig_site/, main west_up at0,0,12 meets stable east_up
at11,0,9, giving stable origin-12,0,3. Main down_east at29,0,0 meets bottom
up_east at29,8,0, giving bottom origin0,-9,0. Stable down_west at0,0,0 meets
stable-bottom up_west at0,0,0, giving stable-bottom origin-12,-1,3. All aligned,
with matching stables/bottom names. Sizes30,12,39;30,9,39;12,6,14;12,1,14 give
inclusive union x-12..29,z0..38,y-9..11:42 by39 horizontal and21 vertical.
This is nominal complete geometry, not measured burial or guaranteed placement.
Corresponding template_pool resources each have one rigid element. Trace has no
missing components or unresolved pool elements. Desert templates in the same
directory belong to the separately inventoried desert_dig_site family.

worldgen/processor_list/dig_site_processor.json has two minecraft:rule entries
using block_entity_modifier type minecraft:append_loot for probability1 matches
of suspicious_sand and suspicious_gravel, preserving each input block type.
Both named archaeology tables have definitions under data/idas/loot_table/archeology/.
This is the modern modifier field, not legacy output_nbt. Final processor is
TickBlocksProcessor for dispenser only; reuse idas-desert-market-assessment's
pinned inspection. No entity or spawner mutation is declared. Literal chest-table
mapping remains separate from these conditional processor assignments.

Main /block_entities/182 and bottom /block_entities/62 are CORNER with empty
metadata. GuardVillagers absence is established by the frozen runtime Mod List
identity in idas-ruins-of-the-deep-assessment. Optional guard declarations are
not confirmed inhabitants. No population, yield or machinery-operation capture
is required to inventory these sources.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-dig-site-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only dig_site and input identity may change.
Final integration, acceptance and PR/review/main remain open.
