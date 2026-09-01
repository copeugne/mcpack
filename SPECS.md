# Adventure / Dungeon / Exploration System
# Dependency-Ordered Implementation Plan — Revised

> Execution rule:
> Complete each numbered item before proceeding to an item that depends on it.
> Where an item contains an explicit test/decision gate, do not proceed with the
> candidate system merely because it successfully launches. It must satisfy the
> stated gameplay, compatibility, and performance requirements.

---

# PHASE I — DESIGN CONTRACT & REPRODUCIBLE BASELINE

## 1. Lock the Pack Identity and Adventure Design Contract

- [ ] Define the pack as an engineering-driven multiplayer adventure sandbox.
- [ ] Establish engineering as the principal capability-progression system.
- [ ] Establish exploration as a major reason to develop engineering.
- [ ] Establish combat as expedition pressure rather than the primary progression system.
- [ ] Establish logistics as meaningful gameplay.
- [ ] Establish infrastructure development as meaningful progression.
- [ ] Establish lightweight RPG elements only where they support adventure.
- [ ] Reject character levels as the primary progression mechanism.
- [ ] Reject mandatory skill-tree progression.
- [ ] Reject magic/spell progression.
- [ ] Reject generic legendary-loot treadmill progression.
- [ ] Reject uncontrolled stat inflation.
- [ ] Reject routine damage-sponge enemies.
- [ ] Prefer horizontal capability progression.
- [ ] Keep basic Create progression normally craftable.
- [ ] Keep basic CC:Tweaked progression normally craftable.
- [ ] Keep basic transportation progression normally obtainable.
- [ ] Keep basic Aeronautics progression independent of rare dungeon RNG.
- [ ] Allow engineering solutions to adventure problems.
- [ ] Allow reasonable sequence breaking.
- [ ] Avoid universal indestructible dungeon blocks.
- [ ] Allow deliberate structural destruction unless it fundamentally breaks the system.
- [ ] Allow aircraft to materially improve exploration.
- [ ] Prevent aircraft from eliminating the entire adventure layer.
- [ ] Preserve meaningful roles for:
  - [ ] walking.
  - [ ] horses.
  - [ ] boats.
  - [ ] trains.
  - [ ] aircraft.
- [ ] Preserve meaningful roles for:
  - [ ] factories.
  - [ ] logistics.
  - [ ] computers.
  - [ ] vehicles.
  - [ ] weapons.
  - [ ] siege equipment.
- [ ] Record these principles as non-negotiable design constraints.

### Exit Gate
- [ ] Every later system can be evaluated against an explicit design contract.


## 2. Freeze the Existing Technical Baseline

- [ ] Record Minecraft version.
  - [ ] Confirm 1.21.1.
- [ ] Record exact NeoForge version.
- [ ] Record Java runtime/version.
- [ ] Record every enabled JAR.
- [ ] Record every disabled JAR.
- [ ] Record every mod version.
- [ ] Record configs.
- [ ] Record datapacks.
- [ ] Record server properties.
- [ ] Record world-generation settings.
- [ ] Record JVM flags.
- [ ] Record server hardware.
- [ ] Record CPU.
- [ ] Record physical RAM.
- [ ] Record allocated heap.
- [ ] Record storage type.
- [ ] Record OS.
- [ ] Record expected normal concurrent player count.
- [ ] Record expected peak player count.
- [ ] Hash or otherwise version the baseline files.
- [ ] Preserve an untouched baseline copy.

### Exit Gate
- [ ] The exact original pack can be reconstructed.


## 3. Perform the Exact Version and Dependency Audit

- [ ] Verify every enabled mod against Minecraft 1.21.1.
- [ ] Verify every enabled mod against the installed NeoForge version.
- [ ] Verify required dependencies.
- [ ] Verify dependency versions.
- [ ] Verify optional integrations actually in use.
- [ ] Identify Forge JARs being relied upon under NeoForge.
- [ ] Identify Fabric-derived components.
- [ ] Verify Forgified Fabric API dependencies.
- [ ] Identify overlapping embedded libraries.

- [ ] Specifically investigate:
  - [ ] `DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar`
  - [ ] Confirm exact 1.21.1 support.
  - [ ] Replace if the installed build targets a later 1.21 release.

- [ ] Specifically investigate:
  - [ ] `adorabuild-structures-2.11.0-neoforge-1.21.3.jar`
  - [ ] Confirm whether it is actually compatible with 1.21.1.
  - [ ] Replace/remove if not.

- [ ] Audit all broadly labelled `1.21.x` JARs.
- [ ] Audit all JARs whose filename names another Minecraft point release.
- [ ] Audit server/client-only classifications.
- [ ] Identify unnecessary client mods on the dedicated server.
- [ ] Identify missing server-side dependencies.
- [ ] Resolve hard compatibility failures before proceeding.

### Exit Gate
- [ ] No known unsupported JAR remains in the baseline under an unverified assumption.


## 4. Create the Controlled Test Environment

- [ ] Create a dedicated test server.
- [ ] Keep it separate from production.
- [ ] Clone the validated baseline configuration.
- [ ] Select multiple deterministic test seeds.
- [ ] Include:
  - [ ] ordinary terrain seed.
  - [ ] mountainous seed.
  - [ ] ocean-heavy seed.
  - [ ] biome-diverse seed.
- [ ] Preserve untouched copies.
- [ ] Establish repeatable world deletion/regeneration procedure.
- [ ] Establish configuration-version naming.
- [ ] Establish experimental branch naming.
- [ ] Version-control configs.
- [ ] Version-control datapacks.
- [ ] Version-control custom spawn rules.
- [ ] Version-control loot tables.
- [ ] Configure automated backups.
- [ ] Perform an actual restore test.
- [ ] Confirm restored worlds boot correctly.

### Exit Gate
- [ ] Any experiment can be reproduced or rolled back.


## 5. Establish Measurement and Profiling Methodology

- [ ] Configure Spark.
- [ ] Define idle MSPT measurement.
- [ ] Define active-combat MSPT measurement.
- [ ] Define fresh-worldgen MSPT measurement.
- [ ] Define TPS measurement.
- [ ] Define memory measurement.
- [ ] Define garbage-collection measurement.
- [ ] Define entity-count measurement.
- [ ] Define pathfinding-cost measurement.
- [ ] Define chunk-generation measurement.
- [ ] Define structure-count methodology.
- [ ] Define structure-distance methodology.
- [ ] Define travel-time methodology.
- [ ] Define dungeon-duration methodology.
- [ ] Define death-rate methodology.
- [ ] Define loot-value methodology.

- [ ] Define exploration metrics:
  - [ ] structures per 1,000 chunks.
  - [ ] actionable locations per 1,000 chunks.
  - [ ] combat encounters per 1,000 chunks.
  - [ ] proper dungeons per 1,000 chunks.
  - [ ] major expeditions per 1,000 chunks.

- [ ] Define repetition metrics:
  - [ ] unique structure families encountered per hour.
  - [ ] time to first repeated structure family.
  - [ ] repeated dungeon-layout frequency.

- [ ] Define Adventure Activity Ratio:
  - [ ] meaningful interaction time.
  - [ ] divided by total expedition time.

- [ ] Define player-count test cases:
  - [ ] solo.
  - [ ] 2 players.
  - [ ] 4 players.
  - [ ] expected normal concurrency.
  - [ ] expected peak concurrency.

### Exit Gate
- [ ] Every later tuning claim can be tested quantitatively.


---

# PHASE II — BASELINE FORENSICS

## 6. Audit Every Existing Relevant Configuration

