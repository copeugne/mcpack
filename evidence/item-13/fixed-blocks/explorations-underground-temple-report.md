# Explorations Underground Temple

Status: IN PROGRESS. Local Item13 family assessment. Human times, realized
encounters and acquired loot remain NOT MEASURED under the approved scope.

## Existing evidence, failures and smallest complete coverage

Family/root explorations:underground_temple, Overworld. Reuse the accepted
[provider interpretation](../../item-8/sources/explorations-provider/README.md),
Item8 inventory grouping decision, pool-traces-content and Item13 candidate/start
records. Do not repeat the inventory audit, census or generation. This custom
underground root delegates to jigsaw placement and has room,walkway,shaft,
intersection and terminal components; a template count is not a room count.

The source trace lists22 available selected templates and two missing references:
intrusions/corner and rooms/small_hall_down. The retained start pool has weight80
for rooms/large_hall and20 for the missing rooms/small_hall_down. Its packaged
JSON SHA-256 is c895e99060fd1c7540559cd519e34b977309bafb6e35dc53a5811b07faa77013
in the previously bound Explorations archive420d0373711877a5e1a86b7f9b4f54848f3debb2f116c2509a5cc4eb496c979e.
This source weight is not an observed frequency or permission to repair the pool.

All24 indexed starts are SAVED. Six minimal2x2x2 envelopes each contain only the
missing small_hall_down reference: ocean-heavy r1/r2 at(-23,14) and(9,-19),ordinary
r1/r2 at(-24,-17). These remain failures/limitations in the denominator, not small
complete dungeons. Six repeated cases represent three seed/location pairs, not
six independent sampled designs. The two ordinary r1/r2 starts at(-31,1) have
eight initialize_light chunks at their western padded boundary and cannot serve
as complete whole-assembly examples. The other16 assembled cases have full
required chunks. This is existing frame accounting, not a new density estimate.

No fully bounded assembly pair can cover all22 available templates: large_hall_down
is missing from the union of those16. It is present as child19 in both partially
bounded ordinary(-31,1) starts, with BB[-488,41,45,-472,55,61], CLOCKWISE_180.
That component lies away from the incomplete western edge. The missing variant
is therefore available but not yet integrated, not a reason for new generation.
A targeted read can include its bounds plus the original start chunk anchor,
using full existing chunks and the existing extractor. Do not relabel that read
a complete version of the partially bounded assembly.

Select two distinct-seed complete assemblies whose union covers the21 available
components represented by complete cases. Among all eligible pairs, compare their
sorted(candidate-ID SHA-256,ID) tuples lexically. Execute the smaller volume first.
Then inspect the one missing large_hall_down component, choosing the lower hashed
ID of its two existing partial cases. Retain all six minimal starts and select
one by the same hash order for a bounded failure-class block inspection. No choice
uses gameplay scores, loot rolls or presumed ease of combat.

Smallest complete deliverable: the two complete assembly quality assessments,
all22 available component roles, explicit dispositions for both missing source
references and the minimal/incomplete starts,validated playable topology rather
than piece counts,full conditional traversal/combat tasks,enemy/source distinctions,
hazards/chokepoints,dead/empty counts,loot/finale,bypasses/external exposure and
supported replay/large-but-shallow assessment. Do not mark the family complete
until the first representative, remaining assembly and targeted variant are
integrated. No tuning or missing-template replacement is allowed.

Available source potential includes ordinary spawner NBT for cave_spider,
skeleton,spider,witch,zombie, plus a separate piece-bounded natural override for
illusioner,pillager,vindicator(each weight100,groups4..9). Armor stands are
objects, not enemies. Legacy template payloads require checking against saved
blocks; no generic fallback entity or realized encounter is invented. Loot refs
cover barrel,bedrooms,dead_end,dispenser,dungeon,enchanting,large_room,library,
quest_tower under explorations:chests/underground_temple. Dispenser arrow/potion
inputs alone do not establish a working trap. Verify triggers and routes before
scoring a hazard. Masonry-aging source is reused without tuning.

## Declared selection and resource bounds

[Selection](../underground-temple-selection.json) SHA-256
6e8a56b7fc4f97e2c2e61f45d6cef286172c4cbba788d679536db477bc39ae78.
There are28 eligible distinct-seed pairs covering the21 complete-case components.
The rule selects mountainous r2(-19,0),322,905 padded cells, then ordinary
r1(12,23),329,208 cells. The targeted ordinary r1(-31,1) component read is33,852
cells; its envelope[-496,41,16,-472,55,61] includes the component plus original
start-chunk anchor so the existing extractor can retain exact start NBT. Its
padded chunks are all full in the retained chunk-status record. Preserve the
original assembly's incomplete-edge disposition and census identity alongside
the explicit targeted scope. The selected minimal failure is ocean-heavy
r1(-23,14),512 cells. Total bounded reads:686,477 cells,not a playable-volume metric.

Budget each raw read at180 seconds and10 MiB compressed,5 GiB free minimum.
Comparable recent full-inventory reads took10.37..28.78 seconds before these larger
block volumes; this is context, not an execution-time prediction. At most four
reads are declared. Execute only the first complete assembly until its end-to-end
assessment is integrated. For visual inspection, use relevant saved floor/transition
slices in batches, capped at120 seconds per rendering call,64 MiB total local
SVG intermediates and8 MiB total retained PNGs per assembly. Do not commit large
redundant SVG tooltips. Exact raw blocks resolve details hidden by image scaling.
No server is started and no frozen input is modified.

Reproduce selection with its output absent:

```sh
uv run python - <<'PY'
import gzip,hashlib,itertools,json
from pathlib import Path
from tools.analyze_route_opportunities import read_bound
paths={'candidates':Path('evidence/item-13/candidates.json'),'assemblies':Path('evidence/item-13/start-inspection/summary.json'),'pool_traces':Path('evidence/item-8/sources/pool-traces-content.json.gz')}
raw={k:read_bound(p) for k,p in paths.items()};root='explorations:underground_temple'
candidates={r['id']:r for r in json.loads(raw['candidates'])['candidates'] if r['root']==root}
rows=json.loads(raw['assemblies'])['family_root_dimension_candidates'][root+'|'+root+'|minecraft:overworld']
expected=set(json.loads(gzip.decompress(raw['pool_traces']))['structures'][root]['templates'])
eligible=[r for r in rows if r['start_status']=='SAVED' and not r['incomplete_chunks'] and len(r['named_components'])>1]
covered=set().union(*(set(r['named_components']) for r in eligible))&expected
pairs=[p for p in itertools.combinations(eligible,2) if p[0]['seed_role']!=p[1]['seed_role'] and covered<=set(p[0]['named_components'])|set(p[1]['named_components'])]
key=lambda r:(hashlib.sha256(r['id'].encode()).hexdigest(),r['id'])
pair=min(pairs,key=lambda p:sorted(key(r) for r in p))
selected=sorted([candidates[r['id']] for r in pair],key=lambda r:(r['voxel_count'],r['id']))
missing=sorted(expected-covered);assert missing==[root+'/rooms/large_hall_down']
variants=[r for r in rows if missing[0] in r['named_components']]
variant=candidates[min(variants,key=key)['id']].copy()
world=variant['world'];startpath=Path('evidence/item-13/start-inspection')/(world+'.json.gz');startraw=read_bound(startpath)
start=next(r for r in json.loads(gzip.decompress(startraw))['starts'] if r['id']==variant['id'])
piece,=[r for r in start['start_nbt']['Children'] if r.get('pool_element',{}).get('location')==missing[0]]
envelope=piece['BB'].copy();envelope[0]=min(envelope[0],variant['chunk_x']*16);envelope[2]=min(envelope[2],variant['chunk_z']*16)
bounds=[v-3 if i<3 else v+3 for i,v in enumerate(envelope)]
statuses={(dim,x,z):status for dim,x,z,status in json.loads(gzip.decompress(startraw))['chunk_statuses']}
assert all(statuses[(variant['dimension'],x,z)]=='minecraft:full' for x in range(bounds[0]//16,bounds[3]//16+1) for z in range(bounds[2]//16,bounds[5]//16+1))
variant.update(envelope=envelope,bounds=bounds,voxel_count=(bounds[3]-bounds[0]+1)*(bounds[4]-bounds[1]+1)*(bounds[5]-bounds[2]+1),scope='Targeted large_hall_down plus source-chunk anchor, not whole assembly',component_bb=piece['BB'],start_record_path=str(startpath),start_record_sha256=hashlib.sha256(startraw).hexdigest())
failures=[r for r in rows if r['named_components']==[root+'/rooms/small_hall_down']]
failure=candidates[min(failures,key=key)['id']]
result={'scope':'Two complete assemblies plus retained existing component and missing-template failure','input_sha256':{k:hashlib.sha256(v).hexdigest() for k,v in raw.items()},'candidate_count':len(rows),'complete_assembled_count':len(eligible),'eligible_pair_count':len(pairs),'selected':selected,'component':variant,'failure':failure,'failure_ids':[r['id'] for r in failures],'missing_from_complete_assemblies':missing,'available_template_count':len(expected),'summary':{'reads':4,'families':1,'voxels_before_block_extraction':sum(r['voxel_count'] for r in selected)+variant['voxel_count']+failure['voxel_count']}}
p=Path('evidence/item-13/underground-temple-selection.json');assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n')
print(hashlib.sha256(p.read_bytes()).hexdigest(),result['summary'])
PY
```

