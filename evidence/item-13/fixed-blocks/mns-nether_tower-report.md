# Nether Tower: quality assessment

Status: IN PROGRESS. Source/saved enemy and reward inputs are integrated.
Playable topology, complete task timing and quality synthesis remain required.

Sample: full-ocean-heavy-r1-baseline|minecraft:the_nether|mns:nether_tower|14|16.
Reuse the retained [saved blocks](mns-nether_tower.json.gz), SHA-256
03e5bcfe3dacf13b7780dc46b1a525145ad945aa5255baecc6e7386fac47eb0c.
The compressed file is 8,464 bytes and contains 43,732 padded voxels. Envelope
[213,51,245,235,96,267], padded bounds [210,48,242,238,99,270]. Existing extraction
and custody records retain world identity and complete chunk coverage. No new
world generation or extraction is required for this inspection.

## Source correspondence and encounter inputs

The saved rigid single-pool component directly selects `mns:nether_tower`, with
empty processors, origin (235,51,245) and CLOCKWISE_90 rotation. Source local
(u,v,w) maps to (235-w,51+v,245+u). This is one fixed authored component, not a
room count or proof of continuous vertical access.

Use the previously verified MNS JAR SHA-256
05024f18690436fff2fbc088f880a95cc30f23bacfe6e8058f6b02106032a990.
Its `data/mns/structure/nether_tower.nbt` SHA-256 is
06621f2778578d2bf4b043abb8afbc54cfaba827f38a43b1ccca5167e68e55a6.
Source dimensions are 23x46x23. The template's entities list is empty and its
palette contains no spawner state. Saved block entities likewise contain no
spawner. The packaged `data/mns/worldgen/structure/nether_tower.json` has empty
spawn_overrides. These establish zero explicit template-resident enemies and
zero authored spawner sources, not zero realized enemies in the accepted world.
Natural mobs, surrounding structures and actual encounters remain NOT MEASURED.
A no-natural-spawn conditional task can therefore have zero authored combat work;
it must not be reported as a measured peaceful visit.

All seventeen source reward blocks map to unique matching saved block entities,
with identical type and LootTable assignments:

| Group | Saved positions | Source table |
| --- | --- | --- |
| West lower stack | (218,55,258), (218,55,259), (218,55,261), (218,55,262), (218,56,258), (218,56,262), (218,57,258) | `mns:chests/houses` |
| Inner lower stack | (219,55,258), (219,55,259), (219,55,262), (219,56,258), (221,55,262) | `mns:chests/houses` |
| East lower stack | (222,55,261), (222,55,262), (222,56,262), (223,57,262) | `mns:chests/houses` |
| Elevated chest | (224,75,256) | `mns:chests/treasure` |

