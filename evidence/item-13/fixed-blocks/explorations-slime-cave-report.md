# Explorations Slime Cave

Status: IN PROGRESS. Authoritative local Item13 assessment, under the separately
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
