# Historical Cloud Handoff - Items 5-10 Continuation

> Historical checkpoint: this file records the repository state on 2026-09-03 UTC and is not the current continuation authority. Use `SPECS.md`, the master execution status in `Adventure-Engineering-Pack-Execution-Ledger.md`, and current Git/GitHub state for present status. The dated instructions below are preserved as recovery history.

## Current continuation checkpoint - 2026-09-04

This section supersedes the dated status and restart instructions below. Preserve the rest of this file as recovery history. `SPECS.md` remains the dependency-ordered requirements authority, and `Adventure-Engineering-Pack-Execution-Ledger.md` remains the status and evidence vocabulary authority.

### Git and delivery state

- A fresh fetch on 2026-09-04 found `origin/main` at `eb84d842a7b108863dcdd4c86435a875f8a0c575` with no newer remote commits. The active branch is `experiment/item-7-worldgen-audit`, based on that ref. Its final r3 machine evidence is committed in `7bcce66` before this reconciliation increment.
- PR #11 merged Item 5 delivery as `398bf59b3a89669ec402026d52250c2b86e54047`.
- PR #12 merged the initial Item 6 generated-default capture as `895ed1d999cd22ca511035e666ad8ac308ae63c1`.
- PR #14 merged the completed Item 6 audit as `f38ea66ecc28911c33d525dcde26434853673ad3`. Its final Codex review completed against `96a914c8a457d2f23698cdaeba18c6ed899b56d1` and reported no major issues. The GitHub API currently exposes no thumbs-up reaction on that cycle, so do not claim that reaction; preserve this as a review-record discrepancy unless later evidence resolves it.
- `eb84d842a7b108863dcdd4c86435a875f8a0c575` only renamed `CLAUDE.md` to `AGENTS.md` after the Item 6 merge.
- Item 7 final raw evidence is durably published at `https://github.com/copeugne/mcpack/releases/tag/item-7-raw-evidence-2026-09-04-r3`. The annotated tag resolves to source revision `4503d647b81fbb15bc7f577d91df01867aa90e79`, and all four assets passed restore verification plus two independent remote downloads and hash checks. The first and r2 releases remain preserved as superseded custody attempts. All three releases have identical asset sizes and SHA-256 values.
- Exact-SHA reviews at `97262a21b0b76c253f57e32b8665e48d0a63f822`, `8c7e7b8bb5db79d826b78cab5a678605a8b5fc23`, and `438260f40fd0d50ff5f087a2b8aac028d5a39927` returned `REJECTED`. Their valid findings drove clean-export, descriptor custody, locking, strict-schema, repository-binding, destination-publication, active mutation-test, and fresh-release corrections. All three rejected reviews are preserved under `evidence/item-7/review/`. A fresh final-SHA review remains mandatory.
- Preserve the existing untracked `.codegraph`, `.omo/`, and `mcpack-reconstructed-28(1).bundle` paths. Committed evidence belongs under `evidence/`; acceptance-relevant source, tools, tests, and exact commands must remain tracked for reproduction.

### Current gate status

| Item | Current status | Evidence-bound meaning |
|---:|---|---|
| 1 | `COMPLETE` | The design contract and Earned Sandbox Freedom Doctrine remain binding. |
| 2 | `COMPLETE` | Reconstructed baseline evidence, clean-room proof, durable retrieval, and Git receipts pass. |
| 3 | `COMPLETE` | All 190 candidates have dispositions; the exact 136-candidate retained dedicated-server set passed its scoped static and lifecycle gate. |
| 4 | `COMPLETE` | The isolated four-seed environment and backup/restore gate pass. |
| 5 | `COMPLETE` | The versioned measurement protocol, strict evidence tooling, and pinned-Temurin pilot gate pass. Spark overhead remains `UNKNOWN`, and the pilot is not a performance baseline. |
| 6 | `COMPLETE` | The untouched retained-stack configuration is frozen and audited. The manifest contains 228 paths, with 88 audited and 140 explicitly out of scope. No tuning was performed. |
| 7 | `PASS`, delivery pending | Two fresh four-seed runs inspected 54,816 exact selected chunks. The 192 anomaly rows, 762 packaged structure restrictions, all 37 provider-component dispositions, 1,222 warning signatures, 128 reviewed captures, final r3 restore-tested archives, and 124-artifact completion receipt pass. Three exact-SHA reviews were rejected and their valid findings were fixed. Fresh exact-SHA review, GitHub Codex review, merge, and delivered-ref verification remain. |
| 8 | `BLOCKED` by Item 7 delivery | Begin the runtime-backed canonical structure inventory only after the Item 7 pull request is cleanly reviewed, merged into `main`, and verified. |
| 9 | `BLOCKED` by Item 8 | Reclassify every verified family exactly once only after Item 8 passes. |
| 10 | `BLOCKED` by Items 7 through 9 | Regenerate and preserve predeclared density evidence only after the preceding gates pass. |
| 11 | `BLOCKED` | Do not implement, run, repair, or lint Item 11 before the final Items 2 through 10 audit passes. It also requires at least two blind human operators. |

