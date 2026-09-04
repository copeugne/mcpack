# Adventure & Engineering Pack — Execution and Evidence Ledger

**Ledger version:** 0.18
**Created:** 2026-09-01
**Governing source:** User-supplied `Adventure / Dungeon / Exploration System — Dependency-Ordered Implementation Plan — Revised` (Items 1–51)
**Current execution gate:** Recovery Gate R-1 — reconstruct baseline artifacts before Item 11
**Release state:** Not eligible for implementation or release

---

## 1. Purpose

This ledger prevents a checkbox from being treated as evidence. The submitted 51-item plan remains the governing adventure-system specification. This companion record tracks:

- decisions and their rationale;
- measurements and raw evidence;
- unresolved variables;
- blockers and dependencies;
- deviations from the source plan;
- configuration and artifact identities;
- validation failures and corrective loops;
- release-gate evidence.

The intended product is an engineering-driven multiplayer adventure sandbox, not a loosely curated collection of mods.

---

## 2. Evidence Rules

### 2.1 Status vocabulary

| Status | Meaning |
|---|---|
| `UNSTARTED` | No work or acceptable evidence exists. |
| `IN PROGRESS` | Work has started, but the exit gate is not satisfied. |
| `BLOCKED` | A named dependency, artifact, decision, or authority is missing. |
| `DECIDED` | A design choice has been explicitly ratified and recorded. |
| `OBSERVED` | A result was seen, but the test is not yet controlled or repeatable. |
| `MEASURED` | A result was produced by a defined method with retained raw data. |
| `VERIFIED` | Independent repetition or a deterministic verification supports the result. |
| `FAILED` | The exit gate or acceptance criterion was tested and not met. |
| `COMPLETE` | Every subitem and the exit gate have qualifying evidence. |
| `SUPERSEDED` | Replaced by a versioned decision; history remains recorded. |

### 2.2 Completion rule

An item is `COMPLETE` only when:

1. every required input is identified;
2. every subitem is resolved;
3. evidence is linked or embedded;
4. the exit gate has an explicit pass result;
5. known failures have dispositions;
6. downstream assumptions are updated;
7. the decision/configuration version is recorded.

“The server launched” proves only launch compatibility. It does not prove gameplay quality, interoperability, persistence correctness, scalability, or acceptable performance.

### 2.3 No-assumption rule

Unknown values remain `UNKNOWN`. They may be resolved only by:

- an explicit user decision;
- inspection of supplied artifacts;
- authoritative compatibility evidence;
- a controlled experiment;
- a reproducible measurement;
- a documented derivation from already verified values.

Default settings, filename claims, community reputation, and successful startup are not substitutes for verification.

---

## 3. Initial Structural Audit of the 51-Item Plan

### 3.1 Overall assessment

The source plan is unusually strong for an **adventure/dungeon/exploration subsystem**. It correctly delays final mod selection until after baseline forensics and requirements, distinguishes density from discoverability, treats multiplayer depletion as separate from Lootr-style container instancing, and validates mature-server behavior rather than only fresh worlds.

It is not yet a complete master plan for the requested **adventure and engineering pack**. Engineering is primarily treated as an input to adventure rewards and expedition utility. A comparable engineering/automation design, integration, balance, reliability, and validation track is absent.

### 3.2 Critical defects that prevent honest Item 51 completion

