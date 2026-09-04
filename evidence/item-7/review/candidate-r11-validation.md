# Item 7 r11 candidate validation

## Bound evidence

- Archive source revision: `4b6d12e6507ecf948edd11bef9033faeea622c81`.
- Annotated tag object: `4bd01efe585cdc5a8a26a1b19f688a276fb31d62`.
- Release: `https://github.com/copeugne/mcpack/releases/tag/item-7-raw-evidence-2026-09-04-r11`.
- World archive inventory SHA-256: `7907bfd705bb8b1b7e794133e634e59ba1d3a694210353da65193eff7dd79027`, 716 files.
- Save-order audit SHA-256: `55ef4a83a0c618520f05110c216e66d4915615141ff43fc7a963e6fdb249dd12`, 12 lifecycles.
- Completion SHA-256: `ecfef0a93778dc75bc5d0ec3bb11ee1692eb90d55106a0b81483251366ed88ed`, 138 artifacts, `PASS`.

The four immutable release assets are:

| Asset | Files | Raw bytes | Archive bytes | Archive SHA-256 |
| --- | ---: | ---: | ---: | --- |
| Core | 4,618 | 2,515,785,938 | 243,943,142 | `2229673778123d8b7737048610d9c171aea9b49900724acc0f35ac48eed25773` |
| Run A worlds | 249 | 484,774,742 | 291,011,199 | `575b8644bb888e2f2c09311f0ba3ac063ea00eda1d51159e0038218a28d96fa7` |
| Run B worlds | 250 | 484,038,098 | 289,949,293 | `3a82829fa159323ec1844d6f98fdc9ab6b25feab78d15c1b268d2a2692c268ff` |
| Auxiliary worlds | 217 | 165,166,012 | 48,648,807 | `d865320a9b1d2b44e59eb7d854fa499309746dc71a04b6b8caa46ede2a0c5a25` |

All four archives were built from a fresh hash-verified r9 restoration using the tracked implementation at the tagged r11 source revision. All four r11 archives then restored into absent targets at `/home/lonestar/Desktop/Projects/mcpack-item7-r11-delivery/restored/`. Restore verified all 5,334 files and rejected symlinks, special files, hardlinks, and `session.lock` from the accepted source boundary.

r10 has the same valid raw payload and passed remote verification, but it is not accepted custody. Its immutable source tag predates the commit that made the save-order audit a required completion artifact. The rejection is preserved in `evidence/item-7/review/rejected-r10-custody.md`.

## Remote verification

The two successful independent remote verification commands were:

```sh
tools/verify_item7_release.sh copeugne/mcpack item-7-raw-evidence-2026-09-04-r11 evidence/item-7/archive/r11 evidence/item-7/archive/r11/publication.json /home/lonestar/Desktop/Projects/mcpack-item7-r11-release-download-1
tools/verify_item7_release.sh copeugne/mcpack item-7-raw-evidence-2026-09-04-r11 evidence/item-7/archive/r11 evidence/item-7/archive/r11/publication.json /home/lonestar/Desktop/Projects/mcpack-item7-r11-release-download-2
```

Both downloads matched every committed asset size and SHA-256. The first success is recorded at `2026-09-04T18:41:56Z` in `evidence/item-7/archive/r11/publication.json`.

## Exact inventory rebuild

```sh
uv run python tools/build_item7_world_archive_inventory.py \
  --run-a /home/lonestar/Desktop/Projects/mcpack-item7-r11-delivery/restored/run-a \
  --run-a-archive-name mcpack-item7-raw-run-a-worlds-r11.tar.gz \
  --run-b /home/lonestar/Desktop/Projects/mcpack-item7-r11-delivery/restored/run-b \
  --run-b-archive-name mcpack-item7-raw-run-b-worlds-r11.tar.gz \
  --auxiliary /home/lonestar/Desktop/Projects/mcpack-item7-r11-delivery/restored/auxiliary \
  --auxiliary-archive-name mcpack-item7-raw-auxiliary-worlds-r11.tar.gz \
  --output /tmp/item7-world-inventory-r11-rebuilt.json
cmp evidence/item-7/world-archive-inventory.json /tmp/item7-world-inventory-r11-rebuilt.json
sha256sum evidence/item-7/world-archive-inventory.json /tmp/item7-world-inventory-r11-rebuilt.json
```

## Exact save-order rebuild

