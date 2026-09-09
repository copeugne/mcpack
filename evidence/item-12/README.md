# Item 12 structure discoverability

Status: COMPLETE through clean-reviewed, merged [PR39](https://github.com/copeugne/mcpack/pull/39).
[Verified delivery](#verified-delivery) records the accepted head and fetched main.
Item 13 is not started.

The user separately authorized inspection and automated assessment on 2026-09-09.
The [protocol](protocol.md), `item12-discoverability-v3`, defines sampling,
viewpoints, denominators, failure handling and uncertainty. Human recognition,
discovery rates and actual player command dependence remain NOT MEASURED. This
is a separate Item 12 decision, not an extension of the Items 10/11 amendment.

## Current result and local gate

**PASS under the authorized assessment scope.** The [report](report.md) covers all
sixteen accepted worlds, 464 family/world cases and 94 observed canonical families.
The other 354 accepted families retain Item 8 source assessments but have no case
in this finite Overworld frame. No zero visibility or all-dimension conclusion is
inferred for them. Generation counts per 4,096 chunks remain independent from
viewpoint outcomes and architectural judgments.

The [assessments](assessments.md) distinguish external entrance components,
conditional stairs/shafts, internal importance cues and caches without a separate
entrance. A packaged [trial-map survival lead](navigation-source/README.md) prevents
equating burial with mandatory /locate. Exact doorway visibility, cave connectivity,
player recognition and runtime map acquisition are not measured. Envelope targets
are geometric proxies. Internal observer cells remain UNKNOWN; other observers
may stand on water or other structures, and low/high azimuths differ. This is not
a walkability result or causal elevation experiment.

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

The full applicable pre-review gate passed [610 tests in 450.28 seconds](validation/full-gate.txt).
After the narrow fixes, the [nine affected tests](validation/v3-final-tests.txt)
pass, including exact report reproduction, the two review regressions and evidence
identity rejection. Final [lint](validation/v3-final-lint.txt),
[formatting](validation/v3-final-format.txt) and [types](validation/v3-final-types.txt)
pass. Unchanged upstream gates are not repeated solely for reassurance.

A clean tracked export of correction commit `62401a14`, with a separate
[locked environment](validation/clean-v3-sync.txt), reproduces the ordinary r1
baseline byte for byte in [42.829 seconds](validation/clean-v3-reproduction.txt),
SHA-256 `284e44dc5fc934e9aa520a5ac90c619fa94487f4c2c604da476d7db485512027`.
It consumes existing hash-verified restores through explicit `--raw-root`.
This is clean-code reproduction, not generation or a server benchmark.

[Version 3 totals](validation/v3-resource-totals.txt): 757.156 summed producer
seconds, range 36.435 to 66.286, and 792,086 compressed result bytes. The report is
128,667 bytes. Derivation: sum the sixteen accepted outputs' byte sizes and each
matching producer log's `real` minutes*60+seconds. Count cases and unique family
IDs separately. These fit the predeclared correction allowance of 20 minutes and
1 MiB, within the original 160-minute/1-GiB ceilings. Timings include operational
contention and are not server-performance measurements. Peak memory is not claimed.

The original ordinary representative completed fourteen assessments, a report,
focused tests and 28 technical panels before initial expansion. V2 first completed
a biome-diverse counterexample; v3 first completed the ordinary counterexample
([pilot report](validation/internal-observer-pilot-report.md)). V3 pilot cost:
40.228 seconds and 19,317 bytes, checked before the remaining fifteen worlds.
The initial availability inspection verified 6,806,284,224 world bytes and
1,784,216,273 census bytes in 11.099 seconds. All processing used read-only restores.

Manual inspection of the [ordinary sections](ordinary-sections.svg) and relevant
[mountainous panels](mountainous-sections.svg) is recorded in assessments.md.
The [v3 comparison](validation/v3-diagram-comparison.txt) proves both galleries
unchanged from v2 except result-hash labels, so prior visual QA applies. These are
heightmap diagrams, never player screenshots. Initial ImageMagick rendering omitted
strokes; CairoSVG 2.9.0 rendered them, and explicit fill-opacity fixed an inconsistent
color. Browser local-file policy blocked browser inspection; local rasterization
required no browser action. The first SVG and failed import/type/lint attempts
remain under validation/. No fabricated visual observation is used.

## Review findings and preserved rejected evidence

The completed review of `aa9f700f` raised valid
[finding 3968701864](https://github.com/copeugne/mcpack/pull/39#discussion_r3968701864):
endpoint equality self-occluded 364 rays across 19 families. The regression
[fails before](validation/top-boundary-before.txt) and
[passes after](validation/top-boundary-after.txt) the strict-boundary fix.
Predeclared v2 changes 364 rays to CLEAR and updates two first-blocker diagnostics
without clearing those rays ([full comparison](validation/top-boundary-matrix.txt)).
Every non-ray field remained unchanged. The narrow fix and pilot are in `51268726`;
the complete v2 matrix is in `eb2742a2`. V3 retains this correction.

The completed review of `eb2742a2` raised valid
[finding 3969034729](https://github.com/copeugne/mcpack/pull/39#discussion_r3969034729):
398 of 3,216 registry observer cells lie inside their target's inclusive horizontal
envelope, affecting 68 cases; 22 have all eight inside. They cannot establish
external discoverability. Predeclared v3 preserves cells and heights but marks
all 3,980 associated rays UNKNOWN with reason `observer_inside_envelope` and makes
low/high/relief UNKNOWN for rings with any internal cell. No observer is moved.
The [regression fails before](validation/internal-observer-before.txt) and
[passes after](validation/internal-observer-after.txt); correction and pilot are
in `62401a14`. The [full comparison](validation/internal-observer-matrix.txt) verifies
every external view unchanged and all other source, sample and profile data equal.
The airship and abandoned-temple assessments now explicitly exclude their internal
rings. All other cited numerical examples remain correct.

Exact comparison derivation: pair v2 and v3 cases/views by their unchanged order.
A cell is internal iff its X and Z fall within the saved inclusive envelope bounds.
Require each internal ray to equal the documented UNKNOWN record; require external
view dictionaries equal. Affected low/high/relief must be null; unaffected
observations must match. Remove rays and low/high/relief from paired observations,
and remove protocol identifier and protocol/producer hashes from document inputs;
require remaining decoded documents equal. Count internal cells, their rays and
affected cases directly. No new validator framework or archive revision is needed.

Rejected versions and their local PASS claims are immutable Git evidence:
[v1 at aa9f700f](https://github.com/copeugne/mcpack/tree/aa9f700feb20f9221427e7000721495bee83e889/evidence/item-12),
[v2 at eb2742a2](https://github.com/copeugne/mcpack/tree/eb2742a2bd0e9ec979e5831c6865dd4622e78000/evidence/item-12).
Preserved failure logs keep their original whitespace. No v3 world-analysis attempt
failed or substituted a sample. Item 10's heap-failed and incomplete-save ocean
attempts remain excluded under their original custody; the accepted third attempt
is unchanged.

Item 11 retains its separately declared conservative height-field metric. Item 12
uses different boundary/observer rules without relabeling or recalculating Item 11.
No source-world, placement or frozen-identity conflict was found. Completed audits,
classification, world generation, preservation and route processing were not repeated.

## Reproduction

Use `uv sync --locked`. Restore inputs using the linked Item 10 per-world
instructions. Defaults are `evidence/raw/item10/NAME-custody/restored-world/world`,
adjacent `restored-local/world-backup.json`, and `NAME-analysis/all-strata.json`.
The producer checks archive binding, census identity and the complete world
inventory under the existing Java-compatible POSIX lock before and after reading.
No world is booted. Choose absent output paths to preserve earlier evidence.

```sh
uv run --no-sync python -m tools.analyze_discoverability \
  --name full-ordinary-r1-baseline --output /tmp/item12-v3-representative.json.gz
PYTHONPATH=. uv run --no-sync python evidence/item-12/summarize.py \
  --results evidence/item-12/results --output /tmp/item12-v3-report.md
cmp evidence/item-12/report.md /tmp/item12-v3-report.md
uv run --no-sync pytest -q tests/item12
uv run --no-sync ruff check tools/analyze_discoverability.py tests/item12 \
  evidence/item-12/render.py evidence/item-12/summarize.py
uv run --no-sync basedpyright tools/analyze_discoverability.py tests/item12 \
  evidence/item-12/render.py evidence/item-12/summarize.py
```

For the full matrix obtain the sixteen names from existing `accepted_inputs()`
and invoke the analyzer once per name, retaining each timed log. V3 ran sequentially
into `evidence/raw/item12/v3/NAME.json.gz` and `.txt`, then was promoted to results/
and validation/full/ after comparison. Each output binds committed source and
protocol digests. The renderer takes `--result` and `--output` for either gallery.
Visual QA used isolated `uv run --with cairosvg==2.9.0 python` with `cairosvg.svg2png`.
No project dependency or Minecraft client/server installation was added.
The initial availability command remains in the
[predeclaration milestone](https://github.com/copeugne/mcpack/blob/a93a42f3/evidence/item-12/README.md#reproduce-input-availability).

## Verified delivery

**COMPLETE under the separately authorized inspection and automated assessment scope.**
Codex completed its final review of
`4fc7e6050d449c69c91ebcddc56e86ee16648ddd` at 2026-09-09 14:10:42 UTC,
posted the [clean result](https://github.com/copeugne/mcpack/pull/39#issuecomment-5603273097)
and returned its thumbs-up (reaction `496740300`, 14:10:47 UTC).
The completed cycle introduced no new inline or discussion findings. All four
previous findings were fixed and their threads resolved: top-boundary occlusion,
internal observers, ledger punctuation (`a3924ecc`) and stale handoff continuation
(`4fc7e605`). The measurement results remain unchanged since `0e8bc2da`.

PR39 merged at 2026-09-09 14:11:53 UTC as
`33e11923091af76d7ada3b5f59f6681a49b16e4e`. A fresh fetch verified that exact
`origin/main` ref, accepted-head ancestry and zero tree differences from the
reviewed head. The local gate, raw evidence, failure dispositions, clean review
and durable main delivery therefore all pass. Human metrics remain NOT MEASURED.

This completion record is authored on `codex/item12-completion-record` from that
verified main. Its later delivery ref is verified through current Git/PR history;
the PR39 snapshot above is the immutable Item 12 acceptance reference. No source,
protocol, result or upstream evidence changes accompany this record. Do not start
Item 13 without a new user instruction.
