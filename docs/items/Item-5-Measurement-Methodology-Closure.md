# Item 5 — Measurement and Profiling Methodology Closure

**Status:** `COMPLETE`
**Protocol:** `ae-measurement-v0.1`
**Date:** 2026-09-01

## Exit gate

**PASS.** Every later tuning claim now has a defined measurement family, provenance envelope, sampling rule, raw-data contract and decision gate. Numeric design budgets remain explicitly unresolved and cannot be chosen after seeing favorable candidate results.

## Coverage

| Requirement | Definition |
|---|---|
| Idle MSPT | Empty and one-player loaded 10-minute captures after controlled stabilization |
| Combat MSPT | Versioned fixtures; tick distribution, TPS loss, entities, navigation and projectiles |
| Fresh worldgen | Untouched snapshots, fixed frontier route, cache split, backlog and responsiveness |
| TPS | Time series paired with tick duration; TPS alone is insufficient |
| Memory/GC | 10-second memory samples, Spark summary and JVM GC/safepoint log; no forced primary GC |
| Entities/pathfinding | Registry/dimension/chunk counts and fixed navigation fixtures |
| Chunk generation | Requested/completed/saved counts, latency, throughput, backlog and save duration |
| Structures/distance | Unique starts per fully generated chunk, sequential four-seed sampling and spatial distribution |
| Travel/dungeons/death | Fixed routes; phase-coded dungeon time; exposure-normalized deaths and recovery |
| Loot/salvage | Separate inventories with multi-axis capability/economic value |
| Exploration | Five requested per-1,000-chunk rates with explicit denominator |
| Repetition | Family/hour, time/distance to repeat and topology fingerprints |
| Activity Ratio | Timestamped meaningful seconds divided by expedition seconds plus category breakdown |
| Player counts | P1, P2, P4, P6 and P10; grouped and distributed loads separated |

## Spark proof

Spark `1.10.124`, SHA-256 `647e8a81afbe414dba1df4ba15fd06c5d32d4cb544e68828405e8e074c2e16db`, ran as the only third-party mod on a hash-verified restored seed-42 world. `spark tps`, `spark health --memory`, `spark gc`, manual start and local-file stop all succeeded. The local profile, debug log, activity file and restore receipt are hash-retained. Save and shutdown were clean.

`spark health show --memory` failed for the exact pin and is excluded. The smoke is labelled exploratory because it predates the committed method and deliberately omits benchmark windows.

## Enforced artifacts

- `measurement/protocol-v0.1.json`: seeds, players, samples, windows and comparison rules.
- `measurement/run.schema.json`: retained run contract.
- `measurement/templates/run.json`: non-evidence starter.
- `tools/validate_measurement_run.py`: project invariants plus optional JSON Schema validation.
- `measurement/spark/config.json`: no background profiler or response broadcast.

Production hardware and numeric performance/cadence/loot budgets remain `UNKNOWN`. Baselines may be measured; final acceptance must wait for predeclared owning-item thresholds.

