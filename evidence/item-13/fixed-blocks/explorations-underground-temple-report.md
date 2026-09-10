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

## Library room and obstructed rewards

Child49 is a library interior withinX-307..-300,Z-32..-21. The middle bookshelf
bank splits two aisles but leaves common front and rear connections; do not count
shelf rows as separate rooms. The front activity area opens east throughZ-22 to
the previously validated junction. No saved library spawner is present. Two
unrolled `library` chest assignments occur at(-307,31,-25) and(-300,31,-25),
above bookshelf stacks. Their lids are capped respectively by full stone bricks
and mossy stone bricks atY32. Under the already verified `ChestBlock` rule these
are blocked openings, not usable loot nodes merely because table assignments exist.

This establishes a concrete reward-access defect. Elevation, adjacent upper
stairs, ceiling clearance and retained webs must be accounted for before any
breaching/retrieval scenario is accepted. Do not silently count inspection of
the chests as acquisition or assign a zero-cost remedy. Existing geometric/source
evidence is sufficient to establish the blocked lids; no server trial is needed
to restate that rule. The raw assignments remain preserved and unrolled.

Predeclare a front-area native inspection from(-295,27,-22) west toX-304,
then north toZ-23, west toX-306, south toZ-21, east toX-300 and north toZ-22,
returning east to the junction. Keep the adult route and dry-plant treatment;
avoid the web at(-305,27,-22) by usingZ-23 on the westward segment. This validates
the entrance/common area only. The deeper bookshelf aisles and an explicit
reward-access solution remain necessary before the library assessment closes.

The declared front circuit passes in both directions:26 horizontal blocks,
zero elevation change and no removals or placements. Both full-block lid caps
are bound explicitly in the same executable check. This resolves the library
entrance and common front area, while preserving the obstructed reward disposition.
Route, Ruff, formatting and type checks pass. No saved world or raw extraction
was modified. The deeper aisle and reward work remains incomplete.

## Library elevated reward remedy declaration

Use two independent three-scaffold columns at(-302,Z-25) and(-305,Z-25),
supported on their fullY26 floors. Reach each base from the common front area
through the adjacent southern stance atZ-24. Clear the eastern base's web atY27
with the iron sword and the western base's east-facing dry sculk vein atY27 by
hand. Place the base and extend twice using the existing side-click rule. Climb
tofeet30; the column has clearance throughY31.8 beneath the retainedY32 ceiling.
Validate the complete climb column, placement rays and return descent.

From each elevated station remove, in order, the adjacent upper stair atY31,
the roof block directly above that stair atY32, and the chest's lid cap atY32.
For the east chest these X coordinates are-301,-301,-300; for the west chest,
-306,-306,-307, allZ-25. Aim at the stair's solid upper half, then the neighboring
roof's underside and finally the exposed side of the lid cap. The intermediate
roof removal is necessary to give a ray above the chest without targeting through
it. Verify each ray before adding that hypothetical removal. Finally inspect the
intact chest from the scaffold top and descend. No bookshelf or chest is destroyed.

This remedy requires six scaffolds, six masonry removals, one web removal and
one vein removal. It is an explicit engineering cost for the observed blocked
state, not a correction to the frozen structure. No raw blocks are changed.
Successful chest interaction and conditional GUI transfer remain distinct from
actually generated or acquired items; complete scenario timing must include
climbs, placements, selections, manipulation, acquisition and verification.

Both remedies pass in their declared order. Each column supplies a three-block
ascent and descent, for12 vertical blocks across the two local returns. Ground
approaches from(-304,27,-22) are four blocks east-side and three west-side each
way, plus two entry/exit blocks per column,18 horizontal blocks total. Active
mining is50 ticks (2.5 seconds): six masonry blocks at six ticks each, one web
at eight and one vein at six. Placement, movement, selection, acquisition and
verification costs remain separate. The original capped state is preserved in
checks preceding the hypothetical removals. The remedy is not a claim that the
frozen layout offers ordinary unmodified chest access.

Predeclare an aisle circuit from(-302,27,-25) north toZ-32, west toX-305, south
toZ-25, south toZ-24, east toX-302 and north to the start. The east base web is
already removed by the declared remedy. Seven additional webs intersect this
route: east aisle(-302,28,-27),(-302,27,-31); rear(-303,27,-32); west aisle
(-305,27,-31),(-305,28,-30),(-305,27,-30),(-305,27,-26). Remove them with the
iron sword from the preceding standing cell before each advance, upper first
where two share a cell. Verify each ray and the entire returned path. No bookshelf
is removed to manufacture a loop. Additional active web work is56 ticks (2.8s).

The first aisle run rejected the front return at(-304,27,-24), where the declared
seven-web set omitted another intersecting web. Preserve that failure. Amend the
same route to remove this eighth web from(-305,27,-24) before crossing east.
The accepted additional web budget becomes64 ticks (3.2s), superseding the
seven-web estimate above; this is an added real obstruction, not a shape exemption.

The amended22-horizontal-block aisle circuit passes all eight ordered web rays
and both traversal directions without removing shelves. The front and rear
connections support one library activity room with an internal aisle loop; that
loop is not automatically a separate cycle in the inter-room graph. Combined
library manipulation is six masonry blocks, nine webs (including the eastern
scaffold base) and one vein, plus six scaffold placements. Active mining totals
114 ticks (5.7s); full task phases remain to be integrated without double-counting
overlapping front/aisle approaches. The room is not empty/dead: shelves provide
salvage and the two assigned rewards have explicit, costly access. No final-room
role or observed replay enjoyment follows from those facts. Both original blocked
lids and the rejected seven-web plan remain recorded. The route, Ruff, formatting
and type checks pass; all raw evidence remains unchanged.

## Lower terminal rewards and barred cells declaration

From the lower junction(-288,27,-14), inspect the west terminal chest
(-295,27,-16) from(-295,27,-14), then the east chest(-281,27,-12) from
(-281,27,-14), returning to the junction after each. Both assigned `dead_end`
tables remain unrolled. Both lids have straight top stairs above, not full
collision cubes; apply the previously verified chest-lid rule and check the
actual rays. These functional reward alcoves are not empty/dead merely because
their templates use that name. Do not infer a sealed exterior from their labels.

The southern hall's cell component has two separately bounded activity spaces
behind iron bars atZ26, separated by the wallX-273. The west interior contains
a bed and barrel; the east interior contains a bed, barrel and empty cauldron.
The shared passageZ27..29 is a connector. The two-block-high barred openings are
closed native boundaries, not doors that can be assumed open.

Predeclare entry from the southern hall threshold(-280,39,28) along the passage.
For the west cell remove bars at(-275,40,26), then(-275,39,26) from(-275,39,27).
Enter at(-275,39,25), inspect the barrel(-274,39,25), then the bed from
(-276,39,23), usingX-276 betweenZ25 and23. Return to the passage. For the east
cell remove bars at(-270,40,26), then(-270,39,26) from(-270,39,27). Enter at
(-270,39,25), inspect the bed from(-270,39,23), then cross throughZ24 toX-272
and inspect its barrel at(-272,39,22) fromZ23, and cauldron atZ25 fromZ24.
Return through the breach and to the hall threshold. Validate ordered mining
rays, adult sweeps, all reward/facility rays and floor support. No other bars,
beds or furnishings are removed. Integration with the main hall route remains
conditional on resolving the intervening whole-assembly links.

Both lower terminal approaches pass:14 horizontal return blocks each,28 total,
with no manipulation. Their straight stair caps are not blocked full-cube lids.
Both cells also pass all ordered bar-removal, barrel, bed and cauldron rays and
bidirectional adult transitions. The west return is22 horizontal blocks and the
east return38, both atfeet39. These separately returned local circuits total60;
the whole task may share the passage but must declare its actual ordering before
using a different total. Neither room is empty/dead under the stated access model.

Pinned `Blocks` offsets12944..12950 give iron bars hardness5. With the declared
diamond pick, each removal uses19 active ticks, four totaling76 ticks (3.8s).
Selection, aiming, movement and acquisition remain additional task phases. Native
cell entry stays blocked; the inspected model earns access through mining.
No water, cauldron output, slept night or realized enemy population is inferred.

Current reward-access accounting:29 of31 chest/barrel nodes now have local
validated approaches or explicit remedies. The two remaining nodes are the
southern upper terminal chest(-290,39,47) and western terminal chest(-324,33,5).
The two dispenser table assignments are separately retained trap ammunition
potential, not ordinary chest acquisitions. Thus all33 table assignments remain
accounted for without calling the partial whole-assembly route complete. Route,
Ruff, formatting and types pass. No accepted world or raw extraction was changed.

## Final terminal rewards and western source branch declaration

Inspect the southern terminal from the second hall's south threshold(-288,39,36)
alongX-288 toZ47, then inspect chest(-290,39,47) and return. Its top straight
stair cap follows the established non-full lid rule. Validate the intervening
three-way center(-288,39,40), with north, east and south arms of three blocks.
The eastern lava branch remains distinct from this dry terminal route.

For the western terminal, first connect the western upper junction(-300,39,0)
south toZ5, then use a six-scaffold column at(-300,Z6), baseY33 on the retained
fullY32 floor. Descend six blocks, step north to(-300,33,5), place and extend the
base five times, and validate the column and upper ledge return. Retain the
initial six-block fall and three requested damage points before hooks. From the
base, reach the lower junction(-300,33,7) and follow its west corridor toX-317.

Remove, in order, webs(-305,34,7),(-307,34,7),(-308,34,7), then the spawner
(-308,33,7), then webs(-309,33,7),(-311,34,7),(-311,33,7). Work from the adjacent
east standing cell before each advance. This is the same six-web/one-source
mechanism as the earlier east corridor, but its actual saved positions and rays
must pass independently. The saved cave-spider source hasDelay0; this plan does
not promise disabling it before activation. Continue to(-324,33,7), inspect the
terminal chest(-324,33,5) under its top straight stair, and return.

No additional blocks are removed, no water or lava is crossed, and no realized
enemy is assumed absent. The shaft, source-work and terminal pieces must compose
under their declared geometry; complete encounter and task timing remain separate.

Both terminal approaches and chest rays pass. The southern return is22 horizontal
blocks, with the three native junction arms verified. The western corridor and
terminal return is48 horizontal blocks from its lower junction. Its six ordered
web removals and one cave-spider source removal all have verified rays; active
mining is67 ticks (3.35s), excluding selections, movement and encounter work.
The western shaft construction and return pass with six scaffold placements,
16 horizontal blocks including its upper approach, setup stance and lower-junction
connection, and12 vertical blocks. Its initial fall exposure remains explicit.

All31 chest/barrel assignments now have local access proofs or declared remedies
in this first assembly. The two dispenser assignments remain separate trap
ammunition potential. This closes local reward-node access coverage only: it does
not yet prove one complete route, all connector alternatives, source suppression,
combat workload or task duration. Both terminal reward alcoves are functional
under the model, not empty rooms inferred from `dead_end` names. The first lint
run requested splitting a compound lid assertion; that narrow presentation fix
preserves the same checks. Final route, Ruff, formatting and type checks pass.

## Main-hall overhead bypass declaration

The original native lava centerline remains rejected. Side-tunnel candidates
outside the corridor are not accepted alternatives: X-291 atfeet39 meets water
atZ11..16 and lacks solid support atZ11..14; X-285 meets water throughout much
ofZ9..19. These are retained inspection rejections, not dry passages or permission
to ignore fluid updates. A dry overhead route is available for explicit testing.

Predeclare a tunnel atX-288,feet43,Z8..20. The corridor's retained center roofY42
provides full support forZ9..19. At the first hall thresholdZ8, remove the three
vertical cellsY42,43,44 fromfeet39, bottom first. Place four scaffoldsY39..42
from the adjacent hall stanceZ7, then climb tofeet43. From each preceding cleared
cell mine the next cell'sY44 andY43 blocks, in that order, continuing throughZ20.
Validate each ray and adult step before advancing. The remainingY42 roof must
stay intact throughoutZ9..19, separating the tunnel from the lava below.

AtZ19 mine the second hall threshold's floor cell(-288,42,20), descend four
blocks tofeet39 atZ20, and step south toZ21. Build a second four-scaffold column
atZ20 from that stance. Validate its placement rays, whole shaft and reverse
climb. The first shaft is built before ascent; the second initial descent retains
one requested fall-damage point before hooks. No flight, remote placement or
free recovery is assumed. Returning uses both built columns.

This plan uses eight scaffolds and28 removals: three cells in the first shaft,
24 tunnel cells atY43/44,Z9..20, and the second shaft'sY42 floor. Check all six
neighbors of the removed cells for water/lava before accepting a static dry
model; retain unsupported fluid or falling-material behavior as a failure.
No lava source is plugged, no frozen configuration is changed, and no live
fluid behavior is claimed. The bypass must be costed as engineering work, not
as the original twelve-block native hall connection.

The declared overhead link passes all28 ordered removal rays, both scaffold
placement rays per shaft, adult swept columns and bidirectional supported tunnel
traversal. The immediate neighbor-state set is exactly air, stone, stone bricks,
cracked/mossy stone bricks and deepslate brick wall, with no waterlogged states.
The tunnel retains its masonry floor above the lava. This supports the declared
dry construction model without claiming a runtime fluid experiment.

The local build-and-return demonstration is28 horizontal blocks:24 for the
out-and-back tunnel and four for the two adjacent placement stances. It has16
vertical blocks across the two shaft ascents/descents and eight placements.
The28 stone/masonry removals contribute168 active ticks (8.4s) with the diamond
pick. Tool selection, aiming, placement, movement, encounter work and verification
remain additional phases. The second shaft's initial four-block drop retains
its stated exposure. This now connects the two halls under an explicit earned
breach route; the native lava centerline and rejected wet side routes remain
separate evidence. Route, Ruff, formatting and type checks pass. Raw blocks and
the frozen configuration remain unchanged.

## Remaining three source branches declaration

Resolve the cave-spider corridors north from(-317,33,7) toZ-7, west from
(-300,33,28) toX-317, and south from(-300,33,28) toZ45. Each contains six webs
and one source, but the two southern corridors reverse the first/last web-pair
arrangement relative to the northern one. Use the exact saved coordinates in
the checker. Before advancing each step remove the declared intersecting upper
web, then lower web/source, from the preceding standing cell. PreserveDelay0
and natural encounters as unresolved timing inputs; no positive grace period.

Connect the southern lower junction with a six-scaffold shaft atX-299,Z28,
baseY33, from the southern hall's western threshold(-296,39,28). Walk west to
the ledgeX-298, descend atX-299, and step east to(-298,33,28). Remove the downward
dry vein at(-299,33,28), place the base on its fullY32 floor and extend five times.
Validate the full column, both placement rays, the return climb and the one-block
west connection to(-300,33,28). Retain the six-block initial fall and three
requested damage points before hooks. No nearby sculk block or water is removed.

At the western endpoint(-317,33,28), inspect all four cardinal arms for three
blocks and return. The north branch's endpoint at(-317,33,-7) meets calcite at
(-317,34,-8), so a further upright centerline step is blocked; do not assert a
fully sealed exterior. The southern endpointZ45 is a local terminal inspection,
not proof that every adjacent cave approach is closed. Validate each declared
path independently and confirm that the completed local source-access set covers
all nine saved spawners, without claiming realized enemy removal.

All three declared branches pass in both directions after their exact ordered
removals. Return distances are28,34 and34 horizontal blocks respectively, with
no elevation changes inside those corridors. Their18 webs and three sources
contribute201 active mining ticks (10.05s). The southern shaft also passes,
including its base-vein removal, placement rays and return: six scaffolds,
ten horizontal blocks including approach/setup/junction steps, and12 vertical
blocks. Its one hand vein adds six active ticks (0.3s), separate from all placement
and movement phases. The six-block initial fall remains exposed.

The western lower junction's four arms pass. The northern endpoint's calcite
head obstruction is confirmed, preserving that local boundary. The executable
coverage check compares source positions directly with all nine saved spawner
block entities; each has a validated local removal route. This closes source
access coverage for the first assembly, not observed spawning, encounter duration
or one complete suppression schedule. The whole task must combine these routes,
account for all existing source activation and natural-spawn conditions, and
retain environmental and below-boundary uncertainty. Route, Ruff, formatting and
types pass. No raw evidence or runtime was changed.

## First assembly construction union

The executable now derives the union of all locally validated hypothetical
removals from their saved block coordinates. This avoids adding the same work
again when a later route reuses a previously cleared cell. Reproduce with
`uv run python -m evidence.item-13.underground_temple_route`. It reports 112 unique
cells, grouped below using the source-supported tool assumptions already declared
above. This is construction work for the selected remedies, not a minimal-edit
solution or a complete dungeon time.

| Removed material | Unique cells | Tool | Active ticks per cell | Subtotal ticks |
| --- | ---: | --- | ---: | ---: |
| Stone, stone bricks and their declared masonry/stair variants | 49 | Diamond pick | 6 | 294 |
| Cobweb | 43 | Iron sword | 8 | 344 |
| Gravel | 2 | Hand | 18 | 36 |
| Iron bars | 4 | Diamond pick | 19 | 76 |
| Dry sculk vein | 4 | Hand | 6 | 24 |
| Spawner | 9 | Diamond pick | 19 | 171 |
| Vine | 1 | Hand | 6 | 6 |
| Total | 112 | As above | Variable | 951 |

