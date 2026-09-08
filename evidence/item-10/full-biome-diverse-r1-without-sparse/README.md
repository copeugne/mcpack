# Biome-diverse repetition-1 control

Status: GENERATION AND RAW CUSTODY PASS; CENSUS IN PROGRESS.
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
`all-strata-runtime.txt`. No census result is accepted at this checkpoint.
