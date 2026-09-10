# Small Tower: quality assessment

Status: local modeled/inspection assessment recorded. Source inputs, checked
connections, complete conditional timing and quality synthesis are integrated.
Family repetitions, broader coverage and Item 13 delivery remain IN PROGRESS.
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

## Inter-island connector: declared construction and checked geometry

The direct line between the lower station and middle source is not a native
level walkway. At Z310,Y157, X418..427 are air. X416..417 are oak-leaf support,
with another leaf at (417,158,310). The middle landing is blocked at X414..415,
Y158/159. Do not infer connectivity from the shared component envelope or count
the leaves as a durable constructed bridge. This rejects that direct walk,
without claiming that every possible native/parkour route has been exhausted.

Predeclare a 14-scaffold tower and 13-cobblestone connector after completing the
lower pocket. Remove short grass at (428,144,309), then stand at
(428.5,144,309.5), on grass at Y143. Place the first scaffold at (428,144,310) on
its full grass support; the placement ray to the floor top is unobstructed and
within reach, with the actor outside the target cell. Extend upward through Y157
using thirteen further scaffold side-clicks. All fourteen cells are saved air,
as are Y158/159 above. Reuse the pinned scaffolding extension and distance-zero
support rules already established for the Nether Tower. Do not substitute
horizontal scaffold extension beyond its supported distance limit.

Enter the column and climb from feet Y144 to Y158. The first bridge placement
requires a specific distinction from ordinary crouched edge building: crouching
on scaffolding can descend through it. Use an upright first edge station at
(427.9,158,310.5), retaining 0.2 blocks of overlap with the scaffold top. Aim at
(428,157.95,310.5), its exposed west upper-rim face, to place cobblestone at
(427,157,310). The ray is about 1.673 blocks from upright eye Y159.62 and reaches
the rim from outside its west face. The actor's feet are above the placed block,
and the new cobblestone then supports the transition to ordinary crouched
building. This is a stipulated precise stationary placement, not observed play.

Extend west to X418 with nine more cobblestone blocks at Y157,Z310. Every target
cell and both body cells above it are air. Use the previously established
crouched edge-placement geometry on the new full blocks. From the supported
X418 station, remove the leaf at (417,158,310), then replace the leaf floor at
(417,157,310) with cobblestone before entering it. Replace (416,157,310) similarly
from X417. Thus neither leaf floor is retained as required support.

From X416 at feet Y158, remove the two east-facing wall blocks at
(415,158,310) and (415,159,310), retaining the stone floor Y157. From the cleared
X415 station remove (414,158,310) and (414,159,310), again retaining its stone
floor. Their near vertical faces are within reach. From X414, disable the wither-skeleton
source at (413,157,310) using its exposed top, then fill that floor cell with the
thirteenth cobblestone. This prevents source removal from leaving a hole in the
connector. Reach (412.5,158,310.5), then move south one block to the already
verified main-ladder station (412.5,158,311.5).

The exact nine removals for this connector, including its source objective, are:

| Position | Saved block |
| --- | --- |
| (428,144,309) | short grass |
| (417,158,310) | oak leaves |
| (417,157,310) | oak leaves |
| (416,157,310) | oak leaves |
| (415,158,310) | cobblestone |
| (415,159,310) | mossy cobblestone |
| (414,158,310) | andesite |
| (414,159,310) | andesite |
| (413,157,310) | wither-skeleton spawner |

After those specified changes, every centerline column X412..428 at Z310 has
clear body cells Y158/159. The retained floor cells are grass at X412 and stone
at X414/415; new cobblestone occupies X413, X416..427, and the scaffold top supplies
X428. This continuous source-shape model joins the islands with fourteen blocks
of vertical rise and sixteen horizontal blocks across their gap/landing line.
It also connects to the main ladder through the checked one-block south exit.

Outbound movement from the lower station includes two horizontal blocks to visit
the scaffold-placement station and enter the column, fourteen vertical blocks,
then seventeen horizontal blocks to the main ladder station. The reverse journey
uses seventeen horizontal and fourteen vertical blocks, ending at the original
lower coordinates inside the retained distance-zero scaffold column. Hence the
connector out-and-back is 36 horizontal and 28 vertical blocks. The first
0.6-horizontal-block edge adjustment is already within the crossing distance;
it must be timed upright rather than as crouching on the scaffold. Later bridge
movement uses the appropriate declared crouch allowance. Precise allocation and
all mining/placement costs remain for the complete timing table.