- [ ] Inspect Sparse Structures.
- [ ] Inspect Structure Essentials.
- [ ] Inspect ServerCore.
- [ ] Inspect C2ME.
- [ ] Inspect Chunky.
- [ ] Inspect Structure Layout Optimizer.
- [ ] Inspect WDA configs.
- [ ] Inspect YUNG configs.
- [ ] Inspect IDAS configs.
- [ ] Inspect Moog configs.
- [ ] Inspect village-generation configs.
- [ ] Inspect Loot Integrations.
- [ ] Inspect mob spawning configs.
- [ ] Inspect difficulty-related configs.
- [ ] Record all non-default values.
- [ ] Identify global structure-spacing multipliers.
- [ ] Identify per-structure overrides.
- [ ] Identify disabled structure sets.
- [ ] Identify hidden causes of low encounter density.
- [ ] Do not change anything yet.

### Depends On
- Items 2–5.


## 7. Audit Current Terrain and Worldgen Interactions

- [ ] Test:
  - [ ] Tectonic.
  - [ ] Terralith.
  - [ ] Biomes O' Plenty.
  - [ ] Regions Unexplored.
  - [ ] TerraBlender.
  - [ ] Lithostitched.
  - [ ] BetterEnd.
  - [ ] YUNG.
  - [ ] WDA.
  - [ ] IDAS.
  - [ ] Integrated structures.
  - [ ] Moog.
  - [ ] Explorify.
  - [ ] Explorations.
  - [ ] Repurposed Structures.
  - [ ] CTOV.
  - [ ] Towns & Towers.

- [ ] Inspect for:
  - [ ] fragmented biomes.
  - [ ] tiny biomes.
  - [ ] unnatural terrain transitions.
  - [ ] buried structures.
  - [ ] floating structures.
  - [ ] cliff intersections.
  - [ ] bad underwater placement.
  - [ ] overlapping structures.
  - [ ] overlapping villages.
  - [ ] failed placements.
  - [ ] impossible biome restrictions.
  - [ ] excessive terrain modification around structures.

- [ ] Separate:
  - [ ] cosmetic issues.
  - [ ] gameplay issues.
  - [ ] performance issues.
  - [ ] outright generation failures.

### Depends On
- Item 6.


## 8. Inventory Every Structure Family

- [ ] Enumerate structures from WDA.
- [ ] Enumerate WDA Seven Seas.
- [ ] Enumerate YUNG's structures.
- [ ] Enumerate IDAS.
- [ ] Enumerate Integrated Stronghold.
- [ ] Enumerate Integrated Villages.
- [ ] Enumerate Moog families.
- [ ] Enumerate Explorify.
- [ ] Enumerate Explorations.
- [ ] Enumerate Repurposed Structures.
- [ ] Enumerate AdoraBuild.
- [ ] Enumerate CTOV.
- [ ] Enumerate Towns & Towers.
- [ ] Enumerate Better Village.
- [ ] Enumerate Village Taverns.

- [ ] For each structure family record:
  - [ ] dimension.
  - [ ] biome constraints.
  - [ ] approximate footprint.
  - [ ] approximate vertical size.
  - [ ] intended hostility.
  - [ ] mob source.
  - [ ] loot-table source.
  - [ ] generated spawners.
  - [ ] whether enemies are authored or natural.
  - [ ] visual discoverability.
  - [ ] underground/surface classification.

### Depends On
- Items 6–7.


## 9. Classify the Existing Structure Stack

- [ ] Provisionally classify every structure family as:
  - [ ] Tier 0 — ambient landmark.
  - [ ] civilization.
  - [ ] Tier 1 — small encounter.
  - [ ] Tier 2 — proper dungeon.
  - [ ] Tier 3 — major expedition.
  - [ ] Tier 4 — world objective.

- [ ] Flag structures that appear dungeon-like but lack meaningful gameplay.
- [ ] Flag structures that are mostly decoration.
- [ ] Flag oversized structures with little internal gameplay.
- [ ] Flag overlapping themes.
- [ ] Flag redundant village families.
- [ ] Flag redundant ruins.
- [ ] Flag redundant towers.
- [ ] Flag redundant dungeon archetypes.

### Depends On
- Item 8.


## 10. Measure Baseline Structure and Encounter Density

- [ ] Generate representative test regions across all selected seeds.
- [ ] Measure structures per 1,000 chunks.
- [ ] Measure actionable locations per 1,000 chunks.
- [ ] Measure combat encounters per 1,000 chunks.
- [ ] Measure proper dungeons per 1,000 chunks.
- [ ] Measure major expeditions per 1,000 chunks.
- [ ] Measure village density.
- [ ] Measure average nearest-neighbor distance by category.
- [ ] Measure clustering.
- [ ] Measure large empty regions.
- [ ] Compare biomes.
- [ ] Compare seeds.
- [ ] Determine Sparse Structures' contribution to the observed distribution.

### Depends On
- Items 5–9.


## 11. Measure Baseline Exploration Pacing and Repetition

- [ ] Perform fixed-duration/fixed-distance exploration on foot.
- [ ] Repeat by horse.
- [ ] Repeat by boat.
- [ ] Record:
  - [ ] visual discoveries.
  - [ ] actionable discoveries.
  - [ ] hostile encounters.
  - [ ] dungeons.
  - [ ] major structures.
  - [ ] villages.
  - [ ] dead travel time.

- [ ] Calculate Adventure Activity Ratio.
- [ ] Measure unique structure families encountered per hour.
- [ ] Measure time to first repeat.
- [ ] Measure repeated structures over fixed distances.
- [ ] Identify visual richness that provides little gameplay.
- [ ] Identify genuinely empty travel.
- [ ] Separate low spawn density from low discoverability.

### Depends On
- Item 10.


## 12. Measure Structure Discoverability

- [ ] Evaluate surface visibility.
- [ ] Evaluate underground entrance visibility.
- [ ] Evaluate visibility from valleys.
- [ ] Evaluate visibility from high terrain.
- [ ] Evaluate biome concealment.
- [ ] Evaluate whether structures have recognizable silhouettes.
- [ ] Evaluate whether underground entrances communicate importance.
- [ ] Determine whether players require `/locate` to realistically find certain content.
- [ ] Distinguish:
  - [ ] generated frequently but hard to notice.
  - [ ] genuinely generated rarely.
- [ ] Record discoverability independently from generation density.

### Depends On
- Items 10–11.


## 13. Measure Baseline Dungeon Quality

- [ ] Sample every significant dungeon family.
- [ ] Record room count.
- [ ] Record branching.
- [ ] Record vertical progression.
- [ ] Record dungeon depth.
- [ ] Record traversal time.
- [ ] Record combat time.
- [ ] Record enemy count.
- [ ] Record enemy diversity.
- [ ] Record meaningful hazards.
- [ ] Record chokepoints.
- [ ] Record dead/empty rooms.
- [ ] Record loot distribution.
- [ ] Record final-room quality.
- [ ] Record bypass opportunities.
- [ ] Record external-access vulnerabilities.
- [ ] Determine expected replay value.
- [ ] Identify structures that are visually large but mechanically shallow.

### Depends On
- Items 9–12.


## 14. Measure Baseline Enemy and Combat Quality

- [ ] Test vanilla hostile mobs.
- [ ] Test Illager Invasion.
- [ ] Test Creeper Overhaul.
- [ ] Test Better Combat.
- [ ] Measure melee/ranged composition.
- [ ] Test pathfinding.
- [ ] Test doorway/chokepoint exploitation.
- [ ] Test verticality.
- [ ] Test ranged pressure.
- [ ] Test group pressure.
- [ ] Identify predictable encounters.
- [ ] Identify structures where enemies cannot effectively reach players.
- [ ] Identify whether difficulty currently comes primarily from mob count.
- [ ] Identify whether combat becomes repetitive across different structure families.

