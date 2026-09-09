# Item 12 discoverability results

Complete predeclared viewpoint matrix. See README for acceptance, review and delivery status.

Protocol: [item12-discoverability-v2](protocol.md). Human recognition and player discovery rates: NOT MEASURED.

These are family-balanced saved-world cases, not discovery probabilities. Each case retains its full family abundance per 4,096 chunks separately from geometric rays. Overworld only; other dimensions retain Item 8 source assessment and Item 10 density. Architectural/entrance judgments are in [assessments](assessments.md); navigation evidence is [separate](navigation-source/README.md).

C/O/U means CLEAR/OCCLUDED/UNKNOWN, followed by the full ray denominator. Low/high use the complete eight-cell ring; UNKNOWN means at least one missing eye. Relief can include buildings or water, not just terrain. Low and high cells also differ in azimuth, so this is not a causal elevation experiment. A clear envelope point is not a visible authored block, recognizable silhouette or entrance.

WORLD_SURFACE (WS) and MOTION_BLOCKING_NO_LEAVES (NL) use the same observer eye. NL is a foliage-sensitive heightmap comparison, not a measured no-trees world. Finite boundaries, fluid opacity, ignored overhangs/caves, purposive seeds and two repetitions limit interpretation. Zeroes do not prove absence.

## full-biome-diverse-r1-baseline

[Raw observations](results/full-biome-diverse-r1-baseline.json.gz), SHA-256 `23aafd85335bb8ede94567fc2e240c1b6d2ff3df530ff9767a2444cc515afdea`. Selected cases: 24.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| ctov:village<br>ctov:medium/village_desert@-22,10 | 1 / 4096 | regions_unexplored:saguaro_desert | 25.0 | 3/2/0 of 5; 3/2/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 11/29/0 of 40; 11/29/0 of 40 |
| explorations:desert_ruin<br>explorations:desert_ruin@27,-21 | 1 / 4096 | minecraft:desert | 21.0 | 4/1/0 of 5; 4/1/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 12/28/0 of 40; 12/28/0 of 40 |
| explorations:scarecrow<br>nonregistry:0 | 1 / 4096 | terralith:bryce_canyon | 13.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| explorations:slime_cave<br>explorations:slime_cave@-25,12 | 4 / 4096 | minecraft:dripstone_caves | 11.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@-17,19 | 3 / 4096 | minecraft:dripstone_caves | 24.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:underground_camp<br>idas:underground_camp/underground_camp@-31,0 | 1 / 4096 | terralith:cave/granite_caves | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| minecraft:nether_fossil<br>minecraft:nether_fossil@9,24 | 7 / 4096 | biomesoplenty:dryland | 24.0 | 0/5/0 of 5; 0/5/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 15/25/0 of 40; 21/19/0 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_desert@7,11 | 1 / 4096 | terralith:lush_desert | 14.0 | 3/2/0 of 5; 3/2/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 32/8/0 of 40; 34/6/0 of 40 |
| minecraft:trial_chambers<br>minecraft:trial_chambers@16,26 | 1 / 4096 | biomesoplenty:dryland | 12.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mss:desert_pyramid<br>mss:desert_pyramid@8,29 | 1 / 4096 | biomesoplenty:dryland | None | UNKNOWN extremum | UNKNOWN extremum | 18/17/5 of 40; 18/17/5 of 40 |
| mvs:cart<br>mvs:cart@14,20 | 1 / 4096 | biomesoplenty:lush_desert | 11.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 5/0/0 of 5 | 2/38/0 of 40; 9/31/0 of 40 |
| mvs:dead_tree<br>mvs:dead_tree_oak@8,7 | 1 / 4096 | biomesoplenty:wasteland | 27.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 7/33/0 of 40; 11/29/0 of 40 |
| mvs:floating_islands<br>mvs:floating_islands@29,17 | 1 / 4096 | biomesoplenty:wasteland | None | UNKNOWN extremum | UNKNOWN extremum | 20/15/5 of 40; 21/14/5 of 40 |
| mvs:harvest_heap<br>mvs:haystack@5,10 | 3 / 4096 | biomesoplenty:wasteland | 20.0 | 0/5/0 of 5; 0/5/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 15/25/0 of 40; 19/21/0 of 40 |
| mvs:well<br>mvs:small_tower_well@16,17 | 2 / 4096 | terralith:lush_desert | 11.0 | 1/4/0 of 5; 1/4/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 13/27/0 of 40; 13/27/0 of 40 |
| mvs:windmill<br>mvs:windmill@18,22 | 1 / 4096 | biomesoplenty:dryland | 17.0 | 0/5/0 of 5; 0/5/0 of 5 | 1/4/0 of 5; 1/4/0 of 5 | 4/36/0 of 40; 4/36/0 of 40 |
| mvs:wooden_wheat_farm<br>mvs:wooden_wheat_farm@7,7 | 1 / 4096 | biomesoplenty:wasteland | 23.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 8/32/0 of 40; 8/32/0 of 40 |
| quark:monster_box<br>nonregistry:3828 | 326 / 4096 | biomesoplenty:spider_nest | None | UNKNOWN extremum | UNKNOWN extremum | 0/7/1 of 8; 0/7/1 of 8 |
| supplementaries:cave_urn_cache<br>nonregistry:17637 | 3755 / 4096 | biomesoplenty:spider_nest | 15.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| supplementaries:road_sign<br>supplementaries:road_sign@10,2 | 1 / 4096 | biomesoplenty:wasteland | 24.0 | 5/0/0 of 5; 5/0/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 20/20/0 of 40; 20/20/0 of 40 |
| towns_and_towers:desert_mimic<br>towns_and_towers:mimic_desert@21,17 | 1 / 4096 | minecraft:desert | 14.0 | 3/2/0 of 5; 3/2/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 19/21/0 of 40; 19/21/0 of 40 |
| yungsextras:desert_obelisk<br>nonregistry:31422 | 2 / 4096 | biomesoplenty:lush_desert | 28.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| yungsextras:desert_small_ruins<br>nonregistry:31425 | 2 / 4096 | biomesoplenty:lush_desert | None | UNKNOWN extremum | UNKNOWN extremum | 0/5/3 of 8; 0/5/3 of 8 |
| yungsextras:desert_well<br>nonregistry:31431 | 3 / 4096 | minecraft:desert | 20.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| biomesoplenty:dryland | 4 | 37/118/5 of 160 | 43/112/5 of 160 | 6 / 160 |
| biomesoplenty:lush_desert | 3 | 2/51/3 of 56 | 9/44/3 of 56 | 7 / 56 |
| biomesoplenty:spider_nest | 2 | 0/15/1 of 16 | 0/15/1 of 16 | 0 / 16 |
| biomesoplenty:wasteland | 5 | 70/125/5 of 200 | 79/116/5 of 200 | 9 / 200 |
| minecraft:desert | 3 | 31/57/0 of 88 | 31/57/0 of 88 | 0 / 88 |
| minecraft:dripstone_caves | 2 | 0/80/0 of 80 | 0/80/0 of 80 | 0 / 80 |
| regions_unexplored:saguaro_desert | 1 | 11/29/0 of 40 | 11/29/0 of 40 | 0 / 40 |
| terralith:bryce_canyon | 1 | 0/8/0 of 8 | 0/8/0 of 8 | 0 / 8 |
| terralith:cave/granite_caves | 1 | 0/25/15 of 40 | 0/25/15 of 40 | 0 / 40 |
| terralith:lush_desert | 2 | 45/35/0 of 80 | 47/33/0 of 80 | 2 / 80 |

## full-biome-diverse-r1-without-sparse

[Raw observations](results/full-biome-diverse-r1-without-sparse.json.gz), SHA-256 `70caa7dd0af6763623602832dc3712d74a9b647af1f07a172816fa0498bb26e6`. Selected cases: 49.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| adorabuild_structures:house<br>adorabuild_structures:red_sand_house_medium_1@-30,19 | 1 / 4096 | terralith:bryce_canyon | None | UNKNOWN extremum | UNKNOWN extremum | 3/22/15 of 40; 9/16/15 of 40 |
| betterdungeons:small_dungeon<br>betterdungeons:small_dungeon@-19,13 | 2 / 4096 | minecraft:dripstone_caves | 16.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| ctov:pillager_outpost<br>ctov:pillager_outpost_desert@-10,3 | 1 / 4096 | regions_unexplored:saguaro_desert | 7.0 | 4/1/0 of 5; 4/1/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 35/5/0 of 40; 35/5/0 of 40 |
| ctov:village<br>ctov:medium/village_desert@-22,10 | 1 / 4096 | regions_unexplored:saguaro_desert | 25.0 | 3/2/0 of 5; 3/2/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 20/20/0 of 40; 21/19/0 of 40 |
| explorations:desert_ruin<br>explorations:desert_ruin@27,-20 | 2 / 4096 | minecraft:desert | 29.0 | 4/1/0 of 5; 4/1/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 12/28/0 of 40; 12/28/0 of 40 |
| explorations:scarecrow<br>nonregistry:1 | 2 / 4096 | regions_unexplored:eucalyptus_forest | None | UNKNOWN extremum | UNKNOWN extremum | 0/5/3 of 8; 0/5/3 of 8 |
| explorations:slime_cave<br>explorations:slime_cave@22,1 | 16 / 4096 | biomesoplenty:spider_nest | 24.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@23,26 | 9 / 4096 | terralith:cave/granite_caves | 3.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorify:desert_shrine<br>explorify:desert_shrine@-13,14 | 1 / 4096 | regions_unexplored:saguaro_desert | 20.0 | 0/5/0 of 5; 1/4/0 of 5 | 3/2/0 of 5; 3/2/0 of 5 | 10/30/0 of 40; 11/29/0 of 40 |
| explorify:supply_cache<br>explorify:supply_cache/desert@-29,9 | 1 / 4096 | regions_unexplored:joshua_desert | None | UNKNOWN extremum | UNKNOWN extremum | 4/31/5 of 40; 4/31/5 of 40 |
| idas:desert_camp<br>idas:desert_camp/desert_camp@30,27 | 3 / 4096 | terralith:sandstone_valley | None | UNKNOWN extremum | UNKNOWN extremum | 5/20/15 of 40; 7/18/15 of 40 |
| idas:desert_market<br>idas:desert_market/desert_market_orange@1,-21 | 1 / 4096 | biomesoplenty:lush_desert | 23.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 19/21/0 of 40; 20/20/0 of 40 |
| idas:underground_camp<br>idas:underground_camp/underground_camp_deep@26,27 | 3 / 4096 | terralith:cave/granite_caves | 54.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| integrated_villages:village<br>integrated_villages:airship_village@10,3 | 1 / 4096 | biomesoplenty:wasteland | 150.0 | 2/3/0 of 5; 2/3/0 of 5 | 3/2/0 of 5; 3/2/0 of 5 | 21/19/0 of 40; 21/19/0 of 40 |
| minecraft:nether_fossil<br>minecraft:nether_fossil@12,28 | 28 / 4096 | biomesoplenty:dryland | None | UNKNOWN extremum | UNKNOWN extremum | 0/35/5 of 40; 3/32/5 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_desert@-22,-20 | 3 / 4096 | biomesoplenty:wasteland | 32.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 14/26/0 of 40; 15/25/0 of 40 |
| minecraft:trial_chambers<br>minecraft:trial_chambers@-26,7 | 4 / 4096 | terralith:cave/granite_caves | 16.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mss:castle_ruin<br>mss:castle_ruin@20,6 | 1 / 4096 | biomesoplenty:wasteland | 16.0 | 3/2/0 of 5; 3/2/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 20/20/0 of 40; 20/20/0 of 40 |
| mss:castle_tower<br>mss:castle_tower@12,15 | 1 / 4096 | terralith:lush_desert | 12.0 | 2/3/0 of 5; 2/3/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 22/18/0 of 40; 23/17/0 of 40 |
| mss:diorite_house<br>mss:diorite_house@16,28 | 1 / 4096 | biomesoplenty:dryland | 12.0 | 2/3/0 of 5; 2/3/0 of 5 | 3/2/0 of 5; 3/2/0 of 5 | 19/21/0 of 40; 19/21/0 of 40 |
| mss:red_sand<br>mss:red_sand@5,31 | 1 / 4096 | biomesoplenty:dryland | None | UNKNOWN extremum | UNKNOWN extremum | 8/11/21 of 40; 8/11/21 of 40 |
| mvs:cart<br>mvs:cart@11,10 | 1 / 4096 | biomesoplenty:wasteland | 147.0 | 5/0/0 of 5; 5/0/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 15/25/0 of 40; 15/25/0 of 40 |
| mvs:cartographer_tower<br>mvs:cartographer_tower@13,29 | 1 / 4096 | biomesoplenty:dryland | None | UNKNOWN extremum | UNKNOWN extremum | 15/20/5 of 40; 15/20/5 of 40 |
| mvs:desert_pump<br>mvs:desert_pump@-18,10 | 1 / 4096 | regions_unexplored:saguaro_desert | 26.0 | 0/5/0 of 5; 0/5/0 of 5 | 1/4/0 of 5; 1/4/0 of 5 | 9/31/0 of 40; 9/31/0 of 40 |
| mvs:harvest_heap<br>mvs:pile@3,3 | 14 / 4096 | biomesoplenty:wasteland | 152.0 | 5/0/0 of 5; 5/0/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 19/21/0 of 40; 19/21/0 of 40 |
| mvs:lantern<br>mvs:small_oak_lantern@16,-21 | 3 / 4096 | minecraft:desert | 23.0 | 3/0/0 of 3; 3/0/0 of 3 | 0/3/0 of 3; 0/3/0 of 3 | 17/7/0 of 24; 17/7/0 of 24 |
| mvs:large_warped_tower<br>mvs:large_warped_tower@3,27 | 1 / 4096 | biomesoplenty:lush_desert | 27.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 34/6/0 of 40; 36/4/0 of 40 |
| mvs:living_tree<br>mvs:oak_tree@2,-27 | 2 / 4096 | biomesoplenty:lush_savanna | 6.0 | 4/1/0 of 5; 5/0/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 15/25/0 of 40; 19/21/0 of 40 |
| mvs:paths<br>mvs:paths@24,3 | 1 / 4096 | biomesoplenty:wasteland | 21.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 30/10/0 of 40; 31/9/0 of 40 |
| mvs:pond<br>mvs:small_oak_pond@4,-26 | 2 / 4096 | biomesoplenty:lush_savanna | 30.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 11/29/0 of 40; 13/27/0 of 40 |
| mvs:stall<br>mvs:pink_stall@11,16 | 1 / 4096 | terralith:lush_desert | 19.0 | 0/5/0 of 5; 0/5/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 16/24/0 of 40; 19/21/0 of 40 |
| mvs:villager_statue<br>mvs:villager_statue@10,13 | 1 / 4096 | terralith:lush_desert | 13.0 | 4/1/0 of 5; 4/1/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 23/17/0 of 40; 23/17/0 of 40 |
| mvs:well<br>mvs:small_well@6,1 | 2 / 4096 | biomesoplenty:wasteland | 26.0 | 5/0/0 of 5; 5/0/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 24/16/0 of 40; 24/16/0 of 40 |
| mvs:wheat_grain_bin<br>mvs:wheat_grain_bin@18,-29 | 3 / 4096 | regions_unexplored:outback | None | UNKNOWN extremum | UNKNOWN extremum | 19/16/5 of 40; 23/12/5 of 40 |
| mvs:windmill<br>mvs:windmill@-24,13 | 3 / 4096 | regions_unexplored:joshua_desert | 14.0 | 0/5/0 of 5; 0/5/0 of 5 | 2/3/0 of 5; 3/2/0 of 5 | 2/38/0 of 40; 3/37/0 of 40 |
| mvs:wooden_wheat_farm<br>mvs:wooden_wheat_farm@-26,1 | 4 / 4096 | terralith:lush_desert | 22.0 | 3/2/0 of 5; 3/2/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 17/23/0 of 40; 22/18/0 of 40 |
| quark:monster_box<br>nonregistry:1232 | 327 / 4096 | biomesoplenty:spider_nest | None | UNKNOWN extremum | UNKNOWN extremum | 0/7/1 of 8; 0/7/1 of 8 |
| repurposed_structures:outpost<br>repurposed_structures:outpost_desert@13,20 | 1 / 4096 | biomesoplenty:lush_desert | 12.0 | 1/4/0 of 5; 1/4/0 of 5 | 3/2/0 of 5; 4/1/0 of 5 | 27/13/0 of 40; 30/10/0 of 40 |
| repurposed_structures:ruins<br>repurposed_structures:ruins_land_hot@-31,15 | 1 / 4096 | minecraft:wooded_badlands | None | UNKNOWN extremum | UNKNOWN extremum | 6/15/19 of 40; 7/13/20 of 40 |
| supplementaries:cave_urn_cache<br>nonregistry:19816 | 3762 / 4096 | biomesoplenty:wasteland | 24.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| supplementaries:road_sign<br>supplementaries:road_sign@-31,24 | 1 / 4096 | terralith:bryce_canyon | None | UNKNOWN extremum | UNKNOWN extremum | 4/21/15 of 40; 18/7/15 of 40 |
| terralith:rubble<br>terralith:rubble_desert@-23,27 | 1 / 4096 | minecraft:desert | 24.0 | 0/5/0 of 5; 4/1/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 12/28/0 of 40; 28/12/0 of 40 |
| terralith:underground/mining_outpost<br>terralith:underground/mining_outpost@29,-26 | 1 / 4096 | terralith:cave/deep_caves | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| terralith:underground/old_refinery<br>terralith:underground/old_refinery@-17,16 | 1 / 4096 | terralith:cave/deep_caves | 11.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| towns_and_towers:village<br>towns_and_towers:exclusives/village_iberian@5,-28 | 1 / 4096 | biomesoplenty:lush_savanna | 20.0 | 2/3/0 of 5; 2/3/0 of 5 | 3/2/0 of 5; 5/0/0 of 5 | 22/18/0 of 40; 25/15/0 of 40 |
| yungsextras:desert_giant_torch<br>nonregistry:31424 | 1 / 4096 | minecraft:desert | 31.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 1/7/0 of 8 |
| yungsextras:desert_obelisk<br>nonregistry:31425 | 2 / 4096 | minecraft:desert | 32.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 2/6/0 of 8; 3/5/0 of 8 |
| yungsextras:desert_small_ruins<br>nonregistry:31430 | 2 / 4096 | biomesoplenty:lush_desert | None | UNKNOWN extremum | UNKNOWN extremum | 0/5/3 of 8; 0/5/3 of 8 |
| yungsextras:desert_well<br>nonregistry:31439 | 3 / 4096 | minecraft:desert | 13.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| biomesoplenty:dryland | 4 | 42/87/31 of 160 | 45/84/31 of 160 | 3 / 160 |
| biomesoplenty:lush_desert | 4 | 80/45/3 of 128 | 86/39/3 of 128 | 6 / 128 |
| biomesoplenty:lush_savanna | 3 | 48/72/0 of 120 | 57/63/0 of 120 | 9 / 120 |
| biomesoplenty:spider_nest | 2 | 0/47/1 of 48 | 0/47/1 of 48 | 0 / 48 |
| biomesoplenty:wasteland | 8 | 143/145/0 of 288 | 145/143/0 of 288 | 2 / 288 |
| minecraft:desert | 6 | 43/85/0 of 128 | 61/67/0 of 128 | 18 / 128 |
| minecraft:dripstone_caves | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| minecraft:wooded_badlands | 1 | 6/15/19 of 40 | 7/13/20 of 40 | 1 / 40 |
| regions_unexplored:eucalyptus_forest | 1 | 0/5/3 of 8 | 0/5/3 of 8 | 0 / 8 |
| regions_unexplored:joshua_desert | 2 | 6/69/5 of 80 | 7/68/5 of 80 | 1 / 80 |
| regions_unexplored:outback | 1 | 19/16/5 of 40 | 23/12/5 of 40 | 4 / 40 |
| regions_unexplored:saguaro_desert | 4 | 74/86/0 of 160 | 76/84/0 of 160 | 2 / 160 |
| terralith:bryce_canyon | 2 | 7/43/30 of 80 | 27/23/30 of 80 | 20 / 80 |
| terralith:cave/deep_caves | 2 | 0/65/15 of 80 | 0/65/15 of 80 | 0 / 80 |
| terralith:cave/granite_caves | 3 | 0/120/0 of 120 | 0/120/0 of 120 | 0 / 120 |
| terralith:lush_desert | 4 | 78/82/0 of 160 | 87/73/0 of 160 | 9 / 160 |
| terralith:sandstone_valley | 1 | 5/20/15 of 40 | 7/18/15 of 40 | 2 / 40 |

