# Basalt Chambers: two-assembly quality assessment

Status: IN PROGRESS. This report is the authoritative local family deliverable.
Both selected assemblies and all central material outcomes now have local
modeled assessments and verified diagnostic custody. Full Item13 coverage and
final delivery remain pending. Item 14 is UNSTARTED.
Apply the approved Item 13 definitions and modeled/inspection boundary.

## Existing evidence and predeclared sample

The [coverage scope](../coverage.md#adorabuild-variant-scope) requires two assemblies
from distinct seed roles for this procedural family. Both already exist in the
accepted baseline: biome-diverse r2 start(0,-31), ordinary r2 start(10,-9), Nether.
The existing assembly index marks both SAVED with complete padded chunks and all
seven named components. No new generation, runtime experiment or repeated start
inspection is needed. Sample both eligible cases; order by padded voxel count,
then canonical candidate ID, so the25,584-cell biome-diverse case is the small
representative. Finish its full assessment before extracting the55,614-cell case.
These two selected assemblies are not an unbiased frequency or uncertainty sample.

[Selection](../basalt-chambers-selection.json) binds the existing candidate,
assembly and pool-trace inputs. The missing pool `minecraft:basalt_chambers/chambers`
remains a frozen source defect, not permission to repair generation. Named component
coverage is an input, never a substitute for rooms or playable connections.

Minimum deliverable: both saved layouts, actual room/activity boundaries and graph,
vertical/route/burial depths, complete conditional traversal/combat tasks, authored
sources/diversity, mechanism-level hazards/chokepoints, dead/empty denominators,
resource distribution/finale, external bypass costs and supported replay/shallow-form
assessment. Material conditions include center ancient-debris processing and trap
magma/TNT processing. Inspect the actual saved outcomes before deciding whether an
additional minimal material experiment is needed. Preserve unavailable variants
explicitly rather than assuming that component names establish their outcomes.

The exact packaged seven7x7x7 templates are already hash-bound in Item 8's
pool-trace template_contents records. All have empty authored-entity lists and no
container loot references. The spawner template has one blaze source at local(3,3,3),
Delay0, SpawnCount4, Min/MaxSpawnDelay200/800, RequiredPlayerRange16,
SpawnRange4, MaxNearbyEntities6 and empty SpawnPotentials. This describes potential,
not four realized blazes. Saved spawner count/state and interaction distances are
still needed before declaring a phase-aware workload. Reuse the already inspected
blaze source rather than reopening Item 14 combat tests.

Extraction budget:81,198 padded cells total, with only25,584 authorized for the
first representative increment;120 seconds per extraction,20 MiB compressed output
per case,5 GiB free floor. The existing accepted-world extractor supplies complete
pre/post hash inventory checks under the Java-compatible POSIX lock and retains
actual blocks, block entities, surface data and start NBT. Existing small captures
took roughly5..7 seconds, but that does not predict this two-region read. Record
actual duration/size. No server is started. Corrupt/missing chunks or identity
mismatch fail the read and preserve the failed output; do not silently widen bounds.

Timing will retain the approved actor, equipment and A/B/C assumptions. Define
entry/objective/exit, route, navigation knowledge, permitted breaching, source
activation and failure/censoring before calculating times. Human observations,
realized enemies, generated/acquired loot and player outcomes remain NOT MEASURED.

## Reproduction

Selection uses the existing selector and both complete candidates, without adding
a second sampling implementation. Executed construction:

```sh
uv run python - <<'PY'
import importlib, json
from pathlib import Path
m = importlib.import_module('evidence.item-13.select_samples')
root = 'adorabuild_structures:basalt_chambers_large_1'
plan = m.select_fixed_layouts({root}, 'Two complete distinct-seed Basalt Chambers assemblies; smaller representative first')
base = plan['selected'][0]
rows = [r for r in json.loads(Path('evidence/item-13/candidates.json').read_text())['candidates'] if r['root'] == root]
assert len(rows) == 2 and len({r['seed_role'] for r in rows}) == 2
plan['selected'] = [{**base, 'candidate_id': r['id'], 'bounds': r['bounds'], 'voxel_count': r['voxel_count']} for r in sorted(rows, key=lambda r: (r['voxel_count'], r['id']))]
plan['summary'] = {'samples': 2, 'families': 1, 'voxels_before_block_extraction': sum(r['voxel_count'] for r in rows)}
Path('evidence/item-13/basalt-chambers-selection.json').write_text(json.dumps(plan, indent=2) + '\n')
PY
```

Executed representative extraction command:

```sh
timeout 120 uv run python - <<'PY'
import gzip, hashlib, importlib, json, resource, shutil, time
from pathlib import Path
from tools.analyze_route_opportunities import read_bound
m = importlib.import_module('evidence.item-13.measure')
selection_hash = 'eaa4ba0ea4db159f926e85f6367fffd0209bc4be8617fedbaafe7f6ed8157ca3'
plan = json.loads(read_bound(Path('evidence/item-13/basalt-chambers-selection.json'), selection_hash))
chosen = plan['selected'][0]
rows = json.loads(read_bound(Path('evidence/item-13/candidates.json'), plan['input_sha256']['candidates']))['candidates']
case, = [r for r in rows if r['id'] == chosen['candidate_id']]
assert case['bounds'] == chosen['bounds'] and case['voxel_count'] == 25584
output = Path('evidence/item-13/fixed-blocks/basalt-chambers-biome-diverse-r2.json.gz')
assert not output.exists() and not output.is_symlink()
assert shutil.disk_usage('.').free >= 5 * 1024**3
started = time.monotonic()
result = {'selection_sha256': selection_hash, 'cases': [m.extract(case, voxel_budget=25584)]}
result['elapsed_seconds'] = round(time.monotonic() - started, 6)
result['peak_rss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
raw = gzip.compress((json.dumps(result, sort_keys=True, separators=(',', ':')) + '\n').encode(), mtime=0)
assert len(raw) <= 20 * 1024**2
with output.open('xb') as stream:
    stream.write(raw)
print(len(raw), hashlib.sha256(raw).hexdigest(), result['elapsed_seconds'], result['peak_rss_kib'])
PY
```

## First saved input and material/source integration

The representative extraction now passes in10.14308 seconds with46,704 KiB peak
RSS:25,584 cells,10,546 compressed bytes, SHA-256
c51074175f8e721caad92936f701a8d8259f940804378931ef7cbd36dddaf2c0.
Raw input: [biome-diverse r2](basalt-chambers-biome-diverse-r2.json.gz). Its15 saved
jigsaw components are assembly records, not15 rooms. All occupy envelope Y12..18;
the later route section resolves its playable elevations and connections.

One saved blaze spawner at(25,15,-485) retains the declared Delay0 and source
parameters, with no other block entity in the padded view. The structure definition
has empty spawn_overrides. Source residents are empty, source diversity is one
explicit hostile type, and realized population remains NOT MEASURED. No container
loot references are authored by the selected components, and no saved container
block entity is present. Resource objectives still require attribution/access.

The central component's reward at(-3,15,-499) and the trap component's reward at
(-3,15,-485) are ancient debris. Three additional debris blocks inside the total
assembly envelope at(-12,14,-500),(2,15,-504),(17,18,-481) are not those authored
reward positions. Do not count envelope-wide resources as authored dungeon loot
without source attribution. The trap has TNT, six tripwire blocks and four hooks;
no magma block remains in the saved palette. Trigger connectivity and a safe route
must be checked before calling this a meaningful hazard.

Packaged processor `randomize_ancient_debris` (SHA-256
70391b1196aae8513a97a40641214bc44e8d02262f29f809abe1346ad13d1b87)
uses ordered .2 netherite-block and .1 lodestone random matches, otherwise retaining
debris. These are source probabilities, not observed frequencies. Additional
material coverage depends on the second saved center and other existing evidence.
`replace_magma_with_tnt` (SHA-256
6e4ad76ca77c73c12d058a374242fda501b7d02f4457b64bffc1f707f89484b4)
is an unconditional block-match replacement. Magma is therefore not a separately
random generated trap alternative under this selected pool element. Do not add an
unnecessary magma experiment. The structure definition (SHA-256
64914f6f1e735a1de80255bd3501a6072bce5c9294ae31769869ce0200e50652)
uses jigsaw size6, start-height13 and bury adaptation, with the unchanged missing
pool reference retained through its component source. These source settings are
not observed dungeon depth or room count.

Read these exact entries from the accepted Adorabuild jar under
`data/adorabuild_structures/worldgen/processor_list/` and `worldgen/structure/`;
reuse the pinned jar identity from the adjacent Adorabuild reports. The raw
start_nbt/Children records bind each template, processor, rotation and box.

Next bounded view: render the existing seven envelope layers with the established
slice renderer, at most120 seconds and20 MiB combined SVG/PNG. These are block
plans, not player screenshots. Inspect boundaries, passages, support and headroom
before assigning rooms or computing traversal. The larger second case stays deferred
until this representative is integrated end to end.

The [seven-layer block sheet](basalt-chambers-biome-diverse-r2-slices.png) is now
rendered and inspected (SVG2,927,729 bytes; PNG62,947 bytes), below20 MiB. An
initial PNG conversion attempted an unavailable cairosvg module and failed before
writing PNG; the existing ImageMagick path then succeeded. No dependency was added.

```sh
timeout 120 uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/basalt-chambers-biome-diverse-r2.json.gz --output evidence/item-13/fixed-blocks/basalt-chambers-biome-diverse-r2-slices.svg
timeout 120 convert -background white evidence/item-13/fixed-blocks/basalt-chambers-biome-diverse-r2-slices.svg evidence/item-13/fixed-blocks/basalt-chambers-biome-diverse-r2-slices.png
```

The sheet exposes five chamber-shaped air volumes centered at X/Z(-3,-499),
(11,-499),(-3,-485),(11,-485),(25,-485). It also reveals an important connectivity
limit: passage_2 midplanes at(4,-499),(-3,-492),(11,-492),(4,-485) have solid3x3
barriers through Y14..16. Each barrier has crying obsidian at its center Y15 and
polished basalt in the other eight cells. These are actual saved obstacles, not
an inferred absence from the missing pool. Source membership cannot be used to
claim an open loop through those passages. Room floor patterns include holes and
chains; do not substitute an all-solid flat floor before support checks.

The eastern passage_1 centerline X15..21,Z-485 has polished-basalt support Y13
and air Y14..16. Its boundary cells X14 and22 instead have chain atY14/16 and
crying obsidian atY15. A centerline route therefore fails at the boundaries; side
clearances require their own block checks. No accepted native graph or timing is
claimed yet. Next requirement is to validate supported side access, chamber floors
and the four barriers before defining a complete task and any permitted breaches.

## Representative route and task predeclaration

Actor: the approved0.6-wide,1.8-high survival actor, full health, unenchanted iron
sword and diamond pickaxe, no flight, scaffold, armor/stat boost or external mobs.
The actor knows this layout and the trap. The task begins and ends at the verified
inside-first-chamber station(-0.5,13,-499.5). No authored surface entrance has been
established; excavation from an external cave/surface is a separate UNKNOWN cost,
not silently included in this interior entry-to-exit task. Objective: inspect all
five chamber spaces, recover the two authored debris rewards, disable the one
blaze spawner, clear the stipulated surviving blazes, return and verify completion.
TNT and general building-material stripping are optional, excluded from this task.

Use the chamber names A central reward(-3,-499), B northeast empty(11,-499),
C southwest trap(-3,-485), D southeast empty(11,-485), E eastern spawner(25,-485).
Coordinates in the following route are block-column X/Z; standing centers add0.5
to each. Ordinary chamber-perimeter feet areY13, corridor feetY14. Use one-block
jumps/descents at corridor lips with overhead clearance checks; no automatic
one-block step attribute is assumed. The approved step/jump rates charge vertical
travel separately. Stay on full polished-basalt perimeter floors, avoiding the
four1-block-deep floor recesses in each chamber, which have solid saved supportY11.

A station(-1,-500), A pickup detour(-1,-499),(-2,-499),(-1,-499),(-1,-500);
then B(9,-500),(9,-497),(10,-497), D(10,-487), E via(13,-487),(13,-486),(23,-486).
Return over that E branch to D(10,-487); go to C via(9,-487),(9,-486),(-1,-486).
C pickup detour(-1,-485),(-2,-485),(-1,-485),(-1,-486); reverse the C branch,
then reverse the B/A link to the original station. Stop adjacent to each intact
barrier and remove its two side-lane polished-basalt cells before crossing:
(4,14/15,-500), (10,14/15,-492), (4,14/15,-486). No other barrier is removed.
In particular, the northern trap approach remains closed.

Both pickup detours use the adjacent X-axis chain atY12 for their inner standing
cell. Pinned ChainBlock initializer offsets61..80 defines X box
[0,6.5/16,6.5/16,1,9.5/16,9.5/16], with top12.59375 here. Its narrow support
contains the declared centerline; body/head must remain clear on the whole step.
Charge0.40625 down and up for each detour. Source drops must settle within the
declared acquisition window and intersect the player's pickup region; unreachable,
late, lost or blocked drops censor the task. This is not an observed acquisition.

Mine each debris from its east perimeter station before the pickup detour, aiming
at the lower quarter of its east faceY15.25. Mine the spawner from E's west
station, aiming at its lower west faceY15.25. These aim heights are below the
horizontal chain bottom15.40625; verify each ray before accepting access.
Initial tool is selected once; switch to sword after disabling the source and back
to pickaxe afterward. The worked combat case stipulates two ordinary20-health,
zero-armor blazes on E's west perimeter at(23.5,13,-483.5) and(23.5,13,-482.5).
Kill near then far from the entry station. Flying, unreachable enemies, extra
pursuit, damage/healing delays, lingering fire or interrupted source disablement
censor this fixed-route case rather than being hidden in its duration.

The first Delay0 source can activate during the latter B/D crossing. Predeclare
the conservative active-to-disable budget as18 horizontal blocks,3 vertical blocks,
six decision allowances,0.95 seconds mining and one interaction allowance. Repeated
successful batches have the existing minimum200-tick reset rule and at most four
spawns per batch. Report this potential envelope separately from the stipulated
two-enemy worked case. No realized spawn count or success probability is invented.

Complete task allowances before calculation: nine mining interactions (six barrier
blocks, two resources, one spawner), three selections, two acquisition allowances,
one terminal verification. Decision allowances: A3, A/B4, B2, B/D4, D/E5,
post-combat1, E-return3, D/C5, C3, homeward3, plus one target decision per stipulated
enemy. Thus33+N decisions for N enemies. These are the approved provisional
accounting allowances, not measured player inputs. Stop/kill source before combat;
no combat duration feeds back into source activity in this conditional schedule.

### Pickup correction before task acceptance

The declared route passes support and swept clearance:108 horizontal blocks,
17.625 blocks of support-elevation travel and feet range12.59375..14. A direct
source check nevertheless rejects its uncorrected pickup assumption. Player.aiStep
in the pinned SRG jar, offsets297..306, inflates the standing bounding box by
(1,0.5,1), not one block vertically. At the inner chain floor, its upper pickup
limit is12.59375+1.8+0.5=14.89375. An item resting atop the intact Y14 vertical
chain atY15 can remain outside this limit. Preserve this rejected acquisition
sketch; successful route clearance alone does not prove a complete task.

Correction: remove the vertical chain at(-3,14,-499) and(-3,14,-485) from the
respective east perimeter station, before mining each resource. Aim at its east
face X=-2.40625,Y14.5,Z=-498.5 or-484.5. The source-derived vertical chain box
has that face; the ray remains below the resource and outside the target until
its endpoint. The next vertical chain atY13 remains, with top14. A settled item
there can intersect the inner standing cell's pickup region. Drop timing, item
position, available inventory and successful acquisition remain explicit conditions;
a missed/late acquisition still censors this modeled task.

Add two chain-removal interactions,1.9 seconds of mining (19 ticks each at hardness5
and effective pickaxe speed8), and four decision allowances (aim/check per reward).
The corrected task has11 mining interactions and37+N decisions. All routes,
barrier removals, enemy/source timing and other allowances remain as declared.
No block was changed in the accepted world; these are model actions over raw evidence.


### Executed route and interaction checks

The following direct check reuses state_at and the existing overlap predicate.
Full blocks and chain boxes use the source facts above. Fluid/trigger cells are
conservatively excluded, not mislabeled full collision shapes. It checks all108
horizontal transitions, landing support, jump head clearance and five conservative
interaction-ray bounding boxes. Both support-chain identities are checked. The
initial invocation from a /tmp script could not import the repository namespace;
the repository-root module invocation below succeeds without environment changes.

```sh
uv run python -m evidence.item-13.basalt_routes first
```

The accepted inline implementation is now shared with the second case in
[basalt_routes.py](../basalt_routes.py). Its first-case route, shapes and five
ray bounds retain the same results. The original inline form remains in Git.



## First-case topology, quality and complete conditional timing

Under the declared mining-capable actor, the saved layout has five delineated
chambers A..E. Each has a5x5 inner activity footprint bounded by the7x7 outer
shell, with the16-cell full-block perimeter walk at feet13. Interior chains and
four one-block recesses are not extra rooms. The four solid passage_2 midplanes
separate native components; passage_1 connects D/E through its supported side lanes.
Thus the native chamber graph has5 nodes,1 edge,4 components,0 branch junctions
and0 cycles. A/B/C are not natively connected to another chamber; their inclusion
as playable rooms depends explicitly on the approved breaching capability.

The task opens A/B, B/D and D/C using six basalt removals. Its resulting graph
has5 reachable rooms and4 edges, one degree-three junction D, three degree-one
ends A/C/E and no cycle. Opening the fourth A/C barrier would create a cycle and
a hazardous northern C approach; that additional work is excluded from this task.
A centerline or piece graph that reported the loop as already open would be wrong.
Passage side lanes provide one-block-wide clear paths beside central chain/obsidian
obstacles, with full support and enough upright/jump clearance as checked. These
are geometric chokepoints; live enemy doorway/pathfinding behavior is NOT MEASURED.

Safe task graph depths from A: B1,D2,C3,E3 edges. Within the declared perimeter/
corridor network, shortest station distances are C36 and E38 horizontal blocks;
A's resource is available at its initial station. The completed circuit is108
horizontal blocks including two4-block pickup detours. These are scoped station
distances, not shortest paths through arbitrary mining or flight. Support elevation
changes total17.625 blocks, half ascent and half descent, with feet12.59375..14.
This charges changes between support levels, not a measurement of airborne jump arcs.
There is no second stacked floor or deeper reachable level in this sample.

At the five centers, saved WORLD_SURFACE isY127 and authored cap centerY18, a109-
block vertical separation under the Nether roof. The directly retained cap-cover
cellsY19..21 are solid basalt/blackstone at all five centers. This proves three
blocks of immediate cover; it does not prove109 continuous solid blocks or provide
a walkable surface entry. The task's initial interior station and external
excavation cost limitation remain explicit.

Meaningful hazard: the northern C entry crosses attached, powered=false,
disarmed=false tripwires atY13 and14. TripWireBlock.checkPressed tests non-ignoring
entities against the string shape and updates its source (offsets24..137).
TripWireHookBlock gives15 power when triggered, direct power toward its facing,
and notifies neighbors at both hook and backing block (notifyNeighbors0..19).
The west backing basalt at(-6,13,-487) is adjacent to saved TNT(-6,12,-487);
the upper backing block is adjacent to the TNT corner(-6,14,-488). TntBlock.
neighborChanged0..19 primes/removes powered TNT. This exact source/geometry chain
supports an explosive trap mechanism, not merely a TNT palette. No explosion was
run. The chosen eastern C route stays outside every trigger cell, which the
conservative swept check confirms. Its bypass preserves all68 unpowered, unstable=
false TNT blocks. They are optional industrial resource potential; mining them
or triggering the trap is excluded from the task. Room-floor recesses have solid
support one block below and are footing interruptions, not demonstrated deep pits.

Enemy potential is one Delay0 blaze spawner and one explicit hostile type, with
no authored resident or natural override. The fixed two-blaze case uses existing
20-health/zero-armor source: four fully cooled6-damage sword hits,13 ticks per
attack cycle,2.6 active seconds per blaze (5.2 total). Its positions have full
perimeter support and clear melee-height space. Near-then-far targets lie on the
same clear west-perimeter line at2 and3 blocks from the actor; the first target
is removed before engaging the second. This does not claim actual stationary AI.

The corrected active-to-disable clocks are10.8/17.95/28.95 seconds. With
Delay0, at most four successes per batch and minimum200 ticks between successful
batches, conservative source ceilings are8/8/12 entities during those windows.
They ignore restrictive nearby caps and spawn failures, so they are potentials,
not predicted counts. Extra enemies or pre-disable interruption censor the worked
N=2 task. Its5.2-second active combat is not a bound on arbitrary realized combat.

Two empty rooms B/D give2/5 empty. They provide alternative route/connective
purpose, especially the B/D approach that avoids northern C wires and the D/E
link; dead rooms are0/5 under this task, not an assertion that every room contains
loot. Authored resource rewards are one debris in A and one in C. No container
is authored or saved. E's source carries blaze-rod potential: pinned extra.jar
`data/minecraft/loot_table/entities/blaze.json`, SHA-256
 d2136cf90740b88c351e0a61b3e43cc4184591a987dcece1b2e6d9ce6a448523,
has a killed_by_player pool,0..1 rods before looting, and a looting-count increase.
The declared unenchanted case has no looting bonus. Optional rod/TNT collection
is not included in the two-debris task; generated/acquired loot is NOT MEASURED.

Finale: NONE. E is a terminal encounter room but has no distinct scripted finale
or unique placed reward; A/C rewards are distributed elsewhere. Objective clarity
is CONDITIONAL on seeing the resource/source, distinctive terminal challenge ABSENT,
terminal reward linkage ABSENT, and route integration CONDITIONAL on breaching.
The layout has no demonstrated progression lock. In particular, E's east opening
atX28,Z-486 is already airY14..16 above supportedY13; the adjacent X29/30 columns
are solid basalt. An excavated gallery reaching that opening can bypass A..D, but
its external excavation length/cost is UNKNOWN. Do not call it a currently open
external entrance. The report's observed obstacle and source controls support
sequence-breaking potential, not a measured outside-to-goal time.

Replay assessment: authored procedural combinations of passages, empty chambers,
spawners and traps, plus central material outcomes, support layout/objective
variation across generated assemblies. Actual player enjoyment or repeat-session
outcomes are NOT MEASURED. In the same persistent cleared site, removed spawner,
mined rewards and opened barriers are not reset by any observed mechanism here.
The first sample's broad42x35 footprint has five compact spaces and shallow
vertical progression; it is not established as a visually large but mechanically
shallow surface landmark. Its meaningful trap, source and breach choices prevent
reducing it to decorative volume alone.

Mining budget is15.65 seconds: six polished basalt blocks at5 ticks each, two
debris at113 ticks each, one spawner and two chains at19 ticks each. Polished
basalt hardness1.25 is pinned Blocks initializer11227..11233; effective pickaxe
speed8 and the existing mineable tag apply. Keep all37+N decisions,11 interactions,
three selections,two acquisitions and terminal verification from the correction.
The complete formula is:

`108/u + 17.625/j + 15.65 + (37+N)*decision + 11*input + 3*selection + 2*acquisition + verification + 2.6*N/duty`

| Profile | No-enemy conditional task | Two stipulated blazes | Active combat for two |
| --- | ---: | ---: | ---: |
| A | 80.875s | 87.075s | 5.2s |
| B | 129.9s | 138.833333s | 5.2s |
| C | 207.65s | 221.05s | 5.2s |

Wall-clock combat allowance is5.2/duty, not5.2 at every duty. These are explicit
scenario estimates, not observed human times, typical durations or guarantees.
Missing/late pickups, equipment/state changes, lost support, trigger contact,
extra enemies, flying/occluded targets, health recovery, source delay or altered
navigation invalidate the fixed task. No player, enemy or loot was simulated in
this read-only assessment. The first representative now has a local complete
modeled assessment. The second assembly, remaining material outcomes and full
Item 13 review/delivery are still required.


Source-window boundary correction: the first draft used17 horizontal blocks from
the first in-range standing-node center. Activation can occur earlier within the
preceding one-block move. Include that entire step instead, giving18 horizontal
blocks,3 vertical blocks,six decisions,0.95s mining and one input. This corrects a
sub-cell omission before accepting source ceilings. The resulting8/8/12 ceilings
are unchanged, but the source-window clocks above use the corrected distances.

Reproduce the complete arithmetic independently of the geometry command:

```sh
uv run python - <<'PY'
import math
for name,u,j,n,a,s,k,v,duty in zip('ABC',(5,4,3),(1,.5,.25),(.5,1,1.5),(.25,.5,1),(.25,.5,1),(1,2,4),(2,4,8),(1,.75,.5),strict=True):
    base=108/u+17.625/j+15.65+37*n+11*a+3*s+2*k+v
    active=18/u+3/j+6*n+.95+a
    print(name,base,base+2*n+5.2/duty,active,4*math.ceil(active/10))
PY
```

Mapped-method source identity for the mechanism/shape checks: pinned SRG jar
SHA-25626ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71.
Use the pinned Temurin javap with `-c -p` and this classpath:
`instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar`.
Inspected classes are `net.minecraft.world.level.block.ChainBlock`,
`TripWireBlock`, `TripWireHookBlock`, `TntBlock` in that block package, and
`net.minecraft.world.entity.player.Player`. Their method names/offsets above are
precise artifact derivations; no source behavior is labeled a human observation.


## Second predeclared assembly

The representative now passes its local assessment, so the second55,614-cell
assembly may use the already declared120-second/20-MiB/5-GiB limits. Reuse the
same extractor, source identity gates and evidence format. No new server or
generation is needed. Exact command, pending before execution:

```sh
timeout 120 uv run python - <<'PY'
import gzip, hashlib, importlib, json, resource, shutil, time
from pathlib import Path
from tools.analyze_route_opportunities import read_bound
m = importlib.import_module('evidence.item-13.measure')
selection_hash = 'eaa4ba0ea4db159f926e85f6367fffd0209bc4be8617fedbaafe7f6ed8157ca3'
plan = json.loads(read_bound(Path('evidence/item-13/basalt-chambers-selection.json'), selection_hash))
chosen = plan['selected'][1]
rows = json.loads(read_bound(Path('evidence/item-13/candidates.json'), plan['input_sha256']['candidates']))['candidates']
case, = [r for r in rows if r['id'] == chosen['candidate_id']]
assert case['bounds'] == chosen['bounds'] and case['voxel_count'] == 55614
output = Path('evidence/item-13/fixed-blocks/basalt-chambers-ordinary-r2.json.gz')
assert not output.exists() and not output.is_symlink()
assert shutil.disk_usage('.').free >= 5 * 1024**3
started = time.monotonic()
result = {'selection_sha256': selection_hash, 'cases': [m.extract(case, voxel_budget=55614)]}
result['elapsed_seconds'] = round(time.monotonic() - started, 6)
result['peak_rss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
raw = gzip.compress((json.dumps(result, sort_keys=True, separators=(',', ':')) + '\n').encode(), mtime=0)
assert len(raw) <= 20 * 1024**2
with output.open('xb') as stream:
    stream.write(raw)
print(len(raw), hashlib.sha256(raw).hexdigest(), result['elapsed_seconds'], result['peak_rss_kib'])
PY
```

Second input extraction passes in5.527101 seconds,48,280 KiB peak RSS,55,614
cells and16,360 compressed bytes. SHA-256
f77a6dc8a1d956d0d6c0c45b5efe80e6554709b50a2152da601b2265394ed803.
[Raw ordinary r2](basalt-chambers-ordinary-r2.json.gz) and its inspected
[seven-layer sheet](basalt-chambers-ordinary-r2-slices.png) are retained. SVG is
6,971,499 bytes; PNG93,900 bytes, below the20-MiB view allocation. Commands:

```sh
timeout 120 uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/basalt-chambers-ordinary-r2.json.gz --output evidence/item-13/fixed-blocks/basalt-chambers-ordinary-r2-slices.svg
timeout 120 convert -background white evidence/item-13/fixed-blocks/basalt-chambers-ordinary-r2-slices.svg evidence/item-13/fixed-blocks/basalt-chambers-ordinary-r2-slices.png
```

Its28 saved components are one center, seven empty chambers, two trap chambers,
two spawner chambers, seven passage_1, four passage_2 and five dummy_side. These
are verified component roles; playable room count/graph still require the second
case's concrete support and connector checks. The same source templates permit
reuse of shape/mechanism facts, but not copying the first route or timings.

The only two saved block entities are Delay0 blaze spawners at(143,15,-141) and
(157,15,-99), with the same source parameters. The processed central reward at
(157,15,-141) is ancient debris; trap rewards at(157,15,-155) and(143,15,-155)
are also debris. There are136 saved TNT blocks. No container entity is present.
These are authored/source and saved-block facts, not realized encounters or loot.

The accepted intake also records six omit-Sparse control occurrences and no
Item 7/8 prior candidates for this family. Both baseline centers are now known to
retain debris. Before declaring missing netherite/lodestone evidence or creating
any new experiment, inspect the exact existing control centers. Such control
material outcomes must retain their altered density-arm identity and cannot be
counted as extra untouched-baseline samples or natural-frequency measurements.
No control extraction or new material experiment has yet been run for this family.

### Second-case task declaration and trap approach

Reuse the first actor and conditional equipment/state limits, adding ordinary
shears for four deliberate wire cuts. Begin/end at(159.5,13,-139.5) in the central
reward chamber. Objectives are its three authored debris rewards, both disabled
blaze sources, cleared stipulated enemies, inspection of all12 chamber-shaped
spaces and return verification. External excavation remains excluded/UNKNOWN.
The no-flight/no-placement task permits eight side-lane basalt removals, three
resource-support chains, three debris blocks, two spawners and four sheared strings.
No TNT harvesting or intentional detonation is included.

Visit the nearby west source first, before reward pickup or branch exploration;
then its northern trap and the western empty branches. Return to the center for
its reward and northern trap, then follow the southern chain to the second source
before inspecting its empty side branch and returning. The exact itinerary will
be retained in the shared route check. Do not copy first-case distances/timing.

Four side-lane barriers require Y14/15 removals at X/Z(156,-148),(142,-148),
(128,-148),(156,-120). Both traps have south-side attached strings at Z-153,
Y13 and14. Cut X142 for the western trap and X156 for the eastern trap. Stand
at the respective X+0.5,Y14,Z-151.5, outside the wire cell, cut upper then lower
with shears, and only then enter. Source TripWireBlock.playerWillDestroy offsets
18..52 sets DISARMED=true when ordinary shears are held. The source hook
calculation excludes disarmed strings. A pickaxe cut is not an interchangeable
safe action. This is source-supported disarming, not a runtime success claim.

The attached string selection box is[0,1/16,0,1,2.5/16,1] (TripWireBlock static
initializer59..74). Aim inside that thin box at Y14.1 then13.1,Z-152.5. The lower
ray must clear the corridor floor, with the upper string already removed. A
conservative rectangular ray bound includes that floor even when the actual
oblique ray clears it; use the existing first-case shape check with an exact
segment/box intersection for these four current targets. Do not loosen collision
or assume a cube is the string's selection shape.

After each cut, route from the clear entry column(X,-153) through(X,-154),
(X+1,-154),(X+2,-154),(X+3,-154) to the east perimeter reward station. This crosses
one-block floor recesses and a low chain, so explicitly verify supportY11..13,
clearance, transitions and the unaffected remaining wire cells. Reuse the common
first-case check, extending its lower support lookup for this demonstrated need.
Remove the Y14 vertical chain below each resource before harvest, as required by
the first-case pickup correction. The same conditional settling/acquisition rules
apply. No source shape or successful raw measurement is regenerated.

Worked enemies: two ordinary blazes per source. At the west source, use supported
east-perimeter positions(145.5,13,-138.5),(145.5,13,-141.5), from actor station
(145.5,13,-139.5). At the southern source, use north-perimeter positions
(155.5,13,-100.5),(159.5,13,-100.5), from actor(156.5,13,-100.5).
Kill near then far; stationary/reachable targets, no healing/fire/pursuit delay,
no extra enemies and uninterrupted pre-disable travel are conditions, not AI claims.

Each source's conservative active-to-disable budget is15 horizontal blocks,
2 vertical blocks,six decision allowances,one interaction and0.95s mining. It
includes the entire first move that can cross into range. Both sources are
removed before their combat phase. Keep per-source spawn ceilings separate from
the stipulated two-enemy workloads. The raw worlds are never modified by this model.

Predeclared task accounting:20 block interactions (eight basalt,three support
chains,three debris,two spawners,four strings),nine selections,three acquisitions
and one terminal verification. Ordinary mining work uses the already supported
five-tick basalt,19-tick chain/spawner and113-tick debris inputs. Strings have
instant-break source behavior, charged as interactions. Decisions are one initial
orientation,12 first-room assessments,20 action aims,three pickup checks,two
post-combat inspections,one per heading change/reversal in the explicit itinerary,
and one per stipulated enemy target. Thus38+heading_changes+N decisions. These
remain provisional modeled allowances, not observed inputs. Dead-room assessment
uses the resource/source objective, not the circular proposition that every room
must be useful merely because the measurement task surveys it.

Second-case route failure and revised predeclaration: the first execution rejected
standing column(156,-154). Its Y11 support is lava, not solid basalt. Both eastern
trap recesses(156,-154),(158,-154) have saved lava atY10/11 and airY12/13; the
western equivalents have solid basaltY10/11. The no-placement scenario above is
FAILED and retained. The four ordered shear rays passed before that failure.

Revise only this task: carry two full basalt building blocks. After cutting the
eastern strings, from entry(156.5,13,-152.5), place a support at(156,12,-154)
against the west face of the horizontal chain(157,12,-154), aiming at
(157.40625,12.5,-153.5). Move onto that support and place(158,12,-154) against
west face of the full perimeter block(159,12,-154), aiming at(159,12.5,-153.5).
Validate both rays before accepting the modified route. Both blocks occupy saved
air above lava, not replacements of fluid. This is conditional construction, not
observed fluid behavior. Charge two additional placement interactions, two aim
allowances and two selections (blocks then pickaxe), with the same route columns.
Revised accounting is22 interactions,11 selections,40+heading_changes+N decisions;
mining remains23.7 seconds. An interrupted or invalid placement censors this task.

### Second-case accepted geometry and quality

The revised construction scenario passes. Reproduce both cases using the shared
[route check](../basalt_routes.py), which reuses the first case's shape and sweep
implementation and the existing state_at/overlaps functions:

```sh
uv run python -m evidence.item-13.basalt_routes first
uv run python -m evidence.item-13.basalt_routes second
```

Both raw inputs are SHA-256 checked before decoding. The second check verifies
four upper-then-lower shear rays, two ordered placement rays against the declared
chain/perimeter faces,332 horizontal transitions, supportY11..13, jump clearance,
eight source/resource/support-chain interaction bounds and four stipulated melee
stations. It conservatively excludes all remaining wire, hook and fluid cells.
These are GEOMETRIC MEASUREMENTS of a declared modified state, not a simulated
player, trap activation or observed building result. No world file is modified.

Twelve rooms are delineated by actual5x5 internal activity footprints bounded by
7x7 shells, not by all28 assembly pieces. Each center below denotes inclusive
inner X/Z bounds center plus/minus2. Supported perimeters are at feet13;
corridors rise to14, while recess/chain floors vary as checked. There is no
stacked second level. Corridors and five solid dummy branches add no rooms.

| Room | Center X/Z | Content | Task graph neighbors | Depth from A |
| --- | --- | --- | --- | ---: |
| A |157,-141| Central debris |B,C,I|0|
| B |143,-141| Blaze source |A,D,E|1|
| C |157,-155| Debris, wired TNT trap, lava recesses |A|1|
| D |143,-155| Debris, wired TNT trap |B|2|
| E |129,-141| Empty western hub |B,F,G,H|2|
| F |115,-141| Empty terminal |E|3|
| G |129,-155| Empty terminal |E|3|
| H |129,-127| Empty terminal |E|3|
| I |157,-127| Empty connecting room |A,J|1|
| J |157,-113| Empty lower hub |I,K,L|2|
| K |157,-99| Blaze source |J|3|
| L |143,-113| Empty terminal |J|3|

Native connections omit A/C,B/D,E/G,I/J because their passage midplanes are
solid. Native graph:12 nodes,7 edges,5 components,one branching junction E and
zero cycles. The eight declared side-lane basalt removals connect all12 rooms
with11 edges,four branching junctions A/B/E/J,seven ends C/D/F/G/H/K/L and zero
cycles. Breaching and trap disarming/construction are explicit access conditions,
not claims that these routes are natively safe. One-block side lanes beside
central chain/obsidian obstructions are geometric chokepoints; live enemy behavior
at those connections remains NOT MEASURED and outside this Item 13 inspection.

Shortest station distances within the union of checked route transitions are:
A reward0,B source16,C reward20,D reward36,K source46 horizontal blocks. The
furthest checked empty stations F/G are48. These are scoped to this validated
network, not claims of global optimality under arbitrary mining or flight.
Graph depth is at most3 edges. Full return circuit332 includes three4-block
pickup detours and the deliberate empty-branch inspections. Total support-level
travel is54.4375, with27.21875 ascent and descent each; floor span12..14.
This is support elevation, not airborne jump-arc distance.

Saved WORLD_SURFACE is127 at all12 centers,109 above the authored center capY18.
Direct center coverY19..21 is basalt/blackstone at11 centers, but lava at C.
This is not109 blocks of continuous solid cover and does not establish a walkable
Nether-roof entrance. Derive these facts directly from surface_xzy and state_at
at the table's centers, without another restore or survey.

Meaningful hazards are two attached wired explosive approaches plus C's lava
recess exposure. The first case's pinned hook/neighbor/TNT source chain applies:
backing blocks(140,13,-153),(154,13,-153) are saved polished basalt immediately
above TNT at the same X/Z,Y12. Both rooms retain68 TNT each,136 total. Cutting
upper/lower strings with ordinary shears explicitly disarms the chosen lane;
remaining wires stay excluded. The source string has default zero destroyTime:
Blocks initializer14520..14548 constructs Properties.of(), noCollission and
pushReaction without a strength assignment; Properties' constructor leaves that
float at zero. Thus no mining-duration term is added, but input/aim costs remain.
Do not misdescribe this as a literal instabreak initializer call. The two bridge
blocks prevent the chosen actor's support from descending into C's lava. No
explosion, fluid update, live disarming success or damage event was observed.

Empty rooms are7/12 (E,F,G,H,I,J,L). Dead rooms under the resource/source objective
are5/12 (E,F,G,H,L): E only connects three empty leaves. I/J provide necessary
access to source K and are not dead. A terminal-only interpretation gives four
dead leaves, explicitly excluding E; this sensitivity does not change emptiness.

Authored rewards are three debris nodes at A/C/D, at graph depths0/1/2. Both
saved sources B/K have explicit blaze potential,one hostile type,Delay0 and the
same source payload as the first case. Authored residents are absent; realized
counts/diversity remain NOT MEASURED. No container loot is authored or saved.
Blaze-rod and TNT salvage potential retain the first case's source/support limits
and are excluded from this three-debris task. Acquired loot is NOT MEASURED.

Finale NONE: terminal source K has no unique placed reward or scripted terminal
mechanism. Objective clarity is CONDITIONAL on seeing resources/sources,
distinctive terminal challenge ABSENT, terminal reward linkage ABSENT, route
integration CONDITIONAL on the breached main branch, and external bypass exposure
UNKNOWN beyond the retained local shell. Removing K's local wall from an excavated
gallery could skip A/I/J; gallery access and excavation effort are UNKNOWN.
No arbitrary route protection prevents such an engineering solution. C's lava
cover makes direct roof breaching hazardous rather than a free demonstrated entry.

Replay assessment: the two naturally generated assemblies differ materially in
room/branch count, source/trap/reward distribution, empty tails and lava exposure.
That supports expected generated-layout variation, not observed player replay
value. Persistent revisits retain removed sources/rewards and breached barriers;
no automatic physical dungeon reset is established. The56x63 envelope contains
12 compact rooms and no deeper floor progression. Its long horizontal branching
and seven empty rooms support a shallow-content concern, but no surface-view
measurement establishes it as a visually large landmark. Do not replace this
assessment with volume or piece counts.

### Second-case complete conditional task result

The revised formula with N stipulated blazes is:

`332/u + 54.4375/j + 23.7 + (117+N)*decision + 22*input + 11*selection + 3*acquisition + verification + 2.6*N/duty`

The117 decisions are40 declared non-heading allowances plus77 actual heading
changes/reversals. Mining474 ticks at20TPS is23.7 seconds. The22 interactions
include two bridge placements and four instant string cuts. Pickup settling and
support-chain removals use the first case's approved conditional assumptions.

| Profile | No-enemy task | Four stipulated blazes | Active combat for four |
| --- | ---: | ---: | ---: |
| A |216.2875s|228.6875s|10.4s|
| B |359.075s|376.941667s|10.4s|
| C |580.616667s|607.416667s|10.4s|

Each source has a conservative pre-disable clock9.2/15.2/23.95 seconds under the
separately declared15-block activation budget. Delay0 and a minimum ten-second
successful-batch interval give potential ceilings4/8/12 per source, ignoring
restrictive spawn failures/caps. They are neither predicted populations nor the
stipulated two per source. Additional enemies or interruption before disablement
censor the fixed task. Melee station support/clear height-14 lines are checked;
stationary reachable targets and duty allowances remain explicit scenario inputs.

The first-case check still returns108 horizontal blocks and17.625 support-level
travel, with unchanged five interaction bounds. Both local sample assessments
now pass under their respective scenarios. This does not close central material
coverage or the full Item 13 family/review/delivery gates. Next inspect the six
existing omit-Sparse centers for netherite/lodestone before any new experiment.

Focused verification for this increment: both geometry commands pass, ruff check
and formatting pass, basedpyright reports zero errors/warnings, and git diff
--check passes. The no-placement lava failure is preserved above. No additional
world processing or runtime capture was required for this local result.

## Existing control material check predeclaration

The hash-bound accepted census identifies six omit-Sparse occurrences in four
worlds: mountainous r1(-5,31), mountainous r2(31,29), ocean-heavy r2 accepted
attempt3(8,-12),(12,7), ordinary r2(-4,11),(9,22). Inspect every one, retaining
this control identity. Select the unique ancient_debris central component from
each actual start, then read its7x7x7 saved cube (2,058 cells total). This checks
central material outcomes only; do not count these as baseline quality samples.
Use the existing archive binding, full restored inventory checks and POSIX lock,
Anvil/NBT decoder and saved_block_section. Budget120 seconds total,2 MiB retained
JSON and5 GiB free floor; no server, generation or mutable world operation.
Missing center/component/chunk/section, unexpected dimensions, identity mismatch
or overrun fails the read. Preserve outcomes even if none supplies a missing
netherite/lodestone variant. Full control dungeon routes are outside this read.

Reproduction command (run from repository root with the output absent):

```sh
timeout 120 uv run python - <<'PY'
import hashlib, json, shutil, time
from pathlib import Path
from tools.analyze_route_opportunities import ROOT, accepted_inputs, read_bound, verify_world
from tools.analyze_structure_density import saved_block_section
from tools.manage_item4_environment import _world_backup_lock
from mcpack_evidence.item7_anvil import RegionContext, decode_region_payloads
from mcpack_evidence.item7_archive_models import ArchiveManifest
from mcpack_evidence.item7_nbt import decode_compound_nbt

output=Path('evidence/item-13/fixed-blocks/basalt-control-centers.json')
assert not output.exists() and shutil.disk_usage(ROOT).free >= 5*1024**3
begun=time.monotonic(); result=[]
family='adorabuild_structures:basalt_chambers'
root='adorabuild_structures:basalt_chambers_large_1'
for name,identity in sorted(accepted_inputs().items()):
    if name.endswith('-baseline'):continue
    census=read_bound(ROOT/'evidence/raw/item10'/f'{name}-analysis/all-strata.json',identity['input_sha256'])
    rows=[r for r in json.loads(census)['strata']['nether']['classification']['occurrences'] if r['family_id']==family]
    if not rows:continue
    custody=ROOT/'evidence/raw/item10'/f'{name}-custody'
    world=custody/'restored-world/world'
    mr=read_bound(ROOT/'evidence/item-10'/name/'archive-manifest.json')
    manifest=ArchiveManifest.model_validate_json(mr)
    entry=next(r for r in manifest.files if r.relative_path=='world-backup.json')
    backup=json.loads(read_bound(custody/'restored-local/world-backup.json',entry.sha256))
    assert backup['archive_sha256']==next(r.sha256 for r in manifest.files if r.relative_path=='world.tar.gz')
    with _world_backup_lock(world):
        verify_world(world,backup['world_files'])
        chunks={}; payload_hashes={}; loaded=set()
        def chunk_at(cx,cz):
            region=(cx//32,cz//32)
            if region not in loaded:
                relative=f'DIM-1/region/r.{region[0]}.{region[1]}.mca'
                for record,payload in decode_region_payloads(world/relative,RegionContext('minecraft:the_nether',relative,0,256)):
                    key=(record.chunk_x,record.chunk_z)
                    assert key not in chunks
                    chunks[key]=(record.full,decode_compound_nbt(payload))
                    payload_hashes[key]=hashlib.sha256(payload).hexdigest()
                loaded.add(region)
            assert (cx,cz) in chunks and chunks[(cx,cz)][0], ('missing/full',name,cx,cz)
            return chunks[(cx,cz)][1]
        for row in sorted(rows,key=lambda r:(r['chunk_x'],r['chunk_z'])):
            cx,cz=row['chunk_x'],row['chunk_z']; assert row['registry_id']==root
            start=chunk_at(cx,cz)['structures']['starts'][root]
            assert (start['id'],start['ChunkX'],start['ChunkZ'])==(root,cx,cz)
            central=[p for p in start['Children'] if p.get('pool_element',{}).get('location')==family+'/ancient_debris']
            assert len(central)==1
            piece=central[0]; bb=piece['BB']
            assert [bb[i+3]-bb[i]+1 for i in range(3)]==[7,7,7]
            center=[bb[i]+3 for i in range(3)]; sections={}; states=[]; used={(cx,cz)}
            for y in range(bb[1],bb[4]+1):
                for z in range(bb[2],bb[5]+1):
                    for x in range(bb[0],bb[3]+1):
                        key=(x//16,y//16,z//16);used.add((key[0],key[2]))
                        if key not in sections:
                            sections[key]=saved_block_section(chunk_at(key[0],key[2]),key[1])
                        section=sections[key];assert section is not None
                        palette,indices=section
                        index=indices[x%16+16*(z%16)+256*(y%16)]
                        assert 0<=index<len(palette)
                        states.append(palette[index])
            result.append({'world':name,'arm':'omit-Sparse','dimension':'minecraft:the_nether',
                'root':root,'chunk_x':cx,'chunk_z':cz,'census_sha256':identity['input_sha256'],
                'archive_manifest_sha256':hashlib.sha256(mr).hexdigest(),'world_backup_sha256':entry.sha256,
                'start_nbt':start,'bounds':bb,'center':center,'states_yzx':states,
                'center_state':states[171],'chunk_payload_sha256':[[x,z,payload_hashes[(x,z)]] for x,z in sorted(used)]})
        verify_world(world,backup['world_files'])
assert len(result)==6 and sum(len(r['states_yzx']) for r in result)==2058
assert time.monotonic()-begun < 120
raw=(json.dumps({'scope':'saved control central components only; not baseline quality repetitions','cases':result},indent=2,sort_keys=True)+'\n').encode()
assert len(raw)<=2*1024**2
output.write_bytes(raw)
print(json.dumps({'sha256':hashlib.sha256(raw).hexdigest(),'size_bytes':len(raw),'seconds':time.monotonic()-begun,'outcomes':[[r['world'],r['chunk_x'],r['chunk_z'],r['center_state']] for r in result]},indent=2))
PY
```

Control read PASS:77.763812 seconds,6 complete central cubes and2,058 saved cells.
All four complete world inventories match before/after under their locks. The
retained [lossless raw control record](basalt-control-centers.json.gz) is13,531
bytes, SHA-256 `67bb09edb0b1ba27dad55cd3ee5412281611ae342b3adc364ac0af61ec445c1b`.
Decompressed JSON is415,265 bytes, SHA-256
`5bd7563e101196265ce93675b21a3879405eae6d28c2968bb93627caed909404`.
It retains full start NBT, center cubes, exact arm/world/dimension, archive/backup/
census hashes and every contributing chunk payload hash. All declared caps pass.
The temporary uncompressed original remains under ignored evidence/raw/item13/.
The lossless compression step after the command above is:

```sh
uv run python - <<'PY'
import gzip, hashlib
from pathlib import Path
p=Path('evidence/item-13/fixed-blocks/basalt-control-centers.json')
raw=p.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='5bd7563e101196265ce93675b21a3879405eae6d28c2968bb93627caed909404'
packed=gzip.compress(raw,mtime=0)
assert hashlib.sha256(packed).hexdigest()=='67bb09edb0b1ba27dad55cd3ee5412281611ae342b3adc364ac0af61ec445c1b'
p.with_suffix('.json.gz').write_bytes(packed)
PY
```

| Control world suffix | Start chunk | Center X/Y/Z | Saved outcome |
| --- | --- | --- | --- |
| mountainous-r1-without-sparse | -5,31 | -77,15,499 | ancient debris |
| mountainous-r2-without-sparse |31,29|499,15,467|lodestone|
| ocean-heavy-r2-without-sparse-attempt3 |8,-12|131,15,-189|ancient debris|
| ocean-heavy-r2-without-sparse-attempt3 |12,7|189,15,115|ancient debris|
| ordinary-r2-without-sparse |-4,11|-61,15,173|ancient debris|
| ordinary-r2-without-sparse |9,22|141,15,355|ancient debris|

Each world name has the full- prefix in the raw record. These six material
observations are control data, not new baseline quality cases or probability
estimates. Lodestone is now supported by a saved generated occurrence. Netherite
block remains the exact missing central outcome after all eight existing
baseline/control occurrences and the existing empty Item 7/8 candidate list.
No new diagnostic has been run for that gap.

The two mountainous centers both have NONE rotation. Their surrounding terrain
cells differ, including lava, so treating the entire343-cell cubes as identical
would be wrong. On the271 source-authored non-jigsaw/non-structure_void cells,
they differ only at local(3,3,3): debris versus lodestone. Reproduce this direct
comparison against the already hash-bound central template:

```sh
uv run python - <<'PY'
import gzip, hashlib, json, zipfile
from pathlib import Path
from mcpack_evidence.item7_nbt import decode_compound_nbt
p=Path('evidence/item-13/fixed-blocks/basalt-control-centers.json.gz')
raw=gzip.decompress(p.read_bytes())
assert hashlib.sha256(raw).hexdigest()=='5bd7563e101196265ce93675b21a3879405eae6d28c2968bb93627caed909404'
a,b=json.loads(raw)['cases'][:2]
with zipfile.ZipFile('downloads/item3/candidates/adorabuild-structures-2.11.0-neoforge-1.21.3.jar') as z:
    source=z.read('data/adorabuild_structures/structure/basalt_chambers/ancient_debris.nbt')
assert hashlib.sha256(source).hexdigest()=='dcbb6c62c035ed12459c2e182a9dccfa7e20e87298a320f72ff9a0cbdfb1a639'
n=decode_compound_nbt(gzip.decompress(source))
mask=[r for r in n['blocks'] if n['palette'][r['state']]['Name'] not in {'minecraft:structure_void','minecraft:jigsaw'}]
diffs=[]
for r in mask:
    x,y,z=r['pos'];i=x+z*7+y*49
    if a['states_yzx'][i]!=b['states_yzx'][i]:diffs.append(r['pos'])
assert len(mask)==271 and diffs==[[3,3,3]]
print('271 authored cells compared; only the central material differs')
PY
```

Lodestone quality/model integration: source-supported full-block replacement
changes central reward identity and correct-tool mining cost, not the authored
room graph or central support-chain pickup constraint. Reuse the
[temple material source](adorabuild-nether_temple_medium_1-report.md#alternate-material-source-inputs-for-the-declared-placement-diagnostic):
hardness3.5, pickaxe tag, single self-drop potential and ordinary non-fire-resistant
item. The same dry grounded diamond-pick scenario requires14 ticks0.70s instead
of debris113 ticks5.65s. Conditional baseline-layout totals therefore decrease
by4.95s: first-case two-blaze82.125/133.883333/216.10s; second-case four-blaze
223.7375/371.991667/602.466667s. All route, disarming, construction, support-chain,
acquisition and enemy conditions remain. These are modeled center substitutions
supported by saved material evidence, not measured timings of either control
world's full assembly. Do not infer that the control lava setting has the same
external access or route cost. Lodestone does not create a finale, reset or new
hostile type. Its lack of item fire resistance keeps pickup loss a censoring case.

Netherite source inputs, before diagnostic acceptance: pinned Blocks initializer
34035..34075 registers a full ordinary Block, requiresCorrectToolForDrops,
hardness50 and resistance1200. Pinned Items initializer914..933 gives its BlockItem
fireResistant properties. The existing pickaxe and needs_diamond_tool tags both
contain netherite_block (hashes e31b952f7df00a46e2e442e601b1139e87085314364e9137381c71e66f55700f
and fce3d4bef99721711ffb1bcdd72812c82e55e90d02417fa3065c260c0f96b833).
The declared diamond pick therefore meets the tool tier. Nominal dry grounded
mining is ceil(50*30/8)=188 ticks9.40s. These are SOURCE INSPECTION inputs;
saved netherite material acceptance and complete model integration still depend
on the [one-component diagnostic](../basalt-variant/README.md).

Pinned extra.jar `data/minecraft/loot_table/blocks/netherite_block.json`, SHA-256
`4f810334641b04d676026e8e4e08d020326de5fc7db155d78746c2f7a7304bfa`, contains one
single-item netherite_block pool with survives_explosion. This is a self-drop
potential, not generated/acquired loot or permission to assume a pickup succeeds.
Retain support-chain removal and conditional acquisition even for fire-resistant
items. No new room, hostile type or finale follows from the central material.

## Central material coverage resolved locally

The [netherite diagnostic](../basalt-variant/README.md#saved-material-verification)
now passes predicted live placement, frozen lifecycle and a fresh hash-verified
stopped-world comparison of all2,197 padded cells, with zero differences. Its271
source-authored cells match the NONE-rotation natural debris control except for
the central netherite block. It remains a forced material diagnostic, not a third
natural assembly sample or natural-frequency evidence.

The complete family sample set therefore contains both predeclared distinct-seed
baseline assemblies, all seven authored component types, natural/control debris
and lodestone centers, and the exact missing netherite processor outcome. Trap
magma replacement is unconditional TNT; no unsupported random magma alternative
is left outstanding. The missing pool reference remains a frozen source defect,
not an omitted experiment or permission to repair the configuration.

For the same conditional baseline-layout task with a central netherite reward,
replace only central mining5.65s by9.40s, a3.75s increase. Other debris rewards,
source removal, support-chain pickup preparation, decision/input costs, C's bridge
and trap shearing remain. First-case two-blaze totals become90.825/142.583333/
224.80s; second-case four-blaze totals become232.4375/380.691667/611.166667s.
These are explicitly modeled substitutions supported by saved material equivalence,
not observed gameplay or the time to navigate the forced Y160 component. The
central reward changes identity and tool work but does not add a room, branch,
vertical floor, hostile type or authored finale. Persistent replay and external
excavation limitations remain as assessed above.

Local sampling, topology, complete conditional tasks and all central material
outcomes are now integrated for this family. External diagnostic raw custody and
full Item13 family/repetition coverage, final review/fix/thumbs-up, merge and main
delivery remain. Do not mistake this local family result for Item13 COMPLETE.

[Diagnostic custody](../basalt-variant/custody/README.md) now passes immutable
publication, all244 local/download members,503-file downloaded world restore
and identical2,197-cell verification. This resolves the remaining local-family
durability dependency. The full Item13 exit/review/main-delivery gate stays open.