### Depends On
- Item 13.


## 15. Audit Baseline Loot and Salvage Economy

- [ ] Sample loot from every structure tier/family.
- [ ] Record common resources.
- [ ] Record equipment.
- [ ] Record food.
- [ ] Record enchanted items.
- [ ] Record modded loot.
- [ ] Record rare loot.
- [ ] Identify duplicate injections.
- [ ] Identify worthless loot.
- [ ] Identify excessive bulk materials.
- [ ] Identify rewards trivialized by automation.

- [ ] Measure structure salvage value:
  - [ ] valuable building blocks.
  - [ ] metal blocks.
  - [ ] machinery.
  - [ ] decorative rare blocks.
  - [ ] other harvestable components.

- [ ] Compare:
  - [ ] chest-loot value.
  - [ ] structure-salvage value.

- [ ] Identify structures more valuable to quarry than clear.
- [ ] Determine whether that behavior is desirable.

### Depends On
- Items 8 and 13.


## 16. Audit Baseline Multiplayer Persistence and Depletion

- [ ] Have Player A clear representative structures.
- [ ] Have Player B visit afterward.
- [ ] Record remaining loot.
- [ ] Record destroyed spawners.
- [ ] Record broken doors.
- [ ] Record breached walls.
- [ ] Record mined shortcuts.
- [ ] Record removed valuable blocks.
- [ ] Record whether the structure still offers meaningful gameplay.
- [ ] Determine how quickly active players deplete nearby exploration content.
- [ ] Determine late-joiner impact.
- [ ] Distinguish:
  - [ ] loot depletion.
  - [ ] physical dungeon depletion.
  - [ ] encounter depletion.

### Depends On
- Items 13 and 15.


## 17. Establish Baseline Performance

- [ ] Measure idle MSPT.
- [ ] Measure normal gameplay MSPT.
- [ ] Measure fresh-worldgen MSPT.
- [ ] Measure WDA-generation spikes.
- [ ] Measure YUNG-generation spikes.
- [ ] Measure village-generation spikes.
- [ ] Measure combat MSPT.
- [ ] Measure entity tick cost.
- [ ] Measure pathfinding cost.
- [ ] Measure memory usage.
- [ ] Measure GC behavior.
- [ ] Test multiple simultaneous explorers.
- [ ] Record chunk-generation latency.
- [ ] Record server responsiveness during generation.
- [ ] Store these values as the performance baseline.

### Depends On
- Items 5–16.


## 18. Produce the Baseline Root-Cause Report

- [ ] Determine whether "few and far between" primarily comes from:
  - [ ] Sparse Structures.
  - [ ] terrain scale.
  - [ ] structure biome restrictions.
  - [ ] low discoverability.
  - [ ] genuinely low density.
  - [ ] too many non-actionable structures.
  - [ ] excessive travel relative to interaction.

- [ ] Quantify:
  - [ ] structure abundance.
  - [ ] encounter abundance.
  - [ ] dungeon abundance.
  - [ ] repetition.
  - [ ] discoverability.
  - [ ] combat quality.
  - [ ] loot quality.
  - [ ] multiplayer depletion.
  - [ ] performance.

- [ ] Identify root causes rather than symptoms.
- [ ] Rank problems by severity.
- [ ] Do not select final solutions yet.

# PHASE III — REQUIREMENTS & SYSTEM DESIGN

## 19. Define the Final Adventure Structure Taxonomy

- [ ] Convert provisional structure classifications into final design categories.
- [ ] Define Tier 0 — Ambient Landmark.
  - [ ] Primarily supports visual exploration.
  - [ ] Minimal or no combat.
  - [ ] Short interaction time.
  - [ ] Low reward significance.
- [ ] Define Civilization.
  - [ ] Villages.
  - [ ] Settlements.
  - [ ] Taverns.
  - [ ] Trade hubs.
  - [ ] Expedition staging points.
- [ ] Define Tier 1 — Small Encounter.
  - [ ] Approximately 5–15 minutes.
  - [ ] Low-to-moderate combat pressure.
  - [ ] Frequent enough to break travel monotony.
- [ ] Define Tier 2 — Proper Dungeon.
  - [ ] Approximately 20–45 minutes.
  - [ ] Multiple rooms.
  - [ ] Meaningful traversal.
  - [ ] Multiple encounters.
  - [ ] Meaningful reward.
- [ ] Define Tier 3 — Major Expedition.
  - [ ] Approximately 30–90+ minutes.
  - [ ] High preparation requirements.
  - [ ] Group-friendly.
  - [ ] High logistical value.
- [ ] Define Tier 4 — World Objective.
  - [ ] Dimension progression.
  - [ ] Server-scale objectives.
  - [ ] Endgame expeditions.
- [ ] Require every retained structure family to have one clear primary role.

### Depends On
- Item 18.


## 20. Define the Transportation-Scale Model

- [ ] Define expected exploration scale on foot.
- [ ] Define expected exploration scale on horseback.
- [ ] Define expected exploration scale by boat.
- [ ] Define expected exploration scale by train.
- [ ] Define expected exploration scale by aircraft.
- [ ] Define approximate practical travel speeds for each.
- [ ] Define acceptable travel duration to:
  - [ ] Tier 0 content.
  - [ ] Tier 1 content.
  - [ ] Tier 2 content.
  - [ ] Tier 3 content.
  - [ ] Tier 4 objectives.
- [ ] Preserve distinct transportation roles:
  - [ ] Foot = local exploration.
  - [ ] Horse/boat = local/regional movement.
  - [ ] Train = persistent high-throughput regional logistics.
  - [ ] Aircraft = flexible long-range expeditions.
- [ ] Ensure aircraft do not make trains pointless.
- [ ] Ensure trains do not replace exploration.
- [ ] Use the resulting travel model when choosing structure spacing.

### Depends On
- Items 11–12 and 19.


## 21. Define Target Adventure Cadence

- [ ] Define target average time between visual discoveries.
- [ ] Define target average time between actionable discoveries.
- [ ] Define target average time between combat encounters.
- [ ] Define target average time between Tier 1 encounters.
- [ ] Define target average time between Tier 2 dungeons.
- [ ] Define target average time between Tier 3 expeditions.
- [ ] Define target rarity of Tier 4 objectives.
- [ ] Define acceptable Adventure Activity Ratio.
- [ ] Define acceptable dead-travel percentage.
- [ ] Define cadence separately for:
  - [ ] early game.
  - [ ] mid game.
  - [ ] late game.
- [ ] Define cadence separately for:
  - [ ] walking.
  - [ ] horse/boat.
  - [ ] train.
  - [ ] aircraft.
- [ ] Do not solve poor cadence by making giant structures common.

### Depends On
- Items 18–20.


## 22. Define Dungeon Topology Requirements

- [ ] Define minimum requirements for a structure to count as a proper dungeon.
- [ ] Require meaningful interior traversal.
- [ ] Define minimum useful room count.
- [ ] Define acceptable empty-room percentage.
- [ ] Define verticality expectations.
- [ ] Define branching expectations.
- [ ] Define dungeon-depth expectations.
- [ ] Define encounter-spacing expectations.
- [ ] Define rest/breathing-space expectations.
- [ ] Define miniboss/finale placement expectations.
- [ ] Define loot distribution throughout the dungeon.
- [ ] Avoid concentrating all value in one easily reached chest.
- [ ] Require larger dungeons to contain multiple gameplay phases.
- [ ] Define how underground layouts counterbalance aircraft.
- [ ] Preserve destructibility and engineering freedom.

