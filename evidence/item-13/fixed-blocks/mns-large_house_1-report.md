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