These are sixteen barrels and one chest, not seventeen rooms. Reuse the
[Large House table inspection](mns-large_house_1-report.md#active-source-and-positional-correspondence)
for houses/treasure content potential and exact resource hashes. Saved LootTableSeed
values do not establish rolled contents. Access, chest-lid clearance, generated
items and acquired inventories are not established by positional correspondence.
Do not assume that the elevated treasure chest is an authored finale merely
because it is higher than the lower cache.

Reproduce correspondence by decoding the named template with the existing
`mcpack_evidence.item7_nbt.decode_compound_nbt`, applying the transform above to
barrel/chest positions, and joining against `block_entities` in the hash-bound
extraction. The 17 transformed positions are unique and each type/table matches;
there are no source spawner palette states and no source entities. Direct immutable
artifact inspection suffices; no new helper or runtime probe is introduced.

## Bounded topology inspection predeclaration

Inspect the retained block slices to identify entrance, lower cache, vertical
connections, elevated chest access and any other playable activity space. Resolve
actual floor support, doors, ladders/stairs and overhead clearance before modeling
a route. The 20-block difference between lower barrel Y55 and chest Y75 is a
target-height difference, not established progression.

Budget direct queries at one minute, 512 MiB memory and under 1 MiB text. If a
slice render is needed, reuse `render_pilot.render_slices`, with one bounded
180-second conversion and at most 20 MiB SVG/PNG output. This is read-only analysis
of the already retained extraction; no server or world materialization is planned.
Record render failures rather than silently replacing them. Use the separately
accepted complete-task accounting method after access is resolved. Item 14 stays
UNSTARTED.

## Retained slices and first vertical constraint

The bounded conversion completed with clean exit in 32.42 seconds (Bash time,
user 29.17, system 5.12). Its [slice sheet](mns-nether_tower-slices.png) is
201,810 bytes at 1532x4771 pixels; temporary SVG is 7,191,441 bytes, for a combined
7,393,251 bytes. No render failure occurred. The agent inspected the full sheet;
colors represent saved block categories, not collision shapes or human gameplay.

Reproduce without new world reads:

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/mns-nether_tower.json.gz --output /tmp/item13-nether-tower-slices.svg
time -p timeout 180 convert -background white /tmp/item13-nether-tower-slices.svg /tmp/item13-nether-tower-slices.png
```

A full-envelope name query finds no ladder or twisting-vine block. The sixteen
trapdoors are all warped trapdoors at Y79, above the treasure chest. They do not
by themselves provide a lower-to-chest route. Stair-shaped decoration remains
present; its existence is not proof of a continuous climb.

At the chest's column (224,256), the saved vertical sequence is full deepslate
tiles at Y54, air Y55..63, red nether bricks Y64, air Y65, polished blackstone
Y66..74, east-facing single chest Y75, then air Y76/77. The adjacent west column
(223,256) has the same lower sequence through Y66 but air Y67..77. Thus the chest
sits atop a nine-block polished-blackstone column above Y66, with no axial access
through that solid column. Air beside a pillar is not a supported staircase.
The Y64 and Y66 layers also interrupt a direct ascent from the lower cache.
A lateral native route or explicit construction must be established before
counting this as twenty blocks of playable progression.

These facts are reproducible using `render_pilot.state_at` on the two named
columns and a palette-name query over the exact envelope. They resolve the axial
obstruction and preserve the distinction between decorative height and playable
access. Entrance, cache-container access and the complete vertical route remain
the next measurements; no unsupported traversal time is assigned.

## Conditional lower-cache entrance and all-barrel access

Predeclare a west-side engineering entry at (216.5,55,260.5). This is a local
breach boundary, not a claim of a discovered authored door. Both actor body cells
are air above full cobbled-deepslate support at Y54. Remove (217,56,260), crying
obsidian, then (217,55,260), obsidian, using the declared diamond pickaxe from
this supported station. Both west faces are within three blocks. The preserved
floor is full cobbled deepslate. After removal, the two-block eastward movement
to (218.5,55,260.5) has full support and two-high air clearance. This is two paid
cover removals, not native entrance connectivity.

The stacked cache has hidden barrels. Predeclare four front-barrel removals,
each only after opening and transferring that barrel's full contents, plus one
soul-lantern removal. The barrel remains counted once as a reward node even when
its empty block is subsequently removed. Ignore the resulting empty block and
lantern drops; sufficient inventory for the reward transfers remains conditional.
Failure to transfer a front barrel censors the dependent access, not permission
to destroy its contents and claim acquisition.

Use feet Y55 and upright eye Y56.62 at these four stations:

| Station | X/Z | Operations and exposed targets |
| --- | --- | --- |
| A | (218.5,260.5) | Transfer barrel (218,55,259), remove lantern (218,56,259), then remove the emptied barrel. Access (218,Y55/56/57,258) through that cleared column. Transfer and remove (218,55,261), then access (218,Y55/56,262). This covers all seven west-stack barrels. |
| B | (219.5,260.5) | Transfer and remove (219,55,259), then access (219,Y55/56,258). Access (219,55,262) through the clear Z261 column. This covers four inner-stack barrels. |
| C | (221.5,261.5) | Access (221,55,262) and (222,55,261). After transferring the latter, remove it and move east into its former cell. |
| D | (222.5,261.5) | Access (222,Y55/56,262) and the high barrel (223,57,262). This completes the remaining three east-stack barrels. |

For a neighboring lower barrel, target its exposed side at Y55.9, staying below
any lantern or barrel above it. At A, the northern backs have south faces at
Z259; the southern backs have north faces at Z262. For middle-height barrels use
Y56.5. The highest northern barrel can be targeted on its south face at Y57.8,
above the intervening lower stack. At B the same Z259/Y55.9 or Y56.5 rays pass
through the removed front barrel and air above it. The southern barrel's north
face at Z262/Y55.9 is reached before its overhead lantern can intersect the ray.

At D the two directly southern barrels have north faces at Z262/Y55.9 and Y56.5.
For the high eastern barrel, aim at west-face point (223,57.8,262.5). The ray from
D's eye passes above the Y56 barrel at (222,56,262), whose top is Y57, then reaches
the target above the wall at (223,56,262). It stays west of the purple-wool column
at (223,Y55..58,261). The target is approximately 1.63 blocks from the eye, within
the three-block interaction condition. These are explicit face rays, not an
assumption that all barrels in a stack can be opened from a common viewpoint.
Barrel access does not require chest-style lid clearance; no barrel was opened
in the saved world.

Connect the stations by the following X/Z waypoints at feet Y55:
(216.5,260.5), A, B, (221.5,260.5), C, D, C, (221.5,260.5), (216.5,260.5).
All retained floor cells are full cobbled deepslate at Y54, and all body cells
are air or the explicitly removed wall/front-barrel cells. The full lower-cache
out-and-back path is fourteen horizontal blocks. No step, jump, crouch or
standing atop a barrel is implicit. Additional vertical access is separate.

This resolves all sixteen lower barrel targets with two wall removals, four
emptied-barrel removals and one lantern removal. It does not yet resolve the
seventeenth reward, elevated chest, or the complete tower task. Source/saved
queries use the same extraction: inspect Y54..58 at the listed stations, target
positions and ray cells with `render_pilot.state_at`. Preserve every unmodified
block and the conditional nature of the declared removals.

## Elevated chest: explicit scaffold connection

Predeclare nineteen carried scaffolding blocks for a vertical column at (223,256),
west of the chest's solid support. From the lower-cache circuit's (221.5,55,260.5)
waypoint, walk north four blocks to (221.5,55,256.5), then east to the column.
All six horizontal blocks have retained full floors at Y54 and air at Y55/56.
Place the base at (223,55,256) from adjacent (222.5,55,256.5), on full deepslate
tiles. No bridge or unrelated shaft is implicit.

Build seven scaffolds at Y55..61, enter and climb to stand at feet Y62. Head
height is Y63.8, below the red-nether-brick layer at Y64. From this supported
stance, mine (223,64,256), then (223,66,256), polished blackstone, through the
now-cleared lower layer and air at Y65. Their undersides at Y64 and Y66 are
respectively 0.38 and 2.38 blocks above eye Y63.62, within three-block reach.
The lower block must be removed first. This preserves a supported mining stance
for both actions rather than charging grounded work while hanging.

For the first six extensions, click the base's west side near its top rail at
(223,55.95,256.5) from the adjacent station. For the twelve later extensions,
move 0.7 blocks west on the Y62 scaffold top to center X222.8, retaining 0.1 blocks
of body overlap with its support. Keep upright and do not activate descent. Click
the existing scaffold's west face near its top rail at (223,61.95,256.5), then
repeat for all twelve extensions at Y62..73. Return 0.7 blocks east to the center
and climb to feet Y74. The west neighboring cells at Y61..63 are air. This explicit
1.4-block stance adjustment is required, with loss of support censoring the model.
Pinned `ScaffoldingBlockItem.updatePlacementContext` directs an ordinary side
click UP and advances through the existing column to the first replaceable cell;
clicking its top without secondary use instead requests a horizontal extension.
The side-click sequence therefore matters and is included in placement input
allowances, not treated as direct reach to every new top block.
The full inspected column is air from Y55 through Y77 apart from the two named
removals. Every scaffold inherits distance zero from the supported vertical stack,
using the already documented pinned ScaffoldingBlock rules in the Large House
assessment. Supported standing and controlled climb/descent are conditional on
successful placement and actor behavior, not runtime observations.

From (223.5,74,256.5), eye Y75.62, target the chest's west face at
(224.0625,75.5,256.5). This uses the chest's inset shape rather than the full-cell
boundary. The ray is short, passes through the scaffold's open space above its
top, and meets the chest without crossing the solid support at Y74. The chest is
single, with no saved Lock and air immediately above at (224,76,256). Under the
existing no-entity-blocker assumption, saved block geometry therefore satisfies
the chest-opening conditions. Generated inventory, transfer and successful opening
remain NOT MEASURED. No extra upper floor or platform is assumed at chest height.

The out-and-back branch contributes 13.4 horizontal and thirty-eight vertical
blocks, nineteen placements and two additional mined targets. Return follows the
same scaffold column under controlled descent. Keep the tower in place; recovery
is outside the objective. Failure of placement, support, chest access or transfer
censors this branch. Together with the lower-cache route, all seventeen reward
nodes now have conditional access, with 27.4 horizontal and 38 vertical route blocks.
Complete task timing must still add all actions, inventory work and verification.

Reproduce geometry from the same hash-bound extraction: query (223,Y54..77,256),
(224,Y74..76,256), Z256 at X221..223 and X221 at Z256..260, including floor Y54
and body Y55/56. The exact two solid breaks and continuous remaining column are
recorded above; this derivation requires no new world or runtime experiment.