### Depends On
- Items 13, 19, 21.


## 23. Define Dungeon Objective Variety

- [ ] Define allowed dungeon objectives.
  - [ ] Reach a deep chamber.
  - [ ] Clear a defended zone.
  - [ ] Recover a specific object.
  - [ ] Find a map or intelligence item.
  - [ ] Defeat a commander.
  - [ ] Search branching paths.
  - [ ] Destroy hostile infrastructure.
  - [ ] Retrieve multiple components where appropriate.
- [ ] Avoid making every location:
  - [ ] enter.
  - [ ] kill.
  - [ ] loot.
  - [ ] exit.
- [ ] Avoid excessive scripted quest behavior.
- [ ] Preserve sandbox solutions.
- [ ] Ensure objectives tolerate wall breaching and alternative routes where reasonable.
- [ ] Prefer objectives distributed through the dungeon rather than single-room checks.

### Depends On
- Item 22.


## 24. Define Dungeon Persistence and Repeatability Policy

- [ ] Decide whether dungeons are fundamentally:
  - [ ] one-time persistent world events.
  - [ ] repeatable content.
  - [ ] a mixture depending on tier.
- [ ] Decide whether:
  - [ ] destroyed walls remain destroyed.
  - [ ] mined shortcuts remain.
  - [ ] spawners remain destroyed.
  - [ ] player-built bridges remain.
  - [ ] breached entrances remain.
- [ ] Decide how later players experience previously altered dungeons.
- [ ] Distinguish loot freshness from physical dungeon freshness.
- [ ] Determine whether Tier 1 encounters need repeatability.
- [ ] Determine whether Tier 2 dungeons need repeatability.
- [ ] Determine whether Tier 3 expeditions should remain permanently changed.
- [ ] Define whether the world should visibly preserve expedition history.
- [ ] Ensure Lootr or equivalent systems do not create the false assumption that physical content also resets.

### Depends On
- Items 16, 22–23.


## 25. Define the Difficulty Model

- [ ] Make encounter composition the primary difficulty lever.
- [ ] Define difficulty using:
  - [ ] enemy roles.
  - [ ] enemy count.
  - [ ] ranged pressure.
  - [ ] armor/equipment.
  - [ ] positioning.
  - [ ] terrain.
  - [ ] chokepoints.
  - [ ] reinforcements.
  - [ ] elites.
- [ ] Use raw health increases conservatively.
- [ ] Use raw damage increases conservatively.
- [ ] Avoid extreme distance-based scaling.
- [ ] Avoid late-game mobs becoming damage sponges.
- [ ] Define difficulty expectations for:
  - [ ] Tier 1.
  - [ ] Tier 2.
  - [ ] Tier 3.
  - [ ] Tier 4.
- [ ] Define expected difficulty for:
  - [ ] solo players.
  - [ ] duos.
  - [ ] 3–4 player groups.
- [ ] Ensure engineering can meaningfully reduce expedition difficulty.

### Depends On
- Items 14, 19, 22–24.


## 26. Define Enemy Role and Encounter Archetypes

- [ ] Define basic melee enemy role.
- [ ] Define armored melee role.
- [ ] Define ranged role.
- [ ] Define fast/flanking role.
- [ ] Define heavy role.
- [ ] Define defensive role.
- [ ] Define elite role.
- [ ] Define commander role.
- [ ] Define environmental-threat role.

- [ ] Define themed encounter families:
  - [ ] undead.
  - [ ] illager.
  - [ ] cave.
  - [ ] spider.
  - [ ] ocean.
  - [ ] Nether.
  - [ ] End.
  - [ ] dimension-specific.

- [ ] Define easy encounter compositions.
- [ ] Define medium encounter compositions.
- [ ] Define hard encounter compositions.
- [ ] Define expedition encounter compositions.
- [ ] Prefer tactical variety over simply adding more monster species.

### Depends On
- Item 25.


## 27. Define Elite, Miniboss, and Boss Philosophy

- [ ] Define what qualifies as an elite.
- [ ] Define what qualifies as a miniboss.
- [ ] Define what qualifies as a true boss.
- [ ] Decide whether the pack actually needs dedicated boss mods.
- [ ] Prefer faction/location-specific commanders where possible.
- [ ] Avoid bosses that rely primarily on enormous HP pools.
- [ ] Avoid boss progression becoming the pack's primary progression.
- [ ] Ensure siege weapons and engineering remain relevant.
- [ ] Define boss/miniboss reward rules.
- [ ] Define maximum acceptable stat inflation.
- [ ] Keep dedicated boss-mod selection deferred until ordinary encounters are tested.

### Depends On
- Items 25–26.


## 28. Define the Loot Economy

- [ ] Define reward categories:
  - [ ] expedition supplies.
  - [ ] ordinary materials.
  - [ ] equipment.
  - [ ] discovery/intelligence.
  - [ ] engineering materials.
  - [ ] engineering capabilities.
  - [ ] cosmetics.
  - [ ] trophies.
  - [ ] collectibles.
- [ ] Define loot tiers corresponding to structure tiers.
- [ ] Define rarity bands.
- [ ] Define economic value expectations.
- [ ] Avoid bulk iron/copper/gold becoming primary late-game rewards.
- [ ] Avoid excessive diamonds.
- [ ] Avoid excessive enchanted books.
- [ ] Ensure high-value rewards are at least one of:
  - [ ] non-automatable.
  - [ ] difficult to mass-produce.
  - [ ] unique.
  - [ ] prestige-oriented.
  - [ ] horizontally useful.
- [ ] Ensure foundational engineering remains normally craftable.
- [ ] Avoid mandatory rare-RNG progression gates.

### Depends On
- Items 15, 19, 25–27.


## 29. Define Reward Renewability and Automation Rules

- [ ] Classify every planned valuable reward as:
  - [ ] renewable.
  - [ ] non-renewable.
  - [ ] farmable.
  - [ ] non-farmable.
  - [ ] structure-limited.
  - [ ] player-limited.
- [ ] Identify rewards that could become mob-farm outputs.
- [ ] Identify rewards that could be automated using Create.
- [ ] Identify rewards that could be extracted with hoppers/pipes.
- [ ] Identify rewards that could be mass-produced after one discovery.
- [ ] Prevent one rare dungeon drop from unintentionally becoming an industrial resource at hundreds per hour.
- [ ] Decide which automation interactions are desirable.
- [ ] Decide which interactions destroy the intended adventure loop.
- [ ] Prefer reward design changes over arbitrary automation bans.

### Depends On
- Item 28.


## 30. Define Engineering ↔ Adventure Integration

- [ ] Define how Create contributes to expedition preparation.
- [ ] Define how Aeronautics contributes to expeditions.
- [ ] Define how Steam 'n' Rails contributes.
- [ ] Define how CC:Tweaked contributes.
- [ ] Define how Create Big Cannons contributes.
- [ ] Define how Diesel Generators contributes.
- [ ] Define potential future engineering integrations.

- [ ] Define suitable horizontal rewards:
  - [ ] specialized ammunition.
  - [ ] rare schematics.
  - [ ] advanced sensors.
  - [ ] navigation components.
  - [ ] specialized machine parts.
  - [ ] vehicle upgrades.
  - [ ] vehicle cosmetics.
  - [ ] specialized tools.
  - [ ] engineering trophies.

- [ ] Explicitly exclude from dungeon gating:
  - [ ] Mechanical Press.
  - [ ] Mechanical Mixer.
  - [ ] basic bearings.
  - [ ] basic trains.
  - [ ] basic CC:Tweaked computers.
  - [ ] foundational Create mechanisms.