The Item 7 completion command returns `PASS` and records 124 exact artifacts in `evidence/item-7/completion.json`. After the first GitHub review fixes, the focused Item 7 suite passes with 173 tests and the full repository suite passes with 854 tests. The final candidate requires a clean-export gate. The repository-bound r3 verifier redownloaded all four assets and matched every committed size and SHA-256.

### Exact continuation point

1. Treat `evidence/item-7/completion.json` and `docs/items/Item-7-Baseline-Worldgen-Audit.md` as the current acceptance summary. The former zero-mod report is superseded historical context.
2. Preserve the measured semantic nondeterminism. Run A and Run B differ outside the central End; input drift and comparator artifacts were refuted, but the causal provider remains `UNKNOWN`. Do not tune the frozen Item 6 configuration inside Item 7.
3. Preserve the confirmed Better Caves generation failure, the unresolved YUNG's Bridges and YUNG's Extras identifiers, and the 1,166 unresolved warning signatures as downstream work. Do not infer compatibility from server readiness.
4. Run the required exact-SHA independent reviews and runtime debugging audit. Store all committed review evidence under `evidence/item-7/review/` and record the reviewed full SHA with every verdict.
5. Push `experiment/item-7-worldgen-audit`, open a pull request against `main`, request `@codex review`, address every valid finding in separate review-fix commits, and repeat until a completed thumbs-up cycle has no unresolved valid findings.
6. Merge without rewriting the atomic history, fetch, and verify that `origin/main` contains the accepted Item 7 commits. Only then create the Item 8 branch from the verified merged ref.
7. Item 8 must combine verified runtime registries, packaged data, configuration evidence, logs, and generated-world observations. It must resolve canonical families without double-counting aliases, pieces, pools, or templates, and it must carry Item 7 run identity and unknowns forward.

Recovery Gate R-1 remains open for Items 8 through 10 and their final cross-item audit after Item 7 delivery completes.

## 1. Authority, scope, and restart rule

This was the continuation handoff as of **2026-09-03 UTC**. Read it as a dated snapshot. `SPECS.md` remains the chronological and dependency-ordered requirements authority.

Do not redo completed Items 2–5 unless verification or later evidence invalidates a gate. Do not begin Item 11. Continue in order: Item 6, Item 7, Item 8, Item 9, Item 10, the final Items 2–10 cross-item audit, and only then report Item 11 eligibility without implementing Item 11.

The exact restart point is:

> **Merge PR #11, then begin Item 6.** The `docs/item5-current-handoff` branch is based directly on `origin/main` and already contains the exact Temurin build-marker boundary fix plus its regression. Delivery reconciliation is complete on this branch; do not cherry-pick the fix again. Once PR #11 is merged, begin the generated-configuration audit by freezing untouched generated defaults before any tuning.

## 2. Current Git and delivery state

- Repository: `/workspace/mcpack`.
- Current delivery branch at this handoff: `docs/item5-current-handoff`, based directly on `origin/main` at `4f61549`. It carries the exact `541d8ad` change as cherry-picked commit `9b0771f` and this updated handoff. Merge this branch through the repository's normal pull-request workflow before relying on the Item 5 gate. The aggregate `work` branch is not the delivery authority for starting Item 6.
- `origin/main`: `4f61549` (`Merge pull request #9 from copeugne/fix/item5-java-runtime`).
- PR #6 (Item 4): merged as `1af46a5` on 2026-09-02.
- PR #8 (Item 5 protocol/pilot): merged as `4ebf2a9` on 2026-09-03.
- PR #9 (pinned Java 21 correction): merged as `4f61549` on 2026-09-03. Its feature commits are:
  - `9957be6 fix(item5): prove pinned Java 21 pilot runtime`;
  - `f2ea027 docs(item5): complete Java pilot reproduction commands`;
  - `b2a79a4 fix(item5): bind exact Temurin build identity`.