## full-biome-diverse-r2-baseline

[Raw observations](results/full-biome-diverse-r2-baseline.json.gz), SHA-256 `ed01a9206f1c3e136490e05145c5b3cb1222a03100cd639b61fa64c9138a3392`. Selected cases: 24.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| ctov:village<br>ctov:medium/village_desert@-22,10 | 1 / 4096 | regions_unexplored:saguaro_desert | 25.0 | 3/2/0 of 5; 3/2/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 16/24/0 of 40; 17/23/0 of 40 |
| explorations:desert_ruin<br>explorations:desert_ruin@27,-21 | 1 / 4096 | minecraft:desert | 21.0 | 4/1/0 of 5; 4/1/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 12/28/0 of 40; 12/28/0 of 40 |
| explorations:scarecrow<br>nonregistry:1 | 2 / 4096 | biomesoplenty:lush_savanna | 22.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| explorations:slime_cave<br>explorations:slime_cave@-25,12 | 4 / 4096 | minecraft:dripstone_caves | 11.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@-17,19 | 3 / 4096 | minecraft:dripstone_caves | 24.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:underground_camp<br>idas:underground_camp/underground_camp@-31,0 | 1 / 4096 | terralith:cave/granite_caves | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| minecraft:nether_fossil<br>minecraft:nether_fossil@9,24 | 7 / 4096 | biomesoplenty:dryland | 24.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 1/4/0 of 5 | 11/29/0 of 40; 13/27/0 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_desert@7,11 | 1 / 4096 | terralith:lush_desert | 14.0 | 3/2/0 of 5; 3/2/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 31/9/0 of 40; 34/6/0 of 40 |
| minecraft:trial_chambers<br>minecraft:trial_chambers@16,26 | 1 / 4096 | biomesoplenty:dryland | 12.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mss:desert_pyramid<br>mss:desert_pyramid@8,29 | 1 / 4096 | biomesoplenty:dryland | None | UNKNOWN extremum | UNKNOWN extremum | 18/17/5 of 40; 18/17/5 of 40 |
| mvs:cart<br>mvs:cart@14,20 | 1 / 4096 | biomesoplenty:lush_desert | 11.0 | 0/5/0 of 5; 0/5/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 7/33/0 of 40; 9/31/0 of 40 |
| mvs:dead_tree<br>mvs:dead_tree_oak@8,7 | 1 / 4096 | biomesoplenty:wasteland | 27.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 7/33/0 of 40; 11/29/0 of 40 |
| mvs:floating_islands<br>mvs:floating_islands@29,17 | 1 / 4096 | biomesoplenty:wasteland | None | UNKNOWN extremum | UNKNOWN extremum | 20/15/5 of 40; 21/14/5 of 40 |
| mvs:harvest_heap<br>mvs:haystack@5,10 | 3 / 4096 | biomesoplenty:wasteland | 20.0 | 0/5/0 of 5; 0/5/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 12/28/0 of 40; 16/24/0 of 40 |
| mvs:well<br>mvs:small_tower_well@16,17 | 2 / 4096 | terralith:lush_desert | 11.0 | 1/4/0 of 5; 1/4/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 10/30/0 of 40; 12/28/0 of 40 |
| mvs:windmill<br>mvs:windmill@18,22 | 1 / 4096 | biomesoplenty:dryland | 17.0 | 0/5/0 of 5; 0/5/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 5/35/0 of 40; 5/35/0 of 40 |
| mvs:wooden_wheat_farm<br>mvs:wooden_wheat_farm@7,7 | 1 / 4096 | biomesoplenty:wasteland | 23.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 8/32/0 of 40; 8/32/0 of 40 |
| quark:monster_box<br>nonregistry:1232 | 323 / 4096 | biomesoplenty:spider_nest | None | UNKNOWN extremum | UNKNOWN extremum | 0/7/1 of 8; 0/7/1 of 8 |
| supplementaries:cave_urn_cache<br>nonregistry:18136 | 3796 / 4096 | minecraft:dripstone_caves | 18.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| supplementaries:road_sign<br>supplementaries:road_sign@10,2 | 1 / 4096 | biomesoplenty:wasteland | 24.0 | 5/0/0 of 5; 5/0/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 20/20/0 of 40; 20/20/0 of 40 |
| towns_and_towers:desert_mimic<br>towns_and_towers:mimic_desert@21,17 | 1 / 4096 | minecraft:desert | 14.0 | 2/3/0 of 5; 2/3/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 19/21/0 of 40; 19/21/0 of 40 |
| yungsextras:desert_obelisk<br>nonregistry:31423 | 2 / 4096 | minecraft:desert | 32.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 3/5/0 of 8; 3/5/0 of 8 |
| yungsextras:desert_small_ruins<br>nonregistry:31429 | 2 / 4096 | biomesoplenty:lush_desert | None | UNKNOWN extremum | UNKNOWN extremum | 0/5/3 of 8; 0/5/3 of 8 |
| yungsextras:desert_well<br>nonregistry:31437 | 4 / 4096 | biomesoplenty:lush_desert | 19.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| biomesoplenty:dryland | 4 | 34/121/5 of 160 | 36/119/5 of 160 | 2 / 160 |
| biomesoplenty:lush_desert | 3 | 7/46/3 of 56 | 9/44/3 of 56 | 2 / 56 |
| biomesoplenty:lush_savanna | 1 | 0/8/0 of 8 | 0/8/0 of 8 | 0 / 8 |
| biomesoplenty:spider_nest | 1 | 0/7/1 of 8 | 0/7/1 of 8 | 0 / 8 |
| biomesoplenty:wasteland | 5 | 67/128/5 of 200 | 76/119/5 of 200 | 9 / 200 |
| minecraft:desert | 3 | 34/54/0 of 88 | 34/54/0 of 88 | 0 / 88 |
| minecraft:dripstone_caves | 3 | 0/88/0 of 88 | 0/88/0 of 88 | 0 / 88 |
| regions_unexplored:saguaro_desert | 1 | 16/24/0 of 40 | 17/23/0 of 40 | 1 / 40 |
| terralith:cave/granite_caves | 1 | 0/25/15 of 40 | 0/25/15 of 40 | 0 / 40 |
| terralith:lush_desert | 2 | 41/39/0 of 80 | 46/34/0 of 80 | 5 / 80 |

## full-biome-diverse-r2-without-sparse

