# Item 7 rejected GitHub Codex review at e261294

Reviewed revision: `e26129498e905174df2ccbc067db589c244685b1`

Pull request: `https://github.com/copeugne/mcpack/pull/15`

Verdict: `REJECTED`

The completed GitHub Codex review reported three technically valid findings:

1. Completion did not independently bind every raw world archive file to the corresponding archive manifest. Source: `https://github.com/copeugne/mcpack/pull/15#discussion_r3933757888`.
2. Floating-structure detection compared structure bounds with post-placement `WORLD_SURFACE`, so it could not prove an air gap beneath a structure. Source: `https://github.com/copeugne/mcpack/pull/15#discussion_r3933757892`.
3. Analysis and rendering subtracted one block from a decoded heightmap value that already represented highest occupied Y, which could select the wrong biome quart. Source: `https://github.com/copeugne/mcpack/pull/15#discussion_r3933757900`.

Disposition:

- Three focused RED tests reproduced the surface-analysis defects. Commit `6a3a997517974b0b6ca01906638b02228c320110` removes the unsupported floating candidate calculation, reports that method as limited, and samples biomes at decoded highest occupied Y in both analysis and rendering.
- A focused completion RED test proved that the prior API had no independent expected inventory for the three raw world archives. Commit `61a408c9d01ff80614b031e89bca2c869b524f01` adds a tracked descriptor-bound inventory builder and makes completion require exact `FileIdentity` equality for all 716 Run A, Run B, and auxiliary world archive files.
- Commit `bb6dd928b4a95db085c2e44d50296b7152f2b74d` binds visual acceptance to the corrected renderer revision.
- All 32 analyses and all 32 galleries were rebuilt from their hash-bound selected chunk streams. A fresh 128-capture set passed two independent reviews against the same read-only restored core, with every hash, size, dimension, gallery artifact, provenance chain, and region binding verified. Two earlier writable-tree review attempts were rejected and preserved separately.
- Four corrected archives were produced by the hardened staging and archive implementation, restored into absent targets, published under `item-7-raw-evidence-2026-09-04-r4`, and downloaded twice with the tracked verifier. The r4 tag resolves to `bb6dd928b4a95db085c2e44d50296b7152f2b74d`.
- The rebuilt completion receipt returns `PASS` with 125 exact artifact identities and SHA-256 `33b3dffb1f99ea5dca62e03818ae9886d2abed8ecacf2ec432cbd32645c1ea14`.
- The corrected worktree passes 177 Item 7 tests, 858 repository tests, scoped Ruff formatting and checks across 101 files, basedpyright with zero issues, and Item 7 shell syntax.

This rejected review is not approval. The corrected final candidate still requires clean-export validation, fresh exact-SHA review lanes, a new completed GitHub Codex review, and merge verification.
