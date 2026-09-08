# Biome-diverse repetition-1 control

Status: CONTROL-WORLD ACCEPTANCE PASS, with six saved-content exclusions.
Protocol: `item10-full-v1`, observer coverage `item10-observer-coverage-v2`,
continuation `item10-retry-policy-v2`. Seed: `-3503646078644842058`.
Generation source: `44212515b2bea1e1935295e39682f911720c917f`.

This is the third of the five remaining planned worlds authorized before the
final fresh ocean-heavy repetition-2 control retry. The target remains sixteen
complete worlds. Both previous failed control attempts remain preserved.

The unchanged [run receipt](run.json) records all eleven completed selections,
readiness, correlated save confirmation and clean Java exit 0, with no rejection
or process-group kill. Duration: 668.830 seconds. Preflight differs from the
[first ocean control](../full-ocean-heavy-r1-without-sparse/run.json) only in the
declared seed and seed role. Observer identity and selections match exactly.
All 228 frozen configuration files and eleven Chunky paths pass capture. Only
Sparse Structures is omitted by the declared control; no configuration tuning,
fixtures or before-generation commands were used.

The console has no `OutOfMemoryError`, `Failed to save chunk`, `Failed to load
chunk` or `Error upgrading chunk` signature. No instance debug directory was
produced. It retains an ItemStack error at 19:44:37: `Tried to load invalid item`,
with the detail `Item must not be minecraft:air`. This raw error is not erased;
the density measurement does not establish loot correctness. Other raw warnings
remain retained. Lifecycle success is not census acceptance.

## Raw custody

The stopped-world backup preserves 501 files totaling 404,326,401 bytes.
`world.tar.gz` is 140,502,119 bytes, SHA-256
`aedf8edd5b63c212c0c4f6e70d51a2878273fed50ea011f162ecf5ef26804ad5`.
The [world restore](world-restore.json) verifies all 501 files in a fresh target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-biome-diverse-r1-without-sparse-44212515)
contains the raw archive and [manifest](archive-manifest.json), with its fetched
tag matching the generation source. The archive is 141,146,945 bytes, SHA-256
`23f75374c6c560144419064cfb411a90821b74efc4caf4ad9f3c588e30b9c1f5`.
Its 313 files total 170,567,537 uncompressed bytes. Manifest SHA-256:
`da31522b6825a18a73ad7ed60a005cc257e0e30da9563db28a1214d95e259bb6`.
[Local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members. The downloaded manifest is byte-identical.

## Reproduction and census

Reuse the [existing custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this world's name, source, archive and world hash. Generation used:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-biome-diverse-r1-without-sparse --mode probe --preset item10 --role biome-diverse --arm without-sparse --repetition 1
```

The census uses the verified restored world and source `44212515`, including
existing biome-comparison processing. Create the analysis parent directory first
and require the output to be absent:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-biome-diverse-r1-without-sparse-custody/restored-world/world evidence/raw/item10/full-biome-diverse-r1-without-sparse-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-biome-diverse-r1-without-sparse-custody/restored-local --trace-manifest evidence/item-10/full-biome-diverse-r1-without-sparse/archive-manifest.json
```

Timing and diagnostics are retained in the analysis directory's
`all-strata-runtime.txt`. Census session 84601 ended with exit 0 in 597.674 seconds.
The output is 122,228,779 bytes, SHA-256
`3be8f73edcde284032686ed32910cd22154897e6b44fbdcaa30bc1229749c4c9`.
All eleven strata contain exactly 4,096 full selected chunks. Fifty incoming
target classes pass complete observer coverage and trace validation.


## Saved-content exclusions and biome limits

Six Overworld `supplementaries:cave_urn_cache` candidates remain excluded as
CONTENT_NOT_PRESERVED. All seven inspected content positions are in full saved
chunks. The raw constructive observations remain preserved; the later writer is
UNKNOWN. No overlap pairs occur.

| Candidate | Attempt | Content position | Saved block |
| ---: | ---: | --- | --- |
| 12995 | 24651 | (-400,-10,107) | minecraft:polished_tuff |
| 13885 | 24572 | (-434,-16,98) | minecraft:air |
| 16700 | 22287 | (-63,-37,-158), (-59,-37,-156) | minecraft:air at both |
| 21261 | 10710 | (225,28,-370) | minecraft:smooth_basalt |
| 23936 | 11390 | (30,-22,-347) | minecraft:waxed_oxidized_copper_grate |
| 28233 | 15287 | (473,-45,-348) | minecraft:calcite |

Biome rows plus unavailable anchors conserve every stratum's accepted location
count. The central-End arena is the sole unavailable biome anchor. Urn candidate
28296, attempt 6179, at (476,24,354), has observed `terralith:desert_canyon` biome
at quart height 6 but zero sampled chunk-center exposure in that band. Its count
remains one and its rate null. It is not discarded or assigned another denominator.

## Accepted counts and limitations

Rates use count times 1,000 / 4,096 within each stratum. Raw output retains all
category densities, spatial observations, censoring and separate biome bands.

| Stratum | Raw registry starts | All locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Aether | 126 | 8 | 0 | 0 | 0 | 8 | 0 | 0 | 0 |
| Earth orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mars orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Moon orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Moon | 54 | 54 | 54 | 0 | 0 | 0 | 0 | 0 | 0 |
| Venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Overworld | 128 | 4227 | 74 | 19 | 4119 | 15 | 0 | 0 | 4 |
| Central End | 9 | 11 | 10 | 0 | 0 | 0 | 0 | 1 | 0 |
| Outer End | 41 | 48 | 42 | 0 | 2 | 2 | 2 | 0 | 0 |
| Nether | 179 | 597 | 141 | 0 | 442 | 9 | 5 | 0 | 0 |

Aether's 118 cloud starts remain excluded terrain. The observer records 33,086
calls and 32,777 grouped candidates: 25,388 NO_CONSTRUCTIVE_CONTENT, 2,857
OUTSIDE_FRAME, 4,526 OBSERVED_LOCATION and six CONTENT_NOT_PRESERVED.

This completes the sixth matched pair and thirteenth planned cell. The matched
baseline has six Overworld T2 dungeons and one village; this control has fifteen
and four. T2 nearest-observed mean is 139.29447166395042 blocks; the uncensored
mean remains null. Dispersion is 0.8625 and the largest empty full-cell rectangle
is 768 chunks, bounds [-32,15,-16,-1]. These are fixed-window observations under
the declared observer, not observed fights, exploration pacing, loot correctness
or proof of observer-free equivalence. The second repetition remains outstanding.
