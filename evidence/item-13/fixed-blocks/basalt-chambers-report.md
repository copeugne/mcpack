# Basalt Chambers: two-assembly quality assessment

Status: IN PROGRESS. This report is the authoritative local family deliverable.
The first representative now has a complete local modeled assessment. The second
assembly, material coverage and final delivery remain pending. Item 14 is UNSTARTED.
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
the repository-root stdin invocation below succeeds without environment changes.

```sh
uv run python - <<'PY'
import gzip, hashlib, importlib, json, math
from itertools import pairwise
from pathlib import Path
r = Path('evidence/item-13/fixed-blocks/basalt-chambers-biome-diverse-r2.json.gz').read_bytes()
assert hashlib.sha256(r).hexdigest() == 'c51074175f8e721caad92936f701a8d8259f940804378931ef7cbd36dddaf2c0'
c = json.loads(gzip.decompress(r))['cases'][0]
at = importlib.import_module('evidence.item-13.render_pilot').state_at
overlap = importlib.import_module('evidence.item-13.collision.clearance').overlaps
removed = {(x,y,z) for x,z in ((4,-500),(10,-492),(4,-486)) for y in (14,15)}
assert all(at(c,*p)['Name'] == 'minecraft:polished_basalt' for p in removed)
full = {'polished_basalt','smooth_basalt','basalt','blackstone','netherrack',
        'crying_obsidian','ancient_debris','spawner','tnt','nether_gold_ore','nether_quartz_ore'}
def shape(x,y,z):
    if (x,y,z) in removed: return None
    state=at(c,x,y,z); name=state['Name'].split(':')[1]
    if name=='air':return None
    if name=='chain':
        a=[6.5/16]*3+[9.5/16]*3; axis='xyz'.index(state['Properties']['axis'])
        a[axis]=0; a[axis+3]=1
    elif name in full or name in {'lava','tripwire','tripwire_hook'}:
        a=[0,0,0,1,1,1]  # fluids/triggers excluded conservatively, not collision claims
    else: raise ValueError(name)
    return [a[i]+(x,y,z)[i%3] for i in range(6)]
def clear(box):
    for x in range(math.floor(box[0]),math.ceil(box[3])):
        for y in range(math.floor(box[1]),math.ceil(box[4])):
            for z in range(math.floor(box[2]),math.ceil(box[5])):
                b=shape(x,y,z)
                assert b is None or not overlap(box,b), (box,(x,y,z),at(c,x,y,z))
def point(x,z):
    floor=shape(x,13,z)
    if floor is not None and floor[4]==14: y=14
    else:
        floor=shape(x,12,z)
        assert floor is not None
        y=floor[4]
    assert at(c,x,math.floor(y-1e-8),z)['Name'].split(':')[1] in full | {'chain'}
    assert floor[0] <= x+.5 <= floor[3] and floor[2] <= z+.5 <= floor[5]
    p=(x+.5,y,z+.5); clear([p[0]-.3,y,p[2]-.3,p[0]+.3,y+1.8,p[2]+.3])
    return p
ab=[(-1,-500),(9,-500),(9,-497),(10,-497),(10,-487)]
east=[(10,-487),(13,-487),(13,-486),(23,-486)]
west=[(10,-487),(9,-487),(9,-486),(-1,-486)]
a_pick=[(-1,-500),(-1,-499),(-2,-499),(-1,-499),(-1,-500)]
c_pick=[(-1,-486),(-1,-485),(-2,-485),(-1,-485),(-1,-486)]
waypoints=a_pick+ab[1:]+east[1:]+list(reversed(east))[1:]+west[1:]+c_pick[1:]+list(reversed(west))[1:]+list(reversed(ab))[1:]
columns=[waypoints[0]]
for a,b in pairwise(waypoints):
    assert (a[0]==b[0]) != (a[1]==b[1])
    dx=(b[0]>a[0])-(b[0]<a[0]); dz=(b[1]>a[1])-(b[1]<a[1])
    columns += [(a[0]+i*dx,a[1]+i*dz) for i in range(1,abs(b[0]-a[0])+abs(b[1]-a[1])+1)]
points=[point(*p) for p in columns]
vertical=0
for a,b in pairwise(points):
    high=max(a[1],b[1]); low=min(a[1],b[1]); vertical+=high-low
    assert high-low<=1
    # One-block rises require a jump. Reserve0.3 head clearance above the upper support.
    apex=high+.3 if b[1]-a[1]>.6 else high
    clear([min(a[0],b[0])-.3,apex,min(a[2],b[2])-.3,max(a[0],b[0])+.3,apex+1.8,max(a[2],b[2])+.3])
    for p in (a,b):clear([p[0]-.3,p[1],p[2]-.3,p[0]+.3,apex+1.8,p[2]+.3])
print(json.dumps({'horizontal_blocks':len(columns)-1,'support_elevation_travel':vertical,'feet_span':[min(p[1] for p in points),max(p[1] for p in points)],'barrier_removals':sorted(removed)},indent=2))

for eye,target in (([-.5,14.62,-499.5],[-2,15.25,-498.5]),
                   ([-.5,14.62,-485.5],[-2,15.25,-484.5]),
                   ([23.5,14.62,-485.5],[25,15.25,-484.5]),
                   ([-.5,14.62,-499.5],[-2.40625,14.5,-498.5]),
                   ([-.5,14.62,-485.5],[-2.40625,14.5,-484.5])):
    assert math.dist(eye,target)<4.5
    clear([min(eye[i],target[i]) for i in range(3)]+[max(eye[i],target[i]) for i in range(3)])
for z in (-499,-485):
    assert at(c,-3,14,z)=={'Name':'minecraft:chain','Properties':{'axis':'y','waterlogged':'false'}}
print('Five conservative interaction-ray bounds clear; both removable support chains match')
PY
```


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
