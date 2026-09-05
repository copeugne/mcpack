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

## Live dimension biome membership

`77b6eec` delivers the successful `dimension-r3` capture and preserves rejected
`dimension-r1` and `dimension-r2` receipts. `cd04324` checks the result against
the original registry capture and saved dimension identities. Runtime source
revision: `428819f66598777ec0d39d05a3503ec07a5769b5`.
Output SHA: `08fa8185cd2c3f54b5255b2e8f86946c4b37ed471fb1991d0f82c835ffe20c7c`.

This additional read is necessary for Item 8's dimension attribute: saved
Lithostitched delegates omit runtime injected/replaced lists, and NeoForge's
existing dump exports keys only. The source proof is retained under
`../sources/lithostitched-biome-injector-code` and `../sources/neoforge-dump-command-code`.
The probe reuses frozen materialization, readiness, registry dumps, configuration
comparison and correlated shutdown. It adds no mod to the retained 136, installs
no class transformers and does not write to the world. It attaches to the exact
launched PID, submits the read to the server thread, and records only dimension
and possible-biome IDs. The task has a 30-second deadline and attachment a
45-second deadline. This is membership, not measured biome frequency, performance
or proof that any structure passes its placement conditions.

The build uses the pinned JDK, an explicit classpath and a fixed JAR timestamp.
The capture records source, manifest and built-JAR hashes. An initial standalone
compilation failed because the host CLASSPATH contained a malformed path; the
explicit classpath removed that environmental dependency. Scoped Python checks
initially found formatting, annotation and complexity issues, resolved without
adding a second lifecycle or build framework.

```sh
uv run -m tools.run_item8_registry --pristine instances/pristine-baseline-v0 --java-home downloads/item2/temurin/extracted/jdk-21.0.12.1+1 --target instances/item8/dimension-r1 --output evidence/raw/item8/dimension-r1 --timeout-seconds 900 --dimension-biomes
uv run -m tools.run_item8_registry --pristine instances/pristine-baseline-v0 --java-home downloads/item2/temurin/extracted/jdk-21.0.12.1+1 --target instances/item8/dimension-r2 --output evidence/raw/item8/dimension-r2 --timeout-seconds 900 --dimension-biomes
uv run -m tools.run_item8_registry --pristine instances/pristine-baseline-v0 --java-home downloads/item2/temurin/extracted/jdk-21.0.12.1+1 --target instances/item8/dimension-r3 --output evidence/raw/item8/dimension-r3 --timeout-seconds 900 --dimension-biomes
uv run pytest -q tests/item8/test_registry.py tests/item8/test_registry_runner.py
uv run pytest -q tests/item8/test_dimension_capture.py
uv run ruff check src/mcpack_evidence/item8_registry.py tools/run_item8_registry.py tests/item8/test_registry.py tests/item8/test_dimension_capture.py
uv run basedpyright src/mcpack_evidence/item8_registry.py tools/run_item8_registry.py tests/item8/test_registry.py tests/item8/test_dimension_capture.py
```

Use fresh target and output paths for reproduction. r1 at `66b32d3` rejected
agent initialization and killed the process group. Its console omitted queued
failure diagnostics; that missing tail is not reconstructed. Fix `d4e107d`
retains queued diagnostics, and r2 at that revision exposed the actual error:
subclass reflection attempted to resolve an unrelated client-only Screen method.
Fix `428819f` invokes possibleBiomes through the public BiomeSource base class,
avoiding unrelated subclass signatures while preserving virtual dispatch.
r3 is the successful live regression. Both rejected attempts remain rejected.

All 20 lifecycle/runner tests and the focused capture test passed; scoped quality
checks passed. r3 preflight and all seven registry records exactly equal the
original capture. The configuration comparison passed with only its permitted
comment-line differences. Readiness, correlated flush, clean exit and no process
group kill are recorded. All ten expected dimensions are present, every reported
biome is registered, and each membership list is sorted and unique.

Membership counts: Aether 13, Overworld 272, End 29, Nether 14, Mars 2, Moon 2,
Venus 2, and each of the three orbit dimensions 1. The Aether's saved biome-source
list names only four distinct biomes, illustrating why that list was insufficient.
These counts are not frequencies or extra structure families. The raw logs,
probe artifacts, rejected attempts and sanitized configuration have local and
download-tested remote custody in `../raw-custody/README.md`.

Next join this membership evidence to existing per-root biome constraints in the
inventory. Keep unresolved constraints and placement conditions explicit. Do not
repeat this successful capture solely for reassurance or mark Item 8 complete.
