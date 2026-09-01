# Codex Cloud Continuation Handoff

- **Prepared:** 2026-09-01 (America/Los_Angeles)
- **Canonical repository:** `https://github.com/copeugne/mcpack`
- **Branch:** `main`
- **Pre-handoff source checkpoint:** `50a8d74b6627246059e714df55461e7206135819`
- **Cloud handoff milestone:** resolve annotated tag `cloud-handoff-item3-2026-09-01` after fetching tags
- **Live project status:** Item 2 complete; Item 3 incomplete and paused; Items 4–10 not accepted; Item 11 not authorized
- **Resume authorization:** this file prepares the work for continuation. The prior local session was explicitly stopped. A receiving agent must resume project execution only when its launching prompt authorizes continuation.

This file is the standalone operational entry point for a Codex Cloud agent. It does not replace `SPECS.md`, which remains authoritative for task order, dependencies, tests, gates, and definitions. It also does not replace `MCPACK-NEW-SESSION-HANDOFF.md`, which preserves the full recovery history and design context.

## 1. Original Objective

Recheck, execute, validate, document, and complete `SPECS.md` Items 2 through 10 in exact dependency order for a Minecraft Java 1.21.1 NeoForge engineering-driven multiplayer adventure pack. Work must be based on reproducible primary evidence, not reconstructed prose or a server merely reaching readiness.

The required end state is:

1. a reconstructable frozen technical baseline;
2. an exact per-artifact version, loader, dependency, side, conflict, integration, and embedded-library audit;
3. a separate deterministic test-server environment with controls and a proven restore boot;
4. implemented, reproducible profiling and gameplay-measurement procedures;
5. an audit of actual generated configurations without tuning;
6. empirical terrain and world-generation interaction evidence;
7. a runtime-backed inventory of every structure family;
8. an evidence-backed provisional structure classification;
9. valid baseline structure and encounter-density measurements across all selected seeds.

Do not begin Item 11 until every applicable Item 2–10 subitem, dependency, test gate, and exit gate has reproducible evidence in the repository or in a durable, hash-addressed evidence store referenced by the repository.

## 2. Governing Authority and Mandatory Read Order

Before any project action, read these files completely in this order:

1. `SPECS.md` — authoritative chronological and dependency-ordered specification;
2. this `CLOUD_HANDOFF.md` — live Cloud transfer state and exact restart point;
3. `MCPACK-NEW-SESSION-HANDOFF.md` — recovery history, design contract, previous evidence, and broader context;
4. `INFRASTRUCTURE-INSTALLATION-AND-SERVER-TESTING.md` — supplementary infrastructure requirements; it does not replace or reorder `SPECS.md`;
5. `RECOVERY-NOTICE.md` — provenance and the lost-work incident;
6. `Adventure-Engineering-Pack-Execution-Ledger.md` — decisions, unknowns, and historical status;
7. `docs/design/design-contract.md` and `docs/design/earned-sandbox-freedom.md`;
8. the report, protocol, source, tests, and machine evidence for the item being resumed.

Important status conflict: portions of `Adventure-Engineering-Pack-Execution-Ledger.md` section 5 call Items 6–9 complete based on prior reconstructed work, while its master table and the live handoff correctly mark them blocked/incomplete pending regenerated evidence. The live checkpoint in `MCPACK-NEW-SESSION-HANDOFF.md` and this file supersede those historical status statements. Do not edit `SPECS.md` checkboxes or mark an item complete merely to reconcile prose.

## 3. Exact Current Point and Stop Boundary

Item 2 has passed its reconstructability exit gate from new primary empirical evidence and is published. Item 3 is in progress. Work stopped after:

- exact source identity for all 190 candidates;
- acquisition and byte verification of all 190 exact artifacts;
- top-level and nested JAR/metadata inspection;
- capture of manifest `Implementation-Version` values;
- preservation and validation of an exact Maven version-range probe.

No final compatibility evaluator, 190-row disposition matrix, dependency closure, overlap classification, dedicated-server retained set, or runtime-cluster validation exists yet. Therefore Item 3 is incomplete. Items 4–10 must not be advanced until Item 3 passes its exit gate.

The final local action before this handoff was to preserve `tools/MavenVersionRangeProbe.java` in commit `50a8d74b6627246059e714df55461e7206135819`. It was compiled and exercised against the exact Item 2 Java and loader libraries. This is a validated utility checkpoint, not an Item 3 compatibility conclusion.

## 4. Evidence Vocabulary

Use these labels in every report and decision:

| Classification | Meaning at this checkpoint |
|---|---|
| Verified primary evidence | Directly observed artifact bytes, authoritative metadata, exact hashes, generated files, runtime logs, or executed tests retained with provenance. |
| Reconstructed documentation | Surviving reports/protocols recovered after the original transient workspace was lost. Useful as hypotheses and execution guidance, never sufficient for acceptance. |
| Provisional conclusion | A reversible interpretation supported by partial evidence but not yet through its owning gate. |
| Untested assumption | A planning input or expected behavior that has not been empirically validated. |
| Missing evidence | A required result, receipt, raw artifact, runtime observation, or independent check that does not exist or was lost. |

Never promote a reconstructed report, filename, metadata range, or successful launch into runtime compatibility, gameplay correctness, world-generation correctness, or acceptable performance without the evidence required by `SPECS.md`.

## 5. Current Status of Items 2–10

### Item 2 — Freeze the Existing Technical Baseline

**Status:** `complete`

**Exit gate:** pass — the zero-third-party-mod original technical state is reconstructable from exact official inputs, committed state, and validated remote assets.

