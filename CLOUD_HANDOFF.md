# Cloud Handoff — Items 5–10 Continuation

## 1. Authority, scope, and restart rule

This is the authoritative continuation handoff as of **2026-09-03 UTC**. Read it and then `SPECS.md` in full before changing the repository. `SPECS.md` remains the chronological and dependency-ordered requirements authority; this file records actual Git, review, evidence, and runtime state.

Do not redo completed Items 2–5 unless verification or later evidence invalidates a gate. Do not begin Item 11. Continue in order: Item 6, Item 7, Item 8, Item 9, Item 10, the final Items 2–10 cross-item audit, and only then report Item 11 eligibility without implementing Item 11.

The exact restart point is:

> **Delivery reconciliation, then Item 6.** Ensure commit `541d8ad` (the exact Temurin build-marker boundary fix) is present on the branch based on `origin/main`. PR #10 merged into the already-merged `fix/item5-java-runtime` branch, not into `main`; do not assume its merge alone delivered the fix to `main`. After that two-file fix is carried forward and validated, begin the generated-configuration audit without tuning defaults.

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
- PR #10: merged as `d900297` **into `fix/item5-java-runtime`**, with source commit `541d8ad fix(item5): delimit pinned Java build marker`. It rejects a false `+1` prefix match in versions such as `+10`. At handoff, `origin/main` does not contain this two-file change (`tools/run_item5_spark_pilot.py` and `tests/item5/test_spark_pilot.py`). Carry it forward without rewriting history.
- The last PR #9 review thread was technically addressed by `541d8ad`, but GitHub still displayed that old PR #9 thread as unresolved when queried. Treat code delivery, not thread cosmetics on a merged PR, as the gate.
- Existing validated tag `item-4-controlled-environment-2026-09-02` points to `845f954`. Never move or rewrite it.
- No Item 5 milestone tag was created in this work.

Recommended synchronization before new work:

1. `git fetch origin --prune`.
2. Start a continuation branch from `origin/main`, not from local aggregate commit `cff7606`.
3. Use the prepared `docs/item5-current-handoff` branch, or independently carry forward the exact `541d8ad` two-file diff if that branch is superseded. Run the focused and full checks and deliver the change to `main` through the repository's normal workflow.
4. Confirm that the final branch contains both PR #9 and the exact `541d8ad` change before relying on the Item 5 gate.

## 3. Exit-gate status

| Item | Status | Authoritative evidence / note |
|---|---|---|
| 1 | Existing design contract; outside this continuation's implementation scope | Re-audit where relevant during the final cross-item review. |
| 2 | **Complete** | `docs/items/Item-2-Frozen-Technical-Baseline.md`, `evidence/item-2/`, platform tooling, and reconstruction tests. |
| 3 | **Complete** | `docs/items/Item-3-Exact-Version-and-Dependency-Audit.md`, `evidence/item-3/final-compatibility-matrix.json`, exact retained-provider evaluation, and runtime evidence. |
| 4 | **Complete** | PR #6 is merged. Closure and evidence are under `docs/items/Item-4-Controlled-Test-Environment-Closure.md` and `evidence/item-4/`. |
| 5 | **Complete in evidence and implementation, with one delivery reconciliation required** | PRs #8 and #9 are merged. The accepted pilot was genuinely rerun on pinned Temurin `21.0.12.1+1-LTS`; the earlier Java-25 pilot was superseded, not relabeled. Carry `541d8ad` onto the `main`-based continuation before Item 6. |
| 6 | **Exact next substantive item after reconciliation** | Generated configuration audit; freeze actual generated defaults before tuning. |
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

### Item 4 controls

Configuration version is `test-environment-v0.1`. Deterministic seeds remain:

| Role | Seed |
|---|---:|
| ordinary | `42` |
| mountainous | `6671238423019257953` |
| ocean-heavy | `95920844204830198` |
| biome-diverse | `-3503646078644842058` |

All four were independently materialized, booted to readiness, flushed, and stopped. The ordinary backup/restore proof contains 57 world files, excludes `session.lock`, and uses archive SHA-256 `320a63f709a2df2fc9d2abccbb547e9eace05d5b44074fcb501ba294f7f4b0bd`. Preserve the documented failed mountainous watchdog attempt. Keep the Java-compatible POSIX record-lock implementation; do not replace it with BSD `flock`.

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

### 5.2 Accepted and rejected pilots

Committed evidence lives under `evidence/item-5/pilots/` and includes accepted/rejected receipts, compressed logs, lifecycle JSON, local Spark profiles, raw CSV, and deterministic processed JSON. The validator re-hashes every artifact, confines paths to the repository, recomputes processed output, verifies runtime and fixture identities, proves explicit rejected-run failure, and requires both accepted and rejected paths.

The original accepted-looking pilot was invalidated because the relative Java path fell through to Oracle Java `25.0.2`. PR #9 fixed the harness to resolve an absolute Java executable and reran a clean seed-42 retained-stack pilot. The replacement accepted pilot proves:

- Eclipse Adoptium Java `21.0.12.1` at runtime;
- pinned archive/build `Temurin-21.0.12.1+1-LTS`;
- exact 137-JAR identity;
- input-world and stopped output-world hashes;
- successful TPS, memory, and GC probes;
- asynchronous profiler start and completion;
- one preserved 236,557-byte `.sparkprofile`;
- `save-all flush`, clean stop, and return code 0.

