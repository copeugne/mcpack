# Ocean-heavy repetition-1 baseline

Status: GENERATION, CONFIGURATION AND RAW CUSTODY PASS.
Census acceptance remains pending. Protocol: `item10-full-v1`, with
`item10-observer-coverage-v2`. Seed: `95920844204830198`.
Generation source: `5367d2dd664311033b57da448d0fc4a781ca0e8c`.

The unchanged [run receipt](run.json) records all eleven selections completed,
readiness, correlated save flush, clean stop, Java exit 0 and no process-group
kill or rejection. Duration: 512.546 seconds. All 228 frozen files and eleven
declared Chunky files pass capture. No fixture or before-generation commands
were used. No configuration tuning was performed.

Direct comparison with the [preceding baseline](../full-mountainous-r2-baseline/run.json)
finds identical `probe` and lifecycle `selections`. `run.preflight` differs only
in the declared `seed` and `seed_role`, preserving exact runtime/configuration
identity across these seed blocks. Generation is not observed gameplay validation.

## Raw custody

The stopped world backup contains 502 files totaling 425,870,731 bytes.
`world.tar.gz` is 159,097,965 bytes, SHA-256
`500ea7c8f66cbdf42913fece569adcb486e35b554962cf5bd43d759aeebb6ff0`.
The [world restore](world-restore.json) verifies all 502 files in a new target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ocean-heavy-r1-baseline-5367d2dd)
contains the raw archive and [manifest](archive-manifest.json). Its fetched tag
resolves to the generation source above. Archive size: 159,477,835 bytes;
SHA-256 `055608001b2b17a070a41ae8622f4cfd2ff1ce37f34094f94524bb2611c26b71`.
Its 313 files total 183,094,130 bytes before compression. Manifest SHA-256:
`ec89d0df58d22b96576453d410774b4976cee5b0f896ffca82f23c513f078d7d`.
The [local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members, and the downloaded manifest matches byte-for-byte. There are 50
incoming target classes; complete trace acceptance still awaits census analysis.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this run's name, source, archive and world hash. Create output parents first;
each output must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ocean-heavy-r1-baseline --mode probe --preset item10 --role ocean-heavy --arm baseline --repetition 1
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ocean-heavy-r1-baseline --archive evidence/raw/item10/item10-full-ocean-heavy-r1-baseline-5367d2dd.tar.gz --manifest evidence/item-10/full-ocean-heavy-r1-baseline/archive-manifest.json --revision 5367d2dd664311033b57da448d0fc4a781ca0e8c
```

Raw observations and existing diagnostics remain unchanged. Generation and raw
custody do not establish density, gameplay, or Item 10 completion.

The full census is running as session `96485`, using analysis implementation
`760aa2f5`. Executed command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ocean-heavy-r1-baseline-custody/restored-world/world evidence/raw/item10/full-ocean-heavy-r1-baseline-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ocean-heavy-r1-baseline-custody/restored-local --trace-manifest evidence/item-10/full-ocean-heavy-r1-baseline/archive-manifest.json
```

Timing and diagnostics are retained beside the output in `all-strata-runtime.txt`.
