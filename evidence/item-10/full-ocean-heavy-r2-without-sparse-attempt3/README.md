# Ocean-heavy repetition-2 control, final authorized retry

Status: CONTROL-WORLD ACCEPTANCE PASS, with retained content and overlap exclusions.
Protocol: `item10-full-v1`, observer coverage `item10-observer-coverage-v2`,
continuation `item10-retry-policy-v2`. Seed: `95920844204830198`.
Generation source: `498394f1f0ca0de21820bd8a643a68544de59cee`.

This single final retry began after all five authorized remaining planned worlds
passed their censuses. The sample then had fifteen complete cells and seven
matched pairs. Sixteen complete cells remain required. No further retry is
assumed, and a successful launch or save alone cannot satisfy the census gate.

The [first heap failure](../full-ocean-heavy-r2-without-sparse/README.md) and
[second save failure](../full-ocean-heavy-r2-without-sparse-attempt2/README.md)
remain rejected. Their original local archives were checked against their
committed SHA-256 and size both before and after this generation. Both matched.
Neither archive, failure receipt nor proof world was repaired or replaced.

The unchanged [run receipt](run.json) records eleven completed selections,
readiness, correlated save confirmation and clean Java exit 0, without rejection
or process-group kill. Duration: 552.101 seconds. Preflight, observer identity
and selections match [attempt 2](../full-ocean-heavy-r2-without-sparse-attempt2/run.json)
exactly. All 228 frozen configuration files and eleven Chunky paths pass capture.
Only Sparse Structures is omitted. No tuning, fixture or reused world was used.

No `OutOfMemoryError`, `Failed to save chunk`, `Failed to load chunk` or `Error
upgrading chunk` signature was found in the console. No instance debug directory
was produced. The 372 invalid-item messages remain preserved; they do not
establish loot correctness. The earlier failures are not negated by this result.

## Raw custody

The stopped-world backup preserves 502 files totaling 434,511,139 bytes.
`world.tar.gz` is 168,038,803 bytes, SHA-256
`c754bbb6d423f6a27acd17f694f4332588a46b2276eeb7da6df5d71761466802`.
The [world restore](world-restore.json) verifies all 502 files in a fresh target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ocean-heavy-r2-without-sparse-attempt3-498394f1)
contains the raw archive and [manifest](archive-manifest.json). Its fetched tag
matches the generation source. The archive is 168,506,497 bytes, SHA-256
`746f8b4f839595af3bbea96069d62d799c6527e9e0dd20f25c3733ed658cb514`.
Its 313 files total 194,463,598 uncompressed bytes. Manifest SHA-256:
`37aa7cf1ba9f092cbf7ad4817e17c82f9d8e5a0ee6db85b51c6358568967879f`.
[Local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members. The downloaded manifest is byte-identical.

## Reproduction and census

Reuse the [existing custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this world's name, source, archive and world hash. Generation used:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ocean-heavy-r2-without-sparse-attempt3 --mode probe --preset item10 --role ocean-heavy --arm without-sparse --repetition 2 --attempt 3
```

The census uses the verified restored world and unchanged source `498394f1`.
Create the analysis parent directory first; require the output to be absent:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ocean-heavy-r2-without-sparse-attempt3-custody/restored-world/world evidence/raw/item10/full-ocean-heavy-r2-without-sparse-attempt3-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ocean-heavy-r2-without-sparse-attempt3-custody/restored-local --trace-manifest evidence/item-10/full-ocean-heavy-r2-without-sparse-attempt3/archive-manifest.json
```

Timing and diagnostics remain in `all-strata-runtime.txt` in the analysis directory.
Census session 51235 ended with exit 0 in 482.856 seconds. Output is
99,115,673 bytes, SHA-256
`484b6280b09509ef92af6595a33f8515b394579e0569f7ce3c1ec8877aa59f05`.
All eleven strata contain exactly 4,096 full selected chunks. Fifty incoming
classes pass complete observer coverage and trace validation.


## Exclusions and overlap review

Two Overworld `supplementaries:cave_urn_cache` candidates remain
CONTENT_NOT_PRESERVED. Candidate 13831, attempt 25265, has content positions
(-60,-47,326) and (-58,-47,327), saved respectively as `minecraft:amethyst_block`
and `minecraft:smooth_basalt`. Candidate 13927, attempt 25266, has content position
(-61,-47,330), saved as `minecraft:air`. All three are in full chunks. Their raw
constructive observations remain preserved, and the later writer is UNKNOWN.

Outer-End `biomesoplenty:anomaly` candidates 27249 and 27250 have anchors
(7901,60,8034) and (7910,62,8036), attempts 27367 and 27364. Their 2,503 and 2,622
content positions all match saved content, but the sets share exactly 22 positions.
Direct set intersection verifies the raw overlap count. Both in-frame T0 candidates
are REVIEWED, EXCLUDED under the unchanged overlap rule; raw dispositions remain
OVERLAP_REVIEW_REQUIRED. They are not merged or admitted because the saved blocks
match. Admitting both as a sensitivity case would raise outer-End total from 57
to 59, adding 0.48828125 total/T0 locations per 1,000 chunks. This is not a corrected
numerator and does not affect T2 or T3.

## Accepted counts and limitations

Rates use count times 1,000 / 4,096 within each stratum. Category spatial
observations, censoring and biome exposures remain in the hash-bound output.

| Stratum | Raw registry starts | All locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Aether | 122 | 10 | 0 | 0 | 0 | 10 | 0 | 0 | 0 |
| Earth orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mars orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Moon orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Moon | 49 | 49 | 49 | 0 | 0 | 0 | 0 | 0 | 0 |
| Venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Overworld | 90 | 1358 | 31 | 1 | 1304 | 19 | 3 | 0 | 1 |
| Central End | 7 | 9 | 8 | 0 | 0 | 0 | 0 | 1 | 0 |
| Outer End | 45 | 57 | 52 | 0 | 1 | 3 | 1 | 0 | 0 |
| Nether | 187 | 583 | 134 | 8 | 413 | 26 | 2 | 0 | 0 |

Aether's 112 cloud starts remain excluded terrain. The observer records 28,688
calls and 28,503 grouped candidates: 24,194 NO_CONSTRUCTIVE_CONTENT, 2,627
OUTSIDE_FRAME, 1,678 OBSERVED_LOCATION, two CONTENT_NOT_PRESERVED and two
reviewed overlap exclusions. Biome rows plus unavailable anchors conserve every
stratum's accepted location count. The central-End arena is the sole unavailable
biome anchor; no positive-count zero-exposure row occurs.

Overworld T2 nearest-observed mean is 139.5076386733084 blocks; uncensored mean
remains null. Dispersion is 0.7598684210526315 and the largest empty full-cell
rectangle is 256 chunks, bounds [-32,-17,-32,-17]. Compared with repetition 1,
Overworld total changes from 1,401 to 1,358 while T2/T3/village counts remain
19/3/1. Outer-End total stays 57, and Nether changes from 532 to 583.

The successful retry completes the eighth matched pair and sixteenth planned
cell after eighteen attempts, with both earlier failures retained. The unchanged
configuration was not repaired or demonstrated failure-free. All accepted worlds
together supply 720,896 full selected chunks across 176 strata. Combined analysis,
final review/merge and the Items 2 through 10 audit remain outstanding. This is
placement evidence, not observed fights, pacing or observer-free equivalence.