[Raw observations](results/full-biome-diverse-r2-without-sparse.json.gz), SHA-256 `c84dd263baf4a34a347592268055f2b430be0e043b1038481bb5fb29f68e9cf1`. Selected cases: 49.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| adorabuild_structures:house<br>adorabuild_structures:red_sand_house_medium_1@-30,19 | 1 / 4096 | terralith:bryce_canyon | None | UNKNOWN extremum | UNKNOWN extremum | 3/22/15 of 40; 11/14/15 of 40 |
| betterdungeons:small_dungeon<br>betterdungeons:small_dungeon@-19,13 | 2 / 4096 | minecraft:dripstone_caves | 16.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| ctov:pillager_outpost<br>ctov:pillager_outpost_desert@-10,3 | 1 / 4096 | regions_unexplored:saguaro_desert | 7.0 | 5/0/0 of 5; 5/0/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 35/5/0 of 40; 36/4/0 of 40 |
| ctov:village<br>ctov:medium/village_desert@-22,10 | 1 / 4096 | regions_unexplored:saguaro_desert | 25.0 | 3/2/0 of 5; 3/2/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 22/18/0 of 40; 23/17/0 of 40 |
| explorations:desert_ruin<br>explorations:desert_ruin@27,-20 | 2 / 4096 | minecraft:desert | 29.0 | 4/1/0 of 5; 4/1/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 12/28/0 of 40; 12/28/0 of 40 |
| explorations:scarecrow<br>nonregistry:1 | 2 / 4096 | terralith:bryce_canyon | 13.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| explorations:slime_cave<br>explorations:slime_cave@22,1 | 16 / 4096 | biomesoplenty:spider_nest | 24.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@23,26 | 9 / 4096 | terralith:cave/granite_caves | 3.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorify:desert_shrine<br>explorify:desert_shrine@-13,14 | 1 / 4096 | regions_unexplored:saguaro_desert | 20.0 | 0/5/0 of 5; 1/4/0 of 5 | 3/2/0 of 5; 3/2/0 of 5 | 9/31/0 of 40; 10/30/0 of 40 |
| explorify:supply_cache<br>explorify:supply_cache/desert@-29,9 | 1 / 4096 | regions_unexplored:joshua_desert | None | UNKNOWN extremum | UNKNOWN extremum | 8/27/5 of 40; 14/21/5 of 40 |
| idas:desert_camp<br>idas:desert_camp/desert_camp@30,27 | 3 / 4096 | terralith:sandstone_valley | None | UNKNOWN extremum | UNKNOWN extremum | 7/18/15 of 40; 8/17/15 of 40 |
| idas:desert_market<br>idas:desert_market/desert_market_orange@1,-21 | 1 / 4096 | biomesoplenty:lush_desert | 23.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 16/24/0 of 40; 19/21/0 of 40 |
| idas:underground_camp<br>idas:underground_camp/underground_camp_deep@26,27 | 3 / 4096 | terralith:cave/granite_caves | 54.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| integrated_villages:village<br>integrated_villages:airship_village@10,3 | 1 / 4096 | biomesoplenty:wasteland | 150.0 | 1/4/0 of 5; 2/3/0 of 5 | 3/2/0 of 5; 3/2/0 of 5 | 20/20/0 of 40; 21/19/0 of 40 |
| minecraft:nether_fossil<br>minecraft:nether_fossil@12,28 | 28 / 4096 | biomesoplenty:dryland | None | UNKNOWN extremum | UNKNOWN extremum | 0/35/5 of 40; 3/32/5 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_desert@-22,-20 | 3 / 4096 | biomesoplenty:wasteland | 32.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 16/24/0 of 40; 16/24/0 of 40 |
| minecraft:trial_chambers<br>minecraft:trial_chambers@-26,7 | 4 / 4096 | terralith:cave/granite_caves | 16.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mss:castle_ruin<br>mss:castle_ruin@20,6 | 1 / 4096 | biomesoplenty:wasteland | 16.0 | 3/2/0 of 5; 3/2/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 20/20/0 of 40; 20/20/0 of 40 |
| mss:castle_tower<br>mss:castle_tower@12,15 | 1 / 4096 | terralith:lush_desert | 12.0 | 2/3/0 of 5; 2/3/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 22/18/0 of 40; 23/17/0 of 40 |
| mss:diorite_house<br>mss:diorite_house@16,28 | 1 / 4096 | biomesoplenty:dryland | 12.0 | 2/3/0 of 5; 2/3/0 of 5 | 3/2/0 of 5; 3/2/0 of 5 | 19/21/0 of 40; 19/21/0 of 40 |
| mss:red_sand<br>mss:red_sand@5,31 | 1 / 4096 | biomesoplenty:dryland | None | UNKNOWN extremum | UNKNOWN extremum | 8/11/21 of 40; 8/11/21 of 40 |
| mvs:cart<br>mvs:cart@11,10 | 1 / 4096 | biomesoplenty:wasteland | 147.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 10/30/0 of 40; 10/30/0 of 40 |
| mvs:cartographer_tower<br>mvs:cartographer_tower@13,29 | 1 / 4096 | biomesoplenty:dryland | None | UNKNOWN extremum | UNKNOWN extremum | 11/24/5 of 40; 12/23/5 of 40 |
| mvs:desert_pump<br>mvs:desert_pump@-18,10 | 1 / 4096 | regions_unexplored:saguaro_desert | 26.0 | 0/5/0 of 5; 0/5/0 of 5 | 1/4/0 of 5; 1/4/0 of 5 | 8/32/0 of 40; 8/32/0 of 40 |
| mvs:harvest_heap<br>mvs:pile@3,3 | 14 / 4096 | biomesoplenty:wasteland | 152.0 | 5/0/0 of 5; 5/0/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 18/22/0 of 40; 18/22/0 of 40 |
| mvs:lantern<br>mvs:small_oak_lantern@16,-21 | 3 / 4096 | minecraft:desert | 23.0 | 3/0/0 of 3; 3/0/0 of 3 | 0/3/0 of 3; 0/3/0 of 3 | 17/7/0 of 24; 17/7/0 of 24 |
| mvs:large_warped_tower<br>mvs:large_warped_tower@3,27 | 1 / 4096 | biomesoplenty:lush_desert | 27.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 33/7/0 of 40; 36/4/0 of 40 |
| mvs:living_tree<br>mvs:oak_tree@2,-27 | 2 / 4096 | biomesoplenty:lush_savanna | 6.0 | 4/1/0 of 5; 5/0/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 14/26/0 of 40; 18/22/0 of 40 |
| mvs:paths<br>mvs:paths@24,3 | 1 / 4096 | biomesoplenty:wasteland | 21.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 31/9/0 of 40; 31/9/0 of 40 |
| mvs:pond<br>mvs:small_oak_pond@4,-26 | 2 / 4096 | biomesoplenty:lush_savanna | 30.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 11/29/0 of 40; 13/27/0 of 40 |
| mvs:stall<br>mvs:pink_stall@11,16 | 1 / 4096 | terralith:lush_desert | 19.0 | 2/3/0 of 5; 2/3/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 19/21/0 of 40; 25/15/0 of 40 |
| mvs:villager_statue<br>mvs:villager_statue@10,13 | 1 / 4096 | terralith:lush_desert | 13.0 | 4/1/0 of 5; 4/1/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 21/19/0 of 40; 21/19/0 of 40 |
| mvs:well<br>mvs:small_well@6,1 | 2 / 4096 | biomesoplenty:wasteland | 26.0 | 5/0/0 of 5; 5/0/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 23/17/0 of 40; 25/15/0 of 40 |
| mvs:wheat_grain_bin<br>mvs:wheat_grain_bin@18,-29 | 3 / 4096 | regions_unexplored:outback | None | UNKNOWN extremum | UNKNOWN extremum | 20/15/5 of 40; 23/12/5 of 40 |
| mvs:windmill<br>mvs:windmill@-24,13 | 3 / 4096 | regions_unexplored:joshua_desert | 14.0 | 0/5/0 of 5; 0/5/0 of 5 | 3/2/0 of 5; 3/2/0 of 5 | 3/37/0 of 40; 3/37/0 of 40 |
| mvs:wooden_wheat_farm<br>mvs:wooden_wheat_farm@-26,1 | 4 / 4096 | terralith:lush_desert | 22.0 | 3/2/0 of 5; 3/2/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 17/23/0 of 40; 21/19/0 of 40 |
| quark:monster_box<br>nonregistry:1232 | 328 / 4096 | biomesoplenty:spider_nest | None | UNKNOWN extremum | UNKNOWN extremum | 0/7/1 of 8; 0/7/1 of 8 |
| repurposed_structures:outpost<br>repurposed_structures:outpost_desert@13,20 | 1 / 4096 | biomesoplenty:lush_desert | 12.0 | 1/4/0 of 5; 1/4/0 of 5 | 3/2/0 of 5; 4/1/0 of 5 | 26/14/0 of 40; 29/11/0 of 40 |
| repurposed_structures:ruins<br>repurposed_structures:ruins_land_hot@-31,15 | 1 / 4096 | minecraft:wooded_badlands | None | UNKNOWN extremum | UNKNOWN extremum | 5/14/21 of 40; 6/12/22 of 40 |
| supplementaries:cave_urn_cache<br>nonregistry:7114 | 3800 / 4096 | terralith:cave/granite_caves | 6.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| supplementaries:road_sign<br>supplementaries:road_sign@-31,24 | 1 / 4096 | terralith:bryce_canyon | None | UNKNOWN extremum | UNKNOWN extremum | 3/22/15 of 40; 9/16/15 of 40 |
| terralith:rubble<br>terralith:rubble_desert@-23,27 | 1 / 4096 | minecraft:desert | 24.0 | 0/5/0 of 5; 1/4/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 16/24/0 of 40; 21/19/0 of 40 |
| terralith:underground/mining_outpost<br>terralith:underground/mining_outpost@29,-26 | 1 / 4096 | terralith:cave/deep_caves | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| terralith:underground/old_refinery<br>terralith:underground/old_refinery@-17,16 | 1 / 4096 | terralith:cave/deep_caves | 11.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| towns_and_towers:village<br>towns_and_towers:exclusives/village_iberian@5,-28 | 1 / 4096 | biomesoplenty:lush_savanna | 20.0 | 2/3/0 of 5; 2/3/0 of 5 | 3/2/0 of 5; 5/0/0 of 5 | 21/19/0 of 40; 24/16/0 of 40 |
| yungsextras:desert_giant_torch<br>nonregistry:31421 | 1 / 4096 | minecraft:desert | None | UNKNOWN extremum | UNKNOWN extremum | 1/6/1 of 8; 2/5/1 of 8 |
| yungsextras:desert_obelisk<br>nonregistry:31425 | 2 / 4096 | biomesoplenty:lush_desert | 37.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| yungsextras:desert_small_ruins<br>nonregistry:31426 | 3 / 4096 | biomesoplenty:lush_desert | 17.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| yungsextras:desert_well<br>nonregistry:31437 | 7 / 4096 | minecraft:desert | 9.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| biomesoplenty:dryland | 4 | 38/91/31 of 160 | 42/87/31 of 160 | 4 / 160 |
| biomesoplenty:lush_desert | 5 | 75/61/0 of 136 | 84/52/0 of 136 | 9 / 136 |
| biomesoplenty:lush_savanna | 3 | 46/74/0 of 120 | 55/65/0 of 120 | 9 / 120 |
| biomesoplenty:spider_nest | 2 | 0/47/1 of 48 | 0/47/1 of 48 | 0 / 48 |
| biomesoplenty:wasteland | 7 | 138/142/0 of 280 | 141/139/0 of 280 | 3 / 280 |
| minecraft:desert | 5 | 46/73/1 of 120 | 52/67/1 of 120 | 6 / 120 |
| minecraft:dripstone_caves | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| minecraft:wooded_badlands | 1 | 5/14/21 of 40 | 6/12/22 of 40 | 1 / 40 |
| regions_unexplored:joshua_desert | 2 | 11/64/5 of 80 | 17/58/5 of 80 | 6 / 80 |
| regions_unexplored:outback | 1 | 20/15/5 of 40 | 23/12/5 of 40 | 3 / 40 |
| regions_unexplored:saguaro_desert | 4 | 74/86/0 of 160 | 77/83/0 of 160 | 3 / 160 |
| terralith:bryce_canyon | 3 | 6/52/30 of 88 | 20/38/30 of 88 | 14 / 88 |
| terralith:cave/deep_caves | 2 | 0/65/15 of 80 | 0/65/15 of 80 | 0 / 80 |
| terralith:cave/granite_caves | 4 | 0/128/0 of 128 | 0/128/0 of 128 | 0 / 128 |
| terralith:lush_desert | 4 | 79/81/0 of 160 | 90/70/0 of 160 | 11 / 160 |
| terralith:sandstone_valley | 1 | 7/18/15 of 40 | 8/17/15 of 40 | 1 / 40 |

## full-mountainous-r1-baseline

[Raw observations](results/full-mountainous-r1-baseline.json.gz), SHA-256 `0fd390e6695db98b86c70a9f278a167dc3c0b168377fc1c294e3f3f707eb9104`. Selected cases: 28.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| betterdungeons:small_dungeon<br>betterdungeons:small_dungeon@5,0 | 1 / 4096 | biomesoplenty:crag | 89.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| ctov:village<br>ctov:medium/village_mountain_alpine@-27,9 | 2 / 4096 | biomesoplenty:crag | 98.0 | 3/2/0 of 5; 3/2/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 21/19/0 of 40; 21/19/0 of 40 |
| dungeons_arise:abandoned_temple<br>dungeons_arise:abandoned_temple@7,5 | 1 / 4096 | biomesoplenty:crag | 89.0 | 3/2/0 of 5; 3/2/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 25/15/0 of 40; 26/14/0 of 40 |
| dungeons_arise:monastery<br>dungeons_arise:monastery@5,8 | 1 / 4096 | biomesoplenty:crag | 66.0 | 3/2/0 of 5; 3/2/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 19/21/0 of 40; 19/21/0 of 40 |
| explorations:forgotten_well<br>explorations:forgotten_well@20,-17 | 1 / 4096 | biomesoplenty:jacaranda_glade | 31.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 2/38/0 of 40 |
| explorations:large_oak_tree<br>explorations:large_oak_tree@23,-12 | 4 / 4096 | biomesoplenty:prairie | 32.0 | 2/3/0 of 5; 5/0/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 6/34/0 of 40; 21/19/0 of 40 |
| explorations:logs<br>explorations:logs@20,-12 | 2 / 4096 | biomesoplenty:jacaranda_glade | 32.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 4/36/0 of 40 |
| explorations:scarecrow<br>nonregistry:1 | 3 / 4096 | biomesoplenty:aspen_glade | 26.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| explorations:slime_cave<br>explorations:slime_cave@-27,-22 | 4 / 4096 | minecraft:deep_dark | 57.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@-19,0 | 3 / 4096 | biomesoplenty:crag | 80.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:ancient_portal<br>idas:ancient_portal/ancient_portal@12,23 | 1 / 4096 | minecraft:deep_dark | 51.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:bearclaw_inn<br>idas:bearclaw_inn@4,-25 | 1 / 4096 | biomesoplenty:redwood_forest | 42.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 1/4/0 of 5 | 0/40/0 of 40; 4/36/0 of 40 |
| idas:underground_camp<br>idas:underground_camp/underground_camp@-32,9 | 2 / 4096 | minecraft:deep_dark | None | UNKNOWN extremum | UNKNOWN extremum | 0/15/25 of 40; 0/15/25 of 40 |
| minecraft:ancient_city<br>minecraft:ancient_city@22,2 | 1 / 4096 | minecraft:deep_dark | 50.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_mountain@-31,29 | 2 / 4096 | biomesoplenty:crag | None | UNKNOWN extremum | UNKNOWN extremum | 5/15/20 of 40; 11/9/20 of 40 |
| mvs:cart<br>mvs:cart@14,13 | 1 / 4096 | biomesoplenty:crag | 53.0 | 5/0/0 of 5; 5/0/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 20/20/0 of 40; 20/20/0 of 40 |
| mvs:dead_tree<br>mvs:dead_tree_oak@9,8 | 1 / 4096 | biomesoplenty:crag | 59.0 | 0/5/0 of 5; 1/4/0 of 5 | 3/2/0 of 5; 3/2/0 of 5 | 6/34/0 of 40; 10/30/0 of 40 |
| mvs:harvest_heap<br>mvs:pile@19,14 | 6 / 4096 | biomesoplenty:crag | 83.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mvs:lantern<br>mvs:small_oak_lantern@7,6 | 1 / 4096 | biomesoplenty:crag | 91.0 | 0/3/0 of 3; 0/3/0 of 3 | 0/3/0 of 3; 0/3/0 of 3 | 0/24/0 of 24; 0/24/0 of 24 |
| mvs:well<br>mvs:small_tower_well@14,23 | 2 / 4096 | biomesoplenty:crag | 64.0 | 2/3/0 of 5; 2/3/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 11/29/0 of 40; 13/27/0 of 40 |
| mvs:wheat_grain_bin<br>mvs:wheat_grain_bin@16,3 | 1 / 4096 | biomesoplenty:crag | 53.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 14/26/0 of 40; 21/19/0 of 40 |
| mvs:windmill<br>mvs:windmill@22,3 | 1 / 4096 | biomesoplenty:crag | 48.0 | 0/5/0 of 5; 1/4/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 11/29/0 of 40; 13/27/0 of 40 |
| mvs:wooden_wheat_farm<br>mvs:wooden_wheat_farm@6,3 | 1 / 4096 | biomesoplenty:crag | 92.0 | 1/4/0 of 5; 1/4/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 10/30/0 of 40; 11/29/0 of 40 |
| quark:fairy_ring<br>nonregistry:3 | 1 / 4096 | biomesoplenty:jacaranda_glade | 60.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| quark:monster_box<br>nonregistry:3444 | 208 / 4096 | biomesoplenty:prairie | 39.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| repurposed_structures:igloo<br>repurposed_structures:igloo_stone@3,27 | 1 / 4096 | biomesoplenty:crag | 98.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 4/36/0 of 40; 4/36/0 of 40 |
| repurposed_structures:mineshaft<br>repurposed_structures:mineshaft_dark_forest@-16,-7 | 2 / 4096 | biomesoplenty:spider_nest | 45.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| supplementaries:cave_urn_cache<br>nonregistry:17637 | 3784 / 4096 | minecraft:deep_dark | 58.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| biomesoplenty:aspen_glade | 1 | 0/8/0 of 8 | 0/8/0 of 8 | 0 / 8 |
| biomesoplenty:crag | 15 | 146/418/20 of 584 | 169/395/20 of 584 | 23 / 584 |
| biomesoplenty:jacaranda_glade | 3 | 0/88/0 of 88 | 6/82/0 of 88 | 6 / 88 |
| biomesoplenty:prairie | 2 | 6/42/0 of 48 | 21/27/0 of 48 | 15 / 48 |
| biomesoplenty:redwood_forest | 1 | 0/40/0 of 40 | 4/36/0 of 40 | 4 / 40 |
| biomesoplenty:spider_nest | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| minecraft:deep_dark | 5 | 0/143/25 of 168 | 0/143/25 of 168 | 0 / 168 |

## full-mountainous-r1-without-sparse