The masonry group contains 22 stone, 16 stone bricks, five cracked stone bricks,
three mossy stone bricks, one chiseled stone brick, one stone-brick stair and one
mossy stone-brick stair. The union contributes 47.55 conditional seconds of active
mining at 20 TPS. Profile-dependent aiming, selection, placement, navigation,
acquisition, encounter work and verification remain additional phases. This
subtotal must not be reported as traversal time or as observed block breaking.

The declared local remedies require 44 scaffold placements before any reuse:
18 across the three six-block entrance shafts, 12 across the three four-block
tower shafts, six for the two library columns, and eight for the overhead hall
link. These counts are direct sums of disjoint declared columns. Their routes
remain conditional on sufficient carried scaffolds and the stated placement
rules. Do not assume recovery or deduct materials merely because a column might
later be dismantled.

The three initial six-block drops each request three damage points, and the
three initial tower drops plus the southern overhead drop each request one,
under the previously cited fall formula. Their nominal sum is 13 requested
points before hooks and other damage. This is neither an observed health loss
nor a survival guarantee. A complete objective must account for survival through
encounters and environmental hazards without silently adding healing.

This consolidation resolves construction quantity and active-mining overlap.
It does not resolve overlapping local movement, final tool-switch order, source
suppression timing, natural-spawn exposure or the environmental sculk response.
All nine sources have Delay0, so the short single-batch grace assumption used in
some earlier family tasks cannot be transferred to this assembly. No complete
traversal/combat duration is accepted until those dependent conditions and one
joined objective are explicit.

## Remaining native connector inspection declaration

Use the retained first-assembly blocks and the existing adult clearance check.
No new removal is proposed. Validate the upper western corridor from
(-300,39,0) to Z-16 and retain the next centerline lava at Z-17 as a rejected
dry continuation. Validate the northern junction's western terminal from
(-288,39,-23) to X-296, retaining the calcite head obstruction at X-297.
Validate the southern hall junction's eastern approach from(-288,39,40) to
X-283, retaining the next centerline lava at X-282. From the western lower
junction(-300,33,7), inspect south to Z11 before lava at Z12, and north down
the saved staircase to(-300,27,-8) before lava at Z-9.

From the cells passage(-280,39,28), follow the eastern stairs to
(-252,33,28): feet stay39 through X-264, descend one per cell to feet34 at
X-259, then reach feet33 at X-258. Validate both directions, including ascent
clearance beneath the hanging bars. Inspect the eastern lower junction and its
actual terminal arms separately before counting their graph links. Finally,
inspect the library passage's northern connector from(-295,27,-22) to Z-32
and its east/west stubs. Saved piece labels do not establish onward connections.

These local dry routes stop at the first declared obstruction. A lava rejection
does not establish that engineering, swimming or adjacent terrain access is
impossible. Such alternatives are outside these native-route measurements.

All seven declared connectors pass in both directions without additional edits.
The eastern lower junction and library connector also have the following local
inspection routes. Distances are independently returned excursions; their sum
is not a deduplicated complete task.

| Local excursion | Horizontal return blocks | Vertical return blocks |
| --- | ---: | ---: |
| Upper western junction to lava approach Z-16 | 32 | 0 |
| Northern junction west to X-296 | 16 | 0 |
| Southern hall junction east to lava approach X-283 | 10 | 0 |
| Western lower junction south to lava approach Z11 | 8 | 0 |
| Western lower junction north down stairs to Z-8 | 30 | 12 |
| Cells passage east to lower junction X-252 | 56 | 12 |
| Library passage north to Z-32 | 20 | 0 |
| Eastern lower junction north to Z14 ledge | 28 | 0 |
| Eastern lower junction east to X-245 | 14 | 0 |
| Eastern lower junction south to Z38 | 20 | 0 |
| Southeastern connector east to X-249 | 6 | 0 |
| Southeastern connector west to X-254 | 4 | 0 |
| Library northern connector east to X-292 | 6 | 0 |
| Library northern connector west to X-297 | 4 | 0 |

The four stated lava cells and northern calcite head obstruction are confirmed.
The library northern connector is bounded locally by stone at(-295,27,-33),
masonry at(-298,27,-29) and masonry at(-291,27,-29). Its east/west stubs do not
reach the adjacent library or tower through a native centerline. The southeastern
connector is locally capped by calcite at(-252,33,39) and(-248,33,35), with
masonry at(-255,33,35). These are quiet terminal connective spaces under the
reward/source objective, not additional demonstrated reward rooms. Natural
encounters remain unknown; absence of saved block entities cannot establish
that they were empty during play.

The eastern lower junction's northern corridor has a supported ledge at
(-252,33,14), followed by dry side-facing vein at(-252,32,13) over air atY31.
That vein is not a supporting floor. The route therefore stops at the ledge,
retaining an opening toward surrounding terrain instead of inventing a capped
dead end or a proven exterior escape. The nearby enchanting-room direction
does not by itself establish a traversable connection.

The eastern terminal inspection stops at(-245,33,28). The next cell has nickel
ore support atY32, outside this checker's verified support set, followed by a
stone head obstruction at(-243,34,28). This is an explicit final-step geometry
limitation, not evidence that nickel ore cannot support a player. A lit dry
campfire at(-245,33,29) also rules out treating the southern neighboring cell
as an automatically safe detour. Neither a breach nor another support-block
implementation was needed to establish the route's local terminal approach.

These results add two native six-block stair progressions and distinguish
actual supported branches from lava continuations, capped stubs and an exposed
ledge. No removal subtotal changes. Room-graph integration must retain the
stated endpoints and must not connect across any of these unvalidated boundaries.

## First assembly activity partition and reward/source allocation

Apply the protocol's activity-space definition to the locally validated routes.
The primary partition has 25 activity spaces listed below. Each is a delimited
reward, furnishing, source or hazard area reached by a documented local route.
This is an explicit interpretation of playable space, not a count of the 61
serialized pieces. The `room_bounds` coordinates in the existing route executable
bound each activity/fixture footprint, including its associated elevated or
buried fixtures. They are not assertions that every voxel in a rectangular box
is playable. Actual standing cells, obstacles and transitions remain defined by
the route proofs above.

| Room | Activity space | Main feet Y | Chest/barrel assignments | Saved sources | Other distinguishing content |
| --- | --- | ---: | ---: | ---: | --- |
| R01 | Northern main hall | 37..39 | 4 | 0 | Central gold block, four connected spokes |
| R02 | Southern main hall | 37..39 | 4 | 0 | Central gold block, four connected spokes |
| R03 | Tower upper reward floor | 39 | 2 | 0 | Button-controlled approach and northern exit |
| R04 | Tower middle activity floor | 35 | 1 | 0 | Tripwire/dispenser zone and piston panel |
| R05 | Tower bottom hazard floor | 27 | 0 | 0 | Lava channels with validated dry zigzag |
| R06 | Bedroom | 27 | 6 | 0 | Two beds and furnace |
| R07 | Library | 27, temporary columns to 30 | 2 | 0 | Shared front/rear aisles; blocked native lids |
| R08 | Rounded dungeon chamber | 27, source holes 26 | 4 | 4 | Four different saved source types |
| R09 | Western barred cell | 39 | 1 | 0 | Bed; explicit bar breach |
| R10 | Eastern barred cell | 39 | 1 | 0 | Bed and empty cauldron; explicit bar breach |
| R11 | Enchanting room | 33 | 1 | 0 | Enchanting and brewing fixtures |
| R12 | Eastern source corridor | 33 | 0 | 1 | Delimited web/source obstacle zone |
| R13 | Western source corridor | 33 | 0 | 1 | Delimited web/source obstacle zone |
| R14 | Northwestern source corridor | 33 | 0 | 1 | Delimited web/source obstacle zone |
| R15 | Southwestern west source corridor | 33 | 0 | 1 | Delimited web/source obstacle zone |
| R16 | Southwestern south source corridor | 33 | 0 | 1 | Delimited web/source obstacle zone |
| R17 | Northern upper terminal alcove | 39 | 0 | 0 | Lit campfire |
| R18 | Eastern lower north terminal alcove | 33 | 0 | 0 | Lit campfire; rubble access remedy |
| R19 | Far eastern lower terminal alcove | 33 | 0 | 0 | Lit campfire; final ore-supported step unvalidated |
| R20 | Southwestern south terminal alcove | 33 | 0 | 0 | Lit campfire |
| R21 | Eastern lower south reward alcove | 33 | 1 | 0 | Lit campfire; rubble access remedy |
| R22 | Southern upper reward alcove | 39 | 1 | 0 | Lit campfire |
| R23 | Western lower reward alcove | 33 | 1 | 0 | Lit campfire |
| R24 | Lower western reward alcove | 27 | 1 | 0 | Lit campfire |
| R25 | Lower eastern reward alcove | 27 | 1 | 0 | Lit campfire |

The executable allocates each of the 31 saved chest/barrel assignments, nine
spawners and nine campfires to exactly one declared footprint. Allocation passes;
no fixture is omitted or counted twice. R08 contains the witch, spider, zombie
and skeleton sources. Each of R12..R16 contains one cave-spider source. Thus six
activity spaces contain saved spawners, with five source entity types across the
assembly. This says nothing about realized enemy numbers or diversity. The two
dispenser table assignments are trap inputs and stay outside the 31 ordinary
reward-node denominator. All 33 table assignments remain unrolled.

Partition sensitivity is explicit. Five source zones R12..R16 are corridor-shaped
but host bounded web/source obstacles, so the primary definition counts them as
activity spaces. Treating them only as connections gives 20 rooms. The nine small
terminal alcoves R17..R25 are delimited end activities rather than through
corridors; treating all nine as connection endpoints instead gives 16 rooms, or 11
when both alternative conventions are applied. These are definitional alternatives,
not statistical uncertainty or evidence that any content disappears. The library
aisles, each bed, each chest and each spawner are not separate rooms. The tower's
Y31 two-door transit floor is retained as a connector between floors and the
eastern stair branch; counting that floor as another room would add one to any
of these conventions. No single-room count should be compared with another
family without preserving the same partition rules.

Under the primary partition, no room meets the protocol's empty/dead definition
on supported potential content: R01..R04, R06..R11, R21..R25 have reward assignments
with local access; R05 has a required lava-avoidance route; R12..R16 have explicit
sources/web obstacles; R17..R20 have reachable terminal campfire areas. This is
0/25 empty and 0/25 dead under this content definition, not an assertion that
every visit produces encounters, useful loot or meaningful player engagement.
Quiet capped connectors are recorded separately and have not been hidden by
calling every serialized intersection a room. The complete graph must still
include their terminal routes and access purpose.

For the campfire classification, the same pinned server SRG artifact used above
contains `CampfireBlock.entityInside(BlockState,Level,BlockPos,Entity)`. Its
bytecode checks `LIT`, requires a `LivingEntity`, then calls `Entity.hurt` using
`DamageSources.campfire()` and the block's `fireDamage`. Reproduce inspection:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap \
  -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar \
  -c -p net.minecraft.world.level.block.CampfireBlock
