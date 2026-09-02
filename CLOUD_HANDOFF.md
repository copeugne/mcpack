# Cloud Handoff — Items 5–10 Continuation

## 1. Authority and restart rule

This file is the authoritative continuation handoff as of **2026-09-02 UTC**. Read it in full, then read `SPECS.md` in full before changing the repository. `SPECS.md` remains the authoritative chronological and dependency-ordered requirements document; this handoff records actual repository and runtime state.

Do not redo completed Items 2–4 unless verification or later evidence invalidates a gate. Do not begin Item 11. Continue autonomously in strict order:

1. Item 5 measurement and profiling methodology;
2. Item 6 generated-configuration audit;
3. Item 7 real-world generation inspection;
4. Item 8 structure-family enumeration;
5. Item 9 structure classification;
6. Item 10 representative-region validation and density analysis;
7. final Items 2–10 cross-item audit;
8. report whether Item 11 is eligible, without implementing it.

The exact restart point is:

> **Item 5 — configure and validate Spark, then make every required metric operational and reproducible.**

## 2. Current Git and delivery state

- Repository: `/workspace/mcpack`.
- Branch: `work`.
- Item 4 gate commit: `994492c docs(item4): close deterministic environment gate`.
- Item 4 lifecycle commits:
  - `5821bd6 feat(item4): add deterministic environment lifecycle tooling`;
  - `ba31fff feat(item4): automate readiness-driven server lifecycle`.
- Review-fix commit: `316c341 fix(item4): address environment lifecycle review`.
- Lock-compatibility review fix: `57c900b fix(item4): use Minecraft-compatible world locking`.
- Synchronization merge before the review fixes: `845f954 Merge remote-tracking branch 'origin/main' into work`.
- Validated Item 4 tag already pushed: `item-4-controlled-environment-2026-09-02` (points to `845f954`; do not move or rewrite it).
- Pull request: <https://github.com/copeugne/mcpack/pull/6> (`work` into `main`).
- PR #6 originally had three inline findings. Commit `316c341` addresses all three:
  1. an existing empty pristine `mods/` directory is accepted and a non-empty one is rejected;
  2. lifecycle timeout enforcement now uses a reader thread plus a queue deadline and kills the complete process group if the server is silent;
  3. a real persistent daily systemd backup timer and stopped-world backup runner are committed.
- Commit `316c341` and this handoff are pushed. All three review threads were answered and resolved, the PR body was updated to 57 total tests / 8 Item 4 tests, and a new `@codex review` was requested. At handoff, GitHub reported the PR mergeable and clean with no unresolved threads.
- A later review correctly identified that BSD `flock` does not contend with Java `FileChannel` locks. Commit `57c900b` switches the guard to a read/write POSIX record lock via `lockf`, adds a cross-process regression test, and is pushed. That thread was answered/resolved; the PR body now records 58 total tests / 9 Item 4 tests and another review was requested.
- Before new Item 5 work, run `git status`, fetch `origin/main`, and merge it if it advanced. Do not rewrite valid commits.

## 3. Exit-gate status

| Item | Status | Authoritative evidence / note |
|---|---|---|
| 1 | Design contract exists in project history; outside this continuation's implementation scope | Re-audit only in final cross-item review where relevant. |
| 2 | **Complete** | `docs/items/Item-2-Frozen-Technical-Baseline.md`, `evidence/item-2/`, platform tooling and reconstruction tests. |
| 3 | **Complete** | `docs/items/Item-3-Exact-Version-and-Dependency-Audit.md`, `evidence/item-3/final-compatibility-matrix.json`, retained-provider evaluation, and runtime evidence. PR #5 is merged. |
| 4 | **Complete**, subject to PR #6 review completion | `docs/items/Item-4-Controlled-Test-Environment-Closure.md`, `evidence/item-4/`, lifecycle/backup/restore tooling and tests. |
| 5 | **Incomplete; exact next item** | Existing reconstructed prose/schemas are not accepted closure. |
| 6 | **Pending; blocked by Item 5** | Generated configs exist only in ignored runtime instances; audit them only after Item 5 passes and do not tune first. |
| 7 | **Pending; blocked by Item 6** | Item 4 boot evidence is not Item 7 world inspection. |
| 8 | **Pending; blocked by Item 7** | Existing reconstructed inventory is not sufficient runtime proof. |
| 9 | **Pending; blocked by Item 8** | Existing provisional report must be regenerated from verified Item 8 families. |
| 10 | **Pending; blocked by Item 9** | Existing reconstructed density report/tooling is not accepted empirical closure. |
| 11 | **NOT AUTHORIZED** | Do not implement, run, repair, or lint Item 11-specific workflows as part of Items 5–10. |

## 4. Item 3 frozen result used downstream