| Specification subitem | Status and evidence |
|---|---|
| Minecraft version | Complete: 1.21.1. |
| Exact NeoForge version | Complete: 21.1.249. |
| Java runtime/version | Complete: Eclipse Adoptium Temurin 21.0.12.1+1-LTS, Linux x64 HotSpot. |
| Enabled and disabled JARs/mod versions | Complete for the frozen control: zero enabled and zero disabled third-party JARs; `mods/` exists and is empty. The 190 filenames are a separate tentative candidate inventory. |
| Configs, datapacks, server properties, world-generation settings | Complete: copied configs committed; no custom datapacks; seed `8953077177248245348`; `minecraft:normal`; structures enabled. |
| JVM flags | Complete: construction heap `-Xms1G -Xmx4G`; effective runtime/GC receipt retained. This is not a production allocation. |
| Hardware/OS | Complete for the execution host: PikaOS 4, Linux 7.1.0-pikaos, AMD Ryzen 7 7840HS, 8 cores/16 logical CPUs, 27,091,542,016 physical-RAM bytes, Btrfs on NVMe. |
| Player-count assumptions | Recorded planning input: 2–6 normal, 10 peak. Capacity is untested and must be measured later. |
| Hash/version baseline and untouched copy | Complete: 135-file full manifest, 131-file operational reconstruction manifest, full local archive hash, public state overlay, raw-evidence bundle, and restore proof. |
| EULA acceptance | Complete: `eula=true`, committed copy SHA-256 `ee27072e4a23e088522f740ddaab0c7c4145c186969e90a86254faa3a5ec5ce6`. |
| Fresh boot/restart/save/stop/archive/restore boot | Complete and observed. |

Exact platform identities:

| Component | Exact identity |
|---|---|
| Minecraft server | `server.jar`, 51,627,615 bytes; SHA-1 `59353fb40c36d304f2035d51e7d6e6baa98dc05c`; SHA-256 `e3bc55693e93cda0188f2e60aea28113fc647c5e85a15fa3d1b347349231b4bb`. |
| NeoForge installer | `21.1.249`; SHA-256 `d88b448eab73cd65bdf1720844a4828262de30a15fc71bd04dd81acc61c5399a`. |
| Temurin archive | `21.0.12.1+1`; SHA-256 `ce79869e1307ed8ee1e2baa86a412b1eb5b75d10a01006d788a6f968bcfaee94`. |
| Complete local frozen archive | 160,322,927 bytes; SHA-256 `4e4df44f0e0258f3814b5f20d22befd948dff58f21a5e2290ec087df53214c44`; intentionally not redistributed because it contains third-party binaries. |

Durable public release `item-2-evidence-assets-2026-09-01`:

- `pristine-baseline-v0-state.tar.gz`, 1,275,395 bytes, SHA-256 `d7880902d37011075a3548404ffe84f0073ef5da7788b6244a24204dd3531663`;
- `item2-raw-evidence-2026-09-01.tar.gz`, 389,164 bytes, SHA-256 `e97ffe0f036e66be301604de867154a1532f20a5b8cc896c4ed93330e5ae239d`.

Primary references: `docs/items/Item-2-Frozen-Technical-Baseline.md`, `evidence/item-2/`, `infrastructure/manifests/platform-1.21.1.json`, `infrastructure/bin/platform-1.21.1`.

### Item 3 — Perform the Exact Version and Dependency Audit

**Status:** `incomplete`

**Exit gate:** fail/not reached — no unsupported artifact is enabled in the zero-mod control, but the required candidate-by-candidate audit and evidence-supported retained/disabled dispositions do not yet exist.

| Specification subitem | Live status |
|---|---|
| Verify every candidate against Minecraft 1.21.1 | Incomplete. Exact upstream identity and declared metadata were captured; exact loader-semantics evaluation and focused runtime confirmation remain. |
| Verify every candidate against NeoForge 21.1.249 | Incomplete for the same reason. |
| Required dependencies and dependency versions | Incomplete. Parsed declarations exist; active dependency graph and exact Maven-range evaluation do not. |
| Optional integrations in use | Incomplete. |
| Forge JARs relied upon under NeoForge | Incomplete. Filename hazards and embedded NeoForge metadata are known, but all dispositions are not complete. |
| Fabric-derived components and Forgified Fabric API dependencies | Incomplete. Parsed metadata exists; active NeoForge versus inactive Fabric branches must be separated. |
| Overlapping embedded libraries | Inventory complete: 39 outer candidates contain 204 nested JARs. Same-bytes, same-version/different-bytes, multi-version, and mod-ID collision classifications remain incomplete. |
| Seven Seas exact 1.21.1 support | Incomplete. Static range contains 1.21.1; focused runtime disposition is missing. Do not silently replace or enable it. |
| AdoraBuild exact 1.21.1 support | Incomplete. Static range contains 1.21.1; focused runtime disposition is missing. Do not silently replace or enable it. |
| Broad `1.21.x` and other-point-release filenames | Incomplete as a complete set. Filenames are recorded hazards, not compatibility proof. |
| Server/client-only classifications | Incomplete. |
| Unnecessary client mods on dedicated server | Incomplete. |
| Missing server-side dependencies | Incomplete. |
| Resolve hard compatibility failures | Incomplete; no candidate has final enablement approval. |

Verified progress:

- 190 candidates resolved exactly: 176 Modrinth, 14 CurseForge;
- exact artifacts total 699,397,290 bytes;
- all 190 outer ZIPs pass integrity and path-safety checks;
- 188 outer archives classified as mods and 2 as libraries;
- 39 candidates contain 204 inspected nested JARs;
- 71 candidates expose a non-null manifest `Implementation-Version`;
- exact source-evidence release asset `item3-primary-source-raw-2026-09-01.tar.gz`: 20,124,166 bytes, 771 members, SHA-256 `f2bf2902ade83adb3c8e7aac9bb1527000a04833267325666a6e934984a9ef04`.

