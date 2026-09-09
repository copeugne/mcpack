# Desert Pyramid: quality assessment

Status: IN PROGRESS. Active component assembly and source/saved encounter and
reward inputs are integrated. Playable topology, full timing and quality synthesis
remain required. Item 14 stays UNSTARTED.

Sample: full-biome-diverse-r2-baseline|minecraft:overworld|mss:desert_pyramid|8|29.
Reuse [saved blocks](mss-desert_pyramid.json.gz), SHA-256
7dfc8e4d500459ad0839137e3939e9ee19df3a6b3cf1c7ae709b2711f8eb43a4.
This 17,911-byte compressed extraction retains 219,834 padded voxels, envelope
[99,134,440,151,196,487] and bounds [96,131,437,154,199,490]. Existing extraction
and custody records retain the accepted world identity and full chunk coverage.
No regeneration, new world read or runtime experiment is part of this intake.

## Active source assembly

Retained MoogsSoaringStructures-1.21-2.1.2.jar SHA-256:
5392b23878488bf167669b9d9eb0ed3b129115155856ac28059e88d8ac9b0080.
Resolve the base's saved version map using the frozen Minecraft 1.21.1 entry,
`1.21-1.21.8 -> mss:desert_pyramid`, not its later-version location field.
All three saved components are rigid, CLOCKWISE_90, with empty processors.

| Active resource under data/mss/structure/ | Source size | Saved origin | Resource SHA-256 |
| --- | --- | --- | --- |
| desert_pyramid.nbt | 48x48x48 | (151,134,440) | 0291712faf6811316e199888b1a6c1144a849296c3b14286ada557a46c6b5b70 |
| desert_pyramid_top.nbt | 48x15x48 | (151,182,440) | 1f004da3ed8bb53ef3615c58d29209707753e02bb597c88e1914d5c835da29cd |
| desert_pyramid_side.nbt | 17x8x5 | (103,175,454) | fd366e332a22e46e2e05352f91e93abd30aeebbfef561a2c7a9c8e2cc80f6186 |

For each origin (ox,oy,oz), source local (u,v,w) maps to (ox-w,oy+v,oz+u).
All three source entity lists are empty. Base contributes ten spawners and two
chest blocks; top contributes one spawner and two chest blocks; side contributes
neither. Component counts and saved junction offsets are assembly evidence, not
room counts, stair connectivity or dungeon depth.

## Enemy sources and unresolved realized population

All eleven source spawner positions and their SpawnData, SpawnPotentials, Delay,
SpawnCount, Min/MaxSpawnDelay, RequiredPlayerRange, MaxNearbyEntities and SpawnRange
match the saved payloads. Preserve their saved `minecraft:mob_spawner` block-entity
id; no raw normalization or replacement is performed.

| Position | Authored entity | Initial Delay, ticks |
| --- | --- | ---: |
| (110,181,464) | zombie | 0 |
| (111,178,449) | zombie | 0 |
| (114,178,454) | husk | 0 |
| (116,178,443) | husk | 0 |
| (118,180,467) | husk | 0 |
| (123,171,459) | zombie | 0 |
| (126,171,457) | zombie | 0 |
| (126,177,465) | husk | 0 |
| (127,178,450) | zombie | 169 |
| (132,181,481) | husk | 0 |
| (133,182,461) | husk | 0 |

All use SpawnCount 4, SpawnRange 4, RequiredPlayerRange 16, MaxNearbyEntities 6,
MinSpawnDelay 200, MaxSpawnDelay 800 and empty SpawnPotentials. This establishes
five zombie and six husk sources, two explicitly assigned types and zero source
residents. It does not establish 44 realized enemies or a one-wave lifetime cap.
Activation windows and permitted repetitions depend on the eventual route; no
combat time is assigned until those conditions and husk source mechanics are
resolved. Natural mobs and actual encounters remain NOT MEASURED.

## Reward blocks, paired containers and potential

All four source LootTable assignments match the saved records:

| Saved position | Saved chest state | Table |
| --- | --- | --- |
| (115,177,445) | single, south-facing | mss:rare |
| (115,177,452) | single, north-facing | mss:rare |
| (120,182,453) | left, north-facing | mss:general |
| (121,182,453) | right, north-facing | mss:general |

The adjacent left/right pair is one double-chest arrangement. Use four authored
loot-bearing block entities and three container arrangements as separate
denominators. A successful paired opening would expose 54 slots, not two unrelated
27-slot interactions. Pair/lid access and actual runtime opening still require
inspection. Stored LootTableSeed values do not establish rolled contents.

Packaged table `data/mss/loot_table/rare.json`, SHA-256
ddb3f6cf10bda5bacb1aa8d84db1be25bc1e916fe35f75fad80a2705b89201c3,
has one 3..7-roll uniform pool with 27 weighted entries, including diamond/iron/
gold/emerald, apples, netherite scrap, totem, heart of the sea, saddle/horse armor,
trident, equipment and book alternatives. This is potential, not a guaranteed
rare item or generated value. `general.json`, SHA-256
eb37851c0db1093cede4e0fdbab30378d766235a41dc2fe79d87d1e61038ec4f,
has three pools: 1..3 mineral rolls, 2..4 provision/material rolls and 0..1 rolls
from an empty-or-item bonus pool. Keep the two halves' assignments distinct even
when counting one paired container arrangement.

Five saved decorated pots have no item or LootTable field: (113,177,446),
(117,177,451), (122,177,448), (125,177,470), (126,172,454). They are not additional
authored loot nodes from this evidence. The three skull block entities likewise
do not constitute source-resident enemies. Actual generated/acquired loot remains
NOT MEASURED.

Reproduce correspondence with the existing NBT decoder on the named immutable
resources, transform source positions with each saved origin, and compare fields
against `block_entities` in the hash-bound extraction. Use `render_pilot.state_at`
for the four saved chest states. No new helper, validator or runtime probe is
required for these direct source/saved facts.

## Next bounded topology measurement

Inspect actual saved floor/body cells and a slice view before deriving rooms or
paths. Priorities are the side-component entrance, the Y171..182 spawner/reward
bands, their vertical connections, chest pairing/lid clearance and any meaningful
trap mechanism. A 63-block envelope height or three components is not playable
depth. Use the approved complete-task accounting after the route is validated.

Direct read-only queries: one minute, 512 MiB and under 1 MiB textual output.
A 63-layer envelope sheet uses the retained 219,834-voxel padded extraction; allow
one bounded render up to 180 seconds and at most 60 MiB SVG/PNG output, reflecting
its larger footprint than the prior tower. Preserve timeout or overrun rather
than repeatedly rerunning it. Reuse the existing renderer and extraction; no new
world generation, server work or evidence re-extraction is planned.
