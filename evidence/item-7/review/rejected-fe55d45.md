# Item 7 rejected GitHub Codex review at fe55d45

Reviewed revision: `fe55d451bf081341101fc541ead992113133ab5b`

Pull request: `https://github.com/copeugne/mcpack/pull/15`

Review completed: `2026-09-04T15:41:39Z`

Verdict: `REJECTED`

The completed GitHub Codex review reported two technically valid P1 findings:

1. Completion accepted the derived warning audit and disposition without rebuilding the audit from, or binding, every declared raw warning log. Source: `https://github.com/copeugne/mcpack/pull/15#discussion_r3935582647`.
2. Completion accepted the derived control comparison without binding its control and pilot chunk streams and run receipts to the raw files. Source: `https://github.com/copeugne/mcpack/pull/15#discussion_r3935582654`.

Disposition:

- Two focused RED tests reproduced the missing source-binding behavior.
- Commit `fb901b1050f211cb88fe1fb9d074f5d7c1e17407` rebuilds the warning audit from all 11 declared raw logs, requires exact equality with the accepted derived audit, and binds every warning source to the completion artifacts.
- The same commit verifies the embedded path, SHA-256, byte size, and JSONL record count for the control receipt, control chunks, pilot receipt, and pilot chunks, then binds all four raw files to completion.
- Duplicate artifact paths are retained once. Three warning logs were already provider evidence, so the completed artifact set grows from 125 to 137 rather than 140.
- The focused and repository suites pass with 188 Item 7 tests and 869 total tests. Ruff, basedpyright, shell syntax, and the real completion rebuild also pass.
- Because the completion implementation changed after r8, r8 remains preserved history. The corrected final custody source is release `item-7-raw-evidence-2026-09-04-r9`, tagged at `fb901b1050f211cb88fe1fb9d074f5d7c1e17407`.

This rejected review is not approval. The corrected candidate still requires fresh exact-SHA local review, a completed clean GitHub Codex review cycle, merge into `main`, and delivered-ref verification.
