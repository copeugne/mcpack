# Item 7 hands-on QA review at c7babd9

## Identity and verdict

- Reviewed revision: `c7babd9596594bab4f151a50cdc2ccb180c7aa18`.
- Verdict: `PASS`.
- Confidence: `HIGH`.
- Blocking findings: none.

## Executed scenarios

| Scenario | Observed result |
| --- | --- |
| Rebuild world inventory from restored r9 worlds | `PASS`, 716 files, byte-identical, SHA-256 `e417d77272151a91153a94df993da058f174fb568be75a1e61e49916dbc1e994` |
| Rebuild completion with every r9 input | `PASS`, 137 artifacts, byte-identical, SHA-256 `76603b037d38534f56a4a2625666032b60929d7efe74c0a434b73310858c4c69` |
| Mutate a warning source log | Rejected as a warning-audit source mismatch |
| Mutate the pilot control chunk stream | Rejected as a control source identity mismatch |
| Verify restored archive files | All 5,334 files matched; no symlink or `session.lock` |
| Verify visual capture identities | All 128 manifest rows matched |
| Run Item 7 tests | 188 passed |
| Run the repository test suite | 869 passed |
| Run scoped Ruff and basedpyright | Passed; type checker reported 0 findings |
| Inspect process cleanup | No Java, Minecraft, or Item 7 process remained |

The remote r9 tag and release metadata matched the committed publication receipt, and the download-2 asset hashes matched the four committed archive identities. The detached review worktree remained clean.
