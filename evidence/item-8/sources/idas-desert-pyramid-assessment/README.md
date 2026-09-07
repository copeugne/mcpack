# IDAS desert pyramid content assessment

Seven content/placement attributes resolved from existing immutable artifacts.
Two complete-family dimension attributes remain open.

## mob_source

Intersection1 authors skeletons; rooms1,6 author husks. Entrance3 Create glue and room1 Quark glass frame are non-mob data. No unresolved authored entity compounds in the31 reachable templates. Physical spawners have separate selected sources. Entrance2 connectors21,52 target missing desert_pyramid/desert_pyramid_villager pool; do not substitute the differently named villager pool or claim its disconnected entity as generated.

## loot_table_source

Six defined literal tables under idas:chests/desert_pyramid/: desert_pyramid,desert_pyramid_surface,desert_pyramid_treasure,desert_pyramid_tools,desert_pyramid_library,desert_pyramid_tomb. Existing raw references preserve template ownership. Selected desert_pyramid_processor conditionally appends two additional defined archaeology tables (suspicious_sand_desert_pyramid,suspicious_gravel_desert_pyramid) to matching suspicious blocks using modern append_loot. Room8 selects ticking-only processing, so that append rule does not apply there. References and selection weights do not establish reward yields.

## generated_spawners

Eleven ordinary spawner blocks across reachable source templates, not a per-assembly count because branches can repeat or be omitted. Eight in intersection1(1),library(1),main(2),rooms1,4,5,6(1 each) select husk15,stray10 via desert_pyramid_processor. Three empty raw entity compounds in library31,room4 block13,room5 block4 are replaced. Settings delay20,min200,max800,count4,nearby6,player16,range4,block-light0..7. Room8 uses ticking-only processor and retains three raw sources: husk1,cave_spider2. All eleven raw potential arrays empty. No trial spawners. Entrance1 marker220 and entrance1_bottom marker6 are empty-metadata CORNER markers, not DATA enemy instructions.

## authored_or_natural_enemies

Direct skeletons/husks and processor-selected or retained ordinary spawners are authored hostile sources. Root spawn_overrides is empty, with no family-specific natural override. Environmental spawning remains separate. Missing villager pool does not establish villager generation, and source templates do not determine a realized encounter count.

## intended_hostility

Surface pyramid entrance and branching underground tomb/room network with authored hostile sources and loot. Missing villager-pool connection is a preserved baseline defect. No Item9 tier, measured difficulty or successful full layout is inferred.

## visual_discoverability

The63 by62 horizontal,29-high entrance1 template supplies an above-ground architectural cue, with a separate surface entrance2 component. Those are source component dimensions, not complete family extents. The branching underground network is not visible from its full footprint; actual sightlines and occlusion are unmeasured.

## underground_surface_classification

Surface entrance components lead downward into a branching underground network. Root generic_structure projects WORLD_SURFACE_WG offset0,size28,fixed rotation,center-distance250,allowed_y_range_from_start200,terrain range12/radius1,biome radius1,ignore_waterlogging,enhanced adaptation none. Entrance1 and2 elements separately specify custom beards/carves kernel size/distance18/50 and35/35. All reachable elements rigid. Placement limits are not measured dimensions; missing villager pool and disconnected cave components retain their existing dispositions.

## Source selection and geometry limit

Family evidence binds packaged-json-redacted, templates-redacted and
pool-traces-content catalogs by SHA-256. The default root reaches31 templates.
Hallway pool has eight alternatives (six halls,two stairs), intersection four,
turn four (library,three turns), room nine. Each listed weight is1. Hallway,
intersection and turn fall back to room, whose fallback is empty. Repeated
branching means a list of template extents is not an assembled-size observation.
Existing raw Item8 chunks.jsonl search found no retained desert_pyramid start.
Use the existing frozen geometry-capture workflow for one full-start example;
no new measurement system or representative pacing study is needed for Item8.

All selected elements use desert_pyramid_processor except room8, which uses
waterlogging_fix_processor. Pyramid processor applies probability1 modern
minecraft:append_loot to matching suspicious sand/gravel, then randomizes ordinary
spawners with husk15,stray10. Reuse modern modifier inspection in
../idas-dig-site-assessment/README.md, randomizer/manager inspection in
../integrated-villages-provider/README.md and ticking inspection in
../idas-desert-market-assessment/README.md. Room8 retains its authored spawner NBT.
The empty raw spawner compounds are library/block_entities/31,
room4/block_entities/13,room5/block_entities/4. All source potentials empty.
CORNER markers occur at entrance1/block_entities/220 and
entrance1_bottom/block_entities/6, with empty metadata. No unresolved entity NBT.

Six literal chest tables and both archaeology tables are defined in the packaged
catalog. Preserve exact template ownership from the raw references. Borrowed
contents, disconnected cave templates and the differently named villager pool
are not new families or automatic repairs. Missing villager pool remains a defect.
No baseline tuning, reward experiment or additional tooling added for this assessment.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-desert-pyramid-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only desert_pyramid and input identity may change.
Two size attributes, final integration, acceptance and PR/review/main remain open.
