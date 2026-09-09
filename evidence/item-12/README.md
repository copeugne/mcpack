# Item 12 structure discoverability

Status: IN PROGRESS, corrected v2 local gate PASS. [PR39](https://github.com/copeugne/mcpack/pull/39)
requires a fresh completed clean review, merge and verified main delivery.
Item 13 is not started.

The user separately authorized inspection and automated assessment on 2026-09-09.
The [protocol](protocol.md), `item12-discoverability-v2`, defines the assessment
scope, sampling, viewpoints, denominators, failures and uncertainty. Human
recognition, discovery rates and actual player dependence on commands remain
NOT MEASURED. Do not silently extend the Items 10/11 amendment to these claims.

## Current result and local gate

**PASS under the authorized assessment scope.** The [report](report.md) contains
all sixteen accepted worlds, 464 selected family/world cases and 94 observed
canonical families. The other 354 accepted families retain Item 8 source
assessments but have no case in this finite Overworld viewpoint frame. No zero
visibility or all-dimension visibility conclusion is inferred for them.

The report keeps complete family occurrence counts per 4,096 chunks independent
from ray outcomes, low/high viewpoints and biome-grouped contrasts. Its family
appendix joins those values to existing architectural cues. The
[assessments](assessments.md) distinguish external entrance components, conditional
stairs/shafts, internal cues and caches without a separate entrance, and record
conditional /locate risks. A packaged [trial-map survival lead](navigation-source/README.md)
prevents equating buried trial chambers with mandatory admin commands.

This evaluates entrance visibility and importance through source-supported forms
and sampled placement context. It does not measure exact doorway coordinates,
cave connectivity, player recognition or runtime map acquisition. Envelope targets
are geometric proxies. The high and low observers also differ in azimuth and may
stand on structures, water or vegetation; they are not a causal elevation test or
a walkability result. These limits accompany downstream use.

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

## Validation and resources

The full applicable pre-review gate passed [610 tests in 450.28 seconds](validation/full-gate.txt)
for Items 7/10/11/12 readers and relevant evidence paths. After the narrow boundary
fix, all [eight affected tests pass in 15.41 seconds](validation/v2-final-tests.txt),
including exact report reproduction and evidence-identity rejection. Final
[lint](validation/v2-final-lint.txt), [formatting](validation/v2-final-format.txt)
and [types](validation/v2-final-types.txt) pass. Unchanged upstream gates are not
repeated solely for reassurance.

A clean tracked export of correction commit `51268726f397a1fde0ecd286121a406af78583d1`,
with a separate [locked environment](validation/clean-v2-sync.txt), reproduces the
biome-diverse r1 baseline result byte for byte in
[44.758 seconds](validation/clean-v2-reproduction.txt), SHA-256
`23aafd85335bb8ede94567fc2e240c1b6d2ff3df530ff9767a2444cc515afdea`.
It consumes existing hash-verified restores through explicit `--raw-root`.
This is clean-code reproducibility, not fresh generation or a server benchmark.

[Version 2 resource totals](validation/v2-resource-totals.txt): 787.711 summed
producer seconds, range 37.674 to 72.587, and 814,577 compressed result bytes.
The current report is 129,282 bytes. These fit the predeclared 160-minute and
1-GiB ceilings. Exact derivation: over the sixteen accepted names, sum each result's
byte size and its matching producer log's `real` minutes*60+seconds; sum `len(cases)`
and count unique `family_id`. Timings include operational contention and are not
server-performance measurements. The initial availability check verified
6,806,284,224 world bytes and 1,784,216,273 census bytes in 11.099 seconds.

The initial ordinary representative was completed end to end before expansion,
including fourteen family assessments, report, focused tests and 28 technical
panels. Its rejected v1 results remain at `aa9f700f`; its original clean-code
reproduction and initial failure logs remain under validation/. The corrected
representative used biome-diverse r1 baseline, an actual boundary counterexample.
The protocol's ships/elevated-settlement description refers to the original
ordinary representative, not this correction case.

Manual inspection of the [ordinary sections](ordinary-sections.svg) and relevant
[mountainous panels](mountainous-sections.svg) is recorded in assessments.md.
The [v2 diagram comparison](validation/v2-diagram-comparison.txt) proves that both
galleries are unchanged except their result-hash labels, so prior visual QA still
applies. These are heightmap diagrams, never player screenshots. The first SVG
and import/type/lint failures remain in validation/. Initial ImageMagick rendering
omitted strokes; CairoSVG 2.9.0 rendered them, and explicit fill-opacity corrected
an inconsistent eight-digit color. Browser local-file policy blocked browser
inspection; local rasterization required no browser action. None of these
attempts changed a world or supplied fabricated visual evidence.

## Review finding and preserved rejected evidence

The completed review of `aa9f700f` raised
[finding 3968701864](https://github.com/copeugne/mcpack/pull/39#discussion_r3968701864).
It is valid: 364 v1 endpoint-equality rays across 19 families self-occluded when
`ray_y=target_y=height+1`. The [regression fails before](validation/top-boundary-before.txt)
and [passes after](validation/top-boundary-after.txt) the strict-boundary fix.
Protocol v2 was predeclared before corrected collection; all source worlds,
sampling, viewpoints and targets remain fixed.

The corrected pilot takes 37.977 seconds and 40,549 bytes. Its
[comparison](validation/top-boundary-pilot.txt) changes 36 rays to CLEAR and leaves
all non-ray data identical. The [full comparison](validation/top-boundary-matrix.txt)
finds 366 changed ray records: 364 OCCLUDED to CLEAR, and two OCCLUDED records
whose first-blocker diagnostic changes while a later blocker still occludes.
This is why all rays were recomputed rather than blindly clearing old failures.
For every world, remove `protocol`, `inputs.protocol_sha256`,
`inputs.producer_sha256` and each `cases[].observation.views[].rays` from v1 and v2;
the remaining decoded documents are identical. Counts, source identities,
selection, heights, target geometry and profile observations did not change.
The cited numerical examples in assessments.md remain correct under v2.

Version 1 producer, protocol, raw results, reports, diagrams and rejected local
PASS claims remain at pushed commit
[`aa9f700f`](https://github.com/copeugne/mcpack/tree/aa9f700feb20f9221427e7000721495bee83e889/evidence/item-12).
Correction commit `51268726` preserves the narrow fix, regression and corrected
counterexample; the full v2 matrix supersedes the mixed interim checkpoint.
Raw failed-test whitespace is preserved. No new schema, validator framework,
archive revision or controlled world experiment was added.

Item 11 retains its separately declared conservative height-field metric; v2
uses a different boundary definition without relabeling or recalculating Item 11.
No source-world, placement or frozen-identity conflict was found. The completed
audit, classification and route matrix were not repeated. Item 10's
[heap-failed attempt](../item-10/full-ocean-heavy-r2-without-sparse/README.md) and
[incomplete-save attempt](../item-10/full-ocean-heavy-r2-without-sparse-attempt2/README.md)
remain excluded and preserved. The accepted third attempt is unchanged. No v2
world-analysis attempt failed or substituted a location.

## Reproduction

Use `uv sync --locked`. Restore the accepted inputs using the linked Item 10
per-world instructions. Defaults are `evidence/raw/item10/NAME-custody/restored-world/world`,
adjacent `restored-local/world-backup.json`, and `NAME-analysis/all-strata.json`.
The producer validates archive binding, census identity and the complete world
inventory under the existing Java-compatible POSIX lock before and after reading.
No source world is booted. Choose absent output paths; never overwrite old evidence.

Executed commands, with fresh scratch paths substituted for retained outputs:

```sh
uv run --no-sync python -m tools.analyze_discoverability \
  --name full-biome-diverse-r1-baseline \
  --output /tmp/item12-v2-representative.json.gz
PYTHONPATH=. uv run --no-sync python evidence/item-12/summarize.py \
  --results evidence/item-12/results --output /tmp/item12-v2-report.md
cmp evidence/item-12/report.md /tmp/item12-v2-report.md
uv run --no-sync pytest -q tests/item12
uv run --no-sync ruff check tools/analyze_discoverability.py tests/item12 \
  evidence/item-12/render.py evidence/item-12/summarize.py
uv run --no-sync basedpyright tools/analyze_discoverability.py tests/item12 \
  evidence/item-12/render.py evidence/item-12/summarize.py
```

For the full matrix, obtain the sixteen names from the existing `accepted_inputs()`
and invoke that same analyzer once per name, retaining each timed producer log.
V2 was executed sequentially into `evidence/raw/item12/v2/NAME.json.gz` and `.txt`,
then promoted to results/ and validation/full/ only after successful comparison.
The producer source is committed, and each output binds its exact source and
protocol digests. Reproduction must use another absent output directory.

The [renderer](render.py) takes `--result` and `--output` for either gallery.
For visual QA the SVG was rasterized through the isolated command
`uv run --with cairosvg==2.9.0 python`, calling `cairosvg.svg2png` on the SVG.
No project dependency, graphical Minecraft client or server installation is
required. The initial availability inspection command is preserved in the
[predeclaration milestone](https://github.com/copeugne/mcpack/blob/a93a42f3/evidence/item-12/README.md#reproduce-input-availability).

Final completed clean Codex review, merge and verified main delivery remain
required. Do not declare Item 12 COMPLETE or start Item 13 at this local gate.
