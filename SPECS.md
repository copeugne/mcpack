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
  - [ ] provisional encounter sites per 1,000 chunks for automated Items 10 and 11; do not claim observed fights.
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

For Items 10 and 11, apply the user-authorized [automated measurement scope](evidence/item-10/methodology-amendment.md). No human sessions, recording or blind operators are required. The frozen Item 5 v1 collection matrix remains historical for these consumers; automated sampling must be predeclared separately.

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

- [x] Test:
  - [x] Tectonic.
  - [x] Terralith.
  - [x] Biomes O' Plenty.
  - [x] Regions Unexplored.
  - [x] TerraBlender.
  - [x] Lithostitched.
  - [x] BetterEnd.
  - [x] YUNG.
  - [x] WDA.
  - [x] IDAS.
  - [x] Integrated structures.
  - [x] Moog.
  - [x] Explorify.
  - [x] Explorations.
  - [x] Repurposed Structures.
  - [x] CTOV.
  - [x] Towns & Towers.

- [x] Inspect for:
  - [x] fragmented biomes.
  - [x] tiny biomes.
  - [x] unnatural terrain transitions.
  - [x] buried structures.
  - [x] floating structures.
  - [x] cliff intersections.
  - [x] bad underwater placement.
  - [x] overlapping structures.
  - [x] overlapping villages.
  - [x] failed placements.
  - [x] impossible biome restrictions.
  - [x] excessive terrain modification around structures.

- [x] Separate:
  - [x] cosmetic issues.
  - [x] gameplay issues.
  - [x] performance issues.
  - [x] outright generation failures.

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
- [ ] Measure provisional actionable-candidate locations (C and T1 through T4) per 1,000 chunks.
- [ ] Measure provisional encounter sites (T1 through T4) per 1,000 chunks, not observed fights.
- [ ] Measure provisional proper dungeons (exclusive T2) per 1,000 chunks.
- [ ] Measure provisional major expeditions (exclusive T3) per 1,000 chunks; report T4 objectives separately.
- [ ] Measure village density.
- [ ] Measure average nearest-neighbor distance by category.
- [ ] Measure clustering.
- [ ] Measure large empty regions.
- [ ] Compare biomes.
- [ ] Compare seeds.
- [ ] Determine Sparse Structures' contribution to the observed distribution.

### Depends On
- Items 5–9.


## 11. Measure Automated Route Opportunities and Repetition

Apply the [automated measurement scope](evidence/item-10/methodology-amendment.md).
No human sessions, recordings or blind operators are required. Execute only after
Item 10 delivery and the Items 2 through 10 cross-item audit pass.

- [ ] Predeclare automated routes, endpoints and capability assumptions for walking, horse and boat travel.
- [ ] Record failed and infeasible routes with explicit transport limitations.
- [ ] Measure route-adjacent candidate locations and geometric visibility proxies.
- [ ] Record provisional actionable candidates, encounter sites, dungeons, major expeditions and villages along each route.
- [ ] Measure gaps between candidate locations and family repetition over fixed distances.
- [ ] Measure route opportunity coverage with an explicit geometric numerator and denominator.
- [ ] Report modeled travel costs and repeated-family intervals with declared assumptions and uncertainty.
- [ ] Separate placement density from geometric visibility and modeled accessibility.
- [ ] Keep human recognition, actual fights, meaningful-interaction time, enjoyment and human Adventure Activity Ratio explicitly NOT MEASURED. Do not present automated proxies as observed human gameplay.

### Depends On
- Item 10.


## 12. Measure Structure Discoverability

Apply the separately user-authorized [Item 12 inspection and automated assessment
protocol](evidence/item-12/protocol.md). Architectural recognition, entrance cues
and realistic `/locate` dependence are evidence-supported assessments. Human
recognition and discovery rates remain NOT MEASURED; no human trials are required.

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

# POST-BASELINE DELIVERY: SEVEN WORK PACKAGES

The user authorized this consolidation on 2026-09-10. Items 1 through 18 above
remain unchanged. Execute the following packages only after Item 18 is COMPLETE;
editing this plan does not start Item 19 or authorize skipping the baseline.
Legacy numbers 19 through 51 remain requirement IDs and evidence references,
not 33 separate administrative tasks. The
[amendment and source mapping](evidence/item-19/plan-consolidation.md) document
provenance, retained obligations and verification.

