# Adventure & Engineering Minecraft Pack — New-Session Handoff

> Historical checkpoint: this file records the repository state on 2026-09-01 and is not the current continuation authority. Use `SPECS.md`, the master execution status in `Adventure-Engineering-Pack-Execution-Ledger.md`, and current Git/GitHub state for present status. The dated instructions below are preserved as recovery history.

## Current continuation checkpoint - 2026-09-04

This section supersedes the dated status and restart instructions below. Preserve the rest of this file as recovery history. `SPECS.md` remains the dependency-ordered requirements authority, and `Adventure-Engineering-Pack-Execution-Ledger.md` remains the status and evidence vocabulary authority.

### Git and delivery state

- A fresh fetch on 2026-09-04 found `origin/main` at `eb84d842a7b108863dcdd4c86435a875f8a0c575` with no newer remote commits. The active branch is `experiment/item-7-worldgen-audit`, based on that ref. Its corrected implementation and r2 machine evidence reach `4e6b44094a6a11370c1d86b8c3d39a4a31f8ce45` before this reconciliation increment.
- PR #11 merged Item 5 delivery as `398bf59b3a89669ec402026d52250c2b86e54047`.
- PR #12 merged the initial Item 6 generated-default capture as `895ed1d999cd22ca511035e666ad8ac308ae63c1`.
- PR #14 merged the completed Item 6 audit as `f38ea66ecc28911c33d525dcde26434853673ad3`. Its final Codex review completed against `96a914c8a457d2f23698cdaeba18c6ed899b56d1` and reported no major issues. The GitHub API currently exposes no thumbs-up reaction on that cycle, so do not claim that reaction; preserve this as a review-record discrepancy unless later evidence resolves it.
- `eb84d842a7b108863dcdd4c86435a875f8a0c575` only renamed `CLAUDE.md` to `AGENTS.md` after the Item 6 merge.
- Item 7 corrected raw evidence is durably published at `https://github.com/copeugne/mcpack/releases/tag/item-7-raw-evidence-2026-09-04-r2`. The annotated tag resolves to source revision `b13344e8eaa39528b61643bf24534d709cfff131`, and all four assets passed a fresh remote download and hash verification. The first release is preserved, but its staging-process claim is superseded because it lacked Java-compatible world locks and independent copies. The r2 asset hashes match the first release exactly.
- The first exact-SHA review at `97262a21b0b76c253f57e32b8665e48d0a63f822` returned `REJECTED`. It found clean-test dependency on ignored JARs, archive path-swap races, missing world locks and hardlink isolation, permissive provider fields, two oversized modules, and overbroad quality commands. Commits `9d1ff11` through `4e6b440` fix and re-evidence those issues. A fresh final-SHA review remains mandatory.
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
| 7 | `PASS`, delivery pending | Two fresh four-seed runs inspected 54,816 exact selected chunks. The 192 anomaly rows, all 37 provider-component dispositions, 1,222 warning signatures, 128 reviewed captures, corrected r2 restore-tested archives, and 123-artifact completion receipt pass. The first exact-SHA review was rejected and fixed. Fresh exact-SHA review, GitHub Codex review, merge, and delivered-ref verification remain. |
| 8 | `BLOCKED` by Item 7 delivery | Begin the runtime-backed canonical structure inventory only after the Item 7 pull request is cleanly reviewed, merged into `main`, and verified. |
| 9 | `BLOCKED` by Item 8 | Reclassify every verified family exactly once only after Item 8 passes. |
| 10 | `BLOCKED` by Items 7 through 9 | Regenerate and preserve predeclared density evidence only after the preceding gates pass. |
| 11 | `BLOCKED` | Do not implement, run, repair, or lint Item 11 before the final Items 2 through 10 audit passes. It also requires at least two blind human operators. |

The Item 7 completion command returns `PASS` and records 123 exact artifacts in `evidence/item-7/completion.json`. The focused Item 7 suite passes with 155 tests in both the working tree and a clean `git archive` export. The r2 raw-release verifier redownloaded all four assets and matched every committed size and SHA-256.

### Exact continuation point

1. Treat `evidence/item-7/completion.json` and `docs/items/Item-7-Baseline-Worldgen-Audit.md` as the current acceptance summary. The former zero-mod report is superseded historical context.
2. Preserve the measured semantic nondeterminism. Run A and Run B differ outside the central End; input drift and comparator artifacts were refuted, but the causal provider remains `UNKNOWN`. Do not tune the frozen Item 6 configuration inside Item 7.
3. Preserve the confirmed Better Caves generation failure, the unresolved YUNG's Bridges and YUNG's Extras identifiers, and the 1,166 unresolved warning signatures as downstream work. Do not infer compatibility from server readiness.
4. Run the required exact-SHA independent reviews and runtime debugging audit. Store all committed review evidence under `evidence/item-7/review/` and record the reviewed full SHA with every verdict.
5. Push `experiment/item-7-worldgen-audit`, open a pull request against `main`, request `@codex review`, address every valid finding in separate review-fix commits, and repeat until a completed thumbs-up cycle has no unresolved valid findings.
6. Merge without rewriting the atomic history, fetch, and verify that `origin/main` contains the accepted Item 7 commits. Only then create the Item 8 branch from the verified merged ref.
7. Item 8 must combine verified runtime registries, packaged data, configuration evidence, logs, and generated-world observations. It must resolve canonical families without double-counting aliases, pieces, pools, or templates, and it must carry Item 7 run identity and unknowns forward.

Recovery Gate R-1 remains open for Items 8 through 10 and their final cross-item audit after Item 7 delivery completes.

**Prepared:** 2026-09-01
**Live checkpoint updated:** 2026-09-01
**Canonical repository:** `https://github.com/copeugne/mcpack`
**Verified remote branch:** `main`
**Verified remote HEAD before this handoff commit:** `3d1f33551700c9804503d0e27edddce35ea285c4`
**Verified commit count before this handoff commit:** 41
**Primary status:** Item 2 is complete and published. Item 3 is incomplete and stopped after exact acquisition plus top-level and embedded-JAR inspection. Items 4–10 have not been advanced. Item 11 is not authorized.

---

## 0. Historical Validated Checkpoint - Read Before the Older Handoff

As of 2026-09-01, this section superseded older status statements in this file wherever they conflicted. The remainder of the file preserves the recovery history, design contract, and execution context that remained applicable at that checkpoint.

### 0.1 Exact stop boundary

The user explicitly stopped execution while Item 3 was in progress and requested this handoff. Do not continue from Item 4. Resume at the unfinished Item 3 compatibility evaluation, using the committed acquisition and JAR-inspection evidence described below.

The live plan at the stop boundary is:

1. **Complete:** Complete and publish Item 2 baseline evidence, validation, and recovery milestone.
2. **In progress:** Validate all 190 Item 3 candidate artifacts, dependencies, conflicts, sides, and embedded overlaps.
3. **Pending:** Publish Item 3 compatibility matrix, audit report, decisions, limitations, reproduction, and exit gate.
4. **Pending:** Build and validate Item 4 deterministic isolated test environments, controls, and backup/restore boot.
5. **Pending:** Implement and validate Item 5 profiling and gameplay-measurement methodology.
6. **Pending:** Execute Item 6 generated-configuration audit without tuning.
7. **Pending:** Execute Item 7 deterministic terrain/worldgen interaction inspection with preserved evidence.
8. **Pending:** Execute Item 8 runtime-backed structure-family inventory.
9. **Pending:** Execute Item 9 evidence-backed provisional tier classification.
10. **Pending:** Execute Item 10 checkpointed density generation, integrity validation, analysis, and reporting.
11. **Pending:** Run final cross-item QA, push atomic commits/tags, and determine whether Item 11 is authorized.

