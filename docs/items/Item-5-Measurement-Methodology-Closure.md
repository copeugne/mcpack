# Item 5 — Measurement and Profiling Methodology Closure

**Status:** `COMPLETE`
**Protocol:** `ae-measurement-v1`
**Date:** 2026-09-02

## Admission reconciliation

The handoff asked to confirm Spark inside the frozen 136-file retained manifest. Direct verification found that it is **not** in that manifest: Item 3 classified this server-optional instrument as `disabled_not_required_on_server`. The frozen manifest remains byte-identical at SHA-256 `78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb`; silently changing it would invalidate Items 3 and 4.

Item 5 therefore uses `measurement/item5/spark-overlay.json`: the unchanged 136-file gameplay stack plus the exact statically audited Spark artifact as a one-file, server-only profiling overlay. Its SHA-256 is `647e8a81afbe414dba1df4ba15fd06c5d32d4cb544e68828405e8e074c2e16db`, agreeing with Item 3 acquisition evidence. Effective profiling runtime count is 137. This resolves the wording conflict without pretending instrumentation is a gameplay dependency or rewriting the frozen admission set.

## Enforced protocol

`measurement/item5/protocol-v1.json` contains exactly 24 required metric contracts. Every contract supplies purpose, quantity, unit, executable procedure, warm-up, sampling interval/window, duration, repetitions, all four seeds, all five player cases, raw and processed formats/paths, aggregation, acceptance, invalid-run handling, uncertainty and environment hashes.

The player cases are material rather than invented: P1, P2 and P4 come directly from Item 5; normal uses the upper end of Item 2's recorded 2–6 range (P6), and peak uses Item 2's recorded P10. These remain intended load cases, not claims that the Cloud host sustains them.

Pydantic models forbid unknown or missing fields and enforce exact metric/player coverage. `tools/validate_item5.py` validates contracts, receipts and every referenced artifact hash. `tools/analyze_item5_samples.py` produces sorted deterministic JSON from immutable long-form CSV. Tests prove omissions, duplicates and missing fields are rejected.

Every total duration includes the maximum declared 900-second warm-up plus the complete capture window: 1,500 seconds for 600-second performance captures and 4,500 seconds for 3,600-second adventure captures. The deterministic analyzer emits count, minimum, median, mean, p95, p99, maximum, range, IQR, and a 10,000-resample percentile-bootstrap 95% confidence interval for the median. Pilot validation binds each receipt to the exact SHA-256 of the protocol supplied to the validator.

## Spark operational procedure

A clean seed-42 control is materialized from the Item 4 pristine platform and frozen retained manifest. Spark is copied only afterward from its hash-verified Item 3 acquisition path. Background profiling and response broadcasts are disabled. The bounded harness waits for `Done`, then sends:

```text
spark tps
spark health --memory
spark gc
spark profiler start --interval 4
spark profiler stop --save-to-file
save-all flush
stop
```

The sampler interval is 4 ms and capture is 30 seconds for the operational pilot; formal performance runs use each metric contract's warm-up and window instead. A local `.sparkprofile` is mandatory. Uploads and screenshots are neither required nor accepted as sole evidence. Console permission is the dedicated-server operator console; a remote player or command block is not part of this method.

Profiler overhead must be measured by alternating at least five paired, same-seed/no-player captures with and without the 4 ms sampler and reporting the MSPT/RSS differences and confidence interval. Until that experiment is run, overhead is `UNKNOWN`; a profiled capture cannot establish an unprofiled performance budget. Profiler startup/stop failure, absent local output, early shutdown, malformed output, or hash mismatch rejects but never deletes the run.

## Pilot and failure preservation

The first full-stack pilot exposed a real orchestration defect: the harness flushed/stopped while Spark was still assembling profile metadata. Spark saved a local profile but logged `Server already shutting down`, so the run is rejected for profiling evidence even though shutdown itself was clean. The raw profile, compressed log, lifecycle receipt and rejected run receipt are preserved.

The corrected harness waits for `Profiler stopped & save complete!` before flushing and stopping. The accepted pilot receipt records exact commands, timestamps, runtime identities, seed, raw artifacts, deterministic processed output and hashes. The validator requires both accepted and rejected paths whenever pilot receipts are supplied.

## Exit gate

**PASS.** The corrected clean full-stack pilot ran the profiler for 30 seconds measured from Spark’s asynchronous start confirmation, saved a 61,880-byte local profile, completed `save-all flush`, and stopped with exit code 0. Both accepted and rejected evidence paths validate with all artifact hashes. This operational pilot proves collection, preservation, processing and rejection handling; its short, dirty-worktree startup sample is explicitly not a performance baseline or tuning claim. Item 6 is eligible.