```

The executable confirms all nine saved campfires are lit and not waterlogged.
This establishes an avoidable contact-hazard mechanism at the listed alcoves;
it does not establish actual damage, cooking output or combat displacement.
The declared paths avoid contact. The zero empty/dead count must be read with
that modest content threshold and the retained natural-encounter uncertainty.

This partition and allocation are ready for graph integration. Whole-assembly
reachability, graph depth, complete route length and timing still depend on the
joined objective and its source/environment conditions; the table does not
substitute for that required complete-route validation.

## Contracted first-assembly graph

Contract the inspected paths between activity spaces, genuine decision openings
and terminal inspection boundaries. R01 is the graph entry reference, not a
verified surface entrance. This graph includes the declared mining/scaffold
remedies and timed-door assumptions. It is not the untouched native graph.
The explicit adjacency list is `graph_children` in the existing executable;
edges are undirected for geometry and retain their construction prerequisites.
This derivation uses the room partition above and actual local routes, not
template connectivity. It does not yet prove one complete coordinate/phase route.

Junction reference points and their incident branches are:

| Node | Reference feet coordinate | Incident nodes |
| --- | --- | --- |
| J01 | (-288,39,-23) | R01, R03, R17 |
| J02 | (-300,39,0) | R01, J04, T01 |
| J03 | (-276,33,0) | R01, R12, R18, R21 |
| J04 | (-300,33,7) | J02, R13, T02, T03 |
| J05 | (-317,33,7) | R13, R14, R23 |
| J06 | (-248,33,0) | R12, R11, T04, J19 |
| J07 | (-288,31,-34) | R04, R05, T07 |
| J08 | (-288,27,-22) | R05, R06, J09, J10 |
| J09 | (-295,27,-22) | J08, R07, J11, T08 |
| J10 | (-288,27,-14) | J08, R08, R24, R25 |
| J11 | (-295,27,-29) | J09, T09, T10 |
| J12 | (-275,39,28) | R02, R09, J13 |
| J13 | (-270,39,28) | J12, R10, J14 |
| J14 | (-252,33,28) | J13, R19, T11, J15 |
| J15 | (-252,33,35) | J14, T12, T13 |
| J16 | (-288,39,40) | R02, R22, T14 |
| J17 | (-300,33,28) | R02, R15, R16 |
| J18 | (-317,33,28) | R15, T15, T16, T17 |
| J19 | (-241,33,0) | J06, T05, T06 |

Other room-to-room links are R01/R02 through the overhead remedy, R03/R04
through the first tower shaft, and R16/R20 through the southern source corridor
exit. A small pocket inside a junction is not an additional graph arm: the west
sides of J11/J15 and south side of J19 stop within the junction interior instead
of passing through an opening. J17's north side is locally blocked by sculk at
(-300,33,25), with stone at Z24; no extra onward link is assigned.

| Endpoint | Inspected reference feet coordinate | Boundary disposition |
| --- | --- | --- |
| T01 | (-300,39,-16) | Upper western lava begins at Z-17 |
| T02 | (-300,33,11) | Western lower southern lava begins at Z12 |
| T03 | (-300,27,-8) | Western lower northern lava begins at Z-9 |
| T04 | (-248,33,-5) | Previously inspected blind shaft and rim |
| T05 | (-241,33,-3) | Stone cap at Z-4 |
| T06 | (-238,33,0) | Stone cap at X-237 |
| T07 | (-261,25,-34) | Inspected shaft rim; continuation below Y21 unresolved |
| T08 | (-295,27,-19) | Stone at Z-18 |
| T09 | (-295,27,-32) | Stone at Z-33 |
| T10 | (-292,27,-29) | Masonry at X-291 |
| T11 | (-252,33,14) | Exposed ledge; next vein is not a supporting floor |
| T12 | (-252,33,38) | Calcite at Z39 |
| T13 | (-249,33,35) | Calcite at X-248 |
| T14 | (-283,39,40) | Southern upper lava begins at X-282 |
| T15 | (-317,33,25) | Stone at Z24 |
| T16 | (-317,33,31) | Stone at Z32 |
| T17 | (-320,33,28) | Stone at X-321 |

The executable derives61 nodes (25 rooms,19 junctions,17 boundary endpoints),
60 edges and one connected component. Its cycle rank is0. There are21 decision
nodes of degree at least three: all19 listed junctions plus the two main halls.
There are33 graph leaves:16 terminal activity rooms and17 boundary endpoints.
Those33 leaves are not33 empty rooms or33 proven sealed dead ends. In particular,
lava approaches and exposed/below-boundary endpoints remain censored graph
boundaries. Internal hall rings and library aisle loops remain internal geometry
and do not add an inter-room cycle under this contraction.

Shortest graph distances from R01 reach the deepest activity spaces R07,R08,R24
and R25 at eight edges. The deepest nodes are T09/T10 at nine edges. These values
depend on the declared contraction and engineering remedies; they are not
Minecraft generation depth, room count traversed, route-block distance or terrain
cover. No authored finale has been inferred from the deepest node.

| Shortest contracted edge depth from R01 | Chest/barrel assignments | Saved spawners |
| --- | ---: | ---: |
| 0 | 4 | 0 |
| 1 | 4 | 0 |
| 2 | 3 | 1 |
| 3 | 3 | 3 |
| 4 | 2 | 0 |
| 5 | 1 | 1 |
| 6 | 0 | 0 |
| 7 | 6 | 0 |
| 8 | 8 | 4 |
| Total | 31 | 9 |

The fixture allocation and breadth-first graph distances produce this table
directly. It locates potential rewards and source workload; neither distribution
is generated loot or realized combat. It also shows that assigning every reward
to one supposed final room would contradict the saved layout.

During integration, strengthen the existing support check to reject a declared
standing cell when its supporting cell is in the hypothetical removal set.
Reading only the original block at that location would incorrectly permit a
later route to stand over a mined floor. All existing local route checks pass
with this stricter phase boundary. The raw blocks remain unchanged. The full
coordinate/phase route must still account for supported transitions, temporary
columns, door deadlines and task order before these contracted results become
an accepted complete traversal measurement.

The direct support regression first accepts(-288,37,-3), temporarily marks its
Y36 support removed, requires the precise removed-support rejection, and restores
the hypothetical set. It passes along with all local routes, fixture allocation,
graph derivations, Ruff formatting/lint and type checks. No server experiment,
actual removal or runtime timing is implied.

## Joined eastern excursion and post-mining dungeon route declaration

Begin the eastern excursion at J03(-276,33,0), after its entrance-shaft phase.
Visit the northern rubble alcove and return, then the southern reward alcove
and return. Follow the eastern source corridor to J06. Visit the enchanting
room and its reward station and return to J06, retaining two separate timed
button presses and the vine-limited transfer. Next traverse the blind-shaft
approach, one full rim circuit, the one-block pit out and back, and return to
J06. Finally inspect the eastern connector and each of its three local arms
out and back, then return along the source corridor to J03. The short southern
pocket remains an inspection detour, not a new graph link.

Concatenate the existing coordinate lists with exact shared endpoints, dropping
only the duplicate endpoint at each seam. Validate the entire resulting route
against the final hypothetical removals and door state. This is a closed
movement excursion whose construction/interaction phases remain additional;
it does not assume that the remedies were free or present in the saved world.
No selected local segment may begin by teleporting from another segment's end.

For the dungeon chamber, first retain the original pre-mining flat survey.
After all four source holes have been excavated, that same flat route is invalid
because its supporting cells at(-288,26,-5),(-285,26,-2),(-288,26,1) and
(-291,26,-2) have been removed. Predeclare the post-mining alternative: at exactly
those four plan coordinates use feet26 on the already verified full Y25 stone,
with feet27 elsewhere. Recheck both directions of the entry and closed ring,
including every one-block descent and ascent. No hole is invisibly refilled and
no additional block is removed. Preserve any failed clearance before alternatives.

Also join the two western lower excursions using existing paths. From J04,
follow the western source corridor to J05, inspect the northern source branch
and return to J05, visit the western reward alcove, and return to J04. Inspect
the southern lava approach and the northern descending stair/lava approach,
returning to J04 after each. From J17, follow the western source corridor to
J18, inspect its north/south/west capped arms and return along the corridor to
J17. Then inspect the southern source corridor and terminal alcove and return.
The J18 eastern arm is already traversed on arrival/departure; do not add it
again as a separate excursion. Neither circuit crosses its rejected lava bounds.

The joined routes pass with exact seam equality and identical start/end points:

| Closed excursion | Horizontal blocks | Vertical blocks | Start/end |
| --- | ---: | ---: | --- |
| Eastern rooms, source, blind shaft and terminal inspections | 212 | 2 | J03(-276,33,0) |
| Western lower source branches, reward and lava approaches | 114 | 12 | J04(-300,33,7) |
| Southwestern source branches, terminal and capped arms | 86 | 0 | J17(-300,33,28) |
| Dungeon survey after four source holes | 42 | 10 | J10(-288,27,-14) |

Horizontal distance counts each cardinal step once; a stair step also contributes
its vertical displacement. Repeated returns are intentional movements in the
declared excursion. Only duplicated seam coordinates are removed. The eastern
excursion includes six horizontal blocks of vine-limited door transfer in total;
the previously fixed three-block/s transfer and two oak-button deadlines remain
part of that phase. This route does not assert a blind operator or human time.

The dungeon's post-mining horizontal length remains42, but its vertical movement
is ten blocks rather than the original flat survey's zero. Every passage through
an excavated station descends to full stone and climbs out; the northern station
is also crossed by the entry/return path. This demonstrates why source-access
construction cannot be treated as leaving the original movement geometry intact.
No extra mining or filling was used to make the post-mining route pass.

These are integrated subcircuits of the complete objective. Their common-hall
approaches, shaft construction and travel, tower/lower-room circuit, acquisition,
source suppression, combat and verification are still required. Do not sum these
four rows and label the result a complete dungeon task. The post-mining dungeon
survey also must not automatically be charged in addition to a pre-mining survey;
the final declared task order determines which survey and source-access movements
are actually performed.

## Lower activity circuit and explicit scaffold transitions

For continuous post-construction geometry only, enable the ten already declared
scaffold columns. Their(X,Z,base feet,top feet) values are(-277,0,33,39),
(-300,6,33,39),(-299,28,33,39),(-288,-38,35,39),(-287,-30,31,35),
(-288,-38,27,31),(-302,-25,27,30),(-305,-25,27,30),(-288,8,39,43)
and(-288,20,39,43). They still require44 placements. The two separated columns
at X-288,Z-38 do not authorize climbing through the unbuilt Y32..34 interval.
Validate each base against retained support and each full adult column sweep
before adding its exact feet positions to the modeled movement set. Preserve
the previously checked placement rules and rays. No other unsupported position
is authorized by this change; original local construction checks run first with
the modeled set empty.

Begin the lower activity circuit at J08(-288,27,-22). Visit the bedroom and
return, then follow the western passage to J09. Traverse the library front
circuit, inserting the two column ascents/descents and chest-access stops at
their previously verified approach junction. Include one library aisle circuit
at the eastern column base. Return to J09, inspect its northern connector with
east/west stubs and its southern capped stub, then return to J08. Visit J10's
two terminal reward alcoves and post-mining dungeon circuit, and return to J08.
Use exact joined coordinates and retain two bedroom door operations. This is
the post-construction movement circuit; construction and encounter state remain
separate prerequisites, not free starting resources.

Join the tower from J01(-288,39,-23): upper reward path, northern door approach,
first shaft, middle reward path, second shaft, lower two-door path, third shaft,
bottom dry zigzag and the three-block link to J08. On the outbound lower path,
insert the eastern descending branch and one terminal-rim circuit, returning
to J07 before continuing downward. Perform the lower activity circuit once.
Return by the reverse tower transit without repeating the already completed
eastern branch inspection. Keep every shaft entry/exit step in the coordinates;
retain all eight tower stone-button operations and both bedroom oak-button
operations. Initial construction falls and placement effort remain outside this
post-construction circuit and cannot be silently absorbed into climb time.

The lower activity circuit passes as one closed route:222 horizontal blocks
and22 vertical blocks from J08 back to J08. Its vertical work is12 blocks on
the two library columns and ten through the dungeon source holes. All four
dungeon chest rays also pass from the lower, post-excavation stations at feet26;
reward access does not require pretending those floors were restored.

The tower circuit, including that lower activity circuit exactly once and the
eastern branch/rim inspection exactly once, passes at430 horizontal blocks and
58 vertical blocks from J01 back to J01. The tower transit contributes24 vertical
blocks on return, the eastern staircase12 and the lower activity circuit22.
The joins preserve exact shared coordinates and include column entry/exit steps.
These results supersede any attempt to obtain this circuit by indiscriminately
adding every earlier local return demonstration.

The column movement model reuses the pinned scaffold support/collision rules
already recorded in the [Large House assessment](mns-large_house_1-report.md):
vertical distance-zero columns inherit sturdy floor support; the stable top
supports a non-descending actor above it, while internal distance-zero collision
is empty and scaffolding is climbable. Direct inspection of the same pinned
`ScaffoldingBlock.getCollisionShape` confirms the `isAbove`/`isDescending`,
`DISTANCE` and empty/stable-shape branches. The existing `javap -c -p` command
with class `net.minecraft.world.level.block.ScaffoldingBlock` reproduces that
inspection. This is an explicit conditional scaffold model, not a blanket
exemption of ordinary air from support checks.

All ten bases and swept columns pass before their modeled feet positions are
enabled. A direct negative case attempts to climb from(-288,31,-38) into the
unbuilt Y32 gap and is rejected. Initial raw/local route checks still execute
with no modeled scaffolds. No world or configuration was changed.

## Complete post-construction movement circuit declaration

Start and finish at R01's northern inner standing station(-288,37,-3). Perform
one full inner hall ring, then visit the northern branch (terminal alcove and
joined tower circuit), western branch (upper lava approach, entrance shaft and
western lower excursion), and eastern branch (entrance shaft and eastern
excursion), returning to the standing station after each. Follow the southern
spoke and overhead hall link to R02's northern inner station(-288,37,25).
Perform its ring, eastern cells and lower terminal branches, southern reward/lava
approach and southwestern shaft/excursion, returning to that station after each.
Return to the original R01 station through the overhead link.

Reuse the already verified hall rings/spokes. Between a hall's northern station
and another spoke's inner station, select the shorter of the two ring directions,
using the stored forward order for ties. Join that inner station to its outer
threshold with the reversed verified spoke. Full ring surveys and branch returns
are intentional parts of this declared route, not claimed minimum movement.

At the cells, perform each existing cell inspection out and back from the shared
hall threshold. Then traverse the eastern stairs, inspect the northern ledge,
eastern alcove and southern connector with its east/west stubs, and return.
At the southern upper junction, inspect the eastern lava approach once while
passing toward its terminal reward. Each entrance-shaft transfer includes the
adjacent upper approach, one step into the explicit column, six vertical blocks
and the exit step to the lower junction. The overhead transfer includes both
four-block columns and its twelve-block tunnel.

Require exact seams, one closed coordinate route and full occupancy/support
validation with the declared post-construction state. Then calculate cardinal
horizontal distance, absolute ascent/descent and visited floor span directly
from consecutive coordinates. These remain post-construction movement results:
initial excavation, placement, source access, door inputs, loot transfer, combat
and final verification still need their explicit complete-task accounting.

The complete post-construction circuit passes at1,426 horizontal blocks,
84 blocks of ascent and84 of descent, starting and ending at(-288,37,-3).
Its visited feet elevations span25..43. The highest point is the earned overhead
bypass, not an authored upper room; the lowest is the inspected eastern lower
shaft rim, not a verified continuation below the retained boundary. The18-block
span is therefore specific to this circuit and its remedies.

Coverage is checked against the existing room footprints and saved container
set. The route enters all25 activity footprints. For each of the31 chest/barrel
nodes it includes at least one exact standing station from an already validated
interaction ray. The ray checks are retained by the existing checker and matched
to the joined route; an arbitrary point inside a room is not enough to establish
reward access. Each selected ray also avoids every cell occupied by the44 modeled
scaffold blocks, so adding the scaffold columns does not silently occlude it.
The original lid defects and their declared remedies remain part of the result.

This closes continuous post-construction movement and reward-station coverage
for the first assembly. It does not close the complete expedition model. In
particular, the initial drops, construction approaches, source-removal stations,
tool changes, button operations, acquisition assumptions, enemy population and
combat/survival conditions must still be joined to this route or explicitly
accounted for as additional phases. Actual traversal/combat times and acquired
loot remain NOT MEASURED.

## Occupied-source combat case and invalidation conditions

Use the approved reusable conditional accounting method for a specifically
defined occupied-source case, P6. This is an analyst-defined encounter input,
not the observed entity population or a prediction of typical dungeon combat.
At task start, stipulate six distinct adult enemies for each saved source:
30 cave spiders and six each of skeleton, ordinary spider, witch and zombie.
The 54 individuals have nominal source health, no extra armor/equipment modifiers,
effects, passengers, reinforcements or prior damage. Retain the zombie's inherent
armor instead of treating it as zero. Natural spawning is excluded from this
timing case, while its separate authored potential remains in the assessment.

The population is not one successful four-attempt spawn batch. It is a stipulated
already-occupied encounter state. For every still-active source, require its
exact-class nearby count to remain at least six whenever the source evaluates
that condition, until the actor destroys it. Count individuals once in the combat
workload even if nearby query volumes overlap. The five cave-spider groups and
four chamber groups are distinct individuals in P6. No assumption of stationary
AI, invisible cages, changed spawner NBT or a guaranteed containment mechanism
is made. Whether the required population remains nearby during the actual task
is NOT MEASURED. Losing this condition invalidates P6 rather than licensing an
unrecorded additional wave.

This suppression condition has a precise source basis. The pinned
`BaseSpawner.serverTick` uses `EntityTypeTest.forExactClass(entity.getClass())`,
the source block's unit AABB inflated by saved `SpawnRange`, and the
`NO_SPECTATORS` selector. If the count is at least `maxNearbyEntities`, it calls
`delay` and returns before adding the candidate entity. Here the saved values
are six and four respectively, making each query box
[X-4,Y-4,Z-4,X+5,Y+5,Z+5]. A cave spider does not suppress an ordinary-spider
source simply by being a Spider subclass. The nearby cap also is not a global
cap on living dungeon enemies: outside P6, enemies can leave the box and further
waves can occur. All saved Delay0 values remain unchanged.

Use six combat phases: one after each of the five cave-spider sources is removed,
and one after all four buried chamber sources are removed. Clear the relevant
six or 24 stipulated enemies before leaving that phase, returning to its source-
access station. Pursuit, target switching and return from pursuit belong only
to the approved combat duty allowance. Do not charge them again as ordinary
route distance or per-enemy targeting inputs. Source-access movement, mining,
tool selection and phase decisions remain separate costs to integrate.

Reuse the unenchanted iron sword, no criticals/sweeps, nominal six-damage hit and
13-tick full attack-cycle model from the [pinned combat source](../model-source/README.md).
New direct source inspection establishes `CaveSpider.createCaveSpider`
overriding maximum health to 12 and `Witch.createAttributes` setting 26. The existing
source already establishes skeleton/zombie health 20, spider health 16 and zombie
armor 2. Its zero-toughness armor formula gives the zombie 5.904 received damage
per nominal hit. The resulting workload is:

| Enemy | P6 individuals | Nominal health | Required full hits each | Total attack ticks |
| --- | ---: | ---: | ---: | ---: |
| Cave spider | 30 | 12 | 2 | 780 |
| Skeleton | 6 | 20 | 4 | 312 |
| Ordinary spider | 6 | 16 | 3 | 234 |
| Witch | 6 | 26 | 5 | 390 |
| Zombie | 6 | 20 | 4 | 312 |
| Total | 54 | Variable | 156 total hits | 2028 |

At 20 TPS this is 101.4 seconds of nominal attack-cycle work. Dividing by the
approved A/B/C duty fractions 1/.75/.5 gives 101.4/135.2/202.8 seconds for the
combat phases only. These are neither a whole-task duration nor guaranteed
combat bounds. The finite workload is conditional on P6 remaining valid.

Witch healing and hostile status effects are material limitations, not hidden
adjustments to the five-hit estimate. `Witch.aiStep` can select a healing potion;
`performRangedAttack` has harming, slowness and poison choices and separate
healing/regeneration choices for raider targets. `CaveSpider.doHurtTarget` adds
poison after a successful hit against a living target, with seven seconds on
NORMAL and fifteen on HARD. Successful status application, witch healing,
additional equipment/effects, extra enemies, reinforcement or altered attributes
invalidates this nominal no-effect workload. Death, required healing or movement/
input interruption outside the declared allowances also censors a successful
complete-task estimate. No success probability, actual potion use, poison damage
or realized encounter is inferred from these methods.

The five source entity types plus the separate illusioner/pillager/vindicator
natural override constitute eight authored hostile-type possibilities across
the family inputs. P6 uses five of those types; it does not redefine the actual
dungeon's diversity as five or erase the natural override. This distinction
must remain visible in the final quality assessment.

Reproduce the direct inspection with the already pinned SRG artifact (SHA-256
26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71,
reverified for this inspection):

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap \
  -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar \
  -c -p net.minecraft.world.entity.monster.CaveSpider \
  net.minecraft.world.entity.monster.Spider net.minecraft.world.entity.monster.Witch \
  net.minecraft.world.entity.monster.Zombie net.minecraft.world.entity.monster.AbstractSkeleton \
  net.minecraft.world.level.BaseSpawner
```

Reproduce the conditional arithmetic without another measurement tool:

```sh
uv run python - <<'PY'
import math
rows = [('cave_spider',30,12,0),('skeleton',6,20,0),('spider',6,16,0),
        ('witch',6,26,0),('zombie',6,20,2)]
total = 0
for name,count,health,armor in rows:
    effective = min(20,max(armor-6/2,armor*.2))
    damage = 6*(1-effective/25)
    hits = math.ceil(health/damage)
    ticks = count*hits*13
    total += ticks
    print(name,count,health,damage,hits,ticks)
print('total ticks',total,'combat seconds',[total/20/d for d in (1,.75,.5)])
PY
```

This resolves a bounded encounter input and nominal combat work for subsequent
complete-task integration. The actual saved-world population, suppression
success, natural encounters, survival and combat duration remain NOT MEASURED.

## Construction-station integration declaration

Retain all successful interaction rays from the existing checker, extending its
reward-ray retention to the construction targets rather than adding a separate
measurement path. All112 hypothetical removals already have a recorded ray.
Comparison with the full movement circuit finds two unvisited mining stations:
(-298,33,28) for the southern entrance vein and(-288,27,2) for the dungeon's
southern source floor. The three entrance shafts also require their adjacent
lower placement stances, rather than a direct exit to the next junction.

On the first descent of each entrance shaft, step from its base to the declared
placement stance and back before continuing: eastern(-278,33,0), western
(-300,33,5), and southwestern(-298,33,28). These are three two-block horizontal
detours. The southwest stance also supplies the missing vein-removal access.
Do not repeat these placement detours on the return trip.

