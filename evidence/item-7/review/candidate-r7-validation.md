# Item 7 r7 candidate validation

## Bound evidence

- Archive source revision: `ca646c19ad772bd6de6a47f4dcb0fc5dc4b5cbfc`.
- Annotated tag object: `3374ff7ce183d9cb9dd2636e206abec68db3f220`.
- Release: `https://github.com/copeugne/mcpack/releases/tag/item-7-raw-evidence-2026-09-04-r7`.
- World archive inventory SHA-256: `e539dff84ad636f80a9aeaaa9b94febe8b5f1e0e35d9c00af170862f0c00fa99`, 716 files.
- Completion SHA-256: `6bb509d87a215a67186fa70f285b59e6986d813c7c21f9ab19e8479ea078515c`, 125 artifacts, `PASS`.

All four archives were rebuilt from the verified r4 restore with the tracked implementation at the tagged source revision. Their payload hashes are byte-identical to r4. Each archive restored into an absent target with the corrected descriptor-bound target and receipt publication path. The tracked repository-bound verifier downloaded all four assets twice and matched their sizes and SHA-256 values.

The world archive inventory was rebuilt from the r7 restored Run A, Run B, and auxiliary trees. The completion receipt was built twice from the r7 restored core plus the tracked r7 manifests, restore receipts, publication receipt, and world inventory. Both completion outputs were byte-identical.

The canonical completion invocation uses:

- `--raw-root /home/lonestar/Desktop/Projects/mcpack-item7-r7-delivery/restored/core`;
- `--visual-manifest /home/lonestar/Desktop/Projects/mcpack-item7-r7-delivery/restored/core/visual-qa/captures/capture-manifest.tsv`;
- the tracked protocol, provider catalog, biome-restriction audit, and visual review receipts under `evidence/item-7/`;
- provider, repeat, warning, control, run, gap, analysis, and capture inputs under the restored r7 core;
- `evidence/item-7/world-archive-inventory.json`;
- all four manifests and restore receipts under `evidence/item-7/archive/r7/`;
- `evidence/item-7/archive/r7/publication.json`.

The older mutable `/tmp/mcpack-item7-raw-20260904` tree is not an accepted completion input. A rejected QA attempt used that tree and correctly failed on three stale capture identities. The accepted r7 restored core contains capture manifest SHA-256 `219e17ed50b6e5b919c16a2b5bef34b7820b251c7272074d5df91c5123260f91`, which matches both accepted visual review receipts.

## Worktree validation

- `uv run pytest -q tests/item7`: 182 passed.
- `uv run pytest -q`: 863 passed.
- Scoped Ruff formatting: passed across 101 files.
- Scoped Ruff checks: passed.
- Scoped basedpyright: 0 errors, 0 warnings, 0 notes.
- Item 7 shell syntax: passed.
- `git diff --check`: passed.

## Clean export validation

Reconciled candidate `dc4e10bf5a4d686d3b4040548cf3d303c01dfd5c` was exported with `git archive` into `/tmp/mcpack-item7-clean-dc4e10b`. The first combined invocation tried to start with that not-yet-created path as its working directory and failed before creating a process or writing evidence. The corrected invocation created the export from the repository and then ran every check from the export.

- Item 7 tests: 182 passed.
- Repository tests: 863 passed.
- Scoped Ruff formatting and checks: passed across 101 files.
- Scoped basedpyright: 0 errors, 0 warnings, 0 notes.
- Item 7 shell syntax: passed.
- The tracked world inventory builder rehashed all 716 r7 restored world files and reproduced the committed inventory byte for byte.
- The tracked completion builder used the r7 restored core and reproduced the committed 125-artifact `PASS` receipt byte for byte.

The validation-record commit changes only documentation and evidence records. Fresh exact-SHA review lanes and a runtime audit must bind the resulting commit before push.
