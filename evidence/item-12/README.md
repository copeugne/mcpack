# Item 12 structure discoverability

Status: IN PROGRESS. Item 13 is not started.
Authority: SPECS.md Item 12 and the separately user-authorized
[inspection/automated protocol](protocol.md), `item12-discoverability-v1`.
Human recognition and discovery rates remain NOT MEASURED.

## Requirement map before implementation

| Item 12 requirement | Existing evidence reused | Missing deliverable |
| --- | --- | --- |
| Surface visibility | Item 11 raw rays and explicit limitations; Item 8 architecture | Independent sampled viewpoints and external exposure proxies |
| Underground entrance visibility | Item 8 placement/architecture, Item 7 burial context | Explicit entrance assessment, actual saved-world placement sections, no envelope-as-entrance claim |
| Valley viewpoints | Item 11 retained terrain observations | Predeclared low observer, relief and ray outcomes |
| High-terrain viewpoints | Same accepted worlds | Matched high observer and ray outcomes |
| Biome concealment | Item 10 occurrence biome attribution | Same-eye heightmap contrast grouped by recorded biome |
| Recognizable silhouettes | All 448 Item 8 visual descriptions and their source references | Sampled-family architectural judgments with evidence and limitations |
| Entrance importance | Item 8 source forms, underground placement | External lead versus internal-only cue assessments |
| Realistic /locate dependence | Item 8 packaged navigation evidence where present | Inspect applicable survival leads and state bounded command-dependence risk |
| Frequent but concealed versus rare | Item 10 complete counts and denominators | Join existing abundance to independent visibility and assessment results |
| Independent discoverability | Item 11 already distinguishes adjacency/rays/density | Report separate quantities and uncertainties without human-discovery labels |

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

Method decision, input availability and the ordinary representative pass.
The remaining fifteen worlds, their assessments, full report, final validation
and reviewed main delivery remain outstanding.

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