These observations prove identity and parseability only.

### Item 4 — Create the Controlled Test Environment

**Status:** `incomplete` and dependency-blocked by Item 3

**Exit gate:** not reached.

All current Item 4 acceptance subitems remain incomplete: separate test server, validated-baseline clone, untouched controls, world deletion/regeneration, configuration-version naming, experimental-branch naming, versioned configs/datapacks/spawn rules/loot tables, automated backup, real restore, and restored-world boot. Four seed identities survive in `test-environment/seed-suite.json` but are reconstructed inputs, not accepted snapshots or empirical closure:

- ordinary: `42`;
- mountainous: `6671238423019257953`;
- ocean-heavy: `95920844204830198`;
- biome-diverse: `-3503646078644842058`.

### Item 5 — Establish Measurement and Profiling Methodology

**Status:** `incomplete` and dependency-blocked by Items 3–4

**Exit gate:** not reached.

Reconstructed schemas and protocol prose exist, but no accepted implemented methodology exists. The receiving agent must implement and validate Spark setup; idle, combat, and fresh-worldgen MSPT; TPS; memory; GC; entities; pathfinding; chunk generation; structure count/distance; travel time; dungeon duration; death rate; loot value; structures/actionable locations/combat encounters/proper dungeons/major expeditions per 1,000 chunks; repetition; discoverability; Adventure Activity Ratio; exact warm-ups/windows/commands/units/formats/acceptance rules/artifact locations; and solo/2/4/normal/peak player cases.

### Item 6 — Audit Every Existing Relevant Configuration

**Status:** `incomplete` and dependency-blocked by Items 2–5

**Exit gate:** no explicit standalone gate in `SPECS.md`; downstream dependency is unsatisfied.

No current candidate stack has been retained, installed, and allowed to generate the authoritative configs. Therefore the receiving agent must audit only actual generated systems present after Item 3/4 closure. It must inspect Sparse Structures, Structure Essentials, ServerCore, C2ME, Chunky, Structure Layout Optimizer, WDA, YUNG, IDAS, Moog, village generation, Loot Integrations, spawning, and difficulty when present. Record absence instead of inventing a config. Record defaults, every non-default, global spacing, per-structure overrides, disabled sets, performance interactions, and hidden low-density causes. Do not tune during the audit.

### Item 7 — Audit Current Terrain and Worldgen Interactions

**Status:** `incomplete` and dependency-blocked by Item 6

**Exit gate:** no explicit standalone gate in `SPECS.md`; downstream dependency is unsatisfied.

Reconstructed reports are not acceptance evidence. Generate real worlds across all deterministic seeds and test the retained terrain, biome, structure, and dimension systems that actually survived Item 3. Inspect fragmentation, tiny biomes, transitions, buried/floating structures, cliffs, underwater failures, overlaps, village overlaps, failed placements, impossible restrictions, and excessive adaptation. Classify every finding as cosmetic, gameplay-affecting, performance-affecting, or generation failure. Preserve screenshot, coordinates, seed, dimension, configuration hash, logs, and reproduction steps.

### Item 8 — Inventory Every Structure Family

**Status:** `incomplete` and dependency-blocked by Items 6–7

**Exit gate:** no explicit standalone gate in `SPECS.md`; downstream dependency is unsatisfied.

Enumerate actual families from runtime registries, generated reports, datapacks, mod data, and verified runtime evidence. Cover the source families named in `SPECS.md` only when retained/present. For every family record namespace/ID, source, dimension, biome constraints, footprint, vertical size, intended hostility, mob source, loot source, generated spawners, authored versus natural enemies, discoverability, and underground/surface classification. Descriptions and filenames alone are insufficient.

### Item 9 — Classify the Existing Structure Stack

**Status:** `incomplete` and dependency-blocked by Item 8

**Exit gate:** no explicit standalone gate in `SPECS.md`; downstream dependency is unsatisfied.

Classify every verified family provisionally as Tier 0, Civilization, Tier 1, Tier 2, Tier 3, or Tier 4. Record evidence and confidence. Flag pseudo-dungeons, decorative structures, mechanically empty large structures, overlapping themes, and redundant villages, ruins, towers, and dungeon archetypes. Keep provisional classification visibly separate from final design decisions.

### Item 10 — Measure Baseline Structure and Encounter Density

**Status:** `incomplete` and dependency-blocked by Items 5–9

**Exit gate:** not reached. Historical final prose survives, but its raw generation worlds and validators were lost and cannot be accepted.

Generate representative regions across all selected seeds using a documented radius and checkpointed method. Validate complete `minecraft:full` chunk generation and Anvil slot/coordinate integrity before counting. Measure structures, actionable locations, combat encounters, proper dungeons, major expeditions, and villages per 1,000 chunks; nearest-neighbor distances; clustering; empty regions; biome variation; seed variation; and Sparse Structures contribution. Count gameplay value separately from raw frequency. Preserve raw data, intermediate checkpoints, logs, scripts, configuration hashes, world manifests/hashes, final reports, resume receipts, statistical limitations, and uncertainty. Incomplete or corrupt generation is invalid data.

## 6. Decisions Already Made

### Binding project/design decisions