- PR #10: merged as `d900297` **into `fix/item5-java-runtime`**, with source commit `541d8ad fix(item5): delimit pinned Java build marker`. Because its base branch had already been merged, PR #10 did not update `main`.
- PR #11: open from `docs/item5-current-handoff` into `main`. Commit `9b0771f` is the main-based cherry-pick of the exact `541d8ad` two-file change; commit `7db0ec5` updates this handoff. The branch therefore already rejects false `+1` prefix matches such as `+10`. Reconciliation is complete on the PR branch and becomes complete on `main` when PR #11 merges.
- The last PR #9 review thread was technically addressed by `541d8ad`, but GitHub still displayed that old PR #9 thread as unresolved when queried. Treat code delivery, not thread cosmetics on a merged PR, as the gate.
- Existing validated tag `item-4-controlled-environment-2026-09-02` points to `845f954`. Never move or rewrite it.
- No Item 5 milestone tag was created in this work.

Recommended synchronization before new work:

1. `git fetch origin --prune`.
2. Start a continuation branch from `origin/main`, not from local aggregate commit `cff7606`.
3. If PR #11 is still open, continue on or review `docs/item5-current-handoff`; do **not** cherry-pick `541d8ad` again because its exact change is already commit `9b0771f` on this branch.
4. If PR #11 has merged, start a new Item 6 branch from the updated `origin/main` and verify that `tools/run_item5_spark_pilot.py` contains the delimited `+1` matcher and its `+10` regression.
5. Do not infer delivery from PR #10 alone: its base was not `main`.

## 3. Exit-gate status

| Item | Status | Authoritative evidence / note |
|---|---|---|
| 1 | Existing design contract; outside this continuation's implementation scope | Re-audit where relevant during the final cross-item review. |
| 2 | **Complete** | `docs/items/Item-2-Frozen-Technical-Baseline.md`, `evidence/item-2/`, platform tooling, and reconstruction tests. |
| 3 | **Complete** | `docs/items/Item-3-Exact-Version-and-Dependency-Audit.md`, `evidence/item-3/final-compatibility-matrix.json`, exact retained-provider evaluation, and runtime evidence. |
| 4 | **Complete** | PR #6 is merged. Closure and evidence are under `docs/items/Item-4-Controlled-Test-Environment-Closure.md` and `evidence/item-4/`. |
| 5 | **Complete on the PR #11 branch; merge pending** | PRs #8 and #9 supplied the implementation and genuine pinned-Temurin pilot. PR #11 already carries the exact boundary fix on a `main`-based branch. Do not reapply it; merge PR #11 before branching for Item 6. |
| 6 | **Exact next substantive item after PR #11 merges** | Generated configuration audit; freeze actual generated defaults before tuning. |
| 7 | **Pending; blocked by Item 6** | Item 4/5 boot logs are not Item 7 world inspection. |
| 8 | **Pending; blocked by Item 7** | Existing reconstructed inventory is not sufficient runtime proof. |
| 9 | **Pending; blocked by Item 8** | Regenerate classifications from verified Item 8 families. |
| 10 | **Pending; blocked by Item 9** | Existing reconstructed density material is not accepted empirical closure. |
| 11 | **NOT AUTHORIZED** | Do not implement, run, repair, or lint Item 11-specific workflows. |

## 4. Frozen downstream identities

### Item 3 gameplay stack

- Minecraft `1.21.1`.
- NeoForge `21.1.249`.
- Eclipse Adoptium Temurin `21.0.12.1+1-LTS`.
- JVM baseline: `-Xms1G -Xmx4G`.
- Retained gameplay manifest: `evidence/item-3/runtime/retained-server-candidates.txt`.
- Retained count: exactly 136.
- Retained manifest SHA-256: `78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb`.
- Pinned Temurin archive SHA-256: `ce79869e1307ed8ee1e2baa86a412b1eb5b75d10a01006d788a6f968bcfaee94`.

Do not silently re-enable Sable, bundled Aeronautics, Every Compat, the statically rejected spell-engine family, or Simply More/Simply Tooltips. If later runtime evidence contradicts Item 3, reopen Item 3 and repeat every affected downstream gate.

