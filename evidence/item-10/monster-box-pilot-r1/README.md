# Monster Box natural pilot r1: trace and saved blocks corroborated

Source `59b43a6e20344f3362eec5679bff64bc778a9541`, ordinary seed 42, fresh
frozen-stack materialization, unchanged 324-chunk pilot. The committed
[protocol](../protocol.md#monster-box-natural-pilot-r1) preceded launch.
[Diagnostic](diagnostic.json) records readiness, all four selections, correlated
save and clean exit 0 in 88.452 seconds. No forced placements or tuning occurred.

The [archive-bound trace check](trace-validation.json) finds 202 begin/feature/generator_end
sequences and seven successful Monster Box writes, with zero refused writes or
unfinished attempts. The trace is 47,907 bytes. These are validated capture counts, not density measurements or an exposure denominator. Generator calls
include generation outside the 81 selected Overworld chunks. Keep zero-write
calls and all coordinates. No other feature writes appear in this trace.

The [saved-block crosscheck](saved-block-crosscheck.json) corroborates all seven
successful writes at distinct coordinates. Two lie in full chunks and five in
initialize_light neighbors; these statuses are retained, not converted into
completed-chunk density exposure. All 202 attempts remain, including 195 without
writes. A null return in this derived summary means the generator returns void,
not a refused placement. Actual block-write results are retained independently.
Incoming MonsterBoxGenerator SHA-256 matches the retained class identity;
all nine installed incoming classes and the trace match the published archive.

The existing trace checker now handles the two bounded feature populations,
including generator_end without a fabricated boolean, and rejects more than one
write per Monster Box call under the frozen setting. The existing inspector has
a corresponding mode. Reproduce from the restored raw/world roots:

```sh
uv run --no-sync python -m tools.validate_item10_trace --monster-r1 evidence/raw/item10/monster-box-pilot-r1-custody/restored
uv run --no-sync python -c "import runpy; runpy.run_path('evidence/item-10/scarecrow-probe-r3/inspect-writes.py')" --monster-r1
```

Block-ID corroboration does not establish complete block-state equality or
collector noninterference. The BOP positive-path acceptance review remains open
in PR25; integrate that fix before final delivery of the shared validator.

## Raw custody

[Release](https://github.com/copeugne/mcpack/releases/tag/item-10-monster-box-pilot-2026-09-08-r1),
whose fetched tag resolves to the source commit above. Archive
`item10-monster-box-pilot-r1-59b43a6e.tar.gz` is 5,500,263 bytes, SHA-256
`bd17e4ea531cda14be0c23da015ca9f1e3af05d00ca14fef8ccff4c819d4c599`.
[Manifest](archive-manifest.json) binds 257 files. The downloaded manifest is
byte-identical; [download restore](download-restore.json) verifies every member.
The first archive-create call rejected absent output parents before writing;
creating the explicit custody and evidence directories resolved that prerequisite.
No raw evidence or source world was changed by the retry.

[World backup](world-backup.json) records 103 files and nested archive SHA-256
`ae2baecd801b08044a6f414e3a0fd70c128bfb177685ed02e2c0a4147e53f406`.
The [world restore](world-restore.json) was checked against every sorted manifest
path, size and SHA-256 without booting. Reuse the existing archive restore and
world restore tools with these identities; the raw archive root has no wrapper
directory. Local custody is under
`evidence/raw/item10/monster-box-pilot-r1-custody/{downloaded,restored,restored-world}`.

This is a diagnostic milestone, not Item 10 completion. Full occurrence coverage,
observer-cost measurement and density collection remain open. No Item 11 work ran.

Validation: all 322 Item 7/10 tests pass in 57.36 seconds. Changed Python Ruff
and validator/test basedpyright checks pass. No Item 11 workflow was run.
