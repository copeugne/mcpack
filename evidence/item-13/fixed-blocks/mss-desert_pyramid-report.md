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

## Side-component disposition and husk model inputs

Inspection corrects the provisional entrance priority: the side component is not
an established doorway. Its complete active source has 486 air, 162 sandstone,
23 sand, seven stone, one dead bush and one jigsaw blocks. This is a terrain
appendage with no source reward or enemy, not evidence of a playable room or
entrance merely because its resource is named `side`. Saved Y175..179 sections
in that region are predominantly solid. Find the actual access through occupied
floor/body geometry rather than treating the component junction as a door.

Pinned mapped source supports a husk-specific nominal combat input without a
new runtime experiment. `DefaultAttributes` offsets 405..414 register HUSK using
`Zombie.createAttributes`. Reuse the established health 20, intrinsic armor 2
and iron-sword damage derivation in the model-source notes: ordinary unarmored
adults receive 5.904 nominal damage per full attack and require four hits, or
2.6 seconds of reserved 13-tick attack cycles. This is active attack work per
entity, not total combat time or a prediction of encounter count.

`Husk` extends Zombie, returns false from `isSunSensitive`, and applies HUNGER
when `doHurtTarget` succeeds with an empty main hand against a living target.
Its source duration is 140 times the integer effective local difficulty, in
game ticks. Do not assume an observed hunger duration or food consumption here.
`checkHuskSpawnRules` accepts spawner origin without the additional sky-visibility
condition required for its non-spawner branch; it still calls the underlying
monster spawn checks. This does not guarantee a successful attempt in these rooms.
These differences support two assigned enemy types, even though the nominal
per-entity attack-cycle workload matches. Actual sunlight exposure, hunger hits,
reinforcements, equipment, survival and realized populations remain unobserved.

Reproduce these source facts with `javap -c -p` on `Husk` and `DefaultAttributes`
in the already pinned mapped server JAR. They resolve the missing husk mechanism
input; route activation and repeated-spawn accounting are still required before
complete conditional timing can be declared.

A bounded full-envelope block-name query finds 39 vanilla cactus blocks and ten
`biomesoplenty:tiny_cactus` blocks. It finds no TNT, pressure plate, tripwire,
redstone, lava, fire or dispenser block. This rejects an assumed vanilla-pyramid
TNT trap for this retained envelope; it does not prove all gameplay hazards absent.
Cactus contact relevance and the modded tiny-cactus behavior require route/source
support before hazard scoring. No trigger or damage observation is fabricated.

## Preserved full-sheet render timeout

The first predeclared full-sheet attempt failed at the 180-second conversion
limit, exit 124. Bash timing: real 180.02, user 187.22, system 1.09 seconds.
The SVG producer completed and wrote 36,017,200 bytes; the converter did not
return a successful image. No rendered-sheet inspection or complete visual
validation is claimed from this attempt. A live RSS snapshot during conversion
was 563,464 KiB, not a measured peak. The source extraction is unchanged.

Exact reproduction command:

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/mss-desert_pyramid.json.gz --output /tmp/item13-desert-pyramid-slices.svg
time -p timeout 180 convert -background white /tmp/item13-desert-pyramid-slices.svg /tmp/item13-desert-pyramid-slices.png
```

Do not rerun the unchanged full conversion. The 63-layer conversion exceeded
its time budget; the raw blocks are already retained. Continue direct saved-block inspection
and use a bounded sectional view for the relevant Y171..182 activity band. Any
renderer adjustment must remain confined to selecting explicit layers in the
existing path, retaining raw identity and default behavior; no second renderer
or new evidence framework is justified. This is a visualization failure, not a
failed generated-world sample or permission to omit uninspected topology.