In the dungeon's forward ring, replace the direct step from(-287,27,1) into
the southern hole with(-287,27,2),(-288,27,2), then the hole at(-288,26,1).
This reaches the existing floor-mining station before descending and adds two
horizontal blocks. The northern and eastern holes already have their declared
mining approaches in forward order. For the western hole, the earlier proof
mined from the north, which the forward circuit reaches only after the hole.
Validate an alternative from the southern station(-291,27,-1): first remove
the down-facing vein at(-291,27,-2), then its floor atY26, then descend and use
the already verified source ray. Test these rays with those western targets
restored to their original raw state in the hypothetical removal model. Preserve
any failure; do not rely on a ray through an already removed target obstruction.

The forward western-source alternative passes with its vein, floor and source
restored in the hypothetical obstruction set before the ordered checks. The
southern vein/floor rays, descent and existing source ray are valid; no extra
block removal or northern detour is needed. The original hypothetical state is
restored afterward, and the original northern approach remains retained evidence.

The construction-access route passes at1,434 horizontal blocks,84 ascent and84
descent. Its eight extra horizontal blocks are exactly the three two-block shaft
placement detours and the two extra southern-floor approach steps. Each shaft
detour is inserted only on its first descent. The southern approach occurs once,
before entering that hole in the forward circuit. All original movement points
and therefore all25 room/reward-access coverage remain present.

The executable verifies that every one of the112 removal targets has a recorded
ray whose standing station occurs on this route, and that all three declared
entrance placement stances occur. The original local construction checks retain
their raw-obstruction order; this new coverage check does not relabel a ray
through cleared space as an original-state action. The complete timing schedule
still must assign actions at the appropriate first visit, preserve removal and
placement prerequisites, distinguish initial falls from subsequent climbs, and
include tool/input, acquisition, P6 combat and verification costs. These access
distances alone are not a complete construction or expedition time.

## Complete first-assembly task declaration, P6

Start at(-288,37,-3) with the saved construction obstacles present and no
scaffolds placed. Follow the declared work route, execute all112 removals and44
placements as their stations are first reached, disable all nine sources, defeat
the54 stipulated P6 enemies in the six declared combat phases, acquire one
available stack from each of the31 chest/barrel nodes, and return alive to the
same station with those acquisitions. Discovery, surface approach and extraction
to an external base are outside this local task. It does not claim complete
emptying of every container or acquisition of the two central gold blocks.

Actor: one adult player, initially full health/food, fresh unenchanted iron armor
and sword, fresh diamond pick,44 carried scaffolds, an empty-hand selection and
31 inventory slots reserved for reward stacks. Full layout and target knowledge;
no flight, teleportation, critical/sweep attacks, extra construction, external
help, effects or deliberate healing/restocking. Do not credit regeneration as
a modeled survival benefit. Sufficient food/capability to maintain the selected
movement profile and survival throughout remain success conditions, not outputs.

At each container, take its first eligible nonempty stack into one reserved slot
and confirm it. Use the approved acquisition allowance k=1/2/4 seconds per node
as a conditional GUI/transfer budget, including selection and confirmation; this
is not measured Lootr behavior or a guaranteed inventory operation. If a node is
empty, unavailable to this actor, fails to open after the specified remedy or
cannot transfer within that allowance, censor successful completion. Do not
invent an acquired item from its table reference. One stack per node requires
at most31 reward slots; two tools and a remaining scaffold stack fit alongside
them within36 slots. Armor uses its separate equipment slots.

Preserve local construction prerequisites: mine blocking webs/rubble before
advancing; open each button door only after its input/selection pause; remove
each shaft cover before its first descent; place the complete return column
from the validated lower stance before leaving; clear the middle piston panel
before proceeding; build each library column before its elevated lid remedy;
and remove each dungeon floor before descending into its source hole. The
dungeon source order is north/east/south/west, using the now verified forward
western approach. Clear each source's P6 combat group immediately after disabling
it; the four chamber sources form one group after the fourth disablement.
Container acquisition occurs at its first accessible visited station, which may
precede that chamber's group combat. No safety during GUI use is assumed.

The post-construction geometry establishes the work path and station access.
Applying its local action proofs in this order is the conditional execution
schedule, not a live replay. Any prerequisite, body clearance or interaction
failure during that execution invalidates the successful estimate. This includes
entity obstruction or a sculk response that adds an encounter, changes the path
or interrupts work beyond the declared allowances. No sculk block is silenced
or removed to manufacture this condition; actual warning/Warden response remains
NOT MEASURED.

Use the approved A/B/C upright speeds u=5/4/3, vertical transition allowances
j=1/.5/.25 blocks/s, decision pauses n=.5/1/1.5 seconds, interaction allowances
a=.25/.5/1, hotbar selections s=.25/.5/1, acquisitions k=1/2/4, verification
v=2/4/8 and combat duty d=1/.75/.5. These remain analyst sensitivity cases.
Make the following counting rules explicit before deriving the total:

- Charge one stationary navigation/pose pause at each change in the work route's
  three-component step vector, plus one initial orientation and two phase-boundary
  pauses per combat group. This includes landing/column direction changes.
  Pauses occur before a door button is pressed or after the actor clears its
  threshold, never inside its timed transfer. The fixed route has no direction
  change inside those straight transfers.
  For a first fall, move the entry-direction pause to the last supported ledge
  before stepping into the shaft; the model does not pause while standing on air.
- Deliberately select the required hotbar slot before each mined block, even
  when it was already selected; before each of ten column-building sequences;
  before each of six combat phases; and before each button or container action.
  This explicit input protocol avoids an unstated zero-cost tool-switch policy.
- Charge one aiming/input allowance for each removal, each placed scaffold,
  each of12 button operations and each of31 container openings. Mining begins
  after that allowance. The mining allowance does not include breaking ticks;
  the container-opening allowance does not include stack transfer.
- Charge each of31 acquisition allowances once, and one final verification.
  Combat pursuit, attack target switching and return from pursuit are charged
  only through duty, not again as route distance or per-enemy targeting inputs.

Seven first descents are falls, not scaffold travel: three six-block entrance
shafts, three four-block tower shafts and the four-block southern overhead
shaft. Remove those34 vertical blocks from the j term. For these falls only,
use zero initial vertical velocity as the conservative tick-phase convention,
with a permitted departure velocity between one ordinary gravity/drag update
(-.0784000015258789 blocks/tick) and zero. Require ordinary gravity, no jump, fluids,
climbable blocks, effects or midair obstruction, and the verified full landing
support. Model each tick as movement at current velocity followed by
`vy = (vy - .08) * .9800000190734863`, stopping on the landing collision.
This includes the first zero-velocity tick; horizontal entry is separately
budgeted. Landing decisions are already counted in n. An initial velocity outside
that interval, different gravity or different collision state invalidates this
nominal fall budget. Downward velocity within the interval can land sooner; the
zero-velocity calculation is the charged phase convention, not a predicted exact
landing time.

The same pinned `LivingEntity.travel` obtains gravity, moves through
`handleRelativeFrictionAndCalculateMovement`, subtracts gravity and then applies
the quoted vertical drag for an ordinary non-flying actor. `getDefaultGravity`
reads `Attributes.GRAVITY`, whose default is .08. These are source-derived
nominal ticks, not timed server/player observations. Reproduce with the pinned
`javap -c -p` command and classes `net.minecraft.world.entity.LivingEntity` and
`net.minecraft.world.entity.ai.attributes.Attributes`.

The executable finds373 step-vector changes, giving386 decision events after
initial orientation and the twelve combat-boundary pauses. The fixed action
protocol gives199 aiming/input events (112 removals,44 placements,12 buttons,
31 container openings) and171 explicit hotbar selections (112 mining, ten column
sequences, six combat phases,12 buttons and31 container actions). The acquisition
allowance also covers closing each GUI before route movement resumes. No input
pause is charged inside an already-started button transfer.

The nominal fall recurrence gives11 ticks for four blocks and14 for six blocks,
including its initial zero-velocity tick. Seven matched first descents therefore
contribute86 ticks/4.3 seconds. The remaining134 vertical blocks use j. The six
vine-limited horizontal transfer blocks use three blocks/s in all profiles.
The complete conditional time in seconds is:

`T = 1428/u + 6/3 + 134/j + 4.3 + 47.55 + 386n + 199a + 171s + 31k + v + 101.4/d`.

| Phase, seconds | A | B | C |
| --- | ---: | ---: | ---: |
| Movement, including nominal initial falls | 425.90 | 631.30 | 1018.30 |
| Active mining | 47.55 | 47.55 | 47.55 |
| Navigation/phase decisions | 193.00 | 386.00 | 579.00 |
| Targeting/interaction inputs | 49.75 | 99.50 | 199.00 |
| Explicit hotbar selections | 42.75 | 85.50 | 171.00 |
| Conditional acquisition | 31.00 | 62.00 | 124.00 |
| Final verification | 2.00 | 4.00 | 8.00 |
| Noncombat subtotal | 791.95 | 1315.85 | 2146.85 |
| P6 combat | 101.40 | 135.20 | 202.80 |
| Complete conditional task | 893.35 | 1451.05 | 2349.65 |

Report approximately893/1451/2350 seconds, or14.9/24.2/39.2 minutes, preserving
profile and P6 conditions. These are not percentiles, confidence limits, observed
human times, expected first-clear times or guaranteed bounds. Their deliberate
inspection returns, per-operation selections and conditional acquisition objective
are part of this particular task, not claimed optimal play.

The fresh-tool assumption has a nominal durability check. The43 web removals
consume86 sword durability and the156 nominal hits consume156, totaling242 of
the iron tier's250 uses. This leaves only eight nominal uses. The62 pick-mined
blocks consume62 of the diamond tier's1561 uses. Other declared removals use
the empty hand. `SwordItem.createToolProperties` sets damage per mined block to
two, `SwordItem.postHurtEnemy` charges one, `Tier.createToolProperties` sets one
per pick-mined block, and `Item.mineBlock` applies that component on nonzero-
hardness blocks. `Tiers` supplies the250/1561 capacities. Reproduce with the
same pinned `javap -c -p` command and classes `net.minecraft.world.item.SwordItem`,
`net.minecraft.world.item.Item`, `net.minecraft.world.item.Tier` and
`net.minecraft.world.item.Tiers`. Extra durability loss or insufficient remaining
durability invalidates the no-restocking case; no actual tool wear is measured.

Reproduce movement, action counts, matched falls and the complete table with
`uv run python -m evidence.item-13.underground_temple_route`. Source/P6 nominal
attack arithmetic remains reproduced in the preceding section. The complete
timing case now accounts for every declared phase, while preserving the distinction
between source-derived work, geometry, provisional allowances and unobserved
runtime success. Family/variant coverage and the remaining quality assessments
are still required before this family or Item13 can be complete.

## First assembly loot, finale and replay assessment

SOURCE INSPECTION uses the retained Explorations archive SHA-256
420d0373711877a5e1a86b7f9b4f54848f3debb2f116c2509a5cc4eb496c979e.
The paths below are relative to
`data/explorations/loot_table/chests/underground_temple/` in that archive.
`large_room.json` and `dungeon.json` are byte-identical, both SHA-256
fe6a768ad8f3a3d3fedea2bac03605e8e7194161c4d41a843607f77e7e519540.
Their first pool has two to four weighted draws including metals, gems, mob
materials, horse equipment, enchanted-book potential, apples and an empty entry;
the second has four draws of bone, gunpowder, flesh or string. The four-source
chamber therefore has no distinct base reward table from the eight main-hall
chests. This is a comparison of potential, not generated item equality.

`quest_tower.json`, SHA-256
777e3a82ffc5996c8dcc0d47f384d3d560aedda52a6672f25d7dfbd92e5d5186,
has different potential: diamond count zero to five, flesh, an equal-weight
book-or-golden-apple draw, and gold ingots. Its book options are protection,
sharpness, looting and mending. The final golden-apple pool sets its count with
binomial n=0, p=.1, so that particular bonus contributes zero; preserve this
source defect. It does not negate the separate apple alternative or establish
that a diamond or enchanted book will be obtained. No loot roll is performed.

Reproduce these direct source comparisons without a new measurement tool:

```sh
uv run python - <<'PY'
import hashlib
import zipfile
from pathlib import Path
p = Path('downloads/item3/candidates/explorations-neoforge-1.21.1-1.6.2.jar')
assert hashlib.sha256(p.read_bytes()).hexdigest() == '420d0373711877a5e1a86b7f9b4f54848f3debb2f116c2509a5cc4eb496c979e'
with zipfile.ZipFile(p) as archive:
    for name in ('large_room', 'dungeon', 'quest_tower'):
        raw = archive.read(f'data/explorations/loot_table/chests/underground_temple/{name}.json')
        print(name, hashlib.sha256(raw).hexdigest(), raw.decode())
PY
```

Authored finale: NONE identified in this assembly's inspected source and layout.
The tower is a transit setpiece leading onward into the lower network. Its two
upper chests and one middle chest precede the bottom lava route, which has no
reward node. The deeper R08 chamber has four hostile source types but the same
base loot table as the main halls. Neither the name `quest_tower` nor maximum
graph depth establishes a terminal objective. The following assessment addresses
the strongest candidate, the tower, without promoting it to a finale:

| Final-room quality dimension | Disposition | Supported reason |
| --- | --- | --- |
| Objective clarity | ABSENT | No terminal goal or completion trigger identified; the network continues below |
| Distinctive challenge | PRESENT | Three floor descents, tripwire/dispenser zone, piston panel and lava route differ from the repeated source corridors |
| Reward linkage | CONDITIONAL | Three assigned chests have access routes, but all precede completion of the bottom hazard sequence; contents remain unrolled |
| Route integration | PRESENT | Tower connects R01 through J01 to the lower bedroom/library/chamber network |
| External bypass exposure | UNKNOWN | No validated surface-to-tower or cave-to-tower route; local boundary exposures do not establish one |

Concrete internal shortcuts remain compatible with earned sandbox freedom.
The two upper tower chests have the validated 34-horizontal-block return from
J01, with one web removal and a button door, before any lower descent. R08's
four chest stations have a native 42-horizontal-block survey before its source
floor excavation. Thus chest access itself is not gated by destroying those
four sources. Neither shortcut proves combat avoidance: active sources and the
natural override remain possible, and the R08 sources can be within activation
range while a player is in the main hall above. Do not call the hall safe merely
because its own room allocation has no spawners.

The declared overhead hall connection costs 28 removals and eight scaffolds;
the alternate first tower drop costs its floor removal and four scaffolds and
avoids the inspected tripwire line. The two-block middle panel breach, six-block
library masonry remedy with six scaffolds, and four-bar cell breaches are further
specific access remedies. These costs are already included in the complete task,
not additional rewards or free bypasses. The T11 exposed ledge and T07 continuation
below the retained Y21 boundary remain unresolved external-access opportunities,
not proven entrances, exits or safe escape routes.

Meaningful hazards are supported at different evidence levels: lava contact is
avoided by the validated dry paths; seven initial drops require the declared fall
conditions; webs impose measured removal work; nine lit campfires have a source-
verified contact mechanism but are avoided; the tower tripwire has an inspected
trigger/input chain but no observed firing trial. Sources create conditional
encounter pressure, not nine measured encounters. Environmental sculk response
remains an explicit P6 censoring condition. Narrow button doors are measured
chokepoints: the conservative two-sided plate exclusion leaves a .625-block
channel for the .6-wide actor, with two-block door height and timed transfers.
This proves a constrained connection, not live enemy exploitation or an absence
of additional mining alternatives.

Expected replay value is an assessment of inputs. The selected jigsaw component
and assembly variation supports different generated layouts, with repeated
source corridors, branching and distributed rewards. It does not establish
player enjoyment or quantify the probability of a good assembly. The six minimal
starts among 24 indexed starts remain the finite-frame failure observation,
representing three seed/location pairs repeated twice; the missing start-pool
weight is not an observed failure probability. The second complete assembly and
remaining component read are still needed for the declared material comparison.

Revisiting this same persistent dungeon after the modeled task has different
inputs: nine sources have been destroyed, 43 webs removed, access breaches made
and 44 scaffolds placed. Those changes simplify later movement and remove those
particular source mechanisms. A per-player reward system would not by itself
restore physical geometry or spawners. Natural spawning, trap resources and
unmeasured environmental responses prevent a claim that future visits are empty.
Actual loot availability on revisit and player replay behavior are NOT MEASURED.

Large-but-shallow disposition for the whole assembly: NOT ESTABLISHED. Its 25
primary spaces (11 to 26 under the documented partition alternatives), connected
floor progressions, six source areas and distributed rewards supply actual
mechanical content beyond architectural volume. Local thin-content features
are supported: four terminal alcoves have only campfires under the potential-
content definition; five corridors repeat the cave-spider/web motif; and each
large hall has one connected floor/spoke system rather than extra progressions
proportional to its height. The zero empty/dead count uses a permissive potential
threshold and must not be presented as uniformly substantial activity.

## First assembly burial context

The already retained raw extract includes all 8,633 footprint columns of saved
WORLD_SURFACE. The existing Item7 decoder converts values to top non-air block
Y with `value + min_y - 1`; these are not first-air coordinates. Surface Y spans
175 to 273. Relative to the assembly envelope top Y50, the vertical separation
is 125 to 223 blocks. At the declared entry stance (-288,37,-3), surface Y220 is
183 blocks above the feet. These are heightmap separations, not a count of solid
roof blocks or a validated mining path: caves, foliage and overhangs can intervene.
The local exposed T11 ledge at(-252,33,14) lies below surface Y243, and T07 at
(-261,25,-34) below Y206. Neither is demonstrated open to the sky.