- The pack is an engineering-driven multiplayer adventure sandbox.
- Engineering is the principal capability-progression system; exploration provides durable reasons to engineer; combat supplies expedition pressure.
- No magic or spell progression, mandatory skill trees, character-level progression, legendary-loot treadmill, uncontrolled stat inflation, or routine damage-sponge combat.
- Preserve player freedom, destructibility, emergent engineering, and sandbox solutions.
- Meaningful bypasses may exist when earned through preparation, investment, ingenuity, equipment, infrastructure, logistics, risk, or upkeep.
- Do not impose universal unbreakable blocks merely to protect authored routes.
- Basic Create, CC:Tweaked, transportation, trains, and Aeronautics must remain normally obtainable rather than rare dungeon-RNG gates.
- Cooperative PvE is primary; PvP is optional and consensual; unwanted griefing requires technical protection.
- The candidate inventory is tentative, not a mandatory final stack. Evidence may retain, replace, disable, or remove any candidate.
- Do not alter conclusions to preserve the tentative stack.
- Normal concurrency is 2–6 and understood peak is 10 as planning input; validate capacity empirically.
- A fresh v1 world is acceptable; the launched v1 world is persistent afterward with no scheduled resets.

### Execution and evidence decisions

- `SPECS.md` order is binding. Do not reorder, skip, compress, reinterpret, or prematurely complete items.
- Item 2 uses a zero-third-party-mod control. It is frozen and must not be mutated while auditing candidates.
- No candidate is enabled by default. Enable only after supported disposition evidence.
- Never substitute a version silently or accept `1.21.x`/another point-release filename without verification.
- Preserve exact source URLs, retrieval dates, upstream filenames, versions, sizes, and cryptographic hashes.
- If redistribution is not permitted, commit reproducible acquisition instructions and identities, not the binary.
- Ask only for a genuinely load-bearing decision. Record non-load-bearing unknowns and use the safest reversible provisional option.
- Maintain decision logs and explicitly distinguish fact, reconstruction, provisional conclusion, assumption, and missing evidence.
- A server launching proves only that it launched. It does not prove dependency health, client join, gameplay, worldgen, or performance.
- Small atomic commits, full diff inspection before each commit, descriptive local-style messages, immediate push, no unrelated changes, no history rewriting, clean checkpoints, and meaningful annotated tags are mandatory.
- Preserve superseded and failed evidence; mark it as superseded or invalid rather than deleting it.

### Item 3 static hazard facts, not final dispositions

- `DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar`: Modrinth version `erk04BGa`, 244,981 bytes, SHA-256 `549040fbd81d1b33aea38681109685e86d63985785246a831112c4ba5740d2df`; embedded NeoForge metadata declares Minecraft `[1.20,1.22)` and NeoForge `[21,)`.
- `adorabuild-structures-2.11.0-neoforge-1.21.3.jar`: Modrinth version `l7GS6bZj`, 657,734 bytes, SHA-256 `6f399680da36dbb95b9a0dbf8b600f173e650be4d6bc25f50fcac792dcce081e`; embedded NeoForge metadata declares Minecraft `[1.21,1.21.3]` and NeoForge `[21.0.0-beta,)`.
- `cc-tweaked-1.21.1-forge-1.116.1.jar` contains NeoForge metadata and declares NeoForge `[21.1.9,21.2)`.
- `sliceanddice-forge-4.2.4.jar` contains NeoForge metadata; declared requirements include Minecraft `[1.21.1,)`, NeoForge `[21,)`, Kotlin for Forge `[5.8,)`, and Create `[6.0.9,7.0.0)`.
- `modelfix` is client-side and has an orphan/malformed dotted dependency owner `1.21-1.10`; do not repair or reinterpret upstream metadata silently.
- `kotlinforforge-5.11.0-all.jar` is an outer FML library whose nested metadata supplies mod ID `kotlinforforge`.
- Forgified Fabric API supplies top-level and nested IDs. Do not apply its inactive Fabric metadata branch as a NeoForge hard dependency without proving loader behavior.

## 7. Primary Loader-Semantics Research Preserved at the Stop Boundary

The following was verified from exact primary source during the interrupted Item 3 analysis but has not yet been converted into the planned machine-readable `evidence/item-3/loader-semantics-sources.json`. Treat it as preserved research input that must be rechecked once, cited into evidence, and covered by tests before use in final dispositions; do not repeat broad discovery from scratch.

- Frozen server FML loader: `loader-4.0.44.jar`, SHA-256 `f2096cd86d605c0484971fc712208e0dc6cecfe53e056db61d44a98cadc19499`.
- Loader manifest `Git-Commit`: `96010059`; exact source commit: `96010059ad23bfcef8be966c1a675a3abe4c8867`.
- Frozen Maven Artifact runtime: 3.8.5, SHA-256 `91172bc294d6eab02fc9f45f4ea01fd0e418962d128cf489abea7b6957d988ee`.
- Frozen Commons Lang runtime on NeoForge legacy classpath: 3.14.0, SHA-256 `7b96bf3ee68949abb5bc465559ac270e0551596fa34523fddf890ec418dde13c`.
- `MavenVersionAdapter` directly calls `VersionRange.createFromVersionSpec`.
- `JarModsDotTomlModFileReader` discovers `META-INF/neoforge.mods.toml`. All 19 candidates observed with legacy `mods.toml` also have NeoForge metadata; none currently relies solely on legacy metadata.
- `ModInfo` attaches dependency tables only for a declared owning mod ID.
- `ModSorter` filters by physical side; required missing or wrong-range dependencies fail; optional absent dependencies are allowed, while installed optional dependencies with an incompatible version fail; present-and-matching incompatible dependencies fail; discouraged matches warn.
- `VersionSupportMatrix` for Minecraft 1.21.1 may permit fallback coordinates Minecraft `1.21` and NeoForge `21.0.166` if the direct target check fails. Implement from exact source, do not approximate.
- Built-in language provider version comes from the FML JAR implementation version, observed as `4.0`.
- Jar-in-Jar behavior is a version negotiation/selection system, not merely an embedded-file inventory.

