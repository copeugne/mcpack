# Medium House 1: developing quality assessment

Status: IN PROGRESS. This is one selected fixed Nether layout, not completion of
its family coverage or Item 13. Evidence classes below are deliberately separate.

Sample: `full-ordinary-r1-baseline|minecraft:the_nether|mns:medium_house|29|27`.
[Saved blocks](mns-medium-house.json.gz), [selection](../fixed-moog-selection.json),
[collision capture and limitations](../collision/README.md),
[standing](../collision/r1-standing.json) and
[crouching](../collision/r1-crouching.json) bind the accepted world and runtime.
No new dungeon world was generated for this sample. The collision probe used the
saved view in a fresh runtime. Human traversal, combat and acquired loot remain
NOT MEASURED.

## Activity spaces and connections

The declared actor is upright 0.6 by 1.8, crouching to 1.5 on the balcony. It knows
the layout, uses the saved-open right-hand entrance and west twisting vines,
and makes no block changes. Source-supported climbing and static empty-context
collision are model assumptions; this is not an observed player trial.

Two activity spaces are identifiable under the protocol's floor-change rule:

- R1: lower living/work space, approximately X461..467,Z430..434, floor top Y45.
  Three two-block beds occupy the north edge; an anvil and other fixtures occupy
  the southwest edge. Beds and decorations subdivide movement, not separate rooms.
- R2: narrow raised storage balcony along Z431, X462..466, with stored contents
  immediately north at Z430. Slab floor top 47.5 falls to 47.1875 at the central
  closed trapdoor. This floor change and storage function distinguish R2. Because
  it overlooks R1 without a full dividing wall, report a room-count sensitivity
  of one open-plan room versus two activity spaces, not an invented exact count
  insensitive to the definition.

The [crouched route](../collision/r2-route.json) is collision-free over all sixteen
complete swept segments, starting/ending at 467.5,45,435.5. The west vine column
at 461,431 is continuous at Y45..47 and supplies the vertical link to the balcony.
The earlier [upright attempt](../collision/r1-route.json) is rejected: the soul
lantern at 464,49,431 obstructs that crossing. Static standing endpoints alone
would not have validated the motion. Crouching clears the lantern without removal.

The east vine at 467,431 is enclosed at lower level by a wall north, solid blocks
east, and overlapping brimwood leaves west/south at Y46. It is not a second
unmodified lower-room entrance. In the declared model the R1-R2 graph has one
verified connection, zero degree-three junctions and zero independent cycles.
Breaking the leaf block at 467,46,432 is a concrete conditional second connection
from the lower room; its lower block is air and its floor is solid. This is a
one-block modification scenario, not an observed mining time or a forbidden bypass.

The cavity at Y51,Z432 contains spawners at X462 and466 and a barrel at 464.
Its two intervening air cells at X463 and465 have full roof blocks at Y52, leaving
one block of headroom. It does not qualify as an upright/crouched activity room
or a final room. Reaching it by breaching/crawling is a separate capability case.
Walkable roof surfaces and surrounding natural vegetation are not automatically
additional authored activity spaces.

## Contents, rewards and current quality implications

Four saved spawners are present: one explicit piglin assignment on the balcony
at 465,48,430 and three empty entity assignments, each with empty SpawnPotentials.
These are four authored block locations, one explicitly named enemy type and
three unresolved operational assignments, not four realized encounters. Spawn
counts, delay and other NBT are retained in the raw dataset. Do not invent default
pigs, guaranteed spawning, a live enemy population or a combat duration.

There are three saved reward-table nodes, with no generated item inventory shown:

| Position | Location | Table potential |
| --- | --- | --- |
| 463,49,430 | Balcony storage | mns:chests/uncommon |
| 466,48,430 | Balcony storage | mns:chests/houses |
| 464,51,432 | One-block-high roof cavity | mns:chests/empty |

The reused [Item 8 packaged catalog](../../item-8/sources/packaged-json-redacted.json.gz),
archive MoogsNetherStructures-1.21-3.0.0-alpha.2.jar, contains the three exact
`data/mns/loot_table/chests/` paths. The table named empty is not empty: its pool
has 2..4 rolls, an empty entry of weight 8 and nine item entries with total weight31,
including nether wart, gold nuggets and blaze powder. The houses/uncommon tables
have separate pools for supplies and rarer materials/equipment, including ancient
debris or netherite scrap. These are packaged opportunities, not generated or
acquired rewards; conditions, stack counts, injections and access must be retained
in any later quantitative loot model. Filename semantics are not reward evidence.

The two campfires at 467,48,430 and465,49,430 are saved unlit. Do not count them as
active fire damage. Bed use in this Nether dimension, spawner activation and other
possible interactions still require their specific mechanism assessment before
hazard scoring. The hanging lantern is a measured clearance restriction, not a
damage hazard or evidence about enemy pathfinding. Those combat tests remain Item 14.

The form contains a populated lower space and a narrow elevated storage ledge,
plus a roof cavity that lacks standing headroom. It must not be scored as several
full dungeon floors merely from the stacked spawner/container heights. Whether
it meets the final large-but-shallow assessment remains tied to the complete
access, hazard, reward and traversal analysis.

## Concrete unresolved work

Finish actor-context and movement support validation; measure the declared route's
length, depth and conditional time; inspect container interaction/opening and
roof breaching costs; resolve empty spawner behavior and the piglin combat model;
complete meaningful hazards, dead/empty-room dispositions, finale and replay
assessment. Preserve the one-versus-two open-plan sensitivity. This report does
not claim final quality acceptance, full family sampling or review/merge delivery.