## Execution and acceptance rules

- Work packages A through G are the delivery units, in that order. Within each,
  follow the numbered requirements and their retained dependencies below. A
  successful launch never substitutes for a gameplay, compatibility or performance
  gate. Do not install a downstream candidate before its prerequisite decision.
- Use one authoritative report per package, linking existing evidence and affected
  configuration/code. Record decisions, rationale, assumptions, uncertainty,
  failures and dispositions there as they become established. Existing item evidence
  remains authoritative; link it instead of copying or repeating it. Use evidence
  directories under the package's first legacy item number for new shared evidence.
- Define the smallest complete outcome and validation surface for the current
  package. Design work produces decisions and acceptance targets, not premature
  implementation or new measurement systems. Ratify material product choices with
  the user together in a concrete proposal; do not invent taste or target values.
- Each recommendation must connect a documented baseline problem to a desired
  outcome, feasible mechanic, tested difference and tradeoff. Named mods below are
  candidates, not guaranteed additions. Retain the smallest stack that solves the
  measured problems. Preserve earlier compatibility exclusions unless explicitly
  reopened through their affected gates.
- Share samples, runs and reports where their declared identity and method satisfy
  multiple requirements. Re-measure only affected claims after a change; do not
  repeat baseline audits, create a protocol/validator per checkbox, or investigate
  detail that cannot change an acceptance decision. Quantitative claims still need
  measurement or supported models, with observations and assumptions distinguished.
- Deliver coherent implementation/evidence milestones and narrow fixes. One package
  may need multiple reviewable commits or PRs; a package is not permission for an
  omnibus change. Do not require a separate PR, report or completion-record commit
  for every legacy number. Required regression, review/fix, completed clean Codex
  thumbs-up, merge and verified main delivery gates remain in force under AGENTS.md.
- A package is COMPLETE only when every listed requirement and internal gate passes,
  qualifying evidence is durably linked, failures have dispositions and downstream
  assumptions are updated. Mark constituent IDs complete from that same evidence;
  consolidation does not waive any original substantive requirement. UNKNOWN and
  blocked inputs do not become passed by grouping them.

## Package A. Decide the adventure system (19-37)

Input: completed Item 18 and the preserved baseline/design contract.
Deliverable: one ratified design report with target values, policy decisions,
source evidence and candidate acceptance criteria. No mod installation or tuning.

### 19. Define the Final Adventure Structure Taxonomy

Assign every retained family one primary role: Tier 0 ambient landmark (visual,
short interaction, little/no combat, low rewards); civilization (villages,
settlements, taverns, trade and expedition staging); Tier 1 small encounter
(approximately 5-15 minutes, low/moderate pressure, breaks travel monotony);
Tier 2 proper dungeon (20-45 minutes, multiple rooms/encounters, meaningful
traversal/reward); Tier 3 major expedition (30-90+ minutes, preparation,
group-friendly logistics); Tier 4 world objective (dimension progression,
server-scale/endgame expeditions). These are design targets, not baseline timings.

### 20. Define the Transportation-Scale Model

Set practical speeds, exploration scale and acceptable travel durations to each
tier for foot, horse, boat, train and aircraft. Preserve foot for local exploration,
horse/boat for local/regional travel, trains for persistent high-throughput regional
logistics and aircraft for flexible long-range expeditions. Aircraft must not make
trains pointless; trains must not replace exploration. Use this model for spacing.

### 21. Define Target Adventure Cadence

Set average intervals for visual/actionable discoveries, combat, Tier 1/2/3 content
and Tier 4 rarity; target Adventure Activity Ratio and dead-travel percentage.
Specify early/mid/late game and each transport mode separately. Do not solve poor
cadence by making giant structures common.

### 22. Define Dungeon Topology Requirements

Set proper-dungeon minimums: useful rooms, meaningful interior traversal, empty-room
percentage, verticality, branching, depth, encounter spacing and breathing space.
Define miniboss/finale placement and distributed loot; avoid one easily reached
chest holding all value. Large dungeons need multiple gameplay phases. Underground
layouts must counterbalance aircraft while preserving destructibility and engineering.

