# Biome-diverse repetition-1 baseline

Status: BASELINE-WORLD ACCEPTANCE PASS, with two saved-content exclusions.
Protocol: `item10-full-v1`, observer coverage `item10-observer-coverage-v2`,
continuation `item10-retry-policy-v2`. Seed: `-3503646078644842058`.
Generation source: `6bef6d99fa1d4849a5dffb97daed4b2768954cc2`.

This is the second of the five remaining planned worlds authorized before the
final fresh ocean-heavy repetition-2 control retry. The target remains sixteen
complete worlds. Both previous failed control attempts remain preserved.

The unchanged [run receipt](run.json) records all eleven completed selections,
readiness, correlated save confirmation and clean Java exit 0, with no rejection
or process-group kill. Duration: 577.243 seconds. Preflight differs from the
[preceding baseline](../full-ocean-heavy-r2-baseline/run.json) only in the declared
seed and seed role. Observer identity and selections match exactly. All 228 frozen
configuration files and eleven Chunky paths pass capture. No fixtures, tuning or
before-generation commands were used. The console has no `OutOfMemoryError`,
`Failed to save chunk`, `Failed to load chunk` or `Error upgrading chunk` signature.
No instance debug directory was produced. Other raw warnings remain retained;
lifecycle success is not census acceptance.

## Raw custody

The stopped-world backup preserves 501 files totaling 397,569,861 bytes.
`world.tar.gz` is 134,220,283 bytes, SHA-256
`a678c0af829c01358e9248efbd9a6141ae8abd781da45ce1832b53b6e862f7f7`.
The [world restore](world-restore.json) verifies all 501 files in a fresh target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-biome-diverse-r1-baseline-6bef6d99)
contains the raw archive and [manifest](archive-manifest.json), with its fetched
tag matching the generation source. The archive is 134,740,882 bytes, SHA-256
`51bf69b36f931dc7a0195f7cfc3e35abfd8fd9dbb25437084fe420ef7933acfe`.
Its 313 files total 161,306,318 uncompressed bytes. Manifest SHA-256:
`2c66f87955ea6f31717114c94c638a5f41618bac80465f9bb4dc616e917bcaa6`.
[Local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members. The downloaded manifest is byte-identical.

## Reproduction and census

Reuse the [existing custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this world's name, source, archive and world hash. Generation used:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-biome-diverse-r1-baseline --mode probe --preset item10 --role biome-diverse --arm baseline --repetition 1
```

The census uses the verified restored world and source `6bef6d99`, including the
existing biome-comparison processing. Create the analysis parent directory first
and require the output to be absent:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-biome-diverse-r1-baseline-custody/restored-world/world evidence/raw/item10/full-biome-diverse-r1-baseline-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-biome-diverse-r1-baseline-custody/restored-local --trace-manifest evidence/item-10/full-biome-diverse-r1-baseline/archive-manifest.json
```

Timing and diagnostics are retained in the analysis directory's
`all-strata-runtime.txt`. Census session 15991 ended with exit 0 in 569.638 seconds.
The output is 113,226,244 bytes, SHA-256
`1bc84c7cdd4cd21e26d722632de4d39730c370ba9c231ffef0463eaa5d6f30d5`.
All eleven strata have exactly 4,096 complete selected chunks. Fifty archived
incoming target classes pass complete observer coverage and trace validation.

## Saved-content exclusions

Both excluded candidates are Overworld `supplementaries:cave_urn_cache` locations.
Candidate 16688, attempt 22298, has anchor (-61,-37,-158) and two content positions
(-63,-37,-158) and (-59,-37,-156). Candidate 18393, attempt 12523, has anchor
(120,-8,-105) and content position (116,-9,-105). All three positions are in full
saved chunks but contain `minecraft:air`. They remain CONTENT_NOT_PRESERVED
and excluded under the existing rule. Their constructive trace observations do
not override saved content. The responsible later operation is not identified.
No overlap pairs or overlap-review dispositions occur in this result.

## Accepted counts and limitations

Rates use count times 1,000 / 4,096 within the same stratum. The output retains
all category densities, individual spatial observations, censoring and biome bands.

| Stratum | Raw registry starts | All locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Aether | 30 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| Earth orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mars orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Moon orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Moon | 12 | 12 | 12 | 0 | 0 | 0 | 0 | 0 | 0 |
| Venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Overworld | 32 | 4121 | 23 | 3 | 4089 | 6 | 0 | 0 | 1 |
| Central End | 3 | 5 | 4 | 0 | 0 | 0 | 0 | 1 | 0 |
| Outer End | 24 | 29 | 28 | 0 | 0 | 0 | 1 | 0 | 0 |
| Nether | 37 | 452 | 23 | 1 | 422 | 3 | 3 | 0 | 0 |

Aether's 28 cloud starts remain excluded terrain. The observer records 33,034
calls and 32,772 grouped candidates: 25,400 NO_CONSTRUCTIVE_CONTENT, 2,859
OUTSIDE_FRAME, 4,511 OBSERVED_LOCATION and two CONTENT_NOT_PRESERVED. These
are separate call and location denominators. Biome counts conserve all accepted
locations; the central-End arena is the sole unavailable biome anchor. No
positive-count zero-exposure row occurs in this world.

The Overworld's 4,121 locations include six T2 dungeons, no T3 expeditions and one
village. Its high total is dominated by 4,089 provisional T1 locations, not a
count of fights. T2 finite-window nearest-observed mean is 250.19805617985955
blocks; the uncensored mean remains null. Dispersion is 0.9583333333333334 and
the largest empty full-cell rectangle is 2,304 chunks with bounds [-32,15,-32,15].
This is the first accepted biome-diverse baseline and the twelfth accepted planned
cell. Its matched control and second repetition remain outstanding. No tuning,
observer-free causal claim or Item 10 completion follows from this single sample.
