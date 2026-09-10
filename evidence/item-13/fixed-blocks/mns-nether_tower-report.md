# Nether Tower: quality assessment

Status: local conditional assessment recorded. Source/saved inputs, access,
complete-task timing and room/quality synthesis are integrated. Family repetitions
and broader Item 13 coverage remain required.

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

## Complete conditional task timing

Predeclare the local objective: start at (216.5,55,260.5), perform the documented
breach, transfer all sixteen barrel inventories and the elevated chest inventory,
and return alive to the starting station. One fully informed adult starts at full
health/food with unenchanted iron armor/sword, diamond pickaxe of sufficient
durability and nineteen scaffolds. Retain all previously specified removals,
placement order, face-access conditions and return path. No extra construction,
mining, flight, teleportation, assistance, pre-applied effects or healing is allowed.
Construction remains in place. Ignore incidental mined-block drops; material
procurement, discovery and travel to the entry are outside this local objective.

Stipulate no pre-existing or naturally spawned mobs and no entity blockers.
There are no authored sources to activate in this template. Thus this scenario's
combat component is zero, not an observation that a real visit is enemy-free.
Any encounter invalidates this zero-combat scenario; no generic combat estimate
is silently substituted. Survival and successful transfers remain conditions.
All rolled results must fit the actor's available inventory after equipment and
remaining materials, including before each emptied barrel is removed. Capacity
failure censors acquisition rather than implying all seventeen containers fit.

Use the accepted A/B/C provisional allowances. Upright movement rates are 5/4/3
blocks/s; vertical climb and controlled descent rates are 1.5/1/0.75 blocks/s,
as explicitly modeled for the Large House. The circuit has 27.4 horizontal and
38 vertical blocks, including the 1.4-block scaffold placement adjustment. No
extra movement is hidden in mining or inventory allowances.

Predeclare nine stationary decision allowances: initial orientation, breach,
cache station A, cache B, cache C/D, vertical approach, overhead-removal sequence,
upper chest and return. These include reorientation and pose changes. Hold the
pickaxe during the lower-cache container interactions, allowing immediate mining
after each required transfer. Five selections equip the initial pickaxe, scaffold
for the first seven blocks, pickaxe for overhead removals, scaffold for twelve
extensions, then an empty hand for the elevated chest. No sword selection is
charged in the zero-encounter scenario.

Charge nine mined-target interactions (two entry blocks, four emptied barrels,
one lantern and two overhead blocks), nineteen scaffold placement interactions,
and 17*29 container interactions (open, scan/shift-click all 27 slots, close).
This totals 521 aiming/input allowances. A slot operation is charged whether or
not that slot contains an item; it is a provisional GUI allowance, not an observed
inventory. Add seventeen acquisition-confirmation allowances and one final
verification allowance. Mining work is additional to its targeting allowance;
container transfers are not also charged as ground-item pickup.

Use the same pinned nominal mining rule as the earlier reports: whole ticks are
ceil(hardness*30/speed) under correct-tool or no-tool-required conditions. The
mapped `Blocks` initializer registers barrel hardness 2.5 (31196..31199), soul
lantern 3.5 (31718..31721), red nether bricks 2 (25172..25176) and polished
blackstone 2 (34454..34458). Obsidian and crying obsidian use hardness 50. The
pinned pickaxe tag includes the five stone/lantern types, but not barrels. The
barrel does not require a particular tool for drops, so the pickaxe's default
speed 1 and divisor 30 apply. All breaking uses supported stances, no effects,
no submerged penalty and the stipulated 20 TPS, not measured runtime speed.

| Breaking group | Count | Hardness / speed | Ticks each | Total seconds |
| --- | ---: | --- | ---: | ---: |
| Obsidian and crying-obsidian entry | 2 | 50 / 8 | 188 | 18.8 |
| Transferred empty barrels | 4 | 2.5 / 1 | 75 | 15 |
| Soul lantern | 1 | 3.5 / 8 | 14 | 0.7 |
| Red-nether-brick and polished-blackstone overhead blocks | 2 | 2 / 8 | 8 | 0.8 |