[Raw observations](results/full-mountainous-r1-without-sparse.json.gz), SHA-256 `03e846af311d2dfde3ccf7a7bf784a7cd5468fd30d7967c20240df0e67e069a4`. Selected cases: 42.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| betterdungeons:skeleton_dungeon<br>betterdungeons:skeleton_dungeon@0,-32 | 1 / 4096 | biomesoplenty:overgrown_greens | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| betterdungeons:small_dungeon<br>betterdungeons:small_dungeon@-28,31 | 10 / 4096 | biomesoplenty:crag | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| betterdungeons:spider_dungeon<br>betterdungeons:spider_dungeon@10,15 | 2 / 4096 | biomesoplenty:crag | 40.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| betterdungeons:zombie_dungeon<br>betterdungeons:zombie_dungeon@4,15 | 1 / 4096 | biomesoplenty:crag | 36.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| ctov:village<br>ctov:medium/village_mountain_alpine@-27,9 | 2 / 4096 | biomesoplenty:crag | 98.0 | 3/2/0 of 5; 3/2/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 21/19/0 of 40; 21/19/0 of 40 |
| dungeons_arise:abandoned_temple<br>dungeons_arise:abandoned_temple@1,4 | 1 / 4096 | biomesoplenty:crag | 111.0 | 4/1/0 of 5; 4/1/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 17/23/0 of 40; 17/23/0 of 40 |
| dungeons_arise:monastery<br>dungeons_arise:monastery@2,3 | 1 / 4096 | biomesoplenty:crag | 99.0 | 1/4/0 of 5; 1/4/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 14/26/0 of 40; 14/26/0 of 40 |
| explorations:campsite<br>explorations:campsite@4,-26 | 1 / 4096 | biomesoplenty:redwood_forest | 33.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 2/3/0 of 5 | 0/40/0 of 40; 2/38/0 of 40 |
| explorations:forgotten_well<br>explorations:forgotten_well@-9,-16 | 7 / 4096 | biomesoplenty:redwood_forest | 52.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 10/30/0 of 40 |
| explorations:large_oak_tree<br>explorations:large_oak_tree@13,-9 | 9 / 4096 | biomesoplenty:aspen_glade | 44.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 2/3/0 of 5 | 4/36/0 of 40; 19/21/0 of 40 |
| explorations:logs<br>explorations:logs@13,-29 | 6 / 4096 | biomesoplenty:redwood_forest | None | UNKNOWN extremum | UNKNOWN extremum | 0/35/5 of 40; 1/34/5 of 40 |
| explorations:scarecrow<br>nonregistry:1 | 3 / 4096 | biomesoplenty:redwood_forest | 42.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| explorations:slime_cave<br>explorations:slime_cave@-15,0 | 16 / 4096 | biomesoplenty:crag | 79.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@6,9 | 12 / 4096 | biomesoplenty:crag | 53.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:animal_den<br>idas:animal_den/forest_den@4,-26 | 1 / 4096 | biomesoplenty:redwood_forest | 35.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 1/4/0 of 5 | 0/40/0 of 40; 3/37/0 of 40 |
| idas:nexus<br>idas:nexus@12,12 | 1 / 4096 | minecraft:deep_dark | 35.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:underground_camp<br>idas:underground_camp/underground_camp_deep@5,2 | 6 / 4096 | minecraft:deep_dark | 109.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ancient_city<br>minecraft:ancient_city@-11,27 | 5 / 4096 | minecraft:deep_dark | 52.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_mountain@6,5 | 2 / 4096 | biomesoplenty:crag | 96.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:trial_chambers<br>minecraft:trial_chambers@12,-27 | 1 / 4096 | biomesoplenty:spider_nest | 30.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mss:tree<br>mss:tree_1@28,12 | 1 / 4096 | biomesoplenty:crag | None | UNKNOWN extremum | UNKNOWN extremum | 25/10/5 of 40; 29/6/5 of 40 |
| mvs:cart<br>mvs:cart@0,4 | 1 / 4096 | biomesoplenty:crag | 86.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mvs:dead_tree<br>mvs:dead_tree_oak@5,2 | 1 / 4096 | biomesoplenty:crag | 110.0 | 0/5/0 of 5; 0/5/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 4/36/0 of 40; 4/36/0 of 40 |
| mvs:harvest_heap<br>mvs:haystack@2,8 | 14 / 4096 | biomesoplenty:crag | 96.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 8/32/0 of 40; 10/30/0 of 40 |
| mvs:lantern<br>mvs:small_campfire_lantern@19,-28 | 4 / 4096 | biomesoplenty:prairie | 36.0 | 0/5/0 of 5; 2/3/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 16/24/0 of 40; 27/13/0 of 40 |
| mvs:large_warped_tower<br>mvs:large_warped_tower@13,16 | 1 / 4096 | biomesoplenty:crag | 53.0 | 5/0/0 of 5; 5/0/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 38/2/0 of 40; 38/2/0 of 40 |
| mvs:living_tree<br>mvs:oak_tree@2,-28 | 1 / 4096 | biomesoplenty:overgrown_greens | None | UNKNOWN extremum | UNKNOWN extremum | 19/16/5 of 40; 20/15/5 of 40 |
| mvs:paths<br>mvs:paths@-32,29 | 1 / 4096 | biomesoplenty:crag | None | UNKNOWN extremum | UNKNOWN extremum | 0/20/20 of 40; 1/17/22 of 40 |
| mvs:snowy_fossil<br>mvs:snowy_fossil@-24,-27 | 1 / 4096 | terralith:rocky_mountains | 78.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 9/31/0 of 40; 9/31/0 of 40 |
| mvs:villager_statue<br>mvs:villager_statue@4,12 | 1 / 4096 | biomesoplenty:crag | 69.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 4/36/0 of 40; 4/36/0 of 40 |
| mvs:well<br>mvs:small_tower_well@9,3 | 4 / 4096 | biomesoplenty:crag | 67.0 | 0/5/0 of 5; 3/2/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 6/34/0 of 40; 10/30/0 of 40 |
| mvs:wheat_grain_bin<br>mvs:wheat_grain_bin@1,-25 | 2 / 4096 | biomesoplenty:redwood_forest | 44.0 | 0/5/0 of 5; 2/3/0 of 5 | 0/5/0 of 5; 3/2/0 of 5 | 0/40/0 of 40; 10/30/0 of 40 |
| mvs:windmill<br>mvs:windmill@17,9 | 2 / 4096 | biomesoplenty:crag | 48.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 13/27/0 of 40; 13/27/0 of 40 |
| mvs:wooden_wheat_farm<br>mvs:wooden_wheat_farm@19,7 | 1 / 4096 | biomesoplenty:crag | 72.0 | 1/4/0 of 5; 2/3/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 3/37/0 of 40; 5/35/0 of 40 |
| quark:fairy_ring<br>nonregistry:3 | 1 / 4096 | biomesoplenty:jacaranda_glade | 60.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| quark:monster_box<br>nonregistry:3444 | 192 / 4096 | biomesoplenty:prairie | 39.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| repurposed_structures:igloo<br>repurposed_structures:igloo_stone@16,-29 | 1 / 4096 | biomesoplenty:prairie | None | UNKNOWN extremum | UNKNOWN extremum | 0/35/5 of 40; 3/32/5 of 40 |
| repurposed_structures:mineshaft<br>repurposed_structures:mineshaft_dark_forest@22,-5 | 5 / 4096 | biomesoplenty:spider_nest | 39.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| repurposed_structures:pyramid<br>repurposed_structures:pyramid_giant_tree_taiga@9,-30 | 1 / 4096 | biomesoplenty:redwood_forest | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 2/23/15 of 40 |
| supplementaries:cave_urn_cache<br>nonregistry:18136 | 3757 / 4096 | minecraft:deep_dark | 58.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| terralith:rubble<br>terralith:rubble_mountain@-26,1 | 2 / 4096 | terralith:rocky_mountains | 99.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| terralith:underground/old_refinery<br>terralith:underground/old_refinery@-26,-9 | 1 / 4096 | terralith:cave/deep_caves | 18.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| biomesoplenty:aspen_glade | 1 | 4/36/0 of 40 | 19/21/0 of 40 | 15 / 40 |
| biomesoplenty:crag | 19 | 153/567/40 of 760 | 166/552/42 of 760 | 13 / 760 |
| biomesoplenty:jacaranda_glade | 1 | 0/8/0 of 8 | 0/8/0 of 8 | 0 / 8 |
| biomesoplenty:overgrown_greens | 2 | 19/41/20 of 80 | 20/40/20 of 80 | 1 / 80 |
| biomesoplenty:prairie | 3 | 16/67/5 of 88 | 30/53/5 of 88 | 14 / 88 |
| biomesoplenty:redwood_forest | 7 | 0/228/20 of 248 | 28/200/20 of 248 | 28 / 248 |
| biomesoplenty:spider_nest | 2 | 0/80/0 of 80 | 0/80/0 of 80 | 0 / 80 |
| minecraft:deep_dark | 4 | 0/128/0 of 128 | 0/128/0 of 128 | 0 / 128 |
| terralith:cave/deep_caves | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| terralith:rocky_mountains | 2 | 9/71/0 of 80 | 9/71/0 of 80 | 0 / 80 |

## full-mountainous-r2-baseline

[Raw observations](results/full-mountainous-r2-baseline.json.gz), SHA-256 `55dc76b48ee7177fd1dfbb8310b31e077b7d038c8a80872a5cabafed5197e495`. Selected cases: 28.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| betterdungeons:small_dungeon<br>betterdungeons:small_dungeon@5,0 | 1 / 4096 | biomesoplenty:crag | 89.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| ctov:village<br>ctov:medium/village_mountain_alpine@-27,9 | 2 / 4096 | biomesoplenty:crag | 98.0 | 3/2/0 of 5; 3/2/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 21/19/0 of 40; 21/19/0 of 40 |
| dungeons_arise:abandoned_temple<br>dungeons_arise:abandoned_temple@7,5 | 1 / 4096 | biomesoplenty:crag | 89.0 | 3/2/0 of 5; 3/2/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 25/15/0 of 40; 26/14/0 of 40 |
| dungeons_arise:monastery<br>dungeons_arise:monastery@5,8 | 1 / 4096 | biomesoplenty:crag | 66.0 | 3/2/0 of 5; 3/2/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 19/21/0 of 40; 19/21/0 of 40 |
| explorations:forgotten_well<br>explorations:forgotten_well@20,-17 | 1 / 4096 | biomesoplenty:jacaranda_glade | 31.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:large_oak_tree<br>explorations:large_oak_tree@23,-12 | 4 / 4096 | biomesoplenty:prairie | 39.0 | 1/4/0 of 5; 5/0/0 of 5 | 0/5/0 of 5; 5/0/0 of 5 | 5/35/0 of 40; 26/14/0 of 40 |
| explorations:logs<br>explorations:logs@20,-12 | 2 / 4096 | biomesoplenty:jacaranda_glade | 32.0 | 0/5/0 of 5; 2/3/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 9/31/0 of 40 |
| explorations:scarecrow<br>nonregistry:1 | 2 / 4096 | biomesoplenty:jacaranda_glade | None | UNKNOWN extremum | UNKNOWN extremum | 0/5/3 of 8; 0/5/3 of 8 |
| explorations:slime_cave<br>explorations:slime_cave@-27,-22 | 4 / 4096 | minecraft:deep_dark | 57.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@-19,0 | 3 / 4096 | biomesoplenty:crag | 80.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:ancient_portal<br>idas:ancient_portal/ancient_portal@12,23 | 1 / 4096 | minecraft:deep_dark | 51.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:bearclaw_inn<br>idas:bearclaw_inn@4,-25 | 1 / 4096 | biomesoplenty:redwood_forest | 16.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:underground_camp<br>idas:underground_camp/underground_camp@-32,9 | 2 / 4096 | minecraft:deep_dark | None | UNKNOWN extremum | UNKNOWN extremum | 0/15/25 of 40; 0/15/25 of 40 |
| minecraft:ancient_city<br>minecraft:ancient_city@22,2 | 1 / 4096 | minecraft:deep_dark | 50.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_mountain@-31,29 | 2 / 4096 | biomesoplenty:crag | None | UNKNOWN extremum | UNKNOWN extremum | 5/15/20 of 40; 7/13/20 of 40 |
| mvs:cart<br>mvs:cart@14,13 | 1 / 4096 | biomesoplenty:crag | 53.0 | 5/0/0 of 5; 5/0/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 20/20/0 of 40; 20/20/0 of 40 |
| mvs:dead_tree<br>mvs:dead_tree_oak@9,8 | 1 / 4096 | biomesoplenty:crag | 59.0 | 0/5/0 of 5; 1/4/0 of 5 | 3/2/0 of 5; 3/2/0 of 5 | 6/34/0 of 40; 10/30/0 of 40 |
| mvs:harvest_heap<br>mvs:pile@19,14 | 6 / 4096 | biomesoplenty:crag | 83.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mvs:lantern<br>mvs:small_oak_lantern@7,6 | 1 / 4096 | biomesoplenty:crag | 91.0 | 0/3/0 of 3; 0/3/0 of 3 | 0/3/0 of 3; 0/3/0 of 3 | 0/24/0 of 24; 0/24/0 of 24 |
| mvs:well<br>mvs:small_tower_well@14,23 | 2 / 4096 | biomesoplenty:crag | 64.0 | 2/3/0 of 5; 2/3/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 12/28/0 of 40; 13/27/0 of 40 |
| mvs:wheat_grain_bin<br>mvs:wheat_grain_bin@16,3 | 1 / 4096 | biomesoplenty:crag | 53.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 18/22/0 of 40; 21/19/0 of 40 |
| mvs:windmill<br>mvs:windmill@22,3 | 1 / 4096 | biomesoplenty:crag | 48.0 | 0/5/0 of 5; 1/4/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 12/28/0 of 40; 13/27/0 of 40 |
| mvs:wooden_wheat_farm<br>mvs:wooden_wheat_farm@6,3 | 1 / 4096 | biomesoplenty:crag | 92.0 | 1/4/0 of 5; 1/4/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 10/30/0 of 40; 11/29/0 of 40 |
| quark:fairy_ring<br>nonregistry:2 | 2 / 4096 | biomesoplenty:jacaranda_glade | 60.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| quark:monster_box<br>nonregistry:3444 | 215 / 4096 | biomesoplenty:prairie | 39.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| repurposed_structures:igloo<br>repurposed_structures:igloo_stone@3,27 | 1 / 4096 | biomesoplenty:crag | 98.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 4/36/0 of 40; 4/36/0 of 40 |
| repurposed_structures:mineshaft<br>repurposed_structures:mineshaft_dark_forest@-16,-7 | 2 / 4096 | biomesoplenty:spider_nest | 45.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| supplementaries:cave_urn_cache<br>nonregistry:7114 | 3755 / 4096 | minecraft:deep_dark | 47.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| biomesoplenty:crag | 15 | 152/412/20 of 584 | 165/399/20 of 584 | 13 / 584 |
| biomesoplenty:jacaranda_glade | 4 | 0/93/3 of 96 | 9/84/3 of 96 | 9 / 96 |
| biomesoplenty:prairie | 2 | 5/43/0 of 48 | 26/22/0 of 48 | 21 / 48 |
| biomesoplenty:redwood_forest | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| biomesoplenty:spider_nest | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| minecraft:deep_dark | 5 | 0/143/25 of 168 | 0/143/25 of 168 | 0 / 168 |

## full-mountainous-r2-without-sparse