### 23. Define Dungeon Objective Variety

Allow deep-chamber access, defended-zone clearance, object/intelligence recovery,
commander defeat, branching searches, hostile-infrastructure destruction and
multi-component retrieval where appropriate. Avoid making every visit enter/kill/
loot/exit, excessive scripted quests and single-room checks. Distribute objectives
and support reasonable breaching, alternative routes and sandbox solutions.

### 24. Define Dungeon Persistence and Repeatability Policy

Decide one-time/repeatable behavior by tier and whether destroyed walls/spawners,
mined shortcuts, bridges and breached entrances persist. Define later-player
experience, Tier 1/2 repeatability, permanent Tier 3 changes and visible expedition
history. Separate loot freshness from physical/encounter freshness; Lootr does not
imply physical resets.

### 25. Define the Difficulty Model

Use composition first: roles, numbers, ranged pressure, equipment/armor, positioning,
terrain, chokepoints, reinforcements and elites. Set tier-specific and solo/duo/3-4
player expectations. Limit raw health/damage increases and extreme distance scaling;
avoid late-game damage sponges. Engineering must meaningfully reduce difficulty.

### 26. Define Enemy Role and Encounter Archetypes

Define basic/armored melee, ranged, fast/flanking, heavy, defensive, elite, commander
and environmental-threat roles. Build easy/medium/hard/expedition compositions for
undead, illager, cave, spider, ocean, Nether, End and dimension-specific contexts.
Prefer tactical variety over merely adding species.

### 27. Define Elite, Miniboss, and Boss Philosophy

Define elites/minibosses/true bosses, reward rules and maximum stat inflation.
Prefer faction/location commanders; avoid enormous HP pools and boss progression
replacing engineering. Keep siege/engineering useful. Determine whether dedicated
boss mods are needed, deferring selection until ordinary encounters are tested.

### 28. Define the Loot Economy

Define tier placement, rarity and value for supplies, ordinary materials, equipment,
intelligence, engineering materials/capabilities, cosmetics, trophies and collectibles.
Avoid late-game bulk iron/copper/gold as primary rewards and excessive diamonds/books.
High-value rewards must be non-automatable, hard to mass-produce, unique, prestigious
or horizontally useful. Foundational engineering stays normally craftable without
mandatory rare-RNG gates.

### 29. Define Reward Renewability and Automation Rules

Classify every planned valuable reward as renewable/non-renewable, farmable/non-farmable,
structure-limited/player-limited as applicable. Assess mob farms, Create, hoppers/pipes
and mass production after one discovery. Decide desirable automation versus damage
to the adventure loop; prevent unintended industrial-scale rare drops. Prefer reward
redesign over arbitrary automation bans.

### 30. Define Engineering and Adventure Integration

Define expedition roles for Create, Aeronautics, Steam 'n' Rails, CC:Tweaked, Create
Big Cannons, Diesel Generators and potential future integrations. Evaluate specialized
ammunition, schematics, sensors, navigation components, machine parts, vehicle upgrades/
cosmetics, tools and trophies as horizontal rewards; explain why they expand options.
Exclude presses, mixers, basic bearings/trains/computers and foundational Create
mechanisms from dungeon gating. Named ecosystems remain subject to compatibility.

### 31. Define Discovery and Navigation Progression

Define discovery for every tier using maps, clues, coordinates, cartographers,
documents and structure-to-structure leads. Support local discovery -> clue -> dungeon
-> major clue -> expedition. Use Item 12 evidence; avoid requiring /locate or making
GUI structure selectors the normal player experience.

### 32. Define Multiplayer Expedition and Loot Rules

Define solo, duo, 3-4 player and larger-group viability/behavior; group, personal,
shared and globally rare reward policies. Avoid linear multiplication of rare
engineering rewards with player count without punishing cooperation. No mandatory
classes: roles emerge through equipment, vehicles, logistics, computers, weapons
and engineering. Account for persistent dungeon modification.

### 33. Define Civilization and Settlement Roles

