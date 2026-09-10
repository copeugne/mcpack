# Adorabuild modular Nether fortress

Status: IN PROGRESS. Authoritative local Item13 family assessment. Do not confuse
this family with the separately assessed wart house or the courtyard family.

## Existing evidence and predeclaration

Family `adorabuild_structures:nether_fortress`, root
`adorabuild_structures:nether_fortress_large_1`, Nether. The existing
[coverage declaration](../coverage.md#adorabuild-variant-scope) requires two
procedural assemblies from distinct seed roles. The accepted candidate/start
records contain four complete padded cases: biome-diverse r1/r2 at(0,25), ordinary
r1/r2 at(-16,-7). All are SAVED with no incomplete required chunks. Their stored
piece envelopes are identical within each seed pair; this does not prove identical
blocks, loot or realized encounters. No repeated start audit or generation is needed.

Select by ascending SHA-256 of complete candidate ID, with lexical tie break,
requiring a different seed role for the second case. Execute the smaller selected
padded volume first. Do not choose by gameplay outcome. Two selected assemblies
collectively contain every one of the eight source templates; no single case
contains all eight. The fixed-layout selector's all-components-in-one-instance
condition is therefore inapplicable, not a reason to reject these valid procedural
samples or modify the fixed-layout selection contract. The direct selection below
uses the existing bound candidate/start records and hash rule, with no new selector
module or general sampling framework.

Smallest deliverable: two complete saved layouts, coordinate room/activity
boundaries and validated connectors, graph branching/depth and floor progression,
complete conditional traversal/combat tasks, source/encounter distinctions,
hazards/chokepoints, empty/dead denominators, loot/finale, engineering bypass/
external-access limits, and supported replay/large-but-shallow assessment. Apply
the Item13 room/hazard/dead/finale definitions before scoring. Template dimensions
or tower counts do not establish playable room count or depth.

Eight source templates are each5x23x5: bridge_1,dummy_bridge,stairs_1,tower_large_1,
tower_medium_1,tower_medium_2,tower_small_1,tower_small_2. Existing Item8 template
content reports no authored entities or spawner blocks in any of them. Loot-table
references occur in tower_medium_1 (one),tower_medium_2 (two),tower_small_2 (one),
all minecraft:chests/nether_bridge. These are authored references, not observed
container count, generated items or acquired loot. Check root spawn overrides and
actual saved blocks before attributing encounters or reward distribution.

Resource declaration:32,364 ordinary-case padded cells and54,694 biome-diverse
cells,87,058 total. Only the smaller selected case may be extracted before its
representative end-to-end assessment. Bound each read at120 seconds and20 MiB
compressed output, with5 GiB free floor. Reuse measure.extract, accepted archive/
backup binding, full restored inventory verification before/after and the POSIX
lock. No server is started or frozen configuration altered. Existing comparable
Basalt reads took5.53..10.15 seconds, but this is not an assumed execution time.
Retain missing-chunk, identity, geometry or budget failures instead of substituting
another case. Inspect the block sheet before declaring actor route/objectives and
complete-task budgets; no timing score is authorized by template counts alone.

## Selection and source integration

[Selection](../nether-fortress-selection.json) SHA-256
`b5719edf1aa40b47a57aac05cd99fd1a94562f55757f864ac8b31919b51b7142`
chooses ordinary r2 first, then biome-diverse r1. Reproduce from the committed
immutable inputs with the output absent:

```sh
uv run python - <<'PY'
import gzip,hashlib,json
from pathlib import Path
from tools.analyze_route_opportunities import read_bound
paths={'candidates':Path('evidence/item-13/candidates.json'),'assemblies':Path('evidence/item-13/start-inspection/summary.json'),'pool_traces':Path('evidence/item-8/sources/pool-traces-content.json.gz')}
raw={k:read_bound(p) for k,p in paths.items()}
root='adorabuild_structures:nether_fortress_large_1'
candidates={r['id']:r for r in json.loads(raw['candidates'])['candidates'] if r['root']==root}
groups=json.loads(raw['assemblies'])['family_root_dimension_candidates']
options=[r for key,rs in groups.items() if key.split('|')[1]==root for r in rs]
assert len(options)==4 and all(r['start_status']=='SAVED' and not r['incomplete_chunks'] for r in options)
chosen=[]
for r in sorted(options,key=lambda r:(hashlib.sha256(r['id'].encode()).hexdigest(),r['id'])):
    if r['seed_role'] not in {c['seed_role'] for c in chosen}:chosen.append(r)
    if len(chosen)==2:break
expected=set(json.loads(gzip.decompress(raw['pool_traces']))['structures'][root]['templates'])
assert len(chosen)==2 and set().union(*(set(r['named_components']) for r in chosen))==expected
selected=[{**candidates[r['id']],'named_components':r['named_components']} for r in chosen]
selected.sort(key=lambda r:(r['voxel_count'],r['id']))
plan={'scope':'Two distinct-seed procedural assemblies, collective eight-component coverage; smaller representative first','input_sha256':{k:hashlib.sha256(v).hexdigest() for k,v in raw.items()},'eligible_count':4,'selected':selected,'summary':{'samples':2,'families':1,'voxels_before_block_extraction':sum(r['voxel_count'] for r in selected)}}
p=Path('evidence/item-13/nether-fortress-selection.json');assert not p.exists()
p.write_text(json.dumps(plan,indent=2)+'\n')
print(hashlib.sha256(p.read_bytes()).hexdigest())
PY
```

The pinned Adorabuild JAR's
`data/adorabuild_structures/worldgen/structure/nether_fortress_large_1.json`,
SHA-256 `7642d69462eff10ab8da44ab515aa905ba56ed95c04ab4ce80b598b504fdcc6c`,
is a vanilla jigsaw root with start_pool nether_fortress/centers,size6,max distance100,
absolute start_height32 and beard_box terrain adaptation. These are generation
parameters, not playable depth. The monster override uses piece bounding boxes
and five types: blaze(weight10,group2..3),zombified piglin(5,4),wither skeleton
(8,5),skeleton(2,5),magma cube(3,4). This is renewable natural-spawn potential,
not authored residents, spawners, actual enemies or realized group sizes. Do not
copy Basalt's source-disable clock to a family with this different mechanism.

## First saved-block extraction

The following bounded command reuses the accepted extractor. Timing/resource
fields describe this read, not player traversal. Its output is a raw observation
retained losslessly with input and backup identities.

```sh
timeout 120 uv run python - <<'PY'
import gzip,hashlib,importlib,json,resource,shutil,time
from pathlib import Path
from tools.analyze_route_opportunities import read_bound
m=importlib.import_module('evidence.item-13.measure')
sha='b5719edf1aa40b47a57aac05cd99fd1a94562f55757f864ac8b31919b51b7142'
plan=json.loads(read_bound(Path('evidence/item-13/nether-fortress-selection.json'),sha))
selected=plan['selected'][0]
rows=json.loads(read_bound(Path('evidence/item-13/candidates.json'),plan['input_sha256']['candidates']))['candidates']
case,=[r for r in rows if r['id']==selected['id']]
assert case['bounds']==selected['bounds'] and case['voxel_count']==32364
output=Path('evidence/item-13/fixed-blocks/adorabuild-nether-fortress-ordinary-r2.json.gz')
assert not output.exists() and not output.is_symlink() and shutil.disk_usage('.').free>=5*1024**3
started=time.monotonic()
result={'selection_sha256':sha,'cases':[m.extract(case,voxel_budget=32364)]}
result['elapsed_seconds']=round(time.monotonic()-started,6)
result['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
raw=gzip.compress((json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0)
assert len(raw)<=20*1024**2
with output.open('xb') as stream:stream.write(raw)
print(len(raw),hashlib.sha256(raw).hexdigest(),result['elapsed_seconds'],result['peak_rss_kib'])
PY
```

First extraction PASS:32,364 cells,6,992 compressed bytes,4.984122 seconds and
43,588 KiB peak RSS. Raw SHA-256 is
`f4f27779a3d28a151c963a9e3c84f5ca1ae6373cad044d6b922f410018fcb0bd`.
The [saved blocks](adorabuild-nether-fortress-ordinary-r2.json.gz) retain exact
start NBT and all pre/post-verified accepted-world identities. The full23-layer
[PNG](adorabuild-nether-fortress-ordinary-r2-slices.png) was inspected; its cells are
block categories, not collision shapes or a player-view render. SVG/PNG sizes
are4,741,569/112,435 bytes. The SVG is a reproducible rendering intermediate,
kept locally under evidence/raw/item13/fortress-render/ordinary-r2-slices.svg.
Retained blocks, the renderer and inspected PNG supply the complete reviewable
evidence without another multi-megabyte copy of block tooltips. Commands executed
before moving that intermediate:

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/adorabuild-nether-fortress-ordinary-r2.json.gz --output evidence/item-13/fixed-blocks/adorabuild-nether-fortress-ordinary-r2-slices.svg
timeout 120 convert -background white evidence/item-13/fixed-blocks/adorabuild-nether-fortress-ordinary-r2-slices.svg evidence/item-13/fixed-blocks/adorabuild-nether-fortress-ordinary-r2-slices.png
```

## First saved/source facts before topology scoring

There are12 saved assembly pieces: four tower components,three bridge_1 components
and five dummy_bridge components. This is not a12-room result. Every component
has bottomY31 and bounding topY53 even when most upper cells are air. Actual tower
centers are large(-254,-110),medium_2(-264,-110),small_1(-254,-120),small_2(-254,-130).
The first/last tower templates are not interchangeable simply because their boxes
match. The selected second assembly retains the other medium/small alternatives.

Saved chest blocks are exactly(-264,33,-109),(-264,41,-109),(-253,33,-130), all
single chests with minecraft:chests/nether_bridge and explicit LootTableSeed.
No saved Items arrays or spawners are present in the extraction. These are three
saved chest/table assignments, not three realized loot inventories or encounters.
They agree spatially with the two medium_2 references and one small_2 reference.

The large tower's source template SHA-256 is
`4b5ab504f748dbc6d64aeb97d58d14246d00748425117a8f4f0050bbfcb43810`.
It authors106 lava blocks. In the saved tower, the3x3 interior atY33..35 and49..51
is lava; these volumes cannot be counted as player rooms. Four interior lava
columns flank the central cross fromY37 through47. AtY36 and48 four holes expose
those columns beside the full-block cross. This requires actual collision/route
validation rather than counting the23-block box as vertical dungeon progression.
The top cap is not automatically a finale or playable activity room.

Small towers have grounded interiors beginning aboveY32 and staggered top slabs
atY33/34/35 beneath dedicated holes in theirY36 roof. Medium_2 repeats a slab
strip across itsY32/36/40/44 floor levels. These are candidate climbs, not accepted
traversal links until the complete actor sweep and landing support pass. The
bridge center floors are nether_bricks atY36, with air atY37/38. Dummy-bridge
centers are air at those heights, so they do not supply equivalent routes.

WORLD_SURFACE at all four tower centers is127. This is Nether-roof height, not
an exterior entrance or continuous ground cover. Nearby ground at sampled bridge/
dummy centers is soul_soil,gravel or soul_sand atY31 with airY32; do not assume
that the surroundings are a lava sea merely because the large tower contains lava.
External-access analysis can reuse this retained ground instead of inventing a
terrain gap. The actual local approach and climb costs remain to be established.

Next resolve the declared actor/task, slab climbs, guarded cross/bridge links,
chest interaction positions, room/landing/roof distinctions and complete modeled
accounting on this representative before extracting the second assembly. No
room count, traversal total or combat result is accepted from this extraction alone.
