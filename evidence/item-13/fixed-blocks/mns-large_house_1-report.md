# Large House 1: quality assessment

Status: IN PROGRESS. Saved/source enemy and reward inputs are integrated;
room topology, routes, full task timing and quality synthesis remain required.

Sample: full-biome-diverse-r2-baseline|minecraft:the_nether|mns:large_house_1|5|3.
The retained [saved blocks](mns-large_house_1.json.gz), SHA-256
7ee67bdf2bc014bff8c08c4fb981018ff27dbea9483da430ee882618aeb361d1,
contain 72,981 voxels. Envelope [70,32,25,90,76,71], padded bounds
[67,29,22,93,79,74]. Existing extraction records retain complete block coverage,
world/archive identity and before/after inventory verification. Reuse these bytes;
no new world generation, extraction or runtime experiment is needed for intake.

## Active source and positional correspondence

The saved rigid versioned component selects `mns:houses/large_house_1` on frozen
Minecraft 1.21.1 through its `1.21-1.21.4` map entry. Its origin is (90,32,25),
rotation CLOCKWISE_90 and processors empty. Source local (u,v,w) maps to
(90-w,32+v,25+u). Later-version templates are not the active source.

Retained MNS JAR SHA-256:
05024f18690436fff2fbc088f880a95cc30f23bacfe6e8058f6b02106032a990.
Resource `data/mns/structure/houses/large_house_1.nbt`, SHA-256
66adecc037fc69b38d88ffbf89fa2c0b8fd5d14852f8ea3bf1ce25a952222c4c,
has dimensions 47x45x21 and no entity entries. These dimensions identify the
layout; they do not count rooms or vertical progression.

All seven source spawners and sixteen source barrels map to the matching saved
block entity at the transformed coordinate. Spawner SpawnData, SpawnPotentials,
Delay, SpawnCount, Min/MaxSpawnDelay, MaxNearbyEntities, RequiredPlayerRange and
SpawnRange match exactly. Barrel LootTable assignments match; saved loot seeds
are not interpreted as generated contents.

| Spawner position | Explicit source type | Saved initial Delay, ticks |
| --- | --- | ---: |
| (76,33,35) | wither skeleton | 0 |
| (78,35,62) | wither skeleton | 0 |
| (79,45,56) | blaze | 32 |
| (75,45,56) | blaze | 79 |
| (75,47,37) | piglin brute | 173 |
| (77,51,63) | piglin | 237 |
| (76,52,63) | piglin brute | 497 |

All use SpawnCount 4, SpawnRange 4, RequiredPlayerRange 16,
MaxNearbyEntities 6, MinSpawnDelay 200, MaxSpawnDelay 800 and empty potential lists.
This establishes seven authored sources, four hostile types and zero source-
resident entities. It does not establish 28 enemies, simultaneous activation,
realized encounters or a lifetime population ceiling. Spawner activation must
follow the eventual route and each saved delay before combat timing is scored.

| Loot table | Source/saved barrel positions | Count |
| --- | --- | ---: |
| `mns:chests/houses` | (75,33,34), (75,34,34), (80,44,40), (74,44,51) | 4 |
| `mns:chests/uncommon` | (75,33,33), (80,45,41), (74,44,52) | 3 |
| `mns:chests/treasure` | (75,33,32), (77,35,62), (76,35,62), (76,36,62), (74,45,51) | 5 |
| `mns:chests/empty` | (76,33,31), (80,44,41), (78,51,63), (76,51,63) | 4 |

Table names are not outcomes. In particular, `empty` is a real table with one
2..4-roll pool combining an empty alternative and small item alternatives such
as wart, gold nuggets, bones and string. Its four barrels must not be classified
as guaranteed empty or used to label rooms dead. All sixteen retain reward potential;
access and generated/acquired inventories are not measured by this correspondence.

Source table hashes in the same retained JAR:

- `data/mns/loot_table/chests/houses.json`: 7da643c38cccfd46819634bd09dafa5429f0d47b55c8dc6acc18907e1477bbbf.
- `data/mns/loot_table/chests/uncommon.json`: f6729e4590d9ed6968f8e3e0be82b9fd826aa90561671379d484a508efb76b6f.
- `data/mns/loot_table/chests/treasure.json`: 49a977507ae1da435df3ef9ff05ce0157dfa2940c33033eba37d06a6faf76d42.
- `data/mns/loot_table/chests/empty.json`: ee2b49fc5828c50a45e3650280b166fd7738a1a2374488b621c1b6443e2d8d01.

The treasure table's first pool has three rolls among weighted netherite,
debris/scrap, diamond equipment/material and enchanted-apple alternatives. It also
has material and template pools. This supplies potential payoff evidence, not a
rolled inventory or a proof that the highest barrel is the finale. Houses and
uncommon tables likewise contain weighted equipment/material alternatives.

All 987 saved WORLD_SURFACE columns are Y127. The 51-block difference above the
envelope top is heightmap context, not 51 solid blocks of burial or playable depth.

## Next bounded measurement

