# Towns and Towers Desert Mimic

Status: local declared fixed-case scope satisfied. Item 13 remains IN PROGRESS under the approved
inspection/modeled method. Item 14 remains UNSTARTED. Human timing, realized
encounters and acquired loot remain NOT MEASURED.

## Bounded whole-case declaration

Recovery batch begins 2026-09-10 13:50:23 UTC. Select the single fixed
`towns_and_towers:desert_mimic` family/root `towns_and_towers:mimic_desert`,
Overworld. Its three connected authored components are a design, not three rooms.
The existing candidate/assembly indexes retain two full padded occurrences, both
biome-diverse at chunk(21,17), repeated r1/r2. Use the existing deterministic
SHA-256 candidate-ID order, not an outcome-dependent choice. One complete fixed
occurrence is the declared architectural minimum. No new generation is needed.

Required missing claim: this family has no local quality assessment. Existing
Item 8 source attribution and full saved starts supply the inputs but not playable
topology or complete task timing. Reuse them and the existing fixed selector,
extractor, renderer and geometry/source mechanisms. No new reader or runtime
experiment is needed. Freeze actor/objective details after the actual geometry
is known and before calculating the complete conditional task.

Smallest deliverable is one complete local report covering all Item 13 metrics,
with the actual room/connector graph, full objective, source/enemy/reward allocation,
mechanisms, bypass/finale/replay and explicit uncertainty. Integrate these as one
case, not a sequence of separate doorway reports. Preserve rejected routes.

Resource bounds: 50,922 padded cells, 12 full chunks, one existing region file;
300 seconds extraction,10 MiB compressed output,1.5 GiB RSS,5 GiB free-space floor.
Use full inventory verification before/after and the existing POSIX world lock.
Whole selection/analysis/integration budget is45 minutes wall elapsed from the
clock above; focused validation/delivery separately capped at15 minutes. An
analysis overrun stops expansion for reassessment, preserving supported results
and naming the unmet claim. It does not waive the complete-case gate. Record
phase clocks; extractor runtime alone is not the analysis estimate.

Reproduce selection, with output absent, from repository root:

```sh
uv run python - <<'SELECT'
import importlib,json
from pathlib import Path
select=importlib.import_module('evidence.item-13.select_samples').select_fixed_layouts
plan=select({'towns_and_towers:mimic_desert'},'Single fixed Desert Mimic recovery batch; full local quality assessment required')
with Path('evidence/item-13/desert-mimic-selection.json').open('x') as out:
    out.write(json.dumps(plan,indent=2,sort_keys=True)+'\n')
SELECT
uv run python -m evidence.item-13.measure --fixed-root towns_and_towers:mimic_desert --selection evidence/item-13/desert-mimic-selection.json --output evidence/item-13/fixed-blocks/towns-and-towers-desert-mimic.json.gz
```

For reproduction use new output paths and compare the selection and decoded raw
content against retained files; do not overwrite accepted evidence. Producer and
protocol hashes are recorded by the existing extractor.

## Saved inputs and complete-task declaration

Selection/read phase ended2026-09-10 13:52:23 UTC,120 seconds after the batch
clock. Selected biome-diverse r2; all50,922 cells passed,10.355905 seconds extractor
runtime,45,232 KiB RSS,11,104 compressed bytes. Raw SHA-256:
02a98398ed6deae4c084055a095d2e3d9ed0454a2595beff41278216b7ee884a.
The existing extractor verified the complete accepted inventory before/after.
The six-layer PNG was inspected; it is a categorical block plan, not player vision.

All three saved components use empty processors. Main origin(336,34,272),NONE;
Passage1 origin(335,36,274),CLOCKWISE_90; Passage2 origin(325,35,278),CLOCKWISE_90.
The exact source templates/hashes are the accepted pool trace entries:
`kaisyn:other/desert_temple_mimic/{pyramid_main,passages/passage_1,passages/passage_2}`.
Their respective hashes are893f05da9c8c59fd497651defba0e30d3e8c89918da88cc539e771c7b87da708,
2ca04b8e20b5316fd1501217f1d304f35245cee8c53318bf17d5764c6147d965 and
9b3feedf3168c801cf94f70892804177eaba86405cddfea83c5fa0af20960140.
These bind `t_and_t-neoforge-fabric-1.13.9+1.21.1.jar` members in Item8.