| ID | Defect | Consequence | Required correction |
|---|---|---|---|
| `AUD-001` | Scope mismatch: the document governs adventure systems, not the complete pack. | The final release could pass while core engineering progression is incoherent or unstable. | Decide whether this is a subsystem plan or expand it into the master pack plan. |
| `AUD-002` | No engineering capability/progression graph. | Add-ons may duplicate, bypass, or obsolete each other. | Add an engineering-system inventory, capability matrix, tier graph, recipe graph, and acceptance gates. |
| `AUD-003` | Performance metrics exist, but numeric budgets do not. | “Within target” in Item 51 is undefined. | Define TPS/MSPT, memory, GC, chunk latency, bandwidth, save, backup, restore, disk-growth, and client budgets before solution tuning. |
| `AUD-004` | Sampling words such as “representative” and “acceptable variance” are undefined. | Density and pacing claims can be cherry-picked or non-repeatable. | Define seed count, generated area, routes, repetitions, aggregation, outlier policy, confidence/variance reporting, and warm-up rules. |
| `AUD-005` | Candidate feasibility occurs too late for basic platform availability. | Requirements can name systems with no viable 1.21.1 NeoForge implementation. | Split candidate screening into early platform/build availability and later capability/fit testing. |
| `AUD-006` | Item 43 assumes tier-specific control through Sparse Structures/Structure Essentials before proving those controls exist. | The proposed tuning method may be technically impossible. | Add a configuration-capability map before committing to per-tier tuning. |
| `AUD-007` | Item 47 freezes the adventure-relevant engineering stack after much of the integration design. | Rewards and interactions may be designed against an unstable capability set. | Inventory and provisionally freeze core engineering capabilities earlier; retain a later final freeze. |
| `AUD-008` | Item 48 is a compound implementation program, not one atomic item. | Failures cannot be isolated and regression gates are unclear. | Split 48A–48F into independently versioned implementation and validation items. |
| `AUD-009` | Items 49–50 lack mandatory corrective-loop routing. | A failed validation has no formal path back to the owning design/config item. | Add defect ownership, rollback point, retest scope, and regression-loop rules. |
| `AUD-010` | No existing-world migration/new-world policy. | Removing or changing worldgen mods may corrupt, truncate, or permanently mismatch the production world. | Decide new-world versus migration; test upgrades, removed registries, explored/unexplored borders, and rollback. |
| `AUD-011` | No modpack packaging or distribution track. | A tested server tree may not produce a reproducible client/server release. | Add manifests, overrides, client/server separation, licensing/distribution eligibility, pack format, installer/import tests, and artifact hashes. |
| `AUD-012` | No update/channel/change-control policy. | Post-v1 changes can invalidate worlds or clients without controlled rollout. | Add semantic pack versions, changelog, staging, rollback, compatibility windows, and required retest mapping. |
| `AUD-013` | Server operations coverage is partial. | Performance may pass while the service is fragile operationally. | Add startup/shutdown, crash recovery, watchdog, log rotation, disk exhaustion, backup retention, monitoring, permissions, allowlist, and incident runbooks. |
| `AUD-014` | Client experience and client performance are absent. | Server health can pass while players experience crashes, unusable controls, recipe ambiguity, or poor FPS. | Add client hardware tiers, FPS/frame-time, load time, keybind conflicts, UI/recipe discovery, audio/visual clarity, and disconnect/reconnect tests. |
| `AUD-015` | No network budget or adverse-network testing. | Contraptions, aircraft, mobs, and chunk generation may be acceptable locally but fail under realistic latency/loss. | Add throughput, packet, latency, jitter, loss, reconnect, and desynchronization tests. |
| `AUD-016` | No registry/tag/recipe/loot conflict audit across the full stack. | Content may launch but contain broken recipes, duplicate tags, unreachable items, or economy leaks. | Add automated and manual datapack, recipe, tag, loot, advancement, and registry audits. |
| `AUD-017` | No explicit progression-reachability proof. | A circular or unreachable recipe chain can survive ordinary playtesting. | Build a progression dependency graph and verify every required capability from a fresh state. |
| `AUD-018` | No chunkloading/ticket policy. | Factories, trains, computers, mobs, and exploration can create uncontrolled persistent tick load. | Define allowed chunkloaders, ownership, quotas, offline behavior, force-load recovery, and performance limits. |
| `AUD-019` | No CC:Tweaked security/abuse policy. | Multiplayer computers/peripherals may create lag, unauthorized control, surveillance, or denial-of-service patterns. | Define resource limits, peripheral boundaries, networking rules, startup behavior, and abuse tests. |
| `AUD-020` | No destructive contraption/vehicle failure policy outside expeditions. | Crashes, unloaded chunks, claims, or restarts may destroy infrastructure or duplicate assets. | Add persistence, assembly/disassembly, cross-chunk, restart, crash, collision, and recovery tests. |
| `AUD-021` | PvP, griefing, claims, and social rules are unspecified. | Weapon, siege, breaching, and automation policies cannot be fully evaluated for multiplayer. | Explicitly define PvP/griefing/claim assumptions and enforcement boundaries. |
| `AUD-022` | No onboarding/knowledge-delivery plan for a complex engineering stack. | Players may be technically unblocked but unable to discover intended systems. | Define recipe viewer, ponder/manual coverage, advancement/guide policy, and information hierarchy without turning the pack into a quest railroad. |
| `AUD-023` | No localization/accessibility/usability gate. | Important discovery and combat cues may be inaccessible or unclear. | Define minimum text legibility, remappable controls, subtitle/cue expectations, and language scope. |
| `AUD-024` | No legal/distribution verification for modified configs, scripts, datapacks, and bundled mods. | The release artifact may not be distributable through the chosen channel. | Record licenses/permissions and channel rules for every redistributed component. |
| `AUD-025` | No explicit release rollback drill. | A bad release can be backed up yet still lack a tested downgrade path for server and clients. | Test release rollback including world, configs, mods, and client synchronization. |

### 3.3 Dependency/order corrections required

These amendments should be made without discarding the source plan’s useful order:

1. Add a pre-execution governance/evidence item before Item 1.
2. Expand Item 1 to establish the whole-pack scope boundary, magic boundary, PvP/griefing model, lifecycle target, and primary audience.
3. Complete Item 2 only from an actual supplied baseline archive and machine/server manifest.
4. Split Item 3 into:
   - installed-baseline compatibility audit;
   - early named-candidate build availability audit.
5. Expand Item 5 with a statistical sampling protocol and raw-data schema.
6. Add quantitative non-functional budgets after baseline measurement and before selecting/tuning solutions.
7. Add engineering baseline forensics and capability mapping before adventure-to-engineering reward design.
8. Add configuration-capability verification before Item 43.
9. Split Item 48 into separate implementation gates with a regression test after each.
10. Add packaging, migration, client QA, operations, release, and rollback phases before final freeze.
11. Replace the strictly linear “spine” with an explicit dependency graph plus a deterministic execution order. Independent work may be sequenced, but false dependencies should not be invented.

---

## 4. Item 1 — Design Contract Decision Record

### 4.1 Decisions already explicit and accepted

