# Item 7 r9 candidate validation

## Bound evidence

- Archive source revision: `fb901b1050f211cb88fe1fb9d074f5d7c1e17407`.
- Annotated tag object: `f4a573dd5263caef541f4e0ff622469a356bd2b8`.
- Release: `https://github.com/copeugne/mcpack/releases/tag/item-7-raw-evidence-2026-09-04-r9`.
- World archive inventory SHA-256: `e417d77272151a91153a94df993da058f174fb568be75a1e61e49916dbc1e994`, 716 files.
- Completion SHA-256: `76603b037d38534f56a4a2625666032b60929d7efe74c0a434b73310858c4c69`, 137 artifacts, `PASS`.

The four immutable release assets are:

| Asset | Files | Raw bytes | Archive bytes | Archive SHA-256 |
| --- | ---: | ---: | ---: | --- |
| Core | 4,618 | 2,515,785,938 | 243,943,142 | `2229673778123d8b7737048610d9c171aea9b49900724acc0f35ac48eed25773` |
| Run A worlds | 249 | 484,774,742 | 291,011,199 | `575b8644bb888e2f2c09311f0ba3ac063ea00eda1d51159e0038218a28d96fa7` |
| Run B worlds | 250 | 484,038,098 | 289,949,293 | `3a82829fa159323ec1844d6f98fdc9ab6b25feab78d15c1b268d2a2692c268ff` |
| Auxiliary worlds | 217 | 165,166,012 | 48,648,807 | `d865320a9b1d2b44e59eb7d854fa499309746dc71a04b6b8caa46ede2a0c5a25` |

All four archives were built with the tracked implementation at the tagged source revision and restored into absent targets at `/home/lonestar/Desktop/Projects/mcpack-item7-r9-delivery/restored/`. Restore verified all 5,334 files, found no symlinks, and found no `session.lock` file. The payload bytes are unchanged from r8; r9 updates custody to the source revision that binds every derived warning and control claim to its raw inputs.

The first r9 construction attempt used `/tmp` and failed closed because the per-user quota was exhausted. The first remote download at `/home/lonestar/Desktop/Projects/mcpack-item7-r9-release-download-1` was interrupted and left truncated Run A and Run B assets. Both incomplete attempts were removed and are not acceptance evidence.

The two successful independent remote verification commands were:

```sh
tools/verify_item7_release.sh copeugne/mcpack item-7-raw-evidence-2026-09-04-r9 evidence/item-7/archive/r9 evidence/item-7/archive/r9/publication.json /home/lonestar/Desktop/Projects/mcpack-item7-r9-release-download-2
tools/verify_item7_release.sh copeugne/mcpack item-7-raw-evidence-2026-09-04-r9 evidence/item-7/archive/r9 evidence/item-7/archive/r9/publication.json /home/lonestar/Desktop/Projects/mcpack-item7-r9-release-download-3
```

Both successful downloads matched every committed asset size and SHA-256. The first success is recorded at `2026-09-04T16:56:15Z` in `evidence/item-7/archive/r9/publication.json`.

## Exact inventory rebuild

From the repository root, the exact world archive inventory rebuild and comparison invocation is:

```sh
uv run python tools/build_item7_world_archive_inventory.py \
  --run-a /home/lonestar/Desktop/Projects/mcpack-item7-r9-delivery/restored/run-a \
  --run-a-archive-name mcpack-item7-raw-run-a-worlds-r9.tar.gz \
  --run-b /home/lonestar/Desktop/Projects/mcpack-item7-r9-delivery/restored/run-b \
  --run-b-archive-name mcpack-item7-raw-run-b-worlds-r9.tar.gz \
  --auxiliary /home/lonestar/Desktop/Projects/mcpack-item7-r9-delivery/restored/auxiliary \
  --auxiliary-archive-name mcpack-item7-raw-auxiliary-worlds-r9.tar.gz \
  --output /home/lonestar/Desktop/Projects/mcpack-item7-clean-df804b3-tmp/item7-world-inventory-r9-rebuilt.json
cmp evidence/item-7/world-archive-inventory.json /home/lonestar/Desktop/Projects/mcpack-item7-clean-df804b3-tmp/item7-world-inventory-r9-rebuilt.json
sha256sum evidence/item-7/world-archive-inventory.json /home/lonestar/Desktop/Projects/mcpack-item7-clean-df804b3-tmp/item7-world-inventory-r9-rebuilt.json
```

## Exact completion rebuild

From the repository root, the exact completion rebuild and comparison invocation is:

