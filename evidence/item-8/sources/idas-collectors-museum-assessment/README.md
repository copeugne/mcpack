# IDAS collectors museum assessment

Nine remaining entries for two connected source components. Existing immutable
catalogs and established processor inspection suffice; no new runtime or tool.

## mob_source

Main authors absent-provider AlexsMobs rattlesnake,capuchin_monkey,gelada_monkey and absent Cloud Storage balloon/balloon_tie references. Quark glass frames and Create glue in main, and glue in lower component, are non-mob display data. No unresolved authored entity compounds. Ordinary spawners supply selected hostile sources separately; optional entity references do not prove live inhabitants or operating exhibits.

## loot_table_source

Eleven distinct literal loot IDs are defined. Main references six museum tables (basic,bedroom,farm,food,library,space), two desert_pyramid tables (base,tomb), sunken_ship_supply and vanilla jungle_temple. Lower references museum_basic,museum_food,museum_treasure. Shared loot does not merge these other structure families into the museum. Selected processor schedules dispenser ticks and randomizes spawners, without appending container loot NBT. Sources are not measured reward yields.

## generated_spawners

Eighteen ordinary spawner blocks, eleven in main and seven below, all have empty raw SpawnData.entity compounds and empty potentials. Both components select collectors_museum_processor, whose museum list selects zombie15,skeleton10,quark:wraith5 and replaces existing spawner NBT. Settings delay20,min200,max800,count4,nearby6,player16,range4,block-light0..7. Preserve raw unresolved paths while distinguishing the resolved selected replacement source. No trial spawners or generation markers. Authored block counts are not successful generated/spawned counts.

## authored_or_natural_enemies

Processor-selected ordinary spawners provide authored hostile sources. Optional animals and balloon references do not establish additional effective enemies; frames/glue are non-mob data. Empty root spawn_overrides declares no family-specific natural override. Environmental spawning remains separate and realized encounters are unmeasured.

## intended_hostility

Large exhibit-and-loot museum with hostile ordinary spawner sources in both components. Displays, optional entity references and machinery do not establish functioning exhibits. No Item9 tier, measured difficulty or engineering progression gate is inferred.

## visual_discoverability

Broad above-ground museum component supplies architectural approach cues. Nominal213 by211 footprint and139 total height include a78-block lower component, so total height is not the visible silhouette. Occlusion, terrain burial and actual sightlines remain unmeasured.

## underground_surface_classification

Surface-associated main museum with a nominally subterranean lower attachment. Root generic_structure projects WORLD_SURFACE_WG offset0,size1,fixed rotation,max_distance_from_center128,beard_thin adaptation,terrain range25/radius5,biome radius2,ignore_waterlogging. Both components rigid. Pool reachability and reference geometry do not prove the lower piece passes placement/collision/world-height constraints; do not equate center-distance128 to measured size.

## Geometry and evidence

Family evidence binds templates-redacted, packaged-json-redacted and
pool-traces-content catalogs by SHA-256. Templates under
 data/idas/structure/collectors_museum/ are collectors_museum1(size213,61,211)
and collectors_museum2(size213,78,211). Main down_south0,0,210 joins lower
up_south0,77,210; aligned name/target idas:collectors_museum2 match. Adjacent
connector positions yield lower origin0,-78,0 relative to main0,0,0. Inclusive
union x0..212,z0..210,y-78..60 gives213 by211,height139. This is a nominal complete
reference assembly. The lower component is not independently observed here;
placement-envelope, collision and world-height checks may prevent full placement.
Each pool has one rigid element and empty fallback. The trace has no missing
components or unresolved elements. Root center-distance128 is not a size measure.

Both elements select collectors_museum_processor: dispenser ticking then ordinary
spawner randomization using integrated_structure_spawners/museum.json. The selected
list has zombie15,skeleton10,wraith5. Reuse pinned randomizer/manager inspection
in ../integrated-villages-provider/README.md and ticking inspection in
../idas-desert-market-assessment/README.md. All18 raw spawners have empty entity
compounds and potentials; replacement source resolution does not depend on raw IDs.
Raw paths remain in the inventory. No ordinary entity compounds are unresolved,
and neither template contains structure generation markers or trial spawners.

Runtime Mod List evidence/raw/item8/registry-r1/debug.log SHA-256
 e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b
contains Quark(line1660),Create(line1544),not alexsmobs or cloudstorage. The existing
runtime_mod_ids parser confirms this; animal and balloon references remain raw
optional data rather than effective inhabitants.

Defined museum tables under loot_table/chests/collectors_museum/ are museum_basic,
museum_bedroom,museum_farm,museum_food,museum_library,museum_space,museum_treasure.
Also defined are idas:chests/desert_pyramid/desert_pyramid,
idas:chests/desert_pyramid/desert_pyramid_tomb,
idas:chests/sunken_ship/sunken_ship_supply and minecraft:chests/jungle_temple.
Main owns the first six museum references and all four borrowed references;
lower owns basic,food,treasure. This records eleven distinct source IDs without
inferring reward counts, family aliases or working exhibits.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-collectors-museum-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only collectors_museum and input identity may change.
Final integration, acceptance and PR/review/main remain open.