Reproduce from the existing hash-verified extract, without another world read:

```sh
uv run python - <<'PY'
import gzip
import hashlib
import json
from pathlib import Path
p = Path('evidence/item-13/fixed-blocks/explorations-underground-temple-mountainous-r2.json.gz')
raw = p.read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'e86316d3e1fd412a6507533b0f3ac603e3948cb5585d6d95a917fe5168164085'
case = json.loads(gzip.decompress(raw))['cases'][0]
surface = {(x, z): y for x, z, y in case['surface_xzy']}
print(len(surface), min(surface.values()), max(surface.values()))
print('surface minus envelope top', min(surface.values()) - 50, max(surface.values()) - 50)
for x, y, z in ((-288, 37, -3), (-252, 33, 14), (-261, 25, -34)):
    print((x, y, z), surface[x, z], surface[x, z] - y)
PY
```

This integrates the first assembly's supported quality conclusions. The following
scoped distance derivation resolves its remaining route-block depth measurement.
Family and Item13 status remain IN PROGRESS.

### Declared scoped route-distance derivation

Use the already validated work-route cells and only consecutive route transitions
as the coordinate network. Keep transitions directed as actually checked; do not
invent an edge between adjacent but untested cells. Cost each transition by its
horizontal plus absolute vertical block displacement. From the declared entry
(-288,37,-3), compute shortest weighted distances to each room's visited footprint
and to each reward's accepted, scaffold-unobstructed interaction stations. Report
all 25 rooms and all 31 rewards. This directly supplies the missing route-block
depth dimension without treating the 1,602-block work circuit as shortest depth.
It is a post-remedy network metric, not an optimal first-clear itinerary, global
shortest path through all geometry, construction cost or surface-to-entry route.
Door activation conditions remain required but input times are outside distance.
Runtime budget is the existing small route proof plus one finite shortest-path
pass; no world materialization, generation or new raw capture is required.

The scoped pass reaches every checked station. The deepest checked station is
149 route blocks from entry. Room-footprint distances range from zero to 112;
reward-station distances range from zero to 143. Zero means an interaction
station at the declared starting point, not zero acquisition work. Directed
survey segments can make these distances longer than a reversed or alternative
route not present in this network; do not present them as global geometric minima.
The complete task still requires its separately reported construction and timing.

| Room footprint | Shortest scoped blocks |
| --- | ---: |
| R01 | 0 |
| R02 | 40 |
| R03 | 26 |
| R04 | 47 |
| R05 | 73 |
| R06 | 102 |
| R07 | 111 |
| R08 | 112 |
| R09 | 67 |
| R10 | 72 |
| R11 | 56 |
| R12 | 27 |
| R13 | 34 |
| R14 | 52 |
| R15 | 73 |
| R16 | 73 |
| R17 | 27 |
| R18 | 38 |
| R19 | 98 |
| R20 | 84 |
| R21 | 38 |
| R22 | 74 |
| R23 | 52 |
| R24 | 112 |
| R25 | 112 |

| Reward block (X,Y,Z) | Shortest scoped station blocks |
| --- | ---: |
| (-324, 33, 5) | 54 |
| (-307, 31, -25) | 122 |
| (-300, 31, -25) | 119 |
| (-295, 27, -16) | 114 |
| (-290, 27, -2) | 143 |
| (-290, 39, -33) | 35 |
| (-290, 39, 47) | 76 |
| (-289, 37, 0) | 6 |
| (-289, 37, 28) | 52 |
| (-288, 27, -4) | 117 |
| (-288, 27, 0) | 135 |
| (-288, 37, -1) | 0 |
| (-288, 37, 1) | 12 |
| (-288, 37, 27) | 46 |
| (-288, 37, 29) | 58 |
| (-287, 37, 0) | 6 |
| (-287, 37, 28) | 52 |
| (-286, 27, -2) | 125 |
| (-286, 35, -29) | 59 |
| (-286, 39, -35) | 39 |
| (-282, 27, -25) | 106 |
| (-282, 27, -19) | 106 |
| (-281, 27, -12) | 114 |
| (-281, 30, -24) | 106 |
| (-281, 30, -23) | 106 |
| (-281, 30, -21) | 106 |
| (-281, 30, -20) | 106 |
| (-278, 33, 17) | 40 |
| (-274, 39, 25) | 67 |
| (-272, 39, 22) | 76 |
| (-252, 33, 10) | 64 |

Reproduce both tables with `uv run python -m evidence.item-13.underground_temple_route`.
The existing raw hash, full route and ray checks execute before this derivation.
Focused Ruff formatting/lint, type checking and the route executable pass.
This first representative now has integrated topology, scoped depth, vertical
progression, complete conditional task time and quality assessment. Proceed to
the remaining three predeclared reads; no family-wide completion is implied.

## Remaining predeclared saved-block reads

The first representative's end-to-end integration gate has passed. Execute the
other three reads from the existing selection without changing their bounds.
These are static reads from accepted restores, with complete inventory checks
before and after each read under the existing POSIX record lock. They are not
new controlled gameplay experiments. Keep the 180-second and 10-MiB per-read
limits and 5-GiB free-space floor. Retain a completed output even if its resource
limit fails; do not replace it with a passing retry. The original incomplete
assembly remains incomplete when its bounded component is inspected.

Run from the repository root with each output absent:

```sh
uv run python - <<'PY'
import gzip, hashlib, importlib, json, resource, shutil, signal, time
from pathlib import Path
from tools.analyze_route_opportunities import read_bound
sha = '6e8a56b7fc4f97e2c2e61f45d6cef286172c4cbba788d679536db477bc39ae78'
plan = json.loads(read_bound(Path('evidence/item-13/underground-temple-selection.json'), sha))
rows = json.loads(read_bound(Path('evidence/item-13/candidates.json'), plan['input_sha256']['candidates']))['candidates']
extract = importlib.import_module('evidence.item-13.measure').extract

def timeout(signum, frame):
    raise TimeoutError('predeclared read exceeded 180 seconds; preserve prior outputs')

signal.signal(signal.SIGALRM, timeout)
for label, case in (('ordinary-r1', plan['selected'][1]), ('large-hall-down', plan['component']), ('missing-small-hall-down', plan['failure'])):
    original, = [row for row in rows if row['id'] == case['id']]
    if label == 'large-hall-down':
        changed = {'bounds', 'envelope', 'voxel_count'}
        assert all(case[key] == value for key, value in original.items() if key not in changed)
        start = json.loads(gzip.decompress(read_bound(Path(case['start_record_path']), case['start_record_sha256'])))
        selected, = [row for row in start['starts'] if row['id'] == case['id']]
        piece, = [row for row in selected['start_nbt']['Children'] if row.get('pool_element', {}).get('location') == 'explorations:underground_temple/rooms/large_hall_down']
        assert piece['BB'] == case['component_bb']
    else:
        assert case == original
    output = Path(f'evidence/item-13/fixed-blocks/explorations-underground-temple-{label}.json.gz')
    assert not output.exists() and not output.is_symlink()
    assert shutil.disk_usage('.').free >= 5 * 1024**3
    begun = time.monotonic()
    signal.alarm(180)
    try:
        result = {'selection_sha256': sha, 'cases': [extract(case, voxel_budget=case['voxel_count'])]}
        result['elapsed_seconds'] = round(time.monotonic() - begun, 6)
        result['peak_rss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        raw = gzip.compress((json.dumps(result, sort_keys=True, separators=(',', ':')) + '\n').encode(), mtime=0)
        with output.open('xb') as stream:
            stream.write(raw)
    finally:
        signal.alarm(0)
    print(label, len(raw), hashlib.sha256(raw).hexdigest(), result['elapsed_seconds'], result['peak_rss_kib'], flush=True)
    assert result['elapsed_seconds'] <= 180 and len(raw) <= 10 * 1024**2
PY
```

All three reads passed. Each extraction verified the accepted complete-world
inventory before and after reading, required full chunks/sections, and stayed
within the declared resource limits. Producer is `measure.py` at commit8465b5ba;
no server was launched and no raw world was changed.

| Read | Cells | Compressed bytes | Elapsed seconds | Process peak RSS KiB | SHA-256 |
| --- | ---: | ---: | ---: | ---: | --- |
| [Second assembly, ordinary r1](explorations-underground-temple-ordinary-r1.json.gz) | 329208 | 45810 | 9.999266 | 77588 | faed7df352cdcfc1938fb4d49f4f84b2519ad4f1ee55044fa661ae55e6f81d5c |
| [Scoped large_hall_down](explorations-underground-temple-large-hall-down.json.gz) | 33852 | 12771 | 8.725831 | 82892 | a62c45cb2dd69fce020e28b78faf438314ff7e5abb97ebda149ec29699a84c8a |
| [Missing small_hall_down failure](explorations-underground-temple-missing-small-hall-down.json.gz) | 512 | 958 | 8.690210 | 82892 | c8fcd094bf43f7ca3785edc3d58289ef171e875dbd7252fa96915685007fde01 |

Peak RSS is cumulative process high-water usage, not independent per-read memory.
Raw metadata retains archive and world identities. All four planned captures are
now available; this is capture completeness, not family assessment completeness.

### Missing-template failure disposition

The selected ocean-heavy r1 start has one serialized jigsaw child naming the
missing `rooms/small_hall_down`, with no junctions and BB[-360,-33,231,-359,-32,232].
Every one of the 512 padded cells is solid terrain: 508 deepslate, two Create
deepslate zinc ore and two deepslate lapis ore. There are no block entities.
The four envelope surface columns all have WORLD_SURFACE Y62. The saved start
record therefore does not represent a playable tiny dungeon. Its selected local
scope has zero authored playable rooms, sources, reward nodes or finale; it has
no dungeon route to time. Mark traversal/combat task NOT APPLICABLE (failed
placement), not a zero-second successful clear or a dead-room count over an
invented room. It remains one inspected member of the six indexed failure cases,
not a new estimate of their frequency or a reason to exclude the family.

### Second assembly initial distinctions

The ordinary r1 assembly contains 51 serialized pieces, including four tower
components; this is not a room count. Its saved fixtures include 29 chests and
six barrels (35 reward assignments), eight dispensers, five spawners, nine
campfires and eight bed blocks. Sources are one cave spider and four separate
witch/spider/skeleton/zombie sources. Tower rewards account for twelve chest
assignments across its four towers. These are source/fixture counts, not realized
enemies, generated loot or validated reward access. The first assembly's room
graph and route cannot be copied merely because some templates repeat.

The bounded large_hall_down read includes the original start anchor and portions
of neighboring rooms. Its eleven chest/barrel fixtures all lie outside the
component BB[-488,41,45,-472,55,61]; none may be attributed to that hall. The
component itself has an air-filled masonry interior surrounded by saved water
and aquatic plants, making fluid and external-access conditions material to its
local assessment. Its parent assembly's incomplete western boundary is unchanged.

Reproduce these direct saved-artifact counts with the immutable files above:

```sh
uv run python - <<'PY'
import collections, gzip, json
from pathlib import Path
for label in ('ordinary-r1', 'large-hall-down', 'missing-small-hall-down'):
    path = Path(f'evidence/item-13/fixed-blocks/explorations-underground-temple-{label}.json.gz')
    case = json.loads(gzip.decompress(path.read_bytes()))['cases'][0]
    print(label, 'pieces', len(case['start_nbt']['Children']))
    print('fixtures', collections.Counter(row['id'] for row in case['block_entities']))
    if label == 'missing-small-hall-down':
        print(collections.Counter(case['palette'][i]['Name'] for i in case['blocks_yzx']))
        print(case['start_nbt'], case['surface_xzy'])
    if label == 'large-hall-down':
        print('hall fixtures', [row for row in case['block_entities'] if -488 <= row['x'] <= -472 and 41 <= row['y'] <= 55 and 45 <= row['z'] <= 61])
PY
```

The scoped hall's [four-layer saved view](explorations-underground-temple-large-hall-down.png)
was rendered and visually inspected at Y42,43,44,49. The lower hall in the sheet
is the selected component; the upper reward hall and intervening fixtures are
anchor/neighbor context. It shows the central floor opening, surrounding stepped
floor, cardinal transitions and upper decorative framework. This is a saved-block
view, not proof of collision, stable fluid behavior or actor movement. Exact
support, shaft depth, transitions and a complete local task remain to validate.
The view must not borrow neighboring chests as the component's payoff.

```sh
uv run python evidence/item-13/render_pilot.py --input evidence/item-13/fixed-blocks/explorations-underground-temple-large-hall-down.json.gz --output evidence/raw/item13/underground-temple-large-hall-down.svg --layers 42 43 44 49
timeout 120 convert -background white evidence/raw/item13/underground-temple-large-hall-down.svg evidence/item-13/fixed-blocks/explorations-underground-temple-large-hall-down.png
```

Rendering exited successfully within the declared cap. SVG1,627,862 bytes remains
ignored, SHA-256178bcb00e27e1ac4de15ad54d5fee8dae667804f96cdbf1f0a8ac0e461ea9559.
PNG98,611 bytes, SHA-256672bcbd0500dab92be746ac4bdaf224643fcd7f3c55e662d338fffbf91bf993f.
Both remain below their declared size budgets.

## Scoped hall native topology declaration

Use the same adult .6-by-1.8 geometry, conservative stair ascent envelope and
no-mining/no-swimming assumptions as the first hall check. Bind the existing
clearance/support functions to this raw case with empty removal, door and
scaffold sets. The functions are moved unchanged into `temple_geometry.py` for
their two current consumers; this prevents rerunning or importing the first
assembly's experiment state merely to check a second raw case. No new collision
rules or generalized room inference are introduced.

The intended local objective is a dry survey from the northern threshold
(-480,44,45), visiting the inner floor ring, all four thresholds and a supported
central-opening rim, then returning to the northern threshold. Use the first
hall's four radial floor profiles translated to center(-480,53), low feet Y42
and threshold feet Y44. The 24-block ring at radius three avoids the central
opening; the rim station is(-480,42,51). Validate all links in both directions.
No rewards are assumed, no source is disabled, and the shaft is not entered.
This is the scoped component objective, not a substitute for whole-assembly timing.
Reject the central standing cell(-480,42,53) because its floor is air. Preserve
that failure rather than supplying an invisible floor or an undeclared scaffold.

The native local survey passes: 66 horizontal blocks, eight ascent and eight
descent, returning to the northern threshold. All four spokes, both directions
of the inner ring, and the rim approach pass the unchanged checker. The central
unsupported standing cell is rejected as declared. This is one continuous hall
activity space with an internal two-block floor span, not four rooms or fourteen
blocks of playable progression inferred from its shell height.

The opening contains a narrow central wall post and staggered slabs below it,
not a uniformly open three-by-three fall shaft. Exact saved cells at(-479,Y,52)
and(-479,Y,53) are air for Y38..41; stepping into those columns would leave the
validated supported floor and can descend below the captured minimum. The post
at(-480,40,53) is a waterlogged stone-brick wall, while(-480,40,52) is a waterlogged
bottom slab. Do not model either as a whole solid floor, claim a uniform fall
height, or infer a safe spiral descent from its template name. Start NBT identifies
an attached `shafts/large` component spanning Y23..40, but playable travel below
Y38 is outside this scoped capture. The second complete assembly includes that
shaft template and remains the planned complete-case opportunity to assess it.

### Scoped hall complete survey model

Predeclare the local actor at(-480,44,45), upright, fully informed of the fixed
route and opening, with ordinary walking/one-block jumping, no swimming, flight,
mining, placement or combat. Use fresh ordinary armor, full initial health/food,
no effects or assistance; equipment does not change the declared movement model.
Start on the first navigation decision; end after returning to the start and
verifying all four thresholds and the central rim were visited. No item transfer
is part of this fixture-free survey. This local component task complements the
complete assembly tasks; it does not time the incomplete parent dungeon.

Condition the case on no realized enemies, incoming attacks, fluid intrusion,
forced movement or changed geometry during the survey. This is a zero-enemy
scenario input, not an observation that the family natural override cannot spawn.
A departure from those conditions, missed threshold, fall into the opening,
required recovery or failure to return alive censors the complete task. No
success probability or expected player completion time is estimated.

Use the approved A/B/C movement and decision allowances: horizontal speed u=5/4/3,
vertical speed j=1/.5/.25, per-decision n=.5/1/1.5 seconds, final verification
v=2/4/8. Count one initial decision plus each three-component step-vector change.
There are no button, mining, acquisition or attack phases in this declared task.
Thus complete conditional seconds are `66/u + 16/j + N*n + v`, with N determined
from the validated survey, not an invented observation. Compute and report all
three profiles, keeping their assumptions and censoring rules attached.

The route gives N=49 decisions. Complete conditional survey times are55.7/101.5/
167.5 seconds (approximately56/102/168). Combat workload is zero only under the
declared zero-enemy scenario; realized enemy count, combat time and human traversal
remain NOT MEASURED. The hall has no saved spawner or resident block-entity source,
but the family's natural hostile override still applies as separate potential.

