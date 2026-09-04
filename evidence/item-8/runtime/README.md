# Frozen registry capture

`registry-r1/capture.json` and its seven dump files are the unmodified output of
`tools.run_item8_registry` at source revision
`367ba59d097fc3fe3284adb36cb4536bbc583663`. The receipt identifies the runtime,
configuration parity result, command sequence, and individual dump hashes.
Registry keys are not canonical families and do not prove actual placement.

The original command from the repository root was:

```sh
uv run -m tools.run_item8_registry \
  --pristine instances/pristine-baseline-v0 \
  --java-home downloads/item2/temurin/extracted/jdk-21.0.12.1+1 \
  --target instances/item8/registry-r1 \
  --output evidence/raw/item8/registry-r1 \
  --timeout-seconds 900
```

Use new target and output paths for any reproduction. The original source used a
120-second clean-exit deadline. Later source exposes the same default through
`--exit-timeout-seconds 120`; it does not alter the original receipt retroactively.
Readiness, all seven dump responses, correlated flush, and clean exit were
observed by the capture harness. Full console, latest and debug logs and captured
configuration are durably archived with the complete capture directory. See
`../raw-custody/README.md` for the published archive, manifest and verified
downloaded restore. Preservation does not by itself pass Item 8's gameplay gate.

## Pack and dimension context

`registry-r1/world-context.json` projects `DataVersion`, `Version`, `DataPacks`
and `WorldGenSettings` from the stopped registry instance. It excludes players
and unrelated world metadata. The full generator settings are retained for
source-backed dimension and biome analysis. Its SHA-256 is
`0615a2dcdeb2120a467648df95f69aa9f1ef53e8989ae8c2191028d6f5c1aca2`.

Source `level.dat` is preserved outside ordinary Git at
`evidence/raw/item8/registry-r1/world-metadata/level.dat`, SHA-256
`a867acca9a8970df7e8e474ef4011ad034e7e829785a037fc7a3812798b2be0e`.
It was copied byte-for-byte from the stopped instance and checked with `cmp`.
Durable raw custody is recorded together with the logs and configuration in
`../raw-custody/README.md`.
Reproduce the projection using source `628ba37` or its unchanged successor:

```sh
uv run -m tools.extract_item8_world_context --level evidence/raw/item8/registry-r1/world-metadata/level.dat --output evidence/raw/item8/world-context-reproduction.json
cmp evidence/item-8/runtime/registry-r1/world-context.json evidence/raw/item8/world-context-reproduction.json
```

The metadata records `mod_data` after `vanilla` in the enabled-pack list. Preserve
that order when assessing overrides. The projection is source context, not proof
of every resource's effective value, observed structure placement or Item 8
completion.
