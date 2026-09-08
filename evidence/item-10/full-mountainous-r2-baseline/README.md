# Mountainous repetition-2 baseline

Status: GENERATION, CONFIGURATION AND RAW CUSTODY PASS.
Census acceptance remains pending. Protocol: `item10-full-v1`, with
`item10-observer-coverage-v2`. Seed: `6671238423019257953`.
Generation source: `b6df88877b7248f900ed3e40e3bf73a53183bc82`.

The unchanged [run receipt](run.json) records all eleven selections completed,
readiness, correlated save flush, clean stop, Java exit 0 and no process-group
kill or rejection. Duration: 618.366 seconds. All 228 frozen files and eleven
declared Chunky files pass capture. No fixture or before-generation commands
were used. The raw console retains generation-load warnings, including
"Can't keep up" messages; successful lifecycle checks are not a performance pass.

Direct comparison with the [first baseline](../full-mountainous-r1-baseline/run.json)
finds identical `run.preflight`, `probe` and lifecycle `selections`; this is a
fresh independent repetition under the same frozen sampling and runtime identity.
No configuration tuning was performed.

## Raw custody

The stopped world backup contains 501 files totaling 438,725,769 bytes.
`world.tar.gz` is 173,030,403 bytes, SHA-256
`8f22ac215a520998dacf606a3d774b1cc4ce96bc4323e82d0d26e0ca043fbd5b`.
The [world restore](world-restore.json) verifies all 501 files in a new target.

The raw archive and [manifest](archive-manifest.json) use immutable name
`item10-full-mountainous-r2-baseline-b6df8887.tar.gz`. Archive size: 173,830,470 bytes;
SHA-256 `f800636027c80823a0dab98916712731792dd4f85f9cdcd00eff7213814a8064`.
Its 313 files total 211,482,822 bytes before compression. Manifest SHA-256:
`d334938f7d8a01f0253b588bd2805b42ef38241c416f064c3c0b0b8b301df881`.
The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-mountainous-r2-baseline-b6df8887)
contains both files; its fetched tag resolves to the exact generation source.
The [local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members, and the downloaded manifest matches byte-for-byte. There are 50
incoming target classes; complete trace acceptance still awaits census analysis.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this run's name, source, archive and world hash. Create output parents first;
each output must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-mountainous-r2-baseline --mode probe --preset item10 --role mountainous --arm baseline --repetition 2
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-mountainous-r2-baseline --archive evidence/raw/item10/item10-full-mountainous-r2-baseline-b6df8887.tar.gz --manifest evidence/item-10/full-mountainous-r2-baseline/archive-manifest.json --revision b6df88877b7248f900ed3e40e3bf73a53183bc82
```

Raw observations and existing diagnostics remain unchanged. Generation and raw
custody do not establish density, gameplay, or Item 10 completion.

The full census is running as session `50314`, using analysis implementation
`760aa2f5`. Executed command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-mountainous-r2-baseline-custody/restored-world/world evidence/raw/item10/full-mountainous-r2-baseline-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-mountainous-r2-baseline-custody/restored-local --trace-manifest evidence/item-10/full-mountainous-r2-baseline/archive-manifest.json
```

Timing and diagnostics are retained beside the output in `all-strata-runtime.txt`.
