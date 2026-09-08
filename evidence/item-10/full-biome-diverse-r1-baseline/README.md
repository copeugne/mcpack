# Biome-diverse repetition-1 baseline

Status: GENERATION AND RAW CUSTODY PASS; CENSUS IN PROGRESS.
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
`all-strata-runtime.txt`. No census result is accepted at this checkpoint.