Uninterrupted breaking totals 706 ticks, or 35.3 seconds. With u horizontal rate,
h vertical rate and the accepted decision n, interaction a, selection s,
acquisition k and verification v allowances, complete successful-scenario time is

T = 27.4/u + 38/h + 35.3 + 9*n + 521*a + 5*s + 17*k + v.

| Complete conditional task | A | B | C |
| --- | ---: | ---: | ---: |
| Seconds | 221.1 | 390.2 | 710.6 |

Report approximately 221/390/711 seconds with profile and zero-encounter condition
visible. The large share of inventory time follows the specified all-container
objective and provisional per-slot allowance; it is not measured play or evidence
of a typical player's efficiency. No required phase is silently omitted.

Censor completion on failed transfer/capacity, unmodeled entity encounter,
invalid chest access, death/healing, support or placement failure, changed block/
fluid conditions, input/mining interruption beyond allowances or departure from
20 TPS. No censoring event or elapsed human time has been observed. This complete
conditional estimate does not establish generated/acquired loot, realized combat,
room quality or family-level completion.

Reproduce both source-derived work and complete-task arithmetic:

```sh
uv run python - <<'TOWER_TASK'
import math
rows = [(2,50,8),(4,2.5,1),(1,3.5,8),(2,2,8)]
ticks = sum(count*math.ceil(hardness*30/speed) for count,hardness,speed in rows)
assert ticks == 706
assert 9+19+17*29 == 521
profiles = [('A',5,1.5,.5,.25,.25,1,2),
            ('B',4,1,1,.5,.5,2,4),
            ('C',3,.75,1.5,1,1,4,8)]
for name,u,h,n,a,s,k,v in profiles:
    total = 27.4/u+38/h+ticks/20+9*n+521*a+5*s+17*k+v
    print(name,total)
TOWER_TASK
```

## Integrated topology and quality assessment

Delineate two authored activity spaces under the protocol definition. L is the
lower furnished/cache hall, interior band X218..230, Z250..262, feet Y55 above
the Y54 floor. U is the upper chest chamber, interior band X221..227, Z253..259,
feet Y67 above the Y66 floor, surrounding the central column. Bounds include
fixtures and obstacles, not an assertion that every enclosed cell is walkable.
The slice sheet shows these broad spaces without a supported sequence of
intermediate rooms. The one-high air layer at Y65 between solid Y64/Y66 layers
is not a room for the declared 1.8-high actor. Exterior ledges, roof ornament,
solid mass and the scaffold itself are not extra rooms.

The upper room is more than air beside a pillar: at (222,256), (222,255),
(223,255) and (224,255), Y66 is full polished blackstone and Y67/68 are air.
After constructing the declared shaft, an optional one-block west transfer from
(223.5,67,256.5) to (222.5,67,256.5) therefore lands on an existing upper floor.
This demonstrates room access. It is not added to the timed objective, whose
chest interaction takes place higher on the scaffold and does not require this
optional detour. Existing upper floor height is twelve blocks above the lower
floor; the chest interaction stance is nineteen blocks above the lower entry.

The established native room graph has two nodes and no verified inter-room edge,
so two components. This records the accepted link set, not a proof that every
possible parkour trajectory or arbitrary breach has been ruled out. The complete
engineering route adds one L-U connection through the two removed overhead
blocks: two nodes, one edge, one component, zero degree-three junctions and zero
independent cycles. Both rooms are terminal nodes of that chain. There is no
supported succession of forty-six playable tower levels.

The entry breach is one block wide and two high; the constructed vertical shaft
is one block wide. These are geometric chokepoints, not observed enemy bottlenecks.
Full objective movement is 65.4 blocks (27.4 horizontal, 38 vertical), with nineteen
blocks ascent and nineteen descent. The deepest room is one graph edge from L.
Within the declared connectors, the chest-stance depth from the local entry is
30 movement blocks: five east, four north, two east and nineteen up. Construction
adds the documented 1.4-block out-and-back placement adjustment, distinct from
this shortest connector depth. The optional upper-floor landing is 24 blocks from
entry (eleven approach, twelve up, one west). Lower-cache station D is seven
blocks from entry. None is a global optimum across unspecified engineering.
All 529 saved footprint heightmap values are Y127; actual solid terrain cover
above rooms remains UNKNOWN rather than inferred from the 31-block difference
to envelope top Y96.