[Raw observations](results/full-mountainous-r2-without-sparse.json.gz), SHA-256 `44bc651c4b8ef519f854fdcf67a5a7dd35fa386dc22e122b837fb3f5142d2cf3`. Selected cases: 42.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| betterdungeons:skeleton_dungeon<br>betterdungeons:skeleton_dungeon@0,-32 | 1 / 4096 | biomesoplenty:overgrown_greens | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| betterdungeons:small_dungeon<br>betterdungeons:small_dungeon@-28,31 | 10 / 4096 | biomesoplenty:crag | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| betterdungeons:spider_dungeon<br>betterdungeons:spider_dungeon@10,15 | 2 / 4096 | biomesoplenty:crag | 40.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| betterdungeons:zombie_dungeon<br>betterdungeons:zombie_dungeon@4,15 | 1 / 4096 | biomesoplenty:crag | 36.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| ctov:village<br>ctov:medium/village_mountain_alpine@-27,9 | 2 / 4096 | biomesoplenty:crag | 98.0 | 3/2/0 of 5; 3/2/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 21/19/0 of 40; 21/19/0 of 40 |
| dungeons_arise:abandoned_temple<br>dungeons_arise:abandoned_temple@1,4 | 1 / 4096 | biomesoplenty:crag | 111.0 | 4/1/0 of 5; 4/1/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 17/23/0 of 40; 17/23/0 of 40 |
| dungeons_arise:monastery<br>dungeons_arise:monastery@2,3 | 1 / 4096 | biomesoplenty:crag | 99.0 | 1/4/0 of 5; 1/4/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 14/26/0 of 40; 14/26/0 of 40 |
| explorations:campsite<br>explorations:campsite@4,-26 | 1 / 4096 | biomesoplenty:redwood_forest | 33.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:forgotten_well<br>explorations:forgotten_well@-9,-16 | 7 / 4096 | biomesoplenty:redwood_forest | 60.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 6/34/0 of 40; 9/31/0 of 40 |
| explorations:large_oak_tree<br>explorations:large_oak_tree@13,-9 | 9 / 4096 | biomesoplenty:aspen_glade | 44.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 4/1/0 of 5 | 0/40/0 of 40; 18/22/0 of 40 |
| explorations:logs<br>explorations:logs@13,-29 | 6 / 4096 | biomesoplenty:redwood_forest | None | UNKNOWN extremum | UNKNOWN extremum | 0/35/5 of 40; 0/35/5 of 40 |
| explorations:scarecrow<br>nonregistry:1 | 4 / 4096 | biomesoplenty:aspen_glade | 26.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| explorations:slime_cave<br>explorations:slime_cave@-15,0 | 16 / 4096 | biomesoplenty:crag | 79.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@6,9 | 12 / 4096 | biomesoplenty:crag | 53.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:animal_den<br>idas:animal_den/forest_den@4,-26 | 1 / 4096 | biomesoplenty:redwood_forest | 35.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:nexus<br>idas:nexus@12,12 | 1 / 4096 | minecraft:deep_dark | 35.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:underground_camp<br>idas:underground_camp/underground_camp_deep@5,2 | 6 / 4096 | minecraft:deep_dark | 109.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ancient_city<br>minecraft:ancient_city@-11,27 | 5 / 4096 | minecraft:deep_dark | 52.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_mountain@6,5 | 2 / 4096 | biomesoplenty:crag | 96.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:trial_chambers<br>minecraft:trial_chambers@12,-27 | 1 / 4096 | biomesoplenty:spider_nest | 14.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mss:tree<br>mss:tree_1@28,12 | 1 / 4096 | biomesoplenty:crag | None | UNKNOWN extremum | UNKNOWN extremum | 25/10/5 of 40; 29/6/5 of 40 |
| mvs:cart<br>mvs:cart@0,4 | 1 / 4096 | biomesoplenty:crag | 86.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mvs:dead_tree<br>mvs:dead_tree_oak@5,2 | 1 / 4096 | biomesoplenty:crag | 110.0 | 0/5/0 of 5; 0/5/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 4/36/0 of 40; 4/36/0 of 40 |
| mvs:harvest_heap<br>mvs:haystack@2,8 | 14 / 4096 | biomesoplenty:crag | 96.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 8/32/0 of 40; 10/30/0 of 40 |
| mvs:lantern<br>mvs:small_campfire_lantern@19,-28 | 4 / 4096 | biomesoplenty:prairie | 36.0 | 0/5/0 of 5; 2/3/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 11/29/0 of 40; 22/18/0 of 40 |
| mvs:large_warped_tower<br>mvs:large_warped_tower@13,16 | 1 / 4096 | biomesoplenty:crag | 53.0 | 5/0/0 of 5; 5/0/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 38/2/0 of 40; 38/2/0 of 40 |
| mvs:living_tree<br>mvs:oak_tree@2,-28 | 1 / 4096 | biomesoplenty:overgrown_greens | None | UNKNOWN extremum | UNKNOWN extremum | 14/21/5 of 40; 22/13/5 of 40 |
| mvs:paths<br>mvs:paths@-32,29 | 1 / 4096 | biomesoplenty:crag | None | UNKNOWN extremum | UNKNOWN extremum | 0/20/20 of 40; 0/18/22 of 40 |
| mvs:snowy_fossil<br>mvs:snowy_fossil@-24,-27 | 1 / 4096 | terralith:rocky_mountains | 78.0 | 0/5/0 of 5; 3/2/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 9/31/0 of 40; 12/28/0 of 40 |
| mvs:villager_statue<br>mvs:villager_statue@4,12 | 1 / 4096 | biomesoplenty:crag | 69.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 4/36/0 of 40; 4/36/0 of 40 |
| mvs:well<br>mvs:small_tower_well@9,3 | 4 / 4096 | biomesoplenty:crag | 67.0 | 0/5/0 of 5; 3/2/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 6/34/0 of 40; 10/30/0 of 40 |
| mvs:wheat_grain_bin<br>mvs:wheat_grain_bin@1,-25 | 2 / 4096 | biomesoplenty:redwood_forest | 44.0 | 0/5/0 of 5; 2/3/0 of 5 | 0/5/0 of 5; 4/1/0 of 5 | 0/40/0 of 40; 12/28/0 of 40 |
| mvs:windmill<br>mvs:windmill@17,9 | 2 / 4096 | biomesoplenty:crag | 48.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 13/27/0 of 40; 13/27/0 of 40 |
| mvs:wooden_wheat_farm<br>mvs:wooden_wheat_farm@19,7 | 1 / 4096 | biomesoplenty:crag | 72.0 | 1/4/0 of 5; 2/3/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 3/37/0 of 40; 5/35/0 of 40 |
| quark:fairy_ring<br>nonregistry:4 | 1 / 4096 | biomesoplenty:jacaranda_glade | 60.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| quark:monster_box<br>nonregistry:3201 | 191 / 4096 | minecraft:deep_dark | 29.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| repurposed_structures:igloo<br>repurposed_structures:igloo_stone@16,-29 | 1 / 4096 | biomesoplenty:prairie | None | UNKNOWN extremum | UNKNOWN extremum | 0/35/5 of 40; 2/33/5 of 40 |
| repurposed_structures:mineshaft<br>repurposed_structures:mineshaft_dark_forest@22,-5 | 5 / 4096 | biomesoplenty:spider_nest | 40.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| repurposed_structures:pyramid<br>repurposed_structures:pyramid_giant_tree_taiga@9,-30 | 1 / 4096 | biomesoplenty:redwood_forest | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 3/22/15 of 40 |
| supplementaries:cave_urn_cache<br>nonregistry:20810 | 3856 / 4096 | minecraft:deep_dark | 58.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| terralith:rubble<br>terralith:rubble_mountain@-26,1 | 2 / 4096 | terralith:rocky_mountains | 99.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| terralith:underground/old_refinery<br>terralith:underground/old_refinery@-26,-9 | 1 / 4096 | terralith:cave/deep_caves | 18.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| biomesoplenty:aspen_glade | 2 | 0/48/0 of 48 | 18/30/0 of 48 | 18 / 48 |
| biomesoplenty:crag | 19 | 153/567/40 of 760 | 165/553/42 of 760 | 12 / 760 |
| biomesoplenty:jacaranda_glade | 1 | 0/8/0 of 8 | 0/8/0 of 8 | 0 / 8 |
| biomesoplenty:overgrown_greens | 2 | 14/46/20 of 80 | 22/38/20 of 80 | 8 / 80 |
| biomesoplenty:prairie | 2 | 11/64/5 of 80 | 24/51/5 of 80 | 13 / 80 |
| biomesoplenty:redwood_forest | 6 | 6/214/20 of 240 | 24/196/20 of 240 | 18 / 240 |
| biomesoplenty:spider_nest | 2 | 0/80/0 of 80 | 0/80/0 of 80 | 0 / 80 |
| minecraft:deep_dark | 5 | 0/136/0 of 136 | 0/136/0 of 136 | 0 / 136 |
| terralith:cave/deep_caves | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| terralith:rocky_mountains | 2 | 9/71/0 of 80 | 12/68/0 of 80 | 3 / 80 |

## full-ocean-heavy-r1-baseline

[Raw observations](results/full-ocean-heavy-r1-baseline.json.gz), SHA-256 `d0a600160a6acf9028aab1a97719fb725468da1896c1d36d1336db39123149c2`. Selected cases: 20.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| betterdungeons:skeleton_dungeon<br>betterdungeons:skeleton_dungeon@27,5 | 1 / 4096 | minecraft:lush_caves | 29.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| betterdungeons:small_dungeon<br>betterdungeons:small_dungeon@27,0 | 2 / 4096 | minecraft:stony_shore | 41.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| betteroceanmonuments:ocean_monument<br>betteroceanmonuments:ocean_monument@2,9 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 4/1/0 of 5; 4/1/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 37/3/0 of 40; 37/3/0 of 40 |
| dungeons_arise:illager_galley<br>dungeons_arise:illager_galley@5,0 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 40/0/0 of 40; 40/0/0 of 40 |
| dungeons_arise_seven_seas:unicorn_galleon<br>dungeons_arise_seven_seas:unicorn_galleon@14,4 | 1 / 4096 | minecraft:cold_ocean | 0.0 | 2/3/0 of 5; 2/3/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 30/10/0 of 40; 30/10/0 of 40 |
| explorations:floating_island<br>explorations:floating_island@4,-29 | 3 / 4096 | minecraft:cold_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 15/10/15 of 40; 19/6/15 of 40 |
| explorations:scarecrow<br>nonregistry:1 | 3 / 4096 | minecraft:taiga | None | UNKNOWN extremum | UNKNOWN extremum | 0/5/3 of 8; 0/5/3 of 8 |
| explorations:slime_cave<br>explorations:slime_cave@-25,0 | 4 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@17,23 | 3 / 4096 | minecraft:cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship<br>idas:sunken_ship/sunken_ship@4,0 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship/sunken_ship_ruins<br>idas:sunken_ship/sunken_ship_ruins@6,6 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ancient_city<br>minecraft:ancient_city@25,-26 | 1 / 4096 | minecraft:deep_dark | 20.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ocean_ruin<br>minecraft:ocean_ruin_cold@0,-25 | 3 / 4096 | minecraft:cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_mountain@24,-32 | 2 / 4096 | minecraft:stony_shore | None | UNKNOWN extremum | UNKNOWN extremum | 0/15/25 of 40; 0/15/25 of 40 |
| minecraft:shipwreck<br>minecraft:shipwreck@-13,13 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mss:small_tower<br>mss:small_tower@26,20 | 1 / 4096 | minecraft:cold_ocean | 0.0 | 4/1/0 of 5; 4/1/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 24/16/0 of 40; 26/14/0 of 40 |
| mss:tree<br>mss:tree_3@25,20 | 1 / 4096 | minecraft:cold_ocean | 0.0 | 1/4/0 of 5; 3/2/0 of 5 | 1/4/0 of 5; 3/2/0 of 5 | 19/21/0 of 40; 30/10/0 of 40 |
| quark:monster_box<br>nonregistry:4067 | 114 / 4096 | minecraft:cold_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/5/3 of 8; 0/5/3 of 8 |
| supplementaries:cave_urn_cache<br>nonregistry:23202 | 1149 / 4096 | minecraft:cold_ocean | 24.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| towns_and_towers:ocean_village<br>towns_and_towers:village_ocean@2,30 | 1 / 4096 | minecraft:cold_ocean | 0.0 | 4/1/0 of 5; 4/1/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 29/11/0 of 40; 30/10/0 of 40 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| minecraft:cold_ocean | 9 | 117/161/18 of 296 | 135/143/18 of 296 | 18 / 296 |
| minecraft:deep_cold_ocean | 6 | 77/163/0 of 240 | 77/163/0 of 240 | 0 / 240 |
| minecraft:deep_dark | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| minecraft:lush_caves | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| minecraft:stony_shore | 2 | 0/55/25 of 80 | 0/55/25 of 80 | 0 / 80 |
| minecraft:taiga | 1 | 0/5/3 of 8 | 0/5/3 of 8 | 0 / 8 |

## full-ocean-heavy-r1-without-sparse

[Raw observations](results/full-ocean-heavy-r1-without-sparse.json.gz), SHA-256 `73c59dbd185c237de5adcfc3170e446d1e9f17cf40852effa953ea887bc3af6c`. Selected cases: 31.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| adorabuild_structures:ocean_shrine<br>adorabuild_structures:ocean_temple_small_2@-17,31 | 1 / 4096 | minecraft:deep_cold_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| betterdungeons:small_dungeon<br>betterdungeons:small_dungeon@31,-19 | 6 / 4096 | minecraft:lush_caves | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| bettermineshafts:mineshaft<br>bettermineshafts:mineshaft_lush@-11,21 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 40/0/0 of 40; 40/0/0 of 40 |
| dungeons_arise:illager_galley<br>dungeons_arise:illager_galley@4,1 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 35/5/0 of 40; 36/4/0 of 40 |
| dungeons_arise_seven_seas:victory_frigate<br>dungeons_arise_seven_seas:victory_frigate@3,4 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 28/12/0 of 40; 28/12/0 of 40 |
| explorations:floating_island<br>explorations:floating_island@-11,-31 | 7 / 4096 | minecraft:cold_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 15/10/15 of 40; 19/6/15 of 40 |
| explorations:scarecrow<br>nonregistry:1 | 3 / 4096 | biomesoplenty:field | 25.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| explorations:slime_cave<br>explorations:slime_cave@18,0 | 16 / 4096 | minecraft:cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@-18,-13 | 10 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:nexus<br>idas:nexus@17,8 | 1 / 4096 | terralith:cave/deep_caves | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:pillager_camp<br>idas:pillager_camp@29,-26 | 1 / 4096 | biomesoplenty:field | None | UNKNOWN extremum | UNKNOWN extremum | 3/32/5 of 40; 12/23/5 of 40 |
| idas:sunken_ship<br>idas:sunken_ship/sunken_ship@5,0 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship/sunken_ship_ruins<br>idas:sunken_ship/sunken_ship_ruins@-26,3 | 5 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:underground_camp<br>idas:underground_camp/underground_camp@27,-21 | 2 / 4096 | minecraft:lush_caves | 52.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| integrated_villages:village<br>integrated_villages:airship_village@21,13 | 1 / 4096 | minecraft:cold_ocean | 222.0 | 1/4/0 of 5; 1/4/0 of 5 | 3/2/0 of 5; 3/2/0 of 5 | 14/26/0 of 40; 14/26/0 of 40 |
| minecraft:ancient_city<br>minecraft:ancient_city@27,-10 | 1 / 4096 | minecraft:deep_dark | 54.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ocean_ruin<br>minecraft:ocean_ruin_cold@27,20 | 11 / 4096 | minecraft:cold_ocean | 184.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_ocean@1,10 | 3 / 4096 | minecraft:deep_cold_ocean | 63.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:shipwreck<br>minecraft:shipwreck@9,2 | 6 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:trial_chambers<br>minecraft:trial_chambers@6,10 | 2 / 4096 | minecraft:deep_cold_ocean | 109.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mss:castle_ruin<br>mss:castle_ruin@21,25 | 1 / 4096 | minecraft:cold_ocean | 0.0 | 2/3/0 of 5; 2/3/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 20/20/0 of 40; 20/20/0 of 40 |
| mss:large_tower<br>mss:large_tower@23,17 | 1 / 4096 | minecraft:cold_ocean | 129.0 | 2/3/0 of 5; 2/3/0 of 5 | 3/2/0 of 5; 3/2/0 of 5 | 17/23/0 of 40; 17/23/0 of 40 |
| mvs:harvest_heap<br>mvs:pile@27,-19 | 2 / 4096 | minecraft:taiga | 48.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 3/37/0 of 40 |
| mvs:living_tree<br>mvs:spruce_tree@31,1 | 1 / 4096 | minecraft:taiga | None | UNKNOWN extremum | UNKNOWN extremum | 2/23/15 of 40; 15/10/15 of 40 |
| quark:monster_box<br>nonregistry:3903 | 126 / 4096 | minecraft:lush_caves | None | UNKNOWN extremum | UNKNOWN extremum | 0/7/1 of 8; 0/7/1 of 8 |
| repurposed_structures:mineshaft<br>repurposed_structures:mineshaft_ocean@5,21 | 3 / 4096 | minecraft:lush_caves | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| repurposed_structures:pyramid<br>repurposed_structures:pyramid_ocean@4,13 | 1 / 4096 | minecraft:deep_cold_ocean | 66.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| supplementaries:cave_urn_cache<br>nonregistry:17637 | 1182 / 4096 | minecraft:cold_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/7/1 of 8; 0/7/1 of 8 |
| supplementaries:galleon<br>supplementaries:galleon@-23,31 | 1 / 4096 | minecraft:deep_cold_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 6/0/34 of 40; 6/0/34 of 40 |
| terralith:underground/mining_outpost<br>terralith:underground/mining_outpost@24,-20 | 2 / 4096 | minecraft:lush_caves | 49.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| towns_and_towers:ocean_wreckage<br>towns_and_towers:wreckage_ocean@10,-25 | 1 / 4096 | minecraft:cold_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 40/0/0 of 40; 40/0/0 of 40 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| biomesoplenty:field | 2 | 3/40/5 of 48 | 12/31/5 of 48 | 9 / 48 |
| minecraft:cold_ocean | 8 | 106/166/16 of 288 | 110/162/16 of 288 | 4 / 288 |
| minecraft:deep_cold_ocean | 12 | 109/322/49 of 480 | 110/321/49 of 480 | 1 / 480 |
| minecraft:deep_dark | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| minecraft:lush_caves | 5 | 0/152/16 of 168 | 0/152/16 of 168 | 0 / 168 |
| minecraft:taiga | 2 | 2/63/15 of 80 | 18/47/15 of 80 | 16 / 80 |
| terralith:cave/deep_caves | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |

