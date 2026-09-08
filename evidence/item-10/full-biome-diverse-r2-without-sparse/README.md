# Biome-diverse repetition-2 control

Status: CONTROL-WORLD ACCEPTANCE PASS.
Protocol: `item10-full-v1`, observer coverage `item10-observer-coverage-v2`,
continuation `item10-retry-policy-v2`. Seed: `-3503646078644842058`.
Generation source: `3cd0e358918e9ce7965a239129a827ed6d58436d`.

This is the fourth of the five remaining planned worlds authorized before the
final fresh ocean-heavy repetition-2 control retry. Sixteen complete worlds remain
required. Both previous failed control attempts remain preserved.

The unchanged [run receipt](run.json) records eleven completed selections,
readiness, correlated save confirmation and clean Java exit 0, with no rejection
or process-group kill. Duration: 607.294 seconds. Preflight and observer identity
match [repetition 1](../full-biome-diverse-r1-without-sparse/run.json) exactly;
selections remain unchanged. All 228 frozen configuration files and eleven Chunky
paths pass capture. Only Sparse Structures is omitted. No tuning or fixtures.

The console retains 347 `Tried to load invalid item` messages, an existing
item-loading diagnostic that does not establish loot correctness. No heap,
chunk-save, chunk-load or chunk-upgrade error signature was found. No instance
debug directory was produced. Raw warnings remain preserved.

## Raw custody

The stopped-world backup preserves 501 files totaling 399,820,718 bytes.
`world.tar.gz` is 136,258,217 bytes, SHA-256
`73abf861a74dc1f8e06698d9eeb32c03712a9f46b00ceedb94215275126b6eec`.
The [world restore](world-restore.json) verifies all 501 files in a fresh target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-biome-diverse-r2-without-sparse-3cd0e358)
contains the raw archive and [manifest](archive-manifest.json). Its fetched tag
matches the generation source. The archive is 136,812,711 bytes, SHA-256
`098d2d8d300cdad9e07828d18b15ac5d08b2bbae6665e18bbd6c9a47a1687886`.
Its 312 files total 164,287,212 uncompressed bytes. Manifest SHA-256:
`9d5f268a128065a9575bd41c0f14cf38901d29738d9f60053b0a149cb22ade0b`.
[Local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 312 members; downloaded manifest bytes match. Relative to the
first repetition, the sole absent path is the unexercised incoming
`BetterEndGatewayFeature.class`, governed by the existing coverage-v2 rule.

## Reproduction and census

Reuse the [existing custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this world's name, source, archive and world hash. Generation used:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-biome-diverse-r2-without-sparse --mode probe --preset item10 --role biome-diverse --arm without-sparse --repetition 2
```

The census uses the verified restored world and unchanged source `3cd0e358`.
Create the analysis parent directory first; require the output to be absent:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-biome-diverse-r2-without-sparse-custody/restored-world/world evidence/raw/item10/full-biome-diverse-r2-without-sparse-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-biome-diverse-r2-without-sparse-custody/restored-local --trace-manifest evidence/item-10/full-biome-diverse-r2-without-sparse/archive-manifest.json
```

Timing and diagnostics remain in `all-strata-runtime.txt` in the analysis directory.
Census session 25437 ended with exit 0 in 510.364 seconds. Its output is
117,637,348 bytes, SHA-256
`88978f006449ce5c9dd25a5df97bd80580f33e8adc077d4f51a3781cdb8cdc77`.
All eleven strata contain exactly 4,096 full selected chunks. Coverage-v2 passes
with 49 incoming classes and only the declared unexercised Gateway exception.


## Accepted counts and limitations

Rates use count times 1,000 / 4,096 within each stratum. All category spatial
observations, censoring and biome exposures remain in the hash-bound output.

| Stratum | Raw registry starts | All locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Aether | 126 | 8 | 0 | 0 | 0 | 8 | 0 | 0 | 0 |
| Earth orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mars orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Moon orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Moon | 54 | 54 | 54 | 0 | 0 | 0 | 0 | 0 | 0 |
| Venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Overworld | 128 | 4271 | 75 | 19 | 4162 | 15 | 0 | 0 | 4 |
| Central End | 9 | 11 | 10 | 0 | 0 | 0 | 0 | 1 | 0 |
| Outer End | 75 | 77 | 72 | 1 | 1 | 1 | 2 | 0 | 1 |
| Nether | 146 | 560 | 107 | 0 | 438 | 9 | 6 | 0 | 0 |

Aether's 118 cloud starts remain excluded terrain. The observer records 33,020
calls and 32,766 grouped candidates: 25,350 NO_CONSTRUCTIVE_CONTENT, 2,855
OUTSIDE_FRAME and 4,561 OBSERVED_LOCATION. No saved-content mismatch or overlap
occurs. Biome rows plus unavailable anchors conserve every stratum's accepted
location count. The central-End arena is the sole unavailable biome anchor; no
positive-count zero-exposure row occurs.

This is the fourteenth accepted planned cell. The matched baseline is still
outstanding. Compared with the first control repetition, Overworld total rises
from 4,227 to 4,271 while T2, T3 and village counts remain 15, zero and four.
Outer End rises from 48 to 77, while Nether falls from 597 to 560. These repeated
world differences are retained, not selected away. Overworld T2 nearest-observed
mean is 139.29447166395042 blocks, uncensored mean null, dispersion 0.8625 and
largest empty full-cell rectangle 768 chunks, bounds [-32,15,-16,-1]. This is
fixed-window placement evidence, not fights, pacing or observer-free equivalence.
