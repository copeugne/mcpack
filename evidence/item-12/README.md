# Item 12 structure discoverability

Status: IN PROGRESS. Item 13 is not started.
Authority: SPECS.md Item 12 and the separately user-authorized
[inspection/automated protocol](protocol.md), `item12-discoverability-v1`.
Human recognition and discovery rates remain NOT MEASURED.

## Requirement map and delivered evidence

| Item 12 requirement | Existing evidence reused | New evidence delivered |
| --- | --- | --- |
| Surface visibility | Item 11 raw rays and explicit limitations; Item 8 architecture | [All sixteen viewpoint matrices](report.md) |
| Underground entrance visibility | Item 8 placement/architecture, Item 7 burial context | [Conditional source/entrance assessments](assessments.md), [ordinary](ordinary-sections.svg) and [mountainous](mountainous-sections.svg) placement context; no envelope-as-entrance claim |
| Valley viewpoints | Item 11 retained terrain observations | [Per-case low observer, relief and ray outcomes](report.md) |
| High-terrain viewpoints | Same accepted worlds | [Per-case high observer and ray outcomes](report.md), with azimuth confounding explicit |
| Biome concealment | Item 10 occurrence biome attribution | [Complete same-eye heightmap contrasts by recorded biome](report.md) |
| Recognizable silhouettes | All 448 Item 8 visual descriptions and their source references | [Family cue appendix](report.md#independent-family-abundance-and-discovery-cues) and [bounded judgments](assessments.md) |
| Entrance importance | Item 8 source forms, underground placement | [External leads versus internal-only cues](assessments.md) |
| Realistic /locate dependence | Item 8 packaged navigation evidence where present | [Packaged trial-map lead](navigation-source/README.md) and [conditional risks](assessments.md) |
| Frequent but concealed versus rare | Item 10 complete counts and denominators | [Independent family abundance/cue join](report.md#independent-family-abundance-and-discovery-cues) |
| Independent discoverability | Item 11 already distinguishes adjacency/rays/density | [Separate count, ray and assessment quantities](report.md), with explicit denominators and uncertainty |

## Dependency and input disposition

Fetched main `486c2dd6e5fcb9967f69de05176aa52bdaa5903f` contains PR35, PR36,
PR37 and PR38. Startup branch `codex/item11-completion-record` was clean and
identical to main. Item 12 branch starts from that main; no history was rewritten.
The delivered [Item 11 closure](../item-11/README.md#verified-delivery) records its
completed clean final review and merge. The [cross-item audit](../item-10/cross-item-audit.md)
is reused, not repeated. Its Item 7 continuation exception remains explicit.

The [availability inspection](validation/input-availability.txt) verifies all
sixteen archive-bound restored world inventories and exact accepted census hashes.
The shared frozen runtime/configuration identities are those in the delivered
[cross-item audit](../item-10/cross-item-audit.md#exact-shared-inputs): retained 136
JARs, Minecraft 1.21.1, NeoForge 21.1.249, Temurin 21.0.12.1+1-LTS, unchanged
Item 6 configuration. Item 10's Chunky/observer overlay and omit-Sparse control
remain separate from the retained baseline identity. No runtime starts are needed.

Reuse [Item 10 custody and density](../item-10/README.md),
[accepted census index](../item-10/accepted-biome-comparisons.json.gz),
[Item 11 raw observations](../item-11/results/),
[Item 8 inventory](../item-8/inventory.json), and
[Item 9 classification](../item-9/classification.md).
Item 7's visual fidelity review covers heightmap diagrams, not textured player
views or recognition. It cannot close the missing Item 12 perceptual claims.

## Current batch

The full local exit gate passes under the separately authorized assessment scope.
Final completed clean Codex review, merge and verified main delivery remain.
Item 13 is unstarted.

## Reproduce input availability

Executed from the repository root with the existing locked environment. This is
an inspection through existing custody primitives, not another validator framework.
The default raw paths are restored using each linked Item 10 world's commands.

```sh
uv run --no-sync python - <<'PY'
import json, time, shutil
from tools.analyze_route_opportunities import ROOT, accepted_inputs, read_bound, verify_world
from tools.manage_item4_environment import _world_backup_lock
from mcpack_evidence.item7_archive_models import ArchiveManifest
start = time.monotonic()
total = census_bytes = 0
for name, identity in sorted(accepted_inputs().items()):
    custody = ROOT / 'evidence/raw/item10' / f'{name}-custody'
    manifest = ArchiveManifest.model_validate_json(read_bound(
        ROOT / 'evidence/item-10' / name / 'archive-manifest.json'))
    entry = next(r for r in manifest.files if r.relative_path == 'world-backup.json')
    backup = json.loads(read_bound(custody / 'restored-local/world-backup.json', entry.sha256))
    assert backup['archive_sha256'] == next(
        r.sha256 for r in manifest.files if r.relative_path == 'world.tar.gz')
    world = custody / 'restored-world/world'
    with _world_backup_lock(world):
        verify_world(world, backup['world_files'])
    raw = read_bound(ROOT / 'evidence/raw/item10' / f'{name}-analysis/all-strata.json',
                     identity['input_sha256'])
    size = sum(r['size_bytes'] for r in backup['world_files'])
    total += size
    census_bytes += len(raw)
    print(name, 'PASS', len(backup['world_files']), size, len(raw), identity['input_sha256'])
print(json.dumps(dict(world_bytes=total, census_bytes=census_bytes,
                     elapsed_seconds=time.monotonic()-start,
                     free_bytes=shutil.disk_usage(ROOT).free)))
PY
```

## Representative completed before expansion

Ordinary r1 baseline is complete as a bounded fourteen-family increment:
[raw observations](results/full-ordinary-r1-baseline.json.gz),
[numerical report](report.md), [architectural assessments](assessments.md) and
[technical sections](ordinary-sections.svg). The [producer log](validation/full/full-ordinary-r1-baseline.txt)
records 37.150 seconds and 19,960 compressed bytes. A simple sixteen-world
extrapolation is 594.4 seconds and 319,360 bytes; family counts and world content
vary, so retain the larger predeclared 160-minute/1-GiB ceilings. This is an
operational projection, not a benchmark or guarantee. No expansion has occurred
at this checkpoint.

The report preserves 14 selected cases, eight observer cells per geometric case,
separate WS/NL rays, all three UNKNOWN-extremum cases, and full occurrence counts.
The six [focused checks](validation/representative-six-tests.txt) pass, including
selection order, obstruction/UNKNOWN, same-eye contrast, retained report values,
diagram reproduction and rejection of changed/misbound evidence.
[Types](validation/representative-final-types.txt) and
[lint](validation/representative-lint.txt) pass. Initial import/type errors are
retained in validation/initial-* and representative-types.txt; the package marker
and explicit type narrowing corrected them before accepted collection. No world
processing attempt failed or source evidence changed.

Manual inspection of all 28 panels found the surface ships, buried selected
objects, minimal temple envelope, elevated settlement and edge gaps consistent
with the retained coordinates and heights. The panels explicitly disclose their
heightmap-only scope; they cannot reveal a cave entrance or rendered silhouette.
The first SVG is retained in [validation](validation/ordinary-sections-first.svg).
ImageMagick's initial rasterization omitted stroke paths; it was rejected for
visual inspection. CairoSVG rendered the paths, and an explicit fill-opacity
replaced the inconsistently supported eight-digit fill color. Final SVG inspection
shows readable identity/axes, retained gaps and transparent envelopes. This is
artifact visual QA, not player testing. Browser local-file policy blocked the
browser inspection; local rasterization required no browser action.

Executed reproduction commands (choose absent output paths):

```sh
uv run --no-sync python -m tools.analyze_discoverability \
  --name full-ordinary-r1-baseline --output /tmp/item12-representative.json.gz
PYTHONPATH=. uv run --no-sync python evidence/item-12/summarize.py \
  --results evidence/item-12/results --representative --output /tmp/item12-report.md
uv run --no-sync python evidence/item-12/render.py \
  --result evidence/item-12/results/full-ordinary-r1-baseline.json.gz \
  --output /tmp/item12-sections.svg
uv run --no-sync pytest -q tests/item12
uv run --no-sync ruff check tools/analyze_discoverability.py tests/item12 \
  evidence/item-12/render.py evidence/item-12/summarize.py
uv run --no-sync basedpyright tools/analyze_discoverability.py tests/item12 \
  evidence/item-12/render.py evidence/item-12/summarize.py
```

For visual inspection only, the SVG was rasterized with the isolated pinned
CairoSVG 2.9.0 package via `uv run --with cairosvg==2.9.0 python`, calling
`cairosvg.svg2png(url='evidence/item-12/ordinary-sections.svg', write_to=...)`.
The deterministic SVG is committed; no project dependency or client installation
is required for numerical reproduction.

## Clean reproduction and expansion method

A clean tracked export of `bbad023d` with a separate locked environment reproduced
the ordinary raw result byte for byte in 41.701 seconds, SHA-256
`3500ea443906cae3d7b26de8ee2eaec0e9a74b845a998c2b907d4794c6e4baac`.
[Environment installation](validation/clean-sync.txt) and
[producer output](validation/clean-reproduction.txt) are retained. The clean code
consumed the existing hash-verified accepted restores through explicit `--raw-root`;
it does not claim fresh world generation, a new restore or a clean-machine benchmark.

The remaining-world collection uses the same unchanged producer and protocol:

```sh
uv run --no-sync python - <<'PY' > /tmp/item12-remaining.txt
from tools.analyze_route_opportunities import accepted_inputs
print('\n'.join(n for n in sorted(accepted_inputs()) if n != 'full-ordinary-r1-baseline'))
PY
while IFS= read -r name; do
  { time uv run --no-sync python -m tools.analyze_discoverability --name "$name" \
      --output "evidence/item-12/results/$name.json.gz"; } \
    > "evidence/item-12/validation/full/$name.txt" 2>&1 || exit 1
done < /tmp/item12-remaining.txt
```

For reproduction, use an absent output directory and retain new logs separately;
the producer refuses to overwrite accepted results. The original representative
and report are preserved in the milestone commit. No route matrix, world generation,
classification, preservation or configuration audit was repeated for these outputs.

## Full local exit gate

**PASS for the separately authorized Item 12 scope; review and main delivery are
still required.** All ten requirement rows above have delivered evidence and
explicit inference limits. The complete [report](report.md) covers sixteen worlds,
464 selected family/world cases and 94 distinct canonical families. The remaining
354 accepted families have source assessments but no case in this finite viewpoint
frame; no zero discoverability or all-dimension visibility claim is inferred.
The ordinary result bytes and producer are unchanged from the representative
milestone; the other fifteen outputs use the same source and protocol identities. The [assessments](assessments.md) integrate source-supported entrance
mechanisms, importance cues, silhouettes and conditional command-dependence risks.
These assess entrances; they do not measure exact opening coordinates, cave
connectivity, human recognition or actual player reliance on commands.

All sixteen collections succeeded without changing selection or configuration.
Item 10's [heap-failed ocean attempt](../item-10/full-ocean-heavy-r2-without-sparse/README.md)
and [incomplete-save attempt](../item-10/full-ocean-heavy-r2-without-sparse-attempt2/README.md)
remain excluded, preserved evidence. The accepted third attempt remains the only
r2 ocean control input. Missing viewpoints and occlusion are retained outcomes,
not producer failures or reasons to substitute locations.

[Resource totals](validation/resource-totals.txt): 815,332 compressed result bytes;
1,037.807 total producer seconds, range 37.150 to 192.525 seconds. The report is
129,273 bytes. This fits the 160-minute and 1-GiB ceilings. Concurrent source
inspection, clean reproduction and tests affect wall times; these are operational
costs, not server-performance measurements. Exact totals are reproduced by summing
result sizes and the `real` line of each named producer log over the accepted
sixteen-name index, with family/case counts from those same results.

[Full applicable gate](validation/full-gate.txt): **610 tests pass in 450.28 seconds**
for `tests/item7 tests/item10 tests/item11 tests/item12`. The final report integration
adds a focused complete-matrix reproduction check; all [seven final Item 12 tests](validation/final-tests.txt)
pass in 19.14 seconds. Final [lint](validation/final-lint.txt),
[formatting](validation/final-format.txt), and [types](validation/final-types.txt)
pass. No unchanged full gate is repeated solely for reassurance. The source-world
representative reproduces from the clean tracked export as recorded above.

The final generated report is rebuilt with the same script, omitting
`--representative`:

```sh
PYTHONPATH=. uv run --no-sync python evidence/item-12/summarize.py \
  --results evidence/item-12/results --output /tmp/item12-full-report.md
cmp evidence/item-12/report.md /tmp/item12-full-report.md
```

The mountainous gallery uses the same renderer with
`--result evidence/item-12/results/full-mountainous-r1-baseline.json.gz`.
Its inspected terrain and vegetation panels and numerical comparisons are recorded
in assessments.md. No graphical client, new world, operational server, config
change or new archive revision was needed. This completion scope must accompany
future Item 13/20/21/31 use; do not promote it to observed human discovery or use
an envelope ray as proof of a visible entrance.
