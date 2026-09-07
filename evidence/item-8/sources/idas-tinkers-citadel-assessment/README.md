# IDAS tinkers citadel assessment

Nine remaining entries for four branching components. Existing catalogs and
direct pinned processor inspection suffice; no new runtime or measurement system.

## mob_source

Main authors tropical fish and armor stands; main/pieces3,4 author Create glue. Fish are animal sources, stands/glue non-mob data. No directly authored hostile mob or unresolved entity compound. Ordinary spawners are separate hostile sources; selected citadel randomizer replaces existing spawner NBT. Bearing processor queues assembly but does not establish working machinery.

## loot_table_source

Six defined idas:chests/tinkers_citadel/ sources: tinkers_citadel,bedroom,create,library,tools tables in main; tinkers_citadel_vault in3,4. Piece2 has no literal loot reference. Selected processors schedule dispenser ticks,queue windmill bearing assembly and randomize spawners; no container loot assignment. Source attribution is not measured yield or operating machinery.

## generated_spawners

Ten ordinary spawners: main6,piece3 three,piece4 one. Seven raw entity compounds in main/piece4 are empty; piece3 raw data declares zombie,forgotten,skeleton. All use citadel randomizer, selecting skeleton10,zombie10,quark:forgotten10 and replacing NBT. Delay20,min200,max800,count4,nearby6,player range16,spawn range4,block-light0..7. Preserve raw unresolved paths; selected source resolved through existing processor/manager inspection and fallback limits. No trial spawners. Main has two CORNER markers with empty metadata, not DATA enemy instructions. Source count is not successful spawning count.

## authored_or_natural_enemies

Processor-selected skeleton,zombie,forgotten spawners establish authored hostile sources; fish and non-mob stands/glue are separate. Empty root spawn_overrides declares no family-specific natural override; environmental spawning remains separate. No realized encounter quantity claimed.

## intended_hostility

Branching industrial citadel with ordinary spawner-based hostile sources and vault loot. Source machinery and bearing assembly requests do not prove operating equipment. No Item9 tier, measured difficulty or foundational engineering gate is inferred.

## visual_discoverability

Large main industrial structure and upper attachment provide architectural cues. Nominal70 by110 footprint and118 height include the complete reference assembly and padding, not measured visible silhouette or sightlines. Terrain and structure occlusion can conceal approaches.

## underground_surface_classification

Surface-associated branching citadel. Root generic_structure projects WORLD_SURFACE_WG offset0,size4,fixed rotation,terrain range10/radius1,biome radius1,ignore_waterlogging,enhanced adaptation none. Main,piece2,piece3 separately declare custom beards/carves with kernel size/distance35/45,15/10,35/35. All rigid; piece4 nominal origin63 blocks above main. Actual terrain alteration,burial and complete placement unmeasured.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Under data/idas/structure/tinkers_citadel/, main south_up26,7,52 joins2 north_up3,7,0;
main north_up11,17,0 joins3 south_up2,17,37; main up_south39,62,3 joins4
down_south35,0,0. All name/target idas:tinkers_citadel, aligned joints.
Adjacent connections give origins2=23,0,53;3=9,0,-38;4=4,63,3 relative to main0,0,0.
Sizes70,63,53;5,8,19;33,19,38;36,55,34 yield inclusive union x0..69,z-38..71,
y0..117:70 by110 horizontal and118 vertical. These are nominal complete layout
extents, not observed placement. Pools each have one rigid element; trace has no
missing components or unresolved elements. Element terrain kernels remain separate.

All select tinkers_citadel_processor: dispenser ticking,windmill bearing processor,
ordinary spawner randomizer. integrated_structure_spawners/tinkers_citadel.json
lists skeleton,zombie,forgotten weight10 each. Reuse integrated-villages-provider's
pinned randomizer/manager inspection and idas-desert-market-assessment's ticking
inspection. Seven raw empty SpawnData.entity compounds remain preserved; selected
replacement does not depend on those missing identities. Main CORNER markers
/block_entities/278 and1860 have empty metadata. Six literal loot tables defined.

Direct pinned javap -p -c inspection of
com.craisinlord.integrated_api.world.processors.create.WindmillBearingProcessor
matches block description ID block.create.windmill_bearing, mutates incoming NBT
QueueAssembly=true, schedules block tick0 and returns the same position/state
with that NBT; other blocks return unchanged. It neither introduces mob/loot NBT
nor proves successful bearing operation. No null-NBT fallback exists in this method.
Class SHA-256: 96ca163f567571ff10222c53425f7cd2f71480891eb3c05750b2e4e5a087476a.
Artifact: downloads/item3/candidates/integrated_api-1.7.3+1.21.1-neoforge.jar.
This records actual processor behavior without a new machinery experiment.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-tinkers-citadel-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only tinkers_citadel and input identity may change.
Final integration, acceptance and PR/review/main remain open.