```sh
uv run tools/validate_item7_save_sequence.py \
  --core /home/lonestar/Desktop/Projects/mcpack-item7-r11-delivery/restored/core \
  --manifest evidence/item-7/archive/r11/core-manifest.json \
  > /tmp/item7-save-sequence-r11-rebuilt.json
cmp evidence/item-7/save-sequence-r11.json /tmp/item7-save-sequence-r11-rebuilt.json
sha256sum evidence/item-7/save-sequence-r11.json /tmp/item7-save-sequence-r11-rebuilt.json
```

The audit rebuilds all 12 accepted main, gap, control, and successful pilot lifecycles. For each hash-bound console log, the final work marker occurs before `Saving the game`, which occurs before `Saved the game`.

## Exact completion rebuild

```sh
uv run python tools/build_item7_completion.py \
  --raw-root /home/lonestar/Desktop/Projects/mcpack-item7-r11-delivery/restored/core \
  --protocol evidence/item-7/protocol/worldgen-audit-v1.json \
  --provider-catalog evidence/item-7/provider-catalog.json \
  --provider-coverage /home/lonestar/Desktop/Projects/mcpack-item7-r11-delivery/restored/core/run-a/provider-coverage.json \
  --provider-disposition /home/lonestar/Desktop/Projects/mcpack-item7-r11-delivery/restored/core/provider-disposition.json \
  --restriction-audit evidence/item-7/biome-restriction-audit.json \
  --world-archive-inventory evidence/item-7/world-archive-inventory.json \
  --repeat-comparison /home/lonestar/Desktop/Projects/mcpack-item7-r11-delivery/restored/core/repeat-comparison.json \
  --warning-audit /home/lonestar/Desktop/Projects/mcpack-item7-r11-delivery/restored/core/warning-audit.json \
  --warning-disposition /home/lonestar/Desktop/Projects/mcpack-item7-r11-delivery/restored/core/warning-disposition.json \
  --control-comparison /home/lonestar/Desktop/Projects/mcpack-item7-r11-delivery/restored/core/control-comparison.json \
  --visual-manifest /home/lonestar/Desktop/Projects/mcpack-item7-r11-delivery/restored/core/visual-qa/captures/capture-manifest.tsv \
  --visual-review evidence/item-7/visual/integrity-review.json \
  --visual-review evidence/item-7/visual/fidelity-review.json \
  --archive-manifest evidence/item-7/archive/r11/core-manifest.json \
  --archive-manifest evidence/item-7/archive/r11/run-a-worlds-manifest.json \
  --archive-manifest evidence/item-7/archive/r11/run-b-worlds-manifest.json \
  --archive-manifest evidence/item-7/archive/r11/auxiliary-worlds-manifest.json \
  --restore-receipt evidence/item-7/archive/r11/core-restore.json \
  --restore-receipt evidence/item-7/archive/r11/run-a-worlds-restore.json \
  --restore-receipt evidence/item-7/archive/r11/run-b-worlds-restore.json \
  --restore-receipt evidence/item-7/archive/r11/auxiliary-worlds-restore.json \
  --publication evidence/item-7/archive/r11/publication.json \
  --save-sequence-audit evidence/item-7/save-sequence-r11.json \
  --output /tmp/item7-completion-r11-rebuilt.json
cmp evidence/item-7/completion.json /tmp/item7-completion-r11-rebuilt.json
sha256sum evidence/item-7/completion.json /tmp/item7-completion-r11-rebuilt.json
```

The completion builder returns `PASS`. It rebuilds all 16 accepted analyses from selected JSONL, rebuilds the complete Run A and Run B comparison from all accepted selections, rebuilds all warning and control source claims, rebuilds the 12-lifecycle save audit, and requires every derived result to match its committed artifact exactly.

## Current validation state

Clean export revision `44fc86af4c735f30c82e41e7e490029c5f62456b` passed:

- Item 7 tests: 197 passed.
- Repository tests: 878 passed.
- Ruff formatting: 118 files already formatted.
- Ruff lint: all checks passed.
- basedpyright: zero errors, warnings, or notes.
- Shell syntax: passed for the staging and release-verification scripts.
- Repository diff check: passed.
- Inventory rebuild: 716 files, byte-identical at SHA-256 `7907bfd705bb8b1b7e794133e634e59ba1d3a694210353da65193eff7dd79027`.
- Save-order rebuild: 12 lifecycles, byte-identical at SHA-256 `55ef4a83a0c618520f05110c216e66d4915615141ff43fc7a963e6fdb249dd12`.
- Completion rebuild: 138 artifacts, byte-identical at SHA-256 `ecfef0a93778dc75bc5d0ec3bb11ee1692eb90d55106a0b81483251366ed88ed`, `PASS`.

Exact-SHA review lanes and GitHub review remain delivery gates rather than completed claims in this record.
