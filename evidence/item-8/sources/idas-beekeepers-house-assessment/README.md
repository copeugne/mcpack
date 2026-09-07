# IDAS beekeeper house assessment

Nine remaining entries for two connected components. Existing catalogs and
processor inspection suffice; no new runtime or measurement system.

## mob_source

Both templates declare bees and villagers. Main additionally contains non-mob armor stand,item,frames and nested Create seat references. Nine main entity records lack IDs and have empty NBT compounds; preserve source paths without inventing inhabitants. Five hive block entities additionally preserve ten legacy Bees[].EntityData.id=minecraft:bee entries: main2,second1/1/3/3. These saved entries are separate from template entity declarations and do not prove successful release. Both pools select the ticking-only processor, with no mob injection.

## loot_table_source

Main template references three defined idas:chests/beekeepers_house/ tables: beekeepers_bedroom,beekeepers_food,beekeepers_tools. Second component has no literal loot reference. Selected ticking-only processor assigns no loot NBT. Hive and furnishing contents remain source data, not measured honey production, realized reward yields or proof of operational machinery.

## generated_spawners

No physical ordinary or trial spawners in either template. Second component has one structure-block SAVE marker at21,0,47 with empty metadata, not a DATA enemy instruction. Saved hive occupants are distinct from spawner blocks. Selected ticking-only processor does not introduce spawners.

## authored_or_natural_enemies

Authored bees and villagers provide habitation sources, not a deliberately hostile enemy roster. Bees can create conditional interaction risk; their presence is not proof of a realized attack. Frames, items, seats and armor stands are not enemies. Empty root spawn_overrides declares no family-specific natural override; ordinary environmental spawning remains possible.

## intended_hostility

Furnished beekeeper house and attached hive area support civilian habitation and bee-related interaction, with no authored hostile mob or spawner source. Conditional bee risk does not establish a hostile dungeon or Item9 tier. Effective population and operating honey production are not claimed.

## visual_discoverability

Surface-associated house with attached bee-nest/hive area supplies architectural and beekeeping cues. Nominal62 by50 footprint and26 height describe complete layout extents, not a measured visible silhouette or sightline. Vegetation and terrain can obscure portions; no guaranteed visible entrance.

## underground_surface_classification

Surface-associated two-part house/hive assembly. Root generic_structure projects WORLD_SURFACE_WG offset0,size3,beard_thin adaptation,terrain range10/radius1,biome radius1,ignore_waterlogging. Both pools use rigid projection and ticking-only waterlogging_fix_processor. Nominal component origins share y0; actual terrain burial and complete placement remain unmeasured.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Under data/idas/structure/beekeepers_house/, beekeepers_house.nbt has size33,26,48
and east_up aligned jigsaw at32,1,42. beekeepers_house2.nbt has size29,15,48 and
west_up aligned jigsaw at0,1,44. Both name/target idas:beekeepers_house. Adjacent
connection yields second origin33,0,-2 relative to main0,0,0. Inclusive union
x0..61,z-2..47,y0..25 yields62 by50 horizontal and26 vertical. Complete nominal
assembly is not guaranteed generated placement. Both corresponding template_pool
resources have one rigid element and empty fallback. Trace has no missing
components or unresolved elements. Reuse idas-desert-market-assessment's exact
ticking processor inspection; no mob or loot injection follows from that processor.

Main /entities/11,13,15,17,22,25,27,29,31/nbt are empty dictionaries. Retain the
raw unresolved paths as empty source records rather than hypothetical mobs.
Main hive at29,3,39 preserves two legacy Bees entries; second hives at3,4,29;
5,4,33;14,4,11;18,4,11 preserve1,1,3,3 entries. All EntityData IDs are minecraft:bee.
As in existing AdoraBuild and Terralith hive assessments, retain these legacy
keys separately from top-level entities and do not infer successful release.
Second structure marker at21,0,47 is SAVE with empty metadata. The three literal
bedroom/food/tools loot definitions exist under data/idas/loot_table/chests/
beekeepers_house/. No baseline content repair or honey-production measurement
is needed to inventory these sources.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-beekeepers-house-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only beekeepers_house and input identity may change.
Final integration, acceptance and PR/review/main remain open.
