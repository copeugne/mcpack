# Item 12 discoverability results

Representative only. Full Item 12 gate remains open.

Protocol: [item12-discoverability-v3](protocol.md). Human recognition and player discovery rates: NOT MEASURED.

These are family-balanced saved-world cases, not discovery probabilities. Each case retains its full family abundance per 4,096 chunks separately from geometric rays. Overworld only; other dimensions retain Item 8 source assessment and Item 10 density. Architectural/entrance judgments are in [assessments](assessments.md); navigation evidence is [separate](navigation-source/README.md).

C/O/U means CLEAR/OCCLUDED/UNKNOWN, followed by the full ray denominator. Low/high use the complete eight-cell ring; UNKNOWN means at least one missing eye or observer cell inside the target envelope. Internal viewpoints remain UNKNOWN in the full ray denominator. Relief can include buildings or water, not just terrain. Low and high cells also differ in azimuth, so this is not a causal elevation experiment. A clear envelope point is not a visible authored block, recognizable silhouette or entrance.

WORLD_SURFACE (WS) and MOTION_BLOCKING_NO_LEAVES (NL) use the same observer eye. NL is a foliage-sensitive heightmap comparison, not a measured no-trees world. Finite boundaries, fluid opacity, ignored overhangs/caves, purposive seeds and two repetitions limit interpretation. Zeroes do not prove absence.

## full-ordinary-r1-baseline

[Raw observations](results/full-ordinary-r1-baseline.json.gz), SHA-256 `284e44dc5fc934e9aa520a5ac90c619fa94487f4c2c604da476d7db485512027`. Selected cases: 14.

| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |
| --- | ---: | --- | ---: | --- | --- | --- |
| dungeons_arise:illager_galley<br>dungeons_arise:illager_galley@7,5 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 40/0/0 of 40; 40/0/0 of 40 |
| dungeons_arise_seven_seas:corsair_corvette<br>dungeons_arise_seven_seas:corsair_corvette@0,9 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 2/3/0 of 5; 2/3/0 of 5 | 2/3/0 of 5; 2/3/0 of 5 | 31/9/0 of 40; 31/9/0 of 40 |
| explorations:floating_island<br>explorations:floating_island@14,-29 | 4 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 23/12/5 of 40; 27/8/5 of 40 |
| explorations:slime_cave<br>explorations:slime_cave@-21,6 | 4 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| explorations:underground_temple<br>explorations:underground_temple@-24,-17 | 3 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship<br>idas:sunken_ship/sunken_ship@10,7 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| idas:sunken_ship/sunken_ship_ruins<br>idas:sunken_ship/sunken_ship_ruins@10,1 | 1 / 4096 | minecraft:deep_ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| integrated_villages:village<br>integrated_villages:airship_village@6,23 | 1 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/0/40 of 40; 0/0/40 of 40 |
| minecraft:ocean_ruin<br>minecraft:ocean_ruin_cold@0,-28 | 4 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/35/5 of 40; 0/35/5 of 40 |
| minecraft:shipwreck<br>minecraft:shipwreck@-15,21 | 2 / 4096 | minecraft:ocean | 0.0 | 0/5/0 of 5; 0/5/0 of 5 | 0/5/0 of 5; 0/5/0 of 5 | 0/40/0 of 40; 0/40/0 of 40 |
| minecraft:trial_chambers<br>minecraft:trial_chambers@29,30 | 1 / 4096 | minecraft:ocean | None | UNKNOWN extremum | UNKNOWN extremum | 0/10/30 of 40; 0/10/30 of 40 |
| quark:monster_box<br>nonregistry:2833 | 94 / 4096 | minecraft:ocean | 0.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| supplementaries:cave_urn_cache<br>nonregistry:22030 | 837 / 4096 | minecraft:ocean | 0.0 | 0/1/0 of 1; 0/1/0 of 1 | 0/1/0 of 1; 0/1/0 of 1 | 0/8/0 of 8; 0/8/0 of 8 |
| towns_and_towers:ocean_wreckage<br>towns_and_towers:wreckage_ocean@12,18 | 1 / 4096 | minecraft:ocean | 0.0 | 5/0/0 of 5; 5/0/0 of 5 | 5/0/0 of 5; 5/0/0 of 5 | 35/5/0 of 40; 35/5/0 of 40 |

### Biome-grouped ray denominators

Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.

| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |
| --- | ---: | --- | --- | --- |
| minecraft:deep_ocean | 6 | 71/169/0 of 240 | 71/169/0 of 240 | 0 / 240 |
| minecraft:ocean | 8 | 58/118/80 of 256 | 62/114/80 of 256 | 4 / 256 |

## Independent family abundance and discovery cues

14 observed canonical families out of the accepted 448 have sampled Overworld cases in this report. The other 434 have no case here, not proven absence from the pack. Their source assessments remain in the unchanged Item 8 inventory; Item 10 retains all-dimension density.