The middle source is now removed as part of connector construction. Do not also
charge the earlier two-horizontal-block source detour in the full objective.
The main-ladder/upper-chest branch consequently contributes eight horizontal and
22 ladder blocks after arrival. This route costs more than local access alone;
no global minimum-construction claim is made. No construction or traversal was
performed in the accepted world, and any unsupported placement, fall, unexpected
block update or inaccessible target censors the conditional task.

## Witch mechanics and complete-task predeclaration

The pinned witch resistance tag contains magic, indirect_magic, sonic_boom and
thorns, not ordinary player melee. `Witch.getDamageAfterMagicAbsorb` multiplies
tagged damage by 0.15 and separately nullifies self-attributed damage. Do not
apply that resistance to the declared iron sword. The default ordinary witch
has 26 health and no added armor in `createAttributes`. With the existing six
points per fully recharged ordinary iron-sword hit, five attacks cost 3.25 seconds
of active work only **if no successful healing changes the damage requirement**.

`Potions.HEALING` supplies the base instant-heal effect; the pinned
`HealOrHarmMobEffect.applyEffectTick` calls heal(4 << amplifier) for an ordinary
non-inverted recipient. Each base heal can restore up to four points, capped by
missing health. For an externally specified effective healed amount E, ordinary
attack work is bounded by `0.65*ceil((26+E)/6)` if there are no other damage/armor
changes. This is not a complete combat estimate: the healing schedule and pursuit
must also be feasible. There is no finite lifetime-healing or encounter-time cap
established merely by the saved source. Do not infer a healing probability or
fixed number of drinks from the earlier conditional 0.05 branch.

For non-Raider targets, the inspected ranged selection starts with harming;
slowness is selected at horizontal aim-distance at least eight without existing
slowness, otherwise poison can be selected at health at least eight without poison,
otherwise weakness can be selected within horizontal aim-distance three without
weakness and with a random draw below 0.25. Aim-distance includes the target X/Z
velocity terms. These are ordered source conditions, not observed throws, hits
or player status. Drinking suspends ranged attacks. Preserve these
mechanics as encounter-quality inputs rather than treating the witch as an
ordinary passive health pool.

Reproduce with the existing mapped JAR and `javap -c -p` command, substituting
`net.minecraft.world.item.alchemy.Potions` and
`net.minecraft.world.effect.HealOrHarmMobEffect`; the resistance tag is
`data/minecraft/tags/damage_type/witch_resistant_to.json` in the retained extra
JAR. No new runtime experiment or gameplay observation was performed.

Use the approved complete-task method for this worked scenario. Begin/end at
(428.5,144,310.5), disable both sources, transfer both 27-slot chests, defeat the
modeled population and return alive. One fully informed adult begins with full
health/food, iron armor/sword, diamond pickaxe, fourteen scaffolds and thirteen
cobblestone, sufficient durability and conditional free inventory capacity. Use
20 TPS. Only the documented cover, grass, leaves, wall and source removals and
connector construction are permitted. No flight, teleportation, assistance,
extra construction, criticals, sweeps, player healing or status effects. Discovery,
travel to the local entry and resource procurement are outside the local task.
Ignore incidental mining/creature drops and leave construction in place.

At start, stipulate no pre-existing mobs and exclude natural spawning; retain
both saved Delay 0 inputs. Neither source is reset between phases. Clear the
witch population after the lower removals and before leaving that island; clear
the wither-skeleton population after completing the connector and before the
upper ladder/chest visit. Each combat-duty allowance includes pursuit and return
to its own starting station. No successful witch healing, other successful mob
healing, player debuff or unmodeled damage modifier occurs in the worked case.
Any such event invalidates this particular timing case; do not silently retain
its hit counts. Survival and target reachability are conditions, not predictions.
The later graph/hazard assessment must still retain witch potion capability.

| Sequential phase | Upright / crouched / vertical blocks | Removals / placements | GUI operations | Decisions | Selections | Acquisition checks |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| 1. Lower source/cover, witch clear, chest, return | 4 / 0 / 0, plus witch combat duty | 2 / 0 | 29 | 6 | 3 | 1 |
| 2. Construct connector and reach middle ladder station | 3.6 / 15.4 / 14 | 9 / 27 | 0 | 10 | 9 | 0 |
| 3. Middle clear, upper chest and return | 8 / 0 / 22, plus wither-skeleton combat duty | 0 / 0 | 29 | 5 | 2 | 1 |
| 4. Return across connector and descend | 1.6 / 15.4 / 14 | 0 / 0 | 0 | 4 | 0 | 0 |
| Total | 17.2 / 30.8 / 50 | 11 / 27 | 58 | 25 | 14 | 2 |

