# Candidate Identity & Compatibility Audit — v0.3

**Audit date:** 2026-09-01
**Target:** Minecraft Java 1.21.1, NeoForge 21.1.249, Java 21
**Input:** 190 user-supplied candidate filenames
**Scope:** artifact identity, declared game/loader compatibility, release-channel state, declared dependency closure, and environment-side classification

This is a candidate audit, not proof that the full stack is safe. No 190-mod instance previously existed. Runtime compatibility, gameplay fit, worldgen interaction, configuration behavior, and performance still require controlled construction and tests.

## Result

| Measure | Result |
|---|---:|
| Candidate filenames | 190 |
| Proposed enabled | 188 |
| Proposed disabled | 2 |
| Exact identities on Modrinth | 176 |
| Exact identities on official CurseForge pages | 14 |
| Unresolved identities | 0 |
| Exact Modrinth candidates with a newer compatible build | 70 |
| Exact Modrinth candidates with a newer compatible release | 62 |
| Exact Modrinth candidates currently using alpha/beta metadata | 22 |
| Additional CurseForge beta candidates | 1 (`Framework`) |
| Declared dependency edges in the exact Modrinth set | 200 |
| Declared required dependency edges | 116 |
| Required edges not represented by the supplied candidates | 5 |
| Distinct missing required projects | 2 |
| Modrinth projects that require a client and do not require server installation | 28 |

All 190 filenames now have an exact upstream identity. Identity means the upstream record contains the exact filename; it does not mean the candidate is selected for Baseline v0.

## Method and acceptance rule

1. Search results were used only to find candidate projects.
2. A Modrinth identity was accepted only when the project version API contained the exact proposed filename.
3. Search-ranking failures were corrected with stable project IDs and re-run against the same exact-filename rule.
4. CurseForge-only identities were accepted only from official file pages/listings naming the exact filename and declaring Minecraft 1.21.1 plus NeoForge compatibility.
5. Compatible-update checks required Minecraft 1.21.1 and an intersection with the candidate version's loader tags.
6. Newer versions are review triggers, not automatic replacements.
7. Dependency closure in this report uses publisher metadata only. Embedded JAR metadata and actual NeoForge resolution remain separate gates.

## Load-bearing findings

### The supplied versions are not suitable as an immutable baseline

Sixty-two of the 176 Modrinth-resolved candidates already have a newer compatible release. The proposal also includes at least 23 alpha/beta candidates when the CurseForge-only Framework beta is counted. Admitting the list verbatim would knowingly freeze stale and pre-release artifacts without a rationale.

Each selected mod will therefore receive one of four explicit version dispositions:

- retain exact proposed build;
- update to a named compatible build;
- hold at an older build because of a documented integration constraint;
- reject the mod.

### The proposal is not dependency-closed

The declared Modrinth dependency graph contains five missing required edges:

| Requesting candidates | Missing project | Disposition |
|---|---|---|
| Archers, Rogues, Armory, Arsenal | Spell Engine | Reject these four candidates provisionally. They pull the pack toward the spell-combat ecosystem explicitly excluded by the design contract. Reconsider only if a non-spell configuration is proven both technically and aesthetically necessary. |
| LambDynamicLights | Fabric API | Do not treat the metadata edge as satisfied by assumption. The NeoForge build must be tested against Forgified Fabric API or replaced/removed on the client branch. |

The Spell Engine result is both a hard dependency defect in the proposal and a design-fit warning. Adding the missing spell framework merely to make the proposed list launch would violate the project contract.

### Dedicated-server separation is mandatory

Publisher environment metadata identifies 21 exact candidates as client-required/server-unsupported and another seven as client-required/server-optional. At minimum, the dedicated server must exclude the unsupported group. Optional-side libraries will be retained server-side only when a selected server mod actually requires them.

Confirmed client-required/server-unsupported candidates include AmbientSounds, Better Advancements, EMI add-ons, Entity Culling, ImmediatelyFast, Iris, Iris/Flywheel Compat, Just Zoom, LambDynamicLights, Model Gap Fix, Mouse Tweaks, Not Enough Animations, Overflowing Bars, Reese's Sodium Options, Simply Tooltips, and Sodium. The full machine-readable classification is retained in the evidence directory.

### Forge-labelled filenames are not automatically Forge artifacts

The exact upstream records declare the proposed CC:Tweaked, Player Animator, and Simply More files as NeoForge builds despite `forge` appearing in their filenames. CurseForge declares `sliceanddice-forge-4.2.4.jar` as a NeoForge release. They remain subject to embedded-metadata and runtime testing, but the filename alone is not a loader failure.