### 0.2 Git and working-tree state

Before this handoff edit, local `main`, `origin/main`, and `origin/HEAD` all resolved to `3d1f33551700c9804503d0e27edddce35ea285c4`. The tracked working tree was clean. The following untracked paths were deliberately not committed:

- `.codegraph` — pre-existing user artifact;
- `mcpack-reconstructed-28(1).bundle` — pre-existing user recovery bundle;
- `.ulw-notepad.md` — live-session symlink to transient agent state, not project evidence.

Do not delete, stage, or commit the first two paths. The live-session symlink may disappear when that agent session ends and is not a repository requirement.

All relevant Item 2 and Item 3 implementation, tests, committed evidence, source maps, and acquisition procedures through the stop boundary are already committed and pushed. There were no additional uncommitted project sources to rescue when this handoff was prepared.

The handoff commit is marked by annotated tag `item-3-jar-inspection-checkpoint-2026-09-01`. This is a durable partial-work checkpoint only; it does not mark Item 3 complete.

### 0.3 Item 2 — complete from primary empirical evidence

Item 2 passed its reconstructability exit gate. The accepted target is Minecraft 1.21.1, NeoForge 21.1.249, and Eclipse Temurin 21.0.12.1+1-LTS. The zero-mod server booted, flushed, stopped, restarted the existing world, was archived, independently restored, and booted again. The full installed archive was not redistributed because it contains third-party binaries; exact official acquisition plus the public state overlay is the reproducible equivalent.

Relevant pushed commits:

- `884beec` — strict evidence validation;
- `7afacb4` — exact platform provisioning;
- `40ebd9ac4beb3258d1ab3b88e7941da0bf5f5548` — reconstructed baseline evidence;
- `5fce47f1f11a6ffeb1ef7b1dddfafdb7dc6eab29` — Item 2 closeout.

Validated tags and durable assets:

- `item-2-evidence-assets-2026-09-01` targets `40ebd9a` and publishes:
  - `pristine-baseline-v0-state.tar.gz`, 1,275,395 bytes, SHA-256 `d7880902d37011075a3548404ffe84f0073ef5da7788b6244a24204dd3531663`;
  - `item2-raw-evidence-2026-09-01.tar.gz`, 389,164 bytes, SHA-256 `e97ffe0f036e66be301604de867154a1532f20a5b8cc896c4ed93330e5ae239d`.
- `item-2-baseline-recovery-2026-09-01` resolves to `5fce47f1f11a6ffeb1ef7b1dddfafdb7dc6eab29`.

Primary Item 2 evidence is under `evidence/item-2/`; raw runtime evidence and exact acquisition records are under `evidence/raw/item2/` in the reconstructable evidence layout. Do not modify the frozen Item 2 control while finishing Item 3.

### 0.4 Item 3 — committed progress, not completion

Exactly 190 candidate filenames have exact file-level primary-source identities: 176 from Modrinth and 14 from CurseForge. All 190 exact artifacts were acquired into ignored audit storage and verified against publisher hashes where supplied or official file sizes where publisher hashes were unavailable. The acquisition set totals 699,397,290 bytes.

All 190 outer archives passed ZIP integrity, path-safety, and expected SHA-256 checks. The inspection classified 188 outer archives as mods and 2 as libraries. Thirty-nine candidates contain embedded JARs; 204 embedded JARs were inspected, and no archive-integrity issue was reported. These facts prove artifact identity and parseability only. They do not prove loader compatibility, dedicated-server compatibility, dependency closure, conflict freedom, gameplay correctness, or acceptable performance.

Relevant pushed commits, in order:

- `3da9f40` — exact candidate audit model and validator foundation;
- `ca807f97ddc1e36f3e1418e5ce97bdc601ef621a` — exact source identities and raw-source manifest;
- `4c40642` — remote source-evidence verification;
- `ac3b9f5` — exact candidate acquisition and identity manifest;
- `e217570` — top-level candidate JAR metadata inspection;
- `3d1f33551700c9804503d0e27edddce35ea285c4` — embedded-JAR metadata inspection.

Validated Item 3 source-evidence milestone:

- annotated tag `item-3-primary-source-evidence-2026-09-01` resolves to `ca807f97ddc1e36f3e1418e5ce97bdc601ef621a`;
- release asset `item3-primary-source-raw-2026-09-01.tar.gz` is 20,124,166 bytes with SHA-256 `f2bf2902ade83adb3c8e7aac9bb1527000a04833267325666a6e934984a9ef04` and 771 archive members;
- `evidence/item-3/source-evidence-durability.json` records a passing fresh-download, hash, size, and tar-listing verification.

Machine-readable committed evidence:

- `evidence/item-3/source-identity-matrix.json` — exact primary file identities;
- `evidence/item-3/raw-source-manifest.json` — 767 preserved primary-response files, 122,432,761 bytes;
- `evidence/item-3/source-evidence-durability.json` — release retrieval and integrity receipt;
- `evidence/item-3/artifact-acquisition-manifest.json` — exact 190-file acquisition identities and computed hashes;
- `evidence/item-3/jar-inspection.json` — outer and embedded archive/metadata inspection.

Reproduction sources:

- `candidate-mods/item3-curseforge-file-map.json`;
- `candidate-mods/item3-search-query-overrides.json`;
- `src/mcpack_evidence/item3*.py`;
- `src/mcpack_evidence/raw_manifest.py`;
- `tests/item3/`;
- `tools/build_candidate_source_matrix.py`;
- `tools/collect_candidate_modrinth.py`;
- `tools/collect_candidate_curseforge.py`;
- `tools/build_raw_evidence_manifest.py`;
- `tools/acquire_candidate_artifacts.py`;
- `tools/inspect_candidate_jars.py`.

The exact candidate JARs are intentionally not committed to Git. Their ignored local acquisition path at the stop boundary is `downloads/item3/candidates/`. Reacquire them with the committed acquisition tool and verify the regenerated acquisition manifest before relying on them. The committed primary-response bundle contains no candidate JARs.

### 0.5 Named hazard evidence

These are verified static facts, not final enablement decisions:

- `DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar` is exact Modrinth version `erk04BGa`, 244,981 bytes, SHA-256 `549040fbd81d1b33aea38681109685e86d63985785246a831112c4ba5740d2df`. Its embedded NeoForge metadata identifies `dungeons_arise_seven_seas`, Minecraft range `[1.20,1.22)`, and NeoForge range `[21,)`; Minecraft 1.21.1 falls inside the declared static range. The broad filename and changing platform labels remain hazards requiring an explicit audited disposition.
- `adorabuild-structures-2.11.0-neoforge-1.21.3.jar` is exact Modrinth version `l7GS6bZj`, 657,734 bytes, SHA-256 `6f399680da36dbb95b9a0dbf8b600f173e650be4d6bc25f50fcac792dcce081e`. Its embedded NeoForge metadata identifies `adorabuild_structures`, Minecraft range `[1.21,1.21.3]`, and NeoForge range `[21.0.0-beta,)`; Minecraft 1.21.1 falls inside the declared static range. The filename naming 1.21.3 must not be silently ignored, but it is not by itself proof of incompatibility.
- `cc-tweaked-1.21.1-forge-1.116.1.jar` contains NeoForge metadata and declares NeoForge `[21.1.9,21.2)`. Its filename alone is not loader evidence.
- `sliceanddice-forge-4.2.4.jar` contains NeoForge metadata and declares Minecraft `[1.21.1,)`, NeoForge `[21,)`, and required dependencies including Kotlin for Forge `[5.8,)` and Create `[6.0.9,7.0.0)`.
- `modelfix` contains a malformed dotted dependency-table owner (`1.21-1.10`) and is client-side. Preserve this as a metadata hazard; do not repair upstream metadata or infer that the loader enforces the orphaned declarations.
- `kotlinforforge-5.11.0-all.jar` is an outer `FMLModType: LIBRARY`; its nested metadata supplies the `kotlinforforge` mod identity. A top-level-only audit is insufficient.
- Forgified Fabric API exposes both top-level and nested module identities. Do not treat a multi-loader artifact's inactive Fabric metadata branch as an active NeoForge hard dependency without proving the loader behavior.

### 0.6 Evidence categories at the stop boundary

**Verified from primary evidence:** exact source records for all 190 candidates; exact acquired bytes and computed hashes; publisher hash/size checks; outer and embedded ZIP integrity; parsed metadata documents; Item 2 server lifecycle and restore evidence; published release-asset integrity.

**Reconstructed documentation:** reports and protocols inherited from the recovered 28-commit history remain context only unless superseded by the new Item 2 or Item 3 acceptance evidence above.

**Provisional conclusions:** a declared Minecraft or NeoForge range containing the target is a static compatibility signal, not an enablement decision; embedded-library overlaps are potential conflict signals until loader selection and runtime behavior are evaluated.

**Untested assumptions:** no candidate has yet been accepted for the dedicated-server stack; the full 190-candidate set has not been booted and should not be; server/client classifications, dependency closure, conflict behavior, optional integrations, and actual runtime compatibility are unfinished.

**Missing evidence:** the final 190-row compatibility matrix; a machine-readable dependency/conflict/embedded-overlap evaluation; authoritative loader-semantics citations with retrieval dates; focused runtime boot evidence for retained clusters and named hazards; the human-readable Item 3 audit; decision-log entries; limitations and reproduction closeout; Item 3 exit-gate assessment; a final Item 3 recovery tag. Items 4–10 remain pending behind this gate.

### 0.7 Exact restart instructions

1. Read `SPECS.md` completely, then read this entire handoff and `INFRASTRUCTURE-INSTALLATION-AND-SERVER-TESTING.md` completely. The infrastructure document is supplementary and does not supersede `SPECS.md` ordering.
2. Run `git fetch origin main --tags`, verify branch/upstream/history/tags, and confirm `HEAD == origin/main` before editing.
3. Preserve `.codegraph` and `mcpack-reconstructed-28(1).bundle` unchanged.
4. Verify the committed Item 3 evidence and reacquire ignored candidate artifacts if the local audit cache is absent.
5. Resume by grounding NeoForge dependency/version-range/side and Jar-in-Jar semantics, plus Fabric metadata semantics, in authoritative primary sources. Record exact URLs and retrieval date.
6. Add failing-first tests for the compatibility evaluator. Evaluate active NeoForge metadata separately from inactive Fabric metadata on multi-loader artifacts.
7. Produce the dependency graph, side classifications, missing required dependencies, conflicts, optional integrations, and embedded-library overlap report for all 190 exact candidates.
8. Keep every candidate disabled until its disposition is supported. Perform focused isolated runtime boots only for evidence-supported retained clusters; do not mutate the frozen Item 2 control.
9. Publish the machine-readable compatibility matrix and human audit, with explicit decisions for every candidate and both named hazards. Complete the Item 3 decision log, limitations, reproduction record, and exit-gate assessment.
10. Inspect every diff, commit in small conventional increments, push each commit immediately, and create a validated Item 3 recovery tag only after the full Item 3 exit gate passes.
11. Do not begin Item 4 until every applicable Item 3 subitem and gate is genuinely complete.

The last known full validation after the embedded-metadata commit was 28 passing tests plus clean scoped Ruff, formatting, and basedpyright checks for `src/mcpack_evidence`, `tests`, and the Item 3 tools. Fifteen Ruff findings in later reconstructed tools pre-date this work and were deliberately not mixed into Item 3. Re-run the applicable checks after any new change rather than treating this statement as current proof.

---

## 1. Instructions to the Receiving Agent

Read this file completely before acting. Then read, in this order:

1. `RECOVERY-NOTICE.md`
2. `Adventure-Engineering-Pack-Execution-Ledger.md`
3. `docs/design/design-contract.md`
4. `docs/design/earned-sandbox-freedom.md`
5. `docs/recovery/reconstruction-manifest.md`
6. The report or protocol for the exact item being resumed

Do not infer completion from commit messages, report prose, or a successful server launch. The current repository is a transparent reconstruction of a lost working repository. It contains genuine surviving documents, reconstructed tools/protocols, and explicitly non-authoritative result summaries. Raw evidence that was lost must be regenerated.

Work chronologically and dependency-first. Ask the user only when a missing answer is genuinely load-bearing. When the user is absent, log an unknown or a reversible provisional decision rather than silently inventing a value. Continue autonomously whenever the next action is authorized and reversible.

Every change must be:

- atomic;
- validated;
- committed with a conventional, descriptive message;
- pushed immediately to the canonical GitHub repository;
- followed by verification that local `HEAD` equals `origin/main`.

Large or expensive evidence must also receive a durable archive, checksum manifest, and Git tag before downstream work proceeds. Never allow authoritative work to exist only in `/workspace/scratch`, `/tmp`, or another transient directory.

---

## 2. Project Goal

Build the user's long-lived Minecraft Java 1.21.1 NeoForge pack and dedicated server as an **engineering-driven multiplayer adventure sandbox**.

The pack should evoke the engineering freedom and multiplayer chaos that attracted the user to Michael Reeves's “pisspack,” while rejecting spellcasting, wizard progression, mandatory RPG leveling, inflated legendary loot, and generic damage-sponge combat.

Engineering is the principal capability-progression system. Exploration supplies reasons to engineer. Combat creates expedition pressure. Logistics, infrastructure, factories, computers, vehicles, trains, aircraft, weapons, and siege systems should all have durable roles.

The candidate JAR list is a tentative first draft, not a target manifest. Mods may be added, removed, replaced, or rejected whenever evidence and the design contract justify it. Do not optimize around preserving the candidate list.

---

## 3. Binding Design Contract

These decisions are non-negotiable unless the user explicitly revises them.

### 3.1 Identity and progression