Scoped route depth uses the validated ring/spokes, not the full survey return.
From the northern threshold, the inner ring is five horizontal and two downward
blocks away (seven route blocks); the rim adds one horizontal block (eight).
Either east or west threshold requires those five inward blocks, six ring blocks
and five outward blocks, with two descent and two ascent: 20 route blocks. The
southern threshold uses twelve ring blocks instead: 26 route blocks. These are
shortest distances on that ring/spoke network; untested shortcuts across the
floor are excluded. A contracted local graph has one hall node and four threshold
nodes, four edges, and no inter-room cycle. From the north threshold the hall is
one edge away and each other threshold two. The ring is internal circulation,
not a second room or an additional inter-room branch. The central shaft is an
unresolved connection beyond this dry survey, not a fifth validated onward route.

The three cells just outside the north/east/west thresholds have stone-brick
support at Y43 and air at Y44..45. Immediately south,(-480,Y,62) is source water
at Y43..45. This is a concrete unsealed wet exposure at the southern doorway,
not proof of an underwater route to the surface or to loot. Moving through it
requires a swimming/breathing and fluid-state case outside the dry actor model.
No arbitrary indestructibility or route restriction is proposed. Without a live
fluid trial, the saved air interior must not be described as guaranteed stable
when neighboring water updates. Fluid arrival invalidates the dry survey case.

There is one scoped activity space. Under the protocol's supported hazard/content
definition it is not empty or dead (0/1 for each): it connects the thresholds and
contains the central unsupported descent boundary. This is a connective/hazard
role, not a hidden reward. If central hazard ingredients are excluded until a
runtime fall/flow trial, there are no reward, facility or realized-encounter
contents to substitute; its connective purpose still prevents calling it a
useless dead room. No authored finale exists in this component: objective clarity,
distinctive terminal challenge and reward linkage are ABSENT; route integration
is PRESENT through the floor/thresholds; external exposure is PRESENT at the wet
south door, while a useful external bypass remains UNKNOWN.

Expected local replay contribution is limited to navigation and the attached
shaft's role in a larger generated layout. This unchanged fixture-free floor has
no supported new reward objective on revisit, and no observed player replay
outcome is inferred. Its tall upper framework adds no demonstrated upper floor
progression to the two-block stepped floor. It is locally mechanically sparse
relative to its shell, but its connective purpose is explicit and the downstream
shaft cannot be dismissed as shallow from this partial capture. Do not generalize
this scoped result to the incomplete parent or to every temple assembly.

Reproduce the local geometry, negative case, exposure and timing with
`uv run python -m evidence.item-13.temple_hall_down`. The original assembly route
output remains byte-identical after moving its geometry functions; its complete
regression passes. Initial focused lint reported only wrapper complexity,
annotations and style issues; these were corrected without changing geometry.
The local interpretation remains conditional and bounded as described above.

Burial context is separate from playable depth. All289 hall-footprint
WORLD_SURFACE columns are Y62, seven blocks above the component top Y55 and
20 above its low feet Y42. This is saved surface-height separation, primarily
water context here, not seven blocks of solid protective roof or a measured
swimming distance. The local executable reproduces that footprint check.
The scoped hall assessment is now integrated; the second complete assembly and
its full shaft geometry remain the next unmet family coverage requirements.

## Second assembly shaft and initial hall declaration

The second assembly's `shafts/large` child spans[194,7,340,198,24,344]. Its inner
perimeter has17 bottom deepslate-brick slabs, one per Y8..24, rising around the
center post: (195,342),(195,341),(196,341),(197,341),(197,342),(197,343),(196,343),
(195,343), repeating around the perimeter. All17 slabs are saved waterlogged.
This is source/geometry evidence of the intended spiral, not17 rooms or a
validated17-block player ascent. The bottom slab's support is at Y+.5, not Y+1.
The initial dry full-cell checker must reject treating it as an integer-height
standing floor; that checker rejection does not prove the shaft unplayable.

Pinned `SlabBlock` source confirms the bottom collision box is[0,0,0,16,8,16]/16
and `getFluidState` returns a source water state when WATERLOGGED is true. Wet
contact and fractional support need explicit resolution before traversal timing.
Do not silently dry the raw slabs, introduce a scaffold, or label a geometric
spiral count as observed progression. The present evidence resolves the exact
missing geometry but leaves its native actor transition/physics case open.

Reproduce the source inspection with the previously pinned SRG archive:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap \
  -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar \
  -c -p net.minecraft.world.level.block.SlabBlock
```

Independent dry hall validation can proceed. Center the first assembly's known
ring/spoke geometry at(208,384), low feet Y30 and threshold feet Y32. Predeclare
all four bidirectional spokes and the24-block inner ring using the same adult
and no-remedy assumptions. This checks the actual second saved blocks rather
than transferring a template-level conclusion. Then test the northern centerline
from threshold(208,32,376) to(208,32,370), the southern approach to the four-source
chamber. Save failures unchanged and do not assume that the entire chamber or
its rewards are reachable until their own paths and rays pass.

The initial hall and northern approach pass. Before extending that result,
predeclare the chamber survey: from(208,32,376), follow the six-block centerline
to(208,32,370), circle its radius-three square once, and return by the approach.
Check both directions of the ring and one supported access ray to each of its
four saved chests, without exposing their buried spawners. Also validate four
hall chest rays from the radius-three hall stations. Both rooms use the existing
ray check, now shared between two current assembly consumers without changed
rules. These are access-to-assignment claims, not acquired loot or combat success.

Both declared native rooms pass. The ordinary hall has one connected low floor
with four radial transitions spanning feet Y30..32; each five-horizontal-block
spoke has two blocks of elevation change. Its four unrolled chests have clear
lids and supported rays from the ring, and a gold block remains at(208,30,384).
The chamber has one connected floor at Y32, a24-block radius-three circuit and
a six-block approach from the northern hall threshold. Its closed survey totals
36 horizontal blocks and zero vertical. All four chamber chest lids and rays
pass. These are two activity spaces, not eight reward rooms. Neither is empty
under the protocol's potential-content definition, but actual contents and
encounters remain NOT MEASURED.

The nearby chamber's four sources are still buried at Y31 beneath their chests;
none was removed by this native survey. The hall's gold is a physical potential
reward, not acquired material. Do not treat successful chest rays as proof that
combat can be avoided, that the loot is useful, or that acquisition succeeded.
Source access/removal, enemy scenario, other rooms and a joined complete task
remain required. The ordinary assembly's four towers prevent simply copying the
first assembly's complete timing or final-room assessment.

For the shaft, pinned `FlowingFluid.getHeight` returns one when the same fluid is
above, otherwise `getOwnHeight`, which is amount/9. `WaterFluid$Source.getAmount`
returns8. Air is saved immediately above each spiral slab. Thus source water
height is nominally8/9 of its block, above the slab's .5 support plane by7/18
blocks (about.389). This source-derived contact makes dry support-height timing
inappropriate; it does not establish a native ascent rate, drowning outcome,
fluid stability or successful player movement. The exact fluid/transition model
is still unresolved, rather than being folded into the first assembly's j value.

Reproduce this additional source derivation with the same pinned `javap -c -p`
command and classes `net.minecraft.world.level.material.FlowingFluid` and
`'net.minecraft.world.level.material.WaterFluid$Source'` (quote the latter in a
shell to preserve its dollar sign). The local executable retains all17 slab
coordinates, their states and the explicit dry-model rejection. Geometry for
fractional slab support and wet movement must be resolved before a dependent
shaft task is accepted; no new world generation is needed to locate the issue.

Run `uv run python -m evidence.item-13.temple_ordinary_route` to reproduce the
initial room paths, eight rays, shaft inventory and negative case. Focused
formatting, lint and type checks pass. The first assembly's route output is
byte-identical after sharing its ray function and its full check passes. Only
existing rules were moved; a lint directive for their existing4.5-block reach
constant was retained. This milestone advances the second assembly but does not
close its full topology, gameplay-quality model or family coverage gate.

### Predeclared wet-slab collision check

Resolve the shaft's fractional support geometry separately from movement timing.
Reuse the shared checker with an explicit set containing only its17 already
verified waterlogged bottom slabs. For those cells only, use the pinned half-block
collision box and support at Y+.5. Keep fluid contact separate from collision;
this option does not declare the slabs dry. Other unrecognized slab cells still
fail. Validate the17 centered support stations in their ascending order and its
reverse, with the existing conservative one-block transition envelope. Report
16 horizontal and16 vertical transitions only if those checks pass; do not
include the unvalidated upper/lower access connections or infer a whole-shaft
traversal time. The existing dry integer-height rejection must still pass.

The explicit fractional-support check passes for all17 stations in both
orders:16 horizontal and16 vertical blocks from lowest to highest station.
The checks preserve center-post clearance and the conservative higher-endpoint
jump envelope. The default dry checker still rejects fractional slab standing,
and the original integer-height rejection remains. This proves collision and
support geometry under the stated shapes, not a timed player traversal or stable
fluid field. No slab or other saved block was changed.

Pinned `Entity.getFluidJumpThreshold` returns .4 for the declared adult eye
height. `LivingEntity.aiStep` permits `jumpFromGround` when grounded and water
contact is at or below that threshold, subject to its jump delay. The previously
derived nominal7/18-block contact is below .4. This distinguishes the saved
ankle-depth state from an automatically assumed deep-swimming jump. The default
`Attributes.JUMP_STRENGTH` is .41999998688697815; the jump-power method also
applies block jump factor and jump effects, which must remain their nominal
values for any derived case. These facts do not prove that contact remains
shallow during a lateral transfer toward the next, higher waterlogged slab.

For an isolated vertical launch over its original slab, declare no sprint,
effects, incoming velocity, lateral movement, horizontal collision, fluid push
or source change; jump factor one and gravity .08. The first move uses nominal
jump velocity. While in water, the inspected `travel` branch multiplies vertical
velocity by .800000011920929 and `getFluidFallingAdjustedMovement` subtracts
gravity/16 for this upward, non-sprinting case. Once above that slab's8/9 water
height, ordinary vertical drag is .9800000190734863 after subtracting gravity.
The following direct derivation only tests available vertical rise, not an
entire jump trajectory between slabs, and is not a traversal-time result:

```sh
uv run python - <<'PY'
y = 0.0
velocity = .41999998688697815
for tick in range(1, 10):
    wet = y < 8/9 - .5
    y += velocity
    print(tick, round(y, 9), wet)
    velocity = (velocity * .800000011920929 - .08/16
                if wet else (velocity - .08) * .9800000190734863)