Set civilization density and safe/hostile rhythm. Define villages/settlements as
food resupply, trade, maps/rumors, staging and transport hubs. Determine whether
multiple village generators are necessary; separate worldgen decisions from later
NPC/gameplay integration.

### 34. Define Dimension Roles

Decide whether Aether/Deep Aether fit the identity, identify fantasy progression
conflicts with the no-magic direction, and define BetterEnd and End progression.
Classify dimensions as optional expeditions, milestones or endgame objectives,
not disconnected RPG campaigns. Record loot/engineering economy consequences.

### 35. Define Combat-Mod Boundaries

Audit Better Combat, Simply Swords, Simply More, Archers, Rogues, Armory and Arsenal
against accepted exclusions and available evidence. Identify supernatural effects,
magical equipment and excessive scaling. Ratify grounded/fantastical non-magical/
hybrid aesthetics within the design contract. Decide provisional retention before
loot implementation; weapons must not displace engineering progression. Listing a
previously rejected mod is not authorization to re-enable it.

### 36. Define Destructibility, Breaching, and Automation-Bypass Policy

Test/define acceptable hand mining, drills, explosives, contraptions, cannons, roof/
side/tunnel access, chest/hopper extraction, remote peripherals and portable storage.
Distinguish earned engineering from accidental total content bypass. Prefer depth,
distributed objectives/loot and multiple encounters over universal unbreakable blocks.

### 37. Define Expedition Preparation, Failure, and Recovery

Set food, ammunition, tools, repairs, storage, navigation, fuel/power and portable
equipment requirements. Define retreat, death, aircraft crash, ammunition exhaustion,
partial-clear persistence, return and grave recovery. Failure must be meaningful and
recoverable without death spirals or making exploration irrational.

Gate: decisions and targets for all 19-37 are ratified, mutually consistent, supported
by the baseline and sufficient to accept/reject candidates. Reuse one decision table;
do not turn these topics into nineteen separate studies or implementation projects.

## Package B. Select a feasible provisional stack (38-40)

Input: Package A. Deliverable: candidate/retention decisions with controlled comparison
evidence and a versioned provisional manifest, including rejection reasons.

### 38. Perform Early Candidate-Mod Feasibility Screening

Verify actual Minecraft 1.21.1 NeoForge builds, dependencies, server/client side,
launch compatibility, configuration and required mechanics for Dungeon Crawl, Lootr,
In Control!, Improved Mobs, Enhanced AI, Zombie Awareness, Mob Champions and Guard
Villagers. Verify reliable In Control! conditions, especially structure-aware/adjacent
spawning. Separate desired rules from available mechanics. Reject candidates that
cannot solve a documented problem; unsupported builds fail before integration.

### 39. Run Controlled Structure-Redundancy Experiments

Use a full-stack control and identical seed/radius variants removing candidates
individually: Moog's Voyager/Structures/Soaring, Explorify, Explorations, Repurposed
Structures, AdoraBuild, Better Village and other Item 18 overlaps. Test overlapping
village generators equivalently. Compare visual diversity, actionable density,
repetition, uniqueness, worldgen cost, overlap and adventure value. Every retained
family must justify itself. Reuse a comparison run across these outputs.

### 40. Freeze the Provisional Content and Worldgen Stack

Decide retained/removed structure, village, dimension and provisional combat-content
mods; resolve incompatible versions. Explain removals and retained overlaps. Freeze
the manifest before worldgen tuning. This is provisional, not the v1 freeze; later
evidence may justify removal.

Gate: 38 feasibility passes for each proposed candidate; 39 comparisons support 40's
choices. No startup-only acceptance or selection based solely on more content.

## Package C. Fill the dungeon gap and tune distribution (41-43)

Input: Package B and the topology/persistence/cadence decisions. Deliverable: accepted
worldgen stack and configuration, with before/after measurements against Item 21.

### 41. Integrate and Evaluate the Proposed Underground Dungeon Layer

Add Dungeon Crawl to a controlled test branch only after feasibility passes. Check
startup and generation with Tectonic, Terralith, BOP, Regions Unexplored and the
retained structure stack. Test terrain integration, entrance discovery, playable
depth, layout repetition, completion duration, enemies, loot, destructibility,
aircraft relevance and surface-bypass resistance; measure generation cost and density
before custom spacing. Accept only if it fills the documented Tier 2/3 topology gap;
reject generic added volume. Preserve a rejection and resolve the gap before proceeding.