Seven unrolled loot nodes occur: four trapped chests with desert_pyramid at
(344,37,282),(346,37,280),(346,37,284),(348,37,282); three ordinary simple_dungeon
chests at(318,36,282),(324,36,280),(324,36,284). One authored husk spawner is at
(320,36,282),Delay0,Count4,Nearby6,range4,player range16,delays200..800,
explicit SpawnData and empty potential list. The additional husk spawner at
(347,42,269) is outside the component envelope and has different Delay20/current
potential data. It is incidental saved context, not a second authored source.
No template residents occur. Realized enemies remain NOT MEASURED.

Predeclare the complete local objective: start/end at the supported upper-hall
station(344,59,281), survey its accessible activity spaces, reach the lower cache,
acquire available contents of all seven chests and the two authored gold/raw-gold
blocks, disable the authored source, and defeat six stipulated adult husks.
Natural discovery/excavation to this staged interior boundary is excluded and
must stay distinct from burial/external access. No teleport between phases.

Actor: one informed adult, full health/food, unenchanted iron armor/sword, diamond
pickaxe and axe, shears, sufficient carried cobblestone, durability and inventory.
No effects, flight, swimming, external assistance, critical/sweep attacks or healing.
Use20 TPS and the approved A/B/C allowances. The six pre-existing ordinary adult
husks remain within the source's exact-class nearby cap until it is removed,
suppressing additional successful source batches. Extra arrivals, incidental
source successes, reinforcement/conversion, hunger effects, interruption or failed
survival/acquisition censor this scenario. This is not an observed population or
an assertion that the surrounding source cannot activate.

Proposed earned route: remove the seven non-start sandstone/terracotta caps around the
central3x3 shaft and the center blue cap as needed, then place a descending
perimeter staircase of full carried blocks, one block down per horizontal step.
This avoids a22-block free fall and provides the return. Retain the original
start-corner support; validate each actual wall-face placement and subsequent
body sweep. No unsupported dry speed is applied to water.

Remove the center pressure plate without stepping on it. Mine the four trapped
chests with the axe rather than opening them, collecting each before leaving;
this avoids their open-count power input while retaining the TNT hazard below.
Chest.onRemove calls Containers.dropContentsOnDestroy; container getItem unpacks
its loot table with no player. TrappedChestBlock.getSignal depends on open count,
not mining. This supports potential drops, not actual generated/acquired items.
Use the approved four-block conditional pickup-excursion allowance per destroyed
chest/material reward, plus its acquisition allowance; failure to retrieve within
that budget censors completion. Mining is not silently renamed normal looting.

Breach the closed west connection, shear the attached tripwire before crossing,
remove the gold/raw-gold obstruction and candle, reach/disable the husk source,
resolve combat, open the three ordinary chests, then return along the constructed
route. The tripwire shears rule is the existing Basalt source derivation; no trap
activation trial is claimed. Geometry must validate ordered removals, both route
directions, actual target rays and ordinary chest lids before timing acceptance.

Price complete movement, construction, tool selection, decisions, mining,
interactions, conditional pickup/menu transfer, combat and final verification.
The complete graph, task arithmetic and quality assessment belong in the next
integrated result, with retained failures and measured phase time. No separate
per-door deliverables or new runtime machinery are justified.

The complete geometry now passes in operation order, including both tower-niche
landings, all21 individual stair placements,20 removals and three ordinary chest
rays. The original upper straight line met the pillar at(344,59,280); the existing
flat-grid path finder supplies a checked detour. Cap inspection corrected three
orange-terracotta cells that the initial sketch called sandstone. A plate ray
from(347,37,281) met the last placed stair; moving to(346,37,281) resolves it.
The original corner-stair chest station was rejected; the accepted stations use
straight full-height treads. No new collision runtime was required.

The shared check adds only this case's full sandstone/terracotta cubes, straight
sandstone stairs and cave-air recognition. Its existing full-cell conservative
obstacle rule and bottom/straight stair predicates remain. Waterlogged smooth
stairs atY35 support feetY36 on their full-height upper half; all retained body
sweeps stay above the containing fluid cell. This is different from standing
inside water on a half-height slab. No stair is removed and no wet speed is used.
Any fluid arrival into the body volume invalidates the dry task assumption.

Before arithmetic, fix its accounting: upper survey is performed before shaft
cap removal. Subsequent route uses the constructed state; replaying the earlier
survey after removing its floor is correctly rejected. Count actual cardinal
horizontal steps, vertical changes and direction changes in the committed route.
For each simultaneous one-block horizontal/vertical move, charge
`max(1/u,1/j)` once, replacing that step's ordinary horizontal cost. Use the
existing A/B/C controlled vertical rates j=1/.5/.25 blocks/s, as provisional
one-step budgets, not measured jumping. The low-ceiling return step is crouched;
its controlled-step budget includes that posture change. Add24 horizontal blocks
of conditional pickup excursions for the six destroyed reward nodes.

