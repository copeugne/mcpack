# Item 5 — Quantitative Measurement and Profiling Methodology

**Protocol:** `ae-measurement-v0.1`
**Platform:** Minecraft 1.21.1 / NeoForge 21.1.249 / Java 21
**Status:** binding for baseline forensics; final numeric budgets unresolved

## 1. Evidence contract

This protocol makes later claims reproducible and falsifiable. It defines how performance, exploration, structures, combat, dungeons, persistence, and loot are measured. It does not invent final acceptance budgets before the production host and baseline distributions exist.

Conclusions have distinct meanings:

1. `OBSERVED`: seen in an uncontrolled session.
2. `MEASURED`: a retained run satisfies this protocol and its schema.
3. `VERIFIED`: required seeds/replicates support the result and its declared comparison rule.

Every run records an immutable ID and UTC interval; purpose/scenario; Git commit and dirty state; protocol and build hashes; platform, JAR, config, datapack and world-snapshot identities; seed/dimension/route; host, heap and JVM flags; player/client load; warm-up and capture windows; raw artifact hashes; metric numerator, denominator, unit, aggregation and sample count; failures, exclusions and deviations.

A dirty worktree is allowed only for `exploratory` evidence and cannot support a freeze. Failed and outlying runs are retained. Secrets and player-identifying data are never retained.

## 2. Experimental design

### Development seed suite

| Role | Seed |
|---|---:|
| Ordinary | `42` |
| Mountainous | `6671238423019257953` |
| Ocean-heavy | `95920844204830198` |
| Biome-diverse | `-3503646078644842058` |

Comparisons pair the same seed, snapshot, route, host state, heap and commands. Destructive or mutating trials restore a hash-verified world first. Fresh generation uses untouched chunks. These are development seeds; v1 requires a separate blinded validation suite so tuning is not judged only on tuned worlds.

### Replication and sampling

- Deterministic inventory/config tests: one run plus a deterministic repeat.
- Runtime scenarios: one discarded warm-up replicate plus at least five measured replicates.
- Human gameplay: at least three runs per seed, transport mode and tested group size; route order rotates to reduce learning bias.
- Structure surveys: all four seeds, beginning at 4,096 unique fully generated chunks per seed. Expand in powers of two until each category has 30 observations or 32,768 chunks/seed. Fewer than 30 observations is reported as sparse/right-censored, not precise.
- Paired comparisons report absolute and percentage change, sample count, median, p95, p99, max, IQR/range and bootstrap 95% confidence interval.
- “Materially better” or “acceptable” requires a practical threshold declared before comparison. Until its owning item defines one, report measurements without accepting/rejecting the system.

Statistical outliers remain in the primary result. An additional sensitivity result may exclude one only for an objective recorded reason. A failed run receives a new run ID when repeated and is never silently replaced.

### Warm-up and interference

- Restart the server between performance replicates unless longevity is under test.
- Record cold/warm filesystem cache; never combine unlike cache states.
- Idle/combat use generated chunks; worldgen uses never-generated chunks.
- Idle stabilization is 10 minutes after `Done`; loaded-idle adds five stationary minutes. Capture is 10 minutes.
- Record other processes above 1% CPU or 250 MiB RAM.
- Disable unrelated backups, pregeneration and scans unless they are the scenario.
- Never run two profilers together unless overhead is the subject.

## 3. Spark contract

Spark `1.10.124` is pinned. `measurement/spark/config.json` disables background profiling and response broadcast to avoid hidden sampling and admin noise. The exact artifact proved these console commands:

```text
spark tps
spark health --memory
spark gc
spark profiler start --interval 4
spark profiler stop --save-to-file
```

The locally saved `.sparkprofile` is the retained evidence; web upload is optional. `spark health show --memory` failed on this build and is prohibited in automation. Spark's 20 TPS target and 50 ms real-time tick envelope are platform facts, not the pack's eventual p95/p99 budgets.

## 4. Performance methods

### Idle MSPT

Measure `idle-empty` (no players) and `idle-loaded` (one stationary player, fixed view/simulation distance at generated ordinary-seed spawn) separately. Capture tick median/p95/p99/max, TPS, heap/non-heap, process CPU, entities/block entities, GC and a saved profile for 10 minutes.

### Active-combat MSPT

Use versioned fixtures with exact arena geometry, entity IDs/equipment/effects, positions, reinforcement schedule and player actions. Capture first aggro through 60 seconds after the last hostile, minimum five minutes. Record tick distribution, TPS-loss duration, entity roles/types, navigation CPU, projectiles, damage events, duration and deaths. Test applicable P1/P2/P4/P6/P10 cases. More mobs is not equivalent to better difficulty.

### Fresh-worldgen and chunks

Restore an untouched seed and follow a versioned all-frontier route at controlled speed. Record chunks requested/completed/saved, throughput, latency median/p95/p99/max when exposed, tick distribution/time below 20 TPS, generation backlog each second, responsiveness probe every five seconds, CPU/memory/GC/disk, save duration and identifiable structure spikes. Cold and warm-cache variants are separate. Aircraft tests are later named scenarios, not substitutes for fixed-speed control.

### TPS/MSPT

TPS alone is invalid because it caps at 20. Report tick duration and seconds/percentage above 50 ms and eventual warning/failure budgets.

### Memory and GC

Sample RSS, heap used/committed/max and non-heap every 10 seconds. Record collector, count, total/p95/max pause where exposed, allocation trend and old-gen occupancy after natural collections. Formal runs use:

```text
-Xlog:gc*,safepoint:file=<run-dir>/gc.log:time,uptime,level,tags
```

