# Item 7 r8 candidate validation

## Bound evidence

- Archive source revision: `85efc96b5f1c2d3518a594905a65a2777d904b4b`.
- Annotated tag object: `7bd8dad5c4ae4baec9eddc767c96aac7d05b30af`.
- Release: `https://github.com/copeugne/mcpack/releases/tag/item-7-raw-evidence-2026-09-04-r8`.
- World archive inventory SHA-256: `331bde517e6fb072a4aa0a66fb77b733559b27f92098f8fc1f236405bbe02f3e`, 716 files.
- Completion SHA-256: `c369178431abba0c17404b9723a47fa66e945c305b5477c63bd5a9a6ec281582`, 125 artifacts, `PASS`.

All four archives were rebuilt from the verified r7 restore with the tracked implementation at the tagged source revision. Their payload hashes are byte-identical to r7. Each archive restored into an absent target after its output parents were safely opened without following symlinks. The tracked repository-bound verifier downloaded all four assets twice to distinct disk-backed directories and matched their sizes and SHA-256 values.

The first download attempt used `/tmp/mcpack-item7-r8-release-download-1` and failed with `disk quota exceeded` before verification completed. That incomplete directory was removed. It is not acceptance evidence and is not counted among the two successful downloads.

The two successful verification commands were:

```sh
tools/verify_item7_release.sh copeugne/mcpack item-7-raw-evidence-2026-09-04-r8 evidence/item-7/archive/r8 evidence/item-7/archive/r8/publication.json /home/lonestar/Desktop/Projects/mcpack-item7-r8-release-download-1
tools/verify_item7_release.sh copeugne/mcpack item-7-raw-evidence-2026-09-04-r8 evidence/item-7/archive/r8 evidence/item-7/archive/r8/publication.json /home/lonestar/Desktop/Projects/mcpack-item7-r8-release-download-2
```

## Exact inventory rebuild

From the repository root, the exact world archive inventory rebuild and comparison invocation is:

```sh
uv run python tools/build_item7_world_archive_inventory.py \
  --run-a /tmp/mcpack-item7-r8-delivery/restored/run-a \
  --run-a-archive-name mcpack-item7-raw-run-a-worlds-r8.tar.gz \
  --run-b /tmp/mcpack-item7-r8-delivery/restored/run-b \
  --run-b-archive-name mcpack-item7-raw-run-b-worlds-r8.tar.gz \
  --auxiliary /tmp/mcpack-item7-r8-delivery/restored/auxiliary \
  --auxiliary-archive-name mcpack-item7-raw-auxiliary-worlds-r8.tar.gz \
  --output /tmp/item7-world-inventory-r8-rebuilt.json
cmp evidence/item-7/world-archive-inventory.json /tmp/item7-world-inventory-r8-rebuilt.json
sha256sum evidence/item-7/world-archive-inventory.json /tmp/item7-world-inventory-r8-rebuilt.json
```

## Exact completion rebuild

From the repository root, the exact completion rebuild and comparison invocation is:

```sh
uv run python tools/build_item7_completion.py \
  --raw-root /tmp/mcpack-item7-r8-delivery/restored/core \
  --protocol evidence/item-7/protocol/worldgen-audit-v1.json \
  --provider-catalog evidence/item-7/provider-catalog.json \
  --provider-coverage /tmp/mcpack-item7-r8-delivery/restored/core/run-a/provider-coverage.json \
  --provider-disposition /tmp/mcpack-item7-r8-delivery/restored/core/provider-disposition.json \
  --restriction-audit evidence/item-7/biome-restriction-audit.json \
  --world-archive-inventory evidence/item-7/world-archive-inventory.json \
  --repeat-comparison /tmp/mcpack-item7-r8-delivery/restored/core/repeat-comparison.json \
  --warning-audit /tmp/mcpack-item7-r8-delivery/restored/core/warning-audit.json \
  --warning-disposition /tmp/mcpack-item7-r8-delivery/restored/core/warning-disposition.json \
  --control-comparison /tmp/mcpack-item7-r8-delivery/restored/core/control-comparison.json \
  --visual-manifest /tmp/mcpack-item7-r8-delivery/restored/core/visual-qa/captures/capture-manifest.tsv \
  --visual-review evidence/item-7/visual/integrity-review.json \
  --visual-review evidence/item-7/visual/fidelity-review.json \
  --archive-manifest evidence/item-7/archive/r8/core-manifest.json \
  --archive-manifest evidence/item-7/archive/r8/run-a-worlds-manifest.json \
  --archive-manifest evidence/item-7/archive/r8/run-b-worlds-manifest.json \
  --archive-manifest evidence/item-7/archive/r8/auxiliary-worlds-manifest.json \
  --restore-receipt evidence/item-7/archive/r8/core-restore.json \
  --restore-receipt evidence/item-7/archive/r8/run-a-worlds-restore.json \
  --restore-receipt evidence/item-7/archive/r8/run-b-worlds-restore.json \
  --restore-receipt evidence/item-7/archive/r8/auxiliary-worlds-restore.json \
  --publication evidence/item-7/archive/r8/publication.json \
  --output /home/lonestar/Desktop/Projects/mcpack-item7-r8-completion-rebuilt.json
cmp evidence/item-7/completion.json /home/lonestar/Desktop/Projects/mcpack-item7-r8-completion-rebuilt.json
sha256sum evidence/item-7/completion.json /home/lonestar/Desktop/Projects/mcpack-item7-r8-completion-rebuilt.json
```

Both exact rebuild commands returned `PASS`; both `cmp` commands returned zero; and the paired SHA-256 values matched the identities recorded above.

The older mutable `/tmp/mcpack-item7-raw-20260904` tree is not an accepted completion input. The accepted r8 restored core contains capture manifest SHA-256 `219e17ed50b6e5b919c16a2b5bef34b7820b251c7272074d5df91c5123260f91`, which matches both accepted visual review receipts.

## Worktree validation

- `uv run pytest -q tests/item7`: 186 passed.
- `uv run pytest -q`: 867 passed.
- Scoped Ruff formatting: passed across 104 files.
- Scoped Ruff checks: passed.
- Scoped basedpyright: 0 errors, 0 warnings, 0 notes.
- Item 7 shell syntax: passed.
- `git diff --check`: passed.
- The tracked archive CLI created and restored a one-file archive byte for byte and emitted a verified receipt.

## Clean export validation

The first clean export at `f68cd0be8d2d9d4223bd2b9b003e32534a1bac75` passed every check below but preceded the verification-time correction. It is superseded as final clean-export evidence.

Final evidence candidate `7184cc7ea2a56cf18304a1e180c649af5fefbb99` was exported with `git archive` into `/home/lonestar/Desktop/Projects/mcpack-item7-clean-7184cc7`. Pytest used `/home/lonestar/Desktop/Projects/mcpack-item7-clean-7184cc7-tmp` so temporary writes did not depend on the exhausted `/tmp` quota.

- Item 7 tests: 186 passed.
- Repository tests: 867 passed.
- Scoped Ruff formatting and checks: passed across 104 files.
- Scoped basedpyright: 0 errors, 0 warnings, 0 notes.
- Item 7 shell syntax: passed.
- The tracked world inventory builder rehashed all 716 r8 restored world files and reproduced the committed inventory byte for byte.
- The tracked completion builder used the r8 restored core and reproduced the final committed 125-artifact `PASS` receipt byte for byte.

The validation-record commit changes only this evidence record and synchronized handoff text. Fresh exact-SHA review lanes and a runtime audit must bind the resulting commit before push.
