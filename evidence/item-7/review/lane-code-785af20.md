# Item 7 code review at 785af20

- Exact revision: `785af200f51c28c7cd3183401ca306c589c8ee49`.
- Verdict: `FAIL`.
- Confidence: `HIGH`.

## Findings

1. `HIGH`: `OutputSequence.checkpoint_and_send` ordered reader publication, not server emission. A preexisting save pair delayed in the pipe or reader buffer could receive sequence numbers after the checkpoint and satisfy the main, gap, and control lifecycle state machines. The reviewer reproduced `state.flushed = True` with delayed generic messages. The retained line-order audit could not establish command causality.
2. `MEDIUM`: `src/mcpack_evidence/item7_completion_runs.py` contained 252 pure lines, two above the applicable 250-line ceiling.

The accepted-analysis and repeat-comparison rebuilds passed review. The reviewer also reproduced 197 Item 7 tests, scoped Ruff, and scoped basedpyright with zero diagnostics.

## Disposition

Commit `9b9a133` replaced reader checkpoints with unpredictable before and after console markers around `save-all flush` and added delayed-buffer regressions for all three runners. Commit `f4b915a` reused the canonical anomaly specifications and brought the completion module below the pure-line ceiling. Fresh empirical evidence remains required because r11 logs do not contain the new markers.