| ID | Binding decision | Status |
|---|---|---|
| `DC-001` | The pack is an engineering-driven multiplayer adventure sandbox. | `DECIDED` |
| `DC-002` | Engineering is the principal capability-progression system. | `DECIDED` |
| `DC-003` | Exploration gives engineering a sustained purpose. | `DECIDED` |
| `DC-004` | Combat supplies expedition pressure; it is not the primary progression system. | `DECIDED` |
| `DC-005` | Logistics and infrastructure are meaningful gameplay and progression. | `DECIDED` |
| `DC-006` | RPG elements remain lightweight and subordinate to adventure. | `DECIDED` |
| `DC-007` | Character levels, mandatory skill trees, stat inflation, damage sponges, and a legendary-loot treadmill are rejected. | `DECIDED` |
| `DC-008` | Spellcasting, wizardry, and supernatural spell progression are rejected. | `DECIDED` |
| `DC-009` | Create Enchantment Industry may remain when it functions as engineering rather than spell progression. | `DECIDED` |
| `DC-010` | Basic Create, CC:Tweaked, ordinary transportation, and basic Aeronautics progression remain normally obtainable and are not rare-dungeon RNG gates. | `DECIDED` |
| `DC-011` | Horizontal capability rewards are preferred over vertical stat escalation. | `DECIDED` |
| `DC-012` | Engineering solutions and reasonable sequence breaking are legitimate. | `DECIDED` |
| `DC-013` | Destructibility is the default; universal indestructible dungeon blocks are rejected. | `DECIDED` |
| `DC-014` | Aircraft materially improve exploration but must not erase adventure or train utility. | `DECIDED` |
| `DC-015` | Walking, horses, boats, trains, and aircraft each retain a distinct useful role. | `DECIDED` |
| `DC-016` | Factories, logistics, computers, vehicles, weapons, and siege equipment each retain meaningful use. | `DECIDED` |
| `DC-017` | The dedicated server is a first-class design target, not an afterthought. | `DECIDED` |

### 4.2 Unresolved Item 1 contract variables

| Variable ID | Question | Why it blocks later work | Status |
|---|---|---|---|
| `DC-U01` | Is this document the master whole-pack plan, or the adventure subsystem within a larger master plan? | **Resolved:** expand into the complete master plan, including engineering, client, operations, packaging, migration, and release. | `DECIDED` |
| `DC-U02` | What exactly is excluded by “no magic”: player spell systems only, or also fantasy dimensions, supernatural enemies/items, and vanilla-style enchantment? | **Resolved:** prohibit player spell systems and wizard progression; fitting fantasy creatures, dimensions, enchanting, and non-spell rewards may remain. | `DECIDED` |
| `DC-U03` | What is the accepted aesthetic boundary: grounded industrial, fantastical-but-non-spellcasting, or deliberately hybrid? | **Resolved:** mostly grounded industrial. Overt fantasy beyond vanilla requires specific justification; engineering remains the dominant player-facing language. | `DECIDED` |
| `DC-U04` | Is PvP expected, optional, or disabled; and is destructive griefing protected socially, technically, or not at all? | **Resolved:** cooperative PvE with optional consensual PvP and technical protection against unwanted griefing. | `DECIDED` |
| `DC-U05` | What is the intended server lifecycle and reset model? | **Resolved:** persistent world with no scheduled resets after v1. | `DECIDED` |
| `DC-U06` | What player range is the primary balance target? | **Resolved:** 2–6 normal concurrent players; 10-player peak. | `DECIDED` |
| `DC-U07` | What does “reasonable sequence breaking” permit and what outcomes must remain protected? | **Resolved:** earned sandbox freedom. Bypasses may be extremely powerful, but must require effort proportionate to their effect. Legitimately earned player capabilities are not arbitrarily disabled. Freedom and sandbox play take precedence, subject only to technical correctness, server stability, and player-consent/griefing boundaries. | `DECIDED` |
| `DC-U08` | Is a fresh world acceptable/required, or must an existing production world be preserved? | **Resolved:** Adventure & Engineering v1 may require a fresh world; that launched v1 world is then persistent. | `DECIDED` |

### 4.3 Earned Sandbox Freedom Doctrine

The following rules resolve the apparent conflict among source Items 29, 36, 50E, and 51:

1. **Capability must be earned.** The effort threshold may be supplied through engineering complexity, infrastructure, materials, energy/fuel, logistics, knowledge, risk, travel, setup time, or operational upkeep.
2. **Power must be proportional to investment.** A trivial, immediate, or nearly free bypass is a balance defect; a powerful result from a substantial engineered system is legitimate progression.
3. **Solutions remain real.** Once players have legitimately built or acquired a capability, the pack does not add arbitrary blacklists, indestructible blocks, invisible restrictions, or special-case prohibitions merely to force the authored route.
4. **Routes and encounters are not sacred.** Players may breach, tunnel, fly, bombard, automate, remotely operate, extract, or otherwise solve content in unintended ways when the solution satisfies the earned-effort rule.
5. **Industrialization is allowed.** A discovered reward or resource may become automatable if the automation path itself is legitimate and proportionately earned. The response to an overly cheap loop is to rebalance inputs, throughput, risk, setup, or renewability—not to negate engineering freedom.
6. **Bugs are not earned capabilities.** Duplication glitches, corruption, crashes, desynchronization, permission escapes, or implementation errors may be fixed without violating sandbox freedom.
7. **Consent remains binding.** Freedom does not authorize unwanted destruction, theft, PvP, surveillance, or denial of service against other players on the cooperative server.
8. **Shared-server stability remains binding.** Systems may be constrained only as necessary to prevent disproportionate technical harm, with the least restrictive mechanism that works.
9. **Item 51's word “trivially” is decisive.** Engineering may eventually compress or even dominate the adventure loop after meaningful investment; it must not erase the loop before that capability has been worked for.

### 4.4 Item 1 status

**Status: `COMPLETE`**
All identity, scope, magic, aesthetic, multiplayer, lifecycle, scale, world-start, and sequence-breaking variables are resolved. The design contract and Earned Sandbox Freedom Doctrine are binding evaluation criteria for every downstream system.

---

## 5. Item 2 — Baseline Intake Gate

