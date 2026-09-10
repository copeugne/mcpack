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

## Lower pocket: conditional entry, source and chest

Use local exterior station (428.5,144,310.5), supported by grass at Y143 with air
at Y144/145. The witch source at (428,144,311) is reachable on its north face from
this station. However, merely removing it leaves cobblestone at (428,145,311)
and only one block of headroom. That opening is not an upright or crouched actor
entrance. Predeclare removing that one cobblestone cover as well. Both targets
have clear north-face rays from the station: eye (428.5,145.62,310.5), aiming at
(428.5,145.5,311) for the cover and (428.5,144.5,311) for the source. The cover
can be removed first without touching the Y146 block above. Source and cover
removal leave grass support at (428,143,311) and two full air cells above it.

Enter through that cleared column and continue to (428.5,144,312.5), two horizontal
blocks from the exterior station. The interior station also has grass support
and two air body cells. From eye Y145.62, aim at (427.9375,144.5,312.5), the chest's
east face. The 1.253-block ray is unobstructed. Its top at (427,145,312) is air;
the saved single, south-facing chest has no Lock field. Under the existing
unlocked/no-blocking-entity scenario, one 27-slot GUI opening is supported.
The decorated pot at (428,144,313) is not on this route and need not be removed.
Reverse the two blocks to leave. No saved blocks or loot contents were changed.

This supplies a four-horizontal-block local out-and-back with two removals
(source plus cover), one container arrangement and its conditional combat work.
It does not yet connect this exterior station to the higher island. The one-block
headroom obstruction is a retained baseline defect in the first source-only entry
idea, not an observed failed human traversal.

## Main ladder and upper reward circuit

Use middle station (412.5,158,311.5). First move one block north to
(412.5,158,310.5), target the wither-skeleton source's exposed top center
(413.5,158,310.5), then return south. Both station columns have grass at Y157
and air at Y158/159, as does the volume above the source. Its interaction ray
is 1.903786 blocks from upright eye Y159.62; removal leaves both station floors
untouched. This is source access, not a realized encounter clear.

Enter the west-facing ladder column at (413.5,158,311.5), climb to feet Y169,
then exit west to (412.5,169,311.5). The eleven ladder cells Y158..168 are attached
to full blocks at X414: stone, stone bricks, andesite or double cobblestone slabs.
Their blocking plate occupies X413.8125..414, while the centered 0.6-wide actor
occupies X413.2..413.8. Reuse the pinned ladder/climbable and top-transfer model
from the prior house/Pyramid work. The column contains no intervening solid cap;
Y169/170 are air. The west exit has full andesite support at Y168 and air at
Y169/170. The modeled link is reversible and has eleven blocks of rise, with no
ladder replacement, mining or scaffolding required.

From that upper landing, move north to (412.5,169,310.5), then east to
(413.5,169,310.5). Both have full Y168 floors and two air body cells. Aim from eye
Y170.62 at (414.0625,169.5,310.5), the upper chest's west face, a 1.253-block ray.
The saved single, south-facing chest has no Lock field and air immediately above
at Y170. One 27-slot opening is supported under the same conditional container
model. Return over the same two upper horizontal blocks and descend the ladder.

From the middle station the complete local source/upper-chest out-and-back is ten
horizontal blocks and 22 ladder blocks: two horizontal for the source visit,
four for entering/exiting the ladder on ascent/descent, and four for the upper
chest visit. No new blocks are needed for that local circuit. The separate upper
ladder at X410 and the exterior vines remain outside this objective route and
must not be counted as additional connected rooms without their own assessment.
No runtime climb, GUI opening or acquired loot has been observed.

Reproduce the floor/body, attachment and container conditions:

```sh
uv run python - <<'SMALL_TOWER_ACCESS'
import gzip, hashlib, importlib, json
from pathlib import Path
p=Path('evidence/item-13/fixed-blocks/mss-small_tower.json.gz')
assert hashlib.sha256(p.read_bytes()).hexdigest()=='467abef723159bc158f717ffb54f895307529b4a37c0d91743af3d62458ea14f'
c=json.loads(gzip.decompress(p.read_bytes()))['cases'][0]
s=importlib.import_module('evidence.item-13.render_pilot').state_at
full={'minecraft:grass_block','minecraft:stone','minecraft:stone_bricks',
      'minecraft:andesite','minecraft:cobblestone'}
removed={(428,144,311),(428,145,311)}
assert s(c,428,144,311)['Name']=='minecraft:spawner'
assert s(c,428,145,311)['Name']=='minecraft:cobblestone'
assert s(c,428,146,311)['Name']=='minecraft:cobblestone'
for x,y,z in [(428,144,310),(428,144,311),(428,144,312),
              (412,158,311),(412,158,310),(412,169,311),(412,169,310),(413,169,310)]:
    assert s(c,x,y-1,z)['Name'] in full
    assert all((x,k,z) in removed or s(c,x,k,z)['Name']=='minecraft:air' for k in (y,y+1))
for y in range(158,169):
    assert s(c,413,y,311)=={'Name':'minecraft:ladder','Properties':{'facing':'west','waterlogged':'false'}}
    support=s(c,414,y,311)
    assert support['Name'] in full or support=={'Name':'minecraft:cobblestone_slab','Properties':{'type':'double','waterlogged':'false'}}
assert all(s(c,413,y,311)['Name']=='minecraft:air' for y in (169,170))
assert s(c,413,157,310)['Name']=='minecraft:spawner'
assert all(s(c,413,y,310)['Name']=='minecraft:air' for y in (158,159))
for x,y,z in ((427,144,312),(414,169,310)):
    assert s(c,x,y+1,z)['Name']=='minecraft:air'
    assert s(c,x,y,z)=={'Name':'minecraft:chest','Properties':{'facing':'south','type':'single','waterlogged':'false'}}
    be=next(b for b in c['block_entities'] if (b.get('x'),b.get('y'),b.get('z'))==(x,y,z))
    assert 'Lock' not in be
print('Lower pocket and main ladder/upper-chest local conditions pass.')
SMALL_TOWER_ACCESS
```
