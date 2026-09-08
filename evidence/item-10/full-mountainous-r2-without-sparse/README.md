# Mountainous repetition-2 Sparse Structures control

Status: GENERATION, CONFIGURATION AND RAW CUSTODY PASS.
Census acceptance remains pending. Protocol: `item10-full-v1`, with
`item10-observer-coverage-v2`. Seed: `6671238423019257953`.
Generation source: `1632e3de907f7c2c63a48677926ffe0de71324b2`.

The unchanged [run receipt](run.json) records all eleven selections completed,
readiness, correlated save flush, clean stop, Java exit 0 and no process-group
kill or rejection. Duration: 663.491 seconds. All 228 frozen files and eleven
declared Chunky files pass capture. No fixture or before-generation commands
were used. Both arms use probe mode with the frozen observer.

Direct comparison with the [first control](../full-mountainous-r1-without-sparse/run.json)
finds identical `run.preflight`, `probe` and lifecycle `selections`; only the
repetition and fresh instance change. This reuses the same exact Sparse Structures
omission, seed, configuration and sampling identity rather than tuning the control.

## Raw custody

The stopped world backup contains 501 files totaling 444,441,718 bytes.
`world.tar.gz` is 179,912,028 bytes, SHA-256
`d51f2724b033e788becb2a4b04f93c96bab53384c3afed0df9eb3ae58783a760`.
The [world restore](world-restore.json) verifies all 501 files in a new target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-mountainous-r2-without-sparse-1632e3de)
contains the raw archive and [manifest](archive-manifest.json). The fetched tag
resolves to the generation source above. Archive size: 180,748,230 bytes;
SHA-256 `2587ce92a4153006394c7350a5d4137bd1d51fc4a6d4ea79ef8c0be3fd22ad73`.
Its 313 files total 218,269,209 bytes before compression. Manifest SHA-256:
`fb689f40dc8a5651e99afd6e78e83b41a1bea723bedb8b64aaa094ac3a021cd5`.
The [local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members; downloaded and local manifests match byte-for-byte. There are 50
incoming target classes; complete trace acceptance still awaits census analysis.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this run's name, source, archive and world hash. Create output parents first;
each output must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-mountainous-r2-without-sparse --mode probe --preset item10 --role mountainous --arm without-sparse --repetition 2
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-mountainous-r2-without-sparse --archive evidence/raw/item10/item10-full-mountainous-r2-without-sparse-1632e3de.tar.gz --manifest evidence/item-10/full-mountainous-r2-without-sparse/archive-manifest.json --revision 1632e3de907f7c2c63a48677926ffe0de71324b2
```

Raw observations and existing diagnostics remain unchanged. Generation and raw
custody do not establish density, gameplay, or Item 10 completion.

The full census is running as session `95707`, using analysis implementation
`760aa2f5`. Executed command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-mountainous-r2-without-sparse-custody/restored-world/world evidence/raw/item10/full-mountainous-r2-without-sparse-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-mountainous-r2-without-sparse-custody/restored-local --trace-manifest evidence/item-10/full-mountainous-r2-without-sparse/archive-manifest.json
```

Timing and diagnostics are retained beside the output in `all-strata-runtime.txt`.