## full-ocean-heavy-r2-baseline

[Raw observations](results/full-ocean-heavy-r2-baseline.json.gz), SHA-256 `c904af7da4f24c69cd7daff5c3163dee748bde7268c7463a9bd4a05bc5951d7e`. Selected cases: 20.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| betterdungeons:skeleton_dungeon<br>betterdungeons:skeleton_dungeon@27,5 | 1 / 4096 | minecraft:lush_caves | 29.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| betterdungeons:small_dungeon<br>betterdungeons:small_dungeon@27,0 | 2 / 4096 | minecraft:stony_shore | 41.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| betteroceanmonuments:ocean_monument<br>betteroceanmonuments:ocean_monument@2,9 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 4/1/0 of 5; 4/1/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 37/3/0 of 40; 37/3/0 of 40 |
| dungeons_arise:illager_galley<br>dungeons_arise:illager_galley@5,0 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 40/0/0 of 40; 40/0/0 of 40 |
| dungeons_arise_seven_seas:unicorn_galleon<br>dungeons_arise_seven_seas:unicorn_galleon@14,4 | 1 / 4096 | minecraft:cold_ocean | 0.0 | 2/3/0 of 5; 2/3/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 30/10/0 of 40; 30/10/0 of 40 |
| explorations:floating_island<br>explorations:floating_island@4,-29 | 3 / 4096 | minecraft:cold_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 15/10/15 of 40; 19/6/15 of 40 |
| explorations:scarecrow<br>nonregistry:1 | 4 / 4096 | minecraft:taiga | None | UNKNOWN extremum | UNKNOWN extremum | 0/5/3 of 8; 0/5/3 of 8 |
| explorations:slime_cave<br>explorations:slime_cave@-25,0 | 4 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@17,23 | 3 / 4096 | minecraft:cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship<br>idas:sunken_ship/sunken_ship@4,0 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship/sunken_ship_ruins<br>idas:sunken_ship/sunken_ship_ruins@6,6 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ancient_city<br>minecraft:ancient_city@25,-26 | 1 / 4096 | minecraft:deep_dark | 20.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ocean_ruin<br>minecraft:ocean_ruin_cold@0,-25 | 3 / 4096 | minecraft:cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_mountain@24,-32 | 2 / 4096 | minecraft:stony_shore | None | UNKNOWN extremum | UNKNOWN extremum | 0/15/25 of 40; 0/15/25 of 40 |
| minecraft:shipwreck<br>minecraft:shipwreck@-13,13 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mss:small_tower<br>mss:small_tower@26,20 | 1 / 4096 | minecraft:cold_ocean | 0.0 | 4/1/0 of 5; 4/1/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 24/16/0 of 40; 26/14/0 of 40 |
| mss:tree<br>mss:tree_3@25,20 | 1 / 4096 | minecraft:cold_ocean | 0.0 | 1/4/0 of 5; 3/2/0 of 5 | 1/4/0 of 5; 3/2/0 of 5 | 19/21/0 of 40; 30/10/0 of 40 |
| quark:monster_box<br>nonregistry:4064 | 117 / 4096 | minecraft:cold_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/5/3 of 8; 0/5/3 of 8 |
| supplementaries:cave_urn_cache<br>nonregistry:18136 | 1192 / 4096 | minecraft:cold_ocean | 0.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| towns_and_towers:ocean_village<br>towns_and_towers:village_ocean@2,30 | 1 / 4096 | minecraft:cold_ocean | 0.0 | 4/1/0 of 5; 4/1/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 29/11/0 of 40; 30/10/0 of 40 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| minecraft:cold_ocean | 9 | 117/161/18 of 296 | 135/143/18 of 296 | 18 / 296 |
| minecraft:deep_cold_ocean | 6 | 77/163/0 of 240 | 77/163/0 of 240 | 0 / 240 |
| minecraft:deep_dark | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| minecraft:lush_caves | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| minecraft:stony_shore | 2 | 0/55/25 of 80 | 0/55/25 of 80 | 0 / 80 |
| minecraft:taiga | 1 | 0/5/3 of 8 | 0/5/3 of 8 | 0 / 8 |

## full-ocean-heavy-r2-without-sparse-attempt3

[Raw observations](results/full-ocean-heavy-r2-without-sparse-attempt3.json.gz), SHA-256 `cd51fa49be58acd3eb2afd726c73e894edc0e13d842d470791f0522847608598`. Selected cases: 31.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| adorabuild_structures:ocean_shrine<br>adorabuild_structures:ocean_temple_small_2@-17,31 | 1 / 4096 | minecraft:deep_cold_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| betterdungeons:small_dungeon<br>betterdungeons:small_dungeon@31,-19 | 6 / 4096 | minecraft:lush_caves | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| bettermineshafts:mineshaft<br>bettermineshafts:mineshaft_lush@-11,21 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 40/0/0 of 40; 40/0/0 of 40 |
| dungeons_arise:illager_galley<br>dungeons_arise:illager_galley@4,1 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 35/5/0 of 40; 36/4/0 of 40 |
| dungeons_arise_seven_seas:victory_frigate<br>dungeons_arise_seven_seas:victory_frigate@3,4 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 28/12/0 of 40; 28/12/0 of 40 |
| explorations:floating_island<br>explorations:floating_island@-11,-31 | 7 / 4096 | minecraft:cold_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 15/10/15 of 40; 19/6/15 of 40 |
| explorations:scarecrow<br>nonregistry:1 | 4 / 4096 | minecraft:taiga | None | UNKNOWN extremum | UNKNOWN extremum | 0/5/3 of 8; 0/5/3 of 8 |
| explorations:slime_cave<br>explorations:slime_cave@18,0 | 16 / 4096 | minecraft:cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@-18,-13 | 10 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:nexus<br>idas:nexus@17,8 | 1 / 4096 | terralith:cave/deep_caves | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:pillager_camp<br>idas:pillager_camp@29,-26 | 1 / 4096 | biomesoplenty:field | None | UNKNOWN extremum | UNKNOWN extremum | 3/32/5 of 40; 9/26/5 of 40 |
| idas:sunken_ship<br>idas:sunken_ship/sunken_ship@5,0 | 1 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship/sunken_ship_ruins<br>idas:sunken_ship/sunken_ship_ruins@-26,3 | 5 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:underground_camp<br>idas:underground_camp/underground_camp@27,-21 | 2 / 4096 | minecraft:lush_caves | 52.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| integrated_villages:village<br>integrated_villages:airship_village@21,13 | 1 / 4096 | minecraft:cold_ocean | 222.0 | 1/4/0 of 5; 1/4/0 of 5 | 3/2/0 of 5; 3/2/0 of 5 | 14/26/0 of 40; 14/26/0 of 40 |
| minecraft:ancient_city<br>minecraft:ancient_city@27,-10 | 1 / 4096 | minecraft:deep_dark | 54.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ocean_ruin<br>minecraft:ocean_ruin_cold@27,20 | 11 / 4096 | minecraft:cold_ocean | 184.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_ocean@1,10 | 3 / 4096 | minecraft:deep_cold_ocean | 63.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:shipwreck<br>minecraft:shipwreck@9,2 | 6 / 4096 | minecraft:deep_cold_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:trial_chambers<br>minecraft:trial_chambers@6,10 | 2 / 4096 | minecraft:deep_cold_ocean | 109.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mss:castle_ruin<br>mss:castle_ruin@21,25 | 1 / 4096 | minecraft:cold_ocean | 0.0 | 2/3/0 of 5; 2/3/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 20/20/0 of 40; 20/20/0 of 40 |
| mss:large_tower<br>mss:large_tower@23,17 | 1 / 4096 | minecraft:cold_ocean | 129.0 | 2/3/0 of 5; 2/3/0 of 5 | 3/2/0 of 5; 3/2/0 of 5 | 17/23/0 of 40; 17/23/0 of 40 |
| mvs:harvest_heap<br>mvs:pile@27,-19 | 2 / 4096 | minecraft:taiga | 48.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 3/37/0 of 40 |
| mvs:living_tree<br>mvs:spruce_tree@31,1 | 1 / 4096 | minecraft:taiga | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 16/9/15 of 40 |
| quark:monster_box<br>nonregistry:4064 | 120 / 4096 | minecraft:cold_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/5/3 of 8; 0/5/3 of 8 |
| repurposed_structures:mineshaft<br>repurposed_structures:mineshaft_ocean@5,21 | 3 / 4096 | minecraft:lush_caves | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| repurposed_structures:pyramid<br>repurposed_structures:pyramid_ocean@4,13 | 1 / 4096 | minecraft:deep_cold_ocean | 66.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| supplementaries:cave_urn_cache<br>nonregistry:20810 | 1144 / 4096 | minecraft:lush_caves | 0.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| supplementaries:galleon<br>supplementaries:galleon@-23,31 | 1 / 4096 | minecraft:deep_cold_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 6/0/34 of 40; 6/0/34 of 40 |
| terralith:underground/mining_outpost<br>terralith:underground/mining_outpost@24,-20 | 2 / 4096 | minecraft:lush_caves | 49.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| towns_and_towers:ocean_wreckage<br>towns_and_towers:wreckage_ocean@10,-25 | 1 / 4096 | minecraft:cold_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 40/0/0 of 40; 40/0/0 of 40 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| biomesoplenty:field | 1 | 3/32/5 of 40 | 9/26/5 of 40 | 6 / 40 |
| minecraft:cold_ocean | 8 | 106/164/18 of 288 | 110/160/18 of 288 | 4 / 288 |
| minecraft:deep_cold_ocean | 12 | 109/322/49 of 480 | 110/321/49 of 480 | 1 / 480 |
| minecraft:deep_dark | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| minecraft:lush_caves | 5 | 0/153/15 of 168 | 0/153/15 of 168 | 0 / 168 |
| minecraft:taiga | 3 | 0/70/18 of 88 | 19/51/18 of 88 | 19 / 88 |
| terralith:cave/deep_caves | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |

## full-ordinary-r1-baseline

[Raw observations](results/full-ordinary-r1-baseline.json.gz), SHA-256 `a9a8b433719fe6312c04a7ba8a2d601d2a50fde39f785a4f706aca7d405cfb91`. Selected cases: 14.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| dungeons_arise:illager_galley<br>dungeons_arise:illager_galley@7,5 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 40/0/0 of 40; 40/0/0 of 40 |
| dungeons_arise_seven_seas:corsair_corvette<br>dungeons_arise_seven_seas:corsair_corvette@0,9 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 2/3/0 of 5; 2/3/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 31/9/0 of 40; 31/9/0 of 40 |
| explorations:floating_island<br>explorations:floating_island@14,-29 | 4 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 23/12/5 of 40; 27/8/5 of 40 |
| explorations:slime_cave<br>explorations:slime_cave@-21,6 | 4 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@-24,-17 | 3 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship<br>idas:sunken_ship/sunken_ship@10,7 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship/sunken_ship_ruins<br>idas:sunken_ship/sunken_ship_ruins@10,1 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| integrated_villages:village<br>integrated_villages:airship_village@6,23 | 1 / 4096 | minecraft:ocean | 132.0 | 1/4/0 of 5; 1/4/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 10/30/0 of 40; 10/30/0 of 40 |
| minecraft:ocean_ruin<br>minecraft:ocean_ruin_cold@0,-28 | 4 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/35/5 of 40; 0/35/5 of 40 |
| minecraft:shipwreck<br>minecraft:shipwreck@-15,21 | 2 / 4096 | minecraft:ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:trial_chambers<br>minecraft:trial_chambers@29,30 | 1 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/20/20 of 40; 0/20/20 of 40 |
| quark:monster_box<br>nonregistry:2833 | 94 / 4096 | minecraft:ocean | 0.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| supplementaries:cave_urn_cache<br>nonregistry:22030 | 837 / 4096 | minecraft:ocean | 0.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| towns_and_towers:ocean_wreckage<br>towns_and_towers:wreckage_ocean@12,18 | 1 / 4096 | minecraft:ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 35/5/0 of 40; 35/5/0 of 40 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| minecraft:deep_ocean | 6 | 71/169/0 of 240 | 71/169/0 of 240 | 0 / 240 |
| minecraft:ocean | 8 | 68/158/30 of 256 | 72/154/30 of 256 | 4 / 256 |

## full-ordinary-r1-without-sparse

[Raw observations](results/full-ordinary-r1-without-sparse.json.gz), SHA-256 `9104f8e0ffbb17764c8a43dd0f85a61a7a79a70306fc29706de5fb9dcb1043ea`. Selected cases: 24.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| adorabuild_structures:ocean_shrine<br>adorabuild_structures:ocean_temple_small_2@-30,3 | 1 / 4096 | minecraft:deep_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| betteroceanmonuments:ocean_monument<br>betteroceanmonuments:ocean_monument@7,2 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 39/1/0 of 40; 39/1/0 of 40 |
| dungeons_arise:illager_galley<br>dungeons_arise:illager_galley@4,3 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 37/3/0 of 40; 37/3/0 of 40 |
| dungeons_arise_seven_seas:pirate_junk<br>dungeons_arise_seven_seas:pirate_junk@1,5 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 4/1/0 of 5; 4/1/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 34/6/0 of 40; 34/6/0 of 40 |
| explorations:floating_island<br>explorations:floating_island@-11,-28 | 9 / 4096 | minecraft:deep_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 21/14/5 of 40; 27/8/5 of 40 |
| explorations:slime_cave<br>explorations:slime_cave@22,1 | 16 / 4096 | regions_unexplored:bioshroom_caves | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@-12,9 | 12 / 4096 | minecraft:lukewarm_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship<br>idas:sunken_ship/sunken_ship@-31,-31 | 1 / 4096 | minecraft:deep_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/15/25 of 40; 0/15/25 of 40 |
| idas:sunken_ship/sunken_ship_ruins<br>idas:sunken_ship/sunken_ship_ruins@0,4 | 6 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| integrated_villages:village<br>integrated_villages:airship_village@15,19 | 1 / 4096 | minecraft:ocean | 133.0 | 1/4/0 of 5; 1/4/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 17/23/0 of 40; 17/23/0 of 40 |
| minecraft:ocean_ruin<br>minecraft:ocean_ruin_cold@24,28 | 13 / 4096 | minecraft:ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_ocean@16,22 | 3 / 4096 | minecraft:ocean | 128.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:shipwreck<br>minecraft:shipwreck@27,-14 | 7 / 4096 | minecraft:ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:trial_chambers<br>minecraft:trial_chambers@19,-15 | 4 / 4096 | minecraft:ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mss:tree<br>mss:tree_4@30,11 | 1 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 9/16/15 of 40; 9/16/15 of 40 |
| mss:volcano<br>mss:volcano@27,18 | 1 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 10/25/5 of 40; 10/25/5 of 40 |
| quark:monster_box<br>nonregistry:2833 | 94 / 4096 | minecraft:ocean | 0.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| repurposed_structures:mineshaft<br>repurposed_structures:mineshaft_ocean@-3,-17 | 2 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| repurposed_structures:pyramid<br>repurposed_structures:pyramid_ocean@2,3 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| repurposed_structures:temple<br>repurposed_structures:temple_ocean@3,8 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| supplementaries:cave_urn_cache<br>nonregistry:9288 | 847 / 4096 | minecraft:deep_ocean | 0.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| supplementaries:galleon<br>supplementaries:galleon@-21,-30 | 2 / 4096 | minecraft:deep_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 28/7/5 of 40; 28/7/5 of 40 |
| towns_and_towers:ocean_village<br>towns_and_towers:village_ocean@-20,-26 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 2/3/0 of 5; 3/2/0 of 5 | 2/3/0 of 5; 3/2/0 of 5 | 29/11/0 of 40; 30/10/0 of 40 |
| towns_and_towers:ocean_wreckage<br>towns_and_towers:wreckage_ocean@10,-18 | 1 / 4096 | minecraft:ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 40/0/0 of 40; 40/0/0 of 40 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| minecraft:deep_ocean | 13 | 188/250/50 of 488 | 195/243/50 of 488 | 7 / 488 |
| minecraft:lukewarm_ocean | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| minecraft:ocean | 9 | 76/232/20 of 328 | 76/232/20 of 328 | 0 / 328 |
| regions_unexplored:bioshroom_caves | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |

## full-ordinary-r2-baseline

[Raw observations](results/full-ordinary-r2-baseline.json.gz), SHA-256 `4f9dfcaf8e4e034ee876202ef91cc3a3a936ddbc784da97ad7f38de5423e7266`. Selected cases: 14.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| dungeons_arise:illager_galley<br>dungeons_arise:illager_galley@7,5 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 40/0/0 of 40; 40/0/0 of 40 |
| dungeons_arise_seven_seas:corsair_corvette<br>dungeons_arise_seven_seas:corsair_corvette@0,9 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 2/3/0 of 5; 2/3/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 31/9/0 of 40; 31/9/0 of 40 |
| explorations:floating_island<br>explorations:floating_island@14,-29 | 4 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 23/12/5 of 40; 27/8/5 of 40 |
| explorations:slime_cave<br>explorations:slime_cave@-21,6 | 4 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@-24,-17 | 3 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship<br>idas:sunken_ship/sunken_ship@10,7 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship/sunken_ship_ruins<br>idas:sunken_ship/sunken_ship_ruins@10,1 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| integrated_villages:village<br>integrated_villages:airship_village@6,23 | 1 / 4096 | minecraft:ocean | 132.0 | 1/4/0 of 5; 1/4/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 10/30/0 of 40; 10/30/0 of 40 |
| minecraft:ocean_ruin<br>minecraft:ocean_ruin_cold@0,-28 | 4 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/35/5 of 40; 0/35/5 of 40 |
| minecraft:shipwreck<br>minecraft:shipwreck@-15,21 | 2 / 4096 | minecraft:ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:trial_chambers<br>minecraft:trial_chambers@29,30 | 1 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/20/20 of 40; 0/20/20 of 40 |
| quark:monster_box<br>nonregistry:2833 | 93 / 4096 | minecraft:ocean | 0.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| supplementaries:cave_urn_cache<br>nonregistry:24974 | 818 / 4096 | regions_unexplored:bioshroom_caves | None | UNKNOWN extremum | UNKNOWN extremum | 0/5/3 of 8; 0/5/3 of 8 |
| towns_and_towers:ocean_wreckage<br>towns_and_towers:wreckage_ocean@12,18 | 1 / 4096 | minecraft:ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 35/5/0 of 40; 35/5/0 of 40 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| minecraft:deep_ocean | 6 | 71/169/0 of 240 | 71/169/0 of 240 | 0 / 240 |
| minecraft:ocean | 7 | 68/150/30 of 248 | 72/146/30 of 248 | 4 / 248 |
| regions_unexplored:bioshroom_caves | 1 | 0/5/3 of 8 | 0/5/3 of 8 | 0 / 8 |

## full-ordinary-r2-without-sparse

[Raw observations](results/full-ordinary-r2-without-sparse.json.gz), SHA-256 `d28e206ab6595d7aa95a1d3c8b98c5714d5a1618ca8b5d4738493b304b3f3a5b`. Selected cases: 24.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| adorabuild_structures:ocean_shrine<br>adorabuild_structures:ocean_temple_small_2@-30,3 | 1 / 4096 | minecraft:deep_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/25/15 of 40; 0/25/15 of 40 |
| betteroceanmonuments:ocean_monument<br>betteroceanmonuments:ocean_monument@7,2 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 39/1/0 of 40; 39/1/0 of 40 |
| dungeons_arise:illager_galley<br>dungeons_arise:illager_galley@4,3 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 37/3/0 of 40; 37/3/0 of 40 |
| dungeons_arise_seven_seas:pirate_junk<br>dungeons_arise_seven_seas:pirate_junk@1,5 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 4/1/0 of 5; 4/1/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 34/6/0 of 40; 34/6/0 of 40 |
| explorations:floating_island<br>explorations:floating_island@-11,-28 | 9 / 4096 | minecraft:deep_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 21/14/5 of 40; 27/8/5 of 40 |
| explorations:slime_cave<br>explorations:slime_cave@22,1 | 16 / 4096 | regions_unexplored:bioshroom_caves | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@-12,9 | 12 / 4096 | minecraft:lukewarm_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship<br>idas:sunken_ship/sunken_ship@-31,-31 | 1 / 4096 | minecraft:deep_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/15/25 of 40; 0/15/25 of 40 |
| idas:sunken_ship/sunken_ship_ruins<br>idas:sunken_ship/sunken_ship_ruins@0,4 | 6 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| integrated_villages:village<br>integrated_villages:airship_village@15,19 | 1 / 4096 | minecraft:ocean | 133.0 | 1/4/0 of 5; 1/4/0 of 5 | 4/1/0 of 5; 4/1/0 of 5 | 17/23/0 of 40; 17/23/0 of 40 |
| minecraft:ocean_ruin<br>minecraft:ocean_ruin_cold@24,28 | 13 / 4096 | minecraft:ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:ruined_portal<br>minecraft:ruined_portal_ocean@16,22 | 3 / 4096 | minecraft:ocean | 128.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:shipwreck<br>minecraft:shipwreck@27,-14 | 7 / 4096 | minecraft:ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:trial_chambers<br>minecraft:trial_chambers@19,-15 | 4 / 4096 | minecraft:ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| mss:tree<br>mss:tree_4@30,11 | 1 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 9/16/15 of 40; 9/16/15 of 40 |
| mss:volcano<br>mss:volcano@27,18 | 1 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 10/25/5 of 40; 10/25/5 of 40 |
| quark:monster_box<br>nonregistry:2833 | 94 / 4096 | minecraft:ocean | 0.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| repurposed_structures:mineshaft<br>repurposed_structures:mineshaft_ocean@-3,-17 | 2 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| repurposed_structures:pyramid<br>repurposed_structures:pyramid_ocean@2,3 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| repurposed_structures:temple<br>repurposed_structures:temple_ocean@3,8 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| supplementaries:cave_urn_cache<br>nonregistry:20646 | 842 / 4096 | minecraft:ocean | 0.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| supplementaries:galleon<br>supplementaries:galleon@-21,-30 | 2 / 4096 | minecraft:deep_ocean | None | UNKNOWN extremum | UNKNOWN extremum | 28/7/5 of 40; 28/7/5 of 40 |
| towns_and_towers:ocean_village<br>towns_and_towers:village_ocean@-20,-26 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 2/3/0 of 5; 3/2/0 of 5 | 2/3/0 of 5; 3/2/0 of 5 | 29/11/0 of 40; 30/10/0 of 40 |
| towns_and_towers:ocean_wreckage<br>towns_and_towers:wreckage_ocean@10,-18 | 1 / 4096 | minecraft:ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 40/0/0 of 40; 40/0/0 of 40 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| minecraft:deep_ocean | 12 | 188/242/50 of 480 | 195/235/50 of 480 | 7 / 480 |
| minecraft:lukewarm_ocean | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |
| minecraft:ocean | 10 | 76/240/20 of 336 | 76/240/20 of 336 | 0 / 336 |
| regions_unexplored:bioshroom_caves | 1 | 0/40/0 of 40 | 0/40/0 of 40 | 0 / 40 |

## Independent family abundance and discovery cues

94 observed canonical families out of the accepted 448 have sampled Overworld cases in this report. The other 354 have no case here, not proven absence from the pack. Their source assessments remain in the unchanged Item 8 inventory; Item 10 retains all-dimension density.

The count ranges below are existing full-frame placement counts, separately for baseline (B) and omit-Sparse control (C), among worlds in which the family occurs. Zero-occurrence worlds are shown separately. A case is WS-clear when any of its sampled rays clears; WS-occluded means every ray is occluded; the remaining cases are UNKNOWN/mixed without a clear ray. These are case counts, not all-placement discoverability rates. Source forms are reused artifact assessments, not new human recognition data.

