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