- Engineering-driven multiplayer adventure sandbox.
- Engineering is the primary capability progression.
- Exploration exists partly to give engineering sustained purpose.
- Combat is expedition pressure, not the primary progression system.
- Logistics and infrastructure are meaningful gameplay and progression.
- RPG elements remain lightweight and subordinate to adventure.
- Prefer horizontal capability expansion over vertical stat escalation.
- No mandatory character levels.
- No mandatory skill trees.
- No wizard or spell progression.
- No generic legendary-loot treadmill.
- No uncontrolled attribute inflation.
- No routine damage-sponge enemies.
- Create Enchantment Industry may remain only when it functions as engineering, not spell progression.
- Basic Create, CC:Tweaked, transportation, trains, and Aeronautics must remain normally obtainable rather than rare dungeon-RNG gates.

### 3.2 Aesthetic and dimensions

- Mostly grounded industrial presentation.
- Overt fantasy beyond vanilla requires a specific gameplay justification.
- Fantasy creatures, dimensions, vanilla-like enchanting, and non-spell rewards are not automatically banned.
- Aether, Deep Aether, BetterEnd, and other dimension candidates remain undecided until their roles are tested against the pack identity.

### 3.3 Multiplayer and lifecycle

- Cooperative PvE is primary.
- PvP is optional and consensual.
- Unwanted griefing must receive technical protection.
- Normal target: 2–6 concurrent players.
- Understood peak: 10 players.
- Adventure & Engineering v1 may require a fresh world.
- The launched v1 world is persistent afterward, with no scheduled resets.

### 3.4 Transportation roles

- Walking: local and early exploration.
- Horse/boat: local and regional mobility.
- Trains: persistent, high-throughput regional logistics and infrastructure.
- Aircraft: flexible long-range expedition travel.
- Aircraft must improve exploration materially without erasing adventure or making trains pointless.
- Underground topology is expected to counterbalance aircraft naturally.

---

## 4. Earned Sandbox Freedom Doctrine

This doctrine resolves all breaching, automation, sequence-breaking, and bypass questions.

1. A powerful bypass is valid when the capability required was meaningfully earned.
2. Required effort may come from engineering complexity, infrastructure, materials, energy/fuel, knowledge, travel, setup time, logistics, risk, or upkeep.
3. Power should be proportional to investment.
4. Legitimately obtained capabilities remain real; do not negate them with arbitrary blacklists, universal unbreakable blocks, invisible restrictions, or special-case prohibitions.
5. Players may breach, mine, tunnel, fly, bombard, automate, remotely operate, extract, industrialize, or sequence-break when the solution satisfies the earned-effort rule.
6. Authored routes and encounters are not sacred.
7. If a loop is too cheap, rebalance its inputs, throughput, risk, setup, renewability, or upkeep rather than simply banning engineering.
8. Bugs, duplication glitches, corruption, crashes, desynchronization, permission escapes, and implementation errors are not earned capabilities.
9. Freedom never authorizes unwanted PvP, destruction, theft, surveillance, or denial of service against other players.
10. Shared-server stability may impose the least restrictive constraint necessary to prevent disproportionate harm.
11. Engineering may eventually compress or dominate parts of the adventure loop after substantial investment; it must not erase the loop trivially or prematurely.

Use this doctrine as an explicit acceptance criterion in every later design and exploit audit.

---

## 5. Platform and Scale Facts

| Field | Binding/current value |
|---|---|
| Minecraft | Java Edition 1.21.1 |
| Loader | NeoForge 21.1.249 |
| Java | Eclipse Temurin JDK 21.0.12.1+1 LTS, x86-64 HotSpot |
| Baseline gameplay mods | Zero |
| Baseline `mods/` | Empty |
| EULA | User explicitly accepted; `eula=true` authorized |
| Construction heap | `-Xms1G -Xmx4G`; not a final production allocation |
| Current build host | Linux x86-64, 9 logical CPUs, about 21 GiB RAM, about 30 GiB initially free |
| Server | Dedicated modded Java server; production provider/hardware still unknown |
| Normal concurrency | 2–6 players |
| Peak concurrency | 10 players |
| World policy | Fresh v1 permitted; persistent afterward |

Previously reported pristine-baseline identities, which must be regenerated rather than blindly trusted:

- Path: `instances/pristine-baseline-v0`
- Reconstruction/proof seed: `8953077177248245348`
- Manifest: 133 files, 189,135,287 bytes
- Manifest-file SHA-256: `a257c6fc10e743de53a1dfb67ae123b147739b553d41a116985492f654dfc519`
- Snapshot SHA-256: `856f4ca927e9831c93771aa03adecdb186cb916ef134de32501720c507e74555`
- 72 publisher-hash-verified installer inputs were reported.
- First boot and one existing-world restart were reported successful.

Those results survived only as documentation after the workspace-loss incident. They are useful reconstruction targets, not current acceptance evidence.

---

## 6. Candidate Mod/JAR Context

The repository contains the exact proposed filename inventory at:

- `candidate-mods/current-jars-2026-09-01.txt`

It contains 190 filenames:

- 188 proposed enabled;
- 2 proposed disabled;
- the two disabled entries were Distant Horizons and Xaero's Minimap in the supplied list.

The surviving audits are:

- `docs/audits/Baseline-JAR-Inventory-Audit-v0.1.md`
- `docs/audits/Candidate-Identity-Compatibility-Audit-v0.3.md`

Previously reported audit facts:

- 190/190 candidate identities resolved.
- 176 resolved through Modrinth and 14 through official CurseForge records.
- 62/176 Modrinth candidates had a newer compatible release at audit time.
- 22 candidates used alpha/beta metadata.
- Five declared required dependency edges were missing across two dependency groups.
- Archers, Rogues, Armory, and Arsenal requested Spell Engine.
- LambDynamicLights requested Fabric API.
- 21 candidates were client-required/server-unsupported.
- Seven more were client-required/server-optional.
- Client and dedicated-server manifests must therefore be separate.

Named version hazards from the governing specification still require explicit verification:

- `DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar`
- `adorabuild-structures-2.11.0-neoforge-1.21.3.jar`
- every broadly labelled `1.21.x` JAR;
- every JAR naming a different Minecraft point release;
- every Forge-labelled JAR used under NeoForge;
- Fabric-derived components and Forgified Fabric API relationships;
- overlapping embedded libraries.

Separate engineering-anchor experiments were previously reported, but they are not baseline admission or final selection:

| System | Experiment version |
|---|---|
| Create | 6.0.10 |
| Create Aeronautics | 1.3.2, replacing proposed 1.3.0 |
| CC:Tweaked | 1.120.2, replacing proposed 1.119.0 |
| Sable | 2.0.5, replacing proposed 2.0.1 |

The four direct JARs plus 15 embedded dependencies were reportedly server-tested separately. That experiment must be regenerated before it is accepted as evidence.

Do not automatically add Spell Engine merely to preserve the combat candidates. The no-spell design direction may instead justify removing or replacing those mods. Decide from requirements and evidence, not candidate-list inertia.

---

## 7. Git and Recovery History

### 7.1 Incident

The original project repository contained 28 local commits but had no remote. It existed only in transient scratch storage. Workspace reclamation deleted:

- the original Git object database;
- raw evidence;
- original scripts and schemas;
- server instances;
- world snapshots;
- generated region files;
- detailed validators and logs.

