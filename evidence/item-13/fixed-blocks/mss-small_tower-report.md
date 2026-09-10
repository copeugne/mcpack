# Small Tower: quality assessment

Status: IN PROGRESS. Source/saved inputs are integrated; playable topology,
complete timing, quality synthesis and family repetitions remain required.
Items 14 through 18 remain UNSTARTED pending their predecessor gates.

Sample: full-ocean-heavy-r2-baseline|minecraft:overworld|mss:small_tower|26|20.
Reuse [saved blocks](mss-small_tower.json.gz), SHA-256
467abef723159bc158f717ffb54f895307529b4a37c0d91743af3d62458ea14f.
The 10,001-byte compressed extraction retains 92,664 padded voxels, envelope
[397,132,304,434,179,336] and bounds [394,129,301,437,182,339]. Existing selection,
extraction and custody records retain the accepted identity and full saved chunk
coverage. No new world generation, restore or runtime experiment is needed for
this source/block inspection. Reuse the fixed-layout batch's frozen identity.

## Active template and source correspondence

Retained MoogsSoaringStructures-1.21-2.1.2.jar SHA-256:
5392b23878488bf167669b9d9eb0ed3b129115155856ac28059e88d8ac9b0080.
Active resource `data/mss/structure/small_tower.nbt` SHA-256:
29d1955416dd0bea5c92f545b3197816d2855072fb4c5da3fdf82d85482d816b.
Its size is 33x48x38 and its source entity list is empty. The saved start has one
rigid, empty-processor, COUNTERCLOCKWISE_90 component at origin (397,132,336).
Local (u,v,w) transforms to (397+w,132+v,336-u). All source fields for the two
spawners and two chests match their corresponding saved payloads exactly.
One component or its 48-block height is not a room count or playable depth.

| Saved position | Source function | Saved state/input |
| --- | --- | --- |
| (428,144,311) | Witch source | Delay 0, assigned minecraft:witch |
| (413,157,310) | Wither-skeleton source | Delay 0, assigned minecraft:wither_skeleton |
| (427,144,312) | Single chest | mss:rare |
| (414,169,310) | Single chest | mss:houses_rare |

Both spawners have SpawnCount 4, SpawnRange 4, RequiredPlayerRange 16,
MaxNearbyEntities 6, MinSpawnDelay 200, MaxSpawnDelay 800 and empty SpawnPotentials.
Preserve their saved `minecraft:mob_spawner` id. Two assigned types and zero source
residents do not establish eight realized enemies or a single-batch lifetime cap.
Witch healing/potion behavior requires explicit source/model resolution before
using a fixed attack count or complete combat estimate. Reuse existing
wither-skeleton source support rather than repeating its prior audit.

Four decorated pots occur at (428,144,313), (410,158,313), (412,158,312), and
(413,158,312). Their saved payloads contain no item or LootTable. Source pot data
specifies four brick sherds; the saved representation omits that default list.
Do not call those payloads byte-identical or invent an additional loot inventory.
No source resident entities are present, and actual runtime populations are
NOT MEASURED.

## Loot potential

Reuse the previously inspected `mss:rare` table, SHA-256
ddb3f6cf10bda5bacb1aa8d84db1be25bc1e916fe35f75fad80a2705b89201c3,
and its potential-only disposition in the [Pyramid report](mss-desert_pyramid-report.md).
`data/mss/loot_table/houses_rare.json` has SHA-256
0bd53988b4201790e77a0a255110d1ffc881e00020fe00981996016639629cf0:

- Pool 1: 2..4 rolls, seven entries covering candles, lantern, clock, compass,
  name tag, gold nuggets and string.
- Pool 2: 4..7 rolls, nine entries covering iron/gold/diamond/lapis/redstone,
  redstone block, two book entries and golden apple.
- Pool 3: 0..1 rolls, eight entries including an empty alternative, book,
  diamond, golden apple, experience bottle, diamond sword, saddle and enchanted
  golden apple.

These are weighted table alternatives with functions, not guaranteed contents,
expected value or acquired items. Two separate chest arrangements are the local
container denominator. Their reach, lid clearance and route access are pending.
Do not infer final-room quality solely from the higher chest's table name.

## Bounded first geometry view

Predeclare a full default slice rendering of the 48 envelope layers. The smaller
44x39 padded footprint predicts roughly 15 MiB SVG based on the prior Pyramid
sectional view, with PNG additional but below a 24 MiB combined budget. This is
an estimate, not a measured output size. Allow one conversion capped at 180
seconds. Preserve any failure; do not repeat an unchanged timed-out render.
Use the existing renderer and raw file. No additional extraction or machinery.

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/mss-small_tower.json.gz --output /tmp/item13-small-tower-slices.svg
time -p timeout 180 convert -background white /tmp/item13-small-tower-slices.svg /tmp/item13-small-tower-slices.png
```

## Early route and witch-mechanism findings

The saved block scan identifies an eleven-cell west-facing ladder column at
(413,Y158..168,311), two west-facing ladder cells at (410,Y169..170,312), and a
separate south-facing ladder at (411,163,313). Exterior vines occur near
X432..433,Z315..317 in Y132..142. These are concrete access leads, not proof that
either ladder endpoints or vine transitions admit the declared actor. Check body
clearance, support, attachment and reward stations before connecting floors.

Pinned mapped `Witch.createAttributes` sets maximum health 26 and movement speed
0.25. In `aiStep`, after the earlier water/fire branches, a random draw below 0.05
and health below maximum selects `Potions.HEALING`. This is a conditional branch,
not a measured per-second healing rate. `performRangedAttack` returns immediately
while drinking. Healing and ranged attacks therefore cannot simply be modeled as
a generic passive 26-health target without declaring encounter state and healing
assumptions. The subsequent ranged-selection source includes harming, slowness,
poison and weakness alternatives; their conditions and actual effects remain to
be integrated if needed by the chosen complete scenario. No fixed witch combat
time, realized potion throw or human observation is claimed here.

Source identity is the existing mapped Minecraft JAR SHA-256
26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71.
Reproduce the new mechanism inspection:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar -c -p net.minecraft.world.entity.monster.Witch
```

## First-view result

The [full slice sheet](mss-small_tower-slices.png) completed cleanly in 101.44
seconds (user 97.24, system 2.83). SVG is 14,824,119 bytes; PNG is 232,816 bytes
at 2252x6211, combined 15,056,935 bytes. Both declared budgets pass. The agent
inspected its overall height distribution: the lower reward/source pocket, middle
source platform and upper reward band are separated vertically, with substantial
exterior air/support mass between them. The narrow higher column corresponds to
the ladder leads, but the sheet does not prove actor clearance or connectivity.
Its overview scale is not used to read individual collision properties; exact
saved block queries remain required. No failed conversion or repeat extraction
occurred. Next validate entry, the lower pocket and the ladder endpoints before
assigning rooms, depth or complete task cost.
