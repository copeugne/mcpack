# Medium House 2: quality assessment

Status: IN PROGRESS. Source and saved-layout findings are integrated below;
playable connections, room counts and traversal are not yet accepted.

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

## Next required measurement

Validate the declared open-state route, lower-floor access, two proposed vine links,
west-ledge support/headroom and ordinary barrel interaction positions. Reuse
existing source and collision machinery only where its input/state assumptions
apply. Declare the actor, route and costs before dependent processing. Then
record room/branch/depth counts, traversal model, hazards/chokepoints, dead/empty
space denominator, finale and replay assessment. Preserve source versus runtime
and modeled versus observed distinctions. This sample does not finish the
family or Item 13, and no Item 14 experiment has started.
