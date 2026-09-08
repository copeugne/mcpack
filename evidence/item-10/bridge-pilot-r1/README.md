# Bridge fixed-frame diagnostic r1

The [predeclared diagnostic](../protocol.md#bridge-r1-bounded-natural-diagnostic)
ran at `84c4d21eee005dbe75dd8b5383ece2873094691c`. The
[run record](diagnostic.json) verifies fresh frozen runtime/configuration identity,
all four 81-chunk selections, correlated flush and clean exit 0 in 89.441 seconds.
No process-group kill occurred. The instance is stopped and preserved.

All fourteen bridge feature/template/processor hooks installed, with incoming
class bytes retained. No BridgeFeature attempt, configured-variant event, template
placement or processor write occurred. Positive bridge capture therefore remains
UNMET. This is not a zero-density estimate and does not authorize expanding the
frame to find a positive result. Saved bridge block corroboration is unavailable.
The complete mixed trace contains 1,290 attempts and 409 write events, and ends
with zero unfinished attempts. Mixed writes are raw observations, not accepted
bridge occurrences or selected-area densities. No Item 11 workflow ran.

Trace size: 450,494 bytes. SHA-256:
`e2fa1b75a2db93645d543f63b389ffb3425ae634f11eabdcb1ad415a7e79b575`.
The [archive manifest](archive-manifest.json) binds 280 files and 7,809,781
uncompressed bytes. Archive `item10-bridge-pilot-r1-84c4d21e.tar.gz` is 5,688,682
bytes, SHA-256 `f2e7452b9515b9ed1c9a8df8825ad5e6c8cade23309341e4f1739d795822c87c`.
The [release](https://github.com/copeugne/mcpack/releases/tag/item-10-bridge-pilot-2026-09-08-r1)
holds the immutable archive and manifest. The fetched tag matches the source
commit exactly. Downloaded manifest comparison passed byte for byte and the
[download restore](download-restore.json) verified every member.

The [world backup](world-backup.json) binds 103 files. Its nested archive is
5,412,909 bytes, SHA-256
`99fd5df2c0d6d25226e798bd92f69ba4b76a301df97cea1956ec418b1f7dcc7f`.
The existing restore tool succeeded, and all 103 restored paths, sizes and SHA-256
values matched the backup's sorted world_files list without booting. session.lock
is excluded. Local custody is under `evidence/raw/item10/bridge-pilot-r1-custody`.
Reproduce into absent destinations:

```sh
gh release download item-10-bridge-pilot-2026-09-08-r1 --dir DOWNLOAD
uv run --no-sync python -m tools.archive_item7_evidence restore --archive DOWNLOAD/item10-bridge-pilot-r1-84c4d21e.tar.gz --manifest evidence/item-10/bridge-pilot-r1/archive-manifest.json --target RESTORED_RAW --receipt RESTORE_RECEIPT.json
uv run --no-sync python -m tools.manage_item4_environment restore --archive RESTORED_RAW/world.tar.gz --sha256 99fd5df2c0d6d25226e798bd92f69ba4b76a301df97cea1956ec418b1f7dcc7f --target RESTORED_WORLD
```

These are the executed commands with destination placeholders. Direct derivation
of the raw counts is a JSONL count of `begin` and `write` kinds; bridge occurrence
absence is the absence of `bridge_configured` and bridge-class `feature` events.
Hook installation is recorded by `feature_installed`, not inferred from startup.
Collector validation is in the [probe report](../placement-probe.md#bridge-template-and-processor-preparation):
all 380 Item 7/10 tests and focused quality checks pass. Natural positive-path
validation and full Item 10 measurement remain incomplete.

## PR33 trace-integrity fix

[Finding 3955497336](https://github.com/copeugne/mcpack/pull/33#discussion_r3955497336)
is valid. Archive custody did not by itself validate the mixed trace's event
relationships and complete hook population. The existing trace reader now has a
bounded `--bridge-r1` mode. It binds trace and incoming class bytes to their
archived members, requires every declared installation, validates all mixed
attempt/write/parent/part relationships and healthy shutdown, and rejects bridge
feature/configuration/processor events for this zero-attempt diagnostic.

[Deterministic result](trace-validation.json) reproduces 1,290 attempts, 409 writes,
1,073 cave-parent urn attempts and six spiral parts from one source. The fourteen
bridge hooks are part of the complete installation set. This PASS is capture
integrity only, not a positive bridge placement or saved-block acceptance.

```sh
uv run --no-sync python -m tools.validate_item10_trace --bridge-r1 evidence/raw/item10/bridge-pilot-r1-custody/restored
uv run --no-sync pytest -q tests/item10/test_retained_trace.py
```

All 62 retained-trace tests pass. Added cases cover the actual retained archive,
missing hooks, unexpected bridge events, missing attempts, malformed write flags,
unhealthy shutdown, changed trace bytes and changed incoming class bytes.
Missing external raw data causes an explicit prerequisite skip. Focused Ruff and
basedpyright pass after correcting initial test lint findings. All six previous
feature trace results reproduce unchanged. Raw observations, archive, manifests,
release and restore receipts are unchanged; no archive revision is needed.
The full Item 7/10 gate for this bridge PR candidate passes all 388 tests in
84.09 seconds. A fresh Codex review is required before merge.
