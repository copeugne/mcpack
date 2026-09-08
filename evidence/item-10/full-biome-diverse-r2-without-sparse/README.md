# Biome-diverse repetition-2 control

Status: GENERATION AND RAW CUSTODY PASS; CENSUS IN PROGRESS.
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
Census acceptance is pending. Generation completion alone does not close this world.
