# Ocean-heavy repetition-2 control, attempt 2

Status: GENERATION, CONFIGURATION AND RAW CUSTODY PASS.
Census acceptance remains pending. Protocol: `item10-full-v1`, observer coverage
`item10-observer-coverage-v2`, post-failure amendment `item10-retry-policy-v1`.
Seed: `95920844204830198`. Source: `ffa51fb9981c438b802f5ae28e4796750636d5da`.

This is the single predeclared fresh retry of the
[retained failed attempt](../full-ocean-heavy-r2-without-sparse/README.md).
Its success does not erase that failure or identify the allocation that caused it.
The original instance and raw evidence remain at their original paths.

The unchanged [run receipt](run.json) explicitly records attempt 2. All eleven
selections, readiness, correlated save flush and clean stop pass, with Java exit
0 and no process-group kill or rejection. Duration: 549.011 seconds. All 228
frozen files and eleven Chunky paths pass configuration capture. No fixtures,
before-generation commands or configuration tuning were used. The heap-failure
shutdown path was not triggered; no `chunky pause` command was issued.

Direct comparison with the [first control](../full-ocean-heavy-r1-without-sparse/run.json)
finds identical `run.preflight`, `probe` and lifecycle `selections`. The observer
source and JAR remain frozen, and the runtime is the unchanged omit-only-Sparse
Structures control. The console contains no `OutOfMemoryError`, `Failed to load
chunk` or `Error upgrading chunk` signatures. Other raw warnings remain retained;
this is not performance, loot or observed-gameplay acceptance.

## Raw custody

The stopped world backup contains 502 files totaling 434,642,367 bytes.
`world.tar.gz` is 168,099,314 bytes, SHA-256
`7ac74bc1560d2baf3386d2cb4d76486290dd603b3a0fee83c08e0ad47e7af0ae`.
The [world restore](world-restore.json) verifies all 502 files in a new target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ocean-heavy-r2-without-sparse-attempt2-ffa51fb9)
contains the raw archive and [manifest](archive-manifest.json). Its fetched tag
resolves to the source above. Archive size: 168,492,818 bytes; SHA-256
`9ffb3fc05d75e6b84807913ca6c5061c3ccd1a1897ec3282fc914f00ed0a5f7b`.
Its 313 files total 192,219,554 bytes before compression. Manifest SHA-256:
`1138d6b8d0096546e654d5ed85bb95333da71665eaa70c4c62e6032d0be5c6a3`.
The [local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members; the downloaded manifest is byte-identical.
Fifty incoming target classes are preserved; complete trace acceptance awaits
analysis. The failed first attempt retains its separate immutable archive.

## Reproduction

Use the [existing custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this attempt's name, source, archive and world hash. Create output parents
first; every output must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ocean-heavy-r2-without-sparse-attempt2 --mode probe --preset item10 --role ocean-heavy --arm without-sparse --repetition 2 --attempt 2
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ocean-heavy-r2-without-sparse-attempt2 --archive evidence/raw/item10/item10-full-ocean-heavy-r2-without-sparse-attempt2-ffa51fb9.tar.gz --manifest evidence/item-10/full-ocean-heavy-r2-without-sparse-attempt2/archive-manifest.json --revision ffa51fb9981c438b802f5ae28e4796750636d5da
```

The census is running as session `98243`, with the unchanged census implementation
last modified at `760aa2f5`. Executed command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ocean-heavy-r2-without-sparse-attempt2-custody/restored-world/world evidence/raw/item10/full-ocean-heavy-r2-without-sparse-attempt2-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ocean-heavy-r2-without-sparse-attempt2-custody/restored-local --trace-manifest evidence/item-10/full-ocean-heavy-r2-without-sparse-attempt2/archive-manifest.json
```

Timing and diagnostics are retained beside the output in `all-strata-runtime.txt`.
Ten planned cells remain accepted until this census passes. The total attempted
world count includes the failed first attempt; it is never a zero-density result.