Surviving durable materials were later recovered from Library. They included more than initially recognized: the ledger, candidate audits/list, Items 4–11 reports/runbooks, and related documentation.

### 7.2 Reconstruction truth

The published 28 commits are a deliberate replacement history, not the original byte-identical commits.

- Original hashes and exact early commit contents cannot be recovered.
- The final 18 original short hashes/subjects are recorded in `RECOVERY-NOTICE.md`.
- The replacement history preserves those known subjects in chronological positions where possible.
- Reconstructed scripts and JSON protocols are functional scaffolds, not claimed byte-identical originals.
- Files under `evidence/reconstruction/` explicitly declare when raw evidence is unavailable and an item must be rerun.
- Never cite a reconstructed summary as proof that a measurement gate passed.

### 7.3 Verified canonical remote

The remote was freshly cloned and verified while preparing this handoff:

```text
Repository: https://github.com/copeugne/mcpack
Branch: main
HEAD: d0f3d22e3c235c451d9ebcb517ea345bbfa2e8f5
Commit count: 28
Tracked files: 36
Tag: reconstructed-28 -> d0f3d22e3c235c451d9ebcb517ea345bbfa2e8f5
Tag: pre-reconstruction-e0eed6d -> e0eed6d53770622a47ae78fc4cceaad21bdbcd50
Working tree after fresh clone: clean
```

The `pre-reconstruction-e0eed6d` tag preserves the repository's initial placeholder commit before the reconstruction history replaced `main`.

### 7.4 Current 28-commit history

```text
174eece chore: initialize adventure engineering pack
9068223 docs: record reconstruction provenance
3d8a44e docs: establish pack design contract
fa556e6 docs: preserve tentative jar inventory
0667683 docs: audit tentative jar inventory
97bd948 docs: resolve candidate identities
efc5a69 build: pin pristine platform identity
47b5e7a test: define controlled seed environment
4f6cb22 test: define reproducible measurement methodology
a92098d docs: audit pristine configuration baseline
cdfe800 test: characterize pristine terrain control
38ec6d9 docs: inventory pristine structure families
ff43d82 docs: classify pristine structure families
30ed5e7 test: add structure density measurement harness
c880316 test: harden structure survey recovery
06856e8 test: define exploration pacing protocol
f33caaa docs: prepare exploration pacing runbook
e35622b test: validate final repaired chunk state
287bb92 perf: stream structure density analysis
e132602 test: verify exploration observation artifacts
87d58ab test: initialize exploration run manifests
7d737a6 perf: decode integrity NBT selectively
b703b4e test: cross-check selective NBT decoding
5fa6bac test: atomically checkpoint density runs
8238d13 test: resume checkpointed density surveys
9c3d522 test: record density generation integrity failures
d58736d test: record baseline structure density evidence
d0f3d22 docs: close baseline density audit
```

---

## 8. Evidence Hierarchy

### 8.1 Binding authority

1. Explicit user decisions in the design contract and Earned Sandbox Freedom Doctrine.
2. The current execution ledger's status vocabulary and no-assumption rule.
3. Freshly generated raw evidence with hashes, manifests, versioned protocols, and validation.
4. Surviving original reports as historical/reconstruction guidance.
5. Reconstructed tools and summaries as scaffolding only.

### 8.2 What is currently authoritative

- Pack identity and user preferences.
- Platform targets: Minecraft 1.21.1, NeoForge 21.1.249, Java target.
- Candidate filename inventory as a proposal.
- Development seed identities.
- Git remote state and reconstruction provenance.
- The fact that raw evidence was lost.
- The requirement to rerun Items 2–10.
- Item 11's need for real human observation.

### 8.3 What is not current acceptance evidence

- Any commit subject implying a measurement passed.
- `evidence/reconstruction/*.json` result counts.
- Previously reported hashes without regenerated matching artifacts.
- Reconstructed Python tools merely compiling.
- Surviving final reports by themselves.
- A server launching successfully.
- Candidate filenames claiming compatibility.

### 8.4 Completion rule

An item becomes `COMPLETE` only when:

1. every required input is identified;
2. every subitem is resolved;
3. raw evidence is retained and linked;
4. the exit gate explicitly passes;
5. failures have dispositions;
6. downstream assumptions are updated;
7. exact configuration/protocol versions are recorded;
8. the commit and evidence are pushed/archived durably.

Unknown values remain `UNKNOWN`. Resolve them only through explicit user decisions, artifact inspection, authoritative sources, controlled experiments, reproducible measurement, or derivation from already verified facts.

---

## 9. Current Master Status

| Item | Status | Meaning now |
|---:|---|---|
| 1 | `COMPLETE` | Design contract and sandbox doctrine survived and remain binding. |
| 2 | `BLOCKED` | Prior baseline result summarized; binaries, manifest, snapshot, and restore evidence must be regenerated. |
| 3 | `BLOCKED` | Candidate audit documents survived; source evidence/current availability must be regenerated/reverified. |
| 4 | `BLOCKED` | Seed identities/report survived; snapshots, scripts, and restore receipts must be rebuilt. |
| 5 | `BLOCKED` | Method report survived; protocols, schemas, fixtures, and tools need reconstruction verification. |
| 6 | `BLOCKED` | Report survived; machine-readable config evidence must be regenerated. |
| 7 | `BLOCKED` | Reported repeated samples survived; raw samples and verification must be regenerated. |
| 8 | `BLOCKED` | Report survived; structure matrix and registry verification evidence must be rebuilt. |
| 9 | `BLOCKED` | Classification report survived; family matrix and validator must be rebuilt. |
| 10 | `BLOCKED` | Final report/results survived; raw worlds, regions, logs, analysis, and validators must be rerun. |
| 11 | `BLOCKED` | Depends on recovered Item 10, then requires at least two blind human operators. |
| 12–18 | `UNSTARTED` | Strictly depend on completed Item 11 evidence. |
| 19–37 | `UNSTARTED` | Requirements/system design after verified baseline forensics. |
| 38–47 | `UNSTARTED` | Candidate feasibility, stack construction, encounters, loot, and engineering freeze. |
| 48 | `UNSTARTED` | Exact progression implementation; must be split into atomic gates. |
| 49–50 | `UNSTARTED` | Performance hardening and lifecycle validation. |
| 51 | `UNSTARTED` | Adventure v1 release freeze. |

Repository reconstruction is complete. **Scientific/evidence recovery is not complete.** Recovery Gate R-1 stays open until Items 2–10 have qualifying evidence again.

---

## 10. Previously Reported Item 7–9 Findings

Use these to detect gross reconstruction regressions, not as substitute evidence.

### Item 7 — pristine worldgen control

- Four deterministic seed roles.
- 50 stable-height/biome samples per seed.
- 200 samples total.
- Two independent final runs reportedly repeated every raw sample and derived statistic exactly.
- Zero relevant generation-problem lines were reported.
- No terrain, biome, or structure candidates were installed in that control.

### Item 8 — vanilla structure inventory

- 34 structure registry entries.
- 34 exact biome-tag bindings.
- 20 placement sets.
- Grouped into 21 gameplay families.
- Every declared loot source reportedly resolved against embedded vanilla data.

### Item 9 — provisional classification

