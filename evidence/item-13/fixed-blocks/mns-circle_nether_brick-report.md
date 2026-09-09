# Nether Brick Circle: quality assessment

Status: local inspection assessments recorded for both cases. Complete-objective
timing is UNRESOLVED under protocol v2; prior movement results do not pass that
requirement. Item 13 coverage and delivery remain IN PROGRESS.
This is one material layout of mns:circle_ruin;
circle_blackstone remains separately required by the existing coverage record.

Sample: full-ordinary-r2-baseline|minecraft:the_nether|mns:circle_nether_brick|18|6.
[Saved blocks](mns-circle_nether_brick.json.gz), SHA-256
c5f115f0c9ecdcda67addcd30d7aae81377315ff78d169821d5ea9ba7ed46dce,
retain 8,464 voxels and 91 palette states. Envelope [280,65,88,296,74,104];
padded bounds [277,62,85,299,77,107]. The original selection, world/archive
identity and saved start are already retained there; no new generation or
extraction is needed. The [slice sheet](mns-circle_nether_brick-slices.svg)
was visually inspected. It depicts saved block categories, not collision shapes.

Reproduce with the existing renderer:

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/mns-circle_nether_brick.json.gz --output /tmp/item13-circle-slices.svg
```

## Authored layout versus saved environment

The saved start records one rigid mns:ruins/circle_nether_brick component,
rotation COUNTERCLOCKWISE_90, placement origin (280,65,104), with empty processors.
The existing Item 8 packaged pool and template records identify the same fixed
17x10x17 layout. This is a template identity, not a room count. The saved slices
show an open ruin with short walls, stairs/slabs and central spawner blocks;
external vegetation/terrain intersects the surrounding volume. Playable activity
boundaries and routes must use actual shapes, not the rectangular envelope.

Precise immutable source: MoogsNetherStructures-1.21-3.0.0-alpha.2.jar,
SHA-256 05024f18690436fff2fbc088f880a95cc30f23bacfe6e8058f6b02106032a990,
resource data/mns/structure/ruins/circle_nether_brick.nbt, SHA-256
24c67d0c292ede402ff9f706d465dad6b82b59bbf66698477f44d6b5aea69234.
The existing [template catalog](../../item-8/sources/templates-redacted.json.gz)
retains palette, counts and block entities. Direct NBT inspection with the
existing decode_compound_nbt on the decompressed resource supplies coordinates.
For this saved rotation/origin, local(u,v,w) maps to(280+w,65+v,104-u).

Two authored ancient-debris positions, local(5,1,3) and(11,1,9), map exactly
to saved (283,66,99) and(289,66,93). Both remain ancient debris in the raw
world. They are embedded material reward opportunities, despite there being
no chest/barrel nodes. Do not score the ruin as reward-free from container count.
The source-defined soul fire at local(8,4,7), world(287,69,96), is saved AIR.
It is not an active saved hazard; its absence is preserved without inventing a
cause or restoring the intended fire.

The source template has no lava palette entry. The saved envelope contains
five lava blocks at (284,Y70..74,95), all level0. Padding extends that same
column to a sixth source-level lava block at Y75, with magma at Y76 and air
at Y77. No magma block is inside the original envelope. These are saved
surroundings/overlap facts, not evidence of an authored lava trap or an observed
flow sequence. Required or optional route exposure to this column still needs
geometric assessment. Source level0 does not demonstrate a player encounter.

## Encounter and reward evidence

Two saved ordinary spawners remain: piglin at (287,67,96) and piglin brute at
(288,67,97). Each has SpawnCount4, SpawnRange4, MaxNearbyEntities6,
RequiredPlayerRange16, MinSpawnDelay200, MaxSpawnDelay800, Delay 0 and empty
SpawnPotentials. These are two authored enemy types and potential attempt
counts, not two realized encounters or eight guaranteed enemies. Unlike the
houses' missing assignments, both IDs are explicit.

The [predeclared mixed workload](../model-source/README.md#nether-brick-circle-mixed-ordinary-spawner-model)
uses successful counts p,b independently 0..4, ordinary unarmored target health
16/50, and the existing iron-sword profile. Full-contact seconds=1.95*p+5.85*b;
50%-duty seconds=3.9*p+11.7*b. Conditional ranges are 0..31.2 and 0..62.4 for
this one-wave composition grid only. Repeated waves, actual gear and natural
mobs are excluded; human combat and realized encounters remain NOT MEASURED.

The two saved ancient-debris blocks are not generated chest loot or acquired
items. The existing iron-pick actor must not be credited with harvesting them:
the packaged needs_diamond_tool/incorrect_for_iron_tool tags explicitly impose
that capability distinction. A later extraction model must state a supported
harvesting tool and access/mining conditions. No rare engineering capability is
being gated or rebalanced here; this is baseline evidence only. The two blocks'
room/depth distribution awaits validated topology.

All 289 WORLD_SURFACE columns are Y127. The existing height-difference metric
is 127-74=53 blocks above envelope top, not 53 solid blocks of cover to mine.
The open ruin's local overhead exposure must be interpreted separately from
the Nether upper-surface heightmap.

## Concrete remaining work

Validate the open activity-space boundary, supported entry and full route,
partial-block clearances, lava exposure, reward interaction/extraction access
and any internal connections. Then integrate room/branch/depth denominators,
traversal, dead/empty spaces, finale, bypass and replay assessments. Preserve
saved environmental hazards and the missing source fire rather than rebuilding
the intended layout. Reuse the existing fixed-layout blocks and collision tools;
do not repeat inventory/classification, source collection or world generation.
Item 14 remains UNSTARTED.


## Established fortress overlap and supplemental sample

The existing [ordinary-r2 saved-start record](../start-inspection/full-ordinary-r2-baseline.json.gz)
contains betterfortresses:fortress at chunk(19,8), envelope[188,6,17,370,112,240].
Three individual saved pieces intersect this Circle envelope, so the finding
is not based only on the fortress's overall bounding box:

| Fortress template | Saved bounds |
| --- | --- |
| bridge/bridge_end | [282,70,104,286,80,107] |
| bridge/blaze_stairs | [281,69,99,287,78,103] |
| blaze/blaze_0 | [280,69,91,288,84,98] |

More strongly, immutable template data/betterfortresses/structure/blaze/blaze_0.nbt
in YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar, resource SHA-256
e55231fa73c8d12f875936e97636d7aea99632cae0fbe5f5bd5203c388f0136c,
has source-level lava at local(3,Y1..6,4) and magma at(3,7,4). Its saved
COUNTERCLOCKWISE_90 origin(280,69,98) maps these exactly to the six saved
lava blocks (284,Y70..75,95) and magma cap(284,76,95). This supports fortress
attribution for that column. It does not establish generation order or assign
every surrounding brick to a particular processor. The earlier source-vs-saved
hazard distinction now has a concrete neighboring structure explanation.

The original selected sample remains a real mixed baseline case. Its neighboring
fortress must not be counted as Circle rooms or the Circle's authored lava trap.
To separate fixed-layout quality from this overlap, one additional retained-world
sample is required. This is a demonstrated attribution problem, not a reason to
replace an unfavorable sample or perform another generation survey.

The existing candidate index has six Circle starts. Both ordinary r1/r2 starts
intersect the recorded fortress envelope; both mountainous r1/r2 and both
biome-diverse r1/r2 starts have no other recorded structure-envelope intersection.
All six already have complete saved chunks in the assembly records. Filter only
on those recorded overlap/full-chunk criteria, then use the original SHA-256
candidate-ID ordering. The first of four eligible alternatives is
full-mountainous-r1-baseline|minecraft:the_nether|mns:circle_nether_brick|23|5.
Absence of an intersecting envelope is not proof against all terrain interference;
the supplemental blocks still require inspection.

The [supplement selection](../circle-supplement-selection.json) reuses the existing
fixed-selection format and input hashes. It adds one 8464-voxel extraction, not
new worlds. Reuse measure.py with a selection-path argument rather than duplicate
its extractor. Hash-verify the complete accepted restore before/after under the
existing POSIX world lock. Budget: 300 seconds, 10 MiB output and 1.5 GiB peak RSS,
with at least 5 GiB free space; comparable first-house extraction took 6.336 seconds.
Preserve failures and both samples. Planned command (new output):

```sh
uv run python -m evidence.item-13.measure --fixed-root mns:circle_nether_brick --selection evidence/item-13/circle-supplement-selection.json --output evidence/item-13/fixed-blocks/mns-circle-supplement.json.gz
```


Supplement result: [mns-circle-supplement.json.gz](mns-circle-supplement.json.gz)
retains 8464 voxels and 53 palette states under the declared candidate/selection.
The [execution record](mns-circle-supplement-execution.txt) reports 6.644 seconds,
46,184 KiB peak RSS and 4257 compressed bytes, all within budget. SHA-256
3310bbc00d4e28a8d924168ca96e236628f0b581590227ac90cd1f36fc4b8f45.
Complete accepted-world inventories passed before/after the read under the
existing POSIX lock; full chunks/sections and original saved start were verified.
Selection and producer hashes match the current committed inputs. No server
was started and no source world changed. The supplemental palette includes lava
and soul fire, so absence of another recorded structure intersection must not
be misrepresented as hazard-free terrain. Exact positions/topology remain to
be inspected. The original mixed case and all earlier source findings remain.


## Supplemental saved hazards and bounded southern approach

The [supplemental slice sheet](mns-circle-supplement-slices.svg) was visually
inspected and reproduces with the existing renderer using the supplemental input.
The saved start has no rotation, origin(360,32,72), so source coordinates map
by direct addition. The two ancient-debris blocks are at (365,33,75) and
(371,33,81); the source soul fire is actually present here at (368,36,79).
Its presence in this sample does not repair its absence in the original case.
The piglin/brute spawners are respectively (368,34,79) and (367,34,80).

There are nine magma blocks inside the envelope, all at floor Y32:
X370..372,Z78; X369..372,Z79; and X371..372,Z80. No lava lies inside the
original supplemental envelope; its presence in the wider raw palette comes
from padding. Do not infer an interior lava obstacle from palette membership.
These floor blocks are a real optional contact-hazard region. Mapped MagmaBlock
stepOn offsets 0..29 calls hotFloor damage for a living entity that is not
stepping carefully; runtime immunity, modifiers and actual damage were not tested.
BaseFireBlock.entityInside supplies fire-contact behavior for the saved soul
fire. It does not demonstrate an enemy/player encounter merely by existing.

For a bounded geometry check, declare one upright 0.6-wide, 1.8-high actor with
existing iron equipment, full knowledge, no block changes, jumping or flight.
Use feet (368.5,33,85.5) as a local southern approach station, walk straight to
(368.5,33,81.5), inspect the two spawner targets, and return. This is a local
approach circuit, not an authored entrance, complete loot route or whole-ruin
clear. Use the existing flat rates 3/4/5 blocks per second. Interaction, combat,
external approach, mining and acquisition are excluded. Source assumptions are
explicit; no new actor or runtime observation is invented.

Direct retained-block inspection proves support/clearance for all five corridor
cells X368,Z81..85: Y32 is full crimson nylium, and Y33/34 are air in every
cell. The complete continuous actor sweep stays inside those air cells, with
0.2-block horizontal margins and its top below Y35. NyliumBlock extends Block
without a shape/collision override; Blocks initializer 32374..32414 constructs
crimson nylium with ordinary collidable Properties. The mapped base shape rules
already inspected give a full support cube and empty air collision. Neighboring
wall/fence shapes stay in their originating horizontal cell; none enters this
corridor. This directly supports this simple route without inventing partial
block geometry or rerunning a whole saved-view collision experiment.

The closed path is 8 blocks, with zero ascent/descent and zero feet-height span.
Nominal modeled travel is 8/4=2 seconds; the stipulated faster/slower values are
8/5=1.6 and 8/3=2.666667 seconds. These are conditional kinematic budgets for
this short approach only, not observed traversal times or a scored whole dungeon.
The corridor never steps on the nine magma blocks. Its actor top Y34.8 remains
below the soul-fire cell Y36; no contact with that saved block occurs on this
static route. Neither fact establishes safety from spawned enemies or later
world changes.

At its inner station, eye(368.5,34.62,81.5) is 1.419296 blocks from the brute
spawner center(367.5,34.5,80.5) and 2.003597 from the piglin spawner center
(368.5,34.5,79.5), within the declared three-block reach. Both target lines
cross only Y34 air cells before their target. The wall below at (368,33,80)
cannot obstruct them: even its conservative collision maximum is Y34.5, while
the rays stay above 34.5 until reaching their target centers. WallBlock constructor
112..128 uses height 24/16 for its collision shapes; its selection shape is no
taller. Thus both spawners have supported geometric inspection access here.
This is not an observed interaction, spawning trial, mining or encounter clear.

Reproduce the small corridor fact check directly, using the already retained
extractor indexing helper (no new processor or schema):

```sh
uv run python - <<'CHECK'
import gzip, importlib, json
from pathlib import Path
source = Path('evidence/item-13/fixed-blocks/mns-circle-supplement.json.gz')
case = json.loads(gzip.decompress(source.read_bytes()))['cases'][0]
state_at = importlib.import_module('evidence.item-13.render_pilot').state_at
for z in range(81, 86):
    assert state_at(case, 368, 32, z)['Name'] == 'minecraft:crimson_nylium'
    for y in (33, 34):
        assert state_at(case, 368, y, z)['Name'] == 'minecraft:air'