```sh
uv run python tools/build_item7_completion.py \
  --raw-root /home/lonestar/Desktop/Projects/mcpack-item7-r9-delivery/restored/core \
  --protocol evidence/item-7/protocol/worldgen-audit-v1.json \
  --provider-catalog evidence/item-7/provider-catalog.json \
  --provider-coverage /home/lonestar/Desktop/Projects/mcpack-item7-r9-delivery/restored/core/run-a/provider-coverage.json \
  --provider-disposition /home/lonestar/Desktop/Projects/mcpack-item7-r9-delivery/restored/core/provider-disposition.json \
  --restriction-audit evidence/item-7/biome-restriction-audit.json \
  --world-archive-inventory evidence/item-7/world-archive-inventory.json \
  --repeat-comparison /home/lonestar/Desktop/Projects/mcpack-item7-r9-delivery/restored/core/repeat-comparison.json \
  --warning-audit /home/lonestar/Desktop/Projects/mcpack-item7-r9-delivery/restored/core/warning-audit.json \
  --warning-disposition /home/lonestar/Desktop/Projects/mcpack-item7-r9-delivery/restored/core/warning-disposition.json \
  --control-comparison /home/lonestar/Desktop/Projects/mcpack-item7-r9-delivery/restored/core/control-comparison.json \
  --visual-manifest /home/lonestar/Desktop/Projects/mcpack-item7-r9-delivery/restored/core/visual-qa/captures/capture-manifest.tsv \
  --visual-review evidence/item-7/visual/integrity-review.json \
  --visual-review evidence/item-7/visual/fidelity-review.json \
  --archive-manifest evidence/item-7/archive/r9/core-manifest.json \
  --archive-manifest evidence/item-7/archive/r9/run-a-worlds-manifest.json \
  --archive-manifest evidence/item-7/archive/r9/run-b-worlds-manifest.json \
  --archive-manifest evidence/item-7/archive/r9/auxiliary-worlds-manifest.json \
  --restore-receipt evidence/item-7/archive/r9/core-restore.json \
  --restore-receipt evidence/item-7/archive/r9/run-a-worlds-restore.json \
  --restore-receipt evidence/item-7/archive/r9/run-b-worlds-restore.json \
  --restore-receipt evidence/item-7/archive/r9/auxiliary-worlds-restore.json \
  --publication evidence/item-7/archive/r9/publication.json \
  --output /home/lonestar/Desktop/Projects/mcpack-item7-clean-df804b3-tmp/item7-completion-r9-rebuilt.json
cmp evidence/item-7/completion.json /home/lonestar/Desktop/Projects/mcpack-item7-clean-df804b3-tmp/item7-completion-r9-rebuilt.json
sha256sum evidence/item-7/completion.json /home/lonestar/Desktop/Projects/mcpack-item7-clean-df804b3-tmp/item7-completion-r9-rebuilt.json
```

Both builders returned `PASS`. Both `cmp` commands returned zero. The inventory pair matched SHA-256 `e417d77272151a91153a94df993da058f174fb568be75a1e61e49916dbc1e994`; the completion pair matched SHA-256 `76603b037d38534f56a4a2625666032b60929d7efe74c0a434b73310858c4c69`.

The completion builder rebuilds the accepted warning audit from all 11 declared raw logs. It also validates the embedded path, SHA-256, byte size, and record count of the control receipt, control chunks, pilot receipt, and pilot chunks. All 15 sources are required archive artifacts. Three warning sources overlap existing provider evidence, so path de-duplication produces 137 exact artifacts. The implementation, tests, builders, verifier, schemas, and commands required to reproduce these claims are tracked in the repository.

## Clean export validation

Evidence candidate `df804b3789d0c1a2f32f690f71e8c0422d8c5b20` was exported with `git archive` into `/home/lonestar/Desktop/Projects/mcpack-item7-clean-df804b3`. Test temporary files used `/home/lonestar/Desktop/Projects/mcpack-item7-clean-df804b3-tmp`.

- Item 7 tests: 188 passed.
- Repository tests: 869 passed.
- Ruff formatting and checks: passed across 106 files.
- basedpyright: 0 errors, 0 warnings, 0 notes.
- Item 7 shell syntax: passed.
- `git diff --check`: passed.
- The tracked inventory builder rehashed all 716 restored world files and reproduced the committed inventory byte for byte.
- The tracked completion builder used the r9 restored core and reproduced the committed 137-artifact `PASS` receipt byte for byte.

This validation record and the synchronized status documentation are subsequent documentation-only changes. Fresh exact-SHA review lanes and the runtime audit must bind the resulting commit before push.
