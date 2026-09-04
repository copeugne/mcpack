# Item 7 corrected candidate validation

Validated revision: `857164b4e5320d017828102268c0ad87e7c31924`

Pull request: `https://github.com/copeugne/mcpack/pull/15`

## Worktree gate

- `uv run pytest -q tests/item7`: 177 passed.
- `uv run pytest -q`: 858 passed.
- Scoped Ruff formatting and checks passed across 101 Item 7 Python files.
- Scoped basedpyright reported 0 errors, 0 warnings, and 0 notes.
- Item 7 shell syntax and `git diff --check` passed.
- The first full-suite attempt encountered `Disk quota exceeded` only after the focused suite had passed. It produced 92 write failures while pytest created temporary data. Redundant verified downloads and the superseded r4 construction tree were removed; the unchanged full suite then passed all 858 tests. No assertion defect was hidden or changed.

## Clean Git export gate

A clean `git archive` export of the exact revision passed all 177 Item 7 tests, scoped Ruff formatting and checks, basedpyright with zero issues, and Item 7 shell syntax. The first extraction invocation was rejected because it ran `git archive` from the empty export directory. Running the same command from the repository created the intended clean export; this failed invocation changed no evidence.

From the clean export, the tracked world archive inventory builder independently rehashed all 716 restored world files and reproduced `evidence/item-7/world-archive-inventory.json` byte for byte at SHA-256 `d5760086741a126299253da677faa9fa64358cfe5e4d26ae68712da58c7084d2`.

The tracked completion builder returned `PASS` and reproduced `evidence/item-7/completion.json` byte for byte at SHA-256 `33b3dffb1f99ea5dca62e03818ae9886d2abed8ecacf2ec432cbd32645c1ea14`. It binds 125 exact artifacts, the corrected renderer revision, the two accepted visual reviews, all four r4 archives and restores, the r4 publication, and the complete world archive inventory.

## Manual and durability surface

- Two independent reviewers inspected all 128 captures at one read-only restored r4 core. Both returned `PASS`. A post-review 321-file hash sweep found no changed bytes.
- All four r4 archives restored into absent targets with exact file verification.
- The tracked repository-bound release verifier downloaded and verified all four remote assets twice at source revision `bb6dd928b4a95db085c2e44d50296b7152f2b74d`.
- No r4 acceptance artifact depends on `.omo/evidence` or an untracked evidence-producing source file.

This record proves the local and clean-export candidate gates. Fresh independent exact-SHA review lanes, a new GitHub Codex review, merge, and delivered-ref verification remain mandatory.
