# IDAS ruins of the deep assessment

Seven remaining entries for four connected components. Accepted geometry reused;
no new runtime capture, renderer or measurement system.

## mob_source

Entrance authors villagers and guardvillagers:guard; upper ruins authors a turtle and non-mob item/display entities; lower ruins declares alexscaves:hullbreaker and alexsmobs:giant_squid. GuardVillagers, AlexsCaves and AlexsMobs are absent in the frozen Mod List, so their declarations do not prove generated inhabitants. Five ID-less lower-ruins entity records have empty NBT compounds; preserve paths without invented identities. Tunnel has no entities. Selected upper and lower ordinary spawner sources remain separate from direct authored entities.

## loot_table_source

Eight defined literal tables under idas:chests/ruins_of_the_deep/: ruins_basic,ruins_bedroom,ruins_create,ruins_food,ruins_library,ruins_ocean,ruins_tools,ruins_treasure. Entrance uses basic/bedroom/tools; upper ruins uses all except ocean; lower ruins uses ocean; tunnel has no literal loot reference. Selected processors add no loot NBT. Sources establish attribution, not realized yields or operational machinery.

## generated_spawners

Seventeen physical ordinary spawners:16 in upper ruins and1 in lower ruins, none in entrance/tunnel and no trial spawners. Raw upper pig/drowned data is replaced by the top processor list: quark:wraith5,quark:forgotten5,minecraft:skeleton10,minecraft:zombie10. Lower drowned data selects the bottom list, sole minecraft:drowned5. Both randomizers declare delay20,min200,max800,count4,nearby6,player range16,spawn range4,block-light0..7. Reuse existing Integrated API processor/manager semantics and fallback limitations. Upper ruins has one CORNER marker with empty metadata, not a DATA enemy instruction. These are sources and weights, not realized counts.

## authored_or_natural_enemies

Upper and lower processor-selected ordinary spawners provide distinct authored hostile sources. Civilian entrance villagers and upper turtle/display entities do not establish hostile mobs. Optional guard, hullbreaker and giant-squid declarations have absent providers; five empty entity compounds add no identifiable source. Empty root spawn_overrides declares no family-specific natural override. Environmental spawning remains separate.

## intended_hostility

Expedition assembly combines a civilian entrance, connecting tunnel and hostile spawner-bearing upper/lower ruins. Retain this internal distinction rather than treating every component as a separate family or uniformly hostile zone. No Item9 tier, realized intensity or successful optional boss encounter is claimed.

## visual_discoverability

Surface-associated entrance provides an architectural discovery cue leading through a tunnel to deeper ruins. The accepted60 by74 horizontal and103 vertical saved-piece sample describes the assembly envelope, not its visible portion. Interior extent and hostile sources need not be visible from outside; no measured sightline or guaranteed visible entrance.

## underground_surface_classification

Mixed surface entrance and deeper connected ruins. Root generic_structure projects WORLD_SURFACE_WG offset0,size5,fixed rotation,terrain range10/radius2,biome radius1,ignore_waterlogging,with enhanced adaptation none. Entrance pool separately declares custom beards/carves,kernel size17/distance17. Entrance and tunnel use ticking-only waterlogging_fix_processor; upper/lower ruins use their respective spawner processors. Root projection does not classify every connected room as surface or measure burial depth.

## Evidence and dispositions

Family evidence binds pool-traces-content, templates-redacted and packaged JSON.
Root idas:ruins_of_the_deep reaches entrance,tunnel,ruins1,ruins2 with no missing
pool component or unresolved pool element. Under data/idas/worldgen/template_pool/
ruins_of_the_deep/, ruins_of_the_deep1.json selects the top processor and
ruins_of_the_deep2.json selects bottom. Their definitions under processor_list/
ruins_of_the_deep/ contain only ordinary spawner randomization. Matching
integrated_structure_spawners/ruins_of_the_deep_top.json and _bottom.json retain
the selected weights. Reuse integrated-villages-provider/README.md's pinned
processor/manager inspection; idas-desert-market-assessment/README.md establishes
the ticking-only processor behavior used for entrance/tunnel.

The lower template's /entities/10,44,46,47,49/nbt are empty dictionaries. Retain
the raw unresolved paths as malformed source data, not unidentified enemies to
invent or a requirement to repair the frozen content. Upper /block_entities/720
is CORNER mode with empty metadata. All eight literal loot paths have packaged
definitions; this does not measure yield.

Existing runtime_mod_ids parsing of registry-r1/debug.log confirms Quark at line1660
and Create at1544, without alexscaves,alexsmobs,guardvillagers. Log SHA-256:
e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b.
Optional entity declarations are not successful inhabitants. Preserve the source
limitations without changing the baseline or marking the whole family inactive.
Accepted saved-piece sample and custody remain in idas-existing-world-geometry
and the family's bound raw manifest/restore references.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-ruins-of-the-deep-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only ruins_of_the_deep and input identity may change.
Final integration, acceptance and PR/review/main remain open.
