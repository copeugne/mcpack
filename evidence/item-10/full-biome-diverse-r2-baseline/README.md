# Biome-diverse repetition-2 baseline

Status: BASELINE-WORLD ACCEPTANCE PASS, with five saved-content exclusions.
Protocol: `item10-full-v1`, observer coverage `item10-observer-coverage-v2`,
continuation `item10-retry-policy-v2`. Seed: `-3503646078644842058`.
Generation source: `cdde6f07dcecdbfb2c8ca9ba1d679a67a3544ade`.

This is the fifth remaining planned world authorized before the final fresh
ocean-heavy repetition-2 control retry. Sixteen complete worlds remain required.
Both previous failed control attempts remain preserved.

The unchanged [run receipt](run.json) records eleven completed selections,
readiness, correlated save confirmation and clean Java exit 0, without rejection
or process-group kill. Duration: 559.092 seconds. Preflight, observer identity
and selections match [repetition 1](../full-biome-diverse-r1-baseline/run.json)
exactly. All 228 frozen configuration files and eleven Chunky paths pass capture.
No tuning, fixtures or proof-world reuse occurred.

The console retains 22 invalid-item messages. No `OutOfMemoryError`, `Failed to
save chunk`, `Failed to load chunk` or `Error upgrading chunk` signature was found.
No instance debug directory was produced. Item-loading diagnostics remain raw
evidence, not loot-correctness acceptance. Lifecycle success is not census acceptance.

## Raw custody

The stopped-world backup preserves 501 files totaling 397,963,125 bytes.
`world.tar.gz` is 134,105,705 bytes, SHA-256
`c2e00a89f08320efbc15919feec22ceaedc4c25dcb600711add31fc02ef2b30a`.
The [world restore](world-restore.json) verifies all 501 files in a fresh target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-biome-diverse-r2-baseline-cdde6f07)
contains the raw archive and [manifest](archive-manifest.json). Its fetched tag
matches the generation source. The archive is 134,878,935 bytes, SHA-256
`1c2353a535cd8a76edb7091c85dba4e419519f4d68ed45f9253bf37b60f580d5`.
Its 313 files total 171,077,298 uncompressed bytes. Manifest SHA-256:
`c832e4f1817d2cdf64455208478c00adbf8e9a3d367627a5c45cd9669531e841`.
[Local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members. The downloaded manifest is byte-identical.

## Reproduction and census

Reuse the [existing custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this world's name, source, archive and world hash. Generation used:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-biome-diverse-r2-baseline --mode probe --preset item10 --role biome-diverse --arm baseline --repetition 2
```

The census uses the verified restored world and unchanged source `cdde6f07`.
Create the analysis parent directory first; require the output to be absent:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-biome-diverse-r2-baseline-custody/restored-world/world evidence/raw/item10/full-biome-diverse-r2-baseline-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-biome-diverse-r2-baseline-custody/restored-local --trace-manifest evidence/item-10/full-biome-diverse-r2-baseline/archive-manifest.json
```

Timing and diagnostics remain in `all-strata-runtime.txt` in the analysis directory.
Census session 40037 ended with exit 0 in 525.490 seconds. Output is
138,485,071 bytes, SHA-256
`c810618b3ef6eefb09a02470a799357f0c05abb470d14af6667cfaa2f085c163`.
All eleven strata contain exactly 4,096 full selected chunks. Fifty incoming
classes pass complete observer coverage and trace validation.


## Saved-content exclusions

Five Overworld candidates remain CONTENT_NOT_PRESERVED and excluded under the
existing rule. Candidate 3876 is `quark:monster_box`; the other four are
`supplementaries:cave_urn_cache`. All eight inspected content positions are in
full saved chunks. Later writers are UNKNOWN. No overlap pairs occur.

| Candidate | Attempt | Content positions | Saved blocks in position order |
| ---: | ---: | --- | --- |
| 3876 | 6023 | (456,-17,416) | minecraft:air |
| 12209 | 19420 | (-376,-10,-240), (-375,-10,-240), (-373,-10,-241) | minecraft:calcite, minecraft:calcite, minecraft:air |
| 16709 | 22267 | (-63,-37,-158), (-59,-37,-156) | minecraft:air at both |
| 26583 | 15195 | (417,32,-273) | minecraft:calcite |
| 29327 | 5933 | (508,24,503) | minecraft:smooth_basalt |

## Accepted counts and limitations

Rates use count times 1,000 / 4,096 within each stratum. All spatial observations,
individual censoring and separate biome exposures remain in the hash-bound output.

| Stratum | Raw registry starts | All locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Aether | 30 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| Earth orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mars orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Moon orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Moon | 12 | 12 | 12 | 0 | 0 | 0 | 0 | 0 | 0 |
| Venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Overworld | 32 | 4161 | 24 | 3 | 4128 | 6 | 0 | 0 | 1 |
| Central End | 3 | 5 | 4 | 0 | 0 | 0 | 0 | 1 | 0 |
| Outer End | 19 | 39 | 38 | 0 | 0 | 0 | 1 | 0 | 0 |
| Nether | 44 | 446 | 30 | 1 | 409 | 5 | 1 | 0 | 0 |

Aether's 28 cloud starts remain excluded terrain. There are 33,074 observer calls
and 32,775 grouped candidates: 25,357 NO_CONSTRUCTIVE_CONTENT, 2,860
OUTSIDE_FRAME, 4,553 OBSERVED_LOCATION and five CONTENT_NOT_PRESERVED.
Biome rows plus unavailable anchors conserve every stratum's accepted location
count. The central-End arena is the sole unavailable biome anchor; no positive
zero-exposure row occurs.

This completes the seventh matched pair and fifteenth planned cell. The baseline's
Overworld T2 and village counts remain six and one in both repetitions, versus
fifteen and four in both controls. Baseline all-location counts change from 4,121
to 4,161; outer End changes from 29 to 39 and Nether from 452 to 446. Overworld T2
nearest-observed mean is 250.19805617985955 blocks; uncensored mean remains null.
Dispersion is 0.9583333333333334 and the largest empty full-cell rectangle is
2,304 chunks, bounds [-32,15,-32,15]. These are fixed-window placements, not
observed fights, pacing or observer-free equivalence. The final authorized
ocean-heavy control retry is still outstanding; Item 10 is not complete.