Inspect the retained slices and source layout to delineate actual rooms and links,
then validate one complete entrance-to-objective route before timing. Prioritize
the transitions connecting the Y33..36, Y44..47 and Y51..52 object groups; those
height groups are targets for inspection, not presumed floors. Resolve barrel
access, hazards and activation distances before declaring encounter populations.
Use the accepted complete-task accounting method and existing collision tools.

Direct block/source checks use the existing 72,981-voxel sample: budget one minute,
512 MiB and under 1 MiB textual results. If a full slice image is needed, allow
one bounded render up to 180 seconds and 20 MiB of temporary image/SVG output;
record a timeout instead of repeatedly rerunning it. Preserve raw input unchanged.
No new server or world materialization is part of this step. Item 14 is UNSTARTED.

## Authored vine columns and blocked axial exits

The active template has exactly three X/Z columns of twisting vines. The mapped
saved columns retain the following geometry:

| Column | Vine blocks | Immediate upper geometry | Current conclusion |
| --- | --- | --- | --- |
| (77,60) | Y35..40 plant, Y41 tip | Full crying obsidian at Y42, air Y43..45 | The axial ascent is capped. Seven vine blocks alone do not prove access to the upper floor. A side transfer or explicit breach must be resolved. |
| (80,59) | Y44..46 plant, Y47 tip | Open south-facing bottom-half crimson trapdoor Y48, east-facing top nether-brick stair Y49, warped planks Y50, wart block Y51 | The vine does not establish an unobstructed vertical shaft or roof connection. Exact side-exit geometry remains required. |
| (74,55) | One tip at Y44 | Wall-mounted crimson button at Y45, then air | This single plant is not evidence of a floor-to-floor route. |

At (77,60), full polished-blackstone bricks at Y33/34 support the vine base.
At (80,59), the base floor is nether bricks at Y43. The third base is crimson
planks at (74,43,55). Source positions establish authorship; saved block properties
above establish present obstructions. Do not count these three columns as three
playable links or infer a total vertical progression from their combined length.

These are direct inspections of the retained sample and active source named above:
filter source palette names for `twisting_vines`/`twisting_vines_plant`, transform
positions with (90-w,32+v,25+u), and read the adjacent saved cells using the existing
`render_pilot.state_at`. No runtime movement has been observed.

The initial render wrapper attempted `/usr/bin/time`, which is absent and returned
127 before starting the renderer. The same predeclared render was then started
with Bash's built-in `time -p` and the original 180-second timeout. This is a
wrapper failure, not a failed world sample or evidence regeneration. No tool was
installed to repair it.

## Saved main-level partitions

The bounded render completed successfully in 102.29 seconds (Bash time: user 86.89,
system 15.17). SVG plus PNG output totaled 12,109,694 bytes, within the 20 MiB
allowance. A live process snapshot showed 119,500 KiB RSS; this is not a measured
peak. The [retained slice image](mns-large_house_1-slices.png) is the 296,087-byte
PNG; the 11,813,607-byte SVG need not be duplicated in Git. The agent inspected
all Y32..76 slices and detailed Y32..39 and Y44..51 crops. These are saved block
categories, not collision shapes or a rendered human gameplay observation.

Reproduce with existing tooling:

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/mns-large_house_1.json.gz --output /tmp/item13-large-house-slices.svg
time -p timeout 180 convert -background white /tmp/item13-large-house-slices.svg /tmp/item13-large-house-slices.png
convert /tmp/item13-large-house-slices.png -crop 1436x1370+0+2100 +repage /tmp/item13-large-house-upper.png
convert /tmp/item13-large-house-slices.png -crop 1436x1370+0+60 +repage /tmp/item13-large-house-lower.png
```

The main-level interior is visibly partitioned near Z42 and Z50, between the
northern furnished space, middle furnished space and southern blaze space.
This is a room-boundary observation, not yet the complete building room count.
Exact saved cells resolve an actual link at the first partition: actor feet
(75.5,44,41.5) to (75.5,44,43.5), crossing Z42, traverse two horizontal blocks
with air at Y44/45 and full crimson-plank support at Y43. The 0.6-wide,
1.8-high adult fits without changing pose, mining, opening a door or traversing
a partial block. X76 also has air at Y44/45 through the partition, so the opening
has a two-block-wide clear span at that height. Stair decoration at Y46 does not
intrude into this actor's 1.8-block-high swept box.

The Z50 partition differs. Every X73..81 cell at Y44 and Y45 is a full nether-brick
or crimson-plank block. It is not an open doorway at the main walking height.
A direct passage there requires a breach or a separately established alternative;
no link is accepted merely because the rooms share a floor elevation. Upper
partial shapes and exterior access have not been relabeled as a proven bypass.

The long lower vine shaft also cannot supply an axial main-level link: all four
cardinal neighbors of (77,60) at Y40..42 are full polished-blackstone bricks,
while crying obsidian caps its center at Y42. At Y43 the four neighbors are
reinforced deepslate and the center is air. This supports a capped-shaft finding,
not an unobstructed climb from the lower treasure cluster into the blaze space.
Potential lower side exits or permitted breaching still need explicit routes.

These findings resolve one real inter-space connection and two concrete obstacles.
The outstanding requirement is a complete access graph covering lower reward
clusters, the three main spaces, upper reward positions and any other playable
activity space. Do not infer that graph from spawner heights or the tall tower.