### 5.0 Load-bearing correction: no existing instance exists

The user confirmed that there is currently no Minecraft instance and no downloaded mod set. Therefore:

- the 190 supplied filenames are a **proposed candidate inventory**, not an installed baseline;
- no existing configs, datapacks, logs, server properties, JVM flags, or worldgen settings exist to inspect;
- the existing technical baseline is therefore the pinned platform with an empty `mods/` inventory;
- filename compatibility cannot be presumed from a prior successful launch;
- the project must freeze that pristine platform separately from every later mod experiment.

The obsolete collection workflow was removed before it became a deliverable.

### 5.0.1 Revised dependency order for Items 2–6

1. Pin the platform: Minecraft, NeoForge, Java distribution/version, pack format, and test-host identity.
2. Preserve the tentative 190-filename pool without treating it as the target manifest.
3. Construct an empty-mod dedicated-server tree and a platform/client identity manifest.
4. Produce initial platform configs through controlled first launch, then version them.
5. Freeze and restore-test the pristine Baseline v0.
6. Continue Item 3 against candidates selected by later tasks; the pool may gain, lose, or replace mods.
7. Begin controlled test-environment and measurement-method construction before gameplay forensics.

This moves the necessary portion of original Item 3 ahead of baseline creation. It does not waive the later runtime compatibility audit.

### 5.1 Required final-pack artifact set

The project must eventually produce and retain the following for each release candidate. The pristine Item 2 baseline contains only the subset that exists for a zero-mod platform:

- separate client and server `mods/` inventories;
- disabled JARs or a separate disabled-mod inventory;
- `config/`;
- `defaultconfigs/`;
- `kubejs/`, CraftTweaker scripts, or equivalent scripting directories;
- `datapacks/` and world-specific datapacks;
- `server.properties`;
- NeoForge installer/version metadata;
- launcher or pack manifest (`manifest.json`, `modrinth.index.json`, or equivalent);
- `options.txt` and key mappings only if client experience is in scope;
- resource packs and shader configuration if distributed with the pack;
- representative `logs/latest.log` from a clean start and shutdown;
- crash reports, if any;
- world-generation preset/settings;
- JVM launch command/flags with secrets removed;
- backup configuration;
- test-host and eventual production-server OS, CPU model, physical RAM, allocated heap, and storage type;
- expected normal and peak concurrent players;
- whether the current world must be preserved.

Secrets, access tokens, addresses, allowlists, player UUIDs, and authentication credentials must never enter the versioned project artifacts.

### 5.2 Known baseline facts

| Field | Recorded value | Evidence state |
|---|---|---|
| Minecraft | Java Edition 1.21.1 | Mojang manifest resolved; server and mappings acquired and publisher-hash verified |
| Loader | NeoForge 21.1.249 | Official installer and runtime artifacts acquired; offline installation completed |
| Java | Eclipse Temurin JDK 21.0.12.1+1 LTS, x86-64 Linux HotSpot | Acquired from the official Adoptium release and SHA-256 verified |
| Installed third-party baseline mods | 0 | User confirmed no prior instance/mod installation; frozen `mods/` directory is empty |
| Create engineering experiment | Create 6.0.10 | Separate experiment acquired, hash-pinned, and server-tested; not baseline or final selection |
| Aeronautics engineering experiment | Proposed 1.3.0 replaced by 1.3.2 | Separate experiment acquired, hash-pinned, and server-tested; not baseline or final selection |
| CC:Tweaked engineering experiment | Proposed 1.119.0 replaced by 1.120.2 | Separate experiment acquired, hash-pinned, and server-tested; not baseline or final selection |
| Sable engineering experiment | Proposed 2.0.1 replaced by stable 2.0.5 | Separate experiment acquired, hash-pinned, and server-tested; not baseline or final selection |
| Server type | Dedicated modded Java server | Decided; production provider/hardware unknown |
| Normal concurrency | 2–6 players | User decision |
| Peak concurrency | 10 players | User decision |
| Existing world preservation | Fresh v1 world permitted; v1 world persistent afterward | User decision |
| Candidate filename inventory | 190 entries: 188 proposed enabled, 2 proposed disabled | Preserved in `current-jars-2026-09-01.txt`; not an installed baseline |
| Exact candidate identities | 190 of 190 resolved | 176 exact Modrinth identities plus 14 exact official CurseForge identities; zero unresolved filenames |
| Candidate version currency | 62 of 176 Modrinth candidates have a newer compatible release; 22 use alpha/beta metadata | Review queue only; upgrades are not automatic |
| Candidate declared dependency closure | Five required edges missing across two projects | Spell Engine requested by Archers/Rogues/Armory/Arsenal; Fabric API requested by LambDynamicLights |
| Candidate environment split | 21 Modrinth candidates client-required/server-unsupported; seven more client-required/server-optional | Dedicated-server manifest must be separate |
| Current test host | PikaOS 4, Linux 7.1.0, x86-64; AMD Ryzen 7 7840HS, 8 cores/16 logical CPUs; 27,091,542,016 bytes RAM; NVMe-backed Btrfs | Primary host discovery on 2026-09-01; not the production-server specification |
| Local platform installation | Complete through full server boot | Exact official installer completed without modifying its processor plan; fresh boot, restart, restore boot, and clean-room reconstruction all passed |
| Minecraft EULA | Explicitly accepted by the user for this local test server | `eula=true` recorded after authorization |
| Pristine baseline runtime | Fresh boot, existing-world restart, independently restored boot, and clean-room reconstructed boot passed | Four `Done` states, exact seed checks where applicable, flush operations, and clean shutdowns; only Minecraft and NeoForge loaded |
| Pristine generated world | Seed `8953077177248245348` | Reconstruction proof world; not a selected measurement seed |
| Pristine manifest | 135 files, 251 directories, 188,776,734 bytes | Manifest-file SHA-256 `d43da4f72d1de5fe03ae4ea03bc6948316f4667439a6ebc2d47c43ae3e5d7400` |
| Pristine snapshot | Independent extraction and deterministic repack pass; clean-room operational reconstruction also passes | Full local archive SHA-256 `4e4df44f0e0258f3814b5f20d22befd948dff58f21a5e2290ec087df53214c44`; durable state overlay SHA-256 `d7880902d37011075a3548404ffe84f0073ef5da7788b6244a24204dd3531663` |
| Engineering-anchor experiment | 4 direct JARs + 15 embedded dependencies | Separate first boot/two-restart experiment and restore proof passed; not baseline admission |
| Test heap | `-Xms1G -Xmx4G` | Construction-only envelope; not the final production allocation |

