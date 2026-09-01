# Candidate JAR Filename Inventory Audit — v0.3

**Input date:** 2026-09-01
**Target stated by project:** Minecraft Java 1.21.1 + NeoForge
**Source:** User-supplied proposed filename inventory
**Evidence level:** Candidate filenames only; no instance or mod artifacts currently exist

> Correction: This list is not an installed baseline. It is the proposed candidate set from which a verified Baseline v0 must be constructed. Terms such as “enabled” and “disabled” below describe the proposed filename suffix state only.

## Inventory result

| Measure | Result |
|---|---:|
| Total filename entries | 190 |
| Proposed enabled by filename convention | 188 |
| Proposed disabled by `.disabled` suffix | 2 |
| Explicitly names Minecraft 1.21.3 | 1 |
| Uses a broad `1.21`, `1.21.x`, or `1.21.X` label rather than an explicit 1.21.1 label | 26 |
| Enabled filenames with an explicit alpha/beta marker | 8 |
| Enabled filenames labelled Forge rather than NeoForge | 4 |

The count is an inventory result, not a compatibility result. A filename can be inaccurate, renamed, or broader/narrower than the metadata declared inside the JAR.

## Disabled entries

- `DistantHorizons-3.0.3-b-1.21.1-fabric-neoforge.jar.disabled`
- `xaerominimap-neoforge-1.21.1-26.4.2.jar.disabled`

These must remain part of the frozen baseline inventory even though they are not expected to load.

## Explicit point-release investigation

- `adorabuild-structures-2.11.0-neoforge-1.21.3.jar`

Its filename explicitly names Minecraft 1.21.3, so it was quarantined and inspected rather than assumed compatible. The exact Modrinth record tags it for 1.21.1 NeoForge; the publisher-hash-verified JAR declares Minecraft `[1.21, 1.21.3]`, which admits 1.21.1. It remains quarantined until a full world boot and generated-structure test because its embedded resource pack format is 48 and the filename remains contradictory.

`DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar` was also acquired and publisher-hash verified. Its exact upstream record includes 1.21.1, and its embedded metadata declares Minecraft `[1.20, 1.22)`. It passes the declared-version gate but not yet the worldgen/gameplay/performance gates.

## Broad-version labels requiring exact metadata verification

- `AI-Improvements-1.21-0.5.3.jar`
- `DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar`
- `MoogsEndStructures-1.21-2.0.3.jar`
- `MoogsNetherStructures-1.21-3.0.0-alpha.2.jar`
- `MoogsSoaringStructures-1.21-2.1.2.jar`
- `MoogsVoyagerStructures-1.21-5.0.11.jar`
- `MouseTweaks-neoforge-mc1.21-2.26.1.jar`
- `SimpleBackups-1.21-4.0.30.jar`
- `alternate_current-mc1.21-1.9.0.jar`
- `amendments-1.21-2.0.15-neoforge.jar`
- `appleskin-neoforge-mc1.21-3.0.9.jar`
- `cupboard-1.21-3.7.jar`
- `dummmmmmy-1.21-2.0.12-neoforge.jar`
- `emi_enchanting-0.1.2+1.21+neoforge.jar`
- `emi_loot-0.7.9+1.21+neoforge.jar`
- `everycomp-1.21-2.11.44-neoforge.jar`
- `fastasyncworldsave-1.21-2.6.jar`
- `fzzy_config-0.7.6+1.21+neoforge.jar`
- `konkrete_neoforge_1.9.9_MC_1.21.jar`
- `letmedespawn-1.21.x-neoforge-1.5.0.jar`
- `modelfix-1.21-1.10.jar`
- `owo-lib-neoforge-0.12.15.5-beta.1+1.21.jar`
- `packetfixer-3.3.1-1.20.5-1.21.X-merged.jar`
- `resourcefulconfig-neoforge-1.21-3.0.11.jar`
- `resourcefullib-neoforge-1.21-3.0.12.jar`

The twenty-sixth broad-version match is the explicit 1.21.3 AdoraBuild entry already separated above.

## Pre-release builds requiring elevated test coverage

- `MoogsNetherStructures-1.21-3.0.0-alpha.2.jar`
- `accessories-neoforge-1.1.0-beta.53+1.21.1.jar`
- `c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar`
- `iris-neoforge-1.8.14-beta.1+mc1.21.1.jar`
- `lithostitched-1.7.10+beta4-neoforge-21.1.jar`
- `moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar`
- `owo-lib-neoforge-0.12.15.5-beta.1+1.21.jar`
- `sodium-neoforge-0.8.12-beta.1+mc1.21.1.jar`

Pre-release status is not an automatic rejection. It requires a recorded reason for inclusion, compatibility evidence, focused regression tests, and a known rollback candidate.

## Forge-labelled entries under NeoForge

- `cc-tweaked-1.21.1-forge-1.119.0.jar`
- `player-animation-lib-forge-2.0.4+1.21.1.jar`
- `simplymore-forge-1.2.3.jar`
- `sliceanddice-forge-4.2.4.jar`

Each must be verified against embedded loader metadata and the project’s official distribution information. NeoForge compatibility must not be inferred merely because the server currently starts.

## Fabric-derived/bridge-sensitive entries

- `forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar`
- `t_and_t-neoforge-fabric-1.13.9+1.21.1.jar`
- `DistantHorizons-3.0.3-b-1.21.1-fabric-neoforge.jar.disabled`