CHECK
```

The pinned javap procedure in the existing model-source notes reproduces the
NyliumBlock, Blocks, WallBlock, MagmaBlock and BaseFireBlock source derivations.
Reward access/mining capability, activity-space boundary and complete sample
quality scoring remain pending; the corridor must not substitute for those.

## Supplemental reward-face access model

Predeclare two local access checks using the same known-layout actor and saved
blocks. These are geometric/source models, not new world experiments. Retain
the original raw states. No enemies, dynamic updates or interaction latency
are modeled. Stop a check at any unsupported support, collision or sight line;
do not count that target as accessible. Acquisition and mining duration remain
NOT MEASURED, and the iron-pick profile cannot harvest ancient debris.

Northern target: from feet(367.5,33,75.5), upright eye height 1.62, first aim at
(366.09375,33.75,75.5) to toggle the east crimson trapdoor at(366,33,75) from
open=true to false. Then aim at debris center(365.5,33.5,75.5). Only that
trapdoor state changes in the model. The closed lid above the debris remains.
This check is conditional on reaching the station; it is not a route claim.

Southern target: extend the existing southern approach from(368.5,33,81.5)
to(369.3,33,81.5), then crouch with eye height 1.27. Aim along the line to
(371.5,33.1,81.5), initially contacting the west nether-gold-ore cover at
(370,33,81). Model removal of that one cover block, then use the same line
to inspect the ancient-debris face. Leave the bottom slab above the cover,
the surrounding ore and roots unchanged. This declares one cover removal,
not a minimum-cost proof over every possible access direction. Walking rates
remain 3/4/5 blocks per second; crouching, interaction and mining time are
excluded from the movement-only budget.

Result: both local face-access checks pass under those declared changes. The
northern station has full nylium support and air in Y33/34. Its open east panel
occupies X366..366.1875, Y33..34, Z75..76; the first ray contacts its east face
at Y33.808. Folding that panel gives a bottom plate only Y33..33.1875. The
second ray reaches the debris east face at X366,Y33.78, above the folded panel
and below the unchanged lid at Y34..34.1875. Its target-center distance is
2.292248 blocks, within the declared three-block reach. No mining is required
to expose this face. This local check alone does not credit access to the
northern station; the subsequent connecting-circuit section resolves it.

The southern extension crosses only the existing air cell and a crimson-roots
cell with air above, both supported by full nylium. Crimson roots have no
collision (mapped Blocks initializer 32712); they do not require removal for
this actor sweep. The crouched ray enters the cover cell at X370,Y33.897727,
below the slab's bottom Y34. After the declared cover removal it enters the
debris cell at X371,Y33.365909. Even allowing a conservative 0.25-block XZ
plant offset, the ray stays above the roots' 13/16 selection height until
beyond their possible extent. Its endpoint distance is 2.491766 blocks.
The complete southern approach plus extension and return is 9.6 horizontal
blocks, zero vertical travel: movement-only nominal 2.4 seconds, faster 1.92,
slower 3.2. This excludes the explicitly declared pose change and cover removal,
so it is not an entry-to-reward completion time.

Source derivation uses the same pinned mapped Minecraft JAR and javap procedure
as the existing model-source notes. TrapDoorBlock.getShape selects EAST_OPEN_AABB
for an open east-facing state; its static initializer 35..50 builds local
[0,0,0,3/16,1,1]. The bottom closed shape is [0,0,0,1,3/16,1].
useWithoutItem offsets 0..20 checks canOpenByHand and calls toggle, whose
offsets 0..17 cycle OPEN and set the changed state. Blocks initializer 33138
binds the crimson trapdoor to BlockSetType.CRIMSON; that type's initializer
427..463 sets canOpenByHand=true. This supports the conditional toggle rather
than inventing an unlocked opening. RootsBlock static initializer 11..30
defines its selection box [2/16,0,2/16,14/16,13/16,14/16]. The already captured
Player initializer 136..149 supplies crouching height 1.5 and eye height 1.27.
No source inference here proves a live modded interaction or mining outcome.

Reproduce the retained-state and ray arithmetic checks:

```sh
uv run python - <<'REWARD_CHECK'
import gzip, hashlib, importlib, json, math
from pathlib import Path
raw = Path('evidence/item-13/fixed-blocks/mns-circle-supplement.json.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest() == '3310bbc00d4e28a8d924168ca96e236628f0b581590227ac90cd1f36fc4b8f45'
case = json.loads(gzip.decompress(raw))['cases'][0]
state = importlib.import_module('evidence.item-13.render_pilot').state_at
for x, z in [(367,75), (368,81), (369,81)]:
    assert state(case,x,32,z)['Name'] == 'minecraft:crimson_nylium'
    assert state(case,x,34,z)['Name'] == 'minecraft:air'
assert state(case,367,33,75)['Name'] == 'minecraft:air'
assert state(case,368,33,81)['Name'] == 'minecraft:air'
assert state(case,369,33,81)['Name'] == 'minecraft:crimson_roots'
panel = state(case,366,33,75)
assert panel['Name'] == 'minecraft:crimson_trapdoor'
assert panel['Properties'] == dict(facing='east',half='bottom',open='true',powered='false',waterlogged='false')
assert state(case,366,34,75)['Name'] == 'minecraft:air'
lid = state(case,365,34,75)
assert lid['Name'] == 'minecraft:crimson_trapdoor'
assert lid['Properties']['open'] == 'false' and lid['Properties']['half'] == 'bottom'
assert state(case,370,33,81)['Name'] == 'minecraft:nether_gold_ore'
slab = state(case,370,34,81)
assert slab['Name'] == 'minecraft:nether_brick_slab' and slab['Properties']['type'] == 'bottom'
for p in [(365,33,75), (371,33,81)]:
    assert state(case,*p)['Name'] == 'minecraft:ancient_debris'
north_eye, north_aim = (367.5,34.62,75.5), (365.5,33.5,75.5)
south_eye, south_aim = (369.3,34.27,81.5), (371.5,33.1,81.5)
panel_aim = (366.09375,33.75,75.5)
def ray_y(eye, aim, x):
    return eye[1] + (aim[1]-eye[1])*(x-eye[0])/(aim[0]-eye[0])
assert 33 < ray_y(north_eye,panel_aim,366.1875) < 34
assert 33.1875 < ray_y(north_eye,north_aim,366) < 34
assert 33 < ray_y(south_eye,south_aim,370) < 34
assert ray_y(south_eye,south_aim,370.125) > 33.8125
assert 33 < ray_y(south_eye,south_aim,371) < 34
for eye, aim in [(north_eye,panel_aim), (north_eye,north_aim), (south_eye,south_aim)]:
    assert math.dist(eye,aim) < 3
print('north panel contact Y', ray_y(north_eye,panel_aim,366.1875))
print('north debris aim distance', math.dist(north_eye,north_aim))
print('south cover/debris face Y', ray_y(south_eye,south_aim,370), ray_y(south_eye,south_aim,371))
print('south debris aim distance', math.dist(south_eye,south_aim))
print('movement-only seconds at 3/4/5 blocks per second', [9.6/v for v in (3,4,5)])
REWARD_CHECK
```

## Predeclared connection to the northern reward station

Resolve the outstanding northern-station connection with one explicit circuit,
using the same local southern start and reward-face objective. Outbound feet
waypoints are (368.5,33,85.5), (368.5,33,81.5), (369.5,33,81.5),
(369.5,33,80.5), (369.5,33,78.5), (369.5,33,75.5), (367.5,33,75.5).
Return on the same line. Pause at the already checked southern reward station
(369.3,33,81.5), which lies on that route, and at the inner southern station
for the spawner inspection. Keep the reward-face model's two declared changes.

Hold shift and use the crouching pose across the entire segment between
Z80.5 and Z78.5 in both directions, so the complete body crosses the magma
cell at(369,32,79) while stepping carefully. Use the prior house model's
upright 3/4/5 and crouched 0.9/1.2/1.5 blocks per second, without interaction,
mining, combat or pose-transition latency. All other segments are upright.
No jump, bridging, cover removal for movement or flight is permitted. Failure
of support/clearance or the source hazard-avoidance condition censors this
connection rather than silently substituting another route. This is a static
inspection circuit, not a survival or enemy-navigation experiment.

The initial draft incorrectly attributed crouched rates 1/1.3/2 to the house
model. Source inspection of house_route.py's profiles corrected that attribution
before accepting this circuit's timing. The provisional 11.333333/8.576923/6.4
second calculation is rejected; use the corrected calculation below.

Result: the circuit has complete continuous flat support and body clearance.
All traversed feet cells have air at Y33/34 except the already supported
noncolliding roots at(369,33,81). Floors are full nylium except quartz ore at
(369,32,80) and magma at(369,32,79). Mapped DropExperienceBlock and MagmaBlock
extend Block without shape overrides, and their Blocks registrations use
ordinary collidable properties (quartz offsets 16395..16434, magma through
25109). Thus the sweep requires no invented partial-block shapes. Its body
stays within the inspected cell strips, including each corner's shared cell.
All feet stay at Y33; ascent, descent and feet-height span are zero.

Mapped Entity.isSteppingCarefully offsets 0..4 returns isShiftKeyDown. Combined
with MagmaBlock.stepOn, this supports a specific conditional way to avoid the
floor-contact damage call throughout the magma crossing. The shift segment
begins/ends 0.5 blocks outside the magma cell, exceeding the actor half-width
0.3. This is a meaningful route hazard with an explicit avoidance condition,
not an observed safe crossing. Spawned enemies, loss of shift and displacement
can invalidate the condition and are not modeled. The saved soul fire at Y36
is above this route's maximum body top Y34.8.

The closed circuit is 26 blocks: 22 upright and four crouched. Movement-only
seconds are 22/4+4/1.2=8.833333 nominal, 22/5+4/1.5=7.066667 faster,
and 22/3+4/0.9=11.777778 slower. The north station is 13 route blocks from
the declared local start, while the south reward station is 4.8. These are
depths on this validated route, not proven global shortest paths. The circuit
connects both debris-face inspections and the two spawner targets. It does not
measure harvesting, combat, whole-arena room boundaries or all alternate routes.

Extend the preceding REWARD_CHECK after its existing assertions to reproduce
the complete route-strip support and timing calculation:

```python
route_cells = ({(368,z) for z in range(81,86)}
               | {(369,z) for z in range(75,82)}
               | {(x,75) for x in range(367,370)})
for x,z in route_cells:
    floor = ('minecraft:magma_block' if (x,z)==(369,79) else
             'minecraft:nether_quartz_ore' if (x,z)==(369,80) else
             'minecraft:crimson_nylium')
    assert state(case,x,32,z)['Name'] == floor
    assert state(case,x,34,z)['Name'] == 'minecraft:air'
    assert state(case,x,33,z)['Name'] == (
        'minecraft:crimson_roots' if (x,z)==(369,81) else 'minecraft:air')
waypoints = [(368.5,85.5),(368.5,81.5),(369.5,81.5),
             (369.5,80.5),(369.5,78.5),(369.5,75.5),(367.5,75.5)]
outbound = sum(math.dist(a,b) for a,b in zip(waypoints,waypoints[1:]))
assert outbound == 13 and 2*outbound-4 == 22
print('corrected nominal/faster/slower seconds',
      [22/u+4/c for u,c in [(4,1.2),(5,1.5),(3,0.9)]])
```

## Northern external approach and quality synthesis

Predeclare one alternative approach: upright feet(369.5,33,71.5), outside
the recorded envelope's northern boundary Z72, straight south to(369.5,33,75.5),
then west to the existing northern reward station(367.5,33,75.5), and return.
Use the same 0.6-wide, 1.8-high actor, known layout and 3/4/5 flat movement
rates. Permit only the already declared northern trapdoor toggle. No mining,
jumping, flight or assumed enemy suppression supports this route. A missing
floor or unsupported body obstruction fails this proposed connection. The
external approach before the declared station remains outside the measurement.

Retained-state inspection validates this connection: X369,Z71..75 has full
nylium at Y32 and air at Y34. Feet Y33 are air except crimson fungus at Z71
and roots at Z73. Blocks initializer 32436..32460 registers crimson fungus
with noCollission; roots use the source rule already established above.
The western segment uses the already checked X367..369,Z75 air strip.
The continuous sweep stays inside these supported strips, so no plant removal
is needed. The six-block outward path and return total 12 horizontal blocks,
zero vertical change, with movement-only nominal 3 seconds (2.4 faster,
4 slower). Northern reward access still requires its trapdoor toggle and a
different harvesting capability to acquire debris; neither receives a timing
or acquired-loot credit.

This is a supported bypass of the southern approach and its magma crossing,
not proof of avoiding enemies. The external starting station is approximately
8.20 blocks from the piglin spawner and 9.34 from the brute spawner, already
inside both saved RequiredPlayerRange16 distances. The route avoids traversing
their central pedestal but cannot be called an activation bypass or safe loot.
It demonstrates that one material reward has local external access without
progressing through the central hazard region. No arbitrary route protection
or dungeon tuning is proposed.

The supplemental sample supports the following assessment under the declared
room definition. Delineate one outdoor ruin activity area within the broken
perimeter at X360..376,Z72..88, with the validated interior circuit at feet Y33.
The rectangle records the outer limits of the curved fragmented perimeter,
not 289 proven playable cells. Solid pillars, vegetation, reward casings and
the spawner pedestal are obstacles, not additional rooms. The mapped source
positions at local Y1/2 show separated perimeter fragments and a central
pedestal without intervening authored room walls; the saved slices and complete
reward circuit establish a connected activity space. Natural trees obstruct
parts of it, and unvisited pockets are not counted as separate rooms.

| Requirement | Supported assessment and denominator |
| --- | --- |
| Rooms | One outdoor activity area, zero enclosed rooms. Under a strict enclosed-room-only sensitivity, zero rooms and one outdoor encounter site; do not discard that site as empty evidence. |
| Branching/depth | One room-graph node, zero inter-room edges, zero degree-three room junctions and zero room-graph cycles. Entry and both reward objectives occupy the same node, graph depth zero. These do not count free walking alternatives as corridor branches. |
| Route depth | Validated southern-start routes place reward stations at 4.8 and 13 blocks. The northern external alternative reaches its reward station in six blocks. These are route-specific upper bounds on shortest walking depth, not an exhaustive shortest-path result. |
| Vertical progression | The complete two-reward inspection circuit has zero ascent/descent and feet-height span. Higher pillar/pedestal blocks do not constitute validated upper rooms or progression. No distinct authored upper objective is identified in this layout. |
| Dead/empty rooms | Zero empty and zero dead over the one outdoor area: it has two reward materials, two enemy-source types and a meaningful floor hazard. Enclosed-room sensitivity has a zero denominator, so its empty/dead fraction is not defined. |
| Reward distribution | Both debris nodes are in the same activity area, with distinct local casings and access costs. Zero chest/barrel nodes, two embedded material opportunities; acquired items remain NOT MEASURED. No separate final-room concentration exists. |
| Chokepoints | No inter-room chokepoint in this one-area graph. The validated routes fit a 0.6-wide actor without a doorway transition. Plant/terrain obstacles and reward casing apertures remain local constraints, not evidence of a defended corridor or enemy funnel. |
| Final room | NONE. No separate terminal room, ordered prerequisite chain or distinct final encounter is supported by the fixed template and saved reward/spawner layout. The northern approach weakens any inferred mandatory progression to that reward. |
| Finale quality dimensions | Terminal objective clarity, distinctive terminal challenge, terminal reward linkage and ordered route integration are ABSENT as authored finale features. External exposure is PRESENT for the northern reward by the validated alternative, but there is no final room to assign that exposure to. |
| Expected replay value | Low expected authored-layout variation for this fixed root, with two differently covered resource nodes and the same two spawner types. Saved terrain/overlap and the original-versus-supplement fire difference support environmental variation. Actual encounter outcomes, enjoyment and player revisits remain NOT MEASURED. |
| Persistent revisit | Embedded debris is a finite placed resource in this source layout. No regenerating reward mechanism is identified here. Spawner parameters allow repeated attempts; they do not restore mined blocks or establish replay satisfaction. Other runtime regeneration mechanisms are not measured. |
| Visually large but shallow | Mechanically shallow as a single outdoor resource/encounter site with no validated vertical objective sequence. The fragmentary 17-by-17 ruin is not a demonstrated large-building exemplar; do not promote envelope size or ten-block authored height into a claim of dungeon depth or perceived grandeur. |

These conclusions apply to the supplemental fixed-root layout and preserve
the original fortress-overlap case separately. They do not resolve the original
case's complete playable topology, the blackstone material root, every alternate
path or whole-population replay value. The source-supported mixed combat model
above remains the combat assessment; the geometric circuit supplies no realized
enemy count, human traversal/combat time or acquired loot.

Reproduce the added route facts after REWARD_CHECK:

```python
for z in range(71,76):
    assert state(case,369,32,z)['Name'] == 'minecraft:crimson_nylium'
    assert state(case,369,34,z)['Name'] == 'minecraft:air'
    expected = {71:'crimson_fungus',73:'crimson_roots'}.get(z,'air')
    assert state(case,369,33,z)['Name'] == 'minecraft:'+expected
start = (369.5,33,71.5)
print('external start to spawner-center distances',
      [math.dist(start,p) for p in [(368.5,34.5,79.5),(367.5,34.5,80.5)]])
print('north circuit nominal/faster/slower seconds', [12/v for v in (4,5,3)])
```

## Original mixed case: rejected transfer and western access

The supplemental circuit is not valid evidence of original-case connectivity.
Rotate its local coordinates through the original placement transform: the
X369,Z75..78 supplemental strip becomes original X283..286,Z95. Every one
of those four original cells contains full nether bricks at Y66 and Y67,
where the proposed actor would stand. The transformed reward station at
(283.5,66,97.5) is also solid at both body levels. This rejects that route
transfer, not the retained sample. The original source-defined trapdoor cache
at(283,66,99) survives, but its western cover at(282,66,99) now has a full
nether-brick block above, unlike the supplemental open side. Do not infer
generation order or attribute every obstructing brick from this comparison.

Predeclare a smaller original-case alternative, using the same actor, reach
and source-shape rules: upright feet(279.5,66,99.5), outside the envelope's
western boundary X280, walk to(281.3,66,99.5), then crouch. From eye
(281.3,67.27,99.5), aim toward(283.5,66.1,99.5). Toggle the saved west-facing
open crimson trapdoor at(282,66,99) closed, then inspect the debris on the
same line. Return to the start. Only that toggle is permitted; no cover
mining, jumping or flight. This is one reward-face objective, not both rewards
or a dungeon clear. Reject any obstructed ray or unsupported route cell;
interaction, pose-transition, combat, mining and acquired loot remain unmeasured.

This local alternative passes the retained-block/source checks. X279..281,Z99
has full warped nylium at Y65 and air at Y66/67; the upright continuous sweep
therefore has support and clearance. Warped and crimson nylium use the same
NyliumBlock shape behavior. The west-facing open panel occupies local
X13/16..1 across its cell, while its closed bottom plate ends at Y66.1875.
The crouched ray enters the cover cell at X282,Y66.897727, below the full
brick above at Y67. Its first panel contact is at X282.8125,Y66.465625.
After the toggle, the same ray reaches the debris west face at X283,Y66.365909,
above the folded plate. The target-point distance is 2.491766 blocks, below
the stipulated three-block reach. The untouched lid above the debris is also
above this line. No cover block must be mined for this local face access.

The closed walking route is 3.6 horizontal blocks with zero vertical travel:
0.9 movement-only seconds nominal, 0.72 faster, 1.2 slower. This validates
an external alternative to the blocked transferred station, not a connection
to the other reward. Both saved spawners remain within 16 blocks of this
western start, so it is not an enemy-activation bypass. The fortress-attributed
lava column at X284,Z95 does not intersect this local sweep; effects of future
flow, spawning or other world changes are outside this static model. Original
whole-sample topology remains unresolved rather than inherited from the supplement.

Reproduce the original saved facts and arithmetic independently:

```sh
uv run python - <<'ORIGINAL_CHECK'
import gzip, hashlib, importlib, json, math
from pathlib import Path
raw = Path('evidence/item-13/fixed-blocks/mns-circle_nether_brick.json.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'c5f115f0c9ecdcda67addcd30d7aae81377315ff78d169821d5ea9ba7ed46dce'
case = json.loads(gzip.decompress(raw))['cases'][0]
state = importlib.import_module('evidence.item-13.render_pilot').state_at
for x,z in [(x,95) for x in range(283,287)]+[(283,97)]:
    for y in (66,67):
        assert state(case,x,y,z)['Name'] == 'minecraft:nether_bricks'
for x in range(279,282):
    assert state(case,x,65,99)['Name'] == 'minecraft:warped_nylium'
    for y in (66,67):
        assert state(case,x,y,99)['Name'] == 'minecraft:air'
panel = state(case,282,66,99)
assert panel['Name'] == 'minecraft:crimson_trapdoor'
assert panel['Properties'] == dict(facing='west',half='bottom',open='true',powered='false',waterlogged='false')
assert state(case,282,67,99)['Name'] == 'minecraft:nether_bricks'
assert state(case,283,66,99)['Name'] == 'minecraft:ancient_debris'
eye, aim = (281.3,67.27,99.5), (283.5,66.1,99.5)
ys = [eye[1]+(aim[1]-eye[1])*(x-eye[0])/(aim[0]-eye[0])
      for x in (282,282.8125,283)]
assert 66 < ys[0] < 67 and 66.1875 < ys[2] < ys[1] < 67
assert math.dist(eye,aim) < 3
assert all(math.dist((279.5,66,99.5),p) < 16
           for p in [(287.5,67.5,96.5),(288.5,67.5,97.5)])
print('cover/panel/debris ray Y', ys)
print('target-point distance', math.dist(eye,aim))
print('nominal/faster/slower movement seconds', [3.6/v for v in (4,5,3)])
ORIGINAL_CHECK
```

## Predeclared original-case connection search

Before assuming the obstruction requires breaching, reuse analyze_pilot.paths
to search a conservative flat subset of the existing padded block dataset.
Actor feet remain Y66, upright width 0.6 and height 1.8. Admit only full warped
nylium at Y65 with air, warped roots or nether sprouts at both body levels.
The latter two have explicit noCollission registrations in mapped Blocks
at offsets 32177 and 32229 respectively.
All other states are excluded, including partial blocks and magma. Search
cardinal cell centers within the retained X/Z bounds, from(281,66,99) to
(289,66,95), with the existing deterministic neighbor order. No block changes,
flight, jumps or terrain beyond the dataset are allowed. A missing path means
this conservative subset failed, not proof that the real world is disconnected.
Any returned path must have its complete cells retained and source-supported;
its shortest length applies only to this declared subset. Budget: one second
of CPU-scale processing and no new world/runtime/storage capture. Use existing
walking rates only after a connection is found; interaction and combat remain
excluded. This is new local topology processing, not repeated exploration or
discoverability measurement.

Result: 327 cells meet that predicate; 313 are reachable from the start and
the destination is among them. The deterministic path is 28 horizontal blocks,
with compressed X/Z waypoints (281,99), (278,99), (278,91), (279,91),
(279,90), (284,90), (284,92), (287,92), (287,95), (289,95).
Add 0.5 to both coordinates for feet-center positions; Y remains 66.
Each straight segment's intervening cells belongs to the admitted set, so
the 0.6-wide body's continuous sweep fits, including the corner cells. The
path avoids the saved lava column rather than assuming that every route must
cross it. It leaves the Circle envelope locally to skirt the saved obstruction;
that excursion is not an additional Circle room or an authored corridor.
The return makes 56 blocks: nominal 14 seconds, faster 11.2, slower 18.666667,
all movement-only. Fourteen other admitted cells outside the start component
are not fourteen rooms, and excluded partial-block cells are not proven walls.

Second reward-face predeclaration: from the path endpoint(289.5,66,95.5),
move 0.2 blocks to(289.5,66,95.7), crouch with eye height 1.27, and aim at
(289.5,66.1,93.5). Remove only the nether-gold-ore cover at(289,66,94)
in the model, leaving the bottom slab above and all other ore unchanged.
The same line then inspects the debris at(289,66,93). Use the established
source-supported iron-pick cover-removal capability without claiming debris
harvesting or mining time. This is a local geometric access model, not a
new runtime experiment. An obstructed line fails the check.

Result: the local check passes. The endpoint/shifted station has air at both
body levels over full warped nylium. The ray enters the cover at Z95,
Y66.897727, below the slab at Y67; after cover removal it reaches the debris
face at Z94,Y66.365909. Target-point distance 2.491766 is within the stipulated
three-block reach. Thus both original reward faces have access models linked
by the validated detour, despite the rejected rotated circuit. With the 0.2
station adjustment at each end (west X281.3 rather than 281.5; east Z95.7
rather than 95.5), the reward-station connection is 28.4 blocks one way.
Adding the 1.8-block western external approach and returning along the same
route gives 60.4 horizontal blocks, zero vertical travel: movement-only
15.1 seconds nominal, 12.08 faster, 20.133333 slower. Pose changes, one toggle,
one cover removal, combat and acquisition remain excluded rather than silently
treated as instantaneous gameplay. This resolves a two-reward inspection route,
not every reachable pocket or the adjoining fortress's playable topology.

Reproduce with the existing path implementation and retained original input:

```sh
PYTHONPATH=evidence/item-13 uv run python - <<'CONNECTION_CHECK'
import gzip, hashlib, json, math
from pathlib import Path
from analyze_pilot import paths, state_at
raw = Path('evidence/item-13/fixed-blocks/mns-circle_nether_brick.json.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'c5f115f0c9ecdcda67addcd30d7aae81377315ff78d169821d5ea9ba7ed46dce'
case = json.loads(gzip.decompress(raw))['cases'][0]
b = case['bounds']
clear = {'minecraft:air','minecraft:warped_roots','minecraft:nether_sprouts'}
cells = {(x,66,z) for x in range(b[0],b[3]+1) for z in range(b[2],b[5]+1)
         if state_at(case,x,65,z)['Name']=='minecraft:warped_nylium'
         and all(state_at(case,x,y,z)['Name'] in clear for y in (66,67))}
found = paths(cells,(281,66,99))
route = found[(289,66,95)]
assert len(cells)==327 and len(found)==313 and len(route)-1==28
assert state_at(case,289,66,95)['Name']=='minecraft:air'
assert state_at(case,289,67,95)['Name']=='minecraft:air'
assert state_at(case,289,66,94)['Name']=='minecraft:nether_gold_ore'
slab = state_at(case,289,67,94)
assert slab['Name']=='minecraft:nether_brick_slab' and slab['Properties']['type']=='bottom'
assert state_at(case,289,66,93)['Name']=='minecraft:ancient_debris'
eye, aim = (289.5,67.27,95.7),(289.5,66.1,93.5)
ys = [eye[1]+(aim[1]-eye[1])*(z-eye[2])/(aim[2]-eye[2]) for z in (95,94)]
assert all(66<y<67 for y in ys) and math.dist(eye,aim)<3
print('complete cell route',route)
print('cover/debris face ray Y',ys)
print('external circuit movement seconds',[60.4/v for v in (4,5,3)])
CONNECTION_CHECK
```

## Original-case quality synthesis and exact remaining boundary

The original provides a measured overlap outcome, not a second pristine
instance of the supplemental arena. Its source still identifies one open ruin
with two material rewards and two ordinary-spawner types. Saved brick blocks
obstruct the transferred interior route, while the retained detour links both
reward faces through exterior terrain. These established facts support the
following original-case conclusions without counting fortress content as Circle
content or silently accepting a template as playable topology.

| Requirement | Original-case result |
| --- | --- |
| Traversal/vertical progression | The declared two-reward external circuit is 60.4 blocks and has zero ascent, descent and feet-height span. Nominal 15.1 movement-only seconds excludes the recorded interaction and combat tasks. This is a validated route, not a full clear time or a global shortest-path proof. |
| Enemy count/diversity and combat | Two saved spawners with explicit piglin/brute IDs, two potential types. Reuse the declared p,b composition grid and its source-supported 0..31.2/0..62.4-second workloads. No realized enemies, encounters or human combat duration is measured. |
| Hazards | Original authored soul fire is absent. The six-block lava column belongs to the neighboring fortress source and does not intersect the validated detour. Its presence is retained as surrounding hazard evidence, not an unavoidable Circle trap. Future flow and enemy displacement are not observed. |
| Rewards and final room | Both original debris nodes survive and have checked face access. One needs a trapdoor toggle; the other needs one ore-cover removal in the model. Harvesting with the iron baseline receives no credit. No separate Circle terminal room or authored ordered finale is identified; finale remains NONE. |
| Bypass and external exposure | Western external access reaches the first reward face without traversing the central spawners. The detour reaches the second without mining the intervening brick obstruction. Both observations are geometric access results, not spawner-activation or combat bypasses. |
| Expected replay | This pair demonstrates saved environmental variation that changes routes and fire presence, despite a fixed Circle template. Finite embedded rewards and repeat spawner attempts remain different revisit mechanisms. No player preference, enjoyment or satisfaction is invented. |
| Large but shallow | The neighboring fortress can make this combined site visually imposing. Its rooms, height and challenges cannot be attributed to the Circle. The Circle has no supported vertical objective sequence; the overlap's longer detour is not evidence of deeper authored progression. |

For room/branching attribution, retain an explicit unresolved boundary. Restrict
the same admitted flat cells to the original Circle envelope: 173 cells qualify;
the western station's component has 13 and excludes the eastern station. This
does not prove two rooms because the predicate excludes partial blocks and
the envelope is not an authored wall. Nor do 327 padded cells or 313 reachable
cells prove an arena room count. The two verified reward-access zones are
nonempty, but a whole-sample empty/dead-room denominator remains UNKNOWN until
the remaining activity boundaries are resolved. The supplemental one-room
denominator must not be silently copied onto the overlapped sample.

No more source inventory, hazard attribution, reward-face geometry or flat
route processing is needed to establish those facts. The exact outstanding
original-case claim is the playable activity-space/connection boundary under
the partial-block and overlap geometry, including any actual constrained
transition. The existing saved dataset is sufficient input; source generation
or another world survey is not required to resolve it. Blackstone material
coverage remains a separate requirement. The item exit gate has not passed.

Reproduce the restricted connectivity derivation by appending this to
CONNECTION_CHECK, reusing its exact cells and path implementation:

```python
e = case['envelope']
inside = {p for p in cells if e[0]<=p[0]<=e[3] and e[2]<=p[2]<=e[5]}
west = paths(inside,(281,66,99))
assert len(inside)==173 and len(west)==13 and (289,66,95) not in west
print('restricted interior/west-component cells',len(inside),len(west))
```

## Room-boundary disposition

Resolve the preceding room-denominator uncertainty by direct layout assessment,
not by equating the restricted flat-cell components with rooms. Reinspection of
the original retained slice sheet at Y66..74 shows a solid obstruction through
the western-central portion of the ruin, with the surviving cache embedded
in it. Direct saved-state inspection at Y67 confirms full nether bricks across
X282..285,Z94..100 except the cache lid at(283,67,99). That solid mass is not
a playable room or a hidden upper activity floor. The surviving perimeter
fragments, eastern spawners and two resource objectives delimit the same
outdoor ruin site. Both objective sectors have validated access and connect
through the measured exterior detour. Counting every excluded partial block
is unnecessary to distinguish solid mass from an activity room.

Use one outdoor activity area within the original ruined perimeter limits
X280..296,Z88..104, with two separated reward-access sectors. This is a
descriptive room boundary, not a claim that every cell in the rectangle is
playable or internally connected at Y66. Retain a two-area sensitivity if the
overlap's interruption is considered a meaningful activity boundary: western
cache sector anchored at(281.3,66,99.5) and eastern resource/encounter sector
anchored at(289.5,66,95.7). The checked exterior connection between those
anchors is 28.4 blocks. It does not pass through an authored doorway and does
not convert surrounding terrain or the neighboring fortress into Circle rooms.

Under the one-area coding, the room graph has one node and zero inter-room
edges, branches or cycles; both objectives have graph depth zero. Under the
split sensitivity, the validated graph has two nodes and one exterior link,
with zero degree-three junctions or cycles and one link from the western to
eastern sector. This latter graph records the demonstrated connection, not
an exhaustive inventory of all possible parallel exterior routes. There is no
measured inter-room chokepoint on that link. Geometric movement alternatives
inside a single open area are not new room-graph branches.

Empty/dead counts resolve to 0/1 under the one-area coding and 0/2 under the
split sensitivity: each sector has a surviving, accessible reward face, and
the eastern sector also contains both recorded enemy sources. Zero enclosed
Circle rooms are established in this cropped ruin assessment. The fortress's
own enclosed spaces remain outside this family's denominator. Final room NONE,
reward distribution, hazards, replay assessment and modeled timing retain the
evidence and limits above. The two-area sensitivity puts one debris node in
each sector rather than concentrating them in a final room.

The earlier UNKNOWN denominator is therefore resolved as an explicitly
ambiguous descriptive coding, supported by saved layout and complete objective
connections. It is not resolved by pretending that the flat-cell predicate
proves every partial-block route. Global shortest walking distance and a
complete movement graph through every obstacle remain unmeasured. Those limits
do not supply extra rooms or justify another source/world-generation pass.
This closes the local original-case assessment under the authorized inspection
scope, while leaving the separate blackstone-root sample and broader Item 13
coverage, raw custody and delivery gates outstanding.

The focused solid-mass check reproduces after ORIGINAL_CHECK:

```python
for x in range(282,286):
    for z in range(94,101):
        expected = 'crimson_trapdoor' if (x,z)==(283,99) else 'nether_bricks'
        assert state(case,x,67,z)['Name']=='minecraft:'+expected
```

## Complete-objective timing demonstration v2

The timing correction supersedes any implication above that a local assessment
closes the timing requirement. Use the existing supplemental sample, unchanged
raw blocks and source observations. No further layout expansion is authorized
until this representative's complete budget is resolved or its limitation has
an explicit accepted methodological disposition.

Objective: starting at the declared southern station(368.5,33,85.5), disable
both authored spawners, defeat every hostile produced by those sources before
disablement, acquire both placed ancient-debris blocks into inventory, and
return alive to that station. Touching a target or merely exposing its face
does not complete the objective. This is a local clear-and-extract objective;
travel from world spawn and first discovery are outside its explicit boundary.

Actor: one adult player with full health/food, unenchanted iron armor and iron
sword, and an unenchanted diamond pickaxe with enough durability for the declared
blocks, available hotbar slots and inventory capacity for both debris drops.
The diamond pick is an explicit capability change from the earlier iron-pick
inspection profile, required by the recorded debris tool constraint. No buffs,
critical/sweep attacks, flight, teleportation, additional building or external
assistance. Navigation knowledge is complete, with no search for target locations;
navigation execution, aiming and interaction costs are not thereby zero.

Use a stipulated initially empty encounter state for this controlled model,
distinct from the unmeasured entity population in the accepted world. Both saved
spawners remain active with their actual Delay 0 and other retained parameters
until broken. Natural spawning is excluded from this narrowly identified model,
not asserted absent in the baseline. The declared route may use the known
trapdoor toggle, one ore-cover removal and source-supported shift crossing.
Additional pickup/pursuit motion must be counted if required. Death, inability
to reach a required target, failed acquisition or an unresolved encounter state
prevents successful completion; an unsupported duration is UNRESOLVED, not zero.

| Cost component | Existing support | Current complete-objective disposition |
| --- | --- | --- |
| Inspection movement | 26-block circuit, 22 upright/4 crouched; 8.833333 nominal seconds, 7.066667 faster, 11.777778 slower | Reusable movement component only. Pickup, spawner-mining positions and pursuit may add motion; complete movement cost UNKNOWN. |
| Navigation and decisions | Complete target/route knowledge is stipulated | Search for locations is excluded by scenario. Execution, aiming, tool changes and decision latency UNKNOWN; no invented player constant. |
| Interactions/acquisition | One toggle and both reward faces supported; source drop creation and ten-tick pickup eligibility recorded below | Eligible contact, added motion and inventory acquisition are not modeled to completion. UNKNOWN. |
| Mining | Required blocks: two spawners, one ore cover, two debris; diamond capability declared | Nominal uninterrupted source work is 13.8 seconds, derived below. Input cadence, interruptions and full elapsed mining cost remain UNKNOWN. |
| Combat | Prior source health/damage model; one-wave grid applies conditionally if both spawners are disabled before 200 ticks, as derived below | Meeting that deadline, spawn success, pursuit and interruptions remain UNKNOWN. Without the condition, the grid is not a population bound. |
| Waiting/recovery | Saved delays and conditional workload inputs retained | No supported encounter-clear verification, injury/recovery or idle schedule. UNKNOWN where required. |

For a sequential model, total would be the sum of nonoverlapping movement,
navigation, interaction/acquisition, mining, combat and waiting/recovery phases.
Combat interruption pauses mining; its duration is not charged twice. No such
schedule has yet been justified. Therefore total completion time is UNRESOLVED;
8.833333 seconds is neither a dungeon completion estimate nor a finite upper
bound, and adding the old one-wave combat range would not fix the missing costs.

This demonstration reuses the existing sample and identifies the exact next
work: source-supported mining/interaction mechanics and an explicit encounter
schedule, followed by acquisition and any added movement. Investigate blocks
again only if they affect one of those required costs. Do not expand to another
layout or claim a timing pass while these components remain unresolved. Human
times, realized encounters and actual acquired loot remain NOT MEASURED.

## V2 mining component: uninterrupted source model

Predeclare the mining component with the v2 diamond-pick actor grounded, dry,
continuously targeting each required block, without effects, enchantments or
mining-efficiency bonuses. Stipulate block-break-speed multiplier 1 and 20 game
ticks per second. These are nominal source-model inputs, not a runtime attribute
measurement. Reserve whole mining ticks using ceil(1/progress_per_tick) per
block. Do not include targeting, tool switching, post-break input delays,
combat interruptions or pickup in this component. Those remain separate costs;
the component cannot establish total objective duration.

Pinned mapped source derivation (same JAR identity and javap procedure as the
existing [model-source notes](../model-source/README.md)):

- Blocks initializer 7062..7065 registers spawner hardness 5;
  2167..2173 registers nether gold ore hardness 3; 34097..34103 registers
  ancient debris hardness 30. Blast resistance is the other strength parameter
  and must not be substituted for mining hardness.
- Tiers initializer 88..111 constructs DIAMOND with speed 8. PickaxeItem's
  constructor supplies MINEABLE_WITH_PICKAXE; DiggerItem uses
  Tier.createToolProperties, whose offsets 14..20 add minesAndDrops at tier speed.
- The pinned extra JAR's data/minecraft/tags/block/mineable/pickaxe.json,
  SHA-256 e31b952f7df00a46e2e442e601b1139e87085314364e9137381c71e66f55700f,
  lists all three blocks. incorrect_for_diamond_tool.json is empty, SHA-256
  b83114c23eeec820ce7eca52011f13013fb6c64002254be7aebe1e4b36244d48.
  These support the nominal correct-tool branch; they are not a new merged
  runtime-tag observation.
- BlockBehaviour.getDestroyProgress offsets 20..49 divides player destroy speed
  by hardness and then 30 for the correct tool (100 otherwise). The retained
  Player.getDestroySpeed derives tool speed, efficiency, effects, break-speed
  attribute, submerged penalty and airborne penalty. The declared grounded,
  dry, unmodified scenario therefore uses progress=8/(hardness*30).

Reproduce the predeclared whole-tick calculation:

```sh
uv run python - <<'MINING_CHECK'
import math
rows = [('spawner',2,5),('ore cover',1,3),('ancient debris',2,30)]
total = 0
for name,count,hardness in rows:
    ticks = math.ceil(1/(8/(hardness*30)))
    total += count*ticks
    print(name,'count',count,'ticks per block',ticks,'seconds per block',ticks/20)
assert total==276
print('uninterrupted mining component seconds',total/20)
MINING_CHECK
```

Result: 19 ticks(0.95 seconds) per spawner, 12 ticks(0.6 seconds) for the ore
cover, 113 ticks(5.65 seconds) per debris block. The five required block breaks
reserve 276 ticks, 13.8 seconds of uninterrupted source-modeled mining work.
This resolves the nominal work term, not all elapsed mining-phase costs.
It excludes mod/event changes, packet/input cadence, interrupted progress,
delays between blocks and server tick-rate variation. No finite bound on those
omissions is asserted. In particular, the spawners remain active while being
approached and mined; this work term does not resolve enemy count or schedule.
The complete-objective time remains UNRESOLVED, and layout expansion stays paused.

## V2 acquisition and spawner-schedule conditions

Direct source inspection resolves why resource contact and acquisition must
remain distinct. In the pinned extra JAR, ancient_debris block loot-table
resource SHA-256 14125055edd8b94e7819540ff2f5d063395f451d2f7883bf79ece79894cd546d
contains one roll yielding ancient_debris, conditional on survives_explosion.
This is source loot potential for the correct-tool mining model, not a sampled
drop or inventory receipt. Block.popResource checks server side, nonempty stack
and doTileDrops before creating the item. Its positional overload randomizes
each coordinate around the block center by up to 0.25 and adjusts Y by half the
item height. Do not assume the item appears at the inspection ray endpoint.

Block.popResource's private overload offsets 38..44 sets the default pickup delay
before adding the entity. ItemEntity.setDefaultPickUpDelay sets 10; tick offsets
19..43 decrement a positive non-infinite delay. playerTouch offsets 27..63 requires
delay zero, a compatible target and successful Inventory.add. Thus the source
model has ten eligible item ticks before pickup, nominally 0.5 seconds at 20 TPS,
plus actual eligible contact. It does not establish an elapsed acquisition time.
Movement, combat or other work may consume those ticks concurrently; adding
one second for two drops would be unjustified double counting. The retained
face-access stations do not prove pickup contact after randomized item movement.
Added pickup motion and acquisition completion therefore remain UNKNOWN.

Predeclare a conditional spawner-first schedule for this same objective: walk
the already validated four-block southern approach, mine both spawners from
the inner station before voluntarily starting combat or collecting rewards,
then finish combat and extraction. Let H be all extra elapsed ticks before
the second spawner is disabled beyond the nominal approach and two uninterrupted
breaks: aiming, input delays, interruptions, displacement and any lost progress.
H is nonnegative and currently unbounded; this declaration does not claim the
actor can ignore incoming attacks or survive them. Start the clock at activation
in the stipulated initially empty, Delay 0 encounter state.

The retained BaseSpawner.serverTick checks activation, decrements positive delay
and returns (offsets 0..41), then attempts up to spawnCount entries (63..69).
A successful spawn sets the success flag (723..724); the end-of-loop delay
reset occurs at 731..738. delay offsets 27..48 chooses minDelay+nextInt(max-min),
so these saved spawners reset to 200..799 ticks. Failed positioning attempts
are not guaranteed enemies and do not justify a fixed actual count. Nevertheless,
if both spawners are disabled strictly before 200 elapsed game ticks, each can
have at most one successful spawn batch of up to four in this source model.
That is a condition under which the earlier p,b in 0..4 grid applies, not proof
that the condition holds for the complete objective.

At the nominal four-blocks-per-second rate, approach takes 20 tick slots and the
two uninterrupted breaks take 38. The conditional second-disable deadline is
D=58+H ticks. D<200 therefore requires H<142 ticks(7.1 nominal seconds).
No estimate or upper bound for H has been established, and death prevents a
successful schedule. If the condition fails, the old one-wave combat grid is
insufficient; later successful batches must be represented. This links the
mining and encounter models without assigning a fabricated eight-enemy census.

Reproduce the schedule condition's arithmetic:

```sh
uv run python - <<'SCHEDULE_CHECK'
import math
approach_ticks = math.ceil(4/4*20)
break_ticks = 2*math.ceil(5*30/8)
assert approach_ticks+break_ticks==58
assert 200-(approach_ticks+break_ticks)==142
print('nominal approach+mining ticks',approach_ticks+break_ticks)
print('strict extra-time threshold in seconds',142/20)
print('default item pickup delay at 20 TPS',10/20)
SCHEDULE_CHECK
```

These findings reduce two missing components to explicit source constraints.
They do not resolve navigation/input latency, survival, actual spawn success,
post-break movement or inventory acquisition. Total completion time remains
UNRESOLVED; no new layout, runtime actor or player observation was introduced.