### 5.3 Item 2 status

**Status: `COMPLETE`**
The zero-mod original technical state is reconstructible from primary evidence: Minecraft 1.21.1, NeoForge 21.1.249, Temurin Java 21.0.12.1+1, zero third-party mods, generated platform configs/server properties, an empty dedicated-server `mods/` directory, and the recorded construction heap. Fresh boot, restart, independent archive restore, and clean-room materialization all passed. The redistributable state and raw-evidence assets were retrieved from the durable GitHub release with matching hashes, and evidence commit `40ebd9ac4beb3258d1ab3b88e7941da0bf5f5548` is pushed and tagged. The 190 supplied filenames remain a tentative candidate pool governed by Item 3.

The earlier reconstructed figures of 133 files, 189,135,287 bytes, manifest SHA-256 `a257c6fc10e743de53a1dfb67ae123b147739b553d41a116985492f654dfc519`, and snapshot SHA-256 `856f4ca927e9831c93771aa03adecdb186cb916ef134de32501720c507e74555` are retained here as superseded historical claims. They were not forced onto the newly observed baseline and are not acceptance evidence.

### 5.4 Mutable-instance integrity note

The authoritative local pristine baseline is `instances/pristine-baseline-v0` plus its verified frozen archive and manifests. The durable, redistributable recovery surface is the `item-2-evidence-assets-2026-09-01` release, exact authoritative input metadata, and the state overlay; the complete archive is not publicly redistributed because it contains Mojang and NeoForge software. Historical notes about Spark staging and an engineering-anchor experiment describe the lost predecessor workspace and are not claims about the recovered control. The recovered pristine working `mods/` directory and frozen baseline remain empty.

### 5.5 Item 6 configuration audit status

**Status: `COMPLETE`**
The exact retained stack contains 136 JARs under Minecraft 1.21.1, NeoForge 21.1.249, and Eclipse Temurin 21.0.12.1+1-LTS. A clean ordinary seed-42 lifecycle reached readiness, confirmed `save-all flush`, stopped cleanly, and returned zero. Materialization records the matching retained-manifest identity, no production state, and removal of the copied world before generation.

The frozen baseline contains exactly 228 configuration paths: 4 installation, 223 first-startup, 1 world-creation, and 0 shutdown-only. Its audit accounts for every path exactly once: 88 audited and 140 explicitly out of scope. It records 29 systems, 105 legacy setting rows, 44 grouped surfaces with 1,874 grouped leaves, and 7 findings under manifest schema v2. One generated web-validator credential is replaced at capture by an explicit sentinel and bound through `evidence/item-6/config-sanitization.json`; this is evidence-safety redaction, not tuning, and the other 227 frozen paths remain byte-identical. The validator rejects an identity mismatch, a malformed or noncanonical lifecycle/materialization receipt, a path escape or symlinked reference, a linked output parent, an unexplained manifest path, unknown fields, value or rationale mismatches, semantic audit inconsistencies, and a noncanonical manifest contract. Capture also fails before output creation for a missing, wrong-type, or symlinked required source, including nested source-tree symlinks.

No configuration was tuned. The frozen configuration, machine-readable audit, lifecycle and materialization receipts, and completion records are retained under `evidence/item-6/`; the narrative report is `docs/items/Item-6-Baseline-Configuration-Audit.md`. This establishes the unchanged baseline needed by Item 7 and does not claim Item 7 terrain observations or later item results.

### 5.6 Item 7 worldgen-control status

**Status: `PASS`, delivery review and merge pending**
The retained 136-JAR stack was exercised in two independent fresh runs across all four deterministic seeds. Each accepted seed run inspected 3,969 Overworld chunks and 961 chunks in each of the Nether, central End, and outer End, for 54,816 exact selected chunks across eight seed runs. All selected chunks were present once at `minecraft:full`. Sixteen Run A analyses contain all 192 required anomaly rows. Provider closure accounts for all 37 exact components: 23 directly observed, 4 observed through two independent targeted runs, 1 Better Caves generation failure, 7 indirectly observed, and 2 unobserved with explicit Item 8 limits.

Independent fresh runs are not semantically equal outside the central End. Input drift, decoder ordering, transport fields, and heightmap-only explanations were refuted; the causal provider remains `UNKNOWN`. The retained control also has two of 81 heightmap mismatches, so the Chunky comparison is not attributable under measured stack nondeterminism. The warning audit preserves 1,222 signatures and 14,003 occurrences, including 1,166 unresolved signatures rather than silently treating startup as compatibility proof.