- [ ] Document which rewards are horizontal rather than strictly stronger.

### Depends On
- Items 28–29.


## 31. Define Discovery and Navigation Progression

- [ ] Define how players learn about nearby Tier 1 content.
- [ ] Define how players discover Tier 2 dungeons.
- [ ] Define how players discover Tier 3 expeditions.
- [ ] Define how Tier 4 objectives are revealed.
- [ ] Prefer:
  - [ ] maps.
  - [ ] clues.
  - [ ] coordinates.
  - [ ] cartographers.
  - [ ] found documents.
  - [ ] structure-to-structure leads.
- [ ] Define possible chain:
  - [ ] local discovery.
  - [ ] clue.
  - [ ] dungeon.
  - [ ] major clue.
  - [ ] expedition.
- [ ] Avoid requiring `/locate`.
- [ ] Avoid making GUI structure selectors the normal player experience.
- [ ] Account for structure discoverability from Item 12.

### Depends On
- Items 12, 19–23, 28.


## 32. Define Multiplayer Expedition and Loot Rules

- [ ] Define intended solo viability.
- [ ] Define duo viability.
- [ ] Define 3–4 player behavior.
- [ ] Define larger-group behavior.
- [ ] Define group reward policy.
- [ ] Define per-player loot policy.
- [ ] Define shared-loot policy.
- [ ] Define globally rare reward policy.
- [ ] Prevent one dungeon from multiplying rare engineering rewards linearly with player count.
- [ ] Ensure group play is not punished.
- [ ] Avoid mandatory class roles.
- [ ] Allow roles to emerge through:
  - [ ] equipment.
  - [ ] vehicle operation.
  - [ ] logistics.
  - [ ] CC:Tweaked.
  - [ ] weapons.
  - [ ] engineering.
- [ ] Account for persistent dungeon modification from Item 24.

### Depends On
- Items 24, 28–31.


## 33. Define Civilization and Settlement Roles

- [ ] Determine intended role of villages and settlements.
- [ ] Define potential functions:
  - [ ] food resupply.
  - [ ] trade.
  - [ ] expedition maps.
  - [ ] rumors/information.
  - [ ] staging areas.
  - [ ] transport hubs.
- [ ] Determine whether multiple village-generation mods are necessary.
- [ ] Separate worldgen decision from later NPC/gameplay integration.
- [ ] Define expected civilization density.
- [ ] Define safe-vs-hostile world rhythm.

### Depends On
- Items 9, 19, 21, 31.


## 34. Define Dimension Roles

- [ ] Decide whether Aether fits the final identity.
- [ ] Decide whether Deep Aether fits.
- [ ] Identify fantasy progression elements that conflict with the no-magic direction.
- [ ] Define BetterEnd's role.
- [ ] Define End progression.
- [ ] Define whether dimensions are:
  - [ ] optional expeditions.
  - [ ] progression milestones.
  - [ ] endgame objectives.
- [ ] Avoid dimensions becoming disconnected secondary RPG campaigns.
- [ ] Determine whether dimension decisions affect the loot and engineering economy.

### Depends On
- Items 1, 19, 28–30.


## 35. Define Combat-Mod Boundaries

- [ ] Audit:
  - [ ] Better Combat.
  - [ ] Simply Swords.
  - [ ] Simply More.
  - [ ] Archers.
  - [ ] Rogues.
  - [ ] Armory.
  - [ ] Arsenal.
- [ ] Identify supernatural weapon effects.
- [ ] Identify magical-looking equipment.
- [ ] Identify excessive attribute scaling.
- [ ] Decide what aesthetic level is acceptable:
  - [ ] grounded.
  - [ ] fantastical but non-magical.
  - [ ] hybrid.
- [ ] Ensure weapon progression does not replace engineering progression.
- [ ] Decide which combat mods are provisionally retained before final loot tables are built.

### Depends On
- Items 1, 25–30.


## 36. Define Destructibility, Breaching, and Automation-Bypass Policy

- [ ] Test/define acceptable:
  - [ ] hand mining.
  - [ ] drills.
  - [ ] explosives.
  - [ ] Create contraptions.
  - [ ] Create Big Cannons.
  - [ ] roof access.
  - [ ] side-wall breaching.
  - [ ] tunnel bypasses.
  - [ ] automated chest extraction.
  - [ ] remote peripherals.
  - [ ] hopper extraction.
  - [ ] portable storage exploitation.
- [ ] Separate:
  - [ ] clever engineering solution.
  - [ ] accidental total content bypass.
- [ ] Prefer architectural resilience to artificial restrictions.
- [ ] Use:
  - [ ] dungeon depth.
  - [ ] distributed objectives.
  - [ ] distributed loot.
  - [ ] multiple encounters.
- [ ] Avoid universal unbreakable blocks.

### Depends On
- Items 22–24, 29–30.


## 37. Define Expedition Preparation, Failure, and Recovery

- [ ] Define preparation requirements:
  - [ ] food.
  - [ ] ammunition.
  - [ ] tools.
  - [ ] repair materials.
  - [ ] storage.
  - [ ] navigation.
  - [ ] fuel/power where applicable.
  - [ ] portable equipment.
- [ ] Define what happens when an expedition retreats.
- [ ] Define what happens when players die.
- [ ] Define what happens when an aircraft crashes.
- [ ] Define what happens when ammunition runs out.
- [ ] Define whether partially cleared dungeons remain partially cleared.
- [ ] Define whether players can return later.
- [ ] Define grave-recovery expectations.
- [ ] Avoid unrecoverable death spirals.
- [ ] Make failure meaningful without making exploration irrational.

### Depends On
- Items 24–25, 30, 32, 36.


# PHASE IV — FEASIBILITY GATES & CONTENT-STACK REDUCTION

## 38. Perform Early Candidate-Mod Feasibility Screening

- [ ] Verify actual 1.21.1 NeoForge builds for:
  - [ ] Dungeon Crawl.
  - [ ] Lootr.
  - [ ] In Control!.
  - [ ] Improved Mobs.
  - [ ] Enhanced AI.
  - [ ] Zombie Awareness.
  - [ ] Mob Champions.
  - [ ] Guard Villagers.
- [ ] Verify dependencies.
- [ ] Verify server/client classification.
- [ ] Verify launch compatibility.
- [ ] Verify configuration capabilities.
- [ ] Verify whether required mechanics are exposed.
- [ ] For In Control!, verify exactly which conditions can be used reliably.
- [ ] Specifically verify structure-aware or structure-adjacent spawning capabilities.
- [ ] Distinguish desired encounter logic from technically achievable encounter logic.
- [ ] Reject candidates that cannot solve a documented problem.

### Depends On
- Items 18–37.


## 39. Run Controlled Structure-Redundancy Experiments

- [ ] Establish full-stack control world.
- [ ] Generate identical seed/radius variants with candidate structure families removed individually.
- [ ] Test:
  - [ ] Moog's Voyager Structures.
  - [ ] Moog's Structures.
  - [ ] Moog's Soaring Structures.
  - [ ] Explorify.
  - [ ] Explorations.
  - [ ] Repurposed Structures.
  - [ ] AdoraBuild.
  - [ ] Better Village.
  - [ ] other overlaps identified in Item 18.
- [ ] Compare:
  - [ ] visual diversity.
  - [ ] actionable-location density.
  - [ ] repetition.
  - [ ] structure-family uniqueness.
  - [ ] worldgen cost.
  - [ ] overlap.
  - [ ] adventure value.
- [ ] Run equivalent tests for overlapping village generators.
- [ ] Require every retained structure family to justify itself.

### Depends On
- Items 8–18, 33, 38.