The dedicated-server admission set contains exactly **136 candidates**. The retained manifest is:

- `evidence/item-3/runtime/retained-server-candidates.txt`;
- SHA-256 `78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb`.

Targets are Minecraft `1.21.1`, NeoForge `21.1.249`, and Temurin `21.0.12.1+1-LTS`, with `-Xms1G -Xmx4G`. Do not silently re-enable Sable, bundled Aeronautics, Every Compat, the statically rejected spell-engine family, or Simply More/Simply Tooltips. If later runtime evidence contradicts Item 3, reopen Item 3 and repeat affected downstream validation.

## 5. Item 4 completed environment

### 5.1 Versioned controls

Configuration version: `test-environment-v0.1`.

Seed controls in `test-environment/seed-suite.json`:

| Role | Seed |
|---|---:|
| ordinary | `42` |
| mountainous | `6671238423019257953` |
| ocean-heavy | `95920844204830198` |
| biome-diverse | `-3503646078644842058` |

All four were independently materialized with the exact retained set, reached readiness, completed `save-all flush`, and stopped cleanly. Evidence is in `evidence/item-4/runtime-validation.json` and compressed logs under `evidence/item-4/logs/`.

### 5.2 Backup/restore proof

The ordinary control was backed up only after flush and stop:

- 58 world files;
- archive size 1,190,041 bytes;
- archive SHA-256 `2df51369e1c31407f5eb91f0db04f39c631ee0df712235831c2e2853dbe4a772`;
- per-file receipt: `evidence/item-4/ordinary-backup-receipt.json`.

The archive was verified before safe extraction into an absent target. The restored world reached readiness in 62.224 seconds, flushed, and stopped cleanly. See `evidence/item-4/ordinary-restore-receipt.json` and `evidence/item-4/logs/ordinary-restored-boot.log.gz`.

### 5.3 Lifecycle and backup tooling

- `tools/manage_item4_environment.py`:
  - refuses destructive target reuse;
  - verifies retained artifacts before materialization;
  - accepts an existing **empty** pristine `mods/` directory but rejects content;
  - removes a copied pristine `world/` before applying the selected role seed, ensuring first boot generates that seed;
  - writes deterministic seed properties;
  - creates normalized deterministic stopped-world archives;
  - verifies archive hash before extraction;
  - rejects unsafe tar members;
  - holds the Minecraft-compatible POSIX record lock through archive creation and receipt hashing, excludes `session.lock` from backup content to avoid releasing process-scoped locks by closing another descriptor, and refuses a live-world backup (do not replace it with BSD `flock`).
- `tools/run_item4_server_lifecycle.py`:
  - waits for readiness;
  - issues `save-all flush`;
  - waits for `Saved the game`;
  - requests stop;
  - enforces the deadline even if stdout becomes silent;
  - kills the process group on timeout.
- `infrastructure/bin/item4-automated-backup` and `infrastructure/systemd/mcpack-item4-backup@.{service,timer}`:
  - daily 03:15 UTC schedule;
  - persistent catch-up;
  - randomized delay;
  - one instance per seed role;
  - fails rather than backing up a live world.

The Cloud container may not run systemd. The committed service/timer is the configuration deliverable; host installation commands are in `test-environment/README.md`. Do not represent the timer as running in this container unless `systemctl` verification was actually performed.

### 5.4 Preserved failure

A first mountainous attempt used a fixed five-minute command delay. It reached readiness but the unchanged watchdog terminated a later tick before the command arrived. Its log and crash report are preserved under `evidence/item-4/failures/`. The control was deleted, rematerialized, and rerun with the readiness-driven harness; that run passed without tuning any baseline control. Keep this failure in the audit trail.

### 5.5 Runtime state caveat

`instances/`, `downloads/`, `backups/`, and `evidence/raw/` are intentionally ignored. They may exist in the current container but are not durable Git inputs. A future environment must reacquire candidates, provision the pinned platform, and rematerialize controls using committed evidence and tooling. Never claim ignored runtime state exists without checking it.

## 6. Exact next actions

1. Read this handoff and `SPECS.md` completely.
2. Run `git status --short` and inspect `git log --oneline --decorate -10`.
3. Fetch `origin/main`; merge it before Item 5 if it advanced. Do not rewrite Item 4 commits.
4. Query PR #6 for any review submitted after handoff commit `d76e40a`; address new valid findings before relying on the Item 4 gate.
5. If no new finding reopens Item 4, begin Item 5 immediately at section 7 below.
6. Do **not** wait idly for review if Item 5 work can proceed safely on the same dependency-ordered branch.

## 7. Item 5 — exact remaining work