PY
```

This restricted recurrence rises above one block at tick4 and peaks at about
1.241635 blocks at tick6. It is insufficient to validate lateral transfer:
water in the next slab's cell can be encountered before landing and alter the
recurrence. Preserve that boundary instead of declaring a complete wet jump
from a one-dimensional calculation. Reproduce the supporting source with the
same pinned `javap -c -p` command for `net.minecraft.world.entity.Entity`,
`net.minecraft.world.entity.LivingEntity` and
`net.minecraft.world.entity.ai.attributes.Attributes`.

The top slab supports feet Y24.5. The outer ledge above the shaft has feet Y26,
a1.5-block difference, so a direct ordinary one-block step is not established.
The central wall post and the upper opening may supply another route, but that
route has not yet been validated. Bottom access, upper access and lateral wet
transitions are the precise remaining claims before whole-shaft timing. The
full generated block evidence is available; this is a modeling/access gap,
not missing-world evidence or permission to regenerate the accepted world.

## Bounded native wet-step pilot, predeclared before execution

The existing collision and template-placement probes cannot execute actor
movement. Further handwritten fluid recurrences would duplicate runtime behavior
without resolving lateral contact. Add one narrowly scoped FakePlayer motion
probe to the existing fresh-runtime lifecycle instead. This directly addresses
the Item13 playable-transition requirement; it does not introduce a new review
framework, general navigation system or gameplay benchmark. The probe is
`Item13ShaftMotionProbe.java`; runner mode is `collision.run --shaft-motion`.

Actor: one unregistered NeoForge FakePlayer with standing adult .6-by-1.8 body,
no active effects or flight capability, no sprinting, no equipment use, no
passengers and zero initial velocity. Check effective movement speed .1, jump
strength .41999998688697815, gravity .08, water efficiency0 and step height .6.
FakePlayer invulnerability and inactive connection/normal player tick behavior
make this unsuitable for damage, survival, combat or human-time claims. The
actor is never added to a player list or saved; its ephemeral identifier is
neither emitted nor retained. This is a controlled native physics query.

Input: a fresh hash-verified copy of accepted ordinary r1 using the existing
POSIX-locked copy/verification procedure and frozen runtime/configuration.
Load its already verified full chunk(12,21), which contains the pilot, and compare
all175 saved cells X194..198,Y7..13,Z340..344 to the committed ordinary extract
before stepping. Reject any mismatch, unexpected dimensions/attributes/effects,
flight capability or another entity in X193..200,Y7..14,Z339..346. Do not repair
or reset changed cells to make the pilot pass.

Start actor center(195.5,8.5,342.5), on its verified lower slab, with on-ground
flag set and zero velocity. Target center(195.5,9.5,341.5), the next higher slab.
The controller knows both positions. Each native step runs baseTick, aims yaw
at the target with pitch zero, applies forward input1 when horizontal distance
exceeds .05 (otherwise0), no strafe, and holds jumping while feet are below9.4.
Then it runs aiStep. No teleport, direct velocity change, block change, source
removal, flight or manual movement correction is allowed after initialization.

Success requires a later on-ground state with feet within1e-5 of Y9.5 and
horizontal center distance at most .15 from the target, within120 native steps.
Record every position, velocity, on-ground and in-water flag from step0 onward.
Reject timeout or departure below Y7.5 or more than three horizontal blocks from
target. Preserve the attempt and do not expand to other transitions until this
representative is interpreted end to end. A failed attempt identifies this
controller/case's failure; it does not prove no player can traverse the shaft.

All steps execute inside one server-thread query. World/fluid/entity ticks do
not advance independently during that query. Thus step count is a native
manually stepped observation under stationary world state, not elapsed server
gameplay time, a human observation, or proof that fluids remain stable in play.
This deliberate boundary isolates the missing collision/fluid movement behavior.
A success can support only the tested local transition and equivalent states,
not upper access, the complete shaft or the full dungeon. Native physics output
must remain separate from the approved conditional expedition budgets.

Resource declaration: one fresh materialization, one attempt,120 steps maximum;
existing600-second lifecycle bound,30 seconds for chunk loading and30 seconds
for the server-thread query,45 seconds per build command, clean save/stop under
the existing lifecycle. The accepted world is503 files totaling428,092,106 bytes.
Allow2 GiB for the copied world/runtime and100 MiB for probe/log/config output,
with the existing5-GiB free-space floor. Current free space before preparation
is30,350,680,064 bytes. No new generation or frozen tuning is requested.

Command (execution pending at producer commit):

```sh
uv run python -m evidence.item-13.collision.run --shaft-motion evidence/raw/item13/shaft-motion-r1 instances/item13-shaft-motion-r1
```

Compilation succeeds with pinned javac, explicit classpath, `-Xlint:all -Werror`.
The first compile without an explicit classpath failed on an inherited invalid
classpath entry; it ran no experiment. The existing runner already supplies an
explicit classpath, so no host environment change was required. Python runner
formatting, lint and type checks pass. Runtime acceptance remains unproven until
the actual trace, lifecycle and configuration checks have completed.

## Native wet-step pilot result

AUTOMATED RUNTIME OBSERVATION under the predeclared manually stepped method:
one attempted transition, one successful target landing. The actor reached
(195.5,9.5,341.51765179554803), on ground and in water, at native step20. The
horizontal target error is about.017652 blocks, inside the .15 criterion.
There are21 retained states including initialization. This resolves the tested
lateral wet transition; it does not establish the other15 rising links, descent,
upper/lower access, ordinary world-tick behavior or an observed gameplay time.

The trace shows feet Y8.92 after step1,9.496979981 after step3 and a peak near
9.74064758 at step5. Wet contact reappears at step6 while the actor moves toward
the higher slab, and persists through landing. This confirms why the earlier
isolated vertical recurrence could not determine lateral landing behavior.
The result is20 native physics steps, not an asserted one-second player task:
the loop omitted independent world ticks, connected-client input and normal
full player tick processing. No combat, health, loot or replay outcome was tested.

The175-cell loaded-state comparison passed. Dimensions were approximately
.600000024 by1.799999952, within the declared tolerance. Effective movement
speed .10000000149, jump .41999998688697815, gravity .08, water efficiency0 and
step height .6 matched the pilot. No other entity occupied the checked scope.
These are pilot conditions, not a baseline dungeon enemy census. The actor was
unregistered, its ephemeral identity was not retained, and cleanup completed.

[Native trace](../shaft-motion/r1-shaft-motion.json.gz):1,670 compressed bytes,
SHA-25630843845c50d094a45e55249437b19a756f55528e01cc3e6d0077440a6b4ac29.
[Capture/lifecycle](../shaft-motion/r1-capture.json.gz) records launch revision
d11e4a535d628575d985d648d1c0c186b8d3b7bb and probe JAR SHA-256
28d61e20f856d36f267fb14a6a9828d4e462b950031d931530e318c2a6113b60.
The projection's uncompressed SHA-256 is
88239cebba7a2034ac38642efd4d4c4d90599cd677780e06f73a1800fe7c9978.
Gson omits null fields in the native projection; successful acceptance is also
proved by the final state's declared predicate and the capture's null rejection
reason, not by assuming a missing field implies success.

Preflight verified136 retained candidates, runtime4062d6179218916c703269f113663b1e078adebbf6d43a691e692d972e07ac50,
and frozen configuration2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f.
The ordinary accepted source archive/backup identities are bound in the capture.
Readiness, correlated save-all flush, clean stop and exit0 passed; the process
group was not killed. All228 configuration files passed with only the existing
four permitted comment-only normalizations. Total lifecycle elapsed155.903 seconds.
The experimental instance used1,103,541,505 bytes and raw output5,883,695 bytes,
inside the declared2-GiB/100-MiB budgets. No server remains active.

The existing retention tool now accepts this capture mode:
`uv run python -m evidence.item-13.collision.retain --shaft-attempt 1`.
Its [retention record](../shaft-motion/r1-retention.json) binds all five original
and compressed projection/log files, with only the existing console bind-address
redaction. [Raw custody](../shaft-motion/custody/README.md) retains all240 files
and verifies local and externally downloaded restores against the exact launch
tag. This completes this pilot's evidence delivery, not the family or Item13 gate.

Next use the successful representative to resolve the remaining wet transitions
and shaft access under a predeclared expanded case. Any additional runtime
experiment must use another fresh hash-verified materialization. Do not reuse
this stopped instance, extrapolate20 steps across every link without evidence,
or call a partial slab route a complete dungeon expedition.

## Continuous native shaft case, predeclared before expansion

The one-step pilot is accepted and durably delivered. Extend the same probe to
one continuous ascent and return, with a new fresh verified materialization.
No actor reset, teleport, block edit or velocity correction is allowed between
waypoints. This addresses the remaining16-slab sequence and the actual upper
and lower access requirements; it does not claim the parent dungeon complete.

Start at center(195.5,8,343.5), supported by saved stone brick Y7. Visit the17 slab
centers in ascending Y8.5..24.5 order, then central post center(196.5,25.5,342.5),
then western outer ledge center(194.5,26,342.5). Return via the post, all17 slab
centers in reverse order, and the initial bottom stance. This is38 target
landings. Saved top post is a mossy stone-brick wall with UP true and no arms;
its native collision, not a full-cube approximation, determines the landing.
The block at(196,28,342) is a hanging waterlogged lantern, not a solid ceiling
cube. Native collision will decide the upper crossing.

Permit the ordinary crouching capability only for the upper post/ledge excursion,
from the first post target through the return onto the highest slab. Apply
shift state and the native CROUCHING pose; require height1.5. Restore STANDING
height1.8 for the next lower slab. Reject a pose if its resulting bounding box
collides with the world. No size other than these ordinary player poses is allowed.
Each change is retained in the trace; it is a controlled pose input, not an
unrecorded collision override. Use forward input .3 while crouching, rather than
full-speed input through a shorter body. The pilot's dimensions remain the initial state.

Reuse the target-aware yaw, forward/stop and upward jump controller. For the
west-ledge-to-post return only, hold jump while crossing the two-block horizontal
gap even though the target is .5 lower. Other descending transitions do not
request jumps. Success at each target uses the pilot's on-ground,1e-5 vertical
and .15 horizontal tolerances. Preserve momentum between targets. Stop on the
first target that cannot be reached within120 native steps, on departure below
Y7.5 or above Y27.5, or more than three horizontal blocks from the active target.
Retain all completed targets and the first failure; do not reset and continue.

Compare all1,664 loaded cells X193..200,Y6..31,Z339..346 with the same committed
ordinary extract before movement. Require zero other entities in the corresponding
scope. All cells lie in accepted full chunk(12,21). Preserve the same stationary-
world/native-step limitation, actor attributes, no effects/flight/sprinting and
no combat or inventory claim. Do not extrapolate the first pilot's20 steps.

Budget: one fresh world/runtime, one continuous case,38 targets with at most120
native steps each (4,560 total),30-second server-thread query and the existing
600-second lifecycle/30-second chunk-loading bounds. Reuse2-GiB instance,
100-MiB raw-output and5-GiB free-space limits. The observed first launch used
1.104 GB and155.903 seconds, supporting these bounds without assuming a result.
The full case must finish clean save/stop and configuration verification, and
retain failures and raw custody before acceptance.

Command, after committing the producer and with absent targets:

```sh
uv run python -m evidence.item-13.collision.run --shaft-motion-full evidence/raw/item13/shaft-motion-r2 instances/item13-shaft-motion-r2
```

## Continuous shaft r2 outcome: rejected and preserved

The predeclared command ran from producer
`2bdf8c7f3c0497033763a262a3731ce24ef18e82` on a fresh hash-verified ordinary r1
materialization. All 1,664 input cells matched and the scoped entity count was zero.
The [raw projection](../shaft-motion/r2-shaft-motion-full.json.gz) records 442 states
(step0 through441), 18 reached landings out of38 planned, and the exact rejection:
`No landing at target 18 within 120 native steps`.

In this rejected attempt, the actor reached all17 wet slab centers without a reset,
landing on the highest at step295, then the central post at step321. It failed on
the first outer-ledge target, index18. The last position was
(195.30000001192093,25.305512513420364,342.6527891949283), airborne, dry and crouching.
During this target its X coordinate never went below195.30000001192093; the target
center was194.5. These partial diagnostic observations do not pass the full-case
acceptance gate. The return sequence was not attempted. No completed ascent/return
time can be assigned, and multiplying the one-step pilot across this route would
conceal the observed failure. Failure of this controller does not prove that no
player route exists.

The [capture](../shaft-motion/r2-capture.json.gz) records readiness but no correlated
save-all flush or clean stop. The agent exception propagated through attach, and
the existing lifecycle killed the complete process group, returning -9. Elapsed
lifecycle time was222.478 seconds. No post-run configuration audit was reached.
No matching Java process remained at the recovery check. Consequently this is a
preserved rejected experiment, not an accepted runtime result or accepted world.
The unchanged input world remains under its original custody.

The [retention record](../shaft-motion/r2-retention.json) binds all five original
and compressed projection/log files. [External custody](../shaft-motion/r2-custody/README.md)
retains all11 available raw files, with verified local and downloaded restores.
Reproduction of the committed projection uses
`uv run python -m evidence.item-13.collision.retain --shaft-attempt 2` with absent
output files. Raw output totaled5,581,901 bytes, within100 MiB.

Disposition: preserve the native ledge failure and stop controller tuning. The
second assembly still needs a complete supported route and conditional task.
Use the existing explicit construction model to inspect the smallest earned
shaft-access remedy, including placement/removal and interaction costs, before
considering any further fresh runtime experiment. Neither a static remedy nor the
partial native trace establishes human traversal time or a realized encounter.

## Second shaft construction alternative: solid geometry and costs

The rejected native ledge crossing is not repeated. Inspection of the same
hash-bound ordinary extract finds an alternative column at X195,Z343, with a full
stone-brick floor at Y7. Y8..28 contains air except waterlogged bottom deepslate-
brick slabs at Y15 and23. The upper western landing(194,26,343) has full stone-brick
support at Y25 and air at Y26/27. This is an explicit earned construction option,
not an invisible bypass or an assertion that the authored wet spiral is unusable.

Use the existing scaffolding capability and carried diamond pickaxe. Begin at
lower adjacent stance(194.5,8,343.5), build five supported scaffold cells Y8..12,
and climb to feet13. Remove the slab at(195,15,343) from eye(195.5,14.62,343.5).
Move north0.7 blocks to Z342.8 while retaining0.1 block of body overlap with the
scaffold top. Click its north side near Y12.95 to extend the column eight times,
through Y20. Return0.7 blocks south, climb to feet21, and remove(195,23,343) from
eyeY22.62. Repeat the north side-click adjustment and add five cells Y21..25.
Return to center, climb to feet26 and step west onto the supported upper landing.
Return along the same constructed column to the initial adjacent lower stance.
Leave the construction in place; no recovery or acquisition of removed slabs is
required by this connection demonstration.

The [existing route check](../temple_ordinary_route.py) now verifies the 18-block
column, both horizontal transfers, both overhead removal rays, the base side-click
ray and both elevated side-click rays/offset envelopes. It rejects the same route
when either named slab remains. Reuse the pinned side-click-UP, distance-zero
support and scaffold-top derivation from the [Nether Tower](mns-nether_tower-report.md#elevated-chest-explicit-scaffold-connection).
The two elevated offsets add2.8 horizontal blocks. Including two one-block
transfers in each direction, this local out-and-back has6.8 horizontal and36
vertical blocks, 18 placement interactions and two removal interactions. It
requires five equipment selections: scaffold, pickaxe, scaffold, pickaxe,
scaffold. These are local work counts, not the complete dungeon task.

**Fluid limitation remains material.** The solid-clearance model omits the removed
slabs as collision obstacles, but it does not declare their cells dry or simulate
released water. Pinned `ScaffoldingBlock.getStateForPlacement` offsets21..49 set
WATERLOGGED from the destination fluid; `getFluidState` offsets0..23 returns source
water when that property is true. Scaffolding is therefore not a demonstrated
water seal. The surrounding saved water and the two broken waterlogged slabs can
change immersion, support state, drift and breathing during construction. No
post-edit fluid evolution has been measured. The source's water travel branch
also differs from dry climbing: `LivingEntity.travel` offsets219..270 applies its
climbable vertical value only with horizontal collision, then water drag. Do not
silently reuse a dry scaffold speed or assert that these rays prove wet placement.

Mining work is separately supported. `Blocks` copies deepslate-brick slab
properties from deepslate bricks at39970..39989, and those from cobbled deepslate
at39927..39952. Cobbled deepslate strength is3.5 at39667..39673. The existing diamond
speed8 and correct-tool divisor30 apply without effects. `Player.getDestroySpeed`
offsets140..163 multiply speed by SUBMERGED_MINING_SPEED when eyes are in water;
`Attributes` sets its default0.2 at779..799. The additional airborne divisor5 is
at165..176. Binary32 progress accumulation gives the following conditional work:

| State held throughout both removals | Ticks per slab | Two-slab active work |
| --- | ---: | ---: |
| Grounded, eyes dry | 14 | 1.4 seconds |
| Grounded, eyes submerged | 66 | 6.6 seconds |
| Airborne, eyes submerged | 329 | 32.9 seconds |

These are discrete held-state mechanism cases at20 TPS, not probabilities,
observed mining times, bounds on interrupted work or a claim that breathing and
support permit each case. Acquisition, targeting and equipment changes are not
included in active breaking work. Movement, breathing/recovery and interruption
costs must be resolved before this connection supplies a complete timing term.
This is a compact solid-geometry alternative with explicit known costs, not an
accepted completed shaft experiment or a completed second-assembly assessment.
No new world, runtime framework or common geometry exception was introduced.

Reproduce the direct source inspection using the pinned Java binary and SRG JAR
identified earlier in this report; `javap -c -p` on `ScaffoldingBlock`, `Blocks`,
`LivingEntity`, `Player` and `Attributes` gives the offsets above. Geometry:
`uv run python -m evidence.item-13.temple_ordinary_route`. Mining arithmetic:

```sh
uv run python - <<'MINING'
import struct
for label, speed in [('dry grounded',8), ('submerged grounded',1.6),
                     ('submerged airborne',.32)]:
    f = lambda x: struct.unpack('f',struct.pack('f',x))[0]
    progress = f(f(f(speed)/f(3.5))/f(30))
    total = 0
    ticks = 0
    while total < 1:
        total = f(total + progress)
        ticks += 1
    print(label, ticks, 2*ticks/20)
