# Repurposed Nether temple quality assessment

Status: IN PROGRESS. Five selected fixed alternatives of
`repurposed_structures:temple`. Ocean and taiga remain required separately.
Human timing, realized encounters and acquired loot remain NOT MEASURED.
Current local results: basalt, [crimson](#crimson-complete-local-quality-result),
[warped](#warped-complete-local-quality-result) and
[wasteland](#wasteland-complete-local-quality-result) are integrated; soul and
ocean/taiga remain incomplete.

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

## Warped bounded whole-case declaration

At2026-09-10 17:53:16 UTC, declare45 minutes for the retained warped case's
complete analysis/integration, then15 minutes for affected validation/delivery.
The preliminary raw inspection confirms the existing source differences: an upper
double chest, a lower trapped chest beside TNT, a strider source, warped pressure
plates and floor dispensers. These prevent blindly copying crimson's task. Reuse
the existing ordered operation checker with an explicit warped operation list;
no new navigation framework, raw extraction or runtime. New raw storage is zero.
The required result is one complete local room/graph, objective task, source/loot
allocation and quality/bypass assessment in this comparative report. If unresolved
geometry or mechanism remains at the deadline, retain the partial result and
reassess; do not silently extend the cap.

Actor, A/B/C profiles and complete objective remain the group declaration above.
Use staged middle-hall start/end(143,65,62), survey both other floors, suppress
the source and collect all four logical containers (five loot assignments).
The strider is non-hostile; the scenario imposes no attack task and requires a
clear route, with no natural hostiles or body obstruction. This is zero required
modeled combat, not zero observed entities. Source suppression and looting still
cost time. Destroying the trapped chest rather than opening it is permitted
engineering; source verification of that distinction is required before acceptance.
Conditional pickup adds4H per destroyed container; every movement, removal,
interaction, equipment selection and acquisition remains counted. Unknown material
cost or trap behavior prevents a complete total, rather than silently receiving0.

Crimson's previous validation/delivery finished with fetched head68483571 equal
to upstream and a clean tree at17:51:58 UTC,370s after its17:45:48 integration
boundary, within the declared10-minute final bound.

Warped geometry now passes132H,7 up/7 down with21 removals,3 placements and2
openings. The copied native upper ascent failed at(145,66,65), with air instead
of support. Both would-be stair runs lack intermediate steps; three cobblestone
blocks at(145,65,65),(145,65,66),(145,66,66) construct the eastern link using
verified top/side anchor rays. No repair is claimed for the western flight.
The upper lid slabs are deliberately removed in this circuit; their removal is
not asserted necessary for every possible chest-opening method. Initial center
rays hit the conservative front slab/dispenser obstruction; upper chest and
trapped-chest targets now use actual visible box faces. The floor dispenser was
initially rejected as unlisted support; its inherited full-cube shape supports the
accepted dry standing position. The second tripwire is also sheared before its
vine crossing. Raw attached=true/false differences are preserved.

Before full arithmetic, active mining is105 ticks:2 wood slabs*8,2 wood buttons*2,
4 stem/hyphae blocks*8,2 wood chests*10,source19,piston6,4 wood plates*2;
roots,2 wires and2 twisting-vine cells break instantly. The six equipment selections
are blocks,axe,pickaxe,axe,shears,axe. There are26 interaction starts,4 acquisition
allowances and8H conditional pickup for2 destroyed chests. Count direction changes
plus initial orientation and7 phase choices: stair construction,upper reward,
middle survey,source closet,plate lane,northern cache,return. Use14 coupled
vertical steps and0 required combat; no new speed or inventory calibration.

## Warped complete local quality result

The selected warped occurrence now has a complete local conditional result.
Task A/B/C totals are81.45/138.75/228.25s, including movement39.2/59.5/98s and
active mining5.25s. Required modeled combat is0 in the declared clear-route,
non-hostile-source scenario. This neither counts realized striders nor measures
actual combat/traversal. The132H circuit includes7 up/7 down,38 direction changes
and46 navigation allowances. Its21 removals,3 placements,2 opens,6 equipment
selections and4 acquisition allowances remain explicit. Two destroyed chests add
8H conditional pickup; failed retrieval, unexpected entities, trap activation,
failed construction or survival censor the complete result.

Quark VariantTrappedChestBlock extends ChestBlock, retaining its removal/drop
chain, and getSignal clamps ChestBlockEntity.getOpenCount to0..15. Destruction
of the unopened chest therefore does not supply its opening signal. The existing
[Desert Mimic source derivation](towns-and-towers-desert-mimic-report.md#saved-inputs-and-complete-task-declaration)
binds destruction to potential loot-table unpacking without player context, not
observed contents. The adjacent TNT at(148,61,60) has unstable=false and remains
a baseline opening hazard. No runtime trigger or explosion is claimed.

Pinned source/material checks: Blocks.warped_slab uses hardness2 (offset32905),
warped_button uses woodenButton (offset33384), and warped_roots is instabreak
(offset32180). Expanded vanilla axe tags contain slabs, buttons, plates, stems
and hyphae; the Quark axe tag includes ordinary and trapped warped chests. Both
use the already bound wood-chest properties. DispenserBlock and BaseEntityBlock
have no shape override; BlockBehaviour.getShape returns Shapes.block and its
collision method uses that shape with collision enabled. Blocks' dispenser
registration retains collision (offsets3884..3908). Thus actual dispenser tops
are full support, without treating their contents or behavior as measured.
These are exact artifact inspections under the earlier bound SRG/Quark identities.

| Room | Activity envelope/usable floor | Content and empty/dead disposition |
| --- | --- | --- |
| H, middle hall | X141..146,Z60..66,feet65 on the surveyed perimeter | Quiet connecting space and interrupted upper stair locations. Empty, not dead |
| U, upper reward hall | X140..147,Z59..69,feet68 on checked northern, western and eastern arms | Upper double chest; southern growth interrupts the other landing. Not empty/dead |
| L, lower control hall | X139..148,Z64..70,feet61 on supported cells | Button/piston controls and pressure-plate lane, source-closet access. Not empty/dead |
| T, northern trap/cache | X139..147,Z58..63,feet61 on checked cells | Tripwire, trapped chest, neighboring TNT and dispenser. Not empty/dead |
| D, source closet | X146..148,Z65..68; centerlineX147,feet61 after declared work | Non-hostile strider source and two ordinary chests. Not empty/dead |

These are activity envelopes, not five rectangular walkable boxes. The engineered
objective graph has H-U,H-L,L-T,L-D:5 rooms,4 edges, one component, one degree-three
junction(L), no inter-room cycle and terminalsU/T/D. The H-U edge depends on the
three construction blocks; it is not a native stair measurement. The western
upper flight also lacks intermediate supports and has an obstructed landing.
No second H-U edge is accepted from its surviving top stair. This is a measured
local interruption, not proof that every untested external approach is impossible.
Merging the ambiguous L/T activity boundary gives4 rooms,3 edges, no cycle and
no degree-three junction. Empty/dead fractions are1/5 and0/5, or1/4 and0/4 merged.

Declared graph depth from H is1 for U/L,2 for T/D. Actual constructed H-to-upper
landing route is9H/3V; the upper chest interaction is a further11H along the
chosen perimeter. H-L is9H/4V to(143,61,69) after its stem removal. Existing
flat-floor BFS gives L-D7H to(147,61,66),L-T16H to(145,61,61); corresponding
network distances are16H/4V and25H/4V from H. These are scoped route/network
distances, not global shortest paths under arbitrary excavation. Floors61..68
give7 blocks of progression, separate from the14-layer structure envelope.

Meaningful hazards include8 saved wooden pressure plates,4 upward floor dispensers
and2 other dispenser assignments, the northern tripwire and adjacent chest/TNT.
The declared lane removes its4 plates; the other4 retain their baseline potential.
Both literal warped and wasteland dispenser tables specify strong-harming tipped
arrows,1..2 rolls with5..14 arrows per selected entry. The five wasteland
references are preserved. No generated payload or effective shot count is inferred.
Tripwire attachment differs between neighboring saved cells; this is retained
mechanism uncertainty, not proof of an intact firing chain. The task shears both
crossed cells. Missing upper supports and open floor edges expose falling risk;
construction resolves the selected access, not every hazard in the envelope.
Narrow lower lanes and closet impose one-block clearance, but no enemy pathfinding
or observed chokepoint combat is claimed. No lava is used by this modeled route.

Reward distribution has two denominators: five saved assignments versus four
logical containers. U carries2/5 assignments in1/4 containers (a north-facing
left/right pair atX143/144,Y68,Z62); D carries2/5 in2/4, T carries1/5 in1/4.
Four ordinary assignments use chests/temples/warped, including potential gold,
resources, equipment and rare scrap; the trapped first pool instead contains
fungus,quartz,nuggets and wart blocks. Both include their additional trim/lucky
references. All remain unrolled. Different source pools support a reward-quality
difference, not measured item value, acquired output or probabilities.

Authored hostile enemy count/diversity: zero authored hostile source types; one
authored strider source type. Realized entities, natural hostiles and encounters
remain NOT MEASURED. Authored finale: NONE. D remains a terminal candidate with
objective clarity ABSENT, distinctive hostile challenge ABSENT, reward linkage
PRESENT, integration CONDITIONAL on the breach, external exposure PRESENT. U
provides an additional reward goal and vertical engineering task, so D is not
an exclusive reward climax. No invented player-quality score follows from this.

External vulnerability: the same checked eastern example starts at(150,61,64),
removes six original wall blocks atX149,148,147,Y61/62,Z64, then the unextended
piston at(147,62,65), reaching the ordinary chest at(147,61,65) in3H. The wall is
five warped hyphae and one warped wart block, not copied crimson material. All
seven rays and the supported path pass. This bypasses the hall, upper construction
and plate lane to one reward; it does not complete the four-container objective
or establish actual safety. Scoped active breaking is76 ticks with declared
axe/pick tools. The trapped chest's destruction also bypasses its opening trigger,
while the source-closet breach bypasses the native button/piston puzzle.

Expected replay assessment: the fixed template supports processor/terrain and
source/loot variation, not measured player replay choices. This case's broken
stairs, upper chest and non-hostile source materially differ from basalt/crimson.
Same-site revisits retain3 new supports and21 removals, including the source and
two chests; surviving containers do not reconstruct that work. No player outcome
or random-layout rate is invented. The three-level form has rewards on both
upper and lower levels, so it is not mechanically equivalent to crimson's wholly
lower reward distribution. Nevertheless the quiet middle hall, short branch
depths and absence of authored hostile combat support limited objective variety.
The family-wide large/shallow verdict remains open until all seven variants pass.

Reproduce the current case and inspected categorical plan:

```sh
uv run python -m evidence.item-13.repurposed_temple_route warped
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/repurposed-temple-warped.json.gz --output /tmp/item13-warped-review.svg --layers 61 62 65 66 68 69
convert /tmp/item13-warped-review.svg /tmp/item13-warped-review.png
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar net.minecraft.world.level.block.Blocks net.minecraft.world.level.block.DispenserBlock net.minecraft.world.level.block.BaseEntityBlock net.minecraft.world.level.block.state.BlockBehaviour
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/Quark-4.1-480.jar org.violetmoon.quark.content.building.block.VariantTrappedChestBlock
```

The plan inspection is source/geometric analysis, not a human play observation.

Warped analysis/integration and slice inspection ended18:02:41 UTC,565 seconds
after declaration, within the45-minute cap. This includes the explicit failed
native ascent, construction, source binding, task/quality integration and external
example. No new raw extraction or runtime was used. Final affected validation
and delivery now have the separately declared15-minute bound.

Focused validation passes for the warped complete command, lint, formatting and
types on the changed route and shared helper, coverage arithmetic and current
report/index links. All six prior consumers/results are byte-identical to68483571:
large_hall_down, second ordinary temple, first underground temple, Desert Mimic,
Repurposed basalt and crimson. The shared change only admits actual full-cube
dispenser support; no prior route or model changed. Reproduce the current checks:

```sh
uv run ruff check evidence/item-13/repurposed_temple_route.py evidence/item-13/temple_geometry.py
uv run ruff format --check evidence/item-13/repurposed_temple_route.py evidence/item-13/temple_geometry.py
uv run basedpyright evidence/item-13/repurposed_temple_route.py evidence/item-13/temple_geometry.py
for check in temple_hall_down temple_ordinary_route underground_temple_route desert_mimic_route; do
  uv run python -m "evidence.item-13.$check"
done
for variant in basalt crimson warped; do
  uv run python -m evidence.item-13.repurposed_temple_route "$variant"
done
```

At the warped checkpoint, three of seven alternatives satisfied local scope. Soul and
wasteland then had retained raw but needed full assessments; ocean/taiga required
exact sample matching. No Item13 exit gate or Item14 start is claimed.

## Wasteland bounded whole-case declaration

At2026-09-10 18:05:47 UTC, declare45 minutes for the retained wasteland case's
whole quality/task assessment, then15 minutes for focused validation/delivery.
The exact existing raw hash above passes. No world reads, runtime or new raw
storage are needed. Required missing claims are its rotated playable topology,
complete task and quality/bypass result, preserving the Mega Fortress overlap.
The3 temple chest assignments are separate from4 incidental mns chest assignments
and brewing/enchanting fixtures in the padded raw. Incidental blocks still
constrain clearance; they are not silently removed from the sampled environment.

Use the existing group actor, equipment and A/B/C profiles. Staged start/end is
(256,33,338), with lowerfeet29 and upperfeet36. Survey upper/middle areas, suppress
the source, collect all3 temple chests and return. Zombified piglins are neutral
until provoked; declare an unprovoked, unobstructed scenario with no natural
hostiles or attack task. Required modeled combat is0, not observed enemy absence.
Any aggression, body obstruction, trigger activation, failed pickup or unsupported
movement censors this conditional task. Retain ordinary breaching/engineering
costs. Existing mining/drop and neutral-source evidence suffice; no generic
combat estimate or copied crimson geometry is accepted.

Warped's final delivery was verified at18:05:10 UTC, with fetched80ffc568 equal
to upstream and a clean tree,149 seconds after its18:02:41 integration boundary.
That completed the declared15-minute validation/delivery phase within its cap.

The ordered wasteland circuit passes116H,7 up/7 down,12 removals and2 ordinary
chest openings. Its first upper proposal failed on magma support at(256,35,339)
below feet36. The accepted circuit detours one row north in unrotated template
coordinates, preserving that hazard. The lower lane avoids magma support at
(259,28,331), removes two head-height masonry cells and the west-facing powered
lever at(259,30,336). North-facing closet levers and this west-facing lever use
their actual wall-outline target faces; rotation never changes the saved data.
The other powered lever and extended piston remain baseline mechanism evidence.

Before arithmetic, active mining is118 ticks:3 levers*15 (no effective tool),
5 nether-brick blocks*8,one nether-brick chest8,source19,sticky piston6,one
sheared tripwire0. Use diamond pick throughout except the tripwire, then reselect
pick for the final chest-cover block:3 equipment selections. Count14 interaction
starts,3 acquisition allowances and4H conditional destroyed-chest pickup.
Navigation is actual turns plus initial orientation and6 phase choices (upper
survey,lower descent,closet breach,mechanism lane,cache approach,return).
The14 coupled vertical moves replace their ordinary horizontal term. No other
phase is silently omitted and neutral-source combat remains conditionally0.

## Wasteland complete local quality result

The local complete-task A/B/C totals are71.85/121.9/198.733333s. Movement including
conditional pickup is35.2/54.5/91.333333s; active mining is5.9s. Required combat
is0 only in the declared unprovoked, clear-route scenario. Inputs are116H,7 up/7
down,36 direction changes,43 navigation allowances,12 removals,2 opens,3 equipment
selections and3 acquisitions. They model a complete three-container task, not
actual neutral-mob behavior, clear times or acquired loot. Unexpected aggression,
new entities or mechanism changes outside the declared scenario retain censoring.

Room partition and denominator:

| Room | Activity envelope/usable floor | Content and empty/dead disposition |
| --- | --- | --- |
| H, middle hall | X253..258,Z334..339,feet33 on the surveyed perimeter | Quiet connecting space. Empty, not dead |
| U, upper hall | X252..259,Z331..341,feet36 on the checked perimeter | Exposed magma support and open floor edges. Not empty/dead |
| L, lower control hall | X251..260,Z330..336,feet29 on supported cells | Lever/piston mechanism, magma and source-closet approach. Not empty/dead |
| T, northern-template trap/cache | X252..260,Z337..342,feet29 on checked cells | Tripwire and one chest; dispenser/lava potential. Not empty/dead |
| D, source closet | X251..253,Z332..335; centerlineX252,feet29 after work | Neutral zombified-piglin source and two chests. Not empty/dead |

The source's CLOCKWISE_180 orientation puts the template-north cache at higher
world Z. All bounds are activity envelopes, not fully occupiable rectangles.
Two physically separate native upper stair flights pass both directions and join
across the upper perimeter: H-U twice,H-L,L-T,L-D yields5 rooms,5 edges, one
component, one cycle, physical degree-three junctionsH/L and terminalsT/D. The
second flight is(253,33,336) via(254,34,335),(254,35,334) to(253,36,333).
Merging the ambiguous lower L/T boundary yields4 rooms,4 edges, one cycle and
one junctionH. Empty/dead fractions are1/5 and0/5, or1/4 and0/4 merged.

Graph depths from staged H are1 for U/L and2 for T/D. The checked H-U connector
is6H/3V; H-L is7H/4V to(256,29,331). Existing lower-floor BFS gives L-D7H and
L-T16H, making declared network distances14H/4V and23H/4V to their source/cache
stations. These do not imply minimum routes across arbitrary new breaches.
Vertical progression spans29..36,7 blocks, versus the14-layer envelope. All180
WORLD_SURFACE columns are127, the Nether roof context, not98 blocks of solid
cover over the lower floor. The overlapping fortress limits exterior conclusions.

Meaningful hazards: magma support at(256,35,339) interrupts the upper crossing;
(259,28,331) interrupts a direct lower-lane approach. The accepted detours leave
both intact. Other wall magma and open upper edges are retained environmental
exposure, not measured damage. Two saved dispensers reference wasteland_lava,
whose sole entry is one lava bucket with one roll. Their actual facings are south
at(253,30,337),down at(259,32,336). The third dispenser at(255,30,337) references
wasteland's strong-harming arrow potential. All payloads are unrolled and saved
triggered=false. Lava release/hits are not runtime observations. The lower powered
lever pair and extended piston remain source/geometric mechanism evidence;
removing one lever does not establish that the full puzzle or firing chain was
observed working. One crossed attached tripwire is sheared. Narrow lower lanes
and the one-block closet impose real clearance constraints; no live AI exploit
or combat chokepoint effectiveness is inferred.

There are3 ordinary temple loot assignments, all chests/temples/wasteland:2/3 in
D at depth2 and1/3 in T at depth2. Its source pool includes resources, equipment,
rotten flesh and a rare scrap entry, plus additional trim/lucky references.
Four mns loot assignments elsewhere in the padded extraction are incidental
fortress context and are excluded from the three-temple-container denominator.
The main modeled task changes no incidental reward assignment. Actual/generated
items, value and player acquisition remain NOT MEASURED. Source suppression is
counted, but one neutral source type is not an authored mandatory hostile encounter.

Authored finale: NONE. D's candidate attributes are objective clarity ABSENT,
distinctive mandatory hostile challenge ABSENT, reward linkage PRESENT, route
integration CONDITIONAL on masonry/chest/source work, external exposure PRESENT.
The neutral source in this scenario does not support a fabricated fight or
quality score. Provocation can change its behavior, outside the accepted task.

The external example explicitly includes overlap geometry. The direct copied
crimson start at(249,29,336) is solid, and feet30 there have an incidental closed
top trapdoor overhead. Start instead at supported(248,30,336), outside the temple
envelope but within its fortress context. Mine that trapdoor, then7 masonry
blocks atX250..252,Z336 (Y29..31 forX250,Y29..30 forX251/252), descend one block
and remove the unextended piston at(252,30,335) to open(252,29,335). The4H/1down
path,9 removal rays and chest ray pass against the original saved environment.
Trapdoor removal is a declared operation, not a minimum-break claim.
The first low wall ray hit the actor's supporting floor; targeting the exposed
top of(250,29,336) fixes that ray without deleting the support. This is local
fortress-to-temple access, not an approach from open Nether terrain. It reaches
one reward while skipping H,U,L,T and their mechanisms, not the complete task.
The closed source closet is also bypassable by the main task's mining rather
than operating the lever sequence. No overlap replacement or world tuning occurs.

Expected replay: fixed source design with material and generated-context
variation. The observed overlap can alter approach and available neighboring
activity, but one selected overlap gives no population frequency or player
preference. Same-site revisits retain the12 main-task removals, including the
source and one chest. Other containers/fortress fixtures do not reconstruct the
temple. Its three-level form places all temple rewards and its authored source
in the lower branches; the upper magma/fall hazards and paired stair cycle give
limited upper mechanical purpose. This supports shallow objective distribution
across height, not a claim that the upper floor is mechanically empty. The final
seven-variant family comparison remains open for soul,ocean and taiga.

Reproduce this local result and its inspected categorical plan:

```sh
uv run python -m evidence.item-13.repurposed_temple_route wasteland
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/repurposed-temple-wasteland.json.gz --output /tmp/item13-wasteland-review.svg --layers 29 30 33 34 36 37
convert /tmp/item13-wasteland-review.svg /tmp/item13-wasteland-review.png
```

Reuse the pinned mining, Quark chest, lever-outline and drop sources already bound
in this report. The literal lava table is
`data/repurposed_structures/loot_table/dispensers/temples/wasteland_lava.json` in
the retained Repurposed Structures JAR. No extra source capture is needed to
restate its single JSON entry. The categorical plan was manually inspected as
geometry, not player gameplay.

Wasteland analysis/integration, source/plan inspection and initial checks ended
18:13:24 UTC,457 seconds after declaration, within45 minutes. Final staged review
and delivery retain their separately declared15-minute bound. The complete
wasteland command, lint, formatting, types, scope arithmetic and all current
report/index links pass. Basalt, crimson and warped stdout remain byte-identical
to80ffc568; the shared geometry helper did not change in this batch. An initial
comparison wrapper supplied the wrong script argv; the corrected wrapper used
the repository script path and all three comparisons passed. No raw observation
was affected. Use the preceding validation commands with wasteland added to the
variant loop. Four of seven local alternatives now pass; soul,ocean,taiga remain.