Phase 1 selects pickaxe, sword, then empty hand. Phase 2 selects pickaxe for
grass, scaffold, cobblestone for the first ten bridge cells, pickaxe for first
leaf/body removal, cobblestone for that replacement, pickaxe for the second leaf
floor, cobblestone for its replacement, pickaxe for walls/source, then cobblestone
for the source-floor replacement. Phase 3 selects sword then empty hand; the
source was already removed in phase 2 and is not mined or approached twice.

The first 0.6 horizontal blocks leaving scaffolding on the outbound crossing and
the final 0.6 returning to it are upright; the rest of each sixteen-block crossing
uses crouch speed. Two placement-station approach blocks, the two middle-station
exit/entry blocks, lower visit and upper visit complete the horizontal accounting.
Vertical rates are the accepted 1.5/1/0.75 blocks/s A/B/C assumptions. Decisions
are provisional allowances covering each phase's orientation, pose, source,
construction, combat and return transitions, not observed navigation performance.

There are 96 interaction allowances: eleven removals, 27 placements and two times
29 open/scan-or-shift-click/close operations. Add two acquisition confirmations
and one final verification allowance. All rolled contents must fit after equipment
and remaining materials. Any failed transfer, placement, pursuit, survival,
unsupported route, additional recovery/wait or action beyond the declared budgets
censors completion. Active mining, stationary decisions, selections, movement,
container operations and combat duty are separate costs. No extra pursuit length
or attack-switch constant is added on top of duty.

## Complete conditional timing result

Nominal breaking work uses the existing grounded diamond-pick model. Pinned
`Blocks` supplies hardness 5 for spawners, 2 for cobblestone/mossy cobblestone,
1.5 for andesite, and 0.2 for leaves; short grass is `instabreak`. The stone/source
blocks use pickaxe speed 8, leaves default speed 1. The grass removal retains its
interaction allowance but adds no sustained breaking duration. Exact targets were
listed in the access/connector sections; no additional mining is assumed.

| Removal group | Count | Nominal ticks each | Combined seconds |
| --- | ---: | ---: | ---: |
| Spawners | 2 | 19 | 1.90 |
| Cobblestone, including lower cover | 2 | 8 | 0.80 |
| Mossy cobblestone | 1 | 8 | 0.40 |
| Andesite | 2 | 6 | 0.60 |
| Oak leaves | 3 | 6 | 0.90 |
| Short grass | 1 | 0 sustained | 0 |
| Total | 11 | 92 combined | 4.60 |

Predeclare two successful ordinary witches and two successful ordinary
wither skeletons for the worked example, without extra equipment/passengers,
reinforcements, healing or damage modifiers. The two witches require 6.5 seconds
of active attack work in phase 1, the two wither skeletons 5.2 in phase 3. Divide
by the accepted combat duties and include pursuit/return in that allowance.
These populations are scenario inputs, not observed spawn counts or probabilities.

The saved sources can repeat while work proceeds. As in the preceding layouts,
bound active ticks by ceil(20*D), using elapsed time through each removal phase,
then bound successful ordinary entities by `4*(1+floor(ceil(20*D)/200))` for their
saved Delay 0. This overcounts inactive periods and time after removal within a
phase. Include the worked witch combat before the later source's phase end.
The resulting envelope is specific to this worked schedule; changing healing,
counts, pursuit or delays requires recalculation. It is not a jointly attainable
population prediction or a lifetime cap.

| Conditional result | A | B | C |
| --- | ---: | ---: | ---: |
| Noncombat components and final verification, seconds | 105.907 | 172.567 | 274.722 |
| Witch and wither-skeleton combat duty combined, seconds | 11.700 | 15.600 | 23.400 |
| Complete worked task, seconds | 117.607 | 188.167 | 298.122 |
| Witch source successful-entity envelope | 12 | 16 | 28 |
| Wither-skeleton source successful-entity envelope | 28 | 40 | 68 |

Report approximately **118/188/298 seconds** only for the stated successful
no-healing/no-debuff case. The zero-entity scenario is represented by the
noncombat row, not an empirical minimum or proof that the scenario usually
occurs. There is no observed human traversal or combat duration, realized enemy
population, rolled inventory or acquired loot. The source-supported healing and
potion hazards remain material despite their exclusion from this worked case.

Reproduce the component totals and schedule-dependent envelopes:

