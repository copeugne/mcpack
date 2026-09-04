# Accepted Item 7 candidate 00a1740

## Candidate identity

- Exact reviewed revision: `00a174015de96c9219565034428df2421a42c66e`.
- Aggregate local-review verdict: `PASS`.
- Delivery status at review time: `PASS, DELIVERY PENDING`.
- Accepted raw-evidence release: `item-7-raw-evidence-2026-09-04-r8`.
- Archive source revision: `85efc96b5f1c2d3518a594905a65a2777d904b4b`.
- Annotated tag object: `7bd8dad5c4ae4baec9eddc767c96aac7d05b30af`.

## Lane results

| Lane | Verdict | Confidence | Binding evidence |
| --- | --- | --- | --- |
| Goal and constraints | PASS | HIGH, 0.97 | `/root/item7_r4_goal_review` final result |
| Code quality | PASS | HIGH | `/root/item7_r4_code_review` final result |
| Security and evidence integrity | PASS | HIGH | `/root/item7_r4_integrity_review` final result |
| Hands-on QA | PASS | HIGH | `/root/item7_r4_qa_review` final result and `/home/lonestar/mcpack-item7-qa-00a.Gbdpfu/00a174015de96c9219565034428df2421a42c66e-manual-qa.md` |
| Context and reproducibility | PASS | HIGH | `/root/item7_r4_context_review` final result |
| Runtime debugging audit | PASS | HIGH | `/root/item7_r4_runtime_audit` final result and `/tmp/item7-r8-runtime-audit-00a.md` |

Every lane bound its verdict to the exact full revision above. No result from an earlier revision was reused.

## Reproduced evidence

- Item 7 tests: 186 passed.
- Full repository tests: 867 passed in both the final clean-export validation and hands-on QA.
- Scoped Ruff formatting and checks across 104 files: passed.
- Scoped basedpyright: 0 errors, 0 warnings, 0 notes.
- Item 7 shell syntax and Git diff checks: passed.
- World archive inventory: 716 files, byte-identical SHA-256 `331bde517e6fb072a4aa0a66fb77b733559b27f92098f8fc1f236405bbe02f3e`.
- Completion receipt: `PASS`, 125 artifacts, byte-identical SHA-256 `c369178431abba0c17404b9723a47fa66e945c305b5477c63bd5a9a6ec281582`.
- Visual capture manifest: 128 matching captures, SHA-256 `219e17ed50b6e5b919c16a2b5bef34b7820b251c7272074d5df91c5123260f91`.
- Archive, manifest, scalar, inventory, completion, and lifecycle tamper cases rejected as required.
- Real archive CLI creation and restore passed. A real r8 auxiliary restore produced 217 files with no symlinks or `session.lock`.
- Ten lifecycle receipts passed readiness, flush and save, stop, clean-exit, and process-cleanup assertions. No Java process survived QA.
- Fifty-two focused security and evidence-integrity tests and fourteen runtime adversarial archive tests passed.
- Live GitHub metadata matched the r8 tag, four release assets, sizes, and digests recorded in the committed publication evidence.

## Prior finding disposition

The review explicitly rechecked the three blockers found at rejected revision `708478ce925353d8cb64199df0fc47d69df6bdf5`:

1. All archive, manifest, target, and receipt output parents now require safely opened pre-existing paths. Nested symlink-parent regressions prove no escaped intermediate directory is created.
2. Archive behavior and tests are split into concept-named modules below the binding 250 pure-LOC ceiling.
3. `candidate-r8-validation.md` records the literal complete inventory and completion rebuild commands with every required argument and multiplicity.

No actionable findings remained.

## Residuals and delivery gate

- No lane performed a third download of the approximately 848 MiB release. The accepted record already preserves two independent successful repository-bound downloads, and the final lanes verified live release metadata and the restored payloads.
- Reproduction paths in the validation report are host-specific. Another operator may substitute equivalent pre-existing parent paths while preserving the required absent final output targets.
- Item 7 is not `COMPLETE` at this revision. PR `#15` must receive this accepted branch, complete a fresh clean GitHub Codex review cycle with no valid unresolved findings, merge into `main`, and have the delivered ref verified.
- Item 8 remains blocked until that delivery gate passes.
