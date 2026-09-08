# Monster Box natural pilot r1: positive writes, acceptance pending

Source `59b43a6e20344f3362eec5679bff64bc778a9541`, ordinary seed 42, fresh
frozen-stack materialization, unchanged 324-chunk pilot. The committed
[protocol](../protocol.md#monster-box-natural-pilot-r1) preceded launch.
[Diagnostic](diagnostic.json) records readiness, all four selections, correlated
save and clean exit 0 in 88.452 seconds. No forced placements or tuning occurred.

Direct inspection of raw trace.jsonl finds 202 begin/feature/generator_end
sequences and seven successful Monster Box writes, with zero refused writes or
unfinished attempts. The trace is 47,907 bytes. These are provisional capture
counts, not validated occurrence counts or a density denominator. Generator calls
include generation outside the 81 selected Overworld chunks. Keep zero-write
calls and all coordinates. No other feature writes appear in this trace.

Next validate the archived event population and incoming class bindings, then
corroborate the seven saved blocks. No further generation is needed for these
checks. Successful server lifecycle alone does not accept the collector.

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
