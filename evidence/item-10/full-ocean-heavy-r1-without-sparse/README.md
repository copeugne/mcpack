# Ocean-heavy repetition-1 control

Status: GENERATION, CONFIGURATION AND RAW CUSTODY PASS.
Census acceptance remains pending. Protocol: `item10-full-v1`, with
`item10-observer-coverage-v2`. Seed: `95920844204830198`.
Generation source: `6142e94b159a18ab68747b81a9daef206652cf7d`.

The unchanged [run receipt](run.json) records all eleven selections completed,
readiness, correlated save flush, clean stop, Java exit 0 and no process-group
kill or rejection. Duration: 553.698 seconds. All 228 frozen files and eleven
declared Chunky files pass capture. No fixture or before-generation commands
were used. No configuration tuning was performed.

Direct comparison with the [matched baseline](../full-ocean-heavy-r1-baseline/run.json)
finds identical `probe` and lifecycle `selections`. `run.preflight` differs only
in instrumented candidate count (137 to 136), Sparse Structures omission (false
to true), and instrumented runtime digest. The deployed control digest is
`84a884f99e4ac48defb9ea0b2c9e45bf3d0f4f6e881a4be4d8968dc2be14d4da`,
matching the [declared control](../protocol.md#sparse-structures-control-contrast).
Generation is not observed gameplay or performance acceptance.

## Raw custody

The stopped world backup contains 502 files totaling 432,430,406 bytes.
`world.tar.gz` is 166,275,156 bytes, SHA-256
`aaf5286b73e4dfedd2938c8ab3d38a074e51bae9fc9038f70226e17a3b454b53`.
The [world restore](world-restore.json) verifies all 502 files in a new target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ocean-heavy-r1-without-sparse-6142e94b)
contains the raw archive and [manifest](archive-manifest.json). Its fetched tag
resolves to the generation source above. Archive size: 166,700,311 bytes;
SHA-256 `84d9341131df973c32d42d38056f270e76415ee260ef52ceb2d63b140152d0b3`.
Its 313 files total 191,505,513 bytes before compression. Manifest SHA-256:
`c269147861e4042f419a5eaffa08be413b85a03ebc36859b6e133620f002c996`.
The [local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members, and the downloaded manifest matches byte-for-byte.
There are 50 incoming target classes; complete trace acceptance awaits census
analysis. Raw observations and diagnostics remain unchanged.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this run's name, source, archive and world hash. Create output parents first;
each output must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ocean-heavy-r1-without-sparse --mode probe --preset item10 --role ocean-heavy --arm without-sparse --repetition 1
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ocean-heavy-r1-without-sparse --archive evidence/raw/item10/item10-full-ocean-heavy-r1-without-sparse-6142e94b.tar.gz --manifest evidence/item-10/full-ocean-heavy-r1-without-sparse/archive-manifest.json --revision 6142e94b159a18ab68747b81a9daef206652cf7d
```

The census is running as session `89527`, using analysis implementation
`760aa2f5`. Executed command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ocean-heavy-r1-without-sparse-custody/restored-world/world evidence/raw/item10/full-ocean-heavy-r1-without-sparse-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ocean-heavy-r1-without-sparse-custody/restored-local --trace-manifest evidence/item-10/full-ocean-heavy-r1-without-sparse/archive-manifest.json
```

Timing and diagnostics are retained beside the output in `all-strata-runtime.txt`.
Generation and raw custody do not establish density or Item 10 completion.