### 42. Re-Measure the Combined Provisional Worldgen Stack

Generate representative seeds with the pruned stack and accepted dungeon layer.
Compare baseline structure/actionable/Tier 1/2/3/village density per 1,000 chunks,
repetition, discoverability and Adventure Activity Ratio. Identify remaining dead
zones and excess density. These combined-stack results are the sole basis for tuning.

### 43. Iteratively Tune Sparse Structures and Structure Essentials

Tune Tier 0/1/2/3 and village spacing separately: keep megastructures rare, add small
actionable opportunities where needed, reduce clustering and giant neighbors. Configure
overlap, biome-placement and structure-collision safeguards. After meaningful changes,
generate, measure density/discoverability/Activity Ratio, inspect and adjust. Stop when
Item 21 cadence meets its defined targets within acceptable variance.

Gate: accepted dungeon layer -> combined measurements -> distribution tuning, in that
order. Demonstrate the target improvement without concealing overlap or performance
failures. Do not tune spacing around content that has yet to be accepted.

## Package D. Build and evaluate encounters (44-45)

Input: Package C and difficulty/role/boss decisions. Deliverable: tested encounter
rules and the minimum justified AI/elite stack, with configuration and comparisons.

### 44. Implement Encounter Orchestration and Test Composition Alone

Add/configure In Control! only if feasible; use reliable rules for undead, illager,
cave, spider, ocean, Nether and End encounters. Set caps, density and achievable
ranged/melee composition, with minimal elites initially. Prevent runaway spawning
and easy infinite farms. Compare baseline against composition changes using existing
AI first; establish how much this alone solves before adding AI systems.

### 45. Evaluate AI and Elite Layers Incrementally

Keep the composition-only control. Test Improved Mobs separately for equipment,
armor, health/damage, scaling, griefing and MSPT; test Enhanced AI separately for
ranged behavior, zombie mining, creeper breaching, dungeon behavior, base harassment,
engineering damage and MSPT. Test Zombie Awareness only for a remaining perception/
aggro gap, including sound/light/tracking, escalation, base annoyance and MSPT.
Compare individual layers and only justified combinations; select the minimum stack
with material gameplay benefit and reject redundancy. After ordinary encounters
work, evaluate Mob Champions only if needed, constrain RPG legendary loot, and add
commanders/minibosses only for pacing. Revisit boss mods only for a documented gap.

Gate: composition-only result precedes AI comparisons; ordinary encounters precede
elites/bosses. Selected layers must demonstrate value and acceptable shared-server cost.

## Package E. Implement rewards and expedition systems (46-48)

Input: Package D and the economy, persistence and engineering policies.
Deliverable: frozen item-providing stack and tested gameplay implementation.

### 46. Implement Multiplayer Container and Persistence Rules

Add Lootr only if feasible. Check YUNG, WDA, IDAS, Dungeon Crawl, vanilla and modded
containers; record unsupported cases. Decide personal versus shared rewards. Test
late arrivals, concurrent dungeon looting, economic multiplication and physically
destroyed dungeons. Verify Item 24 policy. Freeze multiplayer-loot semantics before
assigning rare rewards.

### 47. Freeze the Adventure-Relevant Engineering and Combat Stack

Resolve engineering additions and inclusion/exclusion. Confirm the actual retained
Create, CC:Tweaked/peripheral, Aeronautics, train/logistics, combat, dimension and
village ecosystems. Update reward candidates from this manifest; do not assign
progression rewards to soon-to-be-removed items. This gate precedes exact item IDs.

### 48. Implement Loot, Discovery, Civilization, and Engineering Integration

Implement the following coherent increments in the existing paths, each with its
affected regression check before dependent work. They share the package report,
not one mixed implementation commit or six separate administrative projects.

- **48A, loot:** translate Item 28 classes to exact item IDs, quantities, probabilities
  and tier placement. Remove excess generic loot and duplicate Loot Integrations
  injections; retain supplies and add horizontal engineering rewards, trophies and
  collectibles while leaving foundational engineering ungated.