The corrected 128 derived inspection captures passed two independent visual review lanes against one read-only r4 restore. The packaged restriction audit inspected 762 provider structures, resolved 757 restrictions, and recorded five impossible restrictions, including three active IDAS compatibility variants with missing tags. The later exact-SHA integrity review proved that restore target and receipt publication were still pathname-based. That review is preserved as rejected evidence. The final implementation publishes and rechecks the restored tree through pinned descriptors, publishes the receipt from a pinned parent, rejects scalar coercion, and rewinds directory descriptors before every scan. Four immutable r7 archives were rebuilt, restored file by file, published under tag `item-7-raw-evidence-2026-09-04-r7`, downloaded twice, and rehashed. Their manifests, corrected restore receipts, release receipt, tracked verification tool, independent 716-file world archive inventory, and 125-artifact completion receipt are committed under `evidence/item-7/`. The local completion gate returns `PASS`.

Exact-SHA local reviews at `97262a21b0b76c253f57e32b8665e48d0a63f822`, `8c7e7b8bb5db79d826b78cab5a678605a8b5fc23`, `438260f40fd0d50ff5f087a2b8aac028d5a39927`, and `5a5623fbe161c3ab1874c8184b8f9f1d0418c9cd`, plus GitHub Codex reviews at `eed044337bed03dcd8893d369cef9e6b5e6fd483` and `e26129498e905174df2ccbc067db589c244685b1`, rejected delivery. Their findings drove clean-export, descriptor custody, record-locking, strict-schema, repository-binding, destination-publication, restore publication, active mutation-test, packaged biome-restriction, raw world inventory, and corrected surface-analysis changes. All rejected reviews and dispositions are preserved under `evidence/item-7/review/`. Repository-level completion still requires fresh exact-SHA review, a clean Codex review cycle, merge into `main`, and delivered-ref verification.

### 5.7 Item 8 structure-inventory status

**Status: `BLOCKED` - previously complete; source matrix and verification evidence lost**
The surviving report records 34 structure registry entries, 34 exact biome-tag bindings, and 20 placement sets grouped exactly once into 21 gameplay families. It also records that declared loot sources resolve in the embedded vanilla data pack and that tentative mod families are absent. The report survives as `Item-8-Baseline-Structure-Inventory.md`, but `structure-inventory/vanilla-1.21.1-structure-families.json` and `evidence/structure-inventory/item8-registry-verification.json` do not. Item 8 must be reconstructed and rerun before its reproducibility exit gate may return to `COMPLETE`.

### 5.8 Item 9 provisional-classification status

**Status: `BLOCKED` - previously complete; family matrix and verification evidence lost**
The surviving report records all 21 baseline families with exactly one provisional primary category: 4 ambient, 1 civilization, 8 Tier 1, 1 Tier 2, 5 Tier 3, and 2 Tier 4. It also records explicit mechanical-depth, decoration, repetition, oversizing, value-concentration, discoverability, and internal-variant overlap flags, with no family declared redundant and no final retention decision. The report survives as `Item-9-Provisional-Structure-Classification.md`, but the family matrix and `evidence/structure-inventory/item9-classification-verification.json` do not. Item 9 must be reconstructed after Item 8 before its reproducibility exit gate may return to `COMPLETE`.

### 5.9 Item 10 structure-density status

**Status: `BLOCKED` — previously complete; raw reproducibility artifacts lost**
The predeclared four-stage protocol reached its 131,072-chunk ceiling. Every final one of 32,768 target slots per seed was independently decoded at `minecraft:full` with matching stored/slot coordinates; all four seeds converged monotonically in two clean passes. The baseline contains 1,007 starts (7.6828/1,000 chunks), 831 actionable-location starts (6.3400), a 762-location static hostility proxy (5.8136), 100 Tier 2 starts (0.7629), 47 Tier 3 starts (0.3586), 31 villages (0.2365), and four right-censored Tier 4 starts. Mineshafts are 57.3% of actionable starts, so static density cannot substitute for observed pacing/discoverability. Sparse Structures is absent and contributes exactly zero to this control. Evidence: `Item-10-Baseline-Structure-and-Encounter-Density.md`, `evidence/structure-density/item10-stage-evaluation-r19.json`, and `evidence/structure-density/item10-chunkpregen-full-validation-r19.json`.

The final report survives, but the referenced raw evidence, generator worlds, validators, and original Git objects were lost when the unpushed transient workspace expired. Item 10 must be reconstructed and rerun before its reproducibility exit gate may return to `COMPLETE`.

### 5.10 Item 11 preparation status

**Status: `BLOCKED` after all non-human preparation**
`exploration-pacing-v0.1`, its run schema, manifest initializer, analyzer, and operator runbook are complete. The binding matrix contains up to 72 valid runs: four seeds × three transport modes × two endpoint types × three replicates, with explicit boat not-applicable handling. Completion requires retained real-client video/trace evidence from at least two blind human operators. A headless structure scan cannot truthfully decide visual recognition, actionability, or meaningful-interaction time. No owner response is required while absent; the load-bearing human-observation gate is logged and kept on the back burner.

### 5.11 Preservation incident and Recovery Gate R-1

**Status: `IN PROGRESS`**
The original 28-commit repository existed only in a transient workspace and had no remote. Workspace reclamation removed the Git object database, raw evidence, scripts, schemas, server instances, and snapshots. Three durable records survived: this ledger, the Item 10 final report, and the Item 11 runbook. The loss invalidates reproducibility claims even where summarized results survive.