First read:

```sh
timeout 180 uv run python - <<'PY'
import gzip,hashlib,importlib,json,resource,shutil,time
from pathlib import Path
from tools.analyze_route_opportunities import read_bound
sha='6e8a56b7fc4f97e2c2e61f45d6cef286172c4cbba788d679536db477bc39ae78'
plan=json.loads(read_bound(Path('evidence/item-13/underground-temple-selection.json'),sha))
selected=plan['selected'][0]
rows=json.loads(read_bound(Path('evidence/item-13/candidates.json'),plan['input_sha256']['candidates']))['candidates']
case,=[r for r in rows if r['id']==selected['id']]
assert case==selected and case['voxel_count']==322905
output=Path('evidence/item-13/fixed-blocks/explorations-underground-temple-mountainous-r2.json.gz')
assert not output.exists() and not output.is_symlink() and shutil.disk_usage('.').free>=5*1024**3
started=time.monotonic()
result={'selection_sha256':sha,'cases':[importlib.import_module('evidence.item-13.measure').extract(case,voxel_budget=322905)]}
result['elapsed_seconds']=round(time.monotonic()-started,6)
result['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
raw=gzip.compress((json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0)
assert len(raw)<=10*1024**2
with output.open('xb') as stream:stream.write(raw)
print(len(raw),hashlib.sha256(raw).hexdigest(),result['elapsed_seconds'],result['peak_rss_kib'])
PY
```

## First accepted saved-block read

GEOMETRIC MEASUREMENT, not runtime gameplay. The first read passed complete-world
inventory verification before and after extraction under the existing lock, with
full required chunks and sections. Raw: [mountainous r2](explorations-underground-temple-mountainous-r2.json.gz),
103,062 compressed bytes, SHA-256
`e86316d3e1fd412a6507533b0f3ac603e3948cb5585d6d95a917fe5168164085`.
Extraction took31.442236 seconds with104,032 KiB peak RSS for322,905 cells, within
the declared budget. The retained61 start children are assembly provenance, not
61 playable rooms. The source child bounds identify candidate activity levels
around Y27,33,37,39; inspect these saved slices before delineating topology.

All33 saved loot assignments use the expected temple namespace. None has an
`Items` field: these are unrolled table assignments, not generated/acquired loot.

| Assigned table suffix | Saved block entities |
| --- | ---: |
| dead_end | 5 |
| library | 2 |
| dungeon | 4 |
| dispenser | 2 |
| quest_tower | 3 |
| large_room | 8 |
| bedrooms | 2 |
| barrel | 6 |
| enchanting | 1 |

These comprise25 chests,six barrels andtwo dispensers. The two trap inventories
remain separate from reward acquisition until their trigger and role are checked.
Room/depth allocation remains pending playable-space delineation.

Nine saved spawners have explicit identities: five cave_spider at(-317,33,-2),
(-308,33,7),(-308,33,28),(-300,33,36),(-268,33,0), plus skeleton(-290,26,-2),
witch(-288,26,-4),zombie(-288,26,0),spider(-286,26,-2). Each corresponding saved
block is minecraft:spawner. All nine have Delay0,MinSpawnDelay200,MaxSpawnDelay800,
SpawnCount4,MaxNearbyEntities6,RequiredPlayerRange16 andSpawnRange4. The five cave
spider sources also have one weight1 matching potential; the other four have empty
potential lists but explicit current SpawnData. These are nine sources andfive
authored enemy identities, not nine realized enemies or a finite clear workload.
An actor activating them can face immediate attempts; do not reuse another
family's positive-delay disablement window or assume one wave clears the temple.
The separate natural override remains an additional source potential.

The padded extraction also contains53 sculk sensors,18 catalysts andthree
shriekers. All three shriekers have can_summon=true andwarning_level0:
(-303,34,-23),(-239,32,-35),(-235,21,-31). The first two are waterlogged; the third
is not. Presence is saved environmental evidence, not proof of a triggered Warden
or an authored temple component. Establish route proximity and source attribution
before adding a hazard/encounter claim. Do not silently erase this environmental
context from a conditional task. Other retained objects include nine campfires,
eight bed block entities,two banners,five skulls,a blast furnace,an enchanting
table andbrewing stand; they are not enemy counts or independent rooms.

Derivation: inspect `cases[0].block_entities`, count exact `id` and `LootTable`
values, and read each spawner/shrieker coordinate through the existing
`render_pilot.state_at` against the same raw palette. All counts above refer to
the padded extraction; temple loot assignments identify their source namespace,
while sculk attribution deliberately remains unresolved. All raw payloads and
coordinates remain available without another world read.

First visual slice command, within the existing rendering budget:

```sh
uv run python evidence/item-13/render_pilot.py --input evidence/item-13/fixed-blocks/explorations-underground-temple-mountainous-r2.json.gz --output evidence/raw/item13/underground-temple-mountainous-r2.svg --layers 27 33 37 39
timeout 120 convert -background white evidence/raw/item13/underground-temple-mountainous-r2.svg evidence/item-13/fixed-blocks/explorations-underground-temple-mountainous-r2.png
```

Remaining first-sample work: validate room partitions and transitions, resolve
lava/bars/shafts/quest-tower access and sculk exposure, then predeclare and measure
a complete conditional objective including active source handling. Traversal,
combat totals, room/branch/dead-room counts, finale and bypass/replay judgments
are not yet accepted for this family. Finish this representative before expanding
to the other three declared reads.

The [four-layer sheet](explorations-underground-temple-mountainous-r2.png) was
visually inspected. PNG242,702 bytes,SHA-256
03394557edd53d6f503bb1d7bc6e30e012ec4b43deefe7551ed0985b6eca6679.
The local SVG is7,830,876 bytes, within64 MiB; the retained PNG is within8 MiB.
White air areas and visible water/cave intersections show why component boxes
cannot establish playable rooms. These selected slices do not validate all
vertical links, collision shapes or external entry. Exact block coordinates remain
the authority where the displayed sheet is reduced.

SOURCE INSPECTION: none of the22 hash-matched packaged template palettes includes
any sculk-named block. This excludes authored template placement of the observed
sculk, without claiming which surrounding generation pass placed each block.
Reproduce the narrow attribution check against the existing trace:

```sh
uv run python - <<'PY'
import gzip,hashlib,json,zipfile
from mcpack_evidence.item7_nbt import decode_compound_nbt
trace=json.load(gzip.open('evidence/item-8/sources/pool-traces-content.json.gz'))
root='explorations:underground_temple'
with zipfile.ZipFile('downloads/item3/candidates/explorations-neoforge-1.21.1-1.6.2.jar') as archive:
    for name in trace['structures'][root]['templates']:
        source=trace['template_contents'][name]['source']
        raw=archive.read(source['path'])
        assert hashlib.sha256(raw).hexdigest()==source['sha256']
        nbt=decode_compound_nbt(gzip.decompress(raw))
        assert 'palette' in nbt and 'palettes' not in nbt
        assert not any('sculk' in state['Name'] for state in nbt['palette'])
print('22 source templates: no authored sculk palette entries')
PY
```

Focused verification passed: the declared selection rebuilt byte for byte in a
separate temporary output, all22 template hashes and the no-sculk palette check
passed, and the retained raw hash,322,905 cells,61 children,nine spawners and33
unrolled assignments matched the report. The staged whitespace check passed.
An initial documentation-edit command failed at heredoc parsing before applying
any edit; the corrected patch succeeded. No raw extraction or runtime failed in
this batch. Broader Item13 quality and delivery gates remain outstanding.

## First assembly: validated hall topology and native obstruction

This increment resolves two activity spaces and their immediate native links.
It does not yet give the whole-assembly room count or complete timing scenario.
The actor for these static checks is an upright adult,0.6 blocks wide and1.8 high,
with known coordinates and ordinary walking/one-block ascent capability. No
mining,placement,flight,swimming or hostile displacement is included. Stair links
use a conservative jump envelope0.3 above the higher endpoint, following the
existing local route-check convention. These are geometric feasibility checks,
not observed movement or a claim of safe combat traversal.