- **48B, renewability:** enforce Item 29 classifications; test mob farms, mass extraction,
  hoppers, Create and applicable CC:Tweaked/peripherals. Unintended trivialization
  fails; explicitly accepted automation remains permitted.
- **48C, discovery:** implement feasible maps, leads, coordinates and settlement/
  cartographer clues. Underground content must be discoverable without admin commands.
- **48D, civilization:** implement food/trade/maps/information/staging functions.
  Evaluate Guard Villagers only if defense is lacking; test MCA if retained and
  constrain NPC counts.
- **48E, engineering/logistics:** give computers, aircraft, trains, factories and
  cannons expedition uses; integrate Farmer's Delight provisioning. Test cargo and
  portable storage while preserving train/aircraft differentiation.
- **48F, recovery:** test You're in Grave Danger in small/deep/major dungeons,
  grave accessibility, retreat/return, vehicle loss and partial clears. Failure must
  remain costly but recoverable.

Gate: container semantics -> final providers -> exact implementation. Every 48A-F
increment has working evidence and affected regression results, not merely designs.

## Package F. Validate performance and the complete lifecycle (49-50)

Input: Package E. Deliverable: one candidate validation report joining performance,
gameplay, persistence, exploit dispositions and baseline regression evidence.

### 49. Validate Performance of the Final Candidate System

Re-run idle/worldgen/combat MSPT, entity/pathfinding, memory and GC profiling. Test
one explorer, groups together/apart, dungeon plus village, and multiple dungeon groups.
Test high-speed aircraft and several independent aircraft; measure chunk backlog,
responsiveness and sustainable travel speeds. Validate C2ME, ServerCore, Structure
Layout Optimizer, Fast Async World Save, Chunky and Simple Backups where retained.
Set pregeneration strategy/spawn radius and whether a border helps; avoid unreasonable
aircraft-scale pregeneration. Test persistent region-file growth, save/backup time,
backup size and a real restore.

### 50. Run Early-, Mid-, Late-, and Mature-Server Validation

Use one planned scenario matrix with explicit actors and observed/model boundaries;
this consolidation does not authorize replacing the required gameplay tests with
source inspection. Cover all of the following:

- **50A, fresh/early:** fresh spawn without admin knowledge, first-hour pacing,
  structures/small encounters, discovery, combat and early Activity Ratio. Major
  Tier 3 content must not routinely neighbor spawn or force immediate high-tier combat.
- **50B, mid:** basic Create, improved equipment, first rail network/aircraft; regional
  discovery, Tier 2 cadence, preparation, map/clue progression and return logistics.
  Engineering must materially improve expeditions.
- **50C, late:** advanced aircraft/weapons, high-throughput factories and mature
  computers; Tier 3, aircraft/roof entry, cannon/tunnel bypass, mobile bases and
  logistics. Underground content and rewards must remain meaningful after automation.
- **50D, mature:** simulate months of progression with shared coordinates, common
  aircraft, established rails, abundant factories and visited structures. Test late
  joiners, Lootr, altered dungeons, distant expeditions, adventure compression by
  infrastructure and continued reward value.
- **50E, engineering/exploits:** test automated loot, spawner/elite/rare-drop farms,
  quarrying, moving valuable blocks, cannons/drills, hoppers and computers. Classify
  desirable engineering, harmless cheese, economy-breaking and adventure-destroying
  exploits. Fix the latter two, preserving earned sandbox solutions.
- **50F, redundancy:** re-evaluate structures, AI, difficulty, loot integrations and
  village mods. Remove non-distinct contributions and costs exceeding gameplay value.
- **50G, regression:** repeat representative baseline measurements and demonstrate
  targeted improvements without major regressions in diversity, pacing, worldgen,
  performance, combat, economy, multiplayer fairness or engineering progression.

Gate: 49 performance passes before 50 full validation; material fixes repeat affected
scenarios. Every lifecycle and regression domain passes its targets, with failures
resolved and raw evidence retained before release consideration.

## Package G. Accept and freeze Adventure v1 (51)

Input: Package F and all prior requirements. Deliverable: accepted release record,
exact versioned server/configuration archive, preserved tests and Adventure-v1 tag.