### Enemy, hazard, empty-space and loot conclusions

Authored enemy count/diversity are zero template residents and zero spawner
sources/types. The source-only count does not include natural mobs. Realized
encounters and human combat time remain NOT MEASURED; zero modeled combat applies
only to the explicitly no-encounter task. There is no source-supported dungeon
encounter composition to score as challenging here.

The meaningful route hazard is fall/displacement exposure during the nineteen-
block climb, especially the placement stance with only 0.1 blocks of support
overlap. Continued support and controlled descent are conditions, not measured
survival. The retained envelope contains lava at (213,51,260) and magma at
(216,51,267), (220,51,267), (224,51,267), all outside/below the verified route.
These do not establish a required lava or magma crossing. No active fire or
working redstone trap is established on the declared path. The two unlit blast
furnaces at (227,Y55/56,262), two cauldrons at (230,55,259/260) and enchanting
table at (228,55,252) are facility/source content, not extra enemies or rooms.
Their operation is outside the acquisition objective and is not observed.

Empty rooms: 0/2. Dead rooms: 0/2. L has sixteen authored barrel rewards and
facilities; U has the elevated treasure chest. There is no supported empty-room
claim based merely on absence of enemies. Loot distribution is 16/17 containers
in L using houses, 1/17 in U using treasure. Table class is potential, not rolled
quantity, value or acquisition. Stacked containers require the documented prior
transfers and removals; their count overstates independently approachable reward
stations if treated as seventeen separate activities.

### Finale, bypass, replay and large-but-shallow conclusions

The upper chamber is a supported terminal reward candidate: it contains the
single elevated treasure-table chest, contrasting with the lower houses-table
barrels. It is not a boss or a scripted completion trigger. Final-room assessment:
objective clarity CONDITIONAL (visible chest placement and differentiated table,
without an explicit quest signal); distinctive terminal encounter ABSENT;
terminal reward linkage PRESENT as source potential; native route integration
UNKNOWN (no validated native climb), engineering integration PRESENT; external
bypass exposure CONDITIONAL on construction. These distinguish a reward finale
from an observed satisfying conclusion.

The concrete partial-objective bypass is lower-cache extraction. The fourteen-
block ground circuit, two obsidian-family entrance removals, four emptied-barrel
removals and one lantern removal expose 16/17 reward containers without upper
construction or ascent. Their source table differs from the upper treasure table,
so this does not establish 16/17 of reward value. The complete scaffold route
provides a construction alternative with nineteen carried blocks and two overhead
removals, preserving effort and fall exposure without assuming a native climb. It demonstrates an
earned construction alternative, not a free roof access or an observed exploit.

Expected replay value: limited authored-layout and encounter novelty, with
conditional loot/terrain variation. The sampled component is a fixed template
with empty processors and no authored mob sources. Further instances can vary
orientation, surrounding terrain and loot results, but those are not observed
probability distributions here. Revisiting the same site after this objective
retains the breach, removed front barrels and scaffold; loot access mechanics
do not reconstruct those physical obstacles. No template mechanism establishes
re-sealing or renewable authored encounters. Player enjoyment/replay behavior
remains NOT MEASURED.

Large-but-shallow: supported in native dungeon-content terms. The tall exterior
contains two delineated activity spaces and no explicit encounter sources, with
most reward nodes in one ground cache and no verified native vertical link.
Construction creates meaningful access work, but template height alone is not
room depth or combat quality. Describe it as a tall resource/extraction structure
with an elevated reward, rather than assuming a multi-floor combat dungeon.

This sample's local assessment is recorded under the accepted conditional scope.
The other selected candidate, family repetitions, remaining families/variants and
Item 13 review/delivery gates are not completed by this result. No new world or
runtime experiment was performed, and Item 14 remains UNSTARTED.
