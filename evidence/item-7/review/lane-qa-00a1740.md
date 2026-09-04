# Item 7 hands-on QA at 00a1740

- Exact reviewed revision: `00a174015de96c9219565034428df2421a42c66e`.
- Verdict: `PASS`.
- Confidence: `HIGH`.

The candidate was exported with `git archive` and tested outside the working tree. The exact inventory and completion invocations are preserved in `candidate-r8-validation.md`; the programs and test support used by this QA are tracked under `tools/`, `src/mcpack_evidence/`, and `tests/item7/`.

| Surface | Result |
| --- | --- |
| `uv run pytest -q tests/item7` | 186 passed |
| `uv run pytest -q` | 867 passed |
| Scoped Ruff format and check | PASS |
| Scoped basedpyright | 0 errors, warnings, or notes |
| Item 7 shell syntax and Git diff check | PASS |
| World inventory rebuild | 716 files, byte-identical SHA-256 `331bde517e6fb072a4aa0a66fb77b733559b27f92098f8fc1f236405bbe02f3e` |
| Completion rebuild | `PASS`, 125 artifacts, byte-identical SHA-256 `c369178431abba0c17404b9723a47fa66e945c305b5477c63bd5a9a6ec281582` |
| Visual capture identity | 128 matches, manifest SHA-256 `219e17ed50b6e5b919c16a2b5bef34b7820b251c7272074d5df91c5123260f91` |
| Real archive restore CLI | PASS, two fixture files restored |
| Archive and manifest tamper attempts | Rejected with no target or receipt |
| Security and completion failure-path selection | 43 passed |
| Lifecycle receipts | Required readiness, flush, save, stop, clean-exit, and cleanup assertions passed |
| Live Java process check | 0 processes |

The release was not downloaded a third time. The committed publication and verifier receipts preserve the two accepted downloads. No actionable findings.