### Item 4 controlled-environment result

#### Versioned controls and seeds

Configuration version is `test-environment-v0.1`. Seed controls are committed in `test-environment/seed-suite.json`:

| Role | Seed |
|---|---:|
| ordinary | `42` |
| mountainous | `6671238423019257953` |
| ocean-heavy | `95920844204830198` |
| biome-diverse | `-3503646078644842058` |

All four controls were independently rematerialized after the copied-world removal fix. Each reached readiness, completed `save-all flush`, received the matching save confirmation, and stopped cleanly. `evidence/item-4/runtime-validation.json` records the seed read from `Data.WorldGenSettings.seed` in each generated `world/level.dat`, together with file size and SHA-256. Compressed runtime logs are under `evidence/item-4/logs/`. Do not replace this evidence with a copied world or infer one seed's behavior from another.

#### Materialization and lifecycle behavior

`tools/manage_item4_environment.py`:

- refuses destructive target reuse;
- verifies retained artifacts before materialization;
- accepts an existing empty pristine `mods/` directory but rejects a non-empty one;
- removes a copied pristine `world/` before applying the selected seed so first boot genuinely generates that role;
- writes deterministic seed properties;
- creates normalized deterministic stopped-world archives;
- verifies archive identity before extraction and rejects unsafe tar members;
- holds a Minecraft-compatible POSIX record lock through archive creation and receipt hashing; and
- deliberately excludes `session.lock`, because closing another descriptor can release process-scoped POSIX locks.

`tools/run_item4_server_lifecycle.py` waits for readiness, requests `save-all flush`, waits for `Saved the game`, requests stop, enforces a deadline even if stdout becomes silent, and kills the complete process group on timeout. Preserve these state boundaries; an unrelated save line is not proof of a requested flush.

#### Backup and restore proof

The ordinary control was backed up only after flush and stop:

- 57 world files;
- `session.lock` excluded;
- archive size 1,172,490 bytes;
- archive SHA-256 `320a63f709a2df2fc9d2abccbb547e9eace05d5b44074fcb501ba294f7f4b0bd`;
- per-file receipt `evidence/item-4/ordinary-backup-receipt.json`.

The archive was verified before safe extraction into an absent target. The restored world reached readiness in 267.369 seconds, flushed, and stopped cleanly. Its receipt is `evidence/item-4/ordinary-restore-receipt.json`; its log is `evidence/item-4/logs/ordinary-restored-boot.log.gz`.

#### Scheduled backup boundary

`infrastructure/bin/item4-automated-backup` and `infrastructure/systemd/mcpack-item4-backup@.{service,timer}` define a persistent daily 03:15 UTC schedule, randomized delay, one instance per seed role, and refusal to archive a live world. The service runs under the dedicated `mcpack` account with explicit writable paths and hardening. Installation commands are in `test-environment/README.md`. The cloud container may not run systemd; never claim the timer is active without actual `systemctl` evidence.

#### Preserved failure and locking constraint

The first mountainous attempt used a fixed five-minute command delay. It reached readiness, but the unchanged watchdog terminated a later tick before the command arrived. The log and crash report are intentionally preserved under `evidence/item-4/failures/`. The instance was deleted, rematerialized, and successfully rerun with readiness-driven orchestration without tuning baseline controls. Do not erase or reinterpret this failure.

Keep the Java-compatible POSIX record-lock implementation. BSD `flock` does not contend with Java `FileChannel` locks and must not be substituted.

## 5. Item 5 completed result

### 5.1 Executable method

- Protocol: `measurement/item5/protocol-v1.json`.
- Strict evidence/analyzer models: `src/mcpack_evidence/item5.py`.
- Deterministic processor: `tools/analyze_item5_samples.py`.
- Cross-artifact validator: `tools/validate_item5.py`.
- Spark lifecycle harness: `tools/run_item5_spark_pilot.py`.
- Workload fixtures:
  - `measurement/item5/combat-fixture-v1.json`;
  - `measurement/item5/worldgen-fixture-v1.json`;
  - `measurement/item5/pathfinding-fixture-v1.json`.
- Spark overlay: `measurement/item5/spark-overlay.json`; Spark is instrumentation layered over the unchanged 136-file gameplay manifest, producing a 137-JAR profiling runtime.

