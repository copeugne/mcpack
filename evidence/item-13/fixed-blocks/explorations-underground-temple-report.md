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
