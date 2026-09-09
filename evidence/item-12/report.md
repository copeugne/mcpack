# Item 12 discoverability results

Representative only. Full Item 12 gate remains open.

Protocol: [item12-discoverability-v1](protocol.md). Human recognition and player discovery rates: NOT MEASURED.

These are family-balanced saved-world cases, not discovery probabilities. Each case retains its full family abundance per 4,096 chunks separately from geometric rays. Overworld only; other dimensions retain Item 8 source assessment and Item 10 density. Architectural/entrance judgments are in [assessments](assessments.md); navigation evidence is [separate](navigation-source/README.md).

C/O/U means CLEAR/OCCLUDED/UNKNOWN, followed by the full ray denominator. Low/high use the complete eight-cell ring; UNKNOWN means at least one missing eye. Relief can include buildings or water, not just terrain. A clear envelope point is not a visible authored block, recognizable silhouette or entrance.

WORLD_SURFACE (WS) and MOTION_BLOCKING_NO_LEAVES (NL) use the same observer eye. NL is a foliage-sensitive heightmap comparison, not a measured no-trees world. Finite boundaries, fluid opacity, ignored overhangs/caves, purposive seeds and two repetitions limit interpretation. Zeroes do not prove absence.

## full-ordinary-r1-baseline

[Raw observations](results/full-ordinary-r1-baseline.json.gz), SHA-256 `3500ea443906cae3d7b26de8ee2eaec0e9a74b845a998c2b907d4794c6e4baac`. Selected cases: 14.

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