Do not force GC in a primary run. A forced-GC diagnostic is separate. A leak requires a repeatable positive post-GC slope after stabilization; threshold/duration remain `PERF-006`.

### Entities and pathfinding

Sample loaded entities/block entities every five seconds by registry ID, dimension and chunk. Pathfinding uses versioned geometry, fixed starts/goals and identical populations. Record navigation/recalculation call-tree time, requests/failures/nodes when exposed, entity count and MSPT. Doors, vertical routes, chokepoints, water and unreachable targets have separate fixture IDs.

## 5. Adventure methods

### Structure identity, density and distance

A chunk counts only at full generation. A structure counts once at its unique start, never by intersecting pieces or repeated `/locate` hits. Record registry ID/family, dimension, start chunk, bounding box, biome, provisional tier, hostility and discoverability.

```text
structures_per_1000_chunks = unique starts / fully generated chunks * 1000
```

Use the same denominator for actionable locations, combat encounters, proper dungeons and major expeditions. Until Items 19/22 finalize categories, retain raw attributes alongside provisional labels. For each category report horizontal and route nearest-neighbor median/p95/max, clustering grids and proportion beyond declared radii; a global mean cannot prove even distribution.

### Exploration and travel

Run both 60-minute and 10,000-horizontal-block routes per mode. Record route, elevation, terrain fraction, actual speed, stops, map knowledge and whether content was visible, noticed, entered, actionable, hostile or completed. Modes are foot, horse, boat, train and aircraft when available. Train construction and operation time remain separate; aircraft records altitude and fresh/generated chunk state.

Report time-to-first and intervals between each tier, civilization, visual, actionable and hostile events. Dead travel means time with no meaningful interaction beyond continuous traversal.

### Discoverability

Approach ground-truth structures along declared bearings/height bands without location knowledge. Record first-visible/recognizable distance, entrance found, visibility-to-entry time, silhouette/entrance cues, concealment and false positives. `/locate` may establish truth only after the blind pass. Density and discoverability stay separate.

### Repetition

Version a family-equivalence map per build. Record unique families/player-hour, time/distance to first repeat, repeats per family/hour/10,000 blocks and repeated topology fingerprint frequency. Cosmetic palettes alone do not create a unique gameplay family.

### Adventure Activity Ratio

```text
AAR = meaningful interaction seconds / total expedition seconds
dead-travel percentage = dead-travel seconds / total expedition seconds * 100
```

Meaningful time includes navigation decisions, expedition-forced preparation, scouting, combat, traversal challenges, objectives, recovery, loot decisions, engineering deployment and return logistics. Uninterrupted forward travel and debug/admin activity do not count. Timestamped categories are mutually exclusive. Report the category breakdown with AAR.

### Dungeon quality and duration

Clock deliberate entry across the declared defended boundary through final exit or abandonment. Record time to objective, exit and total; split traversal, combat, search, objective, loot/inventory, rest/recovery, engineering/breaching, dead time and admin interruption.

Record rooms/useful/empty rooms, branches, graph depth, vertical span, encounters, chokepoints, hazards, finale, external access, bypass route and capability required. Retreat outcome is retained.

### Death rate and recovery

Report deaths/player-hour, deaths/expedition and encounter, wipes/expedition, median/p95 recovery time, unrecovered graves/items, cause, progression, tier and group size. Exploit tests remain separate. A death count without exposure/group size is invalid.

### Loot and salvage

Inventory generated containers before opening/automation: loot-table and item ID, count, components, rarity, instancing and source. Separately record obtainable blocks, machinery, spawners and salvage.

Value remains a vector until Item 28 sets weights: expedition utility, material replacement cost, equipment capability, engineering capability/input, discovery value, prestige, renewability/farmability and post-automation marginal value. Chest loot and salvage never collapse together. Diamond-equivalent value may supplement, never replace, the vector.

## 6. Player matrix

| ID | Players | Purpose |
|---|---:|---|
| P1 | 1 | solo viability/load |
| P2 | 2 | common cooperative pair |
| P4 | 4 | core group |
| P6 | 6 | upper normal concurrency |
| P10 | 10 | declared peak |

Grouped combat and independent explorers in different directions/dimensions are different scenarios. Synthetic clients establish technical load only, never pacing, discoverability, difficulty or enjoyment.

## 7. Claim gate and retention

A tuning claim is admissible only when its run JSON validates, artifacts/hashes survive, required scenario/seeds/players/replicates are present, failures/deviations are disclosed, paired comparison is used where possible, effect/dispersion are reported and the practical threshold was predeclared. Conclusions cannot exceed the instrument.

```text
measurement/{protocol-v0.1.json,run.schema.json,spark/config.json,templates/run.json}
evidence/measurement/<run-id>/{run.json,debug.log,gc.log,profile.sparkprofile,events.csv,metrics.csv}
```

Irrelevant evidence files may be omitted only when `run.json` explains why. Formal release evidence is archived with the matching Git tag and pack hash.

Final `PERF-001..012`, cadence, dungeon topology and loot-value targets remain downstream decisions. This permits honest baseline collection but forbids final acceptance until the owning item predeclares its threshold.


## 8. Enforced v1 artifacts (2026-09-02 continuation)

The earlier v0.1 prose above is design input. The executable authority is now `measurement/item5/protocol-v1.json`, validated by the strict models in `src/mcpack_evidence/item5.py`. It expands every shorthand method into all fields required by the continuation handoff and rejects incomplete coverage. The immutable Item 3 gameplay manifest remains 136 files; Spark is an explicit one-file instrumentation overlay described in the closure report rather than an undisclosed change to the retained stack.