| Family | B count range; absent worlds | C count range; absent worlds | WS clear / all-occluded / other cases | Reused architectural cue assessment |
| --- | --- | --- | --- | --- |
| adorabuild_structures:house | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Wood and sandstone cottages with gabled, flat, stepped and planted roofs, porches and multiple levels. Surface-projected variants have distinct envelopes and interiors; no single visibility distance describes them. |
| adorabuild_structures:ocean_shrine | no occurrences; 8/8 | 1..1; 4/8 | 0 / 0 / 4 of 4 | Open prismarine columned square shrines with gold and stacked tiers in the taller variant. |
| betterdungeons:skeleton_dungeon | 1..1; 6/8 | 1..1; 6/8 | 0 / 2 / 2 of 4 | Underground masonry stair/bridge complex; cave exposure or excavation can reveal it, but no surface entrance is established by the selected topology. |
| betterdungeons:small_dungeon | 1..2; 4/8 | 2..10; 2/8 | 0 / 6 / 4 of 10 | Compact underground masonry room, potentially visible through cave openings or excavation; no surface entrance or exterior landmark in this topology. |
| betterdungeons:spider_dungeon | no occurrences; 8/8 | 2..2; 6/8 | 0 / 2 / 0 of 2 | Big/small tunnels, nests and egg rooms form underground content; cave or terrain openings may reveal it, but an exterior landmark is not established. |
| betterdungeons:zombie_dungeon | no occurrences; 8/8 | 1..1; 6/8 | 0 / 2 / 0 of 2 | Underground chambers/tombs with a conditional surface staircase; terrain can expose an entry cue, while interior sections remain concealed. |
| bettermineshafts:mineshaft | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Underground tunnels are generally concealed; VerticalEntrance has vertical-shaft and surface-tunnel generation paths that may provide an entry cue. Their successful exposure depends on terrain and placement. |
| betteroceanmonuments:ocean_monument | 1..1; 6/8 | 1..1; 6/8 | 4 / 0 / 0 of 4 | Large ocean monument with chamber, dome, ring, parthenon and outside-shrine architecture; underwater portions require aquatic visibility, while upper portions may rise above sea level. |
| ctov:pillager_outpost | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Above-ground tower and surrounding camp features provide potential visual landmarks. |
| ctov:village | 1..2; 4/8 | 1..2; 4/8 | 8 / 0 / 0 of 8 | Settlement buildings, paths, fortifications and canopy designs can provide surface landmarks; the underground design starts14 below the surface projection. |
| dungeons_arise:abandoned_temple | 1..1; 6/8 | 1..1; 6/8 | 4 / 0 / 0 of 4 | Tall temple core and terrain-following roads; retained mountainous example shows roads greatly enlarge the footprint. |
| dungeons_arise:illager_galley | 1..1; 4/8 | 1..1; 4/8 | 8 / 0 / 0 of 8 | Two-section ship layout with tall architectural envelope and interior encounter pieces. |
| dungeons_arise:monastery | 1..1; 6/8 | 1..1; 6/8 | 4 / 0 / 0 of 4 | Raised monastery rooms, roofs, corridors and bridges; terrain affects actual exposure. |
| dungeons_arise_seven_seas:corsair_corvette | 1..1; 6/8 | no occurrences; 8/8 | 2 / 0 / 0 of 2 | Ocean-surface vessel with a tall authored hull/superstructure envelope. Its outline is a source-supported above-water discovery cue; lower hull and interior contents may be obscured. |
| dungeons_arise_seven_seas:pirate_junk | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Ocean-surface vessel with a tall authored hull/superstructure envelope. Its outline is a source-supported above-water discovery cue; lower hull and interior contents may be obscured. |
| dungeons_arise_seven_seas:unicorn_galleon | 1..1; 6/8 | no occurrences; 8/8 | 2 / 0 / 0 of 2 | Ocean-surface vessel with a tall authored hull/superstructure envelope. Its outline is a source-supported above-water discovery cue; lower hull and interior contents may be obscured. |
| dungeons_arise_seven_seas:victory_frigate | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Ocean-surface vessel with a tall authored hull/superstructure envelope. Its outline is a source-supported above-water discovery cue; lower hull and interior contents may be obscured. |
| explorations:campsite | no occurrences; 8/8 | 1..1; 6/8 | 0 / 2 / 0 of 2 | Surface campsite with alternative bases, tents, seating, hay and pen components; low outdoor forms can blend with terrain. |
| explorations:desert_ruin | 1..1; 6/8 | 2..2; 6/8 | 4 / 0 / 0 of 4 | Small surface masonry ruin; eight standalone alternatives differ in damage and height. |
| explorations:floating_island | 3..4; 4/8 | 7..9; 4/8 | 8 / 0 / 0 of 8 | Elevated island placed from the surface heightmap with a +60 start offset. Its aerial outline is a qualitative discovery cue; reaching it presents a height/access challenge. |
| explorations:forgotten_well | 1..1; 6/8 | 7..7; 6/8 | 1 / 3 / 0 of 4 | Small surface well with a +1 start offset; terrain and vegetation may obscure its low outline. |
| explorations:large_oak_tree | 4..4; 6/8 | 9..9; 6/8 | 3 / 1 / 0 of 4 | Large surface oak tree with a broad canopy. Tree silhouette is a qualitative cue, while similar surrounding trees may conceal its distinct form. |
| explorations:logs | 2..2; 6/8 | 6..6; 6/8 | 0 / 2 / 2 of 4 | Low fallen-log forms with small and large alternatives, visually blending with wooded terrain. |
| explorations:scarecrow | 1..4; 2/8 | 2..4; 2/8 | 0 / 7 / 5 of 12 | Small upright five-position figure with material and facing variants. |
| explorations:slime_cave | 4..4; 0/8 | 16..16; 0/8 | 0 / 16 / 0 of 16 | Underground cave chamber; natural caves or terrain openings may reveal it, but no surface landmark is guaranteed. |
| explorations:underground_temple | 3..3; 0/8 | 9..12; 0/8 | 0 / 16 / 0 of 16 | Underground corridors, shafts and rooms with a quest-tower component; cave intersections may reveal interiors, but no guaranteed surface landmark is established. |
| explorify:desert_shrine | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Compact desert shrine with below-surface start and stored loot. |
| explorify:supply_cache | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Small biome-themed 3x4x4 cache installations at the surface reference. |
| idas:ancient_portal | 1..1; 6/8 | no occurrences; 8/8 | 0 / 2 / 0 of 2 | Large portal-frame architecture provides an interior landmark when exposed; underground placement and Nether terrain can obscure it. No surface marker, visible entrance, measured sightline or tested portal navigation is established. |
| idas:animal_den | no occurrences; 8/8 | 1..1; 6/8 | 0 / 2 / 0 of 2 | Small mound and den cavity, with biome-related materials, provide terrain-like local cues. The8-block template height and surrounding vegetation or terrain can obscure the opening. No guaranteed visible entrance or measured discovery distance. |
| idas:bearclaw_inn | 1..1; 6/8 | no occurrences; 8/8 | 0 / 2 / 0 of 2 | Lodge building, connecting path and separate stable yard provide settlement cues distinct from a single isolated house. Terrain and vegetation can hide parts of the assembly. No measured sightline, visible route guarantee or actual service availability is established. |
| idas:desert_camp | no occurrences; 8/8 | 3..3; 6/8 | 2 / 0 / 0 of 2 | Low open worksite, campfire and scattered equipment provide local cues against desert ground. Material and vegetation substitutions remain variants. Four-block template height is not a reliable distant landmark; no measured sightline or discovery distance. |
| idas:desert_market | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Multi-level framed stalls, shaded planted upper details and17-by17 template footprint with16-block height provide architectural cues. Desert material and ladder differences remain variants. Terrain can obscure the structure; no measured discovery distance, visible-entrance guarantee or tested navigation claim. |
| idas:nexus | no occurrences; 8/8 | 1..1; 4/8 | 0 / 4 / 0 of 4 | Broad multi-lobed underground chamber alternatives with central spawner, barrels, material variation and sculk detail. These offer local interior cues but no surface discovery marker is established. No visible entrance, sightline distance or generated exposure measurement. |
| idas:pillager_camp | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Low surface camp, readily obscured by terrain or vegetation. |
| idas:sunken_ship | 1..1; 4/8 | 1..1; 4/8 | 0 / 6 / 2 of 8 | Long hull, mast/deck and furnishings provide ship-shaped cues, with coral decoration in its variant. Water and seabed terrain may obscure the wreck. This differs from detached debris but does not establish visible masts above water, a surface marker or measured sightline. |
| idas:sunken_ship/sunken_ship_ruins | 1..1; 4/8 | 5..6; 4/8 | 0 / 8 / 0 of 8 | Detached wreckage and loot-bearing barrels provide local seabed cues, distinct from the larger mast/deck hull family. Water, terrain and debris can obscure the small structures. No surface marker, visibility distance or guaranteed visible cache is established. |
| idas:underground_camp | 1..2; 4/8 | 2..6; 2/8 | 0 / 6 / 4 of 10 | Small workstation, toolbox, crafting/sack and suspicious-gravel cues distinguish the camp from nearby rock once exposed. Deep alternatives use deepslate and raw-metal blocks. No surface marker, visible cave route or discovery distance is established. |
| integrated_villages:village | 1..1; 6/8 | 1..1; 2/8 | 8 / 0 / 0 of 8 | Settlement buildings and paths are potential landmarks; elevated airships provide an aerial silhouette and lowered pirate components can be obscured by terrain or water. |
| minecraft:ancient_city | 1..1; 4/8 | 1..5; 4/8 | 0 / 8 / 0 of 8 | Large buried city with deepslate walls/buildings, soul-lantern cues and selected sculk patches. Primarily discoverable within underground openings rather than from a guaranteed surface landmark. |
| minecraft:nether_fossil | 7..7; 6/8 | 28..28; 6/8 | 2 / 0 / 2 of 4 | Bone-block skeletal fragments above a supporting surface provide a visual cue. Frozen-stack occurrences include Overworld dryland as well as Nether soul-sand valley; exposure and sightline distance are not measured. |
| minecraft:ocean_ruin | 3..4; 4/8 | 11..13; 4/8 | 0 / 6 / 2 of 8 | Seafloor masonry remnants in warm and cold material treatments, with variable integrity and possible multiple buildings. Water cover, supporting terrain and burial affect exposure; neither the family name nor nominal template size proves visibility from the surface. |
| minecraft:ruined_portal | 1..2; 2/8 | 2..3; 0/8 | 6 / 6 / 2 of 14 | Broken obsidian/crying-obsidian portal frames and surrounding netherrack or altered materials provide cues where exposed. Surface, mountain, underground, partly buried, ocean-floor and Nether placement modes differ; overgrowth and terrain/water can conceal the frame. No guaranteed exposed portal or measured discovery distance. |
| minecraft:shipwreck | 1..2; 4/8 | 6..7; 4/8 | 0 / 8 / 0 of 8 | Ship hull fragments and, in applicable templates, a mast provide visual cues. Ocean-floor and partially buried beached placement change exposure; nominal template dimensions are not visible dimensions. |
| minecraft:trial_chambers | 1..1; 4/8 | 1..4; 0/8 | 0 / 10 / 2 of 12 | Buried chamber/corridor complex with copper-bulb lighting and oxidation variants, spawners, vaults and room connections as internal cues. |
| mss:castle_ruin | no occurrences; 8/8 | 1..1; 4/8 | 4 / 0 / 0 of 4 | Broad low island with scattered ruined masonry and a short tower remnant; open rubble may conceal spawners and chests. |
| mss:castle_tower | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Compact fortified tower on an encircling island; upper enclosure can conceal the skeleton spawner. |
| mss:desert_pyramid | 1..1; 6/8 | no occurrences; 8/8 | 2 / 0 / 0 of 2 | Stepped pyramid on an island with top and side components; the silhouette does not expose its internal encounter layout. |
| mss:diorite_house | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Crossed-roof dwelling on a broad developed island with a deep lower mass and projecting sides. |
| mss:large_tower | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Tower complex with a developed base, descending masses, side platforms and upper tower; enclosures can hide encounters. |
| mss:red_sand | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Developed arid island with projecting side, terraces, vegetation and rooms; enclosed areas can hide spawners and containers. |
| mss:small_tower | 1..1; 6/8 | no occurrences; 8/8 | 2 / 0 / 0 of 2 | Narrow vertical ruin with separated descending island remnants; fragments belong to the same template and enclosure can conceal chests and hostile spawners. |
| mss:tree | 1..1; 6/8 | 1..1; 4/8 | 6 / 0 / 0 of 6 | Eight distinct tree/island shapes with different crown outlines and source heights; elevated silhouettes can be clues without promising a sight distance. |
| mss:volcano | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Crater-like elevated masonry complex with connected encounter spaces; the outer form does not reveal interior threats. |
| mvs:cart | 1..1; 4/8 | 1..1; 4/8 | 6 / 2 / 0 of 8 | Small cart and larger cargo-cart forms, including a bamboo variant; low profiles and cargo can conceal containers. Saved traders are source inhabitants, not a guaranteed discovery cue. |
| mvs:cartographer_tower | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Tall furnished tower with an attached upper section and optional villager. Enclosure conceals internal loot; the vertical silhouette is a potential surface landmark. |
| mvs:dead_tree | 1..1; 4/8 | 1..1; 6/8 | 6 / 0 / 0 of 6 | Bare wood/tree silhouettes or smaller trunk remnants, with size and biome-material differences. They may blend with surrounding woodland or vegetation. |
| mvs:desert_pump | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Narrow upright decorative desert pump form with signs. |
| mvs:floating_islands | 1..1; 6/8 | no occurrences; 8/8 | 2 / 0 / 0 of 2 | Elevated island forms, one with a house and optional villager. Height and open-sky silhouette can aid visibility; distance, terrain and viewing angle still constrain discovery. |
| mvs:harvest_heap | 3..6; 4/8 | 2..14; 2/8 | 6 / 4 / 0 of 10 | Loose raised hay, pumpkin and mixed-crop heaps, with smaller variants. Low crop forms and decoration can conceal containers. |
| mvs:lantern | 1..1; 6/8 | 3..4; 4/8 | 4 / 2 / 0 of 6 | Slender upright lantern landmarks with wood, size and campfire variants; narrow silhouettes can be obscured by vegetation. |
| mvs:large_warped_tower | no occurrences; 8/8 | 1..1; 4/8 | 4 / 0 / 0 of 4 | Tall enclosed warped-material tower with an attached upper ornament. The silhouette may be visible while internal skeleton sources remain concealed. |
| mvs:living_tree | no occurrences; 8/8 | 1..2; 2/8 | 5 / 0 / 1 of 6 | Living tree silhouettes, including broad crowns, smaller trees and a jungle palm. Canopies may stand above nearby ground cover but blend into woodland; Big Oak container contents need not be visible. |
| mvs:paths | no occurrences; 8/8 | 1..1; 4/8 | 2 / 0 / 2 of 4 | Two low landscaped linear routes with dirt-path terrain, borders, vegetation, lights and containers. Vegetation can obscure route details; these templates do not establish a connected travel network. |
| mvs:pond | no occurrences; 8/8 | 2..2; 6/8 | 2 / 0 / 0 of 2 | Low landscaped ponds with mushroom or oak vegetation and surface containers. Vegetation and terrain can obscure water edges or contents. |
| mvs:snowy_fossil | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Snow-biome fossil-shaped structure; local snow and terrain can obscure portions. |
| mvs:stall | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Colored canopy/stall layouts with containers and banner trim; built shelter forms can stand out while cargo remains concealed. |
| mvs:villager_statue | no occurrences; 8/8 | 1..1; 4/8 | 4 / 0 / 0 of 4 | Tall weathered villager-like stone figure with vines; upright silhouette is a source landmark, not an authored live villager. |
| mvs:well | 2..2; 4/8 | 2..4; 4/8 | 8 / 0 / 0 of 8 | Compact well landmarks with biome/material variants, small copper/tower layouts and a larger rare-well form. Upper structures may be visible while lower containers remain concealed. |
| mvs:wheat_grain_bin | 1..1; 6/8 | 2..3; 4/8 | 4 / 2 / 0 of 6 | Elevated storage-bin body on supporting legs with a hopper; upright form is a qualitative landmark, not evidence of an operating production loop. |
| mvs:windmill | 1..1; 4/8 | 2..3; 4/8 | 8 / 0 / 0 of 8 | Small upright support with four projecting sail-like arms; distinctive rotor depiction, without demonstrated rotation or power output. |
| mvs:wooden_wheat_farm | 1..1; 4/8 | 1..4; 4/8 | 8 / 0 / 0 of 8 | Low fenced cultivation plot with wheat, composters and storage decoration; crops and borders can obscure contents. |
| quark:fairy_ring | 1..2; 6/8 | 1..1; 6/8 | 0 / 4 / 0 of 4 | Source-derived surface flower ring marking buried ore. Incomplete placement or copied air can prevent a visible ring. No measured visibility distance. |
| quark:monster_box | 93..326; 0/8 | 94..328; 0/8 | 0 / 8 / 8 of 16 | Source-derived single underground block with activation sound and client flame/smoke particles. Terrain can conceal it; no observed visibility distance is claimed. |
| repurposed_structures:igloo | 1..1; 6/8 | 1..1; 6/8 | 2 / 0 / 2 of 4 | Small biome/material-adapted shelter at the surface. A trapdoor can lead through a ladder shaft to a concealed basement; closed-top alternatives do not establish basement presence. Vegetation, terrain and water affect visibility. No sightline measurement. |
| repurposed_structures:mineshaft | 2..2; 6/8 | 2..5; 2/8 | 0 / 8 / 0 of 8 | Branching supported corridors and rails provide local architectural cues when exposed by caves or excavation. Burial intent generally obscures them from surface travel. MineshaftSkyViewProcessor suppresses applicable blocks at or above local OCEAN_FLOOR_WG, with a supported-rail exception; this is not a guarantee that every component is hidden or a measured sightline. |
| repurposed_structures:outpost | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Watchtower/tower silhouette and surrounding camp/cages provide qualitative local landmarks. Forest cover, terrain and submerged ocean placement can obscure them. Elevated architecture does not establish a sightline distance or guaranteed visible entrance. |
| repurposed_structures:pyramid | no occurrences; 8/8 | 1..1; 2/8 | 0 / 4 / 2 of 6 | Pyramid body provides an above-terrain architectural cue when exposed; pit and hidden-room components can remain buried. Forest vegetation, partial burial and ocean placement can obscure access. This is a qualitative description, not a measured sightline or guaranteed entrance exposure. |
| repurposed_structures:ruins | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Fragmentary buildings and masonry, with large/small land pieces and Nether ruins. Terrain and vegetation may conceal small fragments. Material degradation and missing blocks reduce architectural continuity. No measured sightline or guaranteed discovery distance. |
| repurposed_structures:temple | no occurrences; 8/8 | 1..1; 6/8 | 0 / 2 / 0 of 2 | Compact enclosed temple architecture. Taiga terrain burial, submerged ocean placement and Nether terrain can obscure entrances or lower rooms. Architectural form is a qualitative cue, not a measured sightline or guaranteed visibility. |
| supplementaries:cave_urn_cache | 818..3796; 0/8 | 842..3856; 0/8 | 0 / 14 / 2 of 16 | Scattered treasure-state urns on supported air positions below terrain. |
| supplementaries:galleon | no occurrences; 8/8 | 1..2; 4/8 | 4 / 0 / 0 of 4 | Large sailing ship with mast/sails, deck, submerged hull rooms and optional nearby boats. |
| supplementaries:road_sign | 1..1; 6/8 | 1..1; 6/8 | 4 / 0 / 0 of 4 | Small ground patch with a wood/stone post, directional signs and optional lantern/candle details. Empty destination result creates a notice board instead. |
| terralith:rubble | no occurrences; 8/8 | 1..2; 4/8 | 2 / 2 / 0 of 4 | Small archaeological masonry/timber remnants with size and material alternatives, starting one block below surface projection. |
| terralith:underground/mining_outpost | no occurrences; 8/8 | 1..2; 4/8 | 0 / 2 / 2 of 4 | Underground cache/shelter requiring cavities, openings or excavation for discovery; no guaranteed surface marker. |
| terralith:underground/old_refinery | no occurrences; 8/8 | 1..1; 4/8 | 0 / 4 / 0 of 4 | Buried structure; existing template form and fixed underground height range imply limited surface visibility. |
| towns_and_towers:desert_mimic | 1..1; 6/8 | no occurrences; 8/8 | 2 / 0 / 0 of 2 | Pyramid form can expose an entrance above buried passages, but fixed height rather than surface projection makes visibility depend on local terrain. |
| towns_and_towers:ocean_village | 1..1; 6/8 | 1..1; 6/8 | 4 / 0 / 0 of 4 | Fleet of mast-bearing ships near ocean level; larger silhouette than isolated wreckage, with below-deck occlusion. |
| towns_and_towers:ocean_wreckage | 1..1; 6/8 | 1..1; 4/8 | 6 / 0 / 0 of 6 | Low debris footprint near ocean level; less vertical prominence than the ship families. |
| towns_and_towers:village | no occurrences; 8/8 | 1..1; 6/8 | 2 / 0 / 0 of 2 | Variant-specific settlement silhouettes: house/street clusters, concentrated Grove building and Snowy Slopes inn, trader tents, lighthouse, boats and vertical ramshackle forms. Roads, roofs and buildings suggest visible landmarks while interiors and surrounding vegetation/terrain occlude content. |
| yungsextras:desert_giant_torch | no occurrences; 8/8 | 1..1; 6/8 | 1 / 1 / 0 of 2 | Freestanding torch with four campfires above sandy ground. |
| yungsextras:desert_obelisk | 2..2; 6/8 | 2..2; 6/8 | 2 / 2 / 0 of 4 | Freestanding obelisk above sandy ground; decoration and damaged height vary. |
| yungsextras:desert_small_ruins | 2..2; 6/8 | 2..3; 6/8 | 0 / 1 / 3 of 4 | Small ruined building at sandy ground level, containing two authored loot chests. |
| yungsextras:desert_well | 3..4; 6/8 | 3..7; 6/8 | 0 / 4 / 0 of 4 | Surface well with a buried lower section and archaeology markers; dry, water-filled and wishing variants. |

Source identity: Item 8 inventory SHA-256 `4f7853b7b6531f99d3f0592b2129291d2e0cf24b4ad5d1381b3883dbdcfbc52d`. Each row uses `families[ID].visual_discoverability`; placement definitions and original limitations remain linked in that record. The full world tables retain selected variant, biome, geometry and count denominators. Source visual forms cannot prove actual doorway visibility.
