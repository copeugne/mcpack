# Item 7 rejected exact-SHA review at 785af20

- Reviewed revision: `785af200f51c28c7cd3183401ca306c589c8ee49`.
- Aggregate verdict: `REJECTED`.
- Goal lane: `PASS`.
- Code lane: `FAIL`.
- Integrity lane: `PASS`.
- Hands-on QA lane: `PASS` on the incomplete declared surface.
- Context lane: `FAIL`.
- Runtime debugging lane: `FAIL`.

The candidate was rejected for three valid findings: reader-assigned sequence numbers did not prove that save output followed the flush command, both handoffs understated the current local revision boundary, and the audit embedded the caller's manifest path. The code lane also found a 252-pure-line module.

Commits `edd6fa7`, `9b9a133`, `f4b915a`, and `4e9d737` address the findings. The causal fix invalidates r11's generic line-order audit as final acceptance evidence. Replacement runtime evidence must contain matching unpredictable before and after markers around every accepted `save-all flush`, be archived under a new source-bound custody revision, rebuild completion, and pass a fresh exact-SHA review.

The authoritative lane records are the six sibling `lane-*-785af20.md` files. Agent transcripts, temporary QA directories, `.omo`, and untracked files are not acceptance evidence.