`https://github.com/copeugne/mcpack` is now the canonical remote. Recovery requires reconstructing the project tree, rerunning Items 2–10 where source evidence is unavailable, pushing every atomic commit, and creating tagged/bundled checkpoints for high-cost measurements. No summarized result will be treated as a substitute for missing raw evidence.

---

## 6. Undefined-Variable Register — Initial Pass

This register is additive. More variables will be discovered during artifact inspection and testing.

### 6.1 Platform and release

- `PLAT-001`: exact NeoForge version/build — **resolved: 21.1.249**.
- `PLAT-002`: exact Java vendor and patch version — **resolved: Eclipse Temurin 21.0.12.1+1 LTS**.
- `PLAT-003`: exact client and server pack formats.
- `PLAT-004`: distribution channel(s).
- `PLAT-005`: licensing/redistribution eligibility per component.
- `PLAT-006`: pack version scheme and release channels.
- `PLAT-007`: fresh-world versus existing-world migration requirement.
- `PLAT-008`: rollback compatibility window.
- `PLAT-009`: supported client operating systems.
- `PLAT-010`: supported client hardware tiers.

### 6.2 Server and operations

- `OPS-001`: hosting provider/model.
- `OPS-002`: CPU model and dedicated/shared allocation.
- `OPS-003`: physical RAM and heap allocation.
- `OPS-004`: storage medium, capacity, and I/O limits.
- `OPS-005`: OS/distribution and kernel.
- `OPS-006`: normal and peak player counts — **resolved: 2–6 normal, 10 peak**.
- `OPS-007`: uptime and maintenance expectations.
- `OPS-008`: backup frequency, retention, size, duration, and restore-time objective.
- `OPS-009`: world-border policy.
- `OPS-010`: pregeneration radius/strategy.
- `OPS-011`: monitoring and alert thresholds.
- `OPS-012`: crash-restart and watchdog policy.
- `OPS-013`: log retention and redaction policy.
- `OPS-014`: disk-growth budget.
- `OPS-015`: permissions, operator, allowlist, claims, and griefing model.

### 6.3 Quantitative performance budgets

- `PERF-001`: idle median and p95 MSPT ceiling.
- `PERF-002`: normal-play median and p95 MSPT ceiling.
- `PERF-003`: combat median/p95/p99 MSPT ceiling.
- `PERF-004`: fresh-chunk generation latency and backlog ceiling.
- `PERF-005`: sustainable aircraft speed under expected concurrency.
- `PERF-006`: memory steady-state ceiling and leak criterion.
- `PERF-007`: GC pause frequency/duration ceiling.
- `PERF-008`: entity and block-entity tick budgets.
- `PERF-009`: save duration and pause ceiling.
- `PERF-010`: client FPS/frame-time budgets by hardware tier.
- `PERF-011`: client startup/world-entry duration.
- `PERF-012`: network bandwidth, latency, jitter, and loss assumptions.

### 6.4 Statistical measurement protocol

- `STAT-001`: exact seed set and rationale — **development suite resolved: `42`, `6671238423019257953`, `95920844204830198`, `-3503646078644842058`; blinded v1 validation seeds remain later work**.
- `STAT-002`: generated radius/chunk count per seed and dimension — **resolved: 4,096 initial to 32,768 maximum fully generated chunks/seed until 30 category observations; sparse categories are right-censored**.
- `STAT-003`: route design and navigation-information controls — **resolved for Item 11 by `exploration-pacing-v0.1`: separate 60-minute and 10,000-block endpoints, fixed bearings, blind operators, and no `/locate`/seed-map knowledge**.
- `STAT-004`: repetitions per transport mode and progression stage — **resolved: three human gameplay runs/cell with at least two operators; runtime performance uses five measured plus one discarded warm-up replicate**.
- `STAT-005`: warm-up and cache rules — **resolved by `ae-measurement-v0.1`; unlike cache states are never combined**.
- `STAT-006`: operator/player skill controls.
- `STAT-007`: aggregation and dispersion statistics — **resolved: sample count, median, p95, p99, max, IQR/range, paired change and bootstrap 95% interval**.
- `STAT-008`: outlier and failed-generation handling — **resolved: retain primary outliers and failed runs; objective sensitivity analysis may be additional only**.
- `STAT-009`: acceptable variance and decision thresholds — **method resolved: owning items must predeclare practical thresholds; numeric targets remain intentionally unknown**.
- `STAT-010`: raw-data format, scripts, provenance, and retention — **resolved by run schema, template, validator and artifact hashes**.

### 6.5 Engineering system

- `ENG-001`: complete engineering/add-on inventory.
- `ENG-002`: capability ownership matrix.
- `ENG-003`: progression tiers and prerequisite graph.
- `ENG-004`: duplicated/obsolete capabilities.
- `ENG-005`: recipe conflicts and unreachable recipes.
- `ENG-006`: resource-generation and processing loops.
- `ENG-007`: power/kinetic/fuel economy boundaries.
- `ENG-008`: logistics tiers and throughput targets.
- `ENG-009`: train economics and infrastructure role.
- `ENG-010`: aircraft construction, fuel, payload, range, speed, and loss model.
- `ENG-011`: stationary versus mobile factory boundaries.
- `ENG-012`: siege/ammunition production and combat economy.
- `ENG-013`: CC:Tweaked/peripheral capability and security boundaries.
- `ENG-014`: chunkloading and offline-processing policy.
- `ENG-015`: contraption persistence, restart, cross-chunk, and recovery behavior.
- `ENG-016`: automation performance budgets by scale.
- `ENG-017`: engineering onboarding and information delivery.
- `ENG-018`: intended endgame engineering projects/capabilities.

