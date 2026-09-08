# Biome-diverse repetition-2 baseline

Status: GENERATION AND RAW CUSTODY PASS; CENSUS IN PROGRESS.
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
Census acceptance is pending.