The protocol has 24 exact metric contracts, four seed cases, five material player-load cases, and a distinct zero-player idle case. Models reject missing fields, incomplete cases/hashes, unknown metrics, invalid units, impossible negative physical values, inconsistent ratio operands, invalid proportions, and ambiguous multi-axis samples. Analyzer output separates metric, seed, player case, repetition, component, and unit.

#### Metric and case coverage

The exact 24 metric IDs cover:

- performance: idle MSPT, active-combat MSPT, fresh-worldgen MSPT, TPS, memory, garbage collection, entity count, pathfinding cost, and chunk-generation cost/time;
- adventure and density: structure count, structures per 1,000 chunks, actionable locations per 1,000 chunks, combat encounters per 1,000 chunks, proper dungeons per 1,000 chunks, major expeditions per 1,000 chunks, inter-structure distance, travel time, dungeon duration, death rate, and loot value;
- repetition and pacing: unique structure families per hour, time to first repeated structure family, and repeated dungeon-layout frequency; and
- Adventure Activity Ratio: meaningful interaction time divided by total expedition time.

Every contract states purpose, quantity, unit, command/procedure, warm-up, sampling window, duration, repetitions, seed cases, player cases, raw and processed formats/paths, aggregation, acceptance, rejection, uncertainty, and relevant environment hashes. The required deterministic seeds are ordinary, mountainous, ocean-heavy, and biome-diverse. Material player cases are solo, 2 players, 4 players, expected-normal concurrency, and expected-peak concurrency; idle zero-player measurement remains distinct rather than being silently treated as solo.

Rate metrics retain auditable numerators and positive denominators instead of preserving only derived floats. Proportions are bounded where semantically appropriate; `death_rate` is deliberately not treated as a probability because multiple deaths per exposure may be valid. Multi-axis observations retain explicit components: for example heap memory versus other memory views, wall-clock versus CPU pathfinding cost, and distinct loot-value components. Units are mandatory and metric-specific. Samples are grouped by metric, seed, player case, repetition, component, and unit so unlike experimental conditions cannot be pooled.

#### Trust boundaries and deterministic processing

The Pydantic models reject unknown fields as well as missing required fields. Validation enforces exact per-metric seed, player, and environment coverage and rejects duplicate cases. Sample ingestion rejects empty or header-only CSVs, unknown metric IDs, invalid cases, non-positive repetitions, non-finite values (`NaN` and infinities), incompatible units, missing required components, spurious components on single-axis metrics, and physically impossible negative values.

Receipt-controlled artifact paths are confined to the repository after symlink resolution; absolute paths, traversal, and escaped symlinks are rejected. The validator independently recomputes:

- retained-manifest and host-discovery hashes from committed files;
- protocol, fixture, overlay, runtime, lifecycle, log, profile, sample, and summary hashes;
- deterministic processed output from raw samples; and
- accepted runtime TPS, MSPT, and heap-memory observations from the hash-bound Spark log.

Editing and rehashing only a receipt, CSV, or summary is therefore insufficient to manufacture accepted evidence. Unknown methodology fields and cross-artifact identity mismatches fail closed.

### 5.2 Accepted and rejected pilots

Committed evidence lives under `evidence/item-5/pilots/` and includes accepted/rejected receipts, compressed logs, lifecycle JSON, local Spark profiles, raw CSV, and deterministic processed JSON. The validator re-hashes every artifact, confines paths to the repository, recomputes processed output, verifies runtime and fixture identities, proves explicit rejected-run failure, and requires both accepted and rejected paths.

The first full-stack attempt was rejected because shutdown began before Spark finished metadata collection. After correcting that lifecycle boundary, the original accepted-looking pilot was later invalidated because a relative Java `PATH` entry stopped resolving after the server process changed working directory and `run.sh` fell through to Oracle Java `25.0.2`. That evidence was superseded, never relabeled. PR #9 fixed the harness to resolve an absolute Java executable and reran a clean seed-42 retained-stack pilot. The replacement accepted pilot proves:

- Eclipse Adoptium Java `21.0.12.1` at runtime;
- pinned archive/build `Temurin-21.0.12.1+1-LTS`;
- exact 137-JAR identity;
- input-world and stopped output-world hashes;
- successful TPS, memory, and GC probes;
- asynchronous profiler start and completion;
- one preserved 236,557-byte `.sparkprofile`;
- `save-all flush`, clean stop, and return code 0.