Re-read `SPECS.md` Item 5 before implementation. `docs/items/Item-5-Measurement-Methodology.md`, `docs/items/Item-5-Measurement-Methodology-Closure.md`, `measurement/*.json`, and any old reports are reconstructed starting material only. They must not be marked accepted merely because files exist.

### 7.1 Spark

1. Confirm `spark-1.10.124-neoforge.jar` is in the retained 136 manifest and its exact hash agrees with Item 3 evidence.
2. Rematerialize a clean Item 5 control from Item 4 inputs; do not reuse a mutated Item 4 proof world as a baseline.
3. Boot the retained stack and verify Spark loads from runtime logs.
4. Record exact Spark commands, permissions, output locations, sampling overhead, warm-up, duration, and failure behavior.
5. Preserve a raw Spark output example and a machine-readable receipt. Do not rely on screenshots or web links alone.

### 7.2 Required metric contracts

For **every** metric below, define and implement:

- purpose and exact measured quantity;
- unit;
- collection command/procedure;
- warm-up behavior;
- sample interval/window;
- total run duration;
- repetitions;
- seed cases;
- player-count cases;
- raw format and path;
- processed format and path;
- aggregation/statistic;
- acceptance rule;
- rejection/invalid-run rule;
- uncertainty treatment;
- relevant environment hashes.

Performance metrics:

- idle MSPT;
- active-combat MSPT;
- fresh-worldgen MSPT;
- TPS;
- memory;
- garbage collection;
- entity count;
- pathfinding cost;
- chunk-generation cost/time.

Adventure/world metrics:

- structure count and structures per 1,000 chunks;
- actionable locations per 1,000 chunks;
- combat encounters per 1,000 chunks;
- proper dungeons per 1,000 chunks;
- major expeditions per 1,000 chunks;
- structure distance/inter-structure distance;
- travel time;
- dungeon duration;
- death rate;
- loot value;
- unique structure families per hour;
- time to first repeated structure family;
- repeated dungeon-layout frequency;
- Adventure Activity Ratio = meaningful interaction time / total expedition time.

Player-count cases:

- solo;
- 2 players;
- 4 players;
- expected normal concurrency;
- expected peak concurrency.

Do not invent normal/peak values if the design/baseline evidence does not establish them. Record the unresolved input explicitly and use the known cases without claiming the gate until the specification's cases are materially defined.

### 7.3 Item 5 implementation expectations

- Use schemas/models that reject missing methodology fields.
- Separate immutable raw data from processed output.
- Add deterministic analyzers with tests and fixtures.
- Add a validation command that checks every required metric and player case is covered.
- Run at least one end-to-end pilot that proves collection, raw preservation, processing, and rejection handling; a prose-only methodology does not pass.
- Preserve exact commands, runtime identity, retained manifest hash, configuration version, seed, and timestamps.
- Explicitly assess the Item 5 exit gate before proceeding to Item 6.
- Commit implementation, tests, evidence, and documentation as coherent atomic units.

## 8. Item 6 — generated configuration audit after Item 5 passes

1. Use actual configs generated by clean Item 4/5 retained-stack boots; do not infer from upstream docs when generated files exist.
2. Freeze a hash manifest before tuning anything.
3. Record generated defaults, effective defaults, and every non-default value.
4. Audit spacing, disabled sets, spawn changes, difficulty changes, performance interactions, worldgen interactions, structure interactions, and mod-to-mod config interactions.
5. Explicitly record expected systems that are absent.
6. Cover, when present: Sparse Structures, Structure Essentials, ServerCore, C2ME, Chunky, Structure Layout Optimizer, When Dungeons Arise, YUNG systems, IDAS, Moog systems, village generation, Loot Integrations, spawning, and difficulty.
7. Preserve the original generated tree or a lossless deterministic archive plus per-file manifest.
8. Do not tune during this baseline audit.
9. Validate report-to-manifest consistency before starting Item 7.

## 9. Item 7 — real-world generation inspection after Item 6

1. Regenerate clean worlds for all four deterministic seeds under the frozen config snapshot.
2. Inspect actual terrain, biomes, structures, dimensions, cross-mod generation, boundaries, pathological generation, and expected content presence.
3. Preserve traceable evidence for each observation: seed, dimension, coordinates, command, log, screenshot where applicable, world manifest/hash, observation, anomaly, confidence, and limitation.
4. Synthetic registry enumeration is not a substitute for real-world evidence.
5. Preserve failures and uncertain observations.
6. Validate the Item 7 evidence inventory before Item 8.

## 10. Item 8 — structure-family enumeration after Item 7

Enumerate every relevant gameplay family using registries, datapacks, packaged mod data, runtime evidence, and generated-world evidence. For each family record canonical ID, namespace, source, family/group, placement/biome/dimension/generation constraints, physical footprint, hostility, mobs, loot, spawners, progression significance, discoverability, variants, aliases, runtime verification, evidence, confidence, and uncertainty.

