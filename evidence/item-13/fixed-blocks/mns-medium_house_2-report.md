# Medium House 2: quality assessment

Status: local modeled/inspection assessment and complete conditional timing
recorded. Raw-capture custody is delivered through the linked collision records.
Family repetitions and Item 13 delivery remain IN PROGRESS; no human gameplay is claimed.

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
Raw-capture custody now passes through the linked collision records. Required
family/material repetitions and the final review/merge/main delivery gate remain
pending. Item 14 is UNSTARTED. The complete local timing correction follows.

## Complete four-barrel task and lower roof access

This section completes the local conditional timing model. The previous north
and south times remain movement-only components. Reuse the accepted A/B/C
allowances, existing collision capture and checked north circuit. No new world,
extraction or runtime experiment is needed. Direct block inspection is bounded
by this one roof-access gap, using the retained 8,500-cell input.

Predeclare a three-scaffold branch from the north circuit's lower horizontal
segment. Stop at (17.5,34,112.5). Remove the floor crimson button at (16,34,112),
then place scaffolding at (16,Y34..36,112) on the full polished-blackstone-brick
floor at Y33. The upper two cells are air. Click the base side near its top
rail to extend upward twice, reusing the pinned ScaffoldingBlockItem side-click
rule recorded in the [Nether Tower assessment](mns-nether_tower-report.md#elevated-chest-explicit-scaffold-connection).
Do not substitute top clicks, which request horizontal extension. All three
blocks have distance zero through the supported column. From the adjacent
station, the button center/top and base side are within three-block reach
through otherwise empty body cells. Mine the button without activating it.

Enter the column by walking one block west; climb three blocks to feet
(16.5,37,112.5), standing upright on its top. The complete body is below Y38.8;
saved Y37 and Y38 are air. Mine the stripped crimson stem at (16,39,112) from
below. Its bottom is 0.38 above eye Y38.62. The barrel at (16,40,112) then has
an unobstructed bottom-face ray of length 1.38 through the removed stem cell.
Use the existing unlocked barrel interaction model, which has no chest-lid test.
There is no need to remove the three upper cover blocks or stand inside the
one-block-high roof cavity. The earlier external-roof breach remains an
alternative conditional on reaching the roof; it is not the executed model here.

Descend the same three scaffold blocks and return one block east to resume the
north circuit. Keep the scaffold and breach in place. Crossing the base at feet
Y34 while continuing the lower circuit uses the established scaffold interior
climb/clearance model, not a full solid cube. It does not remove either vine link.
The branch adds two horizontal and six vertical blocks, three placements and
two removals. It adds a reward-interaction station within the existing lower
room, not a third authored room or proof of a roof walking surface.

The full task starts and ends at the existing local entry (19.5,34,115.5):
open the declared right door leaf, inspect and transfer available contents from
all four barrels, and return alive. Use one adult with full health/food,
unenchanted iron armor/sword, diamond pickaxe and three scaffolds, no effects,
flight, healing, additional construction or assistance, full layout knowledge
and 20 TPS. Navigation from outside this local station is excluded explicitly.
Generated items must fit the available inventory; overflow censors this task
instead of inventing unlimited carrying capacity. The worked scenario contains
no natural or other external enemies. Both unresolved-type spawners remain
unchanged; the retained runtime lookup supplies zero resolvable ordinary-spawner
workload, not two enemies to defeat or two mandatory block removals. No realized
encounter or generated inventory is claimed.

Take the roof branch on the outbound north circuit, then complete its existing
three-barrel ledge visit and return. The approved vertical sensitivity rates
1.5/1/0.75 replace the older movement-only vine rates for this complete task;
these are conditional inputs, not calibrated climb observations.

| Cost component | Complete task accounting |
| --- | --- |
| Travel | 22 upright horizontal, 2 crouched horizontal, 11 vertical (5 vine plus 6 scaffold) blocks |
| Decisions | 20: initial door/orientation (1), three lower-floor turns each way (6), vine entry/exit at each end each way (4), ledge stand/crouch choices (2), final entry return choice (1), scaffold construction, entry/climb, mining stop, transfer, descent and route resumption (6) |
| Interactions | 122: four 27-slot menus at 29 operations each (open, 27 conditional transfer attempts, close), one door opening, two removals and three placements |
| Selections | 3: initial pickaxe, scaffold, pickaxe for the overhead stem |
| Acquisition | Four accepted inventory-confirmation allowances, one after each barrel; menu inputs are counted separately |
| Mining | 15 button ticks plus 60 stem ticks = 75 ticks / 3.75 seconds |
| Combat | Zero for the explicitly encounter-free scenario; external mobs invalidate it |
| Completion | One accepted verification allowance; all four transfers and live return required |

Mining uses pinned Blocks.woodenButton strength 0.5 and netherStem strength 2,
called by the crimson-button and stripped-crimson-stem registrations. Neither
requires a correct tool for drops and neither is in the pinned pickaxe mining
tag, so the declared diamond pick has speed 1 for these blocks. Grounded, dry,
unmodified work is ceil(hardness*30)/20 seconds, not diamond speed 8. Source
identity and javap reproduction reuse the [model-source notes](../model-source/README.md).
The pickaxe-tag SHA is e31b952f7df00a46e2e442e601b1139e87085314364e9137381c71e66f55700f.

Complete A/B/C conditional totals are **64.066667 / 116.416667 / 206.972222
seconds**, approximately **64/116/207 seconds**. The long menu budget is explicit;
zero modeled combat does not imply an instantaneous loot clear. Censor on failed
placement or support, obstructed access, interaction/mining delay beyond the
allowances, inventory overflow, death, required healing, unexpected enemies or
changed tick conditions. No success probability or actual player time is inferred.
Four of four saved barrel arrangements now have conditional access. Rewards remain
three on the west ledge and one in the nonplayable roof cavity; this model does
not relocate the fourth reward into a newly invented room. Family repetitions,
other material layouts and Item 13 review/delivery remain pending.

Reproduce the newly inspected cells and complete arithmetic:

```sh
uv run python - <<'HOUSE2_COMPLETE'
import gzip, hashlib, importlib, json
from pathlib import Path
raw = Path('evidence/item-13/fixed-blocks/mns-medium_house_2.json.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'c1fa53cbbae3cc48f56a48baacdfd80746bd937662a57db35d49f98b698447a6'
c = json.loads(gzip.decompress(raw))['cases'][0]
s = importlib.import_module('evidence.item-13.render_pilot').state_at
expected = {33:'polished_blackstone_bricks',34:'crimson_button',
            35:'air',36:'air',37:'air',38:'air',39:'stripped_crimson_stem',40:'barrel'}
for y,name in expected.items():
    assert s(c,16,y,112)['Name'] == 'minecraft:'+name
for y in (34,35):
    assert s(c,17,y,112)['Name'] == 'minecraft:air'
profiles = [('A',5,1.5,1.5,.5,.25,.25,1,2),
            ('B',4,1.2,1,1,.5,.5,2,4),
            ('C',3,.9,.75,1.5,1,1,4,8)]
for name,u,c,v,n,a,s,k,verify in profiles:
    total = 22/u+2/c+11/v+3.75+20*n+122*a+3*s+4*k+verify
    print(name, 'complete encounter-free task seconds', total)
HOUSE2_COMPLETE
```