`b2a79a4` additionally binds receipts to the Temurin archive digest in `infrastructure/manifests/platform-1.21.1.json`. `541d8ad` closes the remaining parser edge case by preventing `+10` from matching the pinned `+1` prefix.

The lifecycle harness performs bounded readiness and command-state orchestration. It distinguishes profiler-stop request from Spark profile-save confirmation and distinguishes flush request from flush confirmation. It requires the exact seven-command sequence, confirmed TPS/memory/GC probes, exactly one new non-empty local profile, a successful explicit flush, clean stop, zero return code, and no console-pipe failure. Closed stdin is recorded as a failure rather than losing the receipt. Post-launch I/O failures kill and reap the Minecraft process group so no orphaned JVM can continue mutating the world.

Rejected receipts must reference a structurally valid preserved lifecycle and prove a machine-observable failure through explicit lifecycle state, a nonzero integer return code, console-pipe failure, or an accepted marker in a preserved log. Merely labeling a successful lifecycle as rejected does not pass. Separate fixtures/receipts preserve launch failure and cleaned-up post-launch I/O failure behavior.

### 5.3 Known limitations, not false claims

- The operational pilot proves collection, preservation, processing, rejection handling, and environment binding. It is not a formal performance baseline.
- Spark overhead remains `UNKNOWN` until the protocol's paired profiled/unprofiled repetitions are executed.
- The accepted pilot used a dirty worktree and short startup sample; this is explicitly documented and is not a tuning result.
- Two subsequent attempts made while preparing the exact-build review fix hit the unchanged Minecraft watchdog shortly after readiness. They existed only in ignored runtime paths and are absent in this reconstructed environment; do not present them as committed evidence.

## 6. Runtime state in this container

At this handoff, direct checks showed these intentionally ignored paths are **absent**:

- `downloads/`;
- `instances/`;
- `evidence/raw/`.

Therefore, do not claim the current container retains downloaded JARs, the Temurin extraction, NeoForge installations, generated configs, worlds, or raw uncommitted failure logs. Durable reconstruction sources remain committed evidence plus the Item 2 release assets. A new runtime must reacquire and verify all binaries.

The successful PR #9 reconstruction used:

1. `infrastructure/bin/platform-1.21.1 acquire` and `provision-java`;
2. all 190 Item 3 candidates acquired through `tools/acquire_candidate_artifacts.py`;
3. the durable Item 2 state overlay from the `item-2-evidence-assets-2026-09-01` release;
4. a clean ordinary materialization from the 136-file retained manifest;
5. the audited Spark overlay;
6. the Item 5 harness with pinned Temurin.

The Java-based NeoForge installer needed the environment HTTP proxy and a temporary Java trust store containing the environment's MITM proxy CA. These were operational-only inputs and were not committed.

## 7. Exact next actions

1. Read this file and `SPECS.md` completely.
2. Check `git status`, remotes, and recent graph; fetch all remotes.
3. Query PR #11. If it is open, review/merge it; its branch already contains the exact boundary fix and regression. Do not cherry-pick the fix again.
4. After PR #11 merges, create the Item 6 branch from the updated `origin/main` and verify the delimited `+1` matcher plus `+10` rejection test are present.
5. Before relying on the Item 5 gate in a different or superseding branch, run at least:
   - `uv run pytest -q tests/item5`;
   - `uv run pytest -q`;
   - scoped Ruff check and format check;
   - `uv run basedpyright src tests`;
   - the Item 5 validator against both receipts;
   - applicable infrastructure shell checks;
   - `git diff --check`.
6. Begin Item 6 immediately after the merge and checks; delivery reconciliation requires no further code change.
7. Reacquire/rematerialize a clean retained-stack instance, preserve the untouched generated configuration tree or a lossless deterministic archive, and freeze a per-file hash manifest **before any tuning**.

## 8. Item 6 — generated configuration audit

### 8.1 Entry conditions and immutable baseline

Item 6 depends on Items 2–5. Begin only from a branch containing PR #9 and the delimited Temurin `+1` matcher delivered by PR #11. Reacquire all ignored dependencies, verify their committed hashes, and rematerialize a clean retained-stack instance. Do not reuse a proof world or mutated configuration tree.

Boot the exact retained stack only far enough to generate configuration. Before editing anything:

