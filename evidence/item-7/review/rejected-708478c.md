# Rejected Item 7 candidate 708478c

## Candidate identity

- Exact reviewed revision: `708478ce925353d8cb64199df0fc47d69df6bdf5`.
- Aggregate verdict: `FAIL`.
- Disposition: superseded locally. This revision was never pushed to PR `#15`.

## Lane results

| Lane | Verdict | Confidence | Binding evidence |
| --- | --- | --- | --- |
| Goal and constraints | PASS | HIGH | `/root/item7_r4_goal_review` final result |
| Code quality | FAIL | HIGH | `/root/item7_r4_code_review` final result |
| Security and evidence integrity | FAIL | HIGH | `/root/item7_r4_integrity_review` final result |
| Hands-on QA | PASS | HIGH | `/root/item7_r4_qa_review` final result |
| Context and reproducibility | FAIL | HIGH | `/root/item7_r4_context_review` final result |
| Runtime debugging audit | PASS | HIGH | `/root/item7_r4_runtime_audit` final result and `/tmp/item7-r7-runtime-audit-708478.md` |

The passing lanes verified the Item 7 specification accounting, live r7 release identities, 716-file raw world inventory, 125-artifact completion receipt, all 128 visual captures, lifecycle receipts, process cleanup, and the preserved unknowns and limitations. Their approval binds only the exact rejected revision and does not transfer to later commits.

## Blocking findings

1. `restore_archive` created target and receipt parent directories recursively before descriptor-safe path validation. A nested path beneath a symlink could create an intermediate directory outside the approved tree before the operation rejected it. The same pattern existed for archive and manifest output parents.
2. `src/mcpack_evidence/item7_archive.py` and `tests/item7/test_item7_archive_security.py` exceeded the binding 250 pure-LOC module ceiling after the prior security corrections.
3. `evidence/item-7/review/candidate-r7-validation.md` claimed to record the exact accepted completion invocation but omitted required arguments, values, and repeated argument multiplicities.

## Corrective disposition

- Commit `7f7f0c4` requires pre-existing safely opened output parents, adds four regressions proving no escaped intermediate directory is created, and splits archive models, restore behavior, and publication-race tests into modules below 250 lines.
- Commit `c88f12c` records the full literal r7 completion rebuild and comparison command. The command returned `PASS`, reproduced the committed file byte for byte, and matched SHA-256 `6bb509d87a215a67186fa70f285b59e6986d813c7c21f9ab19e8479ea078515c`.
- Because archive implementation changed after the r7 source tag, r7 remains preserved history but cannot close Item 7. A fresh release, restore, publication, completion rebuild, and exact-SHA review are required.