## 40. Freeze the Provisional Content and Worldgen Stack

- [ ] Decide which existing structure mods remain.
- [ ] Decide which structure mods are removed.
- [ ] Decide which village-generation mods remain.
- [ ] Decide which dimension mods remain.
- [ ] Decide which combat-content mods remain provisionally.
- [ ] Resolve version-incompatible mods.
- [ ] Record reasons for each removal.
- [ ] Record reasons for each retained overlapping mod.
- [ ] Freeze the provisional stack before worldgen tuning.
- [ ] Do not treat this as final v1 freeze; later evidence may still justify removal.

### Depends On
- Items 34–35, 38–39.


# PHASE V — ADD THE MISSING DUNGEON LAYER BEFORE SPACING TUNING

## 41. Integrate and Evaluate the Proposed Underground Dungeon Layer

- [ ] Add Dungeon Crawl to the controlled test branch.
- [ ] Verify server startup.
- [ ] Verify generation with:
  - [ ] Tectonic.
  - [ ] Terralith.
  - [ ] BOP.
  - [ ] Regions Unexplored.
  - [ ] current structure stack.
- [ ] Test terrain integration.
- [ ] Test entrance discoverability.
- [ ] Test actual dungeon depth.
- [ ] Test layout repetition.
- [ ] Test completion duration.
- [ ] Test enemy population.
- [ ] Test loot.
- [ ] Test destructibility.
- [ ] Test aircraft relevance.
- [ ] Test whether underground topology genuinely addresses surface bypass.
- [ ] Measure generation performance.
- [ ] Measure density before custom spacing.
- [ ] Accept Dungeon Crawl only if it fills the documented Tier 2/3 topology gap.
- [ ] Reject it if it merely adds more generic structure volume.

### Depends On
- Items 22–24, 38–40.


## 42. Re-Measure the Combined Provisional Worldgen Stack

- [ ] Regenerate representative seeds with:
  - [ ] pruned existing stack.
  - [ ] accepted new dungeon layer.
- [ ] Re-measure:
  - [ ] structures per 1,000 chunks.
  - [ ] actionable locations.
  - [ ] Tier 1 encounters.
  - [ ] Tier 2 dungeons.
  - [ ] Tier 3 expeditions.
  - [ ] villages.
  - [ ] repetition.
  - [ ] discoverability.
  - [ ] Adventure Activity Ratio.
- [ ] Compare to baseline.
- [ ] Identify remaining dead zones.
- [ ] Identify newly excessive density.
- [ ] Use these measurements as the sole basis for spacing tuning.

### Depends On
- Items 40–41.


# PHASE VI — WORLDGEN DISTRIBUTION TUNING

## 43. Iteratively Tune Sparse Structures and Structure Essentials

- [ ] Tune Tier 0 spacing.
- [ ] Tune Tier 1 spacing.
- [ ] Tune Tier 2 spacing.
- [ ] Tune Tier 3 spacing.
- [ ] Tune village spacing separately.
- [ ] Keep megastructures rare.
- [ ] Increase small actionable content where required.
- [ ] Reduce excessive clustering.
- [ ] Prevent giant structures from appearing too close together.
- [ ] Configure Structure Essentials overlap controls.
- [ ] Configure biome-placement safeguards.
- [ ] Configure structure collision behavior.
- [ ] Generate samples after each meaningful change.
- [ ] Re-measure density.
- [ ] Re-measure discoverability.
- [ ] Re-measure Activity Ratio.
- [ ] Iterate:
  - [ ] configure.
  - [ ] generate.
  - [ ] measure.
  - [ ] inspect.
  - [ ] adjust.
- [ ] Stop tuning when target cadence from Item 21 is met within acceptable variance.

### Depends On
- Items 21, 40–42.


# PHASE VII — BUILD ENCOUNTERS BEFORE ENHANCING AI

## 44. Implement Encounter Orchestration and Test Composition Alone

- [ ] Add/configure In Control! if it passed Item 38.
- [ ] Implement only technically reliable rules.
- [ ] Build encounter rules for:
  - [ ] undead.
  - [ ] illagers.
  - [ ] caves.
  - [ ] spiders.
  - [ ] ocean.
  - [ ] Nether.
  - [ ] End.
- [ ] Configure spawn caps.
- [ ] Configure density.
- [ ] Configure ranged/melee composition where achievable.
- [ ] Configure elites only minimally at this stage.
- [ ] Prevent runaway spawning.
- [ ] Prevent easy infinite farms.
- [ ] Test encounter composition using existing mob AI first.
- [ ] Compare:
  - [ ] baseline mobs.
  - [ ] baseline mobs + better encounter composition.
- [ ] Determine how much of the combat problem is solved without AI modification.

### Depends On
- Items 25–27, 38, 43.


## 45. Evaluate AI and Elite Layers Incrementally

- [ ] Establish Composition-Only control:
  - [ ] existing AI.
  - [ ] encounter orchestration enabled.

- [ ] Test Improved Mobs separately.
  - [ ] equipment.
  - [ ] armor.
  - [ ] health.
  - [ ] damage.
  - [ ] difficulty scaling.
  - [ ] griefing.
  - [ ] MSPT.

- [ ] Test Enhanced AI separately.
  - [ ] ranged behavior.
  - [ ] zombie mining.
  - [ ] creeper breaching.
  - [ ] dungeon behavior.
  - [ ] base harassment.
  - [ ] engineering-build damage.
  - [ ] MSPT.

- [ ] Test Zombie Awareness only if a remaining perception/aggro problem exists.
  - [ ] sound.
  - [ ] light.
  - [ ] tracking.
  - [ ] encounter escalation.
  - [ ] base annoyance.
  - [ ] MSPT.

- [ ] Compare:
  - [ ] composition only.
  - [ ] composition + Improved Mobs.
  - [ ] composition + Enhanced AI.
  - [ ] any justified combination.

- [ ] Select the minimum AI stack that materially improves gameplay.
- [ ] Reject redundant AI systems.

- [ ] Test elite requirements after normal encounters are working.
- [ ] Evaluate Mob Champions only if necessary.
- [ ] Disable/constrain RPG-style legendary loot.
- [ ] Introduce commanders/minibosses only where they improve encounter pacing.

- [ ] Re-evaluate the need for dedicated boss mods.
- [ ] Do not add a boss ecosystem unless a documented remaining gap requires it.

### Depends On
- Item 44.


# PHASE VIII — MULTIPLAYER LOOT FOUNDATION BEFORE EXACT LOOT BALANCING

## 46. Implement Multiplayer Container and Persistence Rules

- [ ] Add Lootr if it passed Item 38.
- [ ] Verify:
  - [ ] YUNG containers.
  - [ ] WDA containers.
  - [ ] IDAS containers.
  - [ ] Dungeon Crawl containers.
  - [ ] vanilla structures.
  - [ ] modded containers.
- [ ] Identify unsupported containers.
- [ ] Decide which containers should be instanced.
- [ ] Decide which rewards remain shared.
- [ ] Test late-player access.
- [ ] Test multiple players opening the same dungeon loot.
- [ ] Measure economic multiplication.
- [ ] Test interaction with physically destroyed dungeons.
- [ ] Verify Item 24 persistence policy still works.
- [ ] Establish final multiplayer-loot semantics before assigning rare rewards.

### Depends On
- Items 24, 32, 41, 45.


# PHASE IX — FREEZE ENGINEERING INPUTS BEFORE EXACT REWARD IMPLEMENTATION

## 47. Freeze the Adventure-Relevant Engineering and Combat Stack