The count ranges below are existing full-frame placement counts, separately for baseline (B) and omit-Sparse control (C), among worlds in which the family occurs. Zero-occurrence worlds are shown separately. A case is WS-clear when any of its sampled rays clears; WS-occluded means every ray is occluded; the remaining cases are UNKNOWN/mixed without a clear ray. These are case counts, not all-placement discoverability rates. Source forms are reused artifact assessments, not new human recognition data.

| Family | B count range; absent worlds | C count range; absent worlds | WS clear / all-occluded / other cases | Reused architectural cue assessment |
| --- | --- | --- | --- | --- |
| dungeons_arise:illager_galley | 1..1; 0/1 | no occurrences; 0/0 | 1 / 0 / 0 of 1 | Two-section ship layout with tall architectural envelope and interior encounter pieces. |
| dungeons_arise_seven_seas:corsair_corvette | 1..1; 0/1 | no occurrences; 0/0 | 1 / 0 / 0 of 1 | Ocean-surface vessel with a tall authored hull/superstructure envelope. Its outline is a source-supported above-water discovery cue; lower hull and interior contents may be obscured. |
| explorations:floating_island | 4..4; 0/1 | no occurrences; 0/0 | 1 / 0 / 0 of 1 | Elevated island placed from the surface heightmap with a +60 start offset. Its aerial outline is a qualitative discovery cue; reaching it presents a height/access challenge. |
| explorations:slime_cave | 4..4; 0/1 | no occurrences; 0/0 | 0 / 1 / 0 of 1 | Underground cave chamber; natural caves or terrain openings may reveal it, but no surface landmark is guaranteed. |
| explorations:underground_temple | 3..3; 0/1 | no occurrences; 0/0 | 0 / 1 / 0 of 1 | Underground corridors, shafts and rooms with a quest-tower component; cave intersections may reveal interiors, but no guaranteed surface landmark is established. |
| idas:sunken_ship | 1..1; 0/1 | no occurrences; 0/0 | 0 / 1 / 0 of 1 | Long hull, mast/deck and furnishings provide ship-shaped cues, with coral decoration in its variant. Water and seabed terrain may obscure the wreck. This differs from detached debris but does not establish visible masts above water, a surface marker or measured sightline. |
| idas:sunken_ship/sunken_ship_ruins | 1..1; 0/1 | no occurrences; 0/0 | 0 / 1 / 0 of 1 | Detached wreckage and loot-bearing barrels provide local seabed cues, distinct from the larger mast/deck hull family. Water, terrain and debris can obscure the small structures. No surface marker, visibility distance or guaranteed visible cache is established. |
| integrated_villages:village | 1..1; 0/1 | no occurrences; 0/0 | 0 / 0 / 1 of 1 | Settlement buildings and paths are potential landmarks; elevated airships provide an aerial silhouette and lowered pirate components can be obscured by terrain or water. |
| minecraft:ocean_ruin | 4..4; 0/1 | no occurrences; 0/0 | 0 / 0 / 1 of 1 | Seafloor masonry remnants in warm and cold material treatments, with variable integrity and possible multiple buildings. Water cover, supporting terrain and burial affect exposure; neither the family name nor nominal template size proves visibility from the surface. |
| minecraft:shipwreck | 2..2; 0/1 | no occurrences; 0/0 | 0 / 1 / 0 of 1 | Ship hull fragments and, in applicable templates, a mast provide visual cues. Ocean-floor and partially buried beached placement change exposure; nominal template dimensions are not visible dimensions. |
| minecraft:trial_chambers | 1..1; 0/1 | no occurrences; 0/0 | 0 / 0 / 1 of 1 | Buried chamber/corridor complex with copper-bulb lighting and oxidation variants, spawners, vaults and room connections as internal cues. |
| quark:monster_box | 94..94; 0/1 | no occurrences; 0/0 | 0 / 1 / 0 of 1 | Source-derived single underground block with activation sound and client flame/smoke particles. Terrain can conceal it; no observed visibility distance is claimed. |
| supplementaries:cave_urn_cache | 837..837; 0/1 | no occurrences; 0/0 | 0 / 1 / 0 of 1 | Scattered treasure-state urns on supported air positions below terrain. |
| towns_and_towers:ocean_wreckage | 1..1; 0/1 | no occurrences; 0/0 | 1 / 0 / 0 of 1 | Low debris footprint near ocean level; less vertical prominence than the ship families. |

Source identity: Item 8 inventory SHA-256 `4f7853b7b6531f99d3f0592b2129291d2e0cf24b4ad5d1381b3883dbdcfbc52d`. Each row uses `families[ID].visual_discoverability`; placement definitions and original limitations remain linked in that record. The full world tables retain selected variant, biome, geometry and count denominators. Source visual forms cannot prove actual doorway visibility.