### 51. Validate Definition of Done and Freeze Adventure v1

Verify from the accepted evidence, without repeating unchanged tests:

- **Identity:** engineering is primary; adventure gives it purpose; RPG elements are
  subordinate. No unintended magic/spells, mandatory level grind or dominant
  legendary-loot treadmill.
- **Exploration/dungeons:** meaningful discoveries and small encounters break travel;
  ambient content enriches without overwhelming; proper dungeons are neither too rare
  nor common; major expeditions remain memorable. Repetition and Activity Ratio meet
  targets. Tier 2 traversal, Tier 3 preparation/logistics, underground aircraft balance,
  objective variety and replay variation pass; large shells do not count as quality.
- **Encounters:** context-specific compositions drive difficulty, not inflated HP.
  AI adds measurable value without redundant overhauls; elites are meaningful and
  bosses exist only when they add value.
- **Engineering:** mining, breaching, cannons, vehicles and computers remain useful;
  clever solutions are allowed without trivially deleting the entire adventure loop.
- **Economy:** rewards remain useful after factories; foundational engineering is
  ungated; rare-reward industrialization is intentional; inflation and salvage are
  acceptable; trophies/prestige and horizontal rewards offer multiplayer value/options.
- **Multiplayer:** late joiners have content; loot depletion and physical persistence
  follow policy; group and intended solo play are viable; personal loot does not
  multiply the economy unacceptably.
- **Transport/civilization:** foot, horse/boat, trains and aircraft retain their defined
  roles; aircraft erase neither trains nor dungeons. Settlements serve logistics/
  discovery, village redundancy is removed and NPC density remains acceptable.
- **Persistent operations:** fresh/mid/late/mature progression works despite shared
  coordinates. World size is manageable, backups succeed and restores are verified.
- **Performance:** idle/combat/worldgen MSPT, fast-aircraft exploration, normal
  concurrency and memory meet targets; peak concurrency is understood; no mod creates
  disproportionate tick cost.
- **Documentation:** record exact mod versions/removals and reasons; configs including
  Sparse Structures/Structure Essentials; encounter/AI/difficulty rules; loot tables,
  reward/structure matrices, discovery, intentionally permitted exploits, limitations,
  benchmarks/player counts and backup/restore procedure.

Gate: all definition-of-done domains pass; tag configuration Adventure-v1, archive the
exact server package/configuration and preserve matching tests. Add no further
adventure mods without a measured deficiency; future changes repeat the relevant
validation subset. Required clean review, merge and verified main delivery still
precede declaring release complete.

## Retained dependency order

Items 1-18 retain their existing order and requirements. The deterministic continuation
is A -> B -> C -> D -> E -> F -> G. Within packages, retain these original dependencies;
a range includes every numbered requirement in it. This is an execution map, not
another set of completion tasks.

| Requirement | Depends on |
| --- | --- |
| 19 | 18 |
| 20 | 11-12, 19 |
| 21 | 18-20 |
| 22 | 13, 19, 21 |
| 23 | 22 |
| 24 | 16, 22-23 |
| 25 | 14, 19, 22-24 |
| 26 | 25 |
| 27 | 25-26 |
| 28 | 15, 19, 25-27 |
| 29 | 28 |
| 30 | 28-29 |
| 31 | 12, 19-23, 28 |
| 32 | 24, 28-31 |
| 33 | 9, 19, 21, 31 |
| 34 | 1, 19, 28-30 |
| 35 | 1, 25-30 |
| 36 | 22-24, 29-30 |
| 37 | 24-25, 30, 32, 36 |
| 38 | 18-37 |
| 39 | 8-18, 33, 38 |
| 40 | 34-35, 38-39 |
| 41 | 22-24, 38-40 |
| 42 | 40-41 |
| 43 | 21, 40-42 |
| 44 | 25-27, 38, 43 |
| 45 | 44 |
| 46 | 24, 32, 41, 45 |
| 47 | 34-35, 40, 45-46 |
| 48 | 28-37, 46-47 |
| 49 | 43-48 |
| 50 | 1-49 |
| 51 | All prior requirements and the definition of done above |
