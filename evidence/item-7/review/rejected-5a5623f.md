# Rejected Item 7 review at 5a5623f

Reviewed revision: `5a5623fbe161c3ab1874c8184b8f9f1d0418c9cd`.

Aggregate verdict: `REJECTED`.

## Lane results

- Goal and constraint review: `PASS`, high confidence. It reproduced 177 Item 7 tests, 858 repository tests, scoped quality checks, the 716-file inventory, and the 125-artifact completion receipt.
- Context and requirement review: `PASS`, high confidence. It found no missed Item 7 requirement or stale superseding claim.
- Code-quality review: conditional approval with one medium test defect. The missing-region regression used empty Run B and auxiliary inventories, so it failed before reaching the exact `FileIdentity` comparison named by the test.
- Security and evidence-integrity review: `FAIL`, high confidence. Restore verified the temporary extraction but published the target tree and `verified=true` receipt through replaceable pathnames.
- Runtime debugging audit: `PASS`, high confidence. It passed clean-export and full tests, lifecycle checks, archive round trips, tamper rejection, byte-identical inventory and completion rebuilds, and process cleanup. It separately identified permissive scalar coercion in standalone archive models.
- Hands-on QA: `FAIL`, high confidence, because it rebuilt completion from the older mutable `/tmp/mcpack-item7-raw-20260904` visual tree. That tree has capture-manifest SHA-256 `84c6c9564e7289541a61d7215f0a9a03bd3453913ed52e4d39b7c08f4bd34765` and three capture mismatches. The accepted read-only restore has manifest SHA-256 `219e17ed50b6e5b919c16a2b5bef34b7820b251c7272074d5df91c5123260f91`. This exposed an input-selection and reproduction-documentation defect even though the accepted archive bytes were not corrupt.

The code reviewer wrote a scratch report under the prohibited `.omo/evidence` path despite its read-only instruction. It was immediately relocated to `/tmp/item7-r4-code-review-5a5623f.md`, and `.omo/evidence` was removed again. No accepted or committed evidence depends on that path.

## Corrective disposition

- `dd956fc` publishes restored trees with descriptor-bound no-replace semantics, verifies the complete pinned tree, and publishes receipts from a pinned parent only while the target still names the verified inode.
- `b54905a` makes the missing-region regression reach the intended exact world-file comparison.
- `ac54285` rejects coerced scalar types in archive manifests and restore receipts.
- The first real corrected restore failed closed because the pinned directory scan inherited a nonzero directory offset. No target or receipt was published. `ca646c1` rewinds descriptor scans, adds precise mismatch diagnostics, and passes a real 217-file restore.
- Tags r5 and r6 preserve unpublished failed-attempt source identities. Neither has a GitHub release. Their local manifests and archives remain outside authoritative `evidence/` paths.
- `096ceaa` records the final r7 manifests, corrected restore receipts, publication receipt, and 716-file world inventory. Tag `item-7-raw-evidence-2026-09-04-r7`, annotated tag object `3374ff7ce183d9cb9dd2636e206abec68db3f220`, resolves to `ca646c19ad772bd6de6a47f4dcb0fc5dc4b5cbfc`.
- All four r7 archives restored into absent targets and passed two independent tracked downloads. Payload hashes remain byte-identical to r4 because the corrected defect affected restore custody, not archive content.
- `39217f4` records the rebuilt 125-artifact completion receipt. It returns `PASS` and has SHA-256 `6bb509d87a215a67186fa70f285b59e6986d813c7c21f9ab19e8479ea078515c`.

This rejected review provides no coverage for later revisions. Fresh exact-SHA local review and GitHub Codex review are mandatory before merge.