- 4 ambient/Tier 0 families.
- 1 civilization family.
- 8 Tier 1 families.
- 1 Tier 2 family.
- 5 Tier 3 families.
- 2 Tier 4 families.
- No family was finally declared redundant or selected for removal.

---

## 11. Item 10 — Reported Baseline Density Result

### 11.1 Status

Previously measured, now `BLOCKED` because raw reproducibility artifacts were lost.

### 11.2 Frozen/reconstructed method

- Four deterministic Overworld seeds.
- Nested stages per seed:
  - Stage 1: 4,096 chunks.
  - Stage 2: 8,192 chunks.
  - Stage 3: 16,384 chunks.
  - Stage 4: 32,768 chunks.
- Aggregate ceiling: 131,072 chunks.
- Continue until every provisional category has at least 30 observations or Stage 4 ceiling is reached.
- Sparse categories at the ceiling are right-censored.
- Denominator: saved chunks whose status is exactly `minecraft:full`.
- Count: unique non-`INVALID` structure start keyed by registry ID and authoritative start chunk.
- Integrity requirements:
  - stored coordinate matches Anvil slot;
  - clean `save-all flush` and shutdown;
  - independent offline exact-slot scan;
  - no unreadable or coordinate-shifted accepted targets.

Relevant reconstructed files:

- `measurement/structure-density-v0.1.json`
- `tools/analyze_structure_density.py`
- `tools/structure-density-harness.md`
- `docs/recovery/structure-survey-recovery.md`
- `docs/recovery/atomic-checkpoint-policy.md`
- `docs/recovery/resume-policy.md`
- `docs/recovery/selective-nbt-decoder.md`

Treat these as requirements/scaffolding and validate them before use.

### 11.3 Reported aggregate findings

| Metric | Starts | Per 1,000 chunks |
|---|---:|---:|
| All structures | 1,007 | 7.6828 |
| Actionable locations | 831 | 6.3400 |
| Static hostile-location proxy | 762 | 5.8136 |
| Tier 2 proper dungeons | 100 | 0.7629 |
| Tier 3 major expeditions | 47 | 0.3586 |
| Villages | 31 | 0.2365 |
| Tier 4 objectives | 4 | 0.0305, right-censored |

Mineshafts accounted for:

- 476 starts;
- 47.3% of all starts;
- 57.3% of actionable starts;
- 73.3% of Tier 1 starts.

This is the central interpretation: geometric structure density was not obviously low, but much of it was underground, underwater, buried, or otherwise poorly discoverable. Static density cannot establish good player pacing.

### 11.4 Per-seed reported rates per 1,000 chunks

| Seed role | All | Actionable | Combat proxy | Tier 2 | Tier 3 | Villages |
|---|---:|---:|---:|---:|---:|---:|
| Ordinary | 7.7820 | 6.5308 | 5.8289 | 0.8240 | 0.0916 | 0.1831 |
| Mountainous | 5.2490 | 4.4861 | 3.9978 | 0.5188 | 0.8240 | 0.3662 |
| Ocean-heavy | 9.9487 | 7.9651 | 7.4463 | 0.8240 | 0.3357 | 0.2441 |
| Biome-diverse | 7.7515 | 6.3782 | 5.9814 | 0.8850 | 0.1831 | 0.1526 |

### 11.5 Reported quality controls and failures

Reported accepted final run: `item10-chunkpregen-full-r19`.

Reported accepted integrity:

- 32,768 full/correct target slots per seed.
- Zero final coordinate mismatches.
- Zero final unreadable slots.
- 200/200 height checks.
- 10,190/10,190 selective/full NBT field checks.
- 192/200 biome boundary comparisons were explicitly non-acceptance checks.

Reported rejected approaches/failures:

- Loaded/ticket probes did not prove final saved status.
- Heightmap presence did not prove `minecraft:full`.
- Immediate Chunky shutdown left 1,637/4,096 chunks non-full.
- Live `save-all flush` was not a per-tile serialization oracle.
- A broad completion regex matched the wrong line.
- Chunk Pregenerator area mode did not cover the exact requested rectangle.
- r18 diverse seed had one unreadable slot, three shifted coordinates, and only 28,863 full/correct targets.
- r19's first mountain process was interrupted before checkpoint and excluded.

The rerun must preserve failed attempts and dispositions instead of deleting inconvenient evidence.

### 11.6 What Item 10 did not prove

- It did not measure actual player-visible discovery.
- The combat number was a static location proxy, not observed combat.
- It did not evaluate the tentative 190-JAR stack.
- It did not justify adding/removing structure mods.
- It did not justify changing Sparse Structures or spacing.
- It did not establish dungeon mechanical quality.

Do not select solutions until Items 11–18 identify root causes.

---

## 12. Item 11 — Human Exploration Pacing Gate

### 12.1 Purpose

Item 10 asks where structures exist. Item 11 asks what a player actually sees and experiences while traveling.

A structure can exist without being visible, be visible without being actionable, or be actionable while still producing excessive dead travel or repetition. Headless scans cannot decide human visual recognition, perceived actionability, or meaningful-interaction time.

### 12.2 Test matrix

- Four seeds:
  - ordinary: `42`;
  - mountainous: `6671238423019257953`;
  - ocean-heavy: `95920844204830198`;
  - biome-diverse: `-3503646078644842058`.
- Three transport modes:
  - foot;
  - standardized horse;
  - vanilla boat using natural water only.
- Two endpoint types:
  - 3,600 seconds/60 minutes;
  - 10,000 horizontal path blocks.
- Three replicates per applicable seed × mode × endpoint cell.
- Maximum 72 valid human runs.
- Boat cells may be reviewed `not-applicable` only if the assigned route lacks a continuous natural navigable-water corridor.
- Foot and horse cells are not waived for ordinary terrain difficulty.

### 12.3 Operators

- At least two human operators.
- Each operator tests every transport mode.
- Operators remain blind to structure coordinates, Item 10 evidence, prior route observations, and seed-map results beyond the declared seed role.
- No `/locate`, spectator mode, free camera, debug structure display, or seed-map website.
- An operator cannot repeat a route they have already seen, even in another transport mode.

The unresolved human question is whether the user can be one operator and recruit a second. Do not ask it until Recovery Gate R-1 is near completion unless scheduling lead time justifies asking earlier.

### 12.4 Route bearings

- Fixed-time replicates: 0°, 120°, 240°.
- Fixed-distance replicates: 60°, 180°, 300°.
- Follow the assigned bearing within ±45°, permitting terrain/interaction detours and then resuming the bearing.

### 12.5 Required artifacts per valid run

- Complete client video.
- Five-second position trace.
- Event log.
- Dedicated server log.
- Post-run world archive.
- Run manifest conforming to `measurement/exploration-run.schema.json`.
- SHA-256 identities for external artifacts and manifest.
- Blind reviewer decision and annotations.

### 12.6 Metrics

- Visual discoveries per hour and per 1,000 path blocks.
- Actionable discoveries.
- Hostile encounter episodes.
- Proper dungeons and major structures.
- Villages.
- Meaningful activity time.
- Adventure Activity Ratio.
- Dead-travel percentage.
- Unique structure families per hour.
- Time to first repeated family.
- Repeats per 10,000 blocks.
- Median, range, and IQR by cell.

### 12.7 Current tooling