## Explicit point-release investigations

### AdoraBuild `2.11.0-neoforge-1.21.3`

- Exact upstream identity found.
- Modrinth declares Minecraft 1.21.1 and NeoForge.
- Publisher SHA-512 verified after acquisition.
- Embedded `neoforge.mods.toml` declares Minecraft range `[1.21, 1.21.3]`, which includes 1.21.1 and excludes 1.21.3 under interval semantics.
- Embedded `pack.mcmeta` uses pack format 48.

**Disposition:** no longer rejected solely because of its misleading filename, but still quarantined until a full 1.21.1 world boot and structure-generation test. Its data/resources may have been authored with later-format assumptions even though loader metadata permits 1.21.1.

### When Dungeons Arise: Seven Seas `1.21.x-1.0.4`

- Exact upstream identity found.
- Modrinth explicitly tags 1.21.1 and NeoForge.
- Publisher SHA-512 verified after acquisition.
- Embedded metadata declares Minecraft `[1.20, 1.22)` and server-side NeoForge `[21,)`.

**Disposition:** passes the declared-version gate for 1.21.1. Generation quality, density, overlap, loot, and performance remain unproven.

## Version decisions already made for the anchor branch

| Capability | Proposed | Selected test build | Reason |
|---|---|---|---|
| Create | 6.0.10 | 6.0.10 | Aeronautics/Sable compatibility anchor. |
| Create Aeronautics | 1.3.0 | 1.3.2 | Newer compatible maintenance release. |
| CC:Tweaked | 1.119.0 | 1.120.2 | Newer official 1.21.1 artifact; verified against official Maven bits. |
| Sable | 2.0.1 | 2.0.5 | Newer stable compatible release. |

NeoForge discovered the four direct JARs and fifteen embedded dependencies and resolved their declared dependencies through the EULA gate. This proves discovery and declared dependency resolution only.

## Significant compatible-release review queue

The complete 62-entry queue is machine-readable. High-impact review items include:

| Candidate area | Proposed | Newer compatible release |
|---|---|---|
| Create Big Cannons | 5.11.6 | 5.11.7 |
| Create Enchantment Industry | 2.4.0 | 2.4.2 |
| Create Dragons Plus | 1.11.2b | 1.11.7b |
| Better Combat | 2.3.2 | 2.4.0 |
| Simply Swords | 1.63.0 | 1.70.2 |
| Farmer's Delight | 1.3.2 | 1.3.4 |
| ModernFix | 5.27.12 | 5.27.24 |
| Sodium | 0.8.12 beta | 0.8.13 release |
| YUNG's API | 5.1.6 | 5.1.8 |
| Moog's Structure Library | 3.0.0 alpha | 3.1.2 release |
| Moog's Nether Structures | 3.0.0 alpha.2 | 3.0.0 release |
| Moog's Voyager Structures | 5.0.11 | 5.0.14 |
| Slice & Dice | 4.2.4 | 4.3.3 |
| Structure Essentials | 5.0 | 5.0 (current for 1.21.1) |

## Evidence artifacts

- `evidence/candidate-audit/modrinth-exact-match-final.json` — exact identities and publisher hashes/URLs.
- `evidence/candidate-audit/modrinth-compatible-version-status-final.json` — compatible-version comparison.
- `evidence/candidate-audit/modrinth-dependency-closure.json` — dependency edges and environment classification.
- `evidence/candidate-audit/curseforge-exact-identities.json` — exact CurseForge-only identities and file IDs.
- `artifacts/candidates/version-investigation/` — publisher-hash-verified AdoraBuild and Seven Seas investigation JARs.

## Gate status

| Gate | Status |
|---|---|
| Exact identity for all 190 proposed filenames | `COMPLETE` |
| Declared 1.21.1/loader audit | `COMPLETE` for candidate metadata |
| Compatible-update discovery | `COMPLETE` for Modrinth; targeted CurseForge review recorded |
| Declared Modrinth dependency closure | `COMPLETE`, with two missing projects identified |
| Dedicated-server side classification | `IN PROGRESS`; exact Modrinth group complete, CurseForge/JAR confirmation pending |
| Embedded metadata for all admitted artifacts | `IN PROGRESS`; performed for anchors and explicit point-release investigations |
| Runtime compatibility of admitted Baseline v0 | `BLOCKED` at the EULA-authorized world-boot gate |
| Gameplay, worldgen, and performance compatibility | `UNSTARTED`; requires the constructed controlled baseline |

No candidate is accepted merely because this report resolves its identity or because a server reaches the EULA gate.

