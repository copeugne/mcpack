# Repurposed Nether temple quality assessment

Status: IN PROGRESS. Five selected fixed alternatives of
`repurposed_structures:temple`. Ocean and taiga remain required separately.
Human timing, realized encounters and acquired loot remain NOT MEASURED.
Current local results: basalt and [crimson](#crimson-complete-local-quality-result)
are integrated; three selected Nether variants and ocean/taiga remain incomplete.

## Bounded group declaration

Selection began2026-09-10 14:29:28 UTC; the exact deterministic selection was
recorded at14:30:30 UTC in [selection](../repurposed-nether-temples-selection.json).
One full occurrence of each Nether root (basalt, crimson, soul, warped, wasteland)
is the existing declared fixed-layout minimum. The existing SHA-256 ID ordering
selects among full candidates without outcome-based replacement. Four roots have
one eligible candidate each; wasteland has four. Same-location cross-repetition
material changes are retained, not counted as independent random layout samples.

Required missing claims are each variant's playable room/connector graph, complete
conditional task and full Item13 quality assessment. Existing
[Item8 source assessment](../../item-8/sources/repurposed-temple-assessment/README.md)
identifies all seven templates, processors, source and loot differences. It cannot
supply measured saved topology or objective costs. Reuse that evidence and the
current selector/extractor, geometry rules and source models. Do not rebuild the
inventory, repeat classification or launch a server.

Smallest deliverable: one integrated comparative report with variant-specific
coordinate bounds, contents, graph/depth/elevation, full task accounting and
hazard/bypass/finale/replay/form assessments. Share verified equivalent geometry
and mechanisms; do not silently copy measurements across material differences.
Every selected alternative must have a full local disposition. No per-door reports
or new generalized measurement framework is required.

The five padded envelopes total38,178 cells, maximum7,938 per case. All required
chunks and named components are present in the accepted assembly index. Use the
existing read-only hash-verified restore, full inventory checks before/after and
POSIX locking. No controlled experiment or new materialization is needed.
Extraction cap:300 seconds total,50 MiB compressed total,1.5 GiB RSS and5 GiB
free-space floor. Analysis/integration cap:90 minutes after read completion;
final focused checks/delivery separately20 minutes. These are stopping budgets,
not measured completion predictions. Desert Mimic's36m20s is a single more
construction-heavy observation, not an assumed rate for this five-case group.
Record phase clocks and overruns; an overrun retains evidence and forces scope/
method reassessment without waiving requirements.

Definitions and sufficient-proof boundaries reuse protocol v2. Freeze the actual
actor, equipment, task start/end, source suppression state, permitted engineering,
phase costs and censoring before any numerical complete-task calculation. Source
potential remains distinct from realized enemies and generated/acquired loot.
Striders and unprovoked zombified piglins do not become hostile combat workloads
merely because a spawner exists. An unresolved material movement or combat term
keeps that task total UNRESOLVED. Model allowances remain approved provisional
sensitivity inputs, not human observations.

Reproduction from repository root (use absent alternative outputs for a rerun):

```sh
uv run python - <<'SELECT'
import importlib,json
from pathlib import Path
roots={'repurposed_structures:temple_nether_'+v for v in ('basalt','crimson','soul','warped','wasteland')}
plan=importlib.import_module('evidence.item-13.select_samples').select_fixed_layouts(roots,'Five fixed Nether temple alternatives; full local quality assessment with material mechanisms retained')
with Path('evidence/item-13/repurposed-nether-temples-selection.json').open('x') as out:
    out.write(json.dumps(plan,indent=2,sort_keys=True)+'\n')
SELECT
for variant in basalt crimson soul warped wasteland; do
  uv run python -m evidence.item-13.measure --fixed-root "repurposed_structures:temple_nether_${variant}" --selection evidence/item-13/repurposed-nether-temples-selection.json --output "evidence/item-13/fixed-blocks/repurposed-temple-${variant}.json.gz"
done
```

## Retained saved inputs

Selection/read phase ended14:31:58 UTC,150 seconds after selection began.
All five extractions passed full inventory checks before/after under the existing
lock. Total extractor27.664694s,22,288 compressed bytes, maximum45,984 KiB RSS.
The selected38,178 cells are retained in the five raw files below. Analysis/
integration deadline is16:01:58 UTC. No runtime remains active.
An initial inspection requested nonexistent key `start`; it failed explicitly.
The retained field is `start_nbt`. A later metadata reader expected automatic
execution-text files, but this extractor prints its metrics to stdout. The actual
returned metrics are transcribed here without rerunning or inventing such files.

| Raw basename (repurposed-temple-) | Seconds | Bytes | Peak RSS KiB | SHA-256 |
| --- | ---: | ---: | ---: | --- |
| basalt.json.gz |5.743230|4204|44496|a6884f33bf59e7a2a6be7e01df478ee5339b47ca7c258d5bf85400b78c1c8341|
| crimson.json.gz |5.412687|4235|44340|4d7415d4c2bfefd2ffc5d588d78d09481f5342c02d1765dd9dd7155c7d085724|
| soul.json.gz |5.116182|3564|43512|6b8e3be9810c21dc65ee687e986a396d0241520b9e3e454b8d7e41bf4a158604|
| warped.json.gz |5.370293|4335|44328|6b3785afcc1214c93ed4221d917f751336cb3ebe3f247c27261d136ac570e71f|
| wasteland.json.gz |6.022302|5950|45984|2a5c34da94b8e21898b2b2f7975869ace309805d0425c7b48be23de8b4f7e100|

| Variant | Saved envelope | Rotation | Reward assignments | Source | Dispensers |
| --- | --- | --- | --- | --- | --- |
| basalt | [394,55,313,405,69,327] | NONE |3 ordinary Quark chests, basalt table |1 magma cube |2 basalt tables |
| crimson | [138,60,57,149,73,71] | NONE |3 ordinary Quark chests, crimson table |1 zoglin |4 crimson tables |
| soul | [394,55,313,405,68,327] | NONE |3 ordinary Quark chests, soul table |1 skeleton |4 soul tables |
| warped | [138,60,57,149,73,71] | NONE |4 ordinary Quark chest blocks with warped tables, plus1 trapped chest with warped trapped table; paired upper blocks require container-union accounting |1 strider |5 wasteland assignments plus1 warped assignment |
| wasteland | [250,28,329,261,41,343] | CLOCKWISE_180 |3 ordinary Quark chests, wasteland table |1 zombified piglin |1 wasteland and2 wasteland_lava tables |

These are saved block-entity assignments, not room counts or acquired rewards.
All listed loot nodes remain unrolled. Each source has Delay20,SpawnCount4,
MaxNearbyEntities6,PlayerRange16,SpawnRange4,delays200..800 and a matching
weight-one potential. No source is inferred from a legacy ID alone. The warped
wasteland dispenser references are preserved literal data, not renamed to fit
the variant. Its paired upper chest blocks must not be priced as two independent
full containers if the saved block states form one double chest.

Wasteland overlaps saved Mega Fortress context: external brewing/enchanting
fixtures and `mns:chests/mega_fortress` nodes occur in its padded extraction.
Those are not silently added to the temple's authored reward count. Actual
terrain/overlap blocks still constrain temple access. No outcome-based replacement
of the selected wasteland occurrence is allowed. The first basalt slice sheet
was visually inspected as a categorical plan; it is not an observed player view.

## Complete objective declaration before timing

For each case, start/end in the middle hall at local(5,4,5), relative to the
lower usable floor and the template's horizontal orientation. Survey both upper
and middle activity areas, reach the lower hall and both reward branches, disable
the authored source, collect all temple chest contents, and return. The warped
upper double chest is one opening/transfer location with two saved loot assignments.
Four other variants have three singles; warped also has two lower ordinary
singles and one trapped single. Bypassing mechanisms by measured breaching is
permitted; source counts and native failures remain baseline observations.
The staged interior boundary excludes finding or excavating to the site.

Actor: one informed adult, full health/food, iron armor and unenchanted iron sword,
diamond pickaxe/axe, shears and sufficient blocks, durability and inventory.
No effects, flight, teleport, critical/sweep attacks, swimming or outside aid.
Use approved A/B/C provisional allowances,20TPS, and actual ordered movement,
source breaking, trap disarming, looting, equipment selection and final verification.
Any required unknown movement/mechanism cost keeps the corresponding total unresolved.

Hostile cases stipulate six initial full-health sources' mobs within their exact-
class nearby cap until the source is removed, then clear all six and any stipulated
splitting descendants. Skeletons are ordinary unarmored adults; zoglins ordinary
adults. Basalt separately models initial magma sizes1,2,4 and the2..4-child split
range. Do not use a single size to stand for all magma outcomes. Striders and
unprovoked zombified piglins have zero required hostile combat in the declared
neutral task; six nearby same-class occupants suppress additional source batches.
Provocation, extra arrivals, a broken suppression condition, fluid/body contact,
trap activation, failed survival or collection outside allowances censor completion.
These are conditional populations, not realized baseline encounters.

Quark chest behavior must be source-checked before applying vanilla lid/drop
rules. Basalt's lava remains a body hazard. For block interactions only, the
actor uses an outline ray with fluid handling NONE: pinned Entity.pick selects
that mode when its fluid flag is false; LiquidBlock.getShape returns Shapes.empty.
This permits a ray across fluid, not walking or collecting items through lava.
The source inspection uses the same pinned SRG and javap as Desert Mimic, with
classes Entity and LiquidBlock. Lava is still excluded by body/foot checks.

## Basalt complete-route integration and model inputs

The ordered basalt circuit passes:110 horizontal steps,7 up and7 down. It surveys
middle/upper levels, breaches the lower source closet, resolves all three chest
nodes and returns. Two carried cobblestone cubes replace lava-floor cells
(396,56,323),(397,56,318); each placement ray hits the visible south face of its
actual northern supporting block. This is earned construction in the model,
not a change to the saved world. No lava floor becomes ordinary walkable terrain
without the declared placed block.

Retained native rejections: the proposed middle detour at(397,61,318) has magma
support; the revised circuit avoids it. The lower western route originally met
lava at(396,56,323), then at(397,56,318). A rejected alternate bridge alignment
would have landed on magma at(397,56,322); it was not accepted. The two final
floor replacements resolve the supported route. Fluid entering the body still
censors the task. A proposed low-wall ray hit the head-level obsidian first;
head-before-foot removal is now explicit. No failed route is overwritten in raw.

The accepted source-closet work removes two unpowered blackstone buttons,
obsidian at(403,58,324), blackstone below, the southern Quark chest, the source,
and an unextended sticky piston above the northern chest. It uses left-button
mining, not control activation. All basalt saved wires are power0 and pistons
unextended. The two attached tripwire crossings are sheared. A zero-power wire
is removed for the conservative passage clearance. The north-cache dispenser
above its chest is removed, giving a clear lid and an interaction ray across
lava without body traversal. Missing lids/blocked rays were not assumed usable.

Pinned Quark JAR SHA-256:
989c465df2e4cb9f602840c2eec143358bf11462cc19dc0b0c7c9f17449e75a5.
VariantChestBlock extends vanilla ChestBlock without replacing lid/drop methods;
VariantChestBlockEntity extends ChestBlockEntity. Their constructors preserve
those mechanisms. VariantChestsModule.setup copies NETHER_BRICKS properties for
nether-brick chests, but CHEST for wood types. Thus basalt's destroyed chest has
hardness2 and effective pickaxe, not wood-chest hardness2.5/axe. The Quark
mineable/pickaxe tag explicitly includes nether_brick_chest; mineable/axe includes
crimson/warped wood chests. The source files/classes are direct immutable artifact
references, not a new captured runtime. No retained Lootr variant is involved.

Before timing arithmetic, basalt work inputs are: two buttons2 ticks each,
obsidian188, blackstone6, Quark nether-brick chest8, spawner19, sticky piston6,
two tripwires0, redstone0, dispenser14. Total245 active ticks (12.25s).
The vanilla extra JAR's pickaxe tag includes piston/obsidian/blackstone/dispenser
and #stone_buttons, which includes polished_blackstone_button. The initial tag
lookup in the SRG JAR failed because resources are in the pinned extra JAR;
that source location is retained rather than inventing direct tag absence.

Use15 interaction starts (11 removals,2 placements,2 opens),3 chest-acquisition
allowances and4H conditional pickup excursion for the destroyed chest. Eight
equipment selections: pick, sword, pick, blocks, shears, blocks, shears, pick.
Combat occurs after source removal. No further batches from that removed source
are included; splitting descendants remain in the workload.
Navigation costs are measured direction changes plus initial orientation and six
phase choices: upper survey, lower source closet, first bridge, northern trap
branch, second bridge and return. Charge14 coupled vertical/horizontal steps at
max(1/u,1/j), replacing their ordinary horizontal cost. Final verification is v.
No provisional model allowance is an observed reaction/menu/pickup time.

MagmaCube.setSize delegates health/size to Slime and sets armor=3*size (bytecode
0..20). Reuse the accepted Slime size-squared health and2..4-child removal split
source in the Slime Cave report. Iron sword base6 with the accepted armor formula
gives5.856/5.28/3.84 damage for sizes1/2/4, requiring1/1/5 full13-tick cycles.
Six initial size1 mobs require3.9s active work; size2 plus descendants11.7..19.5s;
size4 plus descendants42.9..97.5s. These correspond to6,18..30 and42..126 defeated
entities respectively, all one enemy type. The ranges come from stipulated split
outcomes, not probabilities or observed spawn size frequencies. Contact-duty
sensitivity applies to the complete active workload, with pursuit/interruptions
conditional as in the approved model. Zoglin.createAttributes fixes adult health40;
its separate six-adult workload is42 cycles/27.3s, not copied from magma or skeleton.

## Basalt local quality result

Primary activity partition (corridors/stairs are links, not additional rooms):

| Room | Activity envelope and usable floor | Supported content/role |
| --- | --- | --- |
| H, middle hall | X397..402,Z317..322,feet61, with central stair opening excluded | Entry circulation, lower/upper stairs and exposed magma/lava edges |
| U, upper hall | X396..403,Z315..325,feet64, excluding central floor opening | Broad perimeter circulation; lava corners and fall opening; no reward/source |
| L, lower control hall | X395..404,Z320..326,feet57 on checked supported cells | Three-button control wall, western tripwire/lava choke and links to both caches |
| T, northern trap/cache | X395..403,Z314..319,feet57 on checked cells | Tripwire, exposed lava and dispensers, one loot chest |
| D, source closet | X402..404,Z321..324; checked centerline X403,feet57 after declared work | Magma source and two loot chests behind closed masonry/piston mechanism |

Bounds are activity envelopes, not claims that every interior cell is occupiable.
Primary graph has two separate H-U stair links plus H-L,L-T,L-D:5 rooms,5 edges,
one component, two physical degree-three junctions(H,L), one inter-room cycle
and two terminals(T,D). H is the staged entry.
Depths:U/L=1,T/D=2. The lower trap/control split is ambiguous because its narrow
western passage joins both activities. Merging L/T gives4 rooms,4 edges, the same upper-stair cycle and one physical
degree-three junction(H); loot/source allocation is unchanged.
Neither piece count nor empty voxel count produced these partitions.

Empty/dead rooms:0/5 primary and0/4 merged, because every delimited space retains
a route-relevant source, reward or meaningful lava/fall/trigger hazard. Upper and
middle rooms have no reward/enemy source, but are not hazard-free empty rooms.
The upper hall is optional to reward extraction; its exposure and shaft opening
remain supported activity pressure rather than an invented encounter.

Checked connector centers give H-U6H/3V and H-L7H/4V. From L, the existing
flat-grid path finder confirms shortest supported post-work lower-floor routes
of7H to D and16H to T. Thus declared-network reward depth is14H/4V to D and
23H/4V to T, at graph depth2. This is shortest on that fixed room/connector
network, not a minimum over all possible new excavations. Accessible floor span
is57..64 (7 blocks), not the15-layer saved envelope. The complete survey/clear
circuit has7 up and7 down,110H,34 direction changes and41 navigation allowances.

The noncombat totals are77.5/127.75/206.083333s for A/B/C. They include movement
34/53/89.333333s,12.25s mining,15 interactions,8 selections,3 acquisitions and
final verification. Complete conditional times by the initial magma size:

| Size | A | B | C |
| --- | ---: | ---: | ---: |
|1|81.4s|132.95s|213.883333s|
|2, including splits|89.2..97s|143.35..153.75s|229.483333..245.083333s|
|4, including splits|120.4..175s|184.95..257.75s|291.883333..401.083333s|

These are MODELED RESULTS under the predeclared contact and failure conditions,
not calibrated player times or confidence intervals. Counts and numerical terms
are printed by the committed route command. Pickup excursions remain provisional;
failed pickup, source suppression or survival do not disappear from the denominator.

Both lower branches contain one-block-wide route constraints. The western path
crosses two one-cell lava floor gaps before the northern cache; the model places
two full cubes. The center stairs are two blocks wide, with two-block height
constraints at lower transitions. Attached unpowered tripwires intersect both
western/northern routes and feed the dispenser circuitry; the model shears them
before crossing. Dispenser payloads are unrolled tables, so no arrow/lava hit rate
or successful activation is reported. The upper opening is a geometric fall
hazard. Basalt's slow obsidian breach and source suppression add actual declared
work; the three-button control is bypassed, not claimed solved.

All3 chest assignments use the same basalt table:2/3 in D,1/3 in T, all depth2.
Actual loot quality/quantity remains NOT MEASURED. Authored finale: NONE. D is a
terminal source/reward closet, but no boss, unique goal/loot table or completion
trigger is identified. For that terminal candidate, objective clarity ABSENT,
distinctive source challenge PRESENT, reward linkage PRESENT, integration
CONDITIONAL on the declared access work, and exterior exposure UNKNOWN for direct
closet entry. Do not rename the upper room as the finale because it is highest.

Concrete external entry: dry supported stance(406,61,321), through(405,61,321)
and(404,61,321), remove basalt at(403,62,321) then blackstone at(403,61,321),
and continue to(402,61,321). The4H path and both rays pass, bypassing the normal
facade entry into H. It does not skip the lower source or establish direct
outside access to D. No dry supported external stance exists in the padded frame
atY57..60 under the stated conservative rules; this is a finite frame limit,
not proof that distant excavation is impossible. The external head block was
initially assumed blackstone; raw inspection corrected it to basalt before
acceptance. Internal obsidian breach bypasses the control mechanism, with its
cost retained rather than treated as free access.

Expected replay: one fixed internal design, same source/table roles, with
processor material, terrain/lava exposure, source-size/split and loot outcomes
providing conditional variation across sites. These are supported inputs, not an
observed replay preference. Same-site revisits do not restore the broken source,
chest, walls, controls/dispenser or remove the two placed blocks. Loot variation
is not physical dungeon reset. This supports limited authored same-site renewal.

Large/shallow assessment: the three-level facade and perimeter upper room do not
supply three levels of objectives. All reward/source work is in the lower two
branches. The upper level's lava/fall exposure gives it mechanical content, so it
is not simply counted as empty volume. Low objective distribution across height
and concentration below the upper-stair loop are supported weaknesses; a whole-family verdict must
retain all seven variants, including the warped upper reward difference.

## Group overrun and retained crimson geometry

At2026-09-10 16:03:43 UTC the clock showed that the16:01:58 analysis deadline
had passed by105 seconds. Stop expansion under the recovery rule. Analysis elapsed
is5,505 seconds from14:31:58, including source inspection, reasoning, edits and
checks. The group is INCOMPLETE: basalt has a full local result; crimson has a
complete checked route but no accepted total/model/quality synthesis; soul, warped
and wasteland have verified raw observations and source attribution only. Ocean
and taiga remain outside this selected group and still required. This is not a
five-case completion, a new experiment budget or evidence that those cases failed.

Crimson's actual route now passes126 horizontal steps,7 ascent/7 descent,
24 removals and2 ordinary chest openings. The third chest is destroyed for access.
It uses no basalt lava-floor placements. Source geometry requires middle-hall
stem/head-block clearing and the eastern lower staircase; the copied west route
met a solid head cell. The copied middle side extension met an unsupported floor.
Upper northern roof growth blocks a cross-room line, so the complete accessible
upper circuit uses its western/eastern arms and southern connector. These are
saved material differences, not license to copy basalt metrics.

Four pressure plates on the chosen lower route are removed before passage,
along with two tripwire cells, the source, closet/lid blocks and vines. Remaining
plates are still baseline hazards, not claimed globally disabled. The two-part
vine near the northern cache is removed bottom before top from a checked west
stance; no unmeasured wait for a lower vine to disappear is silently inserted.
A duplicate-removal attempt on return was rejected; the declared operation list
now applies each explicit clearance once and validates the return in that state.

Focused outline inspection corrected provisional cell-center interaction targets:
south wall buttons/levers use a point inside their actual outline at localZ.1;
plates and floor wire use localY.03, and attached tripwire usesY.1 within its
1/16..2.5/16 shape. Basalt's counts/times remain unchanged after those corrected
rays pass. Floor-only wire has a one-sixteenth-high outline; "up" wire arms remain
conservatively blocking. Pinned Blocks registration explicitly gives redstone wire
and crimson roots no collision (offsets7162 and32712). This narrow body-rule
extension does not erase wire outlines, pressure-plate triggers or lava hazards.

The concrete remaining crimson claims are its operation-cost/source bindings,
complete phase arithmetic, room/graph/depth/content allocation, external example
and finale/replay/form synthesis. The other three selected variants still require
whole local route/task/quality work. Basalt is the representative complete portion;
do not label the group complete or expand to another family after this overrun.

Reassessment: manual per-obstacle route correction consumed most of this group.
Before another case, inspect whether the existing flat-grid path finder and shared
clearance rules can answer the needed three-dimensional connector queries directly.
Name the exact missing operation and the smallest change in those existing paths;
do not add a generalized world-analysis framework, new evidence schema or another
round of bulk reads. Do not expand implementation without establishing that concrete need. If reuse cannot remove the repeated work, retain an explicit cost
estimate instead of quietly extending this group's cap. Acceptance remains unchanged.

Reproduce current checks:

```sh
uv run python -m evidence.item-13.repurposed_temple_route basalt
uv run python -m evidence.item-13.repurposed_temple_route crimson
uv run ruff check evidence/item-13/repurposed_temple_route.py evidence/item-13/temple_geometry.py
uv run ruff format --check evidence/item-13/repurposed_temple_route.py evidence/item-13/temple_geometry.py
uv run basedpyright evidence/item-13/repurposed_temple_route.py evidence/item-13/temple_geometry.py
```

At commit3fef7579, the crimson command deliberately ended with `RuntimeError`
after printing successful geometry counts. That historical partial result is
superseded by the completed integration below; current crimson execution passes.

Basalt terrain context: all180 saved WORLD_SURFACE columns areY127, the Nether
roof context,70 above lower feet57. This is not70 blocks of solid cover or a
surface-access route. The measured dry side-wall entry atY61 is the local cave
access evidence; actual saved blocks, not this heightmap difference, constrain it.

Source derivations can be reproduced without a server:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -c -p -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar net.minecraft.world.entity.monster.MagmaCube net.minecraft.world.entity.monster.Zoglin net.minecraft.world.level.block.LiquidBlock net.minecraft.world.entity.Entity net.minecraft.world.level.block.TripWireBlock net.minecraft.world.level.block.RedStoneWireBlock net.minecraft.world.level.block.ButtonBlock net.minecraft.world.level.block.LeverBlock net.minecraft.world.level.block.Blocks
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -c -p -classpath downloads/item3/candidates/Quark-4.1-480.jar org.violetmoon.quark.content.building.module.VariantChestsModule org.violetmoon.quark.content.building.block.VariantChestBlock org.violetmoon.quark.content.building.block.VariantTrappedChestBlock org.violetmoon.quark.content.building.block.be.VariantChestBlockEntity org.violetmoon.quark.base.util.BlockPropertyUtil
```

BlockPropertyUtil.copyPropertySafe uses ofFullCopy and adjusts light/spawn/view
predicates, preserving the copied hardness. The resource tags cited above are in
the same-version `server-1.21.1-20240808.144430-extra.jar` and the named Quark JAR
members; the SRG identity is bound by the [prior case](towns-and-towers-desert-mimic-report.md#reproduction-and-focused-validation).
At16:07:54 UTC the focused checkpoint checks passed: basalt full command; crimson
geometry with its expected explicit incomplete-model error; lint/format/types;
coverage arithmetic and all report/index links. Four prior consumers (Desert
Mimic and the three temple checks) produce byte-identical stdout against790aeccf's
helper. Final checks so far took251 seconds after the overrun checkpoint, within
the separate20-minute bound. No five-case acceptance or final Item13 gate is claimed.

Delivery was interrupted before commit. On resumption at17:34:33 UTC, Git verified
that the same candidate remained staged, with no unstaged changes. The20-minute
wall-clock delivery cap was exceeded during this interrupted checkpoint. Do not
count that interval as measured active analysis or claim the delivery budget passed.
Preserve the verified staged result and finish its durable delivery before further
case processing; no new measurements are justified by the interruption.

## Recovery decision and crimson integration declaration

On2026-09-10 17:35:56 UTC, after verified delivery of3fef7579, reassessment
compared analyze_pilot.paths (flat four-neighbor BFS), temple_geometry.path_checks
(body/support/sweep validation), and the existing Basalt/fortress route-adjacency
queries. None automatically resolves mining, partial target outlines, trap states
or room judgment. A new three-dimensional path finder would not supply those
missing claims. Crimson's required route already passes. Decision: add no
navigation machinery and do not repeat its route investigation or raw reads.
Finish the existing result's missing model and quality integration first.

This is a new bounded integration batch, not an extension of the failed five-case
analysis cap:25 minutes through18:00:56 UTC, then10 minutes for focused checks and
delivery. Scope is crimson's existing126H route, source bindings, graph/room
allocation, conditional task and one supported external-access disposition.
No soul/warped/wasteland processing in this batch. All source and geometry inputs
are retained. Only an exact missing external example may need a small query against
the saved blocks; no server or new extraction. Expected new raw storage is zero.

Before arithmetic, use the already declared actor/population and A/B/C allowances.
Crimson work: four stems and two hyphae at8 ticks each with diamond axe; one wart
block at30 ticks with that axe (default speed1, no hoe in the actor's equipment);
two levers at15 ticks each (hardness.5, no effective axe/pick tag); four wooden
plates at2 ticks each; wood chest10; source19; sticky piston6; dispenser14.
The remaining four vine segments, two tripwires and one zero-power wire are
instant-breaking. Total165 active ticks (8.25s). Pinned Blocks offsets9731..9734
and25127..25129 bind lever/wart hardness. The extra JAR's expanded axe/pick/hoe
tags distinguish effective wood tools from the declared default-speed wart work.
Quark wood-chest properties/tags and other source inputs are already bound above.

There are24 mining starts,2 opens, no placements,3 acquisition events and4H of
conditional destroyed-chest pickup. Eight selections: axe; pick for source;
sword; pick for piston; shears for first vine; axe for plates/stems; shears for
northern wires/vines; pick for dispenser. Navigation is actual direction changes
plus initial orientation and six phase choices (upper survey, source closet,
plate field, north-stem breach, vine/cache approach, return). Fourteen coupled
vertical steps replace their ordinary horizontal cost at max(1/u,1/j). Six adult
zoglins give27.3s active combat, divided by the existing contact-duty sensitivities.
No omitted phase is assumed zero; actual player timing and realized encounters
remain NOT MEASURED.

## Crimson complete local quality result

The declared integration now covers every local requirement for this selected
crimson template. The complete task is113.25/182.65/292.516667s for A/B/C.
Movement including conditional pickup is37.2/57/94.666667s; noncombat totals
85.95/146.25/237.916667s. Combat contributes27.3/36.4/54.6s. Counts:126H,
7 up/7 down,47 direction changes,54 navigation allowances,24 removals,2 opens,
8 equipment selections and3 chest-acquisition events. These remain conditional
MODELED RESULTS, not observed player times or guaranteed bounds.

| Room | Activity envelope/usable floor | Content and empty/dead disposition |
| --- | --- | --- |
| H, middle hall | X141..146,Z61..66,feet65; actual openings exclude stem/floor obstructions | Quiet connection to both other floors. Empty, not dead |
| U, upper hall | X140..147,Z59..69,feet68 on the checked southern/western/eastern arms | Roof overgrowth limits northern crossing; central fall opening remains a hazard. Not empty/dead |
| L, lower control hall | X139..148,Z64..70,feet61 on actual supported cells | Lever wall and wooden-plate/dispenser field; links to both lower branches. Not empty/dead |
| T, northern trap/cache | X139..147,Z58..63,feet61 on checked cells | Tripwire, dispenser and one chest. Not empty/dead |
| D, source closet | X146..148,Z65..68; checked centerlineX147,feet61 after work | Zoglin source and two chests behind wood/piston. Not empty/dead |

Activity envelopes are not fully occupiable rectangles. The five-room primary
partition has two H-U stair links and H-L,L-T,L-D:5 edges, one component, two
physical junctions(H,L), one upper-stair cycle and terminalsT/D. The ambiguous
L/T merge gives4 rooms,4 edges, one cycle and junctionH. Empty/dead denominators
are1/5 and0/5 primary,1/4 and0/4 merged. H is a necessary quiet connecting space;
ordinary mineable stem obstruction alone is not called a damage hazard.

The two upper flights occupy different openings and connect across the upper
southern floor. The previously recorded basalt graph had contracted them into
one link, incorrectly losing that cycle. Both actual eastern flights now pass
forward/reverse native checks, from(402,61,320) through(401,62,321),(401,63,322)
to(402,64,323) for basalt, and the translated crimson path through(145,66,65),
(145,67,66) to(146,68,67). The current basalt graph above is corrected explicitly;
its room count, objective circuit, task times and loot/source counts are unchanged.
This narrow correction preserves physical alternatives instead of inflating room
count or starting another route investigation.

Depth from staged H:U/L=1,T/D=2. The checked connector network gives H-U6H/3V,
H-L9H/4V using the east lower stair. The existing flat-grid query confirms L-D7H
and L-T16H on the post-work lower floor. Declared-network reward distances are
therefore16H/4V to D and25H/4V to T, not a global minimum over new excavations.
Floor span61..68 is7 blocks, separate from the14-layer envelope. All180 saved
WORLD_SURFACE columns are127, representing the Nether roof, not66 blocks of
solid cover above the lower floor or a surface approach.

Meaningful hazards: the lower wooden plates and attached tripwire feed actual
saved dispenser circuits. The packaged `loot_table/dispensers/temples/crimson.json`
selects strong-harming tipped arrows (1..2 rolls,5..14 arrows per selected entry);
that is source payload potential, not a realized inventory or hit rate. All four
saved dispenser assignments remain unrolled. The chosen route removes four
plates, two wire cells and the dispenser blocking the northern lid; other triggers
remain hazards. No frozen mechanism is tuned or declared harmless. The upper
opening above(144,64,64) permits a four-block drop from feet68 to the supported
lower stair, unlike ordinary safe level circulation. This is source/geometric
hazard potential, not an observed fall or combat event. There is no lava/TNT in
the saved crimson palette. The two-block-wide stair and one-block-wide lower
clearances constrain movement; this does not establish live enemy pathfinding.

All3 chest assignments use the crimson table:2/3 in D and1/3 in T, all depth2.
Source potential includes ordinary resources/equipment and a rare scrap entry;
no generated item, value or acquisition probability was measured. One hostile
source type is authored, with six adults stipulated only for the complete task.
Other ages or natural spawning are not sampled encounter outcomes. Source failure,
additional arrivals, failed suppression, trap activation, unsuccessful pickup or
survival retain the declared censoring conditions.

Authored finale: NONE. For the terminal D candidate, objective clarity ABSENT
(no unique goal/trigger), distinctive source challenge PRESENT (zoglin source),
reward linkage PRESENT (two containers), route integration CONDITIONAL on the
validated access work, external exposure PRESENT by the direct breach below.
No numerical enjoyment or boss-quality score is manufactured.

External bypass: from supported(150,61,64), mine the head/foot pairs atX149,148,147,
Z64 and walk to(147,61,64). Remove the unextended piston at(147,62,65), then open
the chest at(147,61,65). All seven rays, the3H path and final chest ray pass against
the original saved case. The six wall blocks are five crimson hyphae and one wart
block; the initially assumed all-hyphae wall was corrected before acceptance.
This skips H,U,L,T and the plate field to reach D's reward, but does not suppress
the source or prove combat avoidance. With the declared tools its scoped active
breaking work is76 ticks, plus movement/interaction/collection effort; this is
not a second complete task-time claim. The ordinary closet breach also bypasses
the lever/piston control sequence while preserving its wood/piston breaking cost.

Expected replay: a fixed template with processor/terrain-dependent obstruction
and source/loot outcomes, not a measured distribution of alternative dungeons.
Same-site revisits retain removed source/chest, wood, controls and dispenser;
per-container variation does not reconstruct rooms or reset mechanisms. This
supports limited authored same-site renewal, without inventing player preference.
The multilevel form distributes all rewards and authored combat to the lower
branches; upper circulation and its fall opening add limited mechanical purpose.
This supports shallow objective distribution across height, while the paired
stairs provide a genuine loop. It does not establish the entire seven-variant
family as visually large/shallow; warped's upper chest difference remains material.

Crimson integration and manual slice inspection ended17:45:48 UTC,592 seconds
from the new declaration, within its25-minute cap. This includes source binding,
model/quality integration, the external query and paired-stair correction, not a
new whole-world analysis. The six-layer categorical plan was inspected with:

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/repurposed-temple-crimson.json.gz --output /tmp/item13-crimson-review.svg --layers 61 62 65 66 68 69
convert /tmp/item13-crimson-review.svg /tmp/item13-crimson-review.png
```

The plan supports the recorded northern obstruction and activity-floor comparison;
it is not a human gameplay observation. Both current variant commands, lint,
format and types pass. Final candidate scope/link/diff checks and delivery follow
under the separately declared10-minute bound. The original five-case overrun is
not erased or repriced as this smaller integration interval.
