# Explorations Slime Cave

Status: local two-material-state assessment complete; Item13 remains IN PROGRESS.
This assessment uses the separately
approved inspection/modeled scope. Human times, realized enemies and acquired
loot remain NOT MEASURED.

## Scope, source evidence and smallest deliverable

Family/root explorations:slime_cave is included in the accepted population.
Reuse the [coverage](../coverage.md#smaller-temple-tower-and-settlement-scopes),
[custom generator](../../item-8/sources/explorations-slime-cave/README.md) and
[processor attribution](../../item-8/sources/explorations-deepslate/README.md).
The generator selects one15x12x15 cave template with a rotation. This is not a
jigsaw root; its absence from structures in pool-traces-content is expected,
not missing source evidence. The fixed jigsaw selector is inapplicable. Its
custom template is explicitly bound by the accepted inventory/start records.

The template SHA-256 is02f9dc19b1fd4cf766ff772961298ab96049d1353a765889260f0e78953119d3.
Six DATA markers request Slime creation, finalized with STRUCTURE reason and
size nextInt(3)+1. Creation/insertion can fail. One marker requests a slime
spawner with both custom light ranges0..7. One chest assigns
explorations:chests/slime_cave; selected loot-table SHA-256 is
b818aa4f22d55c2065e1eaeb8cb22cdb268e9685ccd697a4f60b22789892a9a7.
The template has no stored entities; marker requests are not realized enemy
counts. The generator has no natural spawn override. Slime size, splitting and
spawner population must have a supported conditional model before combat scoring.

The processor replaces stone with deepslate and mossy cobblestone with tuff only
belowY0. It preserves positions and unrelated blocks, including chest/markers.
These material states can change breach costs but do not by themselves establish
new rooms or families. Use one fully nonnegative and one fully negative saved
assembly to cover both processed materials. Crossing-Y0 cases remain in the
candidate denominator; the source's per-cell threshold explains their mixed
material state without inventing a third template. Reopen sampling if saved
geometry/content contradicts this relationship.

Smallest complete result: saved geometry and source binding for those two states,
room/activity boundaries and validated links; branching, depth and floor changes;
complete conditional traversal/combat tasks with explicit slime descendants;
hazards, chokepoints, dead/empty denominators, loot/finale, external bypass,
replay and large-but-shallow assessments. Apply the existing protocol definitions
before scoring. A single cave template is not proof of one playable room.

The current accepted candidate index contains32 baseline starts. Use the existing
full-start inspection, not a repeated census. Select the lowest SHA-256 candidate
ID within each complete height state, lexical tie break. Analyze the nonnegative
case end to end first, then the below-zero case. This is material-state coverage,
not an independent-seed statistical sample or a distribution estimate. No choice
uses observed dungeon quality or loot outcomes.

Each padded read is7,938 cells; total15,876. Budget120 seconds and2 MiB compressed
per read with5 GiB free. Reuse measure.extract with complete accepted inventory
verification before/after under the POSIX lock. No server, tuning or new generation
is required. Render only after the saved read; inspect actual blocks before the
actor/task and any necessary breach are declared. Preserve identity, missing-chunk,
geometry and budget failures. The first representative must be integrated before
reading the second.

## Selection and first read

[Selection](../slime-cave-selection.json) SHA-256
`dbda68b7d859b391b14df532ca99cafebebf73ead808eded3cb7b65e8c561000`.
There are12 complete nonnegative candidates and8 complete wholly negative
candidates;10 complete candidates cross the material boundary. All32 starts are
SAVED, but only30 have complete required chunks. The two ocean-heavy r1/r2
starts at(-26,-31) have three initialize_light chunks each in their padded
envelope, so remain in the denominator but are ineligible. The precommit identity
check rejected an earlier prose claim of32 eligible; the selection itself correctly
retained30 throughout. Chosen first: ocean-heavy r2 at(5,-23), envelope
[66,0,-368,80,11,-354]. Chosen second: mountainous r2 at(0,-25), envelope
[0,-38,-400,14,-27,-386]. Padded bounds may crossY0 in the first read; the material
stratum is defined by the structure envelope, not padding. Reproduce with the
selection output absent:

```sh
uv run python - <<'PY'
import hashlib,json
from pathlib import Path
from tools.analyze_route_opportunities import read_bound
paths={'candidates':Path('evidence/item-13/candidates.json'),'assemblies':Path('evidence/item-13/start-inspection/summary.json'),'inventory':Path('evidence/item-8/inventory.json')}
raw={k:read_bound(v) for k,v in paths.items()}
root='explorations:slime_cave'
candidates=[r for r in json.loads(raw['candidates'])['candidates'] if r['root']==root]
rows=json.loads(raw['assemblies'])['family_root_dimension_candidates'][root+'|'+root+'|minecraft:overworld']
assert len(rows)==len(candidates)==32
eligible={r['id'] for r in rows if r['start_status']=='SAVED' and not r['incomplete_chunks'] and r['named_components']==[root]}
selected=[]
for state in ('nonnegative','negative'):
 options=[r for r in candidates if r['id'] in eligible and (r['envelope'][1]>=0 if state=='nonnegative' else r['envelope'][4]<0)]
 chosen=min(options,key=lambda r:(hashlib.sha256(r['id'].encode()).hexdigest(),r['id']))
 selected.append({'processing_state':state,'eligible_in_state':len(options),**chosen})
result={'scope':'Two saved material states of one custom cave template; nonnegative representative first','input_sha256':{k:hashlib.sha256(v).hexdigest() for k,v in raw.items()},'candidate_count':32,'eligible_count':len(eligible),'selected':selected,'summary':{'samples':2,'families':1,'voxels_before_block_extraction':sum(r['voxel_count'] for r in selected)}}
p=Path('evidence/item-13/slime-cave-selection.json');assert not p.exists()
p.write_text(json.dumps(result,indent=2)+'\n')
print(hashlib.sha256(p.read_bytes()).hexdigest())
PY
```

First extraction command, retaining source/accepted-world identities and actual
read resources separately from player timing:

```sh
timeout 120 uv run python - <<'PY'
import gzip,hashlib,importlib,json,resource,shutil,time
from pathlib import Path
from tools.analyze_route_opportunities import read_bound
sha='dbda68b7d859b391b14df532ca99cafebebf73ead808eded3cb7b65e8c561000'
plan=json.loads(read_bound(Path('evidence/item-13/slime-cave-selection.json'),sha))
selected=plan['selected'][0]
rows=json.loads(read_bound(Path('evidence/item-13/candidates.json'),plan['input_sha256']['candidates']))['candidates']
case,=[r for r in rows if r['id']==selected['id']]
assert case['bounds']==selected['bounds'] and case['voxel_count']==7938
output=Path('evidence/item-13/fixed-blocks/explorations-slime-cave-nonnegative.json.gz')
assert not output.exists() and not output.is_symlink() and shutil.disk_usage('.').free>=5*1024**3
started=time.monotonic()
result={'selection_sha256':sha,'cases':[importlib.import_module('evidence.item-13.measure').extract(case,voxel_budget=7938)]}
result['elapsed_seconds']=round(time.monotonic()-started,6)
result['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
raw=gzip.compress((json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0)
assert len(raw)<=2*1024**2
with output.open('xb') as stream:stream.write(raw)
print(len(raw),hashlib.sha256(raw).hexdigest(),result['elapsed_seconds'],result['peak_rss_kib'])
PY
```

First saved read PASS:7,938 cells,3,357 compressed bytes,10.371408 seconds,
45,588 KiB peak RSS. [Raw blocks](explorations-slime-cave-nonnegative.json.gz)
SHA-256 `90f69949a5240ddb05c98fd9035d2ea7a456e9d23116377ab7abd5c0a066fef9`.
The full12-layer [view](explorations-slime-cave-nonnegative-slices.png) was
inspected. This is a block-category sheet, not a player screenshot or collision
render. Reproduce without retaining a redundant SVG in ordinary Git:

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/explorations-slime-cave-nonnegative.json.gz --output evidence/raw/item13/slime-cave-nonnegative.svg
timeout 120 convert -background white evidence/raw/item13/slime-cave-nonnegative.svg evidence/item-13/fixed-blocks/explorations-slime-cave-nonnegative-slices.png
```

Saved start: one explorations:slime_cave_piece, CLOCKWISE_90, template origin
(80,0,-368),matching the declared envelope. One saved spawner at(73,3,-360)
has slime SpawnData, both custom light ranges0..7,Delay20,MinSpawnDelay200,
MaxSpawnDelay800,SpawnCount4,MaxNearbyEntities6,RequiredPlayerRange16,
SpawnRange4 and empty SpawnPotentials. This confirms the requested source block
and payload, not actual spawning. Chest(73,4,-360) sits directly above it,
with the expected assigned loot table and saved seed, no Items array. Neither
block entity is evidence of acquired loot or defeated enemies.

Direct inspection of the pinned Explorations archive
420d0373711877a5e1a86b7f9b4f54848f3debb2f116c2509a5cc4eb496c979e and
its template hash above retains slime marker local positions:
(5,2,3),(5,2,10),(9,2,11),(9,3,5),(12,3,3),(1,6,4).
Under saved CLOCKWISE_90, x_world=80-z_local,z_world=-368+x_local.
The corresponding request cells are(77,2,-363),(70,2,-363),(69,2,-359),
(75,3,-359),(77,3,-356),(76,6,-367). These are marker cells, not observed
resident coordinates, successful insertion counts or settled positions.
The spawner/chest marker transformation agrees with their saved coordinates.
The last slime request is high near the chamber boundary; do not assume all six
actors have settled on the same clear floor or are simultaneously within the
spawner's nearby-entity volume.

The saved cavity includes a broad irregular low chamber and upper narrowing air,
with water under parts of the northern floor and outside boundaries. Southern
floor candidates atY1 include stone,slime and moss. This forbids treating the
entire cavity as a flat dry route. A prospective dry local station at(70.5,2,-357.5)
is supported by stone; the central approach can step onto the raised stone at
(73,2,-359) before reaching the spawner/chest. Exact actor sweeps, plant/slime
support handling, source-disable timing and the local start/access limitation
must be declared and checked before any room or complete-task result. No authored
surface entrance or safe distant cave approach is established by this extraction.
The remaining material sample has not been read; the first local assessment
must be completed first.

## Slime source workload before scenario scoring

Use the already pinned mapped server JAR SHA-256
26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -c -p -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar net.minecraft.world.entity.monster.Slime > /tmp/item13-slime.javap
```

Slime.setSize offsets31..41 set maximum health=size squared; offsets75..84
restore health when requested. Slime.remove offsets57..74 choose child size by
integer division by2 and request2+nextInt(3) children, only server-side when
size>1 and dead/dying. Null child creation is skipped. Offsets169..174 set each
child's size and health. Therefore the authored size3 state splits to size1,
not size2. Slime.finalizeSpawn offsets8..56 selects size1<<i for i0..2, yielding
1,2,4 before any caller override. The custom marker handler subsequently chooses
1,2,3; those mechanisms must remain distinct when a spawner scenario is defined.

For an explicitly unarmored, ordinary six-damage fully cooled iron-sword workload,
with every requested split child successfully created and cleared, the source
implies the following attack counts. These are mechanism-derived conditional
workloads, not a complete combat-time result or an observed encounter:

| Initial size | Initial health | Parent attacks | All descendants included, attacks |
| --- | ---: | ---: | ---: |
|1|1|1|1|
|2|4|1|3..5|
|3|9|2|4..6|
|4|16|3|9..23|

The existing13-tick attack-cycle convention multiplies these counts by0.65s of
active work before any combat-duty allowance. Child creation failure, modded
interception, unexpected equipment/effects or environmental death changes this
conditional workload; no probability of such outcomes is claimed. A six-parent
size2 scenario would entail18..30 total attacks including all children, not six
attacks. Actual parents and descendants remain NOT MEASURED. Do not substitute
this source table for actor access, complete traversal/combat accounting or the
saved spawner's repeated-batch timing analysis.

## First local task predeclaration

Actor: one adult, full health/hunger, unenchanted iron armor/sword and diamond
pickaxe, no effects, flight, swimming, building or healing; sufficient durability
and free inventory space for the chest. Known local layout and target positions.
Start/end at(70.5,2,-357.5), a dry station inside the cave's southern perimeter.
This is a local clear/loot task after reaching the chamber, not a measured surface
discovery or excavation route. No authored entrance or external approach is
invented. Unknown external travel is excluded explicitly from this local timing.

Go three blocks east, then step one block north/up to(73.5,3,-358.5), mine the
spawner at(73,3,-360), and return to the start for combat. After clearing the
stipulated parents/children, revisit the same raised station, acquire the chest
contents and return/verify. The chest remains above the removed spawner in the
geometric model; no extra support block is placed. Declare the actual ray/lid
check before treating the chest as accessible. Avoid water and slime-block
support on this route. No source marker position is relabeled a settled enemy.

Worked encounter: six ordinary size2 slimes initially settled at columns/feet
(71,2,-364),(77,2,-363),(69,2,-361),(70,2,-359),(77,2,-359),(75,3,-359),
with X/Z centered in each cell. They must remain in the spawner's nearby-entity
query volume, alive, until disablement. Check their supported geometry and the
query volume. This is an explicit conditional initial state, not six observed
entities or a claim that marker placement guarantees these positions. The nearby
cap must suppress additional spawner insertions before the clear begins; if a
parent leaves the volume or dies early, censor this fixed-six scenario rather
than silently allowing another wave. Natural spawning is excluded.

After disablement, all six parents and their children must engage sequentially
at the dry target station(70.5,2,-358.5), with the actor at the start station one
block south. Slime pursuit/settling into that station is conditional within the
approved combat-duty allowance, not a validated AI route or guaranteed lure.
Each parent produces2..4 size1 children in this scenario, all successfully created
and defeated. Failed engagement, extra mobs, drowning/environmental kills, forced
healing or work exceeding the stated allowances censors completion. No probability
or actual player success is claimed. Validate a size2 target's body, floor and
melee line at that station; smaller children fit within the same envelope.

Use existing A/B/C movement/vertical and analyst allowances. Predeclare11 fixed
decisions: initial orientation,source selection,disablement confirmation,combat
transition,post-combat confirmation,room survey,raised-objective inspection,chest
aim,acquisition check,return selection andterminal condition check. Add one per
upward transition,actual horizontal heading change and each of the six parent
target selections. Descendant switching/pursuit stays in combat duty, avoiding
another per-child charge. Inputs: one mining initiation and one chest open.
Selections: pick then sword. Acquisition: one container; terminal verification:
one. Mining: source-derived1.9s for the spawner with the dry grounded diamond
pick. Count all four legs, not just the first spawner approach. Any different
entry, excavation or additional target work needs a separately declared task.

## First geometric/model result

[Reproduction](../slime_route.py) passes:16 horizontal blocks over four approach/
return legs,4 support-elevation travel(two up/two down),two upward transitions
and seven heading changes. The source/chest station is four horizontal blocks
from the local start and one floor block higher. Route support is dry stone;
no water, slime block, swimming, placement or external excavation is silently
included. Upright support, step envelopes, initial size2 bodies, nearby-query
intersection, both interaction rays/lid space and the fixed melee station pass.
This is GEOMETRIC MEASUREMENT under the declared actor, not recorded gameplay.

```sh
uv run python -m evidence.item-13.slime_route
```

The initial whole-cell avoidance check rejected a size2 body against tall grass
at(78,2,-364). This was a conservative collision proxy, not a solid obstruction.
Pinned Blocks registration offsets19813 and4475 explicitly call noCollission for
tall_grass and short_grass. The checker now ignores those plants only for physical
clearance; interaction rays retain conservative plant avoidance. It does not
silently treat every palette block as air. EntityType's slime registration
(offsets4194..4200) gives0.52x0.52 base dimensions, and Slime.getDefaultDimensions
scales by size, yielding the checked1.04x1.04 size2 bodies. The smaller children
fit within that body envelope. No size3/4 settled-position claim is inferred.

BaseSpawner.serverTick builds the unit source block AABB, inflates it by SpawnRange,
queries the candidate entity class with NO_SPECTATORS, and compares its count to
MaxNearbyEntities (offsets426..503). Here the query box is
[69,-1,-364,78,8,-355]. All six stipulated slime bodies intersect it. At count6,
the code resets the delay and returns without inserting that attempted mob.
Thus the fixed-six task is conditional on retaining those six alive/nearby until
source removal. It is not a universal population cap or a promise that all
source-created slimes stay nearby. Leaving the box, environmental death, missing
parents or additional natural spawning invalidates this particular model.

The saved Delay20 permits an attempt after roughly one second of active ticking;
MinSpawnDelay200 is ten seconds at20TPS. The modeled disablement costs are
D=4/u +1/j +1.9 +4*decision +input +selection, giving6.2/9.9/15.233333s.
The four decisions are initial orientation,source selection,first heading change
and upward alignment. Profile C is beyond the earliest later attempt, so a
single-wave deadline argument would be invalid. The explicit six-nearby condition,
not an invented deadline or ignored spawner, suppresses successful additions
throughout this modeled pre-combat phase. If it fails, use a newly declared
multiwave task rather than retaining these totals.

After removal, the six size2 parents plus2..4 size1 descendants each give18..30
entities defeated and18..30 attacks,11.7..19.5s active work. Six parents are not
six total encounters after splitting. All are one entity type; size/state diversity
is distinct from species diversity. Slime.isTiny returns true at size1 and
isDealsDamage requires a non-tiny slime and effective AI. The children therefore
do not supply the parents' damage pressure, even though clearing them remains
part of this stated objective. Actual spawning, pursuit, splitting success,
damage, loot and combat duration remain NOT MEASURED.

Complete noncombat task is16/u +4/j +1.9 +26*decision +2*input +2*selection
+acquisition +verification. The26 decisions are11 fixed,two upward alignments,
seven headings and six parent target selections. Movement alone is7.2/12/21.333333s.
Combat pursuit/return to the fixed station and descendant targeting remain only
in the approved duty allowance. Chest transfer/menu close is in acquisition.
There is no unpriced healing, excavation or extra wave in the successful task.

| Profile | Noncombat complete budget | With six parents and all children | Active attack work |
| --- | ---: | ---: | ---: |
|A|26.100000s|37.800000..45.600000s|11.7..19.5s|
|B|47.900000s|63.500000..73.900000s|11.7..19.5s|
|C|78.233333s|101.633333..117.233333s|11.7..19.5s|

These are MODELED RESULTS for the declared successful scenario, not calibrated
clear times, survival probabilities or confidence intervals. The active-work
range represents requested child count, not a measured run distribution. Initial
marker sizes1/2/3 and spawner size mechanisms retain their separate source
workloads above; this worked complete task specifies size2 instead of inventing
an average size or assuming a large slime fits every marker location.

## First room, quality and access assessment

The inspected sections show one irregular cave activity space around the central
source/chest, with low floor changes and an upper narrowing vault of air. The
structure extent66..80 / -368..-354 is only its search envelope; it is not fifteen
rooms or225 playable floor cells. The dry validated activity core and objective
approach lie around70..73 / -359..-358 at feet2/3. Walls and the broad connected
interior do not divide this into a corridor tree. The raised three-block stone
objective area is a local pedestal, not a distinct enclosed chamber. Primary
count: one room,one component,zero room edges,zero branch junctions,zero cycles.
Counting that pedestal as a second activity zone yields two nodes/one transition,
still zero branching. Room-graph objective depth is0(primary) or1(zone sensitivity);
shortest checked station distance is four horizontal blocks. The validated floor
span is one block, not the twelve-block template height.

Empty/dead rooms are0/1: the space has a source-supported slime encounter and
reward. There is one saved chest-table assignment above the one spawner. Its
contents are not generated by this analysis. Finale is a compact central objective,
not a separate terminal room or bespoke boss. Objective linkage/integration is
PRESENT, conditional on finding the chamber; distinctive terminal enemy/challenge
is ABSENT and unique terminal reward value is UNKNOWN. One assigned table does
not demonstrate superior items, guaranteed progression or reset behavior.

The active spawner and splitting parents supply conditional combat pressure;
the hollow does not have source evidence of a trap sequence. Water beneath the
northern/side floor creates optional wet movement/mining exposure, and slime-block
surfaces are avoided by the dry task. No drowning, knockback, bounce damage or
live chokepoint exploitation was observed. The raised objective approach is
locally constrained by its pedestal, but the broad room is not an enforced
one-door combat choke. No source-authored maze or gated vertical progression is
supported by these blocks.

A separate source/geometry check passes the chest ray before removing the spawner.
Thus loot access does not require completing the modeled disable/kill objective;
a player who tolerates the encounter can use the same local station. This is a
concrete bypass opportunity, not measured player success. The shell uses ordinary
mineable stone/moss materials, with no demonstrated protected gate. External
excavation/roof breaching remains available in principle, but the unseen approach
and total excavation cost are not invented. At the central columnY11..14 are
saved solid stone, while WORLD_SURFACE is62. At the local start,Y9..14 are stone
and WORLD_SURFACE is also62. These are verified local cover minima and heightmap
context, not proof of a continuous solid column through the unextracted interval.
There is no demonstrated natural exterior doorway or timed outside-to-loot route.

Expected replay assessment: one selected template and rotations/stone replacement
provide placement variation, while size/split state changes encounter composition.
The first case does not establish a new-room progression loop. Removing the
spawner permanently removes that local source in the modeled task; per-player
loot machinery does not prove physical restoration or renewed same-player loot.
Player enjoyment/revisit behavior is NOT MEASURED. Its tall hollow has one compact
objective with one-block validated progression, supporting a mechanically shallow
cave-form assessment. It is underground; no above-ground visual landmark or human
visual prominence is claimed.

The first material representative now has its local task and quality assessment.
Focused route, interaction, body/query and arithmetic checks pass, with Ruff
format/check and basedpyright clean. Proceed to the preselected negative case,
preserving its actual saved terrain/materials instead of copying these metrics.

## Negative material-state read

The first representative passes its local assessment. Execute the second already
selected case under the same120-second,2-MiB,5-GiB-free and identity boundaries.

```sh
timeout 120 uv run python - <<'PY'
import gzip,hashlib,importlib,json,resource,shutil,time
from pathlib import Path
from tools.analyze_route_opportunities import read_bound
sha='dbda68b7d859b391b14df532ca99cafebebf73ead808eded3cb7b65e8c561000'
plan=json.loads(read_bound(Path('evidence/item-13/slime-cave-selection.json'),sha))
selected=plan['selected'][1]
rows=json.loads(read_bound(Path('evidence/item-13/candidates.json'),plan['input_sha256']['candidates']))['candidates']
case,=[r for r in rows if r['id']==selected['id']]
assert case['bounds']==selected['bounds'] and case['voxel_count']==7938
output=Path('evidence/item-13/fixed-blocks/explorations-slime-cave-negative.json.gz')
assert not output.exists() and not output.is_symlink() and shutil.disk_usage('.').free>=5*1024**3
started=time.monotonic()
result={'selection_sha256':sha,'cases':[importlib.import_module('evidence.item-13.measure').extract(case,voxel_budget=7938)]}
result['elapsed_seconds']=round(time.monotonic()-started,6)
result['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
raw=gzip.compress((json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0)
assert len(raw)<=2*1024**2
with output.open('xb') as stream:stream.write(raw)
print(len(raw),hashlib.sha256(raw).hexdigest(),result['elapsed_seconds'],result['peak_rss_kib'])
PY
```

Negative read PASS:7,938 cells,3,394 compressed bytes,28.778387 seconds,
48,656 KiB peak RSS. [Raw blocks](explorations-slime-cave-negative.json.gz)
SHA-256 `f8856e2278ea08228569af7757ee8f12849cd1a38010e8f9f04c19212034f3bb`.
Saved origin(0,-38,-400),rotationNONE,one cave piece; source at(8,-35,-393)
and chest at(8,-34,-393). The spawner retains the same Delay/count/range/custom
light settings, and the chest retains the same table with its own saved seed.
The full12-layer [view](explorations-slime-cave-negative-slices.png) was inspected:
water remains below part of the floor, and saved exterior air interrupts some
side/upper boundary geometry. Do not assume identical surrounding cover.

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/explorations-slime-cave-negative.json.gz --output evidence/raw/item13/slime-cave-negative.svg
timeout 120 convert -background white evidence/raw/item13/slime-cave-negative.svg evidence/item-13/fixed-blocks/explorations-slime-cave-negative-slices.png
```

Predeclare the same local task in the corresponding template coordinates, then
validate it against these saved blocks. From first-case block coordinates(x,y,z),
the negative-case mapping is(z+368,y-38,-320-x). For continuous points it is
(z+368,y-38,-319-x), accounting for rotated cell centers/boundaries. The local
start becomes(10.5,-36,-389.5), objective station(9.5,-35,-392.5). Keep the same
actor, six-size2 conditional encounter, removal objective, four legs, targeting,
acquisition and censoring rules. Check actual deepslate/tuff support rather than
assuming it from the processor's name. Counts/times may be carried over only if
the transformed support, sweeps, source/query and interaction checks pass.

## Negative-case result and material comparison

The transformed route, initial size2 bodies/query, spawner/chest access and melee
station pass on the hash-bound negative saved input. Reproduce with:

```sh
uv run python -m evidence.item-13.slime_route --negative
uv run python -m evidence.item-13.slime_route
```

The first support whitelist rejected the transformed parent station because its
floor at(7,-37,-389) is gravel, not the predicted stone/deepslate pair. Direct
saved inspection shows deepslate immediately beneath atY-38 and again atY-39.
Accept that supported full gravel surface explicitly; do not replace the saved
gravel with assumed processor output. The checker requires stone/deepslate beneath
any admitted gravel support. This is a corrected over-restrictive support test,
not an erased physical obstruction or a claim that every saved cell follows only
the template processor. No block was changed in the actual world.

The validated local task retains16 horizontal blocks,four elevation travel,two
upward transitions and seven headings. Start feet-36,raised station-35. The
nearby query is[4,-39,-397,13,-30,-388]. Both the source payload and conditional
six-parent population contract remain identical. No new mining of the harder
shell is required by this local task, so source-disable costs and the complete
conditional model reproduce the first totals exactly:38..46/64..74/102..117s
rounded across A/B/C. This is a measured equality of the declared route/model
inputs, not a claim that all blocks, loot or real encounters are equal.

One authored chamber,zero primary branching and zero empty/dead rooms remain
supported. The raised objective is again one local pedestal within that space,
with the same two-zone counting sensitivity and four-block station distance.
Depth0(primary)/1(zone sensitivity) and one-block floor span are local task
metrics. The low/high marker placement and the narrowing upper hollow do not
supply a second authored objective floor. The negative sample retains the same
single authored chest over the spawner, source hostility, conditional finale
linkage and direct-chest-access bypass. Spawner removal is not a loot-open gate.
These are family-owned content counts; adjacent contributions are retained below.

The surrounding geometry differs materially. At(14,-392) and(15,-392), saved
cellsY-38..-32 are air, then tuff begins atY-31. This documents an opening toward
external cave space near the east boundary. It does not prove a supported walk
across that opening or a safe drop: no floor is present at those cited levels.
The central source column has tuffY-27..-24 and WORLD_SURFACE94; at the start
column(10,-390), tuff beginsY-29 and WORLD_SURFACE is62. Retain these local solid
cover minima and heightmap context separately from unknown continuous overburden.
Neither result supplies a surface-to-chest mining total or observed discovery.

The retained volume also contains four treasure=true,waterlogged=false
Supplementaries urn blocks at(-3,-30,-390),(-1,-29,-394),(-3,-29,-393),
(2,-28,-391). The first three lie in padding outside the authored template
footprint; the fourth is within its envelope near the upper western edge.
The Slime Cave template does not author urns. Report this adjacent generated
reward potential instead of declaring the whole retained volume contains only
one reward. None is a new Slime Cave chest or proof of a second authored room.
Their collection is outside the explicitly declared source/chest clear task;
no route, acquired contents or complete surrounding-cave clear is claimed.

Pinned supplementaries-neoforge-1.21.1-3.6.8.jar SHA-256
0dd0445af35aa15ad012833c4b8024d2ed70320d1ace0316d2f5b684b06a997d,
UrnBlock.newBlockEntity offsets0..27 returns null for treasure=true. Thus their
absence from saved block_entities is consistent with source, not proof of an
empty reward. Its blocks/urn loot table, SHA-256
7ebcd614eebf70ab6c2473638152b3296ef521ab6091968b7bdc0f788bdd5e52,
includes a treasure-state-conditioned reference to
supplementaries:loot/urn_loot/urn_loot. This is loot potential; no items were rolled
or acquired. Source command:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -c -p -classpath downloads/item3/candidates/supplementaries-neoforge-1.21.1-3.6.8.jar net.mehvahdjukaar.supplementaries.common.block.blocks.UrnBlock > /tmp/item13-urn.javap
```

Biomes O' Plenty hanging-cobweb/webbing states also occur in the retained surrounding
and upper cave. The checked local task does not traverse them. No slowdown,
entanglement or player outcome is inferred solely from the block names. Water,
slime-block surfaces and the external drop retain their route exclusions. The
source-supported slime/spawner pressure and clearly available direct loot bypass
remain the assessment's supported mechanics.

The paired result supports one fixed cave objective with different placement,
processing and surrounding content. Expected replay remains a source-supported
assessment of encounter size/splitting and placement variation, not guaranteed
reset or enjoyment. Both cases are mechanically shallow in their family-owned
room/vertical progression despite the taller hollow. Incidental urns and external
caves do not justify erasing those limits or claiming the entire surrounding cave
has been measured. The two material states are covered locally; mixed-Y0 processing
is explained by the accepted per-cell source and is not another authored layout.

Local family assessment complete under the declared modeled/inspection scope.
Both saved inputs and views, source mechanics, local topology/depth, complete
conditional tasks, enemy distinctions, hazards/chokepoint limits, loot/finale,
bypasses, external exposure and replay/shallow-form findings are retained. Full
Item13 population coverage and review/merge gates remain IN PROGRESS.

Focused final checks: both route modes pass; the original nonnegative output is
byte-identical to pushed af8ba7f4 after adding negative-case support. Ruff format/
check, basedpyright and git diff --check pass. No runtime, frozen configuration
change, repeated survey generation or Item14 work was performed.
