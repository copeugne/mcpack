# Nether Brick Circle: quality assessment

Status: IN PROGRESS. Saved/source evidence is integrated; playable topology and
route scoring remain pending. This is one material layout of mns:circle_ruin;
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
RequiredPlayerRange16, MinSpawnDelay200, MaxSpawnDelay800, Delay0 and empty
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