1. preserve the untouched generated configuration tree, or a deterministic lossless archive of it;
2. generate a sorted per-file manifest containing relative path, size, and SHA-256;
3. record platform, retained-manifest, Java archive/build, seed, configuration-version, command, and timestamp identities;
4. distinguish files generated at installation, first startup, world creation, and shutdown; and
5. validate the archive/tree against the manifest.

No tuning is authorized during baseline capture. If a boot mutates a file, preserve the pre- and post-boot states and explain which one is effective rather than silently overwriting the baseline.

### 8.2 Required audit coverage

Inspect actual generated configuration, not upstream documentation alone. Cover these systems when present and explicitly record absence when expected but not generated:

- Sparse Structures and every global spacing/separation multiplier or per-structure override;
- Structure Essentials and Structure Layout Optimizer;
- ServerCore, C2ME, and Chunky;
- When Dungeons Arise and WDA Seven Seas;
- YUNG structure systems;
- IDAS and Integrated structures;
- Moog structure families;
- village generation, including CTOV, Towns & Towers, Better Village, and Village Taverns where applicable;
- Loot Integrations and related loot behavior;
- mob spawning and entity limits; and
- difficulty-related settings.

For every relevant setting record file, key/path, generated default, effective value, whether it is non-default, source/owner, scope, interaction partners, and evidence. Identify global structure-spacing multipliers, per-structure overrides, disabled structure sets, hidden low-density causes, spawn/difficulty changes, performance/worldgen interactions, precedence, duplicated controls, and mod-to-mod conflicts. Separate an absent key, a generated default, and a loader/mod implicit default.

### 8.3 Item 6 exit evidence

Produce machine-readable and human-readable outputs that agree exactly. The validator must prove that every reported file exists in the frozen manifest, every cited value matches preserved content, every non-default is accounted for, and no unexplained file is omitted. Preserve limitations and unresolved ownership rather than guessing. Item 7 remains blocked until report-to-manifest consistency passes.

## 9. Item 7 — terrain and world-generation interaction audit

Regenerate clean worlds for all four deterministic seeds under the frozen Item 6 configuration. Inspect actual generated terrain rather than treating Item 4/5 boot logs or synthetic registry enumeration as world evidence. Cover, where retained: Tectonic, Terralith, Biomes O' Plenty, Regions Unexplored, TerraBlender, Lithostitched, BetterEnd, YUNG, WDA, IDAS, Integrated structures, Moog systems, Explorify, Explorations, Repurposed Structures, CTOV, and Towns & Towers.

Inspect for fragmented/tiny biomes, unnatural transitions, buried or floating structures, cliff intersections, bad underwater placement, structure/village overlaps, failed placements, impossible biome restrictions, and excessive terrain modification. Classify each finding separately as cosmetic, gameplay-affecting, performance-affecting, or outright generation failure.

Every observation must preserve seed, dimension, coordinates, command/procedure, relevant log or screenshot, input configuration identity, world manifest/hash, observation, anomaly classification, confidence, and limitation. Screenshots supplement but do not replace machine-readable evidence. If Item 7 contradicts the frozen configuration or retained set, reopen the affected upstream gate.

## 10. Item 8 — structure-family inventory

Inventory every gameplay-relevant structure family only after Item 7. Sources must include runtime registries, datapacks/packaged data, config evidence, logs, and generated-world observations. Enumerate WDA, WDA Seven Seas, YUNG, IDAS, Integrated Stronghold/Villages, Moog families, Explorify, Explorations, Repurposed Structures, AdoraBuild, CTOV, Towns & Towers, Better Village, and Village Taverns when present.

For each canonical family record:

- owning provider and canonical identifier;
- aliases, variants, pools, pieces, and template relationships without double-counting them as families;
- dimension and biome constraints;
- approximate footprint and vertical size;
- surface/underground classification and visual discoverability;
- intended hostility and encounter role;
- authored versus natural enemy source;
- loot-table source and generated spawners;
- runtime/generated-world evidence; and
- confidence, ambiguity, and unresolved questions.

Machine-readable inventory and narrative report must agree on family count and identity. Existing reconstructed inventories are leads, not proof.

## 11. Item 9 — structure-stack classification

Regenerate classification from the verified Item 8 inventory. Assign every canonical family exactly one provisional category: Tier 0 ambient landmark, Civilization, Tier 1 small encounter, Tier 2 proper dungeon, Tier 3 major expedition, or Tier 4 world objective. Apply the definitions in `SPECS.md`; do not infer tier solely from footprint or appearance.

