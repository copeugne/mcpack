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
These are four authored block locations, one resolvable enemy type and three
assignments with no resolvable type, not four realized encounters. The
[frozen-runtime lookup](../collision/README.md#saved-spawner-lookup-result) confirms
that all three empty payloads decode without acquiring a default entity. Their
empty potential lists supply no fallback; the inspected server path returns
before creation. Preserve them as baseline missing assignments, without repair.
Spawn counts, delay and other NBT are retained in the raw dataset. Do not invent default
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

## Route length and conditional traversal time

The [retained route model](../collision/r2-route-model.json) measures a closed
36.25-block inspection circuit: 20 horizontal blocks upright, 10 crouched, 5 on
vines, and 1.25 of explicit trapdoor height adjustments. Feet-height span is 2.5
blocks; accumulated ascent and descent are each 3.125. The nominal rate scenario
produces 20.83 seconds; the illustrative faster/slower scenarios produce 14.42
and 32.78 seconds. All rates, equipment, exclusions and failure rules were declared
in the [route protocol](../collision/README.md#predeclared-route-time-model).

These values are conditional kinematic budgets, not observed gameplay, confidence
intervals, shortest paths or full clears. They exclude combat, activation waits,
interaction/looting time, approach and the roof cavity. The one-versus-two room
sensitivity implies graph depth zero or one for the balcony; shortest spatial
entry-to-objective distance and terrain cover are still unresolved. Sub-block
routes around the lantern were not exhaustively searched: the rejected upright
centerline does not prove that every possible upright crossing fails or that
crouching is mandatory. The accepted crouched circuit is one verified option.

## Encounter component and interaction hazards

The captured [Piglin source](../model-source/captured/world.entity.monster.piglin.Piglin.txt.gz)
assigns 16 maximum health. Under the predeclared ordinary adult, no-armor scenario,
the reused 6-damage iron-sword model takes three 13-tick cycles per piglin. At 20
ticks/second that is 1.95 seconds of reserved attack cycles per successful enemy.

| Successful enemies in the one-wave scenario | 100% contact seconds | 50% contact seconds |
| ---: | ---: | ---: |
| 0 | 0 | 0 |
| 1 | 1.95 | 3.90 |
| 2 | 3.90 | 7.80 |
| 3 | 5.85 | 11.70 |
| 4 | 7.80 | 15.60 |

Derivation for n=0..4: n*ceil(16/6)*13/20; double for the stipulated 50% duty
scenario. This is the explicit piglin-spawner component only. Equipment, attack
conditions and exclusions are in the [model declaration](../model-source/README.md#first-house-piglin-component-and-bed-mechanism).
The saved 733-tick delay corresponds to 36.65 seconds at an ideal 20 ticks/second
once its countdown conditions hold. Do not automatically add it to walking or
attack time, since clocks can overlap. The three empty assignments have no
resolvable enemy potential, so this model now covers the sample's resolvable ordinary-spawner source for one stipulated
wave. Natural population and repeated waves remain outside its scope. Full-clear
time has no finite bound from this model; actual enemies, encounters and combat
times remain NOT MEASURED.

BedBlock's captured source and the packaged Nether bed_works=false setting identify
optional bed interaction in R1 as a conditional explosion hazard. Walking past
beds is not its trigger. Source power 5 and fire-enabled behavior are not measured
blast reach, damage or proof that modded interception is absent. No explosion was
run. Avoiding bed use avoids this particular source trigger. The two unlit saved
campfires are not counted as active fire damage. Spawner pressure remains
conditional on valid activation and successful spawning, not block count alone.

## Empty spaces, finale, bypass and replay assessment

Neither delineated activity space is empty or dead under the protocol: R1 has
an anvil/work function and R2 has two reward-table nodes. Counts are 0/2, or 0/1
when treating both as one open-plan room. The inaccessible roof cavity is excluded
from both numerator and denominator; this does not erase its saved contents.

No distinct authored terminal objective or final activity room is evidenced in
this fixed house. Finale: NONE. Objective clarity and a separate terminal
challenge are absent from the inspected design; balcony rewards are ordinary
storage opportunities. The high barrel does not become a finale by elevation.
Its route integration is absent from the unmodified upright/crouched circuit,
and its roof exposure is conditional on an earned access/breaching capability.

A concrete roof-access scenario has three blocks directly above the barrel at
464,51,432: stripped crimson hyphae at Y52, crimson planks at Y53 and a closed
crimson trapdoor at Y54; Y55..56 are air. Given access to that roof location,
removing those three covering blocks exposes the barrel from above, bypassing
the lower room and balcony. This is a geometric three-block cover measurement,
not a tested mining duration, safe approach or acquired-loot result. Supplying
roof access remains a real prerequisite. It is an earned modification scenario,
not a reason to ban breaching. The one-leaf east-vine opening is another explicit
local modification with the same distinction between source geometry and runtime.

Expected replay value is an assessment: this fixed layout offers little new
route structure on another instance of the same variant, while terrain overlap,
loot-table rolls and potential spawn outcomes can change expedition details.
The second family variant remains separately required. Revisiting this persistent
instance does not by itself restore its physical layout or rewards; no reset or
replenishment was demonstrated. A surviving spawner's repeat-attempt potential
is not a dungeon reset. No player enjoyment or actual replay behavior was measured.

The modest house is mechanically shallow in graph depth under the declared model:
one open-plan space or two connected activity spaces, with no separate finale.
Its layered roof and stacked content positions overstate playable-floor count.
It is not categorized as a giant dungeon from its envelope alone. Full acceptance
of this assessment still requires the unresolved access and movement checks below.

## Concrete unresolved work

Finish actor-context and movement support validation, shortest entry-to-objective
route/terrain-cover measurement, container interaction/opening, and precise
connection widths. Empty-spawner decoding/type disposition is resolved; actual
activation and encounters remain outside the authorized observed metrics.
Roof approach and mining time remain conditional/unmeasured. Preserve the room
sensitivity and modeled-versus-observed boundaries. This report does not claim
final quality acceptance, complete family sampling or review/merge delivery.