```sh
uv run python - <<'SMALL_TOWER_TIMING'
import math
work=[(2,5,8),(2,2,8),(1,2,8),(2,1.5,8),(3,.2,1)]
assert sum(n*math.ceil(h*30/s) for n,h,s in work)==92
# Upright, crouch, vertical, breaking seconds, decisions, interactions, selections, acquisition.
rows=[(4,0,0,1.35,6,31,3,1),(3.6,15.4,14,3.25,10,36,9,0),
      (8,0,22,0,5,29,2,1),(1.6,15.4,14,0,4,0,0,0)]
for index,expected in [(0,17.2),(1,30.8),(2,50),(3,4.6),(4,25),(5,96),(6,14),(7,2)]:
    assert math.isclose(sum(row[index] for row in rows),expected)
profiles=[('A',5,1.5,1.5,.5,.25,.25,1,2,1),
          ('B',4,1.2,1,1,.5,.5,2,4,.75),
          ('C',3,.9,.75,1.5,1,1,4,8,.5)]
for name,u,c,v,d,i,s,a,verify,duty in profiles:
    phases=[U/u+C/c+V/v+B+D*d+I*i+S*s+A*a for U,C,V,B,D,I,S,A in rows]
    witch_end=phases[0]+6.5/duty
    skeleton_end=witch_end+phases[1]
    bounds=[4*(1+math.ceil(20*t)//200) for t in (witch_end,skeleton_end)]
    baseline=sum(phases)+verify
    print(name,'noncombat',round(baseline,6),'complete',round(baseline+11.7/duty,6),
          'worked-schedule source envelopes',bounds)
SMALL_TOWER_TIMING
```

## Remaining spaces and local quality synthesis

The isolated south-facing ladder at (411,163,313) has air immediately below at
Y162 and above at Y164. It supplies no verified standing-floor connection to the
main ladder, whose surrounding shaft blocks remain solid at that height. The
west-facing pair at (410,Y169..170,312) has air below at Y168, a full wall backing
at X411, and a top spruce slab at (410,171,312). That slab occupies Y171.5..172
and blocks a straight upright continuation through the top. The upper-room
side at (411,169,312) is stone. These fragments therefore do not add verified
native room connections. This is not proof that arbitrary scaffold placement,
mining or parkour could never reach them. No source or loot-bearing entity is
assigned to an additional floor there.

The full slice overview and exact states show support mass, narrow tower shaft,
roof ornament and separate island surfaces, not a room at each height. The
following delineation uses the predeclared room/activity-space definition:

| Node | Delimitation and functional evidence | Source / chest arrangements |
| --- | --- | --- |
| L: lower ruin pocket | Broken wall/arch around X427..428,Z311..314; feet Y144; checked entry reaches the one-cell reward station at (428.5,144,312.5) | 1 witch / 1 rare chest |
| M: middle tower room | Interior X412..413,Z310..312, feet Y158, bounded by tower walls with west opening and ladder; pots occupy part of the floor | 1 wither skeleton / 0 |
| U: upper reward room | Interior X412..414,Z310..312, feet Y169, wall ring with openings and upper cap | 0 / 1 houses_rare chest |

Count **three activity rooms**, or **two tower rooms** if the exposed lower ruin
pocket is excluded by a strict covered-interior convention. Keep that sensitivity
explicit. Nearby open island terrain, the engineered scaffold column/bridge,
ornamental ladder fragments and roof surfaces are not extra delineated rooms.
The main shaft is a connection, not eleven stacked rooms. The lower pocket's
other decorative corner is not counted as another room merely because a chest
and pot constrain its floor access.

The verified native inter-room graph has only M-U, with L separate: three nodes,
one edge, two components. L's declared entry additionally needs its source and
cover removed. The engineering graph adds L-M through the scaffold/bridge/wall
strategy: three nodes, two edges, one component. Both graphs have zero verified
cycles and zero degree-three branching junctions. The completed engineering graph
is a chain; L and U are its terminal activity nodes. Unlike the Pyramid bridge,
this connector preserves the verified main ladder after construction.

After construction, entry-to-M is seventeen horizontal blocks and fourteen of
rise; the extra two outbound placement-station blocks are construction work,
not shortest-route depth in the completed graph. From M to the upper chest
station is four horizontal plus eleven ladder blocks. Thus U has graph depth two
from L and a declared connector depth of 21 horizontal plus 25 rise. These are
shortest paths within the verified connector graph, not global optima with
arbitrary flight, mining or jumping. The native M-U floor span is eleven; the
engineering objective's total feet span is 25 (Y144..169), with 25 ascent and
25 descent. The 48-layer component height is not playable depth.

