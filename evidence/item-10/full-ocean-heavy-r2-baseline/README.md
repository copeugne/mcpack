# Ocean-heavy repetition-2 baseline

Status: BASELINE-WORLD ACCEPTANCE PASS, with ten reviewed overlap exclusions.
Protocol: `item10-full-v1`, observer coverage `item10-observer-coverage-v2`,
continuation `item10-retry-policy-v2`. Seed: `95920844204830198`.
Generation source: `7a60ad986d84f886876ece1ac77f20bf510a2cb0`.

This is the first of the five remaining planned worlds authorized before the
final fresh ocean-heavy repetition-2 control retry. The target remains sixteen
complete worlds, and both earlier control failures remain preserved.

The unchanged [run receipt](run.json) records all eleven completed selections,
readiness, correlated save confirmation and clean Java exit 0, with no rejection
or process-group kill. Duration: 526.634 seconds. Preflight, observer identity
and selections exactly match the [first baseline](../full-ocean-heavy-r1-baseline/run.json).
All 228 frozen configuration files and eleven Chunky paths pass capture. No
fixtures, tuning or before-generation commands were used. The console has no
`OutOfMemoryError`, `Failed to save chunk`, `Failed to load chunk` or
`Error upgrading chunk` signature. No instance debug directory was produced.
Other raw warnings remain retained; lifecycle success is not census acceptance.

## Raw custody

The stopped-world backup preserves 502 files totaling 421,639,560 bytes.
`world.tar.gz` is 154,911,992 bytes, SHA-256
`a6487f15631eb2e71a65189825cdcc8c43e3f2920c9d1a1416b0b2a0ba17b232`.
The [world restore](world-restore.json) verifies all 502 files in a fresh target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ocean-heavy-r2-baseline-7a60ad98)
contains the raw archive and [manifest](archive-manifest.json), with its fetched
tag matching the generation source. The archive is 155,653,064 bytes, SHA-256
`a92fe8aba13f3a19f21d384a8da7d85b138765dd9cb958e0c9c39b7737e30a95`.
Its 313 files total 193,851,522 uncompressed bytes. Manifest SHA-256:
`fb9381cd920e028059533f03825d0623f1fb28768812527e7a8b1bd7759558b1`.
[Local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members. The downloaded manifest is byte-identical.

## Reproduction and census

Reuse the [existing custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this world's name, source, archive and world hash. Generation used:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ocean-heavy-r2-baseline --mode probe --preset item10 --role ocean-heavy --arm baseline --repetition 2
```

The census runs on the verified restored world using source `7a60ad98`, which
includes the biome-comparison processing added at `4dbd9df4`. It does not change
the frozen observer or generation configuration. Create the analysis parent
directory first, and require the output to be absent:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ocean-heavy-r2-baseline-custody/restored-world/world evidence/raw/item10/full-ocean-heavy-r2-baseline-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ocean-heavy-r2-baseline-custody/restored-local --trace-manifest evidence/item-10/full-ocean-heavy-r2-baseline/archive-manifest.json
```

Timing and diagnostics are retained in the analysis directory's
`all-strata-runtime.txt`. Census session 90296 ended with exit 0 in 549.917 seconds.
The output is 130,582,629 bytes, SHA-256
`6bcf618583014bd62f39a0e406d5e5f6eadfe2c330935b572eb4e26f31ad10d5`.
All eleven strata have exactly 4,096 complete selected chunks. Fifty archived
incoming target classes pass complete observer coverage and trace validation.

## Overlap and saved-content review

Direct set intersections of `locations[].content_positions` reproduce all five
raw `overlaps` entries. Every listed candidate is inside the outer-End frame,
and the accepted Item 9 roles for anomalies and monoliths are T0:

| Candidates | Families | Anchors X,Y,Z | Shared positions |
| --- | --- | --- | ---: |
| 27214 / 27215 | anomaly / anomaly | (8334,63,8141) / (8337,64,8134) | 210 |
| 27232 / 27273 | anomaly / monolith | (8383,61,8287) / (8378,61,8288) | 20 |
| 27234 / 27235 | anomaly / anomaly | (8391,57,8311) / (8395,58,8303) | 143 |
| 27245 / 27280 | anomaly / monolith | (8454,58,8262) / (8451,58,8268) | 13 |
| 27246 / 27282 | anomaly / monolith | (8455,59,8243) / (8454,59,8239) | 29 |

Family namespace is `biomesoplenty`. Disposition: REVIEWED, EXCLUDED UNDER THE
EXISTING PROTOCOL, as in the [mountainous overlap review](../full-mountainous-r2-baseline/README.md).
These candidates retain matching saved content as well as their raw flags; they
are overlapping observations, not absent generation. No proximity merge or new
exception is introduced. The accepted outer-End total is 73. Counting all ten
excluded T0 candidates would give 83, an additional 2.44140625 per 1,000 chunks.
This sensitivity is not a corrected numerator or confidence interval.

Candidate 4016 is `quark:monster_box`, attempt 2766, Overworld anchor (48,0,464).
Its content position (58,-49,469) is in a full saved chunk but contains
`minecraft:smooth_basalt`. The single mismatch remains CONTENT_NOT_PRESERVED
and excluded. The trace's constructive observation does not override saved content.
The evidence does not identify the later writer responsible for the mismatch.

## Accepted counts and limitations

All rates are count times 1,000 / 4,096 within the same stratum. The output retains
all category densities, individual spatial observations, censoring and biome bands.

| Stratum | Raw registry starts | All locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Aether | 32 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| Earth orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mars orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Moon orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Moon | 11 | 11 | 11 | 0 | 0 | 0 | 0 | 0 | 0 |
| Venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Overworld | 28 | 1341 | 12 | 1 | 1319 | 7 | 2 | 0 | 1 |
| Central End | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| Outer End | 15 | 73 | 73 | 0 | 0 | 0 | 0 | 0 | 0 |
| Nether | 74 | 474 | 59 | 1 | 409 | 3 | 2 | 0 | 0 |

Aether's 29 cloud starts remain excluded terrain. The observer records 28,700
calls and 28,531 grouped candidates: 24,122 NO_CONSTRUCTIVE_CONTENT, 2,625
OUTSIDE_FRAME, 1,773 OBSERVED_LOCATION, one CONTENT_NOT_PRESERVED and ten
reviewed overlap exclusions. These are separate call and location denominators.
Biome counts conserve all accepted locations. The central-End arena is the sole
unavailable biome anchor; no positive-count zero-exposure row occurs in this world.

Compared with the first baseline, Overworld totals change from 1,294 to 1,341,
outer End from 19 to 73, and Nether from 437 to 474. Overworld T2/T3 remain 7/2;
their stability is not proof of deterministic generation. Overworld T2 finite-window
nearest-observed mean is 214.74959351842614 blocks, while the uncensored mean
remains null. Dispersion is 1.4196428571428572 and largest empty full-cell rectangle
is 1,024 chunks. The final matched r2 control is not yet available. This is the
eleventh accepted planned cell, not Item 10 completion or a reduction of its target.
