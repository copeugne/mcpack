# IDAS castle assessment

Seven remaining content/placement entries integrated from existing findings.
Accepted size evidence is retained in the final IDAS geometry capture.

## mob_source

Three castle designs have distinct authored villagers, farm animals and mounts, with shared villager/guard entity-component pools. GuardVillagers is absent, so guard references do not establish functioning guards. Castle2 /entities/10/nbt is an empty compound, preserved unresolved. Displays, seats,glue and item entities are non-mob data. Castle1/2 additionally connect to plains village centers with shared villager,animal,iron_golem and zombie-villager template possibilities; castle3 has no village-center connector. Exact template ownership is preserved below, without assuming every reachable alternative occurs.

## loot_table_source

All13 literal IDs in the reachable graph are defined: five castle tables (base,bedroom,food,library,throne), borrowed witches_treestump, and seven vanilla village tables (cartographer,fisher,plains_house,savanna_house,tannery,toolsmith,weaponsmith). The main designs differ in table ownership; shared village components retain their own references. Castle processor replaces an optional board placeholder, not loot NBT; shared vanilla rule lists have no append_loot or legacy output_nbt. Source references do not establish reward yields or merge other families into Castle.

## generated_spawners

No ordinary or trial spawner blocks or generation markers occur in any of the136 reachable templates, including shared village components. Castle processor only conditionally replaces a purple glass pane; shared village block rules and street-path correction do not introduce spawner sources. No generated spawner source is identified; this does not rule out ordinary environmental mobs.

## authored_or_natural_enemies

Core castles have no identified direct hostile mob or spawner source. Reachable shared plains zombie-villager templates are conditional authored hostile possibilities, not guaranteed castle inhabitants. Iron golems, villagers, animals and absent-provider guards are separate. Empty root spawn_overrides declares no family-specific natural override; environmental spawning remains possible.

## intended_hostility

Castle-settlement family with three designs, inhabitants, mounts and loot rather than a core spawner-driven dungeon. Shared village alternatives can contribute zombie villagers. Absent guards do not prove protection, and displays/glue do not prove working machinery. No Item9 tier or measured difficulty is inferred.

## visual_discoverability

Battlements,towers and the large third-design keep provide surface architectural cues; the first two designs can include a village extension. The retained example is105 by151 horizontally and58 high, not a universal silhouette or typical size. Terrain and surrounding buildings can obscure approaches; actual sightlines remain unmeasured.

## underground_surface_classification

Surface-associated castles with rigid foundation components and optional village settlement extension. Root generic_structure projects WORLD_SURFACE_WG offset0,size4,terrain range10/radius1,biome radius1,ignore_waterlogging,enhanced adaptation none. Main element custom beard/carve kernels size/distance20/15,20/25,35/35 differ by design. Foundations and terrain-following shared village pieces do not make this an underground dungeon; actual terrain alteration and complete component population are not established by a full start chunk.

## Evidence and processor interpretation

Family evidence binds the packaged/template/trace catalogs and final geometry
manifest/downloaded restore by SHA-256. There are136 reachable templates. The
three main designs have equal weight1; each connects to its corresponding bottom.
Castle1 and2 additionally link plains village centers; castle3 does not. Shared
village pieces and the selected tavern contribution retain existing relationships,
not additional castle families. Observed example dimensions do not represent all
three designs. No further geometry or population experiment is needed for Item8.

Core template content under data/idas/structure/castle/:
castle1 authors villager,chicken,pig,item; castle2 mule,horse,armor stands,paintings,
seat,glue and one empty entity NBT at /entities/10/nbt; castle3 horse,mule,donkey,
paintings,glass frames,armor stands,hat stand and glue. Foundations have no entities.
Villager, baby and nitwit components author villagers; guard component authors
GuardVillagers guard, absent from the frozen runtime. Villager_random weights
empty1,adult3,baby1,nitwit1 are selection weights, not observed populations.
Shared graph zombie villagers occur in vanilla plains zombie villager templates;
iron golem in minecraft:village/common/iron_golem. Neither is a guaranteed instance.

All13 raw literal loot IDs are defined in packaged-json-redacted. Castle1 references
castle base/library and vanilla plains_house/toolsmith; castle2 base/library/throne;
castle3 base/bedroom/food/library/throne plus witches_treestump. Other references
belong to shared village templates as recorded in inventory. No raw spawner blocks
or generation markers in the whole reachable graph.

Selected castle_processor has one integrated_block_replace_processor: input
purple_stained_glass_pane,required_mod bountiful,output bountiful:bountyboard,
otherwise minecraft:air,probability1, no output_nbt. Frozen runtime Mod List
(debug.log SHAe5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b)
contains neither bountiful nor guardvillagers, confirmed by existing runtime_mod_ids.
Direct javap -p -c inspection of pinned Integrated API class
com.craisinlord.integrated_api.world.processors.IntegratedBlockReplaceProcessor
in downloads/item3/candidates/integrated_api-1.7.3+1.21.1-neoforge.jar:
class SHAa92f6d152a9351de0c3a1312430540a1eb7c3a7fa8b92fe918a332fb99b31de3.
processBlock compares input block at0..12,checks requiredMod15..22; absent branch
271..333 resolves otherwiseBlock and returns its default state through
createBlockInfo, nonmatching block returns input334..336. Thus castle's missing
Bountiful path selects air, not a working board. No entity/loot assignment is
configured. This records the existing direct inspection, without a new tool.

Shared selected vanilla farm_plains,mossify10/20/70,street_plains,zombie_plains
lists contain minecraft:rule processors without block_entity_modifier or
output_nbt. minecraft:empty has no processing. Preserve the separately inspected
street-path correction at ../lithostitched-street-processor-code/README.md;
block/path variation does not imply injected mobs, loot or operating equipment.

Generated example and archive commands are at
../idas-desert-pyramid-assessment/README.md. Full Castle start line609 in the
restored idas-final-geometry-r1/chunks.jsonl has61 pieces and105x58x151(X,Y,Z).
Its limitations remain unchanged; the geometry is not remeasured here.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-castle-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only castle and input identity may change.
Final integration, acceptance, backup/history and PR/review/main remain open.