Local cover also differs from that envelope. At the lower reward station's
column (428,312), all saved cells Y144..179 are air and WORLD_SURFACE is Y143:
this pocket has no overhead cover on that ray. At the middle source-interaction
column (412,310), air Y158..160 precedes a cap beginning at Y161. It contains
mixed full blocks, a wall at Y164 and a top slab at Y167 through Y168; do not
report all eight layers as eight full solid blocks. At the upper chest-interaction
column (413,310), Y169..172 are air, Y173..175 are full blocks and Y176 is a wall.
Saved WORLD_SURFACE there is Y176. That is three full cap blocks plus partial wall
geometry, not seven blocks of burial. These are authored island/tower cover
observations, not mainland underground depth.

The lower breach is one block wide with two blocks of headroom after both
removals. The main ladder has a one-cell shaft and a three-sixteenths attachment
plate, leaving 0.8125 blocks across its clear centered cross-section; the 0.6-wide
actor fits. The engineered bridge is one block wide and unrailed. These concrete
constraints support fall/exposure and bottleneck assessments, but not claims
about live enemy funneling or multiplayer traffic performance.

Meaningful encounter hazards are the witch's supported healing/ranged-potion
mechanisms and the wither skeleton's supported successful-hit effect. They remain
baseline capabilities even though the worked timing case excludes successful
healing/debuffs. Narrow elevated climbing/building creates a supported fall
exposure if the actor leaves its validated path; no fall, damage or survival
probability was measured. Grass and decorative pots are not counted as damage
hazards. No functioning TNT, redstone or dispenser trap is established from this
sample. Do not manufacture encounter diversity from those decorative blocks.

There are two explicitly assigned enemy types in two sources and no source
residents. The worked example's two of each is an input, not an observation.
Empty and dead counts are **0/3 activity rooms**, or **0/2 tower rooms**: L has
source/reward, M has source and required vertical access, U has reward. The
inaccessible or unverified ornamental fragments are outside this denominator;
they are not invented empty playable rooms.

No explicit authored terminal combat event or completion trigger was found in
the inspected source inputs. U is a terminal reward candidate, not a boss room:

| Final-room dimension | Supported disposition |
| --- | --- |
| Objective clarity | CONDITIONAL: the upper chest is a visible reward target after ascent, but no explicit completion objective is authored |
| Distinctive terminal challenge | ABSENT as an encounter: no source/resident is assigned to U; the eleven-block climb is access work |
| Reward linkage | PRESENT as potential: one houses_rare chest is assigned to U; it is not proven more valuable than L's rare chest |
| Route integration | PRESENT under the checked main-ladder model, once M is reached |
| External/bypass vulnerability | UNKNOWN for an alternative upper raid route; no flight/roof shortcut was validated |

Loot distribution is one of two arrangements in L and one in U, none in M.
The four unfilled pots supply no stored inventory in this sample. Table rolls,
item value, actual opening and acquisition remain distinct and unmeasured.

One concrete partial-objective bypass is supported: take the four-block lower
out-and-back after its source/cover removals and leave with the lower chest's
conditional transfer. That skips the middle source, upper room and all 27
connector placements. It does not claim the full all-source/all-chest objective
is complete or that the witch encounter is harmless. Conversely, no minimal-cost
external approach to U is established merely by its altitude or exposed wall
openings. The expensive connector is one valid earned-engineering option, not
proof that the pack forbids other approaches or that its material count is optimal.

Expected replay variation comes from source/table alternatives, spawn success and
surrounding generated context rather than demonstrated new core rooms: the active
rigid, empty-processor template fixes the source layout. The completed model
removes both spawners and retains scaffolding, bridge and breaches. It supplies
no self-resetting physical encounter on a revisit. Actual persistence, per-player
reward behavior and replenishment remain for their later specified audits. No
player enjoyment, replay frequency or repeat-world distribution is invented.

Flag **limited spatial progression relative to the tall fragmented silhouette**:
three small activity spaces, no verified branching/cycles and one long ladder
connection occupy much less playable content than the full template height
suggests. Vertical access and construction remain mechanically meaningful; the
structure is not called effortless. Complete conditional timing is 118/188/298
seconds for the explicit no-healing/no-debuff worked case. This local synthesis
integrates all descriptive quality dimensions, while family repetitions, material
coverage and Item 13 review/delivery gates remain open.
