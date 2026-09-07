# IDAS labyrinth assessment

Nine remaining entries for five connected default components. Existing immutable
catalogs and established processor inspections suffice; no new runtime or tool.

## mob_source

Floor1 authors blaze,husk,stray,cave_spider and absent-provider AlexsMobs rattlesnake/crocodile references; floor2 authors Quark forgotten and absent rattlesnakes; tomb authors husk and absent anaconda/anaconda_part references. Create glue and item entities are non-mob data. Entrances have no authored entities; no unresolved entity compounds. Floor1 ordinary spawners use the labyrinth randomizer; floor2 uses ticking-only processing and retains raw sources. Optional absent entities do not establish successful encounters.

## loot_table_source

Six literal IDs: four defined idas:chests/labyrinth/ tables (labyrinth in entrance/floor1,croc and library in floor1,tomb in floor2/tomb), and two missing legacy IDs idas:chests/labyrinth in floor1 and idas:chests/throne in floor2. Preserve these missing paths as baseline content defects, without silently correcting them. The labyrinth processor additionally appends defined idas:archeology/suspicious_sand_labyrinth to matching suspicious sand in entrance,entrance2,floor1. This is source attribution, not measured rewards.

## generated_spawners

Eighteen ordinary spawner blocks: twelve in floor1 and six in floor2. Floor1 raw blaze,husk,spider,cave_spider,stray,wraith declarations have empty potentials; labyrinth processor replaces their NBT with weighted husk15,stray10 selections. Settings delay20,min200,max800,count4,nearby6,player16,range4,light0..7. Floor2 ticking-only processing retains raw anaconda1,stray2,husk2,forgotten1 sources; both husk blocks have weight1 matching potentials and authored equipment data. AlexsMobs anaconda is absent in the frozen runtime. No trial spawners. Floor2 /block_entities/3 is an empty-metadata CORNER marker, not a DATA enemy instruction. Authored block counts are not successful spawning counts.

## authored_or_natural_enemies

Direct hostile entities and ordinary spawners supply authored encounter sources, with floor-specific processor behavior and absent optional entities preserved separately. Empty root spawn_overrides declares no family-specific natural override. Environmental spawning remains separate; no realized enemy quantity is claimed.

## intended_hostility

Layered subterranean labyrinth with authored hostile entities, ordinary spawners and tomb loot. Missing legacy loot paths and absent optional mobs limit some packaged content. No Item9 tier or measured difficulty is inferred.

## visual_discoverability

Surface entrance provides the primary approach cue; most of the nominal88-block vertical span lies below its reference origin. Nominal55 by64 footprint includes floors and tomb, not a surface-visible silhouette. Terrain burial, visibility distance and navigational difficulty are unmeasured.

## underground_surface_classification

Surface entrance leading to underground floors and a tomb. Selected default mod_adaptive_structure projects WORLD_SURFACE_WG offset0,size5,fixed rotation,terrain range10/radius1,biome radius1,ignore_waterlogging,enhanced adaptation none. Entrance element separately declares custom beards/carves kernel35/35. All five pieces rigid. Iceandfire is absent, so the documented ModAdaptive consumer keeps the default pool; compatibility alternatives are not generated family additions. Actual terrain burial, world-height acceptance and full placement remain unmeasured.

## Geometry and evidence

Family evidence binds templates-redacted, packaged-json-redacted and
pool-traces-content catalogs by SHA-256. Under data/idas/structure/labyrinth/:

| Link | Parent connector | Child receiver | Child origin | Child size |
| --- | --- | --- | --- | --- |
| entrance to entrance2 | down_west46,0,0 | up_west46,14,0 | 0,-15,0 | 47,15,39 |
| entrance2 to floor1 | down_north23,0,4 | up_north27,22,18 | -4,-38,-14 | 46,23,46 |
| floor1 to floor2 | down_north13,0,4 | up_north17,26,2 | -8,-65,-12 | 35,27,43 |
| floor2 to tomb | south_up8,4,42 | north_up0,0,0 | 0,-61,31 | 19,15,19 |

Entrance origin0,0,0,size47,23,39. Names/targets match
idas:labyrinth_entrance2,idas:labyrinthfloor1,idas:labyrinthfloor2,
idas:labyrinthtomb respectively. Vertical joints aligned; tomb joint rollable.
Opposing fronts allow the displayed reference orientation. Origins use adjacent
connector positions. Inclusive union x-8..46,z-14..49,y-65..22 gives55 by64,height88.
Each active pool has one rigid element and empty fallback. Trace has no missing
pool or unresolved element. This is nominal complete geometry, not observed
successful placement. World-height and collision constraints remain limitations.

Selected labyrinth_processor on entrance,entrance2,floor1 contains a probability1
suspicious-sand rule using modern block_entity_modifier minecraft:append_loot,
then dispenser ticking and labyrinth spawner randomization. Reuse the modern
append_loot interpretation in ../idas-dig-site-assessment/README.md and pinned
randomizer/manager inspection in ../integrated-villages-provider/README.md.
The selected list is husk15,stray10. Floor2 and tomb select only
waterlogging_fix_processor, inspected in ../idas-desert-market-assessment/README.md.
Thus floor1 spawner NBT is replaced but floor2 equipment and raw optional sources
are retained. Two floor2 husk blocks (/block_entities/10,13) have positive weight1
potentials; other floor2 spawners have empty potentials. Floor2 marker3 is CORNER
with empty metadata. No trial spawners or unresolved authored entity compounds.

Runtime Mod List in evidence/raw/item8/registry-r1/debug.log, SHA-256
 e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b,
contains Quark(line1660),Create(line1544),not iceandfire or alexsmobs. Existing
runtime_mod_ids parser confirms these memberships. The previously inspected
ModAdaptive consumer retains the default pool; inactive if_/bop templates do not
become separate families or default content. Optional anaconda parts are not
independent enemy encounters.

Packaged loot_table/chests/labyrinth/{labyrinth,labyrinth_croc,labyrinth_library,
labyrinth_tomb}.json and archeology/suspicious_sand_labyrinth.json are defined.
loot_table/chests/labyrinth.json and chests/throne.json are absent. The latter
legacy references remain attributed to floor1 and floor2 respectively, as baseline
content defects. No source correction, baseline tuning or reward experiment added.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-labyrinth-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only labyrinth and input identity may change.
Final integration, acceptance and PR/review/main remain open.