Exact primary source commit: <https://github.com/neoforged/FancyModLoader/commit/96010059ad23bfcef8be966c1a675a3abe4c8867>

| Source file | SHA-256 of retrieved source |
|---|---|
| `MavenVersionAdapter.java` | `365131c98b70edee0e7b6dc2377c40e6ea56eff4d8127c842eeb687212f60c71` |
| `ModInfo.java` | `3b7af699f333f30ab5b24b7fb0316744365c4dff60e3d93036982c0867443585` |
| `ModSorter.java` | `a1aedb70f632305a9f360e1adb072aa818600df8442a327dba9ecc2785b12927` |
| `VersionSupportMatrix.java` | `a39dcd636dde637729376078fe156334c9424d38882c389defd633f65a1aaaf9` |
| `JarModsDotTomlModFileReader.java` | `34a924221e7158bbc3a8fdd9e204ec1d09a2996e7063bd8dd454a22633479016` |
| `BuiltInLanguageLoader.java` | `04b2e205ff98108c1d78bfea6b5c626d082c1d2426e084a4bcf4b98edf31aa17` |

Official supporting documentation retrieved 2026-09-01:

- <https://docs.neoforged.net/docs/1.21.1/gettingstarted/modfiles/>
- <https://docs.neoforged.net/toolchain/docs/dependencies/jarinjar/>
- <https://maven.apache.org/ref/3.9.16/maven-artifact/apidocs/org/apache/maven/artifact/versioning/VersionRange.html> — current documentation reference; runtime behavior must use frozen Maven Artifact 3.8.5.
- <https://docs.fabricmc.net/develop/loader/fabric-mod-json>

## 8. Work Already Completed and Relevant Files

| Commit | Files/area | Why it exists |
|---|---|---|
| `57f883b` | `INFRASTRUCTURE-INSTALLATION-AND-SERVER-TESTING.md` | Complete supplementary execution requirements supplied by the user. |
| `884beec` | `pyproject.toml`, `uv.lock`, Item 2 Python evidence model/tests | Strict typed evidence validation foundation. |
| `7afacb4` | `infrastructure/bin/*`, platform manifest, shell tests | Exact host discovery and pinned platform acquisition/provisioning. |
| `40ebd9a` | Item 2 report, configs, manifests, execution/raw receipts | Primary frozen-baseline evidence. |
| `5fce47f` | Item 2 closeout, durable-storage/Git receipts, ledger update | Passed reconstructability and durability gate. |
| `3da9f40` | Item 3 models, collectors, file map/overrides, tests | Candidate source-audit foundation. |
| `ca807f9` | source identity matrix, raw manifest, durability receipt, tests/tools | Exact primary identity for all 190 candidates. |
| `4c40642` | Item 3 source durability receipt | Fresh remote asset verification. |
| `ac3b9f5` | artifact acquisition model/tool/manifest/tests | Exact candidate download and hash/size verification. |
| `e217570` | JAR parser/models/tool/tests and inspection JSON | Top-level metadata and archive inspection. |
| `3d1f335` | nested-JAR parser/evidence/tests | Embedded library/mod metadata inspection. |
| `22eef44` | `MCPACK-NEW-SESSION-HANDOFF.md` | Durable Item 3 partial-work stop checkpoint. |
| `4cf150d` | manifest version capture in Item 3 parser/evidence/tests | Resolve `${file.jarVersion}` metadata input for nine declarations; 71 non-null versions recorded overall. |
| `50a8d74` | `tools/MavenVersionRangeProbe.java` | Exact Maven 3.8.5 range-semantics probe, compiled and manually exercised with the frozen loader classpath. |

Important path map:

| Path | Role |
|---|---|
| `candidate-mods/current-jars-2026-09-01.txt` | Exact tentative candidate filenames; not an enablement manifest. |
| `candidate-mods/item3-curseforge-file-map.json` | Exact CurseForge file mapping. |
| `candidate-mods/item3-search-query-overrides.json` | Deterministic Modrinth search overrides. |
| `evidence/item-2/` | Accepted machine-readable Item 2 evidence. |
| `evidence/item-3/source-identity-matrix.json` | Exact 190-candidate source identities. |
| `evidence/item-3/raw-source-manifest.json` | Manifest for 767 retained primary-response files. |
| `evidence/item-3/source-evidence-durability.json` | Remote source-bundle retrieval and integrity receipt. |
| `evidence/item-3/artifact-acquisition-manifest.json` | Exact acquisition identities and hashes. |
| `evidence/item-3/jar-inspection.json` | Parsed outer/nested metadata and archive evidence. |
| `src/mcpack_evidence/item3*.py` | Typed Item 3 evidence and parsing implementation. |
| `tests/item3/` | Current Item 3 regression tests. |
| `tools/collect_candidate_*.py` | Primary-source collectors. |
| `tools/build_candidate_source_matrix.py` | Source identity matrix builder. |
| `tools/acquire_candidate_artifacts.py` | Exact artifact acquisition. |
| `tools/inspect_candidate_jars.py` | Top-level and nested inspection. |
| `tools/MavenVersionRangeProbe.java` | Frozen-runtime range oracle. |
| `test-environment/seed-suite.json` | Reconstructed deterministic seed identities; not accepted Item 4 closure. |
| `docs/items/Item-4*` through `Item-10*` | Reconstructed reports/protocols; rerun guidance only. |
| `evidence/reconstruction/` | Explicitly non-authoritative historical summaries and recovery markers. |
| `measurement/` and legacy analysis tools | Reconstructed methodology/tools requiring validation before use. |

## 9. Git and Durability State

At handoff preparation:

- branch `main` tracked `origin/main`;
- pre-handoff source checkpoint was pushed at full SHA `50a8d74b6627246059e714df55461e7206135819`;
- the Cloud handoff commit is identified by annotated tag `cloud-handoff-item3-2026-09-01`;
- no history was rewritten;
- two local, untracked user artifacts were deliberately untouched: `.codegraph` and `mcpack-reconstructed-28(1).bundle`;
- those untracked artifacts will not exist in a normal Cloud checkout and are not required to resume accepted work;
- ignored local runtime caches (`downloads/`, `instances/`, `evidence/raw/`) are not in Git and must not be assumed present in Cloud.

Important milestone tags:

| Tag | Meaning |
|---|---|
| `item-2-evidence-assets-2026-09-01` | Item 2 evidence asset publication checkpoint. |
| `item-2-baseline-recovery-2026-09-01` | Item 2 reconstructability closeout. |
| `item-3-primary-source-evidence-2026-09-01` | Item 3 exact source identity and raw-source durability checkpoint. |
| `item-3-jar-inspection-checkpoint-2026-09-01` | Partial Item 3 JAR inspection handoff; not completion. |
| `cloud-handoff-item3-2026-09-01` | This Cloud continuation handoff. |

After every receiving-agent commit:

```bash
git diff --check
git diff --staged --stat
git diff --staged
git commit -m '<descriptive repository-style message>'
git push origin main
git fetch origin main --tags
test "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)"
git status --short --branch
```

Stage exact paths or hunks. Do not stage `.codegraph`, recovery bundles, runtime caches, secrets, unrelated edits, or generated third-party binaries. Do not amend, rebase, force-push, or otherwise rewrite published history.

## 10. Tests and Checks Already Run

Current validation was rerun during handoff preparation against pre-handoff source checkpoint `50a8d74b6627246059e714df55461e7206135819` plus the uncommitted handoff document:

- `uv run pytest -q` — 28 passed;
- scoped Ruff lint for `src`, `tests`, and current Item 3 tools — pass;
- matching Ruff format check — pass;
- `uv run basedpyright src tests` — 0 errors;
- `bash tests/infrastructure/test_platform_provisioning.sh` — exit 0;
- `bash tests/infrastructure/test_host_discovery.sh` — exit 0 and authoritative Mojang endpoint probe passed;
- critical local path/reference check for this handoff — pass;
- fresh retrieval of the six exact FML source files at commit `96010059ad23bfcef8be966c1a675a3abe4c8867` — all SHA-256 values matched section 7;
- `git diff --check` — pass.

The Java probe at `50a8d74b6627246059e714df55461e7206135819` was manually validated with the frozen runtime:

- Temurin reported `21.0.12.1+1-LTS`;
- `javac` compilation passed using Maven Artifact 3.8.5 plus Commons Lang 3.14.0;
- exact cases passed: closed range inclusion, exclusive-upper failure, open-ended NeoForge inclusion, recommended singleton range inclusion, and invalid range rejection;
- no build output was retained in Git.

Known pre-existing validation limitation: a full Ruff run over all reconstructed later-item tools reports 15 findings. Those findings predate the accepted Item 3 work and were deliberately not mixed into Item 3 commits. Re-run scoped checks for changed files and report the broader findings separately unless a later owning item authorizes fixing them. `src/mcpack_evidence/item3_jar.py` was 217 pure lines at the last check; split manifest parsing before adding enough behavior to exceed the project’s 250-line ceiling.

Java LSP (`jdtls`) was not installed. No global tooling was modified. Exact `javac`/runtime execution is the current authoritative validation for the 42-line probe.

## 11. Known Problems, Blockers, and Uncertainties

### Current dependency blocker

Items 4–10 are blocked by incomplete Item 3, not by a missing user decision. The next agent can safely continue Item 3 without asking the user if its launching prompt authorizes resumption.

### Missing Item 3 evidence

- machine-readable loader-semantics source receipt;
- exact dependency and conflict evaluator with failing-first tests;
- provided mod-ID/version map including nested IDs and manifest substitution;
- correct physical-side evaluation;
- FML support-matrix fallback evaluation;
- language-loader range evaluation against built-in loader version 4.0;
- orphan dependency-owner report;
- embedded overlap and nested mod-ID collision report;
- final 190-row machine-readable compatibility matrix;
- explicit server/client/shared/disabled/quarantined/unresolved disposition for every candidate;
- focused isolated runtime boots for evidence-supported retained clusters and named hazards;
- human-readable audit, decision log, limitations, reproduction record, and exit-gate assessment.

### Infrastructure and environment uncertainties

- Final production host, heap, storage budget, backup policy, and performance budgets are unresolved; do not block Item 3 on them.
- Player counts are planning inputs, not capacity proof.
- Final client/server distribution formats and redistribution eligibility remain unresolved per artifact.
- Item 10 can require substantial CPU, RAM, disk, and time. Verify Cloud quotas and checkpoint durability before a large generation campaign.
- Cloud checkouts will not contain the 699 MB candidate cache or local Item 2 instance. Reacquire exact artifacts and/or reconstruct from durable assets.
- A GitHub-connected Cloud task may return commits/diffs without granting arbitrary `gh` or push credentials. Verify repository write/tag/release authority before promising pushes or release uploads.
- Client visual inspection and later real-player measurements may require a local graphical client or human operators not available in Cloud. Document the boundary; do not fabricate observations.

## 12. Codex Cloud Environment Requirements

Official Codex Cloud behavior matters here:

- A Cloud task creates an isolated container, checks out the selected branch/commit, runs setup, then runs the agent. See [Codex cloud](https://learn.chatgpt.com/docs/cloud).
- Environment setup can install dependencies and has internet access; agent-phase internet is off by default unless enabled. Setup-shell exports do not persist automatically; configure environment variables in the environment settings or a persistent shell file. Secrets are available only to setup and are removed before the agent phase. See [Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environment).

This project requires one of these two arrangements:

1. **Preferred:** enable agent-phase internet with an allowlist sufficient for primary-source verification and exact downloads from Mojang, NeoForged Maven/GitHub, Adoptium, Modrinth, CurseForge, GitHub releases, Maven, and Fabric/NeoForge documentation; or
2. pre-acquire all exact inputs during setup into durable/cache paths, preserve their hashes and source receipts, and ensure the agent can read them without secrets.

Recommended setup prerequisites:

- Git and Git LFS if the environment uses it;
- Python 3.13 and `uv`;
- `bash`, `curl`, `jq`, `rg`, `tar`, `gzip`, `unzip`, `zip`, `sha1sum`, and `sha256sum`;
- enough disk for at least the 699,397,290-byte candidate set, exact Java/NeoForge/Minecraft artifacts, test instances, evidence, backups, and later world-generation checkpoints;
- GitHub repository permissions for pushes/tags and a separately authorized path for release assets, or an explicit limitation report.

Do not rely on `/home/lonestar/...` local paths in Cloud. All commands below use repository-relative paths and explicit temporary/output roots.

## 13. Install, Build, Reproduce, Run, and Test Commands

### Checkout and integrity

```bash
git fetch origin main --tags
git switch main
git pull --ff-only origin main
test "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)"
git log -15 --oneline --decorate
git tag --list --sort=creatordate
git status --short --branch
```

### Python development environment

```bash
uv sync --dev
uv run pytest -q
uv run basedpyright src tests
```

Use scoped Ruff commands for active Item 3 work:

```bash
uv run ruff check \
  src tests \
  tools/build_candidate_source_matrix.py \
  tools/build_raw_evidence_manifest.py \
  tools/collect_candidate_curseforge.py \
  tools/collect_candidate_modrinth.py \
  tools/acquire_candidate_artifacts.py \
  tools/inspect_candidate_jars.py
uv run ruff format --check \
  src tests \
  tools/build_candidate_source_matrix.py \
  tools/build_raw_evidence_manifest.py \
  tools/collect_candidate_curseforge.py \
  tools/collect_candidate_modrinth.py \
  tools/acquire_candidate_artifacts.py \
  tools/inspect_candidate_jars.py
```

### Item 2 platform reconstruction

All targets must be explicit and absent or empty:

```bash
infrastructure/bin/platform-1.21.1 inspect --root .
infrastructure/bin/platform-1.21.1 acquire --root . --cache downloads/item2/cache
infrastructure/bin/platform-1.21.1 verify-cache --root . --cache downloads/item2/cache --require-complete
infrastructure/bin/platform-1.21.1 provision-java \
  --root . \
  --cache downloads/item2/cache \
  --java-home downloads/item2/temurin
infrastructure/bin/platform-1.21.1 materialize-pristine \
  --root . \
  --cache downloads/item2/cache \
  --java-home downloads/item2/temurin \
  --target instances/cloud-pristine-baseline-v0 \
  --installer-log evidence/raw/item2/cloud-installer.log \
  --state-overlay downloads/item2/pristine-baseline-v0-state.tar.gz
infrastructure/bin/platform-1.21.1 verify-instance \
  --root . \
  --target instances/cloud-pristine-baseline-v0 \
  --reconstruction-manifest evidence/item-2/reconstruction-manifest.json
```

The public state overlay must first be downloaded from the exact URL and verified against `evidence/item-2/durable-storage-receipt.json`. Do not use a different asset with a similar name.

From the materialized target, start the server only with the pinned project-local Java:

```bash
../../downloads/item2/temurin/bin/java \
  @user_jvm_args.txt \
  @libraries/net/neoforged/neoforge/21.1.249/unix_args.txt \
  nogui
```

Wait for the exact readiness event, then issue `seed`, `save-all flush`, and `stop`. Preserve logs. A launch alone is not a gate.

Infrastructure tests:

```bash
bash tests/infrastructure/test_host_discovery.sh
bash tests/infrastructure/test_platform_provisioning.sh
```

### Item 3 exact source and artifact reproduction

The committed outputs already exist; only regenerate when validating provenance or when the ignored cache is absent:

```bash
uv run python tools/collect_candidate_modrinth.py \
  --inventory candidate-mods/current-jars-2026-09-01.txt \
  --query-overrides candidate-mods/item3-search-query-overrides.json \
  --raw-dir evidence/raw/item3/modrinth \
  --output evidence/raw/item3/modrinth-resolutions.json
uv run python tools/collect_candidate_curseforge.py \
  --file-map candidate-mods/item3-curseforge-file-map.json \
  --raw-dir evidence/raw/item3/curseforge \
  --output evidence/raw/item3/curseforge-resolutions.json
uv run python tools/build_candidate_source_matrix.py \
  --inventory candidate-mods/current-jars-2026-09-01.txt \
  --modrinth evidence/raw/item3/modrinth-resolutions.json \
  --curseforge evidence/raw/item3/curseforge-resolutions.json \
  --output evidence/item-3/source-identity-matrix.json
uv run python tools/acquire_candidate_artifacts.py \
  --source-matrix evidence/item-3/source-identity-matrix.json \
  --download-root downloads/item3/candidates \
  --output evidence/item-3/artifact-acquisition-manifest.json \
  --workers 8
uv run python tools/inspect_candidate_jars.py \
  --acquisition-manifest evidence/item-3/artifact-acquisition-manifest.json \
  --output evidence/item-3/jar-inspection.json \
  --workers 8
```

Do not overwrite committed evidence casually. Generate to temporary comparison paths first, diff normalized results, explain timestamp-only changes, and preserve a receipt before replacing accepted evidence.

### Exact Maven range probe

After reconstructing Item 2, compile into a temporary directory with the exact frozen libraries:

```bash
probe_build=$(mktemp -d)
java_home=downloads/item2/temurin
maven_jar=instances/cloud-pristine-baseline-v0/libraries/org/apache/maven/maven-artifact/3.8.5/maven-artifact-3.8.5.jar
lang_jar=instances/cloud-pristine-baseline-v0/libraries/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.jar
"$java_home/bin/javac" -cp "$maven_jar:$lang_jar" -d "$probe_build" tools/MavenVersionRangeProbe.java
printf '%s\n' \
  $'closed_pass\t1.21.1\t[1.21,1.21.3]' \
  $'upper_fail\t1.21.3\t[1.20,1.21.3)' \
  $'open_pass\t21.1.249\t[21,)' \
  $'recommended_pass\t1.21.1\t[1.21.1]' \
  $'invalid_range\t1.21.1\t[broken' \
  | "$java_home/bin/java" -cp "$probe_build:$maven_jar:$lang_jar" MavenVersionRangeProbe
```

Expected statuses in order: `pass`, `fail`, `pass`, `pass`, `invalid`. Remove only the explicit temporary build directory after inspection.

## 14. Exact Next Actions After Explicit Resume Authorization

Execute these in order. Do not jump to Item 4.

1. Read all governing files in section 2 and verify `HEAD` resolves to the Cloud handoff tag with a clean tracked tree.
2. Verify or reconstruct the exact Item 2 platform locally without mutating the frozen control. Reacquire all 190 candidate bytes into ignored storage if absent; verify the committed acquisition manifest before analysis.
3. Recheck the exact FML commit and source-file hashes in section 7. Commit `evidence/item-3/loader-semantics-sources.json` with retrieval date, URLs, exact commit, artifact versions/hashes, conclusions, and limitations. Inspect the full diff, run relevant validation, push immediately.
4. Add failing-first tests for an Item 3 compatibility evaluator. Keep active NeoForge metadata separate from inactive Fabric metadata.
5. Implement provided mod-ID/version mapping including nested mod IDs and `${file.jarVersion}` substitution. Split code before exceeding the 250-line file ceiling.
6. Evaluate direct Minecraft 1.21.1 and NeoForge 21.1.249 ranges plus the exact FML support-matrix fallbacks. Evaluate built-in language-loader ranges against version 4.0 using the exact Maven 3.8.5 oracle.
7. Apply FML semantics for physical side and required, optional, incompatible, and discouraged dependencies. Detect orphan dependency owners such as `modelfix`.
8. Build the embedded overlap report: identical bytes, same version/different bytes, multiple versions, negotiated selection, and nested mod-ID collisions.
9. Emit a final 190-row machine-readable compatibility matrix. Every row needs exact identity, target/loader evidence, dependency closure, side, conflicts, optional integrations, overlap findings, hazard flags, disposition, rationale, confidence, and missing runtime evidence. Default to disabled/quarantined/unresolved until support is proven.
10. Perform focused isolated dedicated-server boots for only evidence-supported retained clusters and named hazards. Keep untouched controls; retain full logs, commands, configs, hashes, readiness/stop evidence, and failure dispositions. A successful launch is necessary but insufficient.
11. Write the human-readable Item 3 audit, decision log, limitations, reproduction instructions, execution record, and exit-gate assessment. Resolve every `SPECS.md` Item 3 subitem explicitly.
12. Run current tests/type/lint/format checks, inspect the complete diff, commit small logical groups, push each immediately, verify remote parity, and create an annotated Item 3 completion/recovery tag only when the gate genuinely passes.
13. Only then begin Item 4. Proceed Items 4, 5, 6, 7, 8, 9, and 10 in their exact dependency order as specified in section 5 and `SPECS.md`.
14. After Item 10, perform cross-item evidence/exit-gate review. Item 11 is authorized only if every applicable Item 2–10 subitem and gate passes with reproducible evidence.

## 15. Prohibited Shortcuts

- Do not resume from Item 4, Item 10, or Item 11 while Item 3 is incomplete.
- Do not treat reconstructed Item 4–10 reports as current empirical proof.
- Do not install all 190 candidates together as a first compatibility test.
- Do not infer compatibility from filenames, project descriptions, broad version labels, or a metadata range alone.
- Do not silently substitute artifacts or versions.
- Do not leave any candidate enabled under an unverified assumption.
- Do not tune configurations during Item 6.
- Do not count corrupt, incomplete, or unvalidated chunks in Item 10.
- Do not invent absent configs, runtime observations, screenshots, coordinates, player data, or performance results.
- Do not delete failed or superseded evidence.
- Do not put secrets, credentials, addresses, allowlists, player UUIDs, or redistribution-restricted binaries into Git.
- Do not leave important work only in `/tmp`, a Cloud workspace, ignored storage, or an unpushed commit.

## 16. Handoff Acceptance Check

A receiving agent has successfully ingested this handoff when it can state, before editing:

1. Item 2 is complete and why;
2. Item 3 is the sole active project item and exactly which evidence is complete versus missing;
3. Items 4–10 remain unaccepted despite reconstructed documents;
4. the exact pre-handoff checkpoint and Cloud handoff tag;
5. where large evidence lives and how to verify/reacquire it;
6. the binding design and Git/durability constraints;
7. the first atomic deliverable: machine-readable exact loader-semantics source evidence;
8. that Item 11 is not authorized.

If any of those answers is unclear, stop and reread the governing files rather than reconstructing intent from memory.
