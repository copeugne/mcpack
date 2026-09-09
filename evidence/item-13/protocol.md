# Item 13 protocol

Version: item13-quality-v2, PREDECLARATION IN PROGRESS. No scoring or runtime
experiment is authorized by an unfinished sampling/model section below.
The user-approved method boundary is recorded in [README.md](README.md).

## Complete-objective timing correction

The latest user-authorized steering requires a complete dungeon objective before
timing acceptance. Earlier route calculations remain movement components, even
when labeled conditional traversal or accompanied by a separate combat workload.
They do not satisfy the complete timing requirement. Historical raw protocol
hashes continue to identify v1 and are not rebound to this correction.

Before expanding layout measurements, demonstrate on an existing sample an
objective with explicit start, terminal conditions, actor/resources, navigation
knowledge, encounter state, permitted bypasses and failures. Account for movement,
navigation/decisions, interactions and item collection, mining/breaching, combat,
and required waiting/recovery. Define phases so concurrent activity is not counted
twice. A sequential sum is an explicit scenario, not proof that real play is
sequential. Existing path length may omit pursuit, pickup and mining-position
adjustments; those omissions need their own disposition.

Use source-supported numerical mechanisms where available, declared scenario
assumptions where defensible, and UNKNOWN where neither supplies an estimate.
Known layout can remove search from a stipulated oracle scenario; it does not
measure player navigation or justify zero aiming/menu/decision latency. A fixed
one-wave enemy workload cannot represent a clear while active spawners continue
attempting to spawn. Likewise geometric contact is not item pickup or mining.

If any required cost, lifecycle or objective condition remains unsupported, total
completion time is UNRESOLVED. Do not fill it with a guessed seconds-per-action
constant, treat it as zero, sum incomplete pieces into a total, or report a finite
upper bound. Preserve partial components and their uncertainty. First-clear,
discovery and observed-human claims remain outside the authorized modeled scope.

