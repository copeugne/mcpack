# Medium House 2: quality assessment

Status: local modeled/inspection assessment recorded. Raw-capture custody and
Item 13 delivery remain IN PROGRESS; no human gameplay is claimed.

Sample: full-mountainous-r2-baseline|minecraft:the_nether|mns:medium_house_2|1|7.
[Saved blocks](mns-medium_house_2.json.gz), SHA-256
c1fa53cbbae3cc48f56a48baacdfd80746bd937662a57db35d49f98b698447a6,
retain 8,500 voxels and 127 palette states. Original envelope is
[7,32,107,25,45,117], retained padded bounds [4,29,104,28,48,120].
World/census/backup identity and the fixed-layout selection are inside that
existing dataset. No new world generation or extraction is required.

The [slice sheet](mns-medium_house_2-slices.svg) was visually inspected after
rendering with the existing renderer. It depicts block categories, not collision
shapes or player observations. Reproduction from repository root:

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/mns-medium_house_2.json.gz --output /tmp/item13-house2-slices.svg
```

## Saved layout and concrete access differences

The lower interior is X13..19,Z110..114 above full authored support at Y33.
Its three beds are at (13/14,34,111), (13/14,34,113) and
(18,34,110/111); the anvil is at (17,34,114). Furnishings are not independent
rooms. A west storage ledge has slabs at (14,36,111/113) and a central
trapdoor at (14,36,112). Twisting-vine columns at (14,110) and (14,114)
reach from Y34 through Y37 and Y36 respectively. These suggest transitions;
exact clearance and support must establish their usable connections.

Both crimson door leaves at (18/19,34/35,115) are saved closed, facing north,
with left and right hinges respectively. Unlike the first house, there is no
saved-open entrance leaf. An ordinary door-opening capability must be declared
and its changed shape supported before an internal route can start there.
The first house's accepted route and collision palette are not this layout's
runtime observation. Reuse source rules where applicable, not its world shapes.

The roof line has spawners at (14,40,112) and (18,40,112), with a barrel at
(16,40,112). Intervening air cells (15/17,40,112) have full blocks at Y41,
leaving one block of headroom. They are not upright/crouched activity rooms.
The barrel faces upward; blackstone at Y41, stripped warped hyphae at Y42 and
a closed bottom warped trapdoor at Y43 cover its column. Y44..45 are air.
Given roof access, removing those three blocks exposes the barrel. This is a
conditional three-block cover scenario, not observed mining, approach or loot.

## Enemy, hazard and reward evidence

Both saved spawners have SpawnData.entity={} and SpawnPotentials=[]. Their
previously completed [frozen-runtime lookup disposition](../collision/README.md#saved-spawner-lookup-result)
is reused: no resolvable entity type and no replacement from an empty list.
The distinct saved delays are 220 and 85 ticks; each SpawnCount is 4. Those
parameters do not supply an enemy when the entity assignment cannot resolve.
Authored ordinary-spawner potential is zero resolvable types; the corresponding
nominal attack workload is zero. This excludes natural mobs and any other
encounter source, and is not an observed enemy census or a zero-second clear.
Realized encounters and human combat/traversal times remain NOT MEASURED.

| Saved reward position | Table potential | Layout location |
| --- | --- | --- |
| 13,37,110 | mns:chests/uncommon | West storage |
| 13,37,111 | mns:chests/houses | West storage |
| 13,38,111 | mns:chests/houses | West storage |
| 16,40,112 | mns:chests/empty | Roof cavity |

These four barrels have saved table seeds but no generated Items or Lock fields.
The first-house [table/source assessment](mns-medium-house-report.md#contents-rewards-and-current-quality-implications)
applies to these identical packaged tables. In particular, the table named empty
contains nonempty item opportunities. Three storage nodes versus one roof node
is a location count, not a reachable-room or acquired-value distribution.
Interaction positions still need geometric support; barrel use does not inherit
a chest-lid obstruction rule.

The same Nether bed-use explosion mechanism applies to the three black beds.
It is an optional interaction hazard, not damage from walking past them. Magma
exists in the padded raw palette but no magma block lies inside the original
envelope; do not count palette presence as an interior floor hazard. Exterior
approach remains separately unmeasured. Buttons and the pressure plate are
mechanism ingredients; no working trap is inferred from their presence.

All 209 saved WORLD_SURFACE columns are Y127. Reusing the pilot height-difference
metric gives 127-45=82 blocks above envelope top, not 82 solid mining blocks.
The roof-barrel column's immediate air break is established above. Full room
and route depth remain pending playable topology.

## Runtime shape coverage and declared opening capability

The [second-house collision capture](../collision/README.md#second-house-saved-view-collision-predeclaration)
now resolves all 8,500 saved cells into 39 AABB unions with no unsupported queries.
The fresh frozen runtime passed its configuration checks, matched flush and clean
shutdown in 211.427 seconds. Its input remains the exact closed-door saved layout.
This is shape coverage, not completed actor movement or room connectivity.

The [door source derivation](../model-source/README.md#second-house-ordinary-door-opening-model)
supports ordinary hand opening. The next route model may open only the right
leaf's two halves at (19,34/35,115), substituting the source-supported open AABB
while preserving the closed runtime capture. The left leaf stays closed. The
actor and default step/vine capabilities reuse the first-house declarations;
actual door interaction and its latency are not measured. This resolves the
material capability choice without inventing a saved-open state.

## Validated south-vine circuit and storage access

The [first route result](../collision/house2-r1-route.json) passes all twenty
complete swept segments under the declared right-door opening substitution.
All lower-route floor cells at Y33 are full crimson planks/hyphae, deepslate
bricks or polished blackstone bricks. The continuous south vine at (14,114),
Y34..36, supports the declared climb to feet Y36.5. The upper ledge at X14 has
bottom slabs at Z111 and113 and a bottom trapdoor at Z112, so its floor tops
are 36.5 and36.1875. The checker verifies slab adjacency at the Z112.7/112.3
height transitions as well as full collision sweeps. This is a supported
kinematic connection, not an observed climb or tick-accurate physics trace.

Closed circuit distance is **32.25 blocks**: 20 upright horizontal, 6 crouched
horizontal, 5 vine vertical and 1.25 step/drop vertical. Feet span=2.5;
ascent=descent=3.125. Reusing the declared rate vectors gives **17.5 seconds**
nominal, **11.75 seconds** faster and **28.333333 seconds** slower. Direct
nominal derivation: 20/4+6/1.2+5/1+1.25/0.5. These are sensitivity scenarios,
not confidence intervals, observed travel or full clears. They exclude opening
the door, pose-change latency, menus, looting, combat and exterior/roof access.
The prefix to the storage station is 16.125 blocks on this declared route;
the north alternative is assessed separately below.

At the endpoint (14.5,36.5,111.5), the upright box
[14.2,36.5,111.2,14.8,38.3,111.8] clears all captured AABBs. The actor can
stand for interaction on the slab, using source-supported eye offset1.62 and
ordinary three-block reach, then resume the declared crouched return route.
Its eye is (14.5,38.12,111.5). Three distinct aim lines establish source/geometry
access under the declared unlocked ordinary-barrel model:

- Upper barrel (13,38,111): aim (13.5,38.5,111.5), distance1.06977.
  Before entering its east face, the ray crosses only air at (14,38,111).
- Lower barrel (13,37,111): aim (13.5,37.5,111.5), distance1.17661.
  At its east face X14 the ray is Y37.81; preceding Y37/38 cells at (14,111)
  are air. It does not enter the upper barrel first.
- North barrel (13,37,110): aim (13.99,37.85,110.9), distance0.83247.
  At Z111 the ray has X14.075,Y37.895; it then reaches X14 at Z110.911765,
  Y37.855294. The intervening twisting-vine head at (14,37,110) has source
  selection bounds X14.25..14.75,Z110.25..110.75, so the ray passes west of
  that shape before entering the target. Using unequal X/Z aim offsets avoids
  an ambiguous hit exactly on the shared corner of two barrels.

The latter selection bounds come from mapped TwistingVinesBlock initializer
11..30, Block.box(4,0,4,12,15,12), and GrowingPlantBlock.getShape returning that
constant shape. Reproduce with the pinned javap command in the existing
[model-source notes](../model-source/README.md), substituting those class names.
Raw air/plant/barrel states come from the linked immutable block dataset; these
rays are explicit coordinate derivations, not a runtime ray-cast observation.
The already-inspected BarrelBlock.useWithoutItem path has no chest-lid test.
All three ordinary storage barrels are accessible under this model; generated
and acquired loot remain NOT MEASURED. The roof barrel remains a breach case.

The lower furnished living/work area and raised west storage ledge support the
same one-open-plan-room versus two-activity-space sensitivity as the first
house. The south circuit verifies one inter-space connection. The following north-route
check resolves the second link before finalizing the graph; neither connection
is inferred from room or structure-piece counts.

## North connection, graph and depth

The [north circuit](../collision/house2-north-route.json) passes twelve complete
swept segments with the same modeled door opening. Its additional lower-floor
cells (15,33,110/111) and (14,33,110) are full polished blackstone bricks.
The floor button at (15,34,110) has an empty captured collision shape. The
continuous vine column (14,110), Y34..37, has empty collision but source-supported
climbability; it permits the declared climb to feet 36.5 and transfer to the
same storage station at (14.5,36.5,111.5). This is the second validated link.

R1 is the furnished lower interior X13..19,Z110..114 at floor 34. R2 is the
raised west storage ledge X14,Z111..113, bounded by its elevation change,
west storage blocks and open east edge. Under this activity-space definition:

| Metric | Two-space interpretation | One-open-plan-room sensitivity |
| --- | --- | --- |
| Reachable rooms / components | 2 / 1 | 1 / 1 |
| Inter-room links | 2, north and south vines | 0 after collapsing internal links |
| Degree-at-least-three internal room vertices | 0 | 0 |
| Independent room-graph cycles | 1 (two distinct parallel links) | 0 after collapse |
| Deepest room / storage room depth | 1 edge | 0 edges |
| Empty rooms / dead rooms | 0/2 and 0/2 | 0/1 and 0/1 |

The entrance is not counted as another room vertex. R1 offers two alternative
vine choices even though its internal room-graph degree is two. The physical
movement loop remains present under either room-partition interpretation;
collapsing an open-plan room must not imply that the second vine disappears.
R1 has an anvil/work function and conditional bed-use hazard; R2 has three
accessible reward-table nodes, so neither is empty or dead. The one-block-high
roof cavity is excluded from playable-room denominators, not erased from content.

Shortest entry-to-storage distance **among the validated centerline links** is
13.5 blocks north versus 16.125 south. North reaches its vine in ten horizontal
blocks, meeting |19.5-14.5|+|115.5-110.5|=10, then climbs 2.5 and travels 1 on
the ledge. This is not a global sub-block shortest route or the first possible
interaction ray; both values target the identical declared storage station.
Finale distance is N/A because no authored finale exists. Three of four saved
reward-table nodes are accessible in R2 (graph depth 1, or 0 under collapse);
one is in the excluded roof cavity. The 3/4 fraction is nodes, not loot value.
Burial context remains the full-footprint 82-block heightmap offset already
recorded, with an immediate air break above the roof-barrel cover.

The north closed circuit is 27 blocks: 20 upright horizontal, 2 crouched and 5
vine vertical, with no trapdoor step. Feet span, accumulated ascent and descent
are each 2.5 blocks. Its nominal modeled budget is 20/4+2/1.2+5/1=11.666667
seconds; faster 20/5+2/1.5+5/2=7.833333 and slower 20/3+2/0.9+5/0.5=18.888889.
The preserved south circuit remains 32.25 blocks and 17.5 nominal seconds. These
are alternative complete surveys to the same storage station, not repeated
player trials. Opening, menus, pose latency, combat and external approach remain
excluded. No timing model becomes a measured human result by choosing the shorter
route. Empty spawner assignments supply zero resolvable ordinary-spawner attack
workload; natural enemies and actual combat remain NOT MEASURED.

## Connection dimensions, hazards, finale and replay

With only the declared right leaf open, the entry gap at Z115.8125..116 is
X19..19.8125, width 0.8125. The stair at (19,36,115) begins at Y36 over its
eastern half, giving two blocks minimum headroom above floor 34. These dimensions
reuse the retained AABB derivation, not a nominal one-block doorway assumption.

The storage ledge has a one-block support strip X14..15 and an open east drop
of 2.5 blocks to the lower floor. At its slab positions, full beams at Y39 give
2.5 blocks headroom. Over the central lower trapdoor, the west half of the top
stair starts at Y39, giving 2.8125 minimum headroom from floor 36.1875. Crouching
is the declared model pose, not a demonstrated necessity. Each vine supplies a
one-cell (1 by 1 block) climb-support domain with open room-side access, not an
enclosed one-block shaft; a finite wall-to-wall width is inapplicable on the
open sides. At both upper vine positions full Y39 blocks give 2.5 headroom.
Both vertical connections are independently available, so neither is the sole
inter-room bottleneck. Live enemy exploitation is untested and belongs to Item 14.

Meaningful mechanisms evidenced here are optional Nether bed-use explosion and
the ledge's displacement/drop exposure. The former requires bed interaction;
the latter can be avoided by staying on the supported strip. Damage and enemy
behavior were not observed. The unassigned spawners do not establish encounter
pressure. No damaging circuit is evidenced by the buttons/pressure plate alone.

Finale: NONE. Objective clarity, distinctive terminal challenge, terminal reward
linkage and final-room route integration are ABSENT in the inspected fixed house:
the rewards are ordinary storage and there is no separately identified endpoint
mechanism. External reward bypass is CONDITIONAL: the previously measured
three-block roof cover can be removed given roof access, skipping R1/R2 and both
vine routes for the roof barrel. That barrel is not promoted to a finale by its
height. The two ordinary vine approaches are route alternatives, not a reward
reset or proof that any potential natural enemies can be bypassed safely.

Expected replay value is a supported assessment: this fixed variant has a small
route choice via two vines, but no deep branch sequence or distinct finale.
A repeat instance may change terrain overlap and loot-table rolls; the two
empty spawner assignments do not supply enemy-type variety. Persistent revisits
do not restore removed blocks or establish renewable loot. No enjoyment or
actual player replay outcome is invented. Relative to its layered roof and
stacked contents, playable depth is shallow: one open-plan room or two activity
spaces. It is a modest house, not a giant dungeon based on its envelope alone.

## Remaining delivery work

Both fixed Medium House alternatives now have local modeled/inspection quality
assessments. Preserve their different entry states, links, enemy assignments and
conditional roof access. Full runtime actor equivalence, actual interactions,
generated/acquired loot and human times remain outside the observed metrics.
Broader raw-capture custody, all other required families/material variants and
the final review/merge/main delivery gate remain pending. Item 14 is UNSTARTED.