Navigation costs are route direction changes plus initial orientation and seven
phase choices (shaft construction, cache strategy, passage breach, wire crossing,
gold work, source/combat transition, return). Interactions are20 mining starts,
21 placements and three container opens. Nine equipment selections: pick, blocks,
pick, axe, pick, shears, pick, sword, empty hand. Each placement includes deliberate
sneak-use; the last wall face is a trapped chest and must not be opened. Nine
acquisition events cover four destroyed chests, three opened chests and two gold
blocks; final verification is separate. No extra combat movement is charged
outside the accepted contact-duty allowance.

Nominal grounded work: six sandstone-family blocks at3 ticks; four terracotta
at5; plate2; four chests with diamond axe at10; tripwire0; raw gold19; candle3;
gold12; spawner19. Total133 ticks/6.65s, with targeting/input delays charged
separately. These use the pinned block hardness (.8,1.25,.5,2.5,0,5,.1,3,5),
diamond tool speed8 where effective and candle default speed1. The existing
[husk source derivation](mss-desert_pyramid-report.md#side-component-disposition-and-husk-model-inputs)
gives four13-tick sword cycles per ordinary adult (health20,intrinsic armor2):
15.6s active work for the stipulated six. Divide only combat work by duty1/.75/.5.
Provisional allowances and successful pickup/survival remain conditional; no
human duration or guaranteed upper/lower bound is produced.

## Integrated topology, task and quality result

The primary partition has six activity spaces, defined from saved walls, floors,
access and contents. Shaft/passage lengths are connectors, not room counts.

| Room | Bounds/usable floor | Content and role | Empty / dead |
| --- | --- | --- | --- |
| H, upper hall | X339..353,Z274..289,feet59, excluding the separately bounded tower niches | Pillared circulation and access to the capped shaft; no independent reward/enemy/facility | Yes / no, necessary connection |
| L, west tower niche | X337..339,Z273..275,feet59,60,61 at checked stair/landing positions | Optional short stair/landing; higher attempted exit blocked by sandstone at(338,62,276) | Yes / yes |
| R, east tower niche | X353..355,Z273..275,feet59,60,61 at checked stair/landing positions | Optional short stair/landing; higher attempted exit blocked by sand at(354,62,276) | Yes / yes |
| C, lower cache | X344..348,Z280..284,feet37 around the central3x3 floor and four chest recesses | Four trapped desert-pyramid assignments, pressure plate and12 TNT below | No / no |
| T, trap alcove | X327..329,Z281..283,feet37; its connected corridor continues east | Tripwire, adjacent piston/lava mechanism and loaded dispenser; route-relevant trigger space | No / no |
| D, terminal husk chamber | X318..324,Z279..285,feet36; gold threshold atX324..325,Y37,Z282 allocated here | One husk source, three simple-dungeon assignments, gold and raw-gold access rewards | No / no |

Footprints delineate the activity envelope, not every occupiable cell. Columns,
chests, steps and walls within them retain their actual exclusions. H excludes
L/R footprints where their horizontal bounds meet. AtY59 all205 conservative
supported cells in the tested upper rectangle connect; these are navigation
cells, not205 rooms. Both tower stair/landing excursions are checked additionally.
The high air volume above these landings is not another accessible floor.

Primary empty/dead denominators are3/6 and2/6. If the two tower niches are merged
into the upper open-plan activity area, the sensitivity is four rooms,1/4 empty
and0/4 dead. The corridor's repeated widenings remain connectors without distinct
content; they are not invented reward rooms. Both readings retain the same source,
reward and hazard locations and do not alter the complete task.

Contracted primary graph: H-L, H-R, H-C, C-T, T-D. Six nodes, five edges, one
component, one degree-three decision junction(H), no inter-room cycle. L/R/D are
terminal branches; H is the staged entry reference, not a demonstrated exterior
entrance. Room depth from H is L/R/C=1,T=2,D=3. Four containers allocate to depth1;
three containers and two solid reward nodes to depth3. Each of seven container
assignments is counted once, with TNT/dispenser inventory separate.

Using the declared checked connector centerlines, H-C is25 horizontal/22 vertical
blocks, C-T18 horizontal, T-D7 horizontal/1 vertical. Thus H-D is50H/23V,73 route
blocks, on this constructed network. It is not a globally shortest excavation
route. The flat upper entry-to-niche anchors are15H west and17H east; the local
landings add two ascent blocks. Required complete-task progression totals27 up
and27 down:22 each for the central shaft, one each at the gold threshold, and
four each across both tower surveys. Accessible sampled floor span isY36..61,
25 blocks; the35-block component envelope does not imply35 traversed floors.

The complete checked circuit is202 horizontal blocks, including54 moves with
one simultaneous vertical block. There are148 flat steps,66 direction changes,
21 placed cubes,20 removals and44 checked ray events. The three ordinary chests
have air above, no saved Lock/Items and actual inset top-face rays. The four
trapped chests are destroyed unopened. The source-derived chest drop chain
supports this bypass, while retrieval remains explicitly conditional.

`T = (148+24)/u +54*max(1/u,1/j) +6.65 +74*n +44*a +9*s +9*k +v +15.6/duty`

| Profile | Movement including conditional pickup | Active combat / duty-adjusted combat | Complete conditional task |
| --- | ---: | ---: | ---: |
| A |88.4s|15.6s /15.6s|171.900000s|
| B |151.0s|15.6s /20.8s|300.950000s|
| C |273.333333s|15.6s /31.2s|519.183333s|

These are source-supported and provisional MODELED RESULTS, not observed clear
times, expected player times or confidence bounds. Construction, pickup and
survival failures retain the declared censoring conditions. No raw world was
edited, no real mobs fought and no loot rolled or transferred by this analysis.

Meaningful hazards and chokepoints: the center pressure plate is directly over
its supporting block and TNT beneath; source pressure-plate power and TNT
neighbor activation make this an actual trigger arrangement. Three chest
positions also have TNT below their supporting floor. Opening trapped chests
supplies open-count power; the modeled task avoids that input by mining them.
The west chest backs onto a closed piston-connected passage; its exact live
response is not measured, so the accepted route explicitly removes the two saved
blocking masonry cells. The one-block-wide/two-block-high passage arches at
X330/334/338 onZ282 are measured chokepoints. The straight route crosses the
attached wire at(329,37,282); it is sheared before passage. The north mechanism
has two saved lava cells at(328,38,277..278), an extended sticky piston/head and
south-facing dispenser at(328,38,276) with23 arrows. These source-linked hazards
are retained; no arrow-hit, lava-arrival or dynamic trap success rate is invented.
The constructed shaft is a22-block vertical hazard without its earned stair.
A free fall is not substituted for the checked return route.

The authored husk source contributes one enemy type, not one observed encounter.
Its six modeled occupants are a stipulated suppression/clear case. The incidental
northern spawner is retained separately and may activate near this site. Ordinary
natural spawning is not disabled by the empty structure override. Extra encounters
remain excluded/censoring conditions for this numerical case, not claims of safety.

Loot and terminal quality: four desert_pyramid versus three simple_dungeon table
references are potential distributions, not sampled contents or monetary value.
The literal gold is source block(4,2,1) in Passage2, mapping to(324,37,282).
Raw gold is that template's jigsaw final_state at(4,2,0), mapping to(325,37,282),
not an accidental terrain ore. Source JAR SHA-256:
04e3a5f6e9aa83b2f305e836ed6bceb656c7a6cae8d945415fd8d55bc2450696.
The western room is the geometric terminal reward/encounter candidate. No explicit
boss, completion trigger or unique final-loot table is identified. Objective
clarity is ABSENT as an authored quest; distinctive source challenge is PRESENT;
reward linkage is PRESENT as three containers plus the threshold materials;
route integration is CONDITIONAL on the validated breach; external bypass
exposure is PRESENT as the following actual saved boundary route.

External alternative: from(321,36,287), a supported dry cave-edge stance, remove
cut sandstone at(321,36,286) and(321,37,286), then walk two blocks to(321,36,285).
The three-point path and ray to the southeastern chest(324,36,284) pass against
the original saved case with only those two removals. This skips the upper hall,
central descent, main cache and tripwire corridor. Cost includes two sandstone
removals (six nominal active ticks) and2H, plus interaction/collection work; this
is a scoped bypass example, not a second full task-time estimate. It does not
avoid source activation or establish a safe route from a distant surface.
The rejected western stance(316,36,282) had no supporting floor and hanging
pointed dripstone, so a generic two-block west-wall shortcut is not accepted.

Burial/external form:840 saved surface columns spanY58..70. The upper-hall entry
column has topY66, seven blocks above feet59; the western chamber center has
surfaceY69,33 above feet36. These are height differences, not solid excavation
thickness. The central column top isY58, preserving the open overhead architectural
axis; no unobserved roof is invented. The21x21 main pyramid has a broad upper
hall and two tall capped niches; the full40x21x35 assembled envelope includes
underground passages and cannot stand for visible size. The tower niches are
mechanically thin relative to their height. Whole-family "visually large but
mechanically shallow" is not established by that envelope alone: three distinct
content-bearing spaces, traps and earned access work remain. Its low branching
and absence of a multi-floor objective sequence along the22-block shaft are
supported limitations, not a visual-volume quality score.

Expected replay assessment: this fixed three-component design has empty
processors, so no supported alternate internal layout is identified. Other sites
can vary terrain/exposure, spawn success and potential loot. The two indexed
r1/r2 cases at the same seed/location are not independent layout variety. On the
same persistent site, four destroyed trapped chests, the removed spawner/gold,
cut connections and placed stair remain changed; table variation does not rebuild
the dungeon. This supports low authored same-site task renewal, not an observed
player boredom or replay outcome.

## Reproduction and focused validation

Run from the repository root, using the retained extraction and selection above:

```sh
uv run python -m evidence.item-13.desert_mimic_route
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/towns-and-towers-desert-mimic.json.gz --output /tmp/item13-mimic-reproduced.svg --layers 36 37 38 58 59 61
convert /tmp/item13-mimic-reproduced.svg /tmp/item13-mimic-reproduced.png
uv run ruff check evidence/item-13/desert_mimic_route.py evidence/item-13/temple_geometry.py
uv run ruff format --check evidence/item-13/desert_mimic_route.py evidence/item-13/temple_geometry.py
uv run basedpyright evidence/item-13/desert_mimic_route.py evidence/item-13/temple_geometry.py
```

The route command validates the raw hash, ordered operations, positive route,
retained native rejections and external bypass, and prints the complete arithmetic.
The visual source reproduces byte for byte; PNG metadata can differ. The retained
[inspected slice sheet](towns-and-towers-desert-mimic.png) is only a rendering of
those saved blocks, not additional empirical evidence.

Source inspection is reproducible with the pinned local javap and server artifact:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -c -p -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar net.minecraft.world.level.block.TrappedChestBlock net.minecraft.world.level.block.ChestBlock net.minecraft.world.Containers net.minecraft.world.level.block.entity.RandomizableContainerBlockEntity net.minecraft.world.level.block.TntBlock net.minecraft.world.level.block.Blocks
```

Pinned SRG SHA-256 is26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71.
Inspect TrappedChestBlock.getSignal/getDirectSignal, ChestBlock.onRemove,
Containers.dropContentsOnDestroy/dropContents and
RandomizableContainerBlockEntity.getItem. This is the exact drop/power derivation,
not a new runtime trial. Block hardness is in Blocks initialization; effective
tool rules reuse the existing source model. The template members and their hashes
above identify the raw-gold final_state and other authored payloads precisely.

The three existing consumers `underground_temple_route`, `temple_ordinary_route`
and `temple_hall_down` pass with byte-identical stdout against the prior helper
at29a4fa6b. The added support materials do not change their accepted results.
Initial lint found three compound assertions and one precedence-style issue;
these were split/parenthesized and the corrected check passes. Types pass with
zero errors or warnings. No broader runtime or world work was needed.

## Phase clock and local disposition

Selection/read:13:50:23 to13:52:23 UTC,120 seconds. Analysis, integrated report,
and exploratory checks:13:52:23 to14:26:43 UTC,2,060 seconds. Total through the
whole local result is2,180 seconds (36m20s), within the declared45-minute bound.
These are explicit UTC tool readings, including reasoning, edits and tool waits;
they are agent wall elapsed, not human labor or a calibrated family average.
Exploratory route/lint checks are included in that analysis interval. Final
candidate validation and delivery begin14:26:43 UTC, under their separate15-minute
cap. Their end is recorded below after delivery preparation, not inferred from
extractor performance.

All declared local Item13 requirements are addressed for the selected fixed design.
The six-room partition and four-room sensitivity, branching/depth/vertical measures,
full conditional traversal/combat task, source counts/diversity, hazards/chokes,
empty/dead allocation, potential rewards/finale, bypass/replay/form assessments
are integrated above. Raw evidence, failures and model conditions remain explicit.
This is one locally satisfied family scope, not reviewed Item13 completion.

Final candidate checks ended14:28:03 UTC,80 seconds after the analysis boundary.
The route, lint, format and type checks pass. All report/index links and anchors
resolve, scope arithmetic yields19 represented/16 locally satisfied families and
529 remaining case completions, and the whitespace check passes. Re-rendered PNG
pixels match exactly (ImageMagick absolute-error count0); only file metadata differs.
Commit/push/ref verification follows within the separately bounded delivery phase.
The delivering Git commit binds this report, executable route and raw extraction.