`b2a79a4` additionally binds receipts to the Temurin archive digest in `infrastructure/manifests/platform-1.21.1.json`. `541d8ad` closes the remaining parser edge case by preventing `+10` from matching the pinned `+1` prefix.

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
3. Create/use a branch based on `origin/main` (`4f61549` or later).
4. Ensure `541d8ad` is present. Do not assume PR #10 delivered it to `main`, because its base was `fix/item5-java-runtime`.
5. Run at least:
   - `uv run pytest -q tests/item5`;
   - `uv run pytest -q`;
   - scoped Ruff check and format check;
   - `uv run basedpyright src tests`;
   - the Item 5 validator against both receipts;
   - applicable infrastructure shell checks;
   - `git diff --check`.
6. Once the boundary fix is on the main-based continuation and checks pass, begin Item 6 immediately.
7. For Item 6, reacquire/rematerialize a clean retained-stack instance, preserve the untouched generated configuration tree or a lossless deterministic archive, and freeze a per-file hash manifest **before any tuning**.

## 8. Item 6 requirements

Use actual configs generated by clean retained-stack boots. Record generated defaults, effective defaults, and every non-default value. Audit spacing, disabled sets, spawn/difficulty changes, performance/worldgen/structure interactions, and mod-to-mod interactions. Explicitly record expected systems that are absent.

Cover, when present: Sparse Structures, Structure Essentials, ServerCore, C2ME, Chunky, Structure Layout Optimizer, When Dungeons Arise, YUNG systems, IDAS, Moog systems, village generation, Loot Integrations, spawning, and difficulty. Preserve the original generated tree or deterministic lossless archive plus per-file manifest. Do not tune during this baseline audit. Validate report-to-manifest consistency before Item 7.

## 9. Items 7–10 sequence

- **Item 7:** regenerate clean worlds for all four seeds under the frozen Item 6 config; inspect real terrain, biomes, structures, dimensions, boundaries, cross-mod generation, pathologies, and expected content with seed/dimension/coordinate/command/world-hash traceability. Synthetic enumeration is not a substitute.
- **Item 8:** enumerate every gameplay-relevant structure family from registries, datapacks, packaged data, runtime evidence, and generated-world evidence. Do not double-count aliases, pools, pieces, or variants.
- **Item 9:** classify every verified family into Tier 0–4 or Civilization using `SPECS.md`, preserving confidence and ambiguity. Machine- and human-readable outputs must agree exactly.
- **Item 10:** generate representative regions for required seeds and distinguish raw structure density from useful encounters. Measure density, value, travel/inter-structure distances, clustering, empty regions, biome/seed/dimension variation, and Sparse Structures' actual effect. Preserve raw observations and deterministic processing.

Do not skip dependency order. Reopen upstream items if later evidence contradicts them.

## 10. Validation baseline

Last verified at PR #9 head `b2a79a4`:

- `uv run pytest -q` — **126 passed**;
- `uv run pytest -q tests/item5` — **67 passed**;
- scoped Ruff check/format — passed;
- `uv run basedpyright src tests` — 0 errors, 0 warnings;
- Item 5 validator — 24 metrics, 6 cases, 2 pilots;
- `tests/infrastructure/test_item4_backup_schedule.sh` — passed;
- `git diff --check` — passed.

PR #10 / commit `541d8ad` separately reported:

- `uv run pytest -q tests/item5/test_spark_pilot.py` — 16 passed;
- `uv run pytest -q tests/item5` — 68 passed;
- scoped Ruff — passed;
- `git diff --check` — passed.

The full suite was not recorded in PR #10's description. Rerun it after carrying `541d8ad` onto the main-based continuation; do not infer a full-suite result.

## 11. Git and evidence discipline

- Inspect status, unstaged diff, staged diff, and recent log before every commit.
- Preserve atomic commits; do not squash or rewrite valid history.
- Keep review fixes distinct from substantive item milestones.
- Keep PR descriptions current with exact checks, evidence, limitations, and unresolved uncertainty.
- Never commit candidate JARs, Minecraft/NeoForge binaries, worlds, secrets, operational caches, proxy trust stores, or downloaded toolchains.
- Compressed UTF-8 logs and Spark profiles are evidence, not executable dependencies; record hashes and purpose.
- Do not alter raw evidence to make it pass. Supersede invalid evidence with a genuine rerun and preserve the failure history.
- Never move existing tags.

## 12. Prohibited shortcuts and stop condition

Do not begin Item 11. Do not tune before Item 6 freezes generated defaults. Do not treat Item 4/5 boot logs as Item 7 inspection. Do not treat Fabric metadata as active NeoForge metadata or assume Forge equivalence. Do not discard failures or uncertainty. Do not present reconstructed prose as empirical proof. Do not claim systemd timers are active without actual `systemctl` evidence.

Continue through Items 6–10 and the final Items 2–10 audit. Stop only when Items 2–10 pass that audit and Item 11 eligibility can be reported without implementing it, or when a genuine external blocker prevents meaningful progress after reasonable investigation and preservation of failure evidence.