The existing clearance overlap predicate and saved-block decoder are reused by
[the family route check](../underground_temple_route.py). New executable logic is
limited to the required layout-specific paths and their support/clearance checks;
the existing family scripts bind different raw layouts and cannot validate these
coordinates. Every non-air cell is conservatively avoided as a full cell, with
wall/fence upward extension. Supporting straight bottom stairs are explicitly
checked: the centered actor overlaps their upper half. Waterlogged support remains
below the actor's feet. No unknown partial block is silently treated as air.

| Space | Delimitation and connected floor | Validated doors | Reward/facility role |
| --- | --- | --- | --- |
| H0 | First curved hall inside X-296..-280,Z-8..8; central playable floor Y37, door thresholds Y39 | North(-288,39,-8),south(-288,39,8),west(-296,39,0),east(-280,39,0) | Four large_room chests around central gold block(-288,37,0) |
| H1 | Second curved hall inside X-296..-280,Z20..36; central playable floor Y37, door thresholds Y39 | North(-288,39,20),south(-288,39,36),west(-296,39,28),east(-280,39,28) | Four large_room chests around central gold block(-288,37,28) |

These are two primary rooms, not eight chest rooms or eight stair rooms. Each
has four validated five-horizontal-block radial connections from its threshold
to a common central floor circuit, with two blocks of floor elevation change.
A24-horizontal-block circuit around the central rewards connects all four spokes.
Both directions pass support,standing and swept-clearance checks. The two-block
floor span is internal progression, not graph depth or the14-block envelope elevation span.
The bounding rectangles locate the rooms; they do not claim every enclosed block
is playable. Full geometry remains in the raw file and explicit paths.

Eight radial chest approaches have unobstructed sampled interaction rays shorter
than4.5 blocks and clear lids. This proves access to assigned containers from the
validated floor, not acquired loot or a completed item-transfer phase. The source
large_hall template contains one gold block at local[8,1,8], matching each saved
central gold block after its retained rotation/translation. These are authored
physical rewards separate from the eight unrolled table assignments. Mining and
pickup are not yet included in a complete task. Neither H0 nor H1 is empty or dead
under the room definitions, since each has this supported reward role. Their
status as an authored finale is not inferred from those rewards.

The northern corridor center X-288,Y39,Z-8..-20 passes in both directions:
12 horizontal blocks. Within its component Z-19..-9, the three interior columns
X-289..-287 are air atY39..40 over masonryY38, with a ceiling atY42. A wall torch
at(-287,41,-14) occupies the upper layer; the2-block guaranteed empty height is
sufficient for the declared upright actor. Ten iron-bar
blocks are at the side walls X-290/-286,Y40,Z-18/-16/-14/-12/-10. They do not form
a centerline gate. The name iron_bars therefore does not establish an obstructed
route. The corridor narrows the hall to a three-block-wide passage;
full-assembly alternate-route availability remains pending.

The northern junction centered(-288,39,-23) has three checked native arms toward
north,south andwest. The western junction centered(-300,39,0) has three toward
east,north andsouth. The first hall's west threshold connects to that junction
with four horizontal blocks. These are established local connection choices;
they are not yet accepted whole-assembly branching totals, since remaining shaft,
quest-tower and longer-loop connectivity still need validation.

The direct southern corridor is a meaningful supported lava obstruction. Its
center X-288,Y39 has lava atZ11..17. AtZ12..16 every interior column X-289..-287
contains lava atY39, so a straight walking-level dry crossing cannot use a side
column. Source lava is saved at(-289,42,13) and(-287,42,15), with falling columns
throughY41 and40. This is a route-intersecting mechanism, not an inference from
a template name or isolated palette entry. Preserve the native centerline as
REJECTED for the declared dry walking actor. A raised crossing, source plugging
or a longer alternate path needs its own placement/access/fluid and cost checks;
none is accepted merely because adjacent air appears on the slice sheet. No
whole-family impossibility, unavoidable damage or live fluid response is claimed.

Reproduce the accepted partial links and explicit native obstruction:

```sh
uv run python -m evidence.item-13.underground_temple_route
```

The command passes both hall spoke/circuit checks,northern corridor,two junction
arm sets,western hall link andeight chest approaches, then reports the rejected
native lava centerline. An initial direct-file invocation failed to import the
repository namespace; the module invocation above is the reproducible command.
This was a command invocation failure, not rejected saved geometry. A broader
all-air assertion atY39..41 later failed on the wall torch at(-287,41,-14); the
corrected two-block empty-height claim above passes without ignoring that block.
The original centerline route remained valid. The full
assembly still requires the remaining playable rooms,source handling,complete
conditional task,bypasses and quality assessment before further declared reads.


The final affected checks pass: module execution,ruff formatting/lint and
basedpyright with zero errors/warnings. No server or world modification was
needed. The first assembly remains a partial local assessment; the accepted
hall geometry and explicit lava rejection must be reused in the complete task.

## Eastern shaft: connection declaration before validation

The eastern hall doorway leads to the upper shaft at center(-276,0). Source
children4 and9 are vertically adjacent, but a piece junction is not climbability.
Saved blocks show a3 by3 opening X-277..-275,Z-1..1 throughY36..38 over a lower
masonry floorY32. There are no ladder blocks in this local shaft. The upper ledge
is at feetY39 and lower floor atY33, a six-block descent requiring an explicit
return capability. The shaft is a connection, not a reward room merely because
its source name contains dead_end.