MINING
```

## Second assembly: upper shaft connection and exposed southern gap

The same existing route check now connects the shaft's upper landing to the main
hall's north threshold using saved solid support and adult clearance in both
directions. From(194,26,343), move south to Z344, east to X196, then south to Z357.
Feet remain26 through Z348 and rise one per block at Z349..354, reaching32. Continue
south at X196 to Z367, east to X205, south to Z370, east to X208 and south to the
already inspected hall threshold(208,32,376). This is47 horizontal and six ascending
blocks one way, or94 horizontal and12 vertical blocks for a return. No mining,
placement, fractional-floor exception or wet cell is used on this saved route.
It is one verified route, not a shortest-path claim. The wet shaft below its upper
landing remains separate and unresolved as recorded above.

This integration prevents an incorrect graph edge inferred from nearby pieces.
A proposed straight southern link at X196,feet32 from Z374 toward Z384 fails first
at Z378: its supporting cell(196,31,378) is source water. All twelve inspected
centerline cells X196,Y31..34,Z378..380 are source water. Immediately north,
X196,Z377 has a full masonry floorY31 and airY32..34. Immediately south, X196,Z381
has stone bricksY32/34 and chiseled stone bricksY33. Thus this centerline is a
three-block external water gap followed by a solid wall, not a dry corridor
between the nearby three-way pieces. The negative check retains the exact failed
support state; the accepted route instead uses the chamber connection.

The open air-to-water boundary at Z377/378 is direct saved-block evidence of an
external fluid-access vulnerability on this northern branch. It supports a
potential flooding/immersion concern and a possible external approach requiring
wet movement; it does not establish realized flooding, safe swimming, a complete
external entry route or a breach-free connection through the southern wall.
Do not infer the cause from a missing template name or piece adjacency alone.
The positive clearance statement is about saved geometry. Post-load fluid
stability is not measured by these static checks and remains explicit uncertainty.

Reproduce with `uv run python -m evidence.item-13.temple_ordinary_route`.
All existing hall/chamber checks, the shaft construction checks and both added
positive/negative connections pass; focused Ruff and type checks pass. No new raw
read, experiment or geometry machinery is required for this integration.

## Second chamber: task declaration before timing integration

Use the established actor/equipment and complete-task accounting to clear only
the four-source chamber, beginning and ending at the main hall north threshold
(208.5,32,376.5). Traverse its outer floor circuit, expose and disable all four
sources from intact adjacent floor stations, defeat the stipulated occupants,
conditionally acquire all four chest contents, and return alive. Keep full layout
knowledge. Do not mine chests, step into source holes, restore floors, swim, heal,
use effects or collect the removed floor/spawner blocks. Any fluid arrival at the
actor, loss of supported footing, extra enemies or failed acquisition censors
this dry chamber case. This is a local task, not the complete temple clear.

Predeclare a six-per-source exact-class suppression case as in the first temple's
P6: six ordinary witches, six spiders, six skeletons and six zombies. Each source
must continue to see at least six members of its matching class within its own
nearby-entity query until disabled; keep them alive until all four sources are
removed. These are stipulated initial conditions, not a placement or success
probability. Natural spawning, extra waves, equipment, passengers, potion/status
changes and healing are excluded. A composition or suppression failure invalidates
the case. Do not describe four saved Delay0 sources as exactly24 realized enemies.

Use two visits to the same supported outer circuit: first to remove four adjacent
floor blocks and four spawners, then, after combat, to acquire the four rewards.
Combat contact-duty includes pursuit and return to the circuit start. Geometry
must verify each source and chest ray and every post-removal floor station.
Acquisition remains conditional on the existing per-container allowance, inventory
capacity and successful menu transfer. No pickup route is inferred from ray reach.
Navigation cost is one event at each circuit direction change, plus initial
orientation, four source selections, combat transition, four reward selections
and the exit choice. Actual mining, eight removal aims, four chest interactions,
three equipment selections (pickaxe, sword, empty hand), four acquisition events
and final verification are separate. Use the accepted A/B/C allowances and duty
fractions. Determine the resulting route/event counts in the existing script;
do not omit the second circuit or call movement alone complete-task timing.

## Second chamber: integrated local result

The declared post-removal route passes. Its32-block outer ring has corners
(204,32,363),(212,32,363),(212,32,371),(204,32,371), starting at(208,32,371).
Four one-block side excursions and returns make each work circuit40 horizontal
blocks. The five-block hall approach, two circuits and five-block exit total90
horizontal blocks with no vertical movement. The source exposure sequence is:

| Source type | Intact feet station | Removed adjacent floor | Source below chest |
| --- | --- | --- | --- |
| Skeleton | (207,32,370) | (208,31,370) | (208,31,369) |
| Witch | (205,32,366) | (205,31,367) | (206,31,367) |
| Spider | (207,32,364) | (208,31,364) | (208,31,365) |
| Zombie | (211,32,366) | (211,31,367) | (210,31,367) |

Each source is inspected from eyeY33.62 through its own adjacent floor opening;
no descent into an opening is required. The same intact station supplies the chest
ray after source removal. All four lids have air directly above, all four saved
containers have the `dungeon` loot table and no Items or Lock. This is conditional
opening/transfer access, not rolled or acquired loot. Water is saved immediately
below each removed adjacent floor at Y30. Eight holes remain after four floor and
four source removals; the route avoids them. Negative checks reject standing over
all four removed exposure floors. Hostile displacement into a hole remains a
meaningful conditional hazard, not an observed fall or combat exploit.

All four bound source payloads have Delay0, SpawnCount4, MaxNearbyEntities6,
SpawnRange4, RequiredPlayerRange16, delay range200..800 and empty SpawnPotentials,
with the four explicit types above. Their potential is four source nodes and four
authored enemy types. The stipulated workload is24 enemies under the exact-class
suppression conditions, not an estimate of the saved world's realized population.

Reuse the first temple's pinned nominal weapon/health calculations: per unmodified
enemy, witch five hits, spider three, skeleton four and zombie four (including
ordinary zombie armor). Six of each gives96 hits. At13 ticks per full nominal
sword interval this is1,248 ticks or62.4 active seconds; duty1/.75/.5 gives62.4/83.2/
124.8 seconds. Witch healing or potion/status changes invalidate this simplified
case rather than silently increasing its health budget. No survival probability
or realized combat time is asserted.

Four masonry exposures use six active mining ticks each and four spawners use19
each with the existing grounded dry diamond-pick model:100 ticks, five seconds.
The complete route has34 direction changes; adding the11 predeclared task choices
gives45 navigation events. Complete conditional local seconds are:

`T = 90/u + 5 + 45n + 12a + 3s + 4k + v + 62.4/d`.

| Approved sensitivity profile | Noncombat budget | Combat budget | Complete local task |
| --- | ---: | ---: | ---: |
| A | 55.25 s | 62.4 s | 117.65 s |
| B | 92 s | 83.2 s | 175.2 s |
| C | 141.5 s | 124.8 s | 266.3 s |

Approximately118/175/266 seconds are conditional modeled chamber tasks, not
observed timings, typical clears, calibrated skill bands or guaranteed bounds.
They include both source and reward circuits and all declared actions. The entire
temple timing must integrate this work with its other routes and encounters;
do not simply add overlapping local surveys or call this a whole-family result.

The verified ring and four work stations occupy one continuous activity space,
not four rooms for four sources. The inspected activity core X204..212,Z363..371
contains all four source/reward pairs within this chamber's enclosing architecture.
It has no demonstrated additional occupied floor; source holes do not become
rooms or vertical progression. Under the protocol's potential-content definition,
this local space is neither empty nor dead (0/1 each). These are content-assessment
denominators, not player occupancy or engagement statistics.

The chamber concentrates four hostile mechanisms with four rewards, but no
explicit authored final-objective marker was identified. Its `dungeon` table is
already proved byte-identical to `large_room` in the first assembly's source
assessment, so it does not establish a higher reward tier than the hall. The
source/loot pairing is a supported challenge/reward arrangement; unique finale
quality and player satisfaction are not inferred. Expected revisit contribution
is conditional: source removal and the eight holes persist as physical changes;
personal loot access alone does not reset them or reproduce this first-clear
scenario. No observed replay outcome is claimed.

Reproduce the route, source/loot identities, failure guards, event counts and all
three totals with `uv run python -m evidence.item-13.temple_ordinary_route`.
Focused Ruff, formatting and type checks pass. This resolves the chamber's local
conditional access/task integration; the second assembly and Item13 remain
IN PROGRESS.

## Second assembly reward alcoves: declared local tasks

Extend the existing saved-route checks to the north chamber alcove and the south
branch off the western hall junction. Start respectively at(208.5,32,363.5) and
(200.5,32,384.5), visit the assigned chest, conditionally acquire its contents and
return alive to the same station. Reuse the actor, layout knowledge and A/B/C
allowances. These local tasks occur after the chamber encounter is cleared; no
pre-existing or natural enemies enter their scope. Unexpected combat, fluid arrival,
failed opening/transfer or lost support censors the stated case. No mining, new
placement, campfire lighting or removed-block pickup is permitted or required.

Budget actual supported out-and-back movement, one navigation event per direction
change plus initial orientation, target selection and exit choice, one chest
interaction, one empty-hand selection, one acquisition and final verification.
Determine lengths and totals from the explicit paths below. Treat these as local
conditional noncombat tasks, not a guarantee of peaceful first entry or a complete
assembly time. Their start points deliberately exclude prior hall/chamber travel.

## Second assembly reward alcoves: integrated result and material difference

Both local tasks pass the existing post-chamber floor and interaction checks:

| Local space | Supported center route | Reward | Out-and-back | A/B/C complete conditional seconds |
| --- | --- | --- | ---: | --- |
| North chamber alcove | X208,feet32,Z363..355 | (210,32,355) | 16H,0V | 8.7 / 15 / 25.33 |
| Western junction south alcove | (200,32,384) west to X196, south to Z391 | (194,32,391) | 22H,0V | 10.9 / 18.5 / 30.33 |

The north route has four navigation events under the declaration; the bent
western route has six. For either, `T=H/u+N*n+a+s+k+v`. Combat is zero only in the
stipulated post-clear, no-additional-enemy case. Saved/realized human time, chest
opening and acquired loot remain NOT MEASURED.

Both chest assignments are unrolled `dead_end` tables, with no Items or Lock.
Their above blocks are straight top-half stone-brick stairs, waterlogged true,
facing east above the north chest and west above the western chest. Reuse the
first assembly's exact ChestBlock/legacy-stair conductor derivation: a non-full
straight stair does not block this source opening predicate. Waterlogging does
not turn that collision shape into a full conducting cube. Both rays use the
actual chest side inset and pass; no lid removal or extra mining is charged.
Entity blockers and actual transfer remain conditions, not inferred observations.

The north alcove lies within X206..210,Z353..358 and the western one within
X194..198,Z388..393, each with its validated floor at feet32. Each is one bounded
reward activity space under the primary partition, or part of its approach under
the stricter corridor/alcove merge. For this two-space partition neither is empty
or dead (0/2 each), because each has an accessible assigned reward. This does not
count template labels as rooms or imply the whole assembly has only two rooms.
No distinctive terminal encounter, higher-tier reward or final-objective marker
is established in either alcove; expected revisit value is limited to whatever
unmeasured repeat loot access remains, rather than a claimed player outcome.

A material saved-state difference is now resolved across the entire second
sample: all nine campfire block entities map to `lit=false,waterlogged=true`
blocks, including(207,32,355) and(197,32,391) beside these two alcoves. Therefore
there are zero lit campfires among nine saved campfires in this assembly.
Pinned `CampfireBlock.entityInside` offsets0..41 gates campfire damage on LIT,
so these states do not supply the first assembly's lit contact-fire mechanism.
The route avoids their blocks. Do not count nine raw campfire entities as nine
active hazards or automatically usable burning cooking stations. Future lighting,
fluid changes and runtime damage remain unmeasured. This difference reinforces
why the two retained material states are separate samples rather than duplicates.

Reproduce the source inspection with pinned `javap -c -p` on CampfireBlock and
all geometry, nine-state checks and arithmetic with
`uv run python -m evidence.item-13.temple_ordinary_route`. Focused lint, formatting
and type checks pass. This increment resolves two local rewards and the saved
campfire-state denominator, not remaining temple routes or Item13 completion.

## Western tower pair: upper reward access declaration

Inspect each retained tower at center Z367 and384 independently. Reuse the
existing upright actor, sword web removal, ordinary stone-button door operation
and source/geometry rules. From(196,32,Z), advance west to X192, shift north one
block, remove the web at(189,32,Z-1) from X190, and reach the outer button station
(188,32,Z-1). Operate its button, cross the iron door to X186 within its pulse,
and inspect the two upper chests via X185,Z-1..Z+1. Operate the inside button for
the return and follow the same route back. Exclude fluid arrival, hostile
interference, failed actuation/transfer and loss of support from this successful
component model. Do not remove other webs, bypass doors or silently inspect the
lower floors. Preserve the rejected straight centerline and the closed-door case.
This is the upper segment of two pending complete tower tasks, not two whole
assessments or a new independent timing protocol.

## Western tower pair: upper reward segment result

Both Z367 andZ384 cases independently pass the same coordinate-relative checks;
no result was accepted from template equality alone. Each direct centerline fails
at(191,32,Z), a saved cobweb. The accepted approach instead reaches X192, shifts
north to Z-1 and removes only(189,32,Z-1), from supported(190,32,Z-1). All other
webs remain. This is eight active sword-mining ticks per tower under the existing
dry grounded model, not time spent traversing webbing or an observed slowdown.

Each closed gate at(187,Y32..33,Z-1) is separately rejected. Both halves are
west-facing, left-hinged iron doors. The outer stone button is(188,34,Z-1),
east-facing, and the inner button(186,34,Z-1), west-facing; both are wall mounted
and saved unpowered. Exact side-face rays pass from the supported adjacent
stations. The source-open plate clearance permits the two-block crossing in
both directions. Reuse the established30-tick stone-button pulse: two blocks at
5/4/3 blocks per second require0.4/0.5/0.667 seconds, below1.5 seconds. Complete
aiming and orientation before pressing; do not put a post-click pause into this
window. Each return requires its own button operation. Actuation, uninterrupted
crossing and absence of hostile displacement remain modeled conditions.

Inside, X185,Z-1..Z+1 connects both chest stations. The four newly accessed
assignments are(184,32,365),(186,32,369),(184,32,382),(186,32,386). All have air
above, no saved Items or Lock, and the `quest_tower` table already inspected in
the first assembly. Their inset side rays pass. No new generated or acquired loot
is measured, and equal table IDs are not equal rolled contents.

Each upper return segment is28 horizontal blocks with zero elevation change,
one web removal, two button operations and two conditional chest accesses. These
are components for the full tower/assembly task, not a complete tower timing.
The upper reward activity space lies between the X183 and187 dividing walls,
with connected X185 floor and both rewards; the webbed entrance provides access
pressure rather than a separate spawner encounter. Do not infer overall tower
depth, finale quality or shallow height from this upper segment alone.

Direct inspection also identifies the next unresolved access boundary in each
western section: top-half waterlogged oak trapdoor(180,31,Z), saved closed and
facing east. Beneath it, feetY28 meets attached, armed, unpowered tripwire at
(180,28,Z), with masonry supportY27. This is a four-block drop target if opened,
not a validated descent or a confirmed live trap firing. Lower reward access,
trap mechanism, water effects and return ascent remain to be integrated before
the tower task is complete. The original accepted world is unchanged.

Reproduce the upper positive/negative routes, button/chest rays and counts with
`uv run python -m evidence.item-13.temple_ordinary_route`. The trapdoor/tripwire
states are direct queries of the same hash-bound extraction. Focused Ruff,
formatting and type checks pass. No new runtime or common geometry machinery was
added; Item13 remains IN PROGRESS.

## Western tower pair: middle-floor connection declaration

For each center Z367/384, extend the known upper reward route from(185,32,Z+1)
through the second ordinary timed door to(181,32,Z+1). Use its buttons from both
sides. Instead of opening the waterlogged trapdoor over the tripwire, remove the
single adjacent masonry floor(181,31,Z), make the controlled four-block descent
to(181,28,Z), and step south to(181,28,Z+1). Place four carried scaffolds at
X181,Z,Y28..31 on the saved masonry floorY27, using the established base-side-click
extension rule. Return through this column and the inner door. Keep the trapdoor
closed and all tripwire untouched. No runtime placement, trap firing or safe
landing is implied. Fluid arrival, damage requiring recovery, hostile displacement
or failed support/placement invalidates this successful connection case. Lower
reward routes and complete tower timing remain separate required work.

## Western tower pair: middle-floor connection result

Both retained cases pass independently. The inner iron doors at(183,Y32..33,Z+1)
are west-facing, right-hinged and saved closed. Each closed crossing is rejected;
the ordinary source-open plate geometry passes. Exact inside/outside wall-button
rays pass at X182/X184,Y34,Z+1. Use the same two-block/30-tick crossing condition
as the outer gate and a separate return press. The supported room link from
X185 to X181 at feet32,Z+1 is four horizontal blocks in each direction.

From(181.5,32,Z+1.5), the removal ray reaches the top of stone brick(181,31,Z).
Its declared removal leaves a full-height .6-wide column to feet28. All saved
Y28..30 cells at X181,Z are air, with full masonry supportY27: cracked stone
bricks in the northern tower, stone bricks in the southern. Both lower adjacent
stations at(181,28,Z+1) have supported forward/return access. Floor-placement
and repeated base-side-click rays pass from the adjacent lower station; the
four distance-zero scaffolds occupy Y28..31. Their column and upper/lower transfers
pass the existing clearance/support rules. No new scaffold or fluid shortcut was
added to the shared checker.

Per tower, this connection adds12 horizontal and eight vertical return-route
blocks, one masonry removal, four scaffold placements and two inner-button
operations. Six active dry grounded mining ticks apply to the masonry. Placement,
button aiming, decisions and selections still require their full-tower accounting;
these components are not a complete traversal time. The initial descent is a
four-block fall, not a scaffold descent before the scaffold exists. The existing
pinned nominal fall formula requests one damage for that stipulated distance on
ordinary masonry; live fall distance, health change and survival are not measured.

The route's column/body remains east of the original tripwire cell X180, with
minimum bodyX181.2; it does not enter that cell's contact volume. The trapdoor
remains closed and waterlogged, and the tripwire remains attached, armed and
unpowered in the saved evidence. This validates a local geometric avoidance,
not a runtime claim that the trap never fires or that neighboring water remains
stable. Fluid arrival, lost support or an unsafe landing still invalidates the
successful dry connection case. Neither input world nor raw block evidence was
mutated. Lower reward circulation and the subsequent descent still need their
own integration before a complete tower claim.

Reproduce both closed-door failures, open paths, removal/placement rays, column
support and retained trap states with
`uv run python -m evidence.item-13.temple_ordinary_route`. Focused Ruff, formatting
and type checks pass. The active handoff preserves the remaining lower-floor work.

## Western tower pair: middle reward and lower connection declaration

At each Z367/384, start from the verified lower adjacent stance(181,28,Z+1).
Expose a passage through the two masonry panel cells(185,Y28..29,Z), using the
pickaxe from X184. Retain the existing condition that the piston circuit does
not change during this modeled passage. Reach(190,28,Z-1) via X189,Z then X189,Z-1,
avoiding the central trapdoor floor at X190,Z, and access the chest at(190,28,Z-2).
This is a breach of the saved panel, not proof of a native gate solution.

For the next connection, remove floor(189,27,Z-1) from the chest station, descend
four blocks to(189,24,Z-1), step east to(190,24,Z-1), and build four scaffolds
Y24..27 at X189,Z-1 on the full stone-brick floorY23. Return through this column.
No web removal is needed within this alternative column. Keep both initial falls,
source water/actuation uncertainty, required survival and placement conditions;
no healing, swimming, trap activation or live pickup is assumed. Validate each
saved case separately and integrate counts as full-tower components, not totals.

## Western tower pair: middle rewards and lower connections integrated

Both middle centerline passages are rejected while their masonry panel remains.
From the supported X184,feet28 station, ordered rays reach both(185,28,Z) and
(185,29,Z). In the northern tower these are stone/chiseled stone bricks; in the
southern they are mossy/cracked stone bricks. All use the already established
masonry hardness model, six dry grounded pick ticks each. This costs two explicit
removals per tower rather than assuming a piece connection is traversable.

Six sticky pistons per tower are saved extended at X185,Y28..30,Z-3/Z+3, facing
south/north respectively. The accepted breached route is conditional on this
circuit state remaining unchanged. It is not a runtime test of piston timing,
redstone correctness or natural gate operation. Removing the panel demonstrates
a possible earned shortcut under the source/geometry model, not an indestructible
route or a guaranteed permanently open passage after later circuit updates.

The checked middle route runs from(181,28,Z+1) north to Z, east to X189, north to
Z-1, then east to X190. It returns over the same supported cells, totaling22
horizontal blocks with no vertical change. Both middle chest assignments at
(190,28,365) and(190,28,382) have air above, no saved Items or Lock, and the existing
`quest_tower` table. Their south inset-face rays pass from(190.5,28,Z-0.5).
These add two conditionally accessible assignments; generated contents and actual
opening/transfer remain NOT MEASURED. All three reward assignments in each of
these towers now have local access evidence, but the full tower task remains open.

From that middle station, floor-removal rays reach(189,27,Z-1). Both cells are
stone bricks. The alternative column has airY24..26 and full stone-brick support
atY23, avoiding the webbed neighboring descent column. The lower east station at
(190,24,Z-1), initial floor placement and repeated base side-clicks pass. Four
supported scaffold cellsY24..27 supply the modeled return, and the middle reward
route is checked again after the floor removal with this declared support.
The extra connection contributes four horizontal and eight vertical return-route
blocks, one six-tick masonry removal and four scaffold placements per tower.
Its initial four-block fall is retained separately from the later scaffold climb;
the same nominal one-damage/unknown-live-damage distinction applies.

Across the two successive constructed drops, these towers now have connected
modeled feet elevations32,28 and24. That is eight blocks of vertical progression
under the stated remedies, not a room count or full dungeon-depth result. The
lower exits, hazards and onward routes still need validation. Each descent keeps
fluid stability, survival and successful construction as explicit conditions;
no world or raw evidence was changed. Do not sum these local return circuits as
an optimized whole-temple clear or omit their interactions when integrating time.

Reproduce both panel failures, source-state checks, middle chest rays, post-removal
support and second shaft with `uv run python -m evidence.item-13.temple_ordinary_route`.
Focused Ruff, formatting and type checks pass. The original tower failures and
trapdoor/tripwire observations remain preserved above.
