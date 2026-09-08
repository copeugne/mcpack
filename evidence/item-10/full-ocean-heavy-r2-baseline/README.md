# Ocean-heavy repetition-2 baseline

Status: GENERATION AND RAW CUSTODY PASS; CENSUS IN PROGRESS.
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
`all-strata-runtime.txt`. No census result is accepted at this checkpoint.