- `measurement/exploration-pacing-v0.1.json`
- `measurement/exploration-run.schema.json`
- `tools/create_exploration_run.py`
- `tools/analyze_exploration_pacing.py`
- `docs/items/Item-11-Baseline-Exploration-Pacing-Runbook.md`

These are reconstructed. Compile and test them, then validate that they implement the full surviving runbook before collecting human evidence.

Item 11 cannot be replaced with simulated clients, bots, structure scans, or the agent's subjective guess.

---

## 13. Governing 51-Item Dependency Spine

The original user specification is a chronological, dependency-ordered adventure-system plan. Preserve this order unless a documented dependency correction is required.

1. Design contract.
2. Baseline freeze.
3. Exact version/dependency audit.
4. Controlled test environment.
5. Measurement/profiling methodology.
6. Configuration audit.
7. Terrain/worldgen interaction audit.
8. Structure-family inventory.
9. Initial structure classification.
10. Structure and encounter density measurement.
11. Exploration pacing and repetition measurement.
12. Discoverability measurement.
13. Dungeon-quality measurement.
14. Enemy/combat-quality measurement.
15. Loot and salvage-economy audit.
16. Multiplayer persistence/depletion audit.
17. Baseline performance measurement.
18. Baseline root-cause report; diagnose without selecting final solutions.
19. Final adventure structure taxonomy.
20. Transportation-scale model.
21. Target adventure cadence.
22. Dungeon-topology requirements.
23. Dungeon-objective variety.
24. Dungeon persistence/repeatability policy.
25. Difficulty model.
26. Enemy roles and encounter archetypes.
27. Elite/miniboss/boss philosophy.
28. Loot economy.
29. Reward renewability and automation rules.
30. Engineering ↔ adventure integration.
31. Discovery/navigation progression.
32. Multiplayer expedition and loot rules.
33. Civilization/settlement roles.
34. Dimension roles.
35. Combat-mod boundaries.
36. Destructibility, breaching, and automation-bypass policy.
37. Expedition preparation, failure, and recovery.
38. Early candidate-mod feasibility screening.
39. Controlled structure-redundancy experiments.
40. Provisional content/worldgen stack freeze.
41. Proposed underground dungeon-layer integration and evaluation.
42. Combined provisional worldgen remeasurement.
43. Sparse Structures/Structure Essentials spacing and overlap tuning.
44. Encounter orchestration before AI enhancement.
45. Incremental AI/elite evaluation.
46. Multiplayer container/persistence foundation, including Lootr if justified.
47. Adventure-relevant engineering/combat stack freeze.
48. Exact loot, renewability, discovery, civilization, engineering, logistics, death, and failure implementation.
49. Final candidate performance hardening.
50. Early/mid/late/mature-server, exploit, redundancy, and regression validation.
51. Adventure v1 definition-of-done validation and freeze.

Later candidate names in the spec—Dungeon Crawl, Lootr, In Control!, Improved Mobs, Enhanced AI, Zombie Awareness, Mob Champions, Guard Villagers—are hypotheses, not mandated inclusions. A candidate must solve a documented measured problem and pass capability, compatibility, gameplay, performance, and redundancy gates.

---

## 14. Required Whole-Pack Plan Expansion

The 51-item source is strong for adventure/dungeon/exploration but insufficient as the complete engineering modpack master plan. Before release, add explicit tracks for:

1. Engineering capability inventory and ownership matrix.
2. Engineering tier/prerequisite graph.
3. Recipe/progression reachability proof.
4. Resource-generation and processing-loop balance.
5. Kinetic/power/fuel economy.
6. Logistics throughput tiers.
7. Train economics and persistent infrastructure role.
8. Aircraft construction, payload, fuel, range, speed, crash/loss, and recovery.
9. Stationary versus mobile factory boundaries.
10. Siege/ammunition economy.
11. CC:Tweaked/peripheral security, abuse, resource, and networking boundaries.
12. Chunkloading ownership, quotas, offline behavior, and recovery.
13. Contraption/vehicle assembly, restart, cross-chunk, crash, and persistence tests.
14. Numeric server performance budgets.
15. Numeric client FPS/frame-time/startup budgets.
16. Network bandwidth, latency, jitter, loss, disconnect, and desynchronization tests.
17. Client/server manifest separation.
18. Registry, tag, recipe, advancement, datapack, and loot-conflict audits.
19. Packaging, installer/import, distribution-channel, and licensing verification.
20. New-world/migration/upgrade policy and removed-registry handling.
21. Startup/shutdown, crash recovery, watchdog, disk exhaustion, monitoring, and log rotation.
22. Backup retention, restore-time objective, and real restore drills.
23. PvP, claims, anti-griefing, permissions, operator, and allowlist policy.
24. Onboarding, recipe-viewer, ponder/manual, advancement, and knowledge-delivery policy without a quest railroad.
25. Accessibility, remappable controls, subtitles/cues, localization scope, and text legibility.
26. Semantic pack versioning, staging, changelog, rollout, rollback, and compatibility windows.
27. Release rollback drill covering world, server, configs, mods, and clients.

Item 48 must be split into independently versioned implementation and validation gates. Items 49–50 need corrective-loop ownership: every failure routes to a specific design/configuration owner, rollback point, retest scope, and regression subset.

---

## 15. Immediate Recovery Plan for the New Agent

### Step 0 — establish durable working state

```bash
git clone https://github.com/copeugne/mcpack.git
cd mcpack
git fetch --tags --prune
test "$(git rev-parse HEAD)" = "d0f3d22e3c235c451d9ebcb517ea345bbfa2e8f5"
test "$(git rev-list --count HEAD)" -eq 28
git status --short --branch
```

Confirm write access with a harmless, authorized workflow before starting expensive work. Do not generate new evidence until commits can be pushed and large artifacts can be archived durably.

### Step 1 — add this handoff to the repository

Add, validate, commit, and push this file as the first new atomic commit. Do not rewrite the reconstructed 28 commits.

Suggested commit:

```text
docs: add new-session project handoff
```

### Step 2 — validate reconstructed scaffolding

- Compile every Python tool.
- Parse every JSON file.
- Verify schema behavior with positive and negative fixtures.
- Compare reconstructed code to surviving report requirements.
- Record gaps instead of assuming behavioral equivalence.
- Push tool corrections atomically before any measurement run.

### Step 3 — rerun Item 2

- Acquire exact official Minecraft/NeoForge/Java inputs.
- Verify publisher hashes and versions.
- Build pristine zero-mod server.
- Generate default configuration with authorized EULA.
- Boot fresh world, save/flush/stop, restart same world, save/flush/stop.
- Freeze manifest and archive.
- Restore into a separate tree.
- Verify every path, size, and SHA-256.
- Record host identity and construction JVM flags.
- Archive evidence durably.
- Update ledger from `BLOCKED` to `COMPLETE` only after exit-gate proof.
- Tag and push.

### Step 4 — rerun Item 3

- Revalidate all 190 candidate identities against current official project metadata.
- Record exact game/loader/environment support.
- Resolve required and optional dependencies.
- Separate client/server candidates.
- Recheck suspicious 1.21.x and 1.21.3-labelled files.
- Preserve source URLs, retrieval times, licenses, hashes, and audit output.
- Do not download or admit the entire candidate pool automatically.

