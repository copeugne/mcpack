# IDAS ancient mines assessment

Nine remaining entries for19 known components. Existing immutable artifacts and
explicit connector derivation suffice; no new runtime or measurement tool.

## mob_source

Direct Quark forgotten in room5,halls2,3 and toretoise in room2 are separate from optional absent AlexsMobs underminer/flutter references. Minecarts,Create glue/seats,glass frames and item entities are non-mob data, not evidence of working machinery. Halls1..4 contain eighteen empty entity NBT compounds (4,5,7,2 respectively); preserve unresolved paths without inventing their identities. Twenty-five ordinary spawners have processor-selected sources. Missing entrance2 pool limits that edge, not the separate room1 branch.

## loot_table_source

Three defined sources: idas:chests/ancient_mines/minesbasic in rooms2,3,4,6,7; minescreate in room5; mineshall in halls1,2,3,4,9. References occur in entity/container data, including chest minecarts. Hall3 additionally references missing legacy idas:chests/mineshall, preserved as a baseline content defect. Selected processors only randomize spawners and add no loot NBT. References do not establish reward yield or operating extraction systems.

## generated_spawners

Twenty-five ordinary spawner blocks, all raw potentials empty. Six top-processed spawners in rooms2(1),5(1),6(4) select spider15,cave_spider10,stray15. Nineteen bottom-processed spawners in room8(6),room9(1),halls1(1),2(4),3(3),4(2),9(2) select cave_spider15. Raw declarations include absent AlexsMobs leafcutter_ant/centipede_head, but selected randomizers replace NBT. Both use delay20,min200,max800,count4,nearby6,player16,range4,block-light0..7. No trial spawners. Hall1 marker /block_entities/12 is CORNER with empty metadata, not a DATA enemy instruction. Block counts are not successful generated or spawned counts.

## authored_or_natural_enemies

Direct forgotten and processor-selected spawners are authored hostile sources, distinct from animals and absent optional entities. Root natural monster override is piece-bound silverfish1 and Quark wraith1, each group1..1. Those weights are not population counts. Environmental spawning and realized encounters remain separate from authored source attribution.

## intended_hostility

Large underground mining-room and hall assembly with authored hostile entities, ordinary spawners and piece-bound natural hostile overrides. Missing pool/loot paths and unresolved entity records are explicit baseline limitations. No Item9 tier, measured difficulty or foundational engineering gate is inferred.

## visual_discoverability

Surface mining entrance provides the approach cue; nominal complete124 by143 footprint and119 height include extensive underground components. The entrance template itself is45 by37 horizontally and19 high. Complete extents include padding and are not a measured visible silhouette or sightline distance.

## underground_surface_classification

Surface entrance descends into rooms and a rotated hall network. Root generic_structure projects WORLD_SURFACE_WG offset0,HIGHEST_LAND,size20,terrain range10/radius1,ignore_waterlogging,enhanced adaptation none. Entrance element separately has custom beards/carves kernel35/35. All19 components rigid. Nominal layout extends100 blocks below entrance origin; terrain, collision and world-height checks may prevent full placement. Missing entrance2 is an unresolved packaged edge, not evidence that the registered root is wholly inactive.

## Geometry and evidence

Family evidence binds templates-redacted, packaged-json-redacted and
pool-traces-content by SHA-256. Template IDs below abbreviate
idas:ancient_mines/ancient_mines_. Sizes are x,y,z. Entrance/rooms use identity
orientation; all halls use R(x,y,z)=(-z,y,x). This is a quarter-turn about local
origin, so hall origins are not minimum corners. For each edge:
child_origin = parent_origin + Rparent(parent_connector) + Rparent(front_step)
               - Rchild(child_receiver).
All joints aligned and name/target IDs match on the listed edges. The missing
entrance2 target of entrance block0 is excluded without inventing a component.