The [Circle complete-objective demonstration](fixed-blocks/mns-circle_nether_brick-report.md#complete-objective-timing-demonstration-v2)
is the current representative. Its unresolved components block expansion, not
read-only work that resolves this methodological gap. No new framework, world
generation or repeated block audit is justified merely to restate known inputs.

## Population and significance

A significant dungeon family is an accepted canonical family with a provisional
T2/T3/T4 role, an existing S/O shallow-form concern, or source evidence of built
interior/vertical/arena traversal or a material hostile variant that warrants
checking that boundary. This includes negative controls for apparently dungeon-like
forms. Significance is not rarity, footprint size, mod name or Item 12 visibility.
The complete 448-row [intake](intake.json) gives 192 inclusions and 256 exclusions
with existing rationale, ambiguity, roots and dimension evidence. The 18 inactive
Item 8 registry groups remain dispositions, not new active families.

Preserve canonical families. Distinguish a material variant when room connectivity,
vertical access, objective, enemy mechanism, hazard mechanism, reward arrangement
or dimension-specific access changes. Texture/wood/biome-only changes are not new
material variants unless they alter collision, hazard or behavior. Do not infer
equivalence from shared names or equal envelope size. Enumerate root-to-variant
mapping using existing Item 8 sources before sample selection. Random procedural
assemblies are repetitions within a generator design, not infinitely many families.

## Definitions fixed before scoring

- Room: a contiguous playable activity space bounded by authored walls, floor
  changes or a clearly delimited outdoor arena, connected to another space by an
  identifiable doorway, corridor, stair, ladder or other traversable transition.
  Corridors are connections unless they host a distinct delimited activity space.
  Visual decoration, padding, solid mass and inaccessible cavities are not rooms.
  Document ambiguous open-plan partitions and give a sensitivity count rather
  than silently splitting them. Number rooms and retain block-coordinate boundaries.
- Playable: space an explicitly declared actor can occupy/reach under the stated
  collision and movement assumptions. Exact block shapes and doors/stairs/ladders,
  fluids and required mining must be resolved; unsupported shapes remain unknown.
  Validate graph links against actual blocks and at least one complete route.
- Branching: room-graph decision junctions with at least three traversable links,
  along with dead ends and independent cycles. Report reachable rooms, edges and
  components. Jigsaw choices, piece counts and template counts are separate data.
- Vertical progression: connected changes in accessible floor elevation, their
  sequence on the objective route, total ascent/descent and accessible floor span.
- Depth: shortest entry-to-objective graph edges and route blocks; deepest reachable
  graph node; and terrain cover in blocks, reported separately. A bounding-box
  height or source generation depth is not playable dungeon depth.
- Meaningful hazard: a supported damage, displacement, denial or resource-pressure
  mechanism intersecting a required or optional playable route/room. Record its
  trigger, affected route, avoidance and evidence class. TNT/redstone palettes alone
  are hazard ingredients, not confirmed working traps.
- Chokepoint: a constrained traversable connection between activity spaces, with
  measured width/height and alternate-route availability. Mechanical exploitation
  by live enemies belongs to later Item 14, not an inferred observation here.
- Empty room: no supported encounter, hazard, reward, objective or usable facility.
  Dead room: an empty room with no necessary connective or access purpose under
  the declared objective. A quiet connecting/rest space is not automatically dead.
  Report both counts over all delineated rooms, with ambiguous rooms separate.
- Finale: an authored terminal goal/encounter/reward space identified from actual
  source behavior and layout. If none exists, record NONE rather than choosing
  the highest room or furthest box. Final-room quality is a supported assessment
  of objective clarity, distinctive challenge, reward linkage, route integration
  and external bypass exposure, each PRESENT/ABSENT/CONDITIONAL/UNKNOWN with reasons.
  Do not manufacture a numerical enjoyment score.
- Loot distribution: supported reward nodes per room/depth and finale concentration.
  Keep table references and conditional injections separate from generated items
  and player-acquired items. A failed assignment remains a failure, not loot.
- Bypass: a concrete alternative entry or route that skips identified rooms,
  encounters or objectives, with capability, material cost and retained effort.
  External exposure and roof access do not themselves prove a viable bypass.
- Replay assessment: expected variation in layout, routes, objective and encounter
  inputs, plus persistence/reward limits. Distinguish repeat generation from revisits
  to the same persistent dungeon. No observed enjoyment or replay behavior is claimed.
- Large but shallow: a supported contrast between the external architectural form
  and limited playable room/route/objective content. Size alone cannot establish it;
  single-room arenas can be intentional and should be described as such.

## Evidence classes

Keep SOURCE INSPECTION, GEOMETRIC MEASUREMENT, MODELED RESULT, AUTOMATED RUNTIME
OBSERVATION and HUMAN OBSERVATION distinct in every sample. Human traversal/combat
time, realized encounters and player enjoyment remain NOT MEASURED under the
separately approved scope. A saved spawner is not a realized enemy population.
A runtime /place result, if required, is a forced assembly diagnostic, not natural
occurrence or density. Forced and naturally generated samples must remain separate.

## Identity, sampling and experiment gate

Frozen inputs are the exact retained 136-JAR identity and Item 6 configuration
recorded in the [delivered audit](../item-10/cross-item-audit.md#exact-shared-inputs).
Accepted Item 10 worlds contain the explicit generation observer/Chunky overlay;
omit-Sparse controls are contextual evidence, never the pristine retained baseline.
Verify complete restored inventories under the existing Java-compatible POSIX lock
before and after read-only analysis. New controlled experiments require fresh,
hash-verified materialization and the existing readiness, correlated save, clean
stop and complete-process-group failure handling. Never tune the frozen config.

Sampling declaration remaining before measurement: finish the material-variant
mapping, consult Item 7/8 references for the exact 119 Item 10 family gaps, select
baseline-first samples and independent repetitions, and identify incomplete or
boundary-censored geometry. Preserve every attempted sample and do not replace a
failure because another example scores better. No pooled confidence intervals for
purposive designs or repeated blocks/rooms. Family, variant, world and room
denominators must be separate. Source alternatives are not observed probabilities.

For each timing model declare actor count, equipment, movement/mining capabilities,
map knowledge, start/end boundary, objective, encounter/spawner state, permitted
bypasses, failure/censoring and source-supported numerical inputs before computing.
A generic seconds-per-enemy constant without evidence is not an accepted combat
model. Special boss mechanics need their own supported treatment. No dependent
model processing before this section is complete.

## Resource and representative gate

The verified reusable inputs occupy 8,590,500,497 bytes (worlds plus censuses).
The intake observed 42,464,829,440 free bytes. These are availability facts, not
an estimate of the remaining topology or experimental work.

Before expensive processing, quantify selected blocks/regions, retained raw output
and any new materializations from the completed variant/sample set. Use one small
representative with actual room/connector validation, source enemy and loot
attribution, timing-model inputs, full report row and focused checks end to end.
Predeclare its runtime/storage cap before starting. Measure its actual cost before
extrapolating a full-run budget. An overrun, incomplete topology or invalid model
must stop expansion and retain the failure; it must not silently simplify the gate.

The smallest additional experiment is determined by a demonstrated missing family
or material variant after existing Item 7/8/10 coverage is checked. Do not regenerate
accepted worlds or launch a broad new survey. Its exact root, dimension, seed,
placement conditions, repetition count and resource bound must be recorded here
before execution. Full-scale execution is not yet predeclared.

## Frozen representative declaration: small dungeon

The following representative is authorized for execution under the approved method;
unfinished full-matrix sections above still prevent full-scale expansion. It resolves
one complete sample path before expanding machinery or experiments.

Family `betterdungeons:small_dungeon`, root of the same name, Overworld only.
All six authored shell sizes (5x5, 7x5, 7x7, 9x5, 9x7, 9x9 internal nominal labels)
and skeleton/spider/zombie processor themes are included in source assessment.
Do not infer room count from those labels: validate the generated playable floor,
partitions, connections, reward/spawner placement and complete survey route.
Loot-pile alternatives are internal reward/salvage variation, not extra families.

Select two natural baseline cases from the eight accepted Item 10 baseline worlds,
using minimum SHA-256 of `world|overworld|registry_id|chunk_x|chunk_z`, with that
string as tie-breaker. After the first selection, require a different seed role
for the second. Do not select by geometry, loot, enemies or successful traversal.
Retain the selected cases if either fails. Repeated layouts are legitimate results.
Other roots, dimensions and omit-Sparse controls are not pilot substitutes.

Extract saved blocks in each selected envelope plus three blocks on every side,
all block entities within it, the exact start NBT, and WORLD_SURFACE heights above
the envelope. This is sufficient for the compact chamber's internal topology and
local wall access; distant cave connectivity and surface approach are not claimed.
Every extracted chunk must be full and every required block section present.
Verify the complete accepted world inventory before and after, under its POSIX lock.
Keep source inventory, archive, backup, census, producer and protocol hashes.

Actor: one modeled adult player, unenchanted iron sword and pickaxe, unenchanted
iron armor, no buffs, criticals, sweep damage, dual wielding, flight, teleport or
additional building during the internal route. The actor knows the entire sampled
layout and reward/spawner positions. The survey begins at the first interior
standing cell at the declared local entry/breach boundary, visits the spawner and
all retained container interaction positions, and returns to that standing cell.
Record the entry coordinate and any necessary breach separately; survey timing
excludes pre-entry cave search, approach excavation, inventory menus and looting
animation. This is not first-discovery or first-clear player timing.

Use cardinal standing-cell paths verified against actual blocks. Room delineation
and the entry/target cells require manual block-plan inspection before route
calculation. Flat movement cost is distance / 4 blocks per second, with 3 and 5
blocks/second sensitivity scenarios reused from Item 11's explicit modeling
assumptions. These speeds are model inputs, not observed retained-pack movement.
Stairs, ladders, fluids or unsupported collision shapes must have an explicit
movement treatment before use; do not silently pass them as air. Unreachable or
ambiguous routes are censored, not assigned zero traversal time.

Combat uses the [source-supported nominal workload](model-source/README.md).
Declare one activation wave, zero through saved SpawnCount successful ordinary
naked adults, no natural population, jockeys, reinforcement or random equipment
inside this scenario. Source spawner delay and repeated-activation potential are
reported separately. Kill budget starts with the first reserved attack cycle and
ends after the final cycle; count complete 13-tick cycles for each necessary hit.
Show 100% and 50% contact-duty scenarios. No live spawner is disabled or modified:
this is a mathematical one-wave comparison, not a runtime intervention. Outside
this bounded workload, active-spawner clear time is unbounded/UNKNOWN. Model failure
or unsupported enemy identity retains UNKNOWN; never substitute a generic enemy.

Bypass assessment permits ordinary mining, roof/side access and tunneling as
capability scenarios. Give actual wall/cover and objective-distribution evidence;
no cannon, flight, mining-speed or live extraction experiment is claimed. Final-room
and replay conclusions use the definitions above and preserve conditional outcomes.

Pilot budget: at most 10 minutes producer time, 2 GiB working memory and 1 MiB new
compressed raw observation output, with a 5 GiB free-space floor. Two compact
maximal 11x7x11 shells plus a three-block border require at most 7,514 voxel cells
in the envelope extraction; actual saved envelopes must be checked against the
budget before reading blocks. Census reads reuse existing files, no duplicate
worlds or runtime launches are needed. Source capture is separate and already
bounded by the exact listed classes. Record actual time/output size. Stop and
retain an overrun or incomplete sample. Do not extrapolate a full-run budget from
this compact chamber to large procedural dungeons without their own size counts.