### Step 5 — rerun Items 4–6

- Regenerate the four deterministic seed snapshots.
- Rebuild repeatable deletion/restoration procedures.
- Rebuild measurement schemas, fixtures, and validator tests.
- Reaudit pristine config/defaults without changing them.
- Perform and retain an actual restore boot.
- Commit/push/tag each independently complete item.

### Step 6 — rerun Items 7–9

- Regenerate and independently repeat terrain/biome samples.
- Rebuild exact structure registry/biome/placement/loot inventory.
- Rebuild 21-family matrix and validator.
- Reapply provisional classification with deficiency/redundancy flags.
- Do not make final retention/removal choices yet.

### Step 7 — rerun Item 10

- Validate the generation harness on small pilots first.
- Preserve all failed pilots and dispositions.
- Generate the four exact nested stage rectangles.
- Require saved `minecraft:full` status and coordinate-correct Anvil slots.
- Cross-check selective NBT decode against a trusted full decoder.
- Use atomic checkpoints and clean resume rules.
- Run independent offline validation.
- Archive worlds/regions/logs separately with SHA-256 manifest.
- Produce stage analyses and final report.
- Compare new results with the historical reported result; explain differences rather than forcing a match.
- Only then return Item 10 to `COMPLETE`.

### Step 8 — prepare Item 11 human work

- Validate tools/runbook.
- Ask the user whether they can serve as one operator and recruit a second.
- Prepare blind route packets and pristine per-run restore process.
- Do not expose Item 10 coordinates to operators.
- Collect, review, hash, analyze, archive, commit, and push manifests/results.

### Step 9 — resume original dependency spine

Proceed to Item 12 only after Item 11's full human-observation exit gate passes.

---

## 16. Durability and Git Policy

The prior loss must not recur.

1. GitHub is canonical.
2. A local commit is not complete until pushed.
3. After every push:

   ```bash
   git fetch origin main
   test "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)"
   git status --short --branch
   ```

4. Commit protocols before experiments.
5. Never put secrets, tokens, addresses, allowlists, or player UUIDs into Git.
6. Large raw evidence stays outside normal Git but receives:
   - immutable archive name;
   - SHA-256 manifest;
   - size and file count;
   - matching Git commit/tag;
   - durable storage in at least two independent locations when practical;
   - a tested restore.
7. Tag each completed numbered item, for example `item-10-baseline-density-rerun`.
8. Create and durably save a verified full Git bundle after each phase.
9. Never delete failed evidence merely because it is inconvenient.
10. If push or archive persistence fails, stop downstream work until durability is restored.

---

## 17. High-Priority Unknowns

Do not ask all of these immediately. Resolve them at the owning dependency gate.

### Platform/release

- Final client and server pack formats.
- Distribution channels.
- Licensing/redistribution eligibility.
- Version/channel scheme.
- Upgrade and rollback compatibility windows.
- Supported client operating systems and hardware tiers.

### Production operations

- Hosting provider/model.
- CPU and dedicated/shared allocation.
- Physical RAM and final heap.
- Storage type, capacity, and I/O limits.
- OS/kernel.
- Uptime and maintenance expectations.
- Backup frequency, retention, size, duration, restore-time objective.
- World border and pregeneration policy.
- Monitoring/alert thresholds.
- Crash restart/watchdog.
- Log retention/redaction.
- Disk-growth budget.
- Claims, operator, allowlist, and permission details.

### Performance

- Idle/normal/combat MSPT budgets.
- Fresh-chunk latency/backlog budget.
- Sustainable aircraft speed.
- Memory/leak and GC budgets.
- Entity/block-entity tick budgets.
- Save-pause budget.
- Client FPS/frame-time/startup budgets.
- Network latency/jitter/loss/bandwidth assumptions.

### Engineering/adventure

- Full engineering inventory and capability ownership.
- Progression and recipe reachability graph.
- Power/fuel/logistics economies.
- Train/aircraft capability and cost boundaries.
- Chunkloading/offline-processing policy.
- CC:Tweaked security.
- Final structure thresholds/cadence/activity targets.
- Dungeon topology, persistence, objectives, and discovery.
- Difficulty, boss, loot, renewability, and multiplayer semantics.
- Dimension roles.
- Death/grave/vehicle recovery.
- Item 11 operator availability.

---

## 18. Things the New Agent Must Not Do

- Do not claim the reconstructed 28 commits are the original history.
- Do not mark Items 2–10 complete from surviving reports alone.
- Do not fabricate missing logs, worlds, hashes, samples, or validator output.
- Do not install all 190 candidates as the baseline.
- Do not treat filenames as compatibility proof.
- Do not choose final structure mods before baseline root-cause analysis.
- Do not solve poor cadence by making giant structures common.
- Do not add spell systems or a wizard progression path.
- Do not turn rare dungeon RNG into a gate for foundational engineering.
- Do not use universal indestructible dungeon blocks to protect authored routes.
- Do not ban a proportionately earned engineering bypass merely because it is powerful.
- Do not add AI stacks before testing encounter composition with existing AI.
- Do not stack redundant AI/difficulty systems.
- Do not use health/damage inflation as the default difficulty lever.
- Do not assume Lootr resets physical dungeons.
- Do not treat per-player loot multiplication as automatically harmless.
- Do not proceed to dependent items when an explicit test/decision gate has failed.
- Do not store authoritative work only in transient scratch storage.
- Do not ask the user non-load-bearing questions that can be measured, inspected, logged, or deferred.

---

## 19. Repository Map

| Path | Role |
|---|---|
| `Adventure-Engineering-Pack-Execution-Ledger.md` | Canonical status, decisions, unknowns, blockers, and next steps |
| `RECOVERY-NOTICE.md` | Truth about original loss and reconstructed Git history |
| `candidate-mods/current-jars-2026-09-01.txt` | Exact tentative filename pool |
| `docs/audits/` | Surviving candidate identity/JAR audits |
| `docs/design/` | Binding design contract and sandbox doctrine |
| `docs/items/` | Surviving Item 4–11 reports/runbooks |
| `docs/recovery/` | Reconstructed recovery/checkpoint/decoder contracts |
| `evidence/reconstruction/` | Explicitly non-authoritative historical summaries and rerun markers |
| `measurement/` | Reconstructed Item 10/11 protocols and schema |
| `platform/pristine-platform.json` | Reported platform target; requires regenerated evidence |
| `test-environment/seed-suite.json` | Development seed identities |
| `tools/` | Reconstructed analysis and run-manifest tooling |

---

## 20. Final Handoff Directive

Resume at **Recovery Gate R-1**, not Item 11 and not mod selection.

The first goal is to make the baseline scientifically reproducible again while preserving the user's design decisions and freedom doctrine. Rebuild Items 2–10 in dependency order, push every atomic change immediately, archive expensive evidence durably, and keep reconstructed historical results visibly separate from new acceptance evidence.

Once Item 10 is genuinely complete again, execute Item 11 with at least two blind human operators. Only then continue Items 12–51.

The project succeeds when it becomes a coherent engineering sandbox whose adventure layer gives factories, logistics, computers, vehicles, trains, aircraft, weapons, and siege equipment meaningful reasons to exist—without magic progression, arbitrary player restrictions, shallow structure spam, or an RPG loot treadmill.