| Child | Parent | Parent connector | Child receiver | Child origin | Size |
| --- | --- | --- | --- | --- | --- |
| entrance | reference | | | 0,0,0 | 45,19,37 |
| room1 | entrance | 20,0,24 down_north | 2,47,22 up_north | 18,-48,2 | 18,48,25 |
| room2 | room1 | 14,1,24 south_up | 14,1,0 north_up | 18,-48,27 | 40,9,17 |
| room3 | room1 | 14,1,0 north_up | 18,1,24 south_up | 14,-48,-23 | 31,9,25 |
| room4 | room3 | 30,1,10 east_up | 0,29,14 west_up | 45,-76,-27 | 32,37,29 |
| room5 | room2 | 39,1,3 east_up | 0,1,17 west_up | 58,-48,13 | 19,9,22 |
| room6 | room2 | 0,1,12 west_up | 46,1,3 east_up | -29,-48,36 | 47,9,27 |
| room7 | room6 | 24,1,26 south_up | 7,29,0 north_up | -12,-76,63 | 15,37,25 |
| room8 | room4 | 17,0,14 down_west | 25,23,20 up_west | 37,-100,-33 | 32,24,41 |
| room9 | room8 | 3,1,0 north_up | 5,1,20 south_up | 35,-100,-54 | 24,9,21 |
| hall1 | room8 | 3,1,40 south_up | 0,1,33 west_up | 73,-100,8 | 48,48,37 |
| hall2 | hall1 | 47,2,36 east_up | 0,2,36 west_up | 73,-100,56 | 33,48,37 |
| hall4 | hall1 | 9,1,36 south_up | 9,1,0 north_up | 36,-100,8 | 48,48,30 |
| hall3 | hall4 | 47,2,0 east_up | 0,2,0 west_up | 36,-100,56 | 33,48,30 |
| hall5 | hall4 | 47,47,0 up_west | 42,0,0 down_west | 36,-52,13 | 43,3,30 |
| hall6 | hall3 | 0,47,0 up_west | 0,0,0 down_west | 36,-52,56 | 33,3,30 |
| hall7 | hall2 | 0,47,36 up_west | 0,0,36 down_west | 73,-52,56 | 33,3,37 |
| hall8 | hall1 | 47,47,36 up_west | 42,0,36 down_west | 73,-52,13 | 43,3,37 |
| hall9 | hall1 | 47,24,0 north_up | 27,1,20 south_up | 94,-77,28 | 37,9,21 |

Transform inclusive local bounds0..size-1 by the stated rotation and origin.
Minimum x is room6(-29),maximum x hall9(94); minimum z room9(-54),maximum z
halls2/3(88); minimum y room8/halls1..4(-100),maximum y entrance(18).
Thus nominal available-component extent is124 by143,height119. Each pool has one
rigid element and empty fallback. This does not prove collision-free placement,
world-height acceptance or a realized complete assembly. Missing entrance2 remains
a packaged defect and does not erase the independent room1 connection.

Entrance,rooms1..7 select ancient_mines_top_processor; rooms8,9 and all halls
select ancient_mines_bottom_processor. Both solely randomize ordinary spawners,
with the lists and settings recorded above. Reuse the pinned randomizer/manager
inspection in ../integrated-villages-provider/README.md. No new mob/loot mechanism.
All25 raw spawner potential arrays are empty; selected NBT replacement is separate
from their authored IDs. The18 unresolved hall entity compounds are exactly empty
NBT, not resolvable identities. Hall1 marker12 is empty-metadata CORNER.

Loot references in pool-traces-content include chest-minecart entity NBT, not only
block containers. Packaged chests/ancient_mines/minesbasic,minescreate,mineshall
are defined; chests/mineshall is missing. Preserve hall3's missing legacy reference.
Frozen runtime Mod List debug.log SHA-256
 e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b
has Quark/Create but no AlexsMobs, as previously verified with runtime_mod_ids.
Optional raw underminer/flutter/ant/centipede references are not effective mobs.
No baseline repair, machinery operation or reward measurement is claimed.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-ancient-mines-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only ancient_mines and input identity may change.
Final integration, acceptance and PR/review/main remain open.