- [ ] Resolve outstanding engineering additions before exact engineering rewards are assigned.
- [ ] Decide final inclusion/exclusion of candidate engineering mods.
- [ ] Confirm final Create ecosystem relevant to adventure.
- [ ] Confirm final CC:Tweaked/peripheral ecosystem.
- [ ] Confirm final Aeronautics ecosystem.
- [ ] Confirm final train/logistics ecosystem.
- [ ] Confirm final combat ecosystem from Item 35.
- [ ] Confirm final dimension stack.
- [ ] Confirm final village stack.
- [ ] Update candidate reward inventory based on the actual retained mods.
- [ ] Ensure no soon-to-be-removed item is used as a progression reward.

### Depends On
- Items 34–35, 40, 45–46.


# PHASE X — BUILD THE ACTUAL PROGRESSION SYSTEM

## 48. Implement Loot, Discovery, Civilization, and Engineering Integration

### 48A. Implement Exact Loot Tables

- [ ] Convert Item 28 reward classes into actual item IDs.
- [ ] Define exact quantities.
- [ ] Define exact probabilities.
- [ ] Define exact structure-tier placement.
- [ ] Remove excessive generic loot.
- [ ] Remove duplicate Loot Integrations injections.
- [ ] Preserve useful expedition supplies.
- [ ] Add rare horizontal rewards.
- [ ] Add trophies.
- [ ] Add collectibles.
- [ ] Add engineering-related rewards.
- [ ] Ensure basic engineering remains ungated.

### 48B. Implement Renewability Rules

- [ ] Apply classifications from Item 29.
- [ ] Verify valuable rewards cannot accidentally become trivial mob farms.
- [ ] Verify structure rewards cannot be mass-extracted without intended interaction unless explicitly accepted.
- [ ] Test hopper/automation behavior.
- [ ] Test Create extraction behavior.
- [ ] Test CC:Tweaked/peripheral interaction where applicable.

### 48C. Implement Discovery Progression

- [ ] Add maps where feasible.
- [ ] Add structure leads.
- [ ] Add coordinate clues.
- [ ] Integrate cartographer/settlement discovery where useful.
- [ ] Ensure underground content is realistically discoverable.
- [ ] Avoid requiring admin commands.

### 48D. Integrate Civilization

- [ ] Make retained settlements useful for:
  - [ ] food.
  - [ ] trade.
  - [ ] maps.
  - [ ] information.
  - [ ] staging.
- [ ] Evaluate Guard Villagers only if civilization lacks defensibility.
- [ ] Test MCA interaction if retained.
- [ ] Avoid excessive NPC counts.

### 48E. Integrate Engineering and Logistics

- [ ] Create expedition uses for CC:Tweaked.
- [ ] Create expedition uses for aircraft.
- [ ] Create expedition uses for trains.
- [ ] Create expedition uses for factories.
- [ ] Create expedition uses for Create Big Cannons.
- [ ] Integrate Farmer's Delight provisioning.
- [ ] Test cargo pressure.
- [ ] Test portable storage.
- [ ] Preserve meaningful train-vs-aircraft differentiation.

### 48F. Implement Death and Failure Behavior

- [ ] Test You're in Grave Danger in:
  - [ ] small dungeons.
  - [ ] deep dungeons.
  - [ ] major structures.
- [ ] Test grave accessibility.
- [ ] Test retreat and return.
- [ ] Test vehicle-loss scenarios.
- [ ] Test partial dungeon clears.
- [ ] Confirm failure is costly but recoverable.

### Depends On
- Items 28–37, 46–47.


# PHASE XI — SYSTEM PERFORMANCE HARDENING

## 49. Validate Performance of the Final Candidate System

- [ ] Re-run idle MSPT.
- [ ] Re-run worldgen MSPT.
- [ ] Re-run dungeon-combat MSPT.
- [ ] Re-run entity tick profiling.
- [ ] Re-run pathfinding profiling.
- [ ] Re-run memory profiling.
- [ ] Re-run GC profiling.

- [ ] Test:
  - [ ] one explorer.
  - [ ] multiple explorers together.
  - [ ] multiple explorers in different directions.
  - [ ] loaded dungeon + loaded village.
  - [ ] multiple active dungeon groups.

- [ ] Test high-speed aircraft crossing fresh chunks.
- [ ] Test several aircraft exploring independently.
- [ ] Measure chunk-generation backlog.
- [ ] Measure server responsiveness.
- [ ] Determine sustainable travel speeds.

- [ ] Validate:
  - [ ] C2ME.
  - [ ] ServerCore.
  - [ ] Structure Layout Optimizer.
  - [ ] Fast Async World Save.
  - [ ] Chunky.
  - [ ] Simple Backups.

- [ ] Determine pregeneration strategy.
- [ ] Determine spawn-region pregeneration radius.
- [ ] Determine whether a world border is useful.
- [ ] Avoid pregenerating unreasonable aircraft-scale world areas.

- [ ] Test persistent-world growth.
- [ ] Measure:
  - [ ] region-file growth.
  - [ ] save time.
  - [ ] backup time.
  - [ ] backup size.
- [ ] Perform another real restore test.

### Depends On
- Items 43–48.


# PHASE XII — FULL GAMEPLAY VALIDATION

## 50. Run Early-, Mid-, Late-, and Mature-Server Validation

### 50A. Fresh-World / Early-Game Test

- [ ] Start from fresh spawn without admin knowledge.
- [ ] Test first-hour pacing.
- [ ] Test first structures.
- [ ] Test first small encounters.
- [ ] Test dungeon discoverability.
- [ ] Test early combat.
- [ ] Ensure major Tier 3 content is not routinely adjacent to spawn.
- [ ] Ensure players are not forced into high-tier encounters immediately.
- [ ] Measure early Adventure Activity Ratio.

### 50B. Mid-Game Test

- [ ] Establish basic Create infrastructure.
- [ ] Establish improved equipment.
- [ ] Establish first train network.
- [ ] Establish initial aircraft.
- [ ] Test regional discovery.
- [ ] Test Tier 2 dungeon cadence.
- [ ] Test preparation requirements.
- [ ] Test map/clue progression.
- [ ] Test return logistics.
- [ ] Verify engineering materially improves expeditions.

### 50C. Late-Game Test

- [ ] Establish advanced aircraft.
- [ ] Establish high-throughput factories.
- [ ] Establish advanced weapons.
- [ ] Establish mature CC:Tweaked infrastructure.
- [ ] Test Tier 3 expeditions.
- [ ] Test aircraft approach.
- [ ] Test roof entry.
- [ ] Test cannon breaching.
- [ ] Test tunnel bypass.
- [ ] Test mobile-base behavior.
- [ ] Test logistics.
- [ ] Verify underground content remains meaningful.
- [ ] Verify loot remains relevant after automation.

### 50D. Mature-Server Test

- [ ] Simulate a server months into progression.
- [ ] Assume:
  - [ ] known coordinates are shared.
  - [ ] aircraft are common.
  - [ ] rail networks exist.
  - [ ] factories provide abundant resources.
  - [ ] nearby structures have been visited.
- [ ] Test late joiners.
- [ ] Test Lootr effectiveness.
- [ ] Test physically altered old dungeons.
- [ ] Test whether distant expeditions remain worthwhile.
- [ ] Test whether infrastructure compresses adventure too far.
- [ ] Test whether rewards still matter.

### 50E. Exploit and Emergent-Engineering Audit

- [ ] Test automated loot extraction.
- [ ] Test spawner farms.
- [ ] Test elite farms.
- [ ] Test rare-drop farms.
- [ ] Test quarrying structures.
- [ ] Test moving valuable dungeon blocks.
- [ ] Test cannon bypasses.
- [ ] Test Create drill bypasses.
- [ ] Test hopper extraction.
- [ ] Test CC:Tweaked automation.
- [ ] Classify findings:
  - [ ] desirable emergent engineering.
  - [ ] harmless cheese.
  - [ ] economy-breaking exploit.
  - [ ] adventure-destroying exploit.
