# Mountainous repetition-1 Sparse Structures control

Status: GENERATION, CONFIGURATION AND RAW CUSTODY PASS.
Census acceptance remains pending. Protocol: `item10-full-v1`, with
`item10-observer-coverage-v2`. Seed: `6671238423019257953`.
Generation source: `3fa7f3117d0f9a5fff3fb4545a4fe51144b16dfa`.

The unchanged [run receipt](run.json) records all eleven selections completed,
readiness, correlated save flush, clean stop, Java exit 0 and no process-group
kill or rejection. Duration: 666.194 seconds. All 228 frozen files and eleven
declared Chunky files pass capture.

Direct comparison with the [matched baseline](../full-mountainous-r1-baseline/run.json)
finds identical `probe` and lifecycle `selections`. `run.preflight` differs only
in `instrumented_candidate_count` (137 to 136), `sparse_structures_omitted`
(false to true) and `instrumented_runtime_sha256` (baseline to the frozen
`84a884f99e4ac48defb9ea0b2c9e45bf3d0f4f6e881a4be4d8968dc2be14d4da` control).
No fixture or before-generation commands were used. Collection runs in probe
mode, with the same frozen observer, not the legacy unobserved control mode.

## Raw custody

The stopped world backup contains 501 files totaling 446,862,457 bytes.
`world.tar.gz` is 182,141,550 bytes, SHA-256
`8c9f214680935a4e3370e4e435ef409ed8774c1c526770f266850995f3958a88`.
The [world restore](world-restore.json) verifies all 501 files in a new target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-mountainous-r1-without-sparse-3fa7f311)
contains the raw archive and [manifest](archive-manifest.json). The fetched tag
resolves to the generation source above. Archive size: 182,743,035 bytes;
SHA-256 `8da0f327a407250cc9ac57eaaacb50f0ca6a28c80b9e26c03528869068aee776`.
Its 313 files total 211,519,630 bytes before compression. Manifest SHA-256:
`c1bdd51b6a8d8574c01005cd5b91e5c4c0a6e74c7e80a9b814e43059c5997f3f`.
The [local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members; the downloaded manifest matches byte-for-byte.
The archive includes
50 incoming target classes; their full trace validation still awaits the census.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this run's name, source, archive and world hash. Create output parents first;
each output must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-mountainous-r1-without-sparse --mode probe --preset item10 --role mountainous --arm without-sparse --repetition 1
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-mountainous-r1-without-sparse --archive evidence/raw/item10/item10-full-mountainous-r1-without-sparse-3fa7f311.tar.gz --manifest evidence/item-10/full-mountainous-r1-without-sparse/archive-manifest.json --revision 3fa7f3117d0f9a5fff3fb4545a4fe51144b16dfa
```

Raw observations and existing diagnostics remain unchanged. Generation and raw
custody do not establish density, gameplay, or Item 10 completion.

The full census is running as session `61273`, using analysis implementation
`760aa2f5`. Executed command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-mountainous-r1-without-sparse-custody/restored-world/world evidence/raw/item10/full-mountainous-r1-without-sparse-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-mountainous-r1-without-sparse-custody/restored-local --trace-manifest evidence/item-10/full-mountainous-r1-without-sparse/archive-manifest.json
```

Timing and diagnostics are retained beside the output in `all-strata-runtime.txt`.
