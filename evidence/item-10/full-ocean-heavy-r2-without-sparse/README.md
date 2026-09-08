# Ocean-heavy repetition-2 control: retained heap-exhaustion failure

Status: FAILED GENERATION, RAW CUSTODY VERIFIED. This is not an accepted census.
Ten of sixteen planned worlds remain individually accepted. Protocol:
`item10-full-v1`, observer coverage `item10-observer-coverage-v2`.
Seed: `95920844204830198`. Source: `662de80c5a9aaa377bc91e28fd4d1fb92c78a34b`.

## Failure and lifecycle disposition

The unchanged [run receipt](run.json) records readiness and nine completed
selections through central End. Outer End stopped progressing at 3,640 of 4,225
requested chunks (86.15%); Nether was not attempted. The selected-area census
cannot be inferred from that requested-chunk progress. Duration to exit:
700.637 seconds. Harness session `62268` exited 1; Java exited 0 after operator
shutdown, with no process-group kill. Generation and lifecycle acceptance failed.

In archived `console.log`, lines 3641 through 3689 record failed loads for
chunks (495,529) and (500,532), `java.lang.OutOfMemoryError: Java heap space`,
and two chunk-load debug reports. Both reports are preserved under `debug/`.
Their line 61 confirms `-Xms1G -Xmx4G`. Their later memory snapshots do not
identify the allocation responsible for exhaustion. No heap dump was captured.
Do not infer an observer leak, a particular mod defect, or a required production
heap from this evidence alone.

Direct comparison with the [first control](../full-ocean-heavy-r1-without-sparse/run.json)
finds identical `run.preflight`, `probe` and lifecycle `selections`. That first
control completed under the same identity. This failed fresh repetition remains
part of the evidence; no retry or changed configuration has been executed.

The existing harness waits for selection completion or its operational timeout;
it did not initiate shutdown on these heap-exhaustion lines. After checking the
exact Java PID, process group and instance working directory, the operator used
its console pipe and the existing `mcpack_evidence.item7_console` functions:
`send_command` for `chunky pause`, then `begin_correlated_flush` and
`advance_correlated_flush` for response-gated save and stop. The
[emergency command record](emergency-shutdown.json) preserves the exact commands.
A 60-second confirmation allowance was set but was not exhausted.

Archived console lines 3692 through 3713 contain the pause, unique before marker,
exactly one ordered Saving/Saved sequence, matching after marker and stopping
message. Both process IDs were absent after exit. The harness receipt's
`save_all_flush: false` and `clean_stop: false` remain unchanged: its normal
end-of-generation flush phase was never reached. The separate operator flush
is corroborated by the raw log and does not convert incomplete generation into
a passing lifecycle or census. No server remains active.

## Preserved raw evidence and restore

The partial stopped-world backup contains 458 files totaling 383,745,514 bytes.
`world.tar.gz` is 137,772,497 bytes, SHA-256
`678ade6fb6b4179a23cbec1912528707c7a84df7a383571d18dc7ee01374edc3`.
The [world restore](world-restore.json) verifies all 458 files in a new target.
Restoring a failed world proves custody only, not complete generation.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ocean-heavy-r2-without-sparse-662de80c-failed-oom)
contains the archive and [manifest](archive-manifest.json). The fetched tag resolves
to the source above. Archive size: 138,020,297 bytes; SHA-256
`8b9e87f39850b4111b30cba418edb17f331681addb0797e9e2def793fa06ab2b`.
Its 315 files total 154,394,359 bytes before compression. Manifest SHA-256:
`bacb81fb59c00fa8cea7e7329da0fc8d96d28c74d7aab086723b2b7b9e0d925f`.
Both [local](local-restore.json) and [downloaded](download-restore.json) raw restores
verify all 315 members; the downloaded manifest is byte-identical.

Contents include the unchanged diagnostic, observer build and 50 captured
incoming classes, trace, console, Minecraft log, two debug reports, emergency
command record, sanitized configuration capture and partial world backup.
The existing Item 6 `capture(instance, output)` function preserved configuration
without changing the instance. Its 238 files include 228 baseline paths and ten
Chunky paths; Nether's task file was not generated. This is a failure capture,
not a passing full Item 10 configuration receipt. The original instance is kept.

## Reproduction and remaining decision

Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ocean-heavy-r2-without-sparse --mode probe --preset item10 --role ocean-heavy --arm without-sparse --repetition 2
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ocean-heavy-r2-without-sparse --archive evidence/raw/item10/item10-full-ocean-heavy-r2-without-sparse-662de80c-failed-oom.tar.gz --manifest evidence/item-10/full-ocean-heavy-r2-without-sparse/archive-manifest.json --revision 662de80c5a9aaa377bc91e28fd4d1fb92c78a34b
```

Use the [existing custody commands](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this run, failed archive name, source and world hash. All restore targets
must be new. The failure capture also called
`mcpack_evidence.item6_capture.capture` on this instance into `captured-config`,
and copied the stopped instance's `logs/latest.log` and `debug/` unchanged.

Full census was not run on the incomplete world. Under the frozen protocol,
a resource failure pauses collection and cannot reduce the sample. Assess the
heap failure and the harness's delayed failure handling before retrying or
continuing. Any retry must preserve this attempt, retain the frozen identity,
and have an explicit disposition and bounded policy. Do not change heap,
configuration, sampling, or count this attempt as a smaller successful world.
The exact allocation cause and the continuation decision remain unresolved.

## Narrow lifecycle correction after preservation

The demonstrated harness defect is delayed response to the exact logged
`java.lang.OutOfMemoryError: Java heap space` signature. The existing
`item7_lifecycle` now requests one `chunky pause` and reuses its response-gated
flush/stop path. Save confirmation has a 60-second allowance, also bounded by
the original run deadline. If that allowance expires or console I/O fails, the
existing process-group termination path applies. A completed emergency save
never converts the failed generation into an accepted run, even if all expected
selection markers had already arrived. The original source and raw receipt above
remain unchanged. The stopped Minecraft log is now captured on rejected runs
that reached readiness and exited zero, preserving shutdown diagnostics too.

This changes failure handling only. It does not alter the observer source/JAR,
heap, mods, configuration, seeds, generation selections, successful-run commands,
or accepted census processing. No new failure-recovery framework was added.
The allocation responsible for the resource failure remains UNKNOWN. The last
archived trace row records shutdown with zero unfinished attempts; that fact
alone cannot explain or exonerate any allocation source.

Validation: `uv run --no-sync pytest -q tests/item7/test_worldgen_lifecycle.py
tests/item7/test_item7_console.py tests/item10/test_collection_runner.py` passed
34 tests in 1.89 seconds. Added cases replay heap exhaustion before, during and
after selection completion, repeated error lines, later queued completion
markers, confirmed emergency save/stop and shutdown timeout with process-group
termination. These are harness tests, not a new Minecraft experiment or a claim
that heap exhaustion was repaired. Ruff check/format and focused basedpyright
checks pass. The full applicable gate remains required for the final PR candidate.