Do not count aliases, pools, pieces, variants, or implementation details as separate gameplay families unless the classification rules require it. Add completeness and uniqueness checks. Existing reconstructed inventories are hints, not closure.

## 11. Item 9 — classification after Item 8

Classify every verified family into Tier 0, 1, 2, 3, 4, or Civilization using `SPECS.md` criteria. Cite evidence per row and record confidence/ambiguity/gameplay characteristics. Explicitly flag decorative, empty, redundant, pseudo-dungeon, visually substantial but low-gameplay, and uncertain families. Do not force confidence.

Machine-readable and human-readable outputs must agree exactly, with tests for full coverage and valid tiers.

## 12. Item 10 — representative regions and density after Item 9

Generate validated representative regions for all required seeds. Preserve raw structure starts/encounters and measure:

- raw structure density;
- encounter density;
- gameplay-relevant density and value;
- travel and inter-structure distances;
- clustering;
- empty-region frequency and extent;
- biome variation;
- seed variation;
- dimensional variation;
- Sparse Structures' actual effect.

Distinguish raw structure count from useful encounters. Preserve seeds, region boundaries, coordinates, manifests, logs, raw data, processing code, statistical summaries, uncertainty, integrity hashes, and reproduction instructions. Analyses must regenerate from committed/preserved raw data. Verify the Item 10 exit gate explicitly.

## 13. Final Items 2–10 audit

After Item 10 passes:

1. Re-read `SPECS.md` Items 2–10 completely.
2. Verify every checkbox and exit gate against actual evidence, not old status prose.
3. Recompute hashes/manifests and check all referenced paths.
4. Confirm machine/human reports agree.
5. Search authorized scope for unresolved TODO/FIXME/placeholders and reconstructed claims presented as empirical evidence.
6. Check later evidence for contradictions with Items 2–4; reopen and repeat downstream validation where necessary.
7. Run the full project suite, static typing, applicable lint/format checks, shell tests, and evidence validators.
8. Inspect full commit sequence, tags, branch/remote state, and PR state.
9. Push validated milestone tags only under the existing convention; never move existing tags.
10. Explicitly report whether Item 11 prerequisites pass. Do not implement Item 11.

## 14. Validation baseline at handoff

Before the review-fix commit, the repository passed:

- `uv run pytest -q` — 55 tests;
- `uv run pytest -q tests/item4` — 6 tests;
- `uv run basedpyright src tests` — 0 errors and 0 warnings;
- scoped Ruff checks and formatting;
- four full retained-stack seed lifecycles;
- one real backup/restore and restored-world lifecycle.

After commit `316c341`, focused Item 4 validation passed:

- `uv run pytest -q tests/item4` — 8 tests;
- `bash tests/infrastructure/test_item4_backup_schedule.sh` — pass;
- scoped Ruff — pass;
- `uv run basedpyright src tests` — 0 errors and 0 warnings;
- `git diff --check` — pass.

After commit `57c900b`, focused Item 4 validation passed with 9 tests, including a separate process holding the same POSIX record-lock class used by Minecraft/Java. The complete suite passed with 58 tests. A future test not rerun must not be represented as passing at a newer head.

## 15. Git discipline

- Inspect `git status`, unstaged diff, staged diff, and recent log before every commit.
- Preserve atomic commits; do not squash or rewrite valid history.
- Commit code/tests, evidence, and documentation in coherent units rather than a single catch-all commit.
- Push regularly after validation.
- Keep PR bodies current with exact tests, evidence, limitations, exit gates, and unresolved uncertainty.
- Never commit candidate JARs, Minecraft/NeoForge binaries, worlds, unredacted secrets, or operational caches.
- Compressed UTF-8 logs/crash reports are evidence, not executables; record their hashes and purpose.

## 16. Prohibited shortcuts

- Do not begin Item 11.
- Do not skip dependency order.
- Do not treat Item 4 boot logs as Item 7 inspection.
- Do not tune generated configs before Item 6 freezes/audits them.
- Do not claim runtime measurements from methodology prose.
- Do not treat Fabric metadata as active NeoForge metadata.
- Do not assume Forge equivalence.
- Do not discard failed runs or uncertainty.
- Do not use reconstructed Item 5–10 documents as empirical proof without regenerating and validating their evidence.
- Do not claim systemd timers are active in Cloud without actual `systemctl` evidence.

## 17. Stop condition

Continue through Items 5–10 without stopping at intermediate milestones. Stop only when:

- Items 2–10 have passed the final cross-item audit, with Item 11 eligibility reported but Item 11 untouched; or
- a genuine external blocker prevents meaningful progress after reasonable investigation and preservation of failure evidence.