Predeclare a local connection demonstration using six carried scaffolds. Retain
the previous adult geometry and add ordinary controlled descent and scaffolding
climb. Start on the first hall's eastern threshold(-279.5,39,0.5), equivalently
block-column(-280,39,0) with actor centered atX-279.5. Walk east to column-278,
step east into column(-277,0), descend to feetY33, then step west to(-278,33,0).
Place a scaffold base at(-277,33,0) on its full masonry floorY32. Five ordinary
side clicks on the base's west top rail at(-277,33.95,0.5) extend the supported
stack upward throughY38. Reuse the pinned side-click-UP and distance-zero stack
rules from the [Nether Tower scaffold derivation](mns-nether_tower-report.md#elevated-chest-explicit-scaffold-connection).
The adjacent lower stance is centered(-277.5,33,0.5), with eyeY34.62; the side
click remains local rather than requiring direct reach to the new top block.
Re-enter the scaffold column, climb to feetY39, step west onto the original
ledge and return to the hall threshold. Construction remains in place.

This is a conditional connection demonstration, not the whole clear. No extra
mining,fluid modification,flight or pre-existing scaffold is assumed. Validate
all floor/column/headroom cells before accepting this link. Failure to place,
climb,land alive or avoid hostile displacement censors the demonstration. The
nearby cave-spider source remains active potential; this isolated geometry does
not suppress it or count zero combat in the future complete objective.

Initial descent is not described as damage-free. Pinned LivingEntity.calculateFallDamage
computes ceil((fallDistance-SAFE_FALL_DISTANCE)*surfaceMultiplier*FALL_DAMAGE_MULTIPLIER)
for nonimmune types, and causeFallDamage passes positive damage to hurt. Pinned
Attributes defaults are safe distance3 and multiplier1. A stipulated six-block
fall distance on ordinary masonry therefore requests3 damage before any runtime
hooks or subsequent damage handling. This is SOURCE INSPECTION and a conditional
calculation, not a measured player health delta. The complete task must retain
fall exposure and survival, rather than inventing free recovery or assuming live
mods preserve that exact health change. Runtime fall distance and realized damage
remain NOT MEASURED.

The declared shaft geometry passes the existing family command. The upper
approach from column(-280,39,0) to(-278,39,0) has two supported horizontal steps.
The shaft column(-277,0) is clear throughY33..40, with full mossy stone bricks
atY32; the lower adjacent working stance is also supported and clear. Both the
initial floor-top placement ray and subsequent base side-click ray are within
4.5 blocks with intervening air. The six hypothetical scaffold cellsY33..38 give
a top atY39; the source-supported climb and return transfer fit the inspected
column. This establishes a conditional constructed link, not runtime placement.
The setup circuit has eight horizontal and twelve vertical blocks, six placements
and retained initial fall exposure. These are components awaiting integration
with navigation,interactions,combat and other task costs, not a completion time.

The lower junction centered(-276,33,0) has three validated horizontal arms toward
east,north andsouth, each three blocks long, plus connection to the landing/base
station(-277,33,0). Both directions pass. Under the declared scaffold capability
this junction connects back to H0, expanding its reachable floor span toY33..39.
Further spawner/broken walkways remain to be validated; neither their names nor
this shaft result proves their full traversability. No additional primary reward
room or whole-dungeon branch/depth count is assigned to the shaft itself.

Fall-source derivation uses the same pinned SRG archive as prior local models,
SHA-25626ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71.
Inspect LivingEntity.calculateFallDamage offsets15..45 and causeFallDamage34..43;
Attributes initialization264..293 and625..653 records the two relevant defaults.
Reproduce inspection without a server:

```sh
item13_srg=instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar
sha256sum "$item13_srg"
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath "$item13_srg" -c -p net.minecraft.world.entity.LivingEntity
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath "$item13_srg" -c -p net.minecraft.world.entity.ai.attributes.Attributes
```

The extended module and affected lint,formatting and type checks pass. No raw
world or configuration was modified and no new experiment was run. This resolves
the first shaft connection only; the complete first-assembly objective and
remaining material coverage still require the work recorded above.

## Lower north/south branches: declaration

Next validate the two rubble passages from the eastern lower junction to their
terminal alcoves. Keep the known-layout adult and no-mining/no-placement scope
for these native branches. Use X-276; the southern route runs Z0..17 with feetY34
atZ7..9 andY33 elsewhere. The northern route runs Z0..-17 with feetY34 atZ-7..-9
andY33 elsewhere. Predeclare crouching for one-block upward transitions where
needed; retain an upright-only failure rather than silently accepting headroom.
The connected rubble elevations are not additional rooms.

Pinned Blocks registration uses noCollission for vine at offset13375 and
sculk_vein at36523. Permit the known vine and nonwaterlogged sculk-vein cells in
collision checks; retain waterlogged variants as excluded fluid cells. This fixes
a concrete overconservative representation of encountered plants, without treating
cobwebs,fluids or unknown states as empty. Source climbability is not measured
climbing speed. Gravel supports must have full masonry immediately below; no
unsupported falling-block platform is accepted. Validate endpoint chest access
and distinguish the northern campfire alcove from an empty/dead room.

The proposed native center routes are REJECTED. The southern standing-volume
check intersects cracked stone bricks at(-276,34,8); the northern check intersects
stone bricks at(-276,34,-8). Both sites have a second solid layer above the
assumed Y33 rubble support, so feetY34 is not a valid stance. Crouching cannot
resolve a block intersecting the actor's feet. This failure occurs before any
accepted ascent/return sweep. The17-block route lengths are proposals,
not accepted traversal measurements. Do not assign the terminal alcoves to the
reachable-room denominator from these failed paths.

The source-verified plant collision correction remains valid independently of
that failure. It supersedes the earlier literal all-non-air avoidance rule only
for vine and dry sculk vein. Solid blocks,waterlogged vein and cobwebs retain
conservative exclusion. No template or saved world is modified. The route
command now requires both exact standing obstructions to be reproduced and
reports them as REJECTED while preserving the previously accepted hall/shaft
checks. This is a retained failed local attempt, not a complete branch model.

Next resolve an actual detour or predeclared breach through these passages,
including interaction access and costs. Do not silently raise the proposed feet
position: ceiling clearance and the opposite-direction return need validation.
The nearby spawner corridor and enchanting room also remain unresolved. Reuse
these raw cells; no additional world extraction is needed.

Reproduce the narrow plant-source inspection using the same hash-bound SRG path
from the previous section and the pinned javap executable:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath "$item13_srg" -c -p net.minecraft.world.level.block.Blocks
```

Blocks offsets13356..13384 identify vine and its noCollission call; offsets
36504..36529 identify sculk_vein and its noCollission call. These are collision
facts, not proof that aiming/mining rays ignore plant outline shapes.

Focused module execution,formatting,lint and types pass with both rejected
rubble attempts explicitly reproduced. Full branch access remains unresolved.

## Explicit rubble breach declaration

Retain the failed native routes. For a separate constructed-access case, predeclare
a diamond pickaxe for masonry and bare hand for gravel/vine, sufficient durability,
no effects,full health/food and the previously declared adult geometry. Remove
only four center rubble blocks per branch: Y33 atZ7,8,9 andY34 atZ8 in the south;
Y33 atZ-7,-8,-9 andY34 atZ-8 in the north. Work from the adjacent already-cleared
center column atfeetY33, beginning atZ6 or-6. Mine the near Y33 block,advance one
block,remove the upper then lower middle block,advance one block,andremove the
far Y33 block. In the south, first remove the vine at(-276,34,7) after advancing
toZ7 andbefore aiming at the middle upper block. It otherwise lies across that
forward aiming ray. This is five manual removals south andfour north; additional
natural vine detachment is not charged as manual work or required for collision.

Use the source VineBlock outline unions for mining rays: active north/south,
east/west andup faces are1/16-thick plates at the respective cell boundaries.
VineBlock.getShape returns that cached union; a no-face state returns a full cube.
This differs from empty collision. Other unremoved non-air ray cells remain
conservatively opaque. Require a supported stance and a clear ray within4.5 blocks
for every ordered removal. Retain the raw blocks unchanged and apply removals only
to the explicitly modeled working set. Then validate both return routes atY33
and the southern chest's lid/interaction ray. Debris drops are outside acquisition;
no loot transfer,combat or total time is implied by this geometry.

The ordered breach case passes for both branches. All nine manual targets have
supported working stances and checked aiming rays. The resulting center routes
run atfeetY33 from the lower junction toZ17 or-17 andback:34 horizontal blocks
per branch,zero vertical travel. Both directions pass. No fabricated room
connection is inferred from the earlier rejected one-block-rubble model.

Active breaking work under the declared dry,grounded,no-effect tools and20 TPS
is six ticks per masonry block,18 per bare-hand gravel andsix for the bare-hand
vine. This follows the existing correct-tool progress rule(speed/hardness/30)
with masonry hardness1.5 anddiamond speed8,gravel hardness0.6 andhand speed1,
vine hardness0.2 andhand speed1. Pinned Blocks gravel strength is at1774..1777;
vine strength at13381..13384; stone-brick material uses the stone legacy copy.
Each branch has three masonry blocks andone gravel:36 active ticks(1.8s) north,
plus one vine south:42 active ticks(2.1s). These are active breaking components,
not complete traversal/combat times. The approved targeting/input allowances
include initiation andinter-block delay; tool selections,decisions,inventory
work andencounters still belong in the complete task. Reproduce single-precision
progress accumulation rather than assuming mathematical rounding:

```sh
uv run python - <<'PY'
import struct
f=lambda value:struct.unpack('f',struct.pack('f',value))[0]
for hardness,speed in ((1.5,8),(.6,1),(.2,1)):
    progress=f(f(f(speed)/f(hardness))/f(30));total=0;ticks=0
    while total<1:
        ticks+=1;total=f(total+progress)
    print(hardness,speed,ticks,ticks/20)
PY
```

Southern terminal chest(-278,33,17) is single,east-facing andhas a dead_end table
assignment. Its interaction ray from the validated endpoint passes. The first
blanket air-above assertion failed because(-278,34,17) is a straight,top-half,
west-facing stone-brick stair. Preserve that failed assertion; it was not proof
that the chest was blocked. Pinned ChestBlock.isBlockedChestByBlock checks the
above state's isRedstoneConductor predicate. Blocks.legacyStair uses
Properties.ofLegacyCopy, retaining the constructor's default predicate, which
Properties constructor bootstrap3 binds to lambda$new$4: isCollisionShapeFullBlock.
The straight stair's top-half-plus-half-bottom shape is not a full cube. Thus this
above block does not block opening under the source rule. No stair removal is
required in this scenario. Entity blockers such as sitting cats remain excluded
by the conditional task, not measured absent from a live trial. Generated items,
opening/transfer success andacquired loot remain NOT MEASURED.

The two terminal alcoves each have a lit,nonwaterlogged campfire at(-275,33,-17)
and(-275,33,17), beside the checked center endpoint. These give an authored
cooking/rest facility andoptional contact hazard; walking the declared centerline
does not intersect their cells. The northern terminal is therefore not labeled
empty/dead solely from the name dead_ends/normal or lack of a chest. The southern
terminal also has the validated assigned chest. Final room-graph delineation
must retain these activity roles and any corridor/alcove count sensitivity.
Neither terminal is promoted to an authored finale merely for ending a branch.

Source reproduction uses the pinned SRG identity and javap path already recorded:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath "$item13_srg" -c -p net.minecraft.world.level.block.VineBlock
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath "$item13_srg" -c -p net.minecraft.world.level.block.ChestBlock
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath "$item13_srg" -v -p 'net.minecraft.world.level.block.state.BlockBehaviour$Properties'
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath "$item13_srg" -c -p net.minecraft.world.level.block.StairBlock
```

VineBlock initializer78..167 defines the outline plates; calculateShape combines
active faces andgetShape returns the cached union. ChestBlock's block-obstruction
method0..17 supplies the predicate above. StairBlock.getShape0..32 selects the
state-specific top/bottom array. This is source/geometry evidence, not an observed
client opening or a tick-accurate mining trial.

The extended module,formatting,lint andtype checks pass. Earlier native rubble
failures remain required outputs. This resolves the two lower branches locally;
the spawner corridor,other rooms andcomplete first-assembly task remain pending.

## Eastern spawner corridor: ordered clearance declaration

Continue from the lower junction(-276,33,0),using the declared grounded adult,
iron sword anddiamond pickaxe,with no effects or mining interruptions. Keep feetY33
andZ0 through the eastern corridor to the next junction atX-248. Predeclare six
cobweb removals with the sword: (-271,34,0),(-269,34,0),(-268,34,0),(-267,33,0),
(-265,34,0),(-265,33,0). Mine the spawner(-268,33,0) with the pick immediately
after the third web, before entering its column. Work from the adjacent cleared
western column,with the two X-265 webs worked fromX-266. Validate each stance,
aiming ray andthe resulting forward/return passage before accepting this link.
Other cobwebs remain; no collision exemption for webbing is introduced.

Pinned SwordItem.createToolProperties supplies a minesAndDrops rule with speed15
for cobwebs(offsets4..12); Blocks registers cobweb hardness4 at4435..4438.
The nominal correct-tool work is eight ticks per web. Spawner work is19 ticks,
reusing the accepted hardness5/diamond-speed8 derivation. The discovered Slime
Cave1.9-second mismatch has been narrowly corrected in its own report/script;
do not propagate it here. These seven removals total67 active ticks,3.35 seconds
at20 TPS. Targeting,input delay,tool changes,movement andencounters still need
their separate complete-task accounting. String/experience collection is not
part of this corridor-clearance component.

The saved source has Delay0 andthe previously recorded cave-spider assignment.
It may attempt spawning before the actor reaches its mining stance. This ordered
geometry does not establish zero spawned enemies or one-wave completion. Preserve
that source lifecycle in the later complete encounter model. Any displacement,
mining interruption or additional blockage is outside this ideal clearance check.

The corridor clearance passes: all seven ordered targets have supported,clear
stances andunobstructed rays; intervening advances are checked before each action.
After those declared removals, the Y33 centerline fromX-276 toX-248 is clear in
both directions,28 horizontal blocks each way(56 return total),with no vertical
travel. The next junction is reached; its other arms andthe enchanting room are
not yet accepted by this centerline check. There is no reward room or loot
container inside this connection merely because it contains a source.

Webs are a meaningful source-supported movement hazard,not solid collision.
Pinned WebBlock.entityInside0..70 passes(0.25,approximately0.05,0.25) to
Entity.makeStuckInBlock for the declared no-effect actor; WEAVING changes that
vector andis excluded here. The six removed webs intersect the declared body
path. Remaining overhead/side webs do not intersect its upright envelope; jumping,
combat displacement or a wider actor would require another check. The source and
webs create potential exposure pressure while clearing, not a measured difficulty
rating or observed AI chokepoint exploit.

The source center(-267.5,33.5,0.5) is already within its16-block activation range
of the lower-junction actor center(-275.5,33,0.5),distance sqrt(64.25),about8.02.
It is also within range of the first hall's eastern threshold(-279.5,39,0.5),
distance sqrt(174.25),about13.20. If ticking with an alive actor, activation can
therefore precede entry into this corridor. Do not start the later encounter clock
only at the first web. Zero-delay source state andthis earlier exposure rule out
a claim of guaranteed spawn-free access based solely on the0.95-second mining
work. Actual spawning,targets killed andcombat time remain NOT MEASURED.

Reproduce the source-specific web/tool mechanisms alongside the existing module:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath "$item13_srg" -c -p net.minecraft.world.item.SwordItem
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath "$item13_srg" -c -p net.minecraft.world.level.block.WebBlock
uv run python -m evidence.item-13.underground_temple_route
```

Affected module execution,formatting,lint andtypes pass. This batch adds one
validated connection andits source/hazard disposition, not a complete temple
encounter model. No server,world mutation or repeated extraction was needed.

## Enchanting room: native door and reward-route declaration

The eastern junction's south arm leads to a closed iron door at(-248,Y33..34,5),
facing south,hinge right. An exterior north-facing oak button is at(-249,34,4),
attached to full stone bricks(-249,34,5) beside the upper door. An interior
south-facing button is at(-248,35,6),attached to full stone bricks(-248,35,5)
above that upper door. These are explicit power connections,not a presumption
that any button in a palette opens a door.

Predeclare ordinary button use rather than door removal. The known-layout adult
approaches at(-248,33,3),aims at the exterior button's north plate at
(-248.5,34.5,4.9),then crosses to(-248,33,6). Plan orientation before pressing;
make no other interaction between activation andcrossing. On return,press the
interior button from(-248,33,6),aiming at(-247.5,35.5,6.1),andcross back toZ3.
Pinned woodenButton constructs a30-tick button. At20 TPS the1.5-second window
exceeds a declared three-block transfer at3 blocks/s(1s) in every profile.
The entrance contains vine; do not apply the higher open-floor profile speeds
through this transfer. This is a conditional rate, not an observed crossing.
Failure to cross before closure,hostile displacement or interrupted input censors
this native-door scenario; no free retries or permanent-open state are assumed.

Validate both rays andthe opened-door sweep. For this north/south-facing door,
conservatively exclude both possible side plates of thickness3/16; a centered
0.6-wide actor fits between them. This modeled opening does not alter raw state.
ButtonBlock.press schedules release andupdates neighbours; its powered signal
anddirect signal reach15. DoorBlock's neighbour check considers both halves and
updates OPEN/POWERED. The two full supporting masonry blocks transmit the signal
to the upper door. Successful live button operation remains NOT MEASURED.

From the inside threshold,clear web(-249,33,6) with the sword from(-248,33,6),
walk west toX-251 alongZ6,then south toZ9. Clear web(-252,33,9) from(-251,33,9),
step west to(-252,33,9),andinspect chest(-252,33,10). Return by the same path and
button sequence. These two web removals add16 active ticks(0.8s); button inputs,
alignment andinventory work require their separate full-task allowances. Check
the chest ray andabove-block rule without assuming air. Enchanting/brewing
facilities are assessed separately from acquired loot or performed recipes.

The enchanting-room case passes the family module. Both button rays meet the
source plate bounds; their full supporting blocks andexact closed-door halves
match the declaration. The conditional opened-door sweep passes in both
directions. The3/16 side-plate exclusion leaves a0.625-block middle channel for
the0.6-wide actor. This narrow,button-timed connection is a chokepoint under the
declared scenario, not proof of live enemy exploitation. Successful passage
still depends on alignment andthe explicit activation window.

After the two ordered web removals, the inside-threshold-to-chest route is seven
horizontal blocks each way. Including the six blocks from the eastern junction
to the inside threshold gives26 horizontal return blocks andzero vertical
travel for this branch. Both button events andthe two web targets remain required
full-task inputs. No door is mined andno permanent-open state is assumed between
visits. The raw door remains closed in the retained evidence.

Delineate E as one primary room: the irregular activity interior within
X-252..-244,Z6..10,aboveY32 masonry,entered through the single door atZ5. The
coordinate rectangle bounds the space; furniture andwalls within it are not all
playable cells. The checked route connects the entry to its western reward corner,
andfacility rays establish access from that connected floor. Shelves andfurnishings
are not separate rooms. E has one unrolled enchanting loot-table assignment in
chest(-252,33,10),an enchanting table(-250,33,7) andbrewing stand(-245,33,7).
It is neither empty nor dead under the declared definitions. It is not identified
as an authored finale merely because the chest lies behind a door.

The chest has a cobweb immediately above. Reuse the pinned ChestBlock
redstone-conductor test: cobweb's noCollission registration makes its collision
shape non-full,so this block does not block opening under that rule. The chest
ray from(-252,33,9) passes below the overhead web andmeets the inset north face.
Entity blockers remain excluded conditionally. Enchanting-table access is from
(-251,33,7); brewing-stand access is from the inside threshold(-248,33,6).
Their rays pass without additional movement or removals. Enchantment power,
required materials,performed recipes,generated rewards andactual menu/transfer
success remain NOT MEASURED. These are supported facility opportunities.

Source commands,using the same pinned SRG path andidentity already recorded:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath "$item13_srg" -c -p net.minecraft.world.level.block.ButtonBlock
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath "$item13_srg" -c -p net.minecraft.world.level.block.DoorBlock
```

Blocks.woodenButton offset5 sets30 ticks. ButtonBlock.press0..35 sets powered,
updates neighbours andschedules release; getDirectSignal0..29 provides15 in the
connected direction while powered. Its initializer109..152 defines the
north/south button plates. DoorBlock.neighborChanged checks power atboth halves;
its opened north/south-facing states select the east/west3/16 plates. These
source mechanisms support the declared static/timed model, not a runtime test.

The extended module,formatting,lint andtypes pass. The next work remains other
junction arms,rooms andsource lifecycles before whole-assembly counts orcomplete
conditional timing. This branch does not authorize expansion to new world reads.


The initial open-floor crossing proposal(0.6/0.75/1s) is superseded above because
the entrance contains vine. Pinned LivingEntity.handleOnClimbable offsets15..42
clamps horizontal components toapproximately0.15 blocks/tick. The corrected
scenario uses3 blocks/s for the whole three-block door transfer in all profiles,
retaining its1.5-second button deadline. Acceleration/input disruption can still
violate that stipulated rate andcensor the crossing; source inspection does not
prove a human will maintain it. Carry this local rate into complete task timing.

## Eastern junction north arm: blind shaft alcove declaration

The north arm from(-248,33,0) reaches a bounded shaft alcove insideX-250..-246,
Z-9..-5. Its outer floor isY32 masonry; the central3 by3 opening meets terrain
aroundY31, not another authored shaft component. This differs materially from
the earlier six-block eastern shaft with a generated lower assembly. Reuse source
child59 andthe same saved blocks. No new depth is inferred from the component name.

Predeclare a native inspection circuit from the junction to(-248,33,-5),west to
X-250,north toZ-9,east toX-246,south toZ-5,andback west toX-248. Then inspect the
central pit through(-248,32,-6),(-248,32,-7),(-248,32,-8),return to the rim and
junction. Keep the adult geometry,no mining/placement andknown coordinates.
The central-column support is full stone atY31; dry sculk-vein cells are handled
by the already verified collision rule. Validate the rim,one-block pit descent
andreturn ascent against actual headroom. Do not substitute the earlier scaffold
solution or claim another six-block drop.

The component's retained bounding volume has no block entities. The central
lantern at(-248,35,-7) is illumination,not a storage objective. There is no saved
container or authored spawner in this alcove. Empty/dead classification remains
conditional on the complete encounter model: the root's piece-bounded natural
illusioner/pillager/vindicator potential is not erased by absence of a block
entity. The static lack of reward/facility is an established fact; no realized
enemy absence is asserted.

The declared circuit passes the saved-block support, adult clearance and swept
transition checks in `uv run python -m evidence.item-13.underground_temple_route`.
It comprises five blocks from the junction to the rim, a sixteen-block rim
circuit, six horizontal blocks for the pit return, and five back to the junction:
32 horizontal blocks and two blocks of vertical travel. Accessible feet elevation
is32..33. No additional scaffold, removal or interaction is required by this
geometric route. This is an optional terminal inspection space, not a demonstrated
deeper connection or a finale. Its room-count sensitivity and conditional empty
classification must be carried into the whole-assembly graph and scenario.

The first focused lint invocation rejected a113-character output line; formatting
corrected that presentation defect without changing the measured path or raw data.

## Eastern terminal connector declaration

Continue the same native inspection actor from(-248,33,0) east to(-241,33,0),
then inspect the east arm throughX-238, the north arm throughZ-3 and the south
recess throughZ2, returning along each arm and finally to the original junction.
No excavation or fluid entry is permitted in this circuit. Child60's serialized
three-way label does not establish three onward playable links: retained terrain
at(-237,33,0) and(-241,33,-4) caps the east and north centerlines, while authored
masonry at(-241,33,3) bounds the south recess. Validate occupied cells, support and
all transitions with the existing adult checker. A capped centerline is a local
native boundary, not proof against mining or against every external cave approach.

The objective is inspection of these branch ends, not acquisition. Check block
entities within child60's boundsX-244..-238,Y32..36,Z-3..3. As for the north shaft,
absence of saved reward/source nodes would not establish realized enemy absence;
retain the piece-bounded natural-spawn condition. Keep this connector distinct
from primary activity rooms when integrating the room graph.

The declared connector circuit passes in both directions: seven blocks to the
connector center, three east, three north and two south, each returned, total30
horizontal blocks and zero vertical travel. Its retained bounding volume has no
block entities. The two local terrain caps and the south masonry boundary are
confirmed at the declared coordinates. Do not count the serialized three-way
element as a junction connecting three further rooms. Both terminal inspections
reuse the existing hash-bound raw extraction and executable route checker; no
world was launched, changed or regenerated. Focused Ruff, formatting and type
checks pass after formatting the two added output/assertion expressions.

## Quest tower upper-floor declaration

Inspect child10 using the retained block extraction. Its four stacked floor
bands are not automatically four accessible rooms. The top level has an entrance
vestibule, a two-chest compartment behind an iron door, and a northern hatch
compartment behind another iron door. Lower levels contain a further chest,
tripwire/dispenser ingredients, iron doors, hatches and lava. Resolve those links
and the trap before assigning full tower topology or timing.

For the upper approach, use the existing adult actor and iron sword. From the
northern junction(-288,39,-23), walk north toZ-27, east toX-287, then north toZ-29.
Remove the single web at(-287,39,-30) from that stance, then advance toZ-31.
Activate the south-facing stone button at(-287,41,-31), cross the north-facing
iron door atZ-32 and stop atZ-33. Orient before activation; the two-block crossing
uses the declared profile movement rate with no intervening action. Repeat from
the north-facing button at(-287,41,-33) on return. Verify both button rays and
their attachment above the door. Retain closure or interruption as censoring.

Inside, visit(-289,39,-33) for the west chest at(-290,39,-33), then walk north
toZ-34, east toX-287, north toZ-35 for the east chest at(-286,39,-35). Return
along that path and through the door to the original junction. Check chest lids,
actual inset-face interaction rays and adult route clearance. This route resolves
only the upper rewards; it neither clears the lower tower nor bypasses their
required assessment. One web costs eight active sword ticks under the existing
source model. Full objective time remains unresolved until the tower and remaining
assembly are integrated.

The upper two-chest circuit passes: nine horizontal blocks to the door approach,
two across it, six between the declared reward stations, all returned, giving34
horizontal blocks and zero vertical travel. Both chest lids have air above them
and their inset-face rays pass. The web removal ray and both button rays also
pass. These are two of the three saved `quest_tower` table assignments, still
unrolled, with no acquired items asserted. This supports an upper reward room
separate from its entrance vestibule; it does not establish a terminal finale.

The pinned server `Blocks.stoneButton()` bytecode passes20 ticks to `ButtonBlock`
at offsets7..27, unlike the earlier oak button's30 ticks. Reuse the bound SRG
archive and `javap -c -p net.minecraft.world.level.block.Blocks` command above.
The two-block crossing costs0.4/0.5/0.666667 seconds under profiles A/B/C, each
below its one-second source deadline. No aim or inventory action is permitted
after pressing until clear of the doorway. The source mechanism and conditional
constant-rate model do not prove successful human operation. One web contributes
0.4 seconds of active mining; decisions, selection, presses, acquisition and
verification remain separate phases in the eventual complete objective budget.
The route command, focused Ruff and type checks pass after formatting. The saved
world and raw extraction are unchanged.

## Tower hatch trap and alternate descent declaration

The upper hatch at(-288,38,-39) is directly above attached, armed tripwire at
(-288,35,-39). The three wire cells spanX-289..-287 between hooks atX-290 and
X-286, bothY35,Z-39. Facing-inward dispensers are immediately above those hooks,
atY36. Their saved `triggered=false` state and unrolled dispenser tables are not
observed firing or damage. The packaged dispenser table has three rolls, each
selecting ordinary arrows (9..27) or tipped arrows of slowness/weakness (5..15).
This is ammunition potential, not generated contents.

Pinned-source `TripWireBlock.entityInside` calls `checkPressed`, which queries
entities intersecting the wire shape. `TripWireHookBlock.getSignal` emits15 when
powered; a dispenser immediately above a hook can receive that neighbor signal.
`DispenserBlock.neighborChanged` schedules its action four ticks after a new
powered state. Thus the hatch landing intersects a supported projectile-trap
trigger, conditional on source updates and resolved ammunition. Do not assign
an observed hit count, potion effect or health loss. The saved wire's westmost
connection flags differ from the middle wire, but all three cells and both hooks
retain `attached=true`; activation is a source-supported potential, not an
automated circuit test.

Reproduce this inspection with the previously hash-bound SRG on the classpath:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar -c -p net.minecraft.world.level.block.TripWireHookBlock net.minecraft.world.level.block.TripWireBlock net.minecraft.world.level.block.DispenserBlock
```

For an explicit alternative, predeclare one masonry removal at(-288,38,-38)
and four carried scaffolds. Reach(-288,39,-37) through the upper northern door
at(-289,39,-36), using its two stone buttons and the same two-block timed crossing.
Mine the declared floor block from this adjacent stance, descend four blocks to
feetY35 atX-288,Z-38 and step south toZ-37. Place the scaffold base on the full
floorY34 at(-288,35,-38), then extend it vertically three times using the existing
side-click stacking rule. Climb back toY39 and exit south to the retained ledge.
Validate the whole swept column and placement rays before accepting the link.

This alternative avoids the tripwire'sZ-39 row without disarming it. It requires
one masonry removal, four placements and a four-block initial drop, with one
requested fall-damage point under the previously stated formula before hooks.
Assume no knockback or other entity triggers during this local demonstration;
violations censor the scenario. Do not treat the alternative as free, native
ladder access or observed safe play. Raw blocks remain unchanged.

The declared alternate link passes. The approach from the upper east-chest
station to the southern hatch ledge is five horizontal blocks in each direction.
Entering/leaving the descent column adds two, and stepping to/from the lower
placement stance adds two:14 horizontal blocks and eight blocks of vertical
travel for this local return demonstration. The entire adult swept column is
clear after the single declared floor removal; it stays south of the armed wire.
The base floor is full masonry, and the floor-removal, base-placement and repeated
base-side-click rays pass. Four distance-zero scaffold segments span feet35..39
under the previously verified construction rule. Both northern-door button rays,
the two-block door crossing and its reverse pass under the same one-second
deadline as the earlier stone-button door.

This establishes a conditional connection from the upper room to the middle
floor with an explicit trap bypass. It does not establish the middle-floor chest
approach, deeper rooms or a complete objective budget. The masonry adds six active
diamond-pick ticks (0.3 seconds); four placements, two button presses, tool
selection and fall exposure must remain in the final scenario. The partial route
command, focused Ruff and types pass. No runtime firing, fall, placement or player
movement was observed.

## Middle reward and next floor connection declaration

The middle floor is divided atZ-34 by a three-high, three-wide masonry panel
between extended sticky pistons atX-291 andX-285. Piston heads occupyX-290/-286;
the centerX-288 remains solid atY35..37. Treat this as a native closed barrier,
not an air corridor. Its powered circuit and the hatch tripwire are retained.

Predeclare a controlled breach with unchanged circuit state and no entity
triggering the wire. From the lower scaffold stance(-288,35,-37), advance toZ-35
and remove the center panel cells(-288,35,-34), then(-288,36,-34), using the
diamond pick. Proceed south toZ-30, east toX-287 and south toZ-29. Inspect the
chest at(-286,35,-29) from that station and return by the same path. Check the
ordered mining rays, route sweeps, chest ray and lid. This skips the native
barrier mechanism with two masonry removals; any circuit transition or renewed
obstruction censors this stipulated static scenario. The two removals contribute
twelve active mining ticks (0.6 seconds), not a complete breach time.

For the next floor, use a separate four-scaffold connection atX-287,Z-30.
From the middle chest station, mine the floor(-287,34,-30), descend to feet31,
and step south to(-287,31,-29). Place the scaffold base at(-287,31,-30) on the
fullY30 floor, extend it three times by side clicks, then climb to feet35 and
exit south. This avoids the web-filled original hatch columnX-288,Z-29. Validate
the swept column and placement rays. Retain the four-block drop and one requested
fall-damage point before hooks. No webs are silently removed. This demonstrates
the return connection only; lower-floor room and final descent assessment remain.

Both declared portions pass. The middle reward route is nine horizontal blocks
each way (18 return), with no elevation change. Both ordered panel-removal rays,
the chest ray and clear lid pass. All six boundary piston states are explicitly
checked as extended. This resolves approach to the third saved `quest_tower`
chest assignment, without asserting generated or acquired loot or operation of
the intended piston puzzle. The three tower rewards now all have supported
approaches under the stated native-door and breach conditions.

The next descent has four horizontal blocks and eight vertical blocks for its
local return circuit. The full adult column clears after the one floor removal;
the lower southern stance, full base support and both placement rays pass. Four
more scaffolds and six active mining ticks are required. The original web-filled
hatch is preserved as a separate route, not silently treated as air. The source
fall exposure remains one requested point before hooks. Route execution, focused
Ruff and types pass. These are geometric and modeled results, not gameplay trials.

## Lower tower doors and eastern descending branch declaration

From the lower scaffold landing(-287,31,-29), move north toZ-30 and remove
the web at(-288,31,-30) from that adjacent stance. Move west into the cleared
cell, then north alongX-288 through the two iron doors atZ-32 andZ-36 toZ-38.
Use each door's stone buttons from the adjacent approach cells:Z-31/-33 and
Z-35/-37, all atY33. Each transfer spans two horizontal blocks under the previously
declared one-second deadline; orientation precedes activation. Validate both
directions and the ordered web-removal ray. No additional webs or walls are
implicitly removed. The bottom hatch remains a separate unresolved descent.

From the intervening lower room center(-288,31,-34), inspect the eastern branch
alongZ-34 throughX-261. Feet remain31 throughX-271, then follow the saved bottom
stairs down one block per eastward cell tofeet26 atX-266, andfeet25 fromX-265
throughX-261. Check support, ceiling clearance and reverse ascent with the existing
adult sweep. Stop at the terminal shaft's western ledge; its pit is not automatically
walkable. No mining or placement is permitted in this branch check. Dry sculk veins
reuse their verified collision treatment; natural encounter and sculk activation
are separate conditions, not zero-cost observed outcomes.

Both declarations pass. The lower tower route totals20 horizontal blocks on
return, with one web removal (eight active sword ticks) and four stone-button
presses across two doors. The eastern branch to its terminal ledge totals54
horizontal blocks and12 vertical blocks on return, with no added manipulation.
This is a six-block reachable floor decrease, not a depth inferred from its
component envelope. Source conditions and complete-objective costs remain separate.

The terminal shaft has a masonry rim atfeet25 aroundX-261..-257,Z-36..-32.
Predeclare a rim-only circuit from(-261,25,-34), north toZ-36, east toX-257,
south toZ-32, west toX-261 and north back toZ-34. Do not descend into the pit.
Unlike the earlier blind shaft, its western pit column(-260,Z-34) is air down
through the retained lower boundaryY21, with no floor resolved below that bound.
Other pit cells meet stone/sculk nearY23. Thus neither a uniform one-block pit
nor an external exit can be asserted. Preserve the unresolved continuation below
the extracted range and the surrounding sculk. Child44's bounds contain no block
entities; this does not establish no natural encounter or no environmental hazard.

The rim-only circuit passes in both directions:16 horizontal blocks with no
elevation change or manipulation. The executable check also binds the open pit
column and block-entity absence to the same raw extraction. The lower doors,
descending branch and terminal rim pass the route command, Ruff, formatting and
type checks. No new world extraction or runtime experiment was required. The
whole-assembly graph must retain this optional terminal inspection and its
unresolved below-boundary continuation separately from the supported stair depth.

## Bottom tower connection and lava-channel declaration

Use the already reached lower northern ledge(-288,31,-38). To retain the same
explicit return construction, mine the masonry floor at(-288,30,-38) from the
adjacent stance(-288,31,-37), then descend tofeet27 and step south toZ-37.
Place four scaffolds in the cleared column on the full floorY26, using the
existing base/side-click construction. Validate the entire column and both rays.
This adds one masonry removal, four placements and a four-block initial drop;
retain one requested damage point before hooks. The neighboring original hatch
is preserved. This is an engineered connection, not a native climbable shaft.

The bottom floor contains alternating lava tongues from the west and east.
Predeclare a dry cardinal route from(-288,27,-37): east toX-286, south toZ-34,
west toX-287, south toZ-33, west toX-288, south toZ-32, west toX-289, south toZ-31,
west toX-290, south toZ-29, east toX-289, south toZ-27, east toX-288 and south
toZ-25. Validate actual support, full adult clearance and every swept transition
in both directions; no jumps, fluid displacement or unrecorded lava removal.
Do not treat the source flow levels as air or ignore falling source columns.
The endpoint is the neighboring bedroom threshold, not its completed assessment.

The local scenario assumes the retained fluid state and no displacement into
adjacent lava. Contact, a changed flow, obstruction or forced deviation censors
it. If the declared dry route fails, retain that failure before any alternative.
Any accepted path establishes geometric avoidance, not observed player safety,
combat maneuverability or complete task time.

The first route invocation stopped at(-286,27,-37) because its floor is full
cobblestone, absent from the checker’s conservative support allowlist. This is
a checker coverage limitation, not a lava crossing or unsupported floor. Add
that ordinary full-block support explicitly and rerun the same declared route;
do not change its coordinates or raw evidence to conceal the initial rejection.
The next invocation similarly rejected full calcite at(-286,27,-35). Inspecting
all declared route supports found only ordinary full masonry, cobblestone and
calcite; add the latter explicitly. Both initial support omissions are retained
here as rejected checker runs, not accepted topology measurements.

The unchanged lava-channel route now passes support, adult occupancy and swept
clearance in both directions. It is20 horizontal blocks from the bottom scaffold
stance to the bedroom threshold,40 on return, with no elevation change. The final
scaffold link separately adds four horizontal blocks and eight vertical blocks
for its local return demonstration. Its removal and placement rays pass. No lava
cell, source column, web or waterlogged shape was exempted to obtain this result.

The declared tower route now connects feet elevations39,35,31 and27, a12-block
floor span, and reaches all three saved tower chest assignments. Vertical return
requires twelve scaffolds across three separately supported columns. The tower
route also requires three floor removals, two piston-panel removals and two web
removals, in addition to its button operations. These are coupled conditions of
this inspected route, not a claim that every player must use this solution.
The three four-block initial drops each retain the previously stated fall exposure;
no free healing or actual health delta is inferred. The source trap and closed
panel, lava avoidance and room-to-room return links can now be integrated into
the whole-assembly graph and complete task. Native hatch operation and live
circuit behavior remain unobserved. The bedroom beyond the endpoint still needs
its own activity-space/reward assessment. Route, Ruff, formatting and type checks
pass; no raw extraction or frozen world was changed.

## Bedroom activity space and reward-access declaration

The bedroom has one shared interior activity space east of the wallX-286,
withinX-285..-281,Z-25..-19, with a common aisle atX-284. Two beds do not make
two rooms: their sleeping bays have no separating doorway or full partition.
The western north-south passageX-289..-287 remains a connector, not a second
bedroom. Its west opening atZ-22 and south continuation remain graph links to
validate. The room contains two chest assignments (`bedrooms`), four high barrel
assignments (`barrel`) and an empty blast furnace. Bed halves are two physical
beds, not four facilities. No room spawner is present; natural hostile potential
and the nearby environmental catalyst remain separate from realized encounters.

Predeclare native button-door access from(-288,27,-25) south toZ-22, east to
X-287, then across the east-facing doorX-286 toX-285. The outer oak button is
(-287,28,-21), facing west; the inner button(-285,28,-23) faces east. Use the
same two-block timed transfer, below the1.5-second oak-button deadline, with no
intervening action. This door needs the rotated open collision plates alongZ,
unlike the earlier north/south-facing doors. Resolve that explicit orientation
in the existing checker rather than treating an east-facing open door as air.

Inside, walk toX-284 atZ-22. Inspect the northern pair of barrels and chest from
(-283,27,-24), reached through(-284,27,-24). Return to the aisle and inspect the
southern pair and chest from(-283,27,-20). Visit the furnace from(-284,27,-20).
Use the aisle for both bed interaction stations atZ-23/-21, then return through
the door to the original threshold. Check all six container rays, chest lids,
adult route clearance and facility rays. Do not stand inside beds or use their
fractional top as an assumed floor. High barrels may be used through an exposed
side; their downward facing does not require reaching through the slab beneath.
No mining, placement, smelting, sleep outcome or generated loot is assumed.

The bedroom survey passes all six container rays, both bed rays and the furnace
ray. Both chest lids are clear; barrels are reached through exposed side faces
above their underside slabs. The connected interior circuit is14 horizontal
blocks, plus eight for the approach return and four for the door return:26 total,
zero vertical travel and no removals or placements. Two oak-button presses remain
explicit in the complete task budget. The room is not empty/dead under the
protocol because it has supported rewards and facilities. No authored finale is
established by a bedroom label or chest count. The six unrolled assignments are
reward potential, and the empty furnace establishes no smelted output.

Predeclare continuation of the western passage from(-288,27,-25) south to
(-288,27,-14), and its west branch from(-288,27,-22) to(-295,27,-22). At both
junction centers inspect each cardinal arm for three blocks and return. Use
unchanged adult clearance, no manipulation and the existing dry-plant rule.
These native transitions must pass independently of their serialized four-way
labels before entering the room graph. Further activity rooms beyond the arms
remain separate assessments.

Both passage links and all four three-block arms at each junction pass in both
directions. The south link is11 horizontal blocks one way; the west link is seven.
Both remain atfeet27. These are two validated branching locations, not inferred
branches from template names. Room-graph edge counting must avoid double-counting
the overlapping approach cells. Focused lint initially rejected a redundant
literal-list concatenation; combining that list preserves the measured route.
The final route, Ruff, formatting and type checks pass.

## Dungeon room geometry and buried sources declaration

Child45 is one connected, rounded activity chamber centered near(-288,27,-2).
Four chest assignments sit directly above four spawners atfloorY26: witch north
(-288,-4), spider east(-286,-2), zombie south(-288,0) and skeleton west(-290,-2).
All haveDelay0 and the already recorded source parameters. The four chest/spawner
pairs are not four rooms or four realized enemies. Loot access and source access
must be distinguished: the floor conceals each source's side faces from an actor
standing atfeet27, while its chest covers the top.

Predeclare a native chest survey from(-288,27,-14) south to(-288,27,-5), then
a24-block rectangular circuit aroundX-291..-285,Z-5..1 returning to that point
and the entry. Inspect each chest from its adjacent outward station, respectively
(-288,-5),(-285,-2),(-288,1),(-291,-2), allfeet27. Check chest lids and rays, full
adult clearance and the complete ring before any source-exposure edits. Keep
dry environmental sculk veins distinct from authored chamber content.

For explicit source access after that native survey, predeclare four separate
one-block floor holes at those outward stations. Their retainedY25 supports
are full stone. At the east/west stations first remove the dry sculk vein atY27,
then remove the masonry floorY26, descend tofeet26 and mine the adjacent spawner
through its exposed side. Leave the chest intact. Return to an adjacent unchanged
floor cell with a one-block ascent. Verify each ordered interaction ray and
transition against its own hypothetical edits; no spawner may be treated as
already removed during the native survey. This establishes access and source
removal work, not successful pre-activation suppression or combat. Delay0 means
no positive grace period may be asserted. Encounter conditions and active time
remain required before a complete task total.

The native42-horizontal-block chest survey passes. The first source-exposure
run then stopped on the west station's adjacent dry sculk vein at(-291,27,-3):
the ray checker treated that entire cell as opaque. This was a conservative
outline limitation, not a failed floor or a demonstrated extra removal. Pinned
`SculkVeinBlock` inherits `MultifaceBlock`; its cached outline combines active
directional faces, each one sixteenth of a block thick. The downward face uses
Y0..1/16, so the rejected ray'sY27.999593 point is above that face. Extend the
existing vine-face treatment to dry sculk veins, adding the downward face and
retaining rejection of unsupported/no-face states and waterlogged cells. Do not
generalize other block shapes or relabel outline checks as runtime interactions.

Reproduce with the bound SRG classpath and pinned `javap -c -p` command for
`net.minecraft.world.level.block.MultifaceBlock` and
`net.minecraft.world.level.block.SculkVeinBlock`. Inspect the constructor's shape
cache, `getShape`, `calculateMultifaceShape`, and static face-box initializer.
Keep the original failed invocation here; rerun the same ordered exposure plan.

The unchanged exposure plan passes after resolving that outline. Four floor
holes expose all four spawner side faces, with intact chest blocks and full stone
support below the actor. Each local descent/ascent is one block, with no assumed
fall damage or placement. The east/west target veins are explicitly removed;
the intervening west-side vein stays in place and the accepted ray passes above
its actual plate. No generic non-air exception was introduced.

Active manipulation work is four masonry removals at six ticks each, four
diamond-pick spawner removals at19 ticks each and two hand vein removals at six
ticks each:112 ticks (5.6 seconds). The pinned `Blocks` initializer gives sculk
vein hardness0.2 at offsets36526..36529; the existing mining model supplies the
other values. This excludes selections, aiming, movement between exposure
stations, encounter work and final verification, all still required for the
complete objective budget. It does not imply suppressing any source before its
first attempt. The chamber is nonempty because of its source and reward content;
four distinct explicit source types are supported, realized enemy counts are not.
Route execution, Ruff, formatting and type checks pass. Raw evidence is unchanged.
