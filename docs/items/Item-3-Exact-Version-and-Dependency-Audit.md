# Item 3 — Exact Version and Dependency Audit

## Status and gate

**Status: complete for dedicated-server admission.** The audit covers all 190 supplied candidates exactly once. The retained dedicated-server set contains 136 candidates; 54 are explicitly disabled or quarantined. No unresolved disposition and no statically unsupported artifact remains enabled. The retained set passed a first boot, readiness observation, `save-all flush`, clean stop, existing-world restart, second readiness observation, second flush, and second clean stop on Minecraft 1.21.1, NeoForge 21.1.249, and Temurin 21.0.12.1+1.

This gate establishes loader, dependency, physical-side, and dedicated-server lifecycle compatibility. It does not establish client join, gameplay correctness, configuration quality, world-generation correctness, or acceptable performance. Those claims belong to later dependency-ordered items.

## Reproduction inputs

- Exact source identity: `evidence/item-3/source-identity-matrix.json`.
- Verified acquisition identity: `evidence/item-3/artifact-acquisition-manifest.json`.
- Active and nested metadata: `evidence/item-3/jar-inspection.json`.
- Loader semantics: `evidence/item-3/loader-semantics-sources.json`.
- Exact Maven requests/results: `evidence/item-3/maven-range-requests.tsv` and `evidence/item-3/maven-range-results.tsv`.
- Full-inventory static evaluation: `evidence/item-3/static-compatibility-exact.json`.
- Retained-provider static evaluation: `evidence/item-3/retained-compatibility-exact.json`.
- Embedded overlap analysis: `evidence/item-3/embedded-overlap-report.json`.
- Final 190-row decision surface: `evidence/item-3/final-compatibility-matrix.json`.
- Runtime commands, manifests, outcomes, and hashed logs: `evidence/item-3/runtime/runtime-cluster-evidence.json`.

The range oracle was compiled with the pinned Temurin runtime against Maven Artifact 3.8.5 and Commons Lang 3.14.0. All artifact hashes match the loader-semantics receipt. The 330 unique range requests contain no invalid result.

## Candidate dispositions

| Disposition | Count | Meaning |
|---|---:|---|
| Retained on dedicated server | 136 | Static checks pass, publisher server metadata does not reject the artifact, dependency closure is present, and the final cluster passed boot and restart lifecycle checks. |
| Disabled, not required on server | 23 | Server-optional or unknown candidate was unnecessary for retained dependency closure. |
| Disabled, client-only | 21 | Exact publisher metadata marks server use unsupported. |
| Quarantined, static failure | 4 | Archers, Armory, Arsenal, and Rogues require absent `spell_engine`; the rejected magic-progression family is not silently repaired. |
| Disabled, runtime failure | 3 | Sable, bundled Aeronautics, and Every Compat failed controlled server admission criteria. |
| Disabled inventory state | 2 | Supplied disabled artifacts remain disabled. |
| Quarantined dependency closure | 1 | Simply More requires server-unsupported Simply Tooltips. |

Every row includes exact publisher and artifact identity, declared targets/loaders, publisher environment, active versus inactive metadata, outer and nested provided IDs, exact loader/Minecraft/NeoForge checks, dependency results, overlap and filename hazards, confidence, rationale, runtime evidence, and final disposition.

## Required dependency semantics

Only `META-INF/neoforge.mods.toml` participates in the active NeoForge branch. Fabric metadata is retained as inactive evidence and never promoted into a NeoForge hard dependency. Loader declarations remain tied to their source document, preventing legacy `mods.toml` ranges such as `[40,)` from being evaluated as active NeoForge language-loader constraints.

The evaluator applies the FML 1.21.1 support matrix only after a direct target failure. Required missing or wrong-range dependencies fail; optional absent dependencies pass; installed optional wrong-range dependencies fail; matching incompatible dependencies fail; matching discouraged dependencies warn. Client-only dependency edges are ignored on the dedicated-server physical side. Unknown dependency owners are reported as ignored orphan tables because FML never attaches them to a declared mod. The full-inventory report describes the 190-candidate audit pool; the separate retained-provider report recomputes every edge against only the 136 installed candidates. The final matrix uses retained-provider results for retained rows, so a disabled optional, required, incompatible, or discouraged provider cannot be mistaken for an installed provider.

Reproduce those two scopes with:

```bash
uv run python tools/evaluate_candidate_compatibility.py \
  --inspection evidence/item-3/jar-inspection.json \
  --oracle-requests evidence/item-3/maven-range-requests.tsv \
  --oracle-results evidence/item-3/maven-range-results.tsv \
  --output evidence/item-3/static-compatibility-exact.json
uv run python tools/evaluate_candidate_compatibility.py \
  --inspection evidence/item-3/jar-inspection.json \
  --oracle-requests evidence/item-3/maven-range-requests.tsv \
  --oracle-results evidence/item-3/maven-range-results.tsv \
  --provider-candidates evidence/item-3/runtime/retained-server-candidates.txt \
  --output evidence/item-3/retained-compatibility-exact.json
```

Nested NeoForge mod IDs and their dependency tables participate in closure. This was necessary to expose bundled Aeronautics' active requirements on Create and Sable. `${file.jarVersion}` is replaced only from the inspected manifest implementation version.

## Named hazards

### Seven Seas

`DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar` declares Minecraft `[1.20,1.22)` and NeoForge `[21,)`. Both exact checks pass. Its isolated server reached readiness and stopped cleanly before it participated in the retained-cluster boot. It is retained; the broad filename remains a hazard flag rather than evidence.

### AdoraBuild

`adorabuild-structures-2.11.0-neoforge-1.21.3.jar` declares Minecraft `[1.21,1.21.3]` and NeoForge `[21.0.0-beta,)`. Minecraft 1.21.1 and NeoForge 21.1.249 pass the exact Maven oracle. Its isolated server reached readiness and stopped cleanly. It is retained; the filename is not treated as authoritative.

### Forge-labelled artifacts

Forge-labelled files are not accepted by filename equivalence. Each retained Forge-labelled artifact exposes active NeoForge metadata, passes its exact dependency checks, and participates in the retained-cluster lifecycle proof. The matrix preserves the filename hazard.

### Fabric-derived content

Forgified Fabric API and other dual-metadata candidates retain both metadata branches in evidence. Only NeoForge declarations drive closure. Runtime logs contain nonfatal compatibility and optional-resource diagnostics; these are not converted into gameplay or world-generation approval and must be reviewed by Items 6–7.

## Embedded libraries

Thirty-nine outer candidates contain 204 nested JAR occurrences. The overlap report records identical bytes, same-version/different-byte groups, multi-version groups, and 15 mod-ID collisions. Collisions are surfaced per candidate in the final matrix. Runtime selection remains authoritative for the admitted cluster; the report does not pretend a flat archive inventory proves Jar-in-Jar negotiation.

## Runtime decisions and preserved failures

- Seven Seas and AdoraBuild isolated boots passed.
- The initial 139-candidate cluster reached readiness but Sable's post-ready GameTest activity prevented administrative command processing; the run was preserved and invalidated.
- Removing Aeronautics alone reproduced the Sable behavior. Sable was disabled; bundled Aeronautics was disabled because its nested mods require Sable.
- A 137-candidate run without Sable reached readiness but exceeded the unchanged 60-second watchdog during Every Compat creative-tab construction. A diagnostic run with the watchdog disabled eventually stopped cleanly, but that altered control was not accepted. Every Compat was disabled instead.
- The resulting 136-candidate set passed first boot and existing-world restart with unchanged `max-tick-time=60000`, full flushes, and clean stops.

Readiness alone was not used as the gate. Failed, interrupted, altered-control, first-boot, and restart evidence is retained with hashes.

## Known limitations carried forward

The retained logs include optional-mixin target warnings, failed online update/key lookups, invalid optional compatibility loot resources, and content-level integration diagnostics. Server lifecycle success does not resolve those findings. Item 4 must clone only the retained manifest; Item 6 must audit generated configs without tuning; Item 7 must validate actual terrain/content behavior. No candidate receives client, gameplay, worldgen, or performance approval from this report.

## Exit-gate assessment

`SPECS.md` Item 3 asks that no known unsupported JAR remain enabled under an unverified assumption. The gate passes for the dedicated-server manifest because all candidates have explicit dispositions, all retained artifacts pass exact active-metadata and dependency checks, client-only and missing-dependency candidates are excluded, runtime failures are disabled, and the retained set passes repeatable lifecycle validation. Items 4–10 remain incomplete and must proceed in order. Item 11 remains unauthorized.