All mods depending on Forgified Fabric API must be identified from embedded dependency metadata. The bridge and its dependents must be tested as one compatibility cluster.

## High-risk overlap clusters for controlled testing

These are not removal recommendations. They are clusters where launch success is especially weak evidence.

### Terrain and biome generation

- Tectonic
- Terralith
- Biomes O' Plenty
- Regions Unexplored
- TerraBlender
- Lithostitched
- zFastNoise

Required checks: supported composition, generation order, biome-size effects, noise-router interaction, terrain seams, structure placement, generation latency, and upgrade behavior.

### Structure generation

- When Dungeons Arise + Seven Seas
- YUNG's structure suite
- IDAS
- Integrated Stronghold/Villages
- Moog's overworld/Nether/End/soaring families
- Explorify
- Explorations
- Repurposed Structures
- AdoraBuild
- CTOV
- Towns and Towers
- Better Village
- Village Taverns

Required checks: registry identity, structure-set spacing, biome tags, collisions, redundancy, discoverability, gameplay value, loot ownership, and worldgen cost.

### Settlement/NPC generation

- CTOV
- Towns and Towers
- Better Village
- Integrated Villages
- Village Taverns
- MCA

Required checks: village replacement/augmentation semantics, POI integrity, NPC counts, pathfinding cost, profession compatibility, and settlement-role redundancy.

### Combat and equipment

- Better Combat
- Simply Swords
- Simply More
- Archers
- Rogues
- Armory
- Arsenal
- Ranged Weapon API
- Shield API
- Illager Invasion
- Creeper Overhaul

Required checks: animation and reach behavior, attribute stacking, supernatural effects, loot injection, equipment power curves, projectile behavior, server authority, and PvP-consent boundaries.

### Performance/core behavior

- AI Improvements
- Alternate Current
- C2ME alpha
- Fast Async World Save
- FerriteCore
- ImmediatelyFast
- Lithium
- ModernFix
- ServerCore
- Structure Layout Optimizer
- Sodium beta
- Entity Culling
- Let Me Despawn
- Packet Fixer

Required checks: each mod individually against a clean control, then justified combinations. Performance mods can overlap, invalidate measurements, or change correctness; “more optimization mods” is not itself a valid objective.

### Recipe and item-viewing systems

- EMI
- JEI
- EMI Enchanting
- EMI Loot
- EMI Ores
- EMI Professions
- Polymorph
- Extra Mod Integrations

Required checks: whether dual EMI/JEI installation is intentional, plugin dependencies, duplicate displays, missing recipes, recipe conflict selection, client/server necessity, and onboarding role.

### Accessory APIs

- Accessories
- Curios

Required checks: which retained content requires each API, bridge behavior if any, slot duplication, item compatibility, and whether both are necessary.

### Loot injection

- Loot Integrations core
- WDA integration
- YUNG integration
- CTOV integration
- Integrated integration
- Moog integration
- Vanilla integration
- Towns and Towers integration

Required checks: exact table targets, duplicate injection paths, probability composition, per-player container behavior, missing tables, and economy multiplication.

## Probable client-side or client-focused entries to classify before dedicated-server deployment

The following are **classification candidates**, not verified classifications:

- Ambient Sounds
- Better Advancements
- Distant Horizons (disabled)
- EMI and its viewer plugins
- ImmediatelyFast
- Iris and Iris/Flywheel compatibility
- Jade
- JEI
- Just Zoom
- LambDynamicLights
- Mouse Tweaks
- Not Enough Animations
- Reese's Sodium Options
- Simply Tooltips
- Sodium
- Sound Physics Remastered
- Xaero's Minimap (disabled)
- Xaero's World Map

Every entry must be classified from project documentation and JAR metadata. Unnecessary client mods must not be copied to the dedicated server package.

## Baseline artifacts still required to complete Item 2

1. Final admitted JAR set with exact hashes and embedded metadata.
2. Generated `config/`, `defaultconfigs/`, server properties, and worldgen settings from an authorized first world boot.
3. Separate reproducible client and dedicated-server manifests.
4. A clean server start, controlled shutdown, restart, and retained logs.
5. A client construction/import and connection smoke test.
6. Production-server hardware/OS/storage/heap values when hosting is chosen; the current test-host facts are already recorded separately.

## Current gate status

- Filename inventory: `COMPLETE`
- Enabled/disabled separation by filename suffix: `COMPLETE`
- Exact upstream identity: `COMPLETE` — all 190 filenames resolved.
- Candidate compatible-version audit: `COMPLETE` for the 176 Modrinth identities; targeted CurseForge status recorded.
- Byte hashing: `IN PROGRESS` — platform, four anchors, AdoraBuild, and Seven Seas pinned; all admitted artifacts remain.
- Embedded metadata extraction: `IN PROGRESS` — anchors and point-release investigations complete.
- Declared dependency resolution: `IN PROGRESS` — five missing required edges across two projects identified in the proposal.
- Client/server classification: `IN PROGRESS` — exact Modrinth environment audit complete; admitted-JAR confirmation pending.
- Authoritative version compatibility: `IN PROGRESS`; identity audit complete, selected-stack runtime audit pending.
- Item 2 overall: `IN PROGRESS` under the revised construct-and-freeze workflow
- Item 3 overall: `IN PROGRESS`