Record rationale, evidence, confidence, ambiguity, and any competing classification. Flag dungeon-looking structures without meaningful gameplay, decorative structures, oversized structures with little internal gameplay, overlapping themes, redundant village/ruin/tower/dungeon archetypes, and unclear aliases. Machine- and human-readable results must have exact family coverage and classification parity.

## 12. Item 10 — representative-region density measurement

Generate representative regions across all selected seeds using the frozen Item 6 configuration and verified Item 8/9 identities. Preserve region selection rules and exposure denominators so sampling cannot be chosen post hoc. Measure:

- structures, actionable locations, combat encounters, proper dungeons, and major expeditions per 1,000 chunks;
- village density;
- average nearest-neighbor/inter-structure distance by category;
- clustering and large empty regions;
- biome, seed, and dimension variation; and
- Sparse Structures' actual contribution to the observed distribution.

Distinguish raw structure density from useful encounters and do not count aliases, pieces, or pools as independent families. Preserve raw observations immutably, process them deterministically through Item 5 contracts, and bind results to world/configuration/manifests. Record uncertainty, failures, censored samples, and limitations. Do not proceed on reconstructed density prose or inventories alone.

## 13. Final Items 2–10 cross-item audit

After Item 10, audit all gates together. Confirm that every downstream artifact references the same Minecraft, NeoForge, Temurin, retained-manifest, configuration, seed, world, and protocol identities; machine-readable and narrative counts agree; failures and uncertainty remain visible; and no later evidence invalidates an earlier gate. Reopen and repeat affected downstream work whenever an identity or conclusion changes.

Only after Items 2–10 pass this audit may the next session report whether Item 11 is eligible. It must not implement, execute, repair, or lint Item 11-specific workflows under this handoff.

## 14. Validation baseline

Last verified at PR #9 head `b2a79a4`:

- `uv run pytest -q` — **126 passed**;
- `uv run pytest -q tests/item5` — **67 passed**;
- scoped Ruff check/format — passed;
- `uv run basedpyright src tests` — 0 errors, 0 warnings;
- Item 5 validator — 24 metrics, 6 cases, 2 pilots;
- `tests/infrastructure/test_item4_backup_schedule.sh` — passed;
- `git diff --check` — passed.

PR #11 branch, after carrying the exact PR #10 change onto `main` history:

- `uv run pytest -q tests/item5/test_spark_pilot.py` — **16 passed**;
- `uv run pytest -q tests/item5` — **68 passed**;
- `uv run pytest -q` — **127 passed**;
- scoped Ruff check and format check — passed;
- `uv run basedpyright src tests` — 0 errors, 0 warnings, 0 notes;
- Item 5 validator — 24 metrics, 6 cases, 2 pilots;
- Item 4 backup schedule shell test — passed;
- `git diff --check` — passed.

These results establish the branch baseline. They do not prove that PR #11 has merged; check GitHub and fetch `origin/main` before starting Item 6.

## 15. Git and evidence discipline

- Inspect status, unstaged diff, staged diff, and recent log before every commit.
- Preserve atomic commits; do not squash or rewrite valid history.
- Keep review fixes distinct from substantive item milestones.
- Keep PR descriptions current with exact checks, evidence, limitations, and unresolved uncertainty.
- Never commit candidate JARs, Minecraft/NeoForge binaries, worlds, secrets, operational caches, proxy trust stores, or downloaded toolchains.
- Compressed UTF-8 logs and Spark profiles are evidence, not executable dependencies; record hashes and purpose.
- Do not alter raw evidence to make it pass. Supersede invalid evidence with a genuine rerun and preserve the failure history.
- Never move existing tags.

## 16. Prohibited shortcuts and stop condition

Do not begin Item 11. Do not tune before Item 6 freezes generated defaults. Do not treat Item 4/5 boot logs as Item 7 inspection. Do not treat Fabric metadata as active NeoForge metadata or assume Forge equivalence. Do not discard failures or uncertainty. Do not present reconstructed prose as empirical proof. Do not claim systemd timers are active without actual `systemctl` evidence.

Continue through Items 6–10 and the final Items 2–10 audit. Stop only when Items 2–10 pass that audit and Item 11 eligibility can be reported without implementing it, or when a genuine external blocker prevents meaningful progress after reasonable investigation and preservation of failure evidence.