### 6.6 Adventure, combat, and world

- `ADV-001`: magic/fantasy/aesthetic boundary.
- `ADV-002`: exact structure taxonomy thresholds.
- `ADV-003`: target cadence by tier, stage, and transport mode.
- `ADV-004`: Activity Ratio target and dead-travel ceiling.
- `ADV-005`: repetition limits and family-equivalence rules.
- `ADV-006`: discoverability scoring rubric.
- `ADV-007`: minimum dungeon topology metrics.
- `ADV-008`: dungeon persistence/repeatability policy.
- `ADV-009`: encounter difficulty budgets by group size.
- `ADV-010`: elite/miniboss/boss need and limits.
- `ADV-011`: reward value model and rarity bands.
- `ADV-012`: renewability/farmability/automation classifications.
- `ADV-013`: per-player/shared/global loot semantics.
- `ADV-014`: civilization density and functions.
- `ADV-015`: dimension inclusion and progression roles.
- `ADV-016`: breaching/sequence-breaking protected outcomes.
- `ADV-017`: death, grave, retreat, vehicle loss, and recovery policy.
- `ADV-018`: early/mid/late/mature-server time horizons.

---

## 7. Master Execution Status

| Item | Short name | Status | Current blocker/evidence |
|---:|---|---|---|
| 1 | Design contract | `COMPLETE` | Binding design contract and Earned Sandbox Freedom Doctrine recorded. |
| 2 | Freeze original technical baseline | `COMPLETE` | Reconstructed from exact inputs; manifest, configs, archive/overlay, four lifecycle scenarios, clean-room proof, durable retrieval, and pushed/tagged Git receipts pass. |
| 3 | Compatibility audit | `COMPLETE` | All 190 candidates have explicit dispositions; the 136-candidate retained dedicated-server set passes exact metadata/dependency checks and repeatable lifecycle validation. Evidence: `docs/items/Item-3-Exact-Version-and-Dependency-Audit.md`, `evidence/item-3/`. |
| 4 | Controlled test environment | `COMPLETE` | Isolated four-seed environment, reproducible materialization, lifecycle validation, and hash-verified backup/restore with restored-world boot pass. Evidence: `docs/items/Item-4-Controlled-Test-Environment-Closure.md`, `evidence/item-4/`. |
| 5 | Measurement methodology | `COMPLETE` | Strict 24-contract protocol, deterministic analyzer, pinned Temurin pilot, accepted/rejected handling, and cross-artifact hash validation pass. Evidence: `docs/items/Item-5-Measurement-Methodology-Closure.md`, `measurement/item5/`, `evidence/item-5/`. |
| 6 | Existing configuration audit | `COMPLETE` | Retained 136-JAR stack, 228 manifest paths with 4/223/1/0 stages, exhaustive 88/140 accounting, 29 systems, 105 legacy setting rows, 44 grouped surfaces with 1,874 grouped leaves, 7 findings, lifecycle/materialization receipts, sanitization binding, path and capture fail-closed gates, and `evidence/item-6/` report evidence pass. |
| 7 | Terrain/worldgen interactions | `PASS, DELIVERY PENDING` | Fresh four-seed retained-stack runs, 54,816 exact selected chunks, 192 anomaly rows, all 762 provider structure restrictions inspected, complete provider and warning dispositions, corrected visual review, final r7 raw archives, descriptor-bound tested restore, 716-file world archive inventory, and the 125-artifact completion gate pass. The latest valid review findings were fixed. Fresh exact-SHA review and merge remain. |
| 8 | Structure-family inventory | `BLOCKED BY ITEM 7 DELIVERY` | Begin only after the accepted Item 7 branch is reviewed, merged into `main`, and the delivered ref is verified. Then rebuild the runtime-backed canonical family inventory. |
| 9 | Initial structure classification | `BLOCKED` | Classification summary survives; family matrix and validator evidence must be reconstructed. |
| 10 | Baseline structure/encounter density | `BLOCKED` | Final report survives; raw generation, analysis, and validation evidence must be rerun. |
| 11 | Exploration pacing/repetition | `BLOCKED` | Also depends on recovered Item 10; afterward requires real-client observations from at least two blind human operators. |
| 12–18 | Remaining baseline forensics | `UNSTARTED` | Strict dependency on completed Item 11 evidence. |
| 19–37 | Requirements/system design | `UNSTARTED` | Depend on verified baseline report; Item 1 variables also affect them. |
| 38–47 | Feasibility and stack construction | `UNSTARTED` | Depend on requirements and actual mod artifacts. |
| 48 | Progression implementation | `UNSTARTED` | Must first be atomized into independent gates. |
| 49–50 | Hardening/lifecycle validation | `UNSTARTED` | Quantitative budgets and corrective loops absent. |
| 51 | Adventure v1 freeze | `UNSTARTED` | Whole-pack release gates are incomplete. |

---

## 8. Next Authorized Execution Step

1. Review the accepted Item 7 evidence and implementation at one exact commit, complete the GitHub Codex review loop, merge the pull request into `main`, and verify the delivered ref.
2. Begin Item 8 only from that verified merged `main`. Reconstruct the canonical runtime-backed structure-family inventory from registries, packaged data, configuration, logs, and generated-world observations.
3. Continue Items 9 and 10 in dependency order, then audit Items 2 through 10 together for identity and narrative consistency.
4. Do not implement, run, repair, or lint Item 11 until the cross-item audit passes. Item 11 will still require real-client evidence from at least two blind human operators.

No later item will be marked complete out of order or from inference.
