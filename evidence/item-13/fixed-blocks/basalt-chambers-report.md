# Basalt Chambers: two-assembly quality assessment

Status: IN PROGRESS. This report is the authoritative local family deliverable.
Room/graph, full-task model, hazards and quality are not yet scored. Item 14 is
UNSTARTED. Apply the approved Item 13 definitions and modeled/inspection boundary.

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

Representative extraction command (pending before first execution):

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
playable elevations and connections remain to be measured.

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