- [ ] Fix only the latter categories.

### 50F. Final Redundancy Audit

- [ ] Re-evaluate every retained structure mod.
- [ ] Re-evaluate every AI mod.
- [ ] Re-evaluate every difficulty mod.
- [ ] Re-evaluate every loot integration.
- [ ] Re-evaluate every village mod.
- [ ] Remove systems whose contribution is no longer distinct.
- [ ] Remove systems whose performance cost exceeds gameplay value.

### 50G. Regression Test

- [ ] Repeat representative baseline measurements.
- [ ] Verify targeted improvements actually occurred.
- [ ] Confirm no major regression in:
  - [ ] structure diversity.
  - [ ] exploration pacing.
  - [ ] worldgen.
  - [ ] server performance.
  - [ ] combat.
  - [ ] loot economy.
  - [ ] multiplayer fairness.
  - [ ] engineering progression.

### Depends On
- Items 1–49.


# PHASE XIII — ADVENTURE V1 RELEASE GATE

## 51. Validate Definition of Done and Freeze Adventure v1

### Adventure Identity

- [ ] Engineering remains the primary capability-progression system.
- [ ] Adventure gives engineering practical purpose.
- [ ] RPG elements remain subordinate.
- [ ] No spell/magic progression has re-entered unintentionally.
- [ ] No generic level-grind system is required.
- [ ] No legendary-loot treadmill dominates progression.

### Exploration

- [ ] Travel contains sufficiently frequent meaningful discoveries.
- [ ] Ambient structures improve world richness without overwhelming it.
- [ ] Small encounters adequately break up travel.
- [ ] Proper dungeons are neither excessively rare nor commonplace.
- [ ] Major expeditions remain memorable.
- [ ] Content repetition is within defined limits.
- [ ] Adventure Activity Ratio meets target ranges.

### Dungeon Quality

- [ ] Tier 2 dungeons provide meaningful traversal.
- [ ] Tier 3 expeditions provide meaningful preparation and logistics.
- [ ] Underground content provides a natural counterbalance to aircraft.
- [ ] Dungeons are not merely large decorated shells.
- [ ] Objective variety is sufficient.
- [ ] Repeat dungeon layouts do not become immediately stale.

### Encounter Quality

- [ ] Enemy compositions differ meaningfully by context.
- [ ] Difficulty comes mainly from encounters rather than inflated HP.
- [ ] Selected AI systems provide measurable value.
- [ ] No redundant AI overhaul remains.
- [ ] Elite encounters are meaningful.
- [ ] Bosses exist only if they genuinely add value.

### Engineering Freedom

- [ ] Mining remains useful.
- [ ] Breaching remains useful.
- [ ] Cannons remain useful.
- [ ] Vehicles remain useful.
- [ ] CC:Tweaked remains useful.
- [ ] Clever engineering solutions are allowed.
- [ ] Engineering cannot trivially delete the entire adventure loop.

### Loot and Economy

- [ ] Dungeon rewards remain valuable after factories exist.
- [ ] Basic engineering progression is not dungeon-gated.
- [ ] Rare rewards cannot be trivially industrialized unless intentionally designed.
- [ ] Loot inflation is controlled.
- [ ] Salvage economy is acceptable.
- [ ] Trophy/prestige rewards provide meaningful multiplayer value.
- [ ] Horizontal rewards meaningfully expand player options.

### Multiplayer

- [ ] Late joiners have viable adventure content.
- [ ] Loot depletion is adequately addressed.
- [ ] Physical dungeon persistence follows an intentional policy.
- [ ] Group play is viable.
- [ ] Solo play remains reasonably viable where intended.
- [ ] Per-player loot does not cause unacceptable economic multiplication.

### Transportation

- [ ] Walking retains an early-game role.
- [ ] Horses/boats retain local/regional utility.
- [ ] Trains retain high-capacity infrastructure value.
- [ ] Aircraft retain flexible long-range expedition value.
- [ ] Aircraft do not render trains irrelevant.
- [ ] Aircraft do not render all dungeons irrelevant.

### Civilization

- [ ] Settlements provide a clear gameplay purpose.
- [ ] Redundant village generators have been removed.
- [ ] NPC density remains acceptable.
- [ ] Settlements contribute to expedition logistics or discovery.

### Persistent Server

- [ ] Fresh-server progression works.
- [ ] Mid-game progression works.
- [ ] Late-game progression works.
- [ ] Mature-server progression remains viable.
- [ ] Known structure coordinates do not completely invalidate adventure.
- [ ] World size remains operationally manageable.
- [ ] Backups complete successfully.
- [ ] Restore procedure has been verified.

### Performance

- [ ] Idle MSPT is within target.
- [ ] Combat MSPT is within target.
- [ ] Worldgen MSPT is within target.
- [ ] High-speed aircraft exploration is sustainable.
- [ ] Expected concurrency is sustainable.
- [ ] Peak concurrency is understood.
- [ ] Memory behavior is acceptable.
- [ ] No candidate mod creates disproportionate tick cost.

### Documentation

- [ ] Record final mod list.
- [ ] Record exact versions.
- [ ] Record removed mods and rationale.
- [ ] Record all relevant configs.
- [ ] Record Sparse Structures settings.
- [ ] Record Structure Essentials settings.
- [ ] Record encounter rules.
- [ ] Record AI settings.
- [ ] Record difficulty settings.
- [ ] Record loot tables.
- [ ] Record reward matrix.
- [ ] Record structure matrix.
- [ ] Record discovery system.
- [ ] Record known exploits intentionally permitted.
- [ ] Record known limitations.
- [ ] Record benchmark results.
- [ ] Record tested player counts.
- [ ] Record backup/restore procedure.

### Final Freeze

- [ ] Tag configuration as `Adventure-v1`.
- [ ] Archive the exact server package/configuration.
- [ ] Preserve the corresponding test results.
- [ ] Do not add further adventure mods without identifying a specific measured deficiency.
- [ ] Require future changes to repeat the relevant subset of this validation process.

---

# FINAL DEPENDENCY SPINE

1. Design contract
2. Baseline freeze
3. Compatibility audit
4. Test environment
5. Measurement methodology
6. Config audit
7. Worldgen audit
8. Structure inventory
9. Initial classification
10. Density measurement
11. Pacing/repetition measurement
12. Discoverability measurement
13. Dungeon-quality measurement
14. Combat measurement
15. Loot/salvage measurement
16. Multiplayer persistence measurement
17. Performance baseline
18. Root-cause report
19. Final tier model
20. Transportation-scale model
21. Target cadence
22. Dungeon topology
23. Dungeon objectives
24. Persistence/repeatability
25. Difficulty
26. Encounter archetypes
27. Elite/boss philosophy
28. Loot economy
29. Renewability/automation
30. Engineering integration
31. Discovery
32. Multiplayer rules
33. Civilization
34. Dimensions
35. Combat boundaries
36. Destructibility/bypass
37. Preparation/failure
38. Candidate feasibility
39. Structure pruning experiments
40. Provisional content freeze
41. New dungeon integration
42. Re-measure combined worldgen
43. Density/overlap tuning
44. Encounter orchestration
45. AI/elite evaluation
46. Multiplayer loot foundation
47. Engineering/combat stack freeze
48. Exact progression implementation
49. Performance hardening
50. Full lifecycle validation
51. Adventure v1 freeze
