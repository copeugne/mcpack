# IDAS tree of wisdom assessment

Nine remaining entries for six connected components. Existing immutable catalogs
and the established ticking-only processor inspection suffice; no new runtime or tool.

## mob_source

All six templates contain no authored entities or unresolved entity compounds. Their selected waterlogging_fix_processor only schedules eligible dispenser/dropper ticks; it does not inject mobs. Ordinary environmental spawning remains possible.

## loot_table_source

One defined literal source, idas:chests/tree_of_wisdom/tree_of_wisdom, occurs in the top component at /block_entities/3, a Quark variant chest. The five lower components contain no loot-table references. The table contains written-book and material reward entries; this identifies sources, not measured yield. The selected ticking-only processor adds no loot NBT.

## generated_spawners

No ordinary or trial spawner blocks occur in any of the six templates. Top /block_entities/1 is a CORNER marker and /block_entities/2 a SAVE marker, both with empty metadata; neither is a DATA enemy instruction. The selected processor adds no spawners.

## authored_or_natural_enemies

No authored enemy entity, spawner or enemy generation instruction is identified. Root spawn_overrides is empty, so it declares no family-specific natural override. Environmental spawning is separate; absence of authored enemies does not guarantee a safe visit.

## intended_hostility

Loot-bearing giant-tree landmark with no identified authored hostile source. Its size does not establish dungeon difficulty or an Item9 tier. Environmental encounters remain possible.

## visual_discoverability

The large tree crown and trunk provide landmark cues, with nominal complete footprint112 by113 and height136. These template extents include padding, not measured visible silhouette or sightlines. Eligible forest surroundings and terrain can obscure approaches.

## underground_surface_classification

Surface-associated tree with rigid base/top and four terrain-matching surrounding pieces. Root generic_structure projects WORLD_SURFACE_WG offset0,size6,max_distance_from_center128,terrain range10/radius3,biome radius1,ignore_waterlogging and enhanced adaptation none. Base element separately specifies custom beards/carves kernel size35,distance35; top declares ignore_bounds and priority. Actual burial, terrain deformation and placement success are unmeasured.

## Geometry and evidence

Family evidence binds templates-redacted, packaged-json-redacted and
pool-traces-content catalogs by SHA-256. Under data/idas/structure/tree_of_wisdom/,
base1 connectors join the following component receivers (positions are x,y,z):

| Child | Base connector | Child receiver | Reference child origin | Child size |
| --- | --- | --- | --- | --- |
| 2 | up_east 28,14,17 | down_east 65,0,61 | -37,15,-44 | 112,121,113 |
| 3 | east_up 40,6,17 | west_up 0,6,61 | 41,0,-44 | 34,7,113 |
| 4 | south_up 19,6,27 | north_up 56,6,0 | -37,0,28 | 78,7,41 |
| 5 | north_up 16,6,0 | south_up 53,6,43 | -37,0,-44 | 78,7,44 |
| 6 | west_up 0,7,14 | east_up 36,7,14 | -37,0,0 | 37,8,28 |

Base size41,15,28 at origin0,0,0. All joints aligned; base target/child name
idas:top for2 and idas:tree for3..6. Origins use adjacent connector blocks.
Inclusive union x-37..74,z-44..68,y0..135 gives nominal112 by113,height136.
Base and top are rigid, while3..6 use terrain_matching: their listed y0 origins
are a flat reference, not a prediction of terrain-relative placement. Root
rotation may exchange horizontal axes. Top ignore_bounds is preserved as a
packaged flag, not proof of successful placement. No missing pools or unresolved
trace elements. Components are not alternatives or additional families.

All six pools select idas:waterlogging_fix_processor. Its sole processor ticks
minecraft:dispenser and minecraft:dropper, as inspected in
../idas-desert-market-assessment/README.md. Reuse that pinned implementation
assessment. The name does not imply further mob or loot processing.
Top template /block_entities/1,2 are empty-metadata CORNER/SAVE editor markers;
/block_entities/3 references the defined loot table. No authored entities,
unresolved entity compounds or ordinary/trial spawners occur in the templates.
The table has written-book components and material entries; no measured reward
quantity, working mechanism or progression requirement is inferred.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-tree-of-wisdom-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only tree_of_wisdom and input identity may change.
Final integration, acceptance and PR/review/main remain open.
