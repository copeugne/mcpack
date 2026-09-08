# Ocean-heavy repetition-2 control, final authorized retry

Status: GENERATION AND RAW CUSTODY PASS; CENSUS IN PROGRESS.
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
Census acceptance is pending; do not count this as the sixteenth complete world yet.
