# Item 8: Baseline Structure-Family Inventory

**Current status:** `IN PROGRESS`. Family inventory integration is delivered;
local acceptance and preservation/history preparation are verified; reviewed main delivery remains open.

The exact136 retained candidates have been inventoried through runtime registries,
packaged data, frozen configuration, generation code/logs and preserved world
observations. The [canonical listing](../../evidence/item-8/inventory.json) contains
448 active families:408 registry families and40 nonregistry families. Its separate
other_registry_groups retains18 inactive/excluded registry groups. Together these
account for all887 runtime roots exactly once, with zero unassigned roots.

All448 active families carry the eleven Item8 attributes. Nonregistry attributes
are joined from the existing33 contribution records; injected components, aliases,
pools and templates are not counted as extra families. Original426 registry-group
rows were preserved unchanged by consolidation. The [evidence record](../../evidence/item-8/README.md)
contains reproduction commands and links to the authoritative source decisions.

Dimensions distinguish nominal template/connector geometry from preserved generated
examples, including padding and observation limits. Mob and loot sources distinguish
raw declarations, selected processor behavior, absent optional providers, natural
spawning and unresolved baseline defects. Source attribution is not measured enemy
population, loot yield, sightline distance, exploration pacing or working machinery.
These additional measurements are not an Item8 repair backlog.

The local requirement/evidence gate is verified. A clean tracked-file export with
freshly acquired pinned JARs and the restored registry capture passed all495 Item8
tests in122.06s. Changed-code lint/type checks pass. The current inventory separates
448 ASSESSED families and18 DISPOSITIONED registry groups from the item delivery
lifecycle. The [acceptance record](../../evidence/item-8/README.md) contains setup
commands, current inventory identity and the preserved earlier failed test result.

Preservation and history preparation are complete. Original source branches,
recovery tags, evidence references and verified backups remain preserved. The
[preservation record](../../evidence/item-8/preservation.md) links both history
mappings and the245 coherent milestones plus provenance increment. Subsequent
review fixes remain separate commits. [PR18](https://github.com/copeugne/mcpack/pull/18)
is the active delivery PR; PR17 was superseded without merging.

Remaining: finish PR18's clean Codex review loop, merge and verify main. Do not
repeat preservation, history reconstruction or accepted measurements. Item9 remains
dependency-blocked. Item7's explicit review exception is preserved in the execution
ledger and does not apply to Item8.

## Historical zero-mod report, superseded

The following report was introduced in `38ec6d9` for a zero-third-party-mod
baseline. Its completion decision and absent-mod claims do not describe the
current retained stack. They are preserved as historical context, not current
acceptance evidence or permission to advance downstream.

**Historical status claim:** `COMPLETE` (superseded)
**Historical baseline:** Minecraft 1.21.1 / NeoForge 21.1.249 / zero third-party mods
**Historical machine inventory:** `structure-inventory/vanilla-1.21.1-structure-families.json`

## Registry proof

The inventory is derived from the pinned runtime, not a wiki list or filename inference:

- `BuiltinStructures` supplies the exact structure constants and registry IDs.
- `BuiltinStructureSets` proves 20 placement sets.
- `Structures` supplies the exact 34 structure-to-biome-tag bindings.
- the embedded vanilla data pack verifies every declared loot table or wildcard prefix.

The validator found 34 runtime structures, 34 inventoried variants, 34 exact biome tags, 21 gameplay families and 20 placement sets. The family/set difference is intentional: Nether Fortress and Bastion are distinct gameplay families sharing the `nether_complexes` placement set. No runtime structure is missing or duplicated, every declared loot source resolves, and every required attribute is non-empty.

Pinned transformed server JAR SHA-256: `26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.

## Family summary

| Family | Variants | Dimension / placement | Hostility and mob source | Loot / spawner summary | Discoverability |
|---|---:|---|---|---|---|
| Pillager outpost | 1 | Overworld surface | hostile; pillager override + authored captives | outpost chest; no spawner | high silhouette |
| Mineshaft | 2 | Overworld underground/mixed | natural cave mobs + cave-spider spawners | minecart chests; cave spider | low; mesa can expose |
| Woodland mansion | 1 | dark-forest surface | authored illagers + natural darkness | mansion chest; conditional spider room | high silhouette, biome-obscured |
| Jungle temple | 1 | jungle surface/shallow | natural mobs + arrow traps | chest/dispenser loot; no spawner | foliage-obscured |
| Desert pyramid | 1 | desert surface/deep shaft | natural mobs + TNT trap | chest + archaeology | high in open desert |
| Igloo | 1 | snowy surface/optional basement | optional authored villager pair | igloo chest; no spawner | medium/low contrast |
| Shipwreck | 2 | ocean/beach | natural drowned nearby | map/supply/treasure; no spawner | low underwater, higher beached |
| Swamp hut | 1 | swamp surface | authored + piece-bounded witch/cat spawning | no chest/spawner | medium |
| Stronghold | 1 | deep Overworld | natural mobs + silverfish spawner | corridor/crossing/library | nearly invisible without leads |
| Ocean monument | 1 | deep ocean | guardian override + elder guardians | salvage, no chest/spawner | medium/high underwater |
| Ocean ruin | 2 | ocean floor/mixed | authored drowned + natural mobs | chests + archaeology | low/medium underwater |
| Nether fortress | 1 | Nether mixed | fortress spawn override + blaze spawners | nether-bridge chest; blaze | variable exposed/buried |
| Nether fossil | 1 | soul-sand-valley surface | natural mobs only | no loot/spawner | medium ambient cue |
| End city | 1 | outer End surface/tall | authored shulkers | End-city treasure; no spawner | high but remote |
| Buried treasure | 1 | coastal shallow underground | natural mobs only | one buried-treasure chest | invisible without map/knowledge |
| Bastion remnant | 1 | Nether mixed | authored piglins/brutes/hoglins + natural | four chest families; conditional magma cube | variable exposed/embedded |
| Village | 5 | Overworld surface | authored civilians; world-system raids | profession/house tables | generally high |
| Ruined portal | 7 | Overworld + Nether, mixed | natural mobs + authored block hazards | ruined-portal chest | high exposed, low buried |
| Ancient city | 1 | deep-dark underground | ordinary spawning suppressed; sculk-triggered Warden | city/ice-box loot | extremely low/no surface cue |
| Trail ruins | 1 | mostly buried Overworld | natural mobs only | common/rare archaeology | low/small surface cue |
| Trial chambers | 1 | Overworld underground | room-authored trial spawners; natural spawning suppressed | corridor/reward/supply/ominous tables | extremely low/no assured entrance |

The machine inventory supplies, for every family and variant: dimension, exact biome-tag key, approximate footprint, approximate vertical extent, hostility, mob source, loot-table source, generated spawners, authored-versus-natural enemy origin, discoverability and surface/underground classification.

## Tentative-mod families

WDA, Seven Seas, YUNG replacements/additions, IDAS, Integrated Stronghold/Villages, Moog, Explorify, Explorations, Repurposed Structures, AdoraBuild, CTOV, Towns & Towers, Better Village and Village Taverns are not installed. Their family counts are zero in the baseline and are not inferred from project pages. Each admitted candidate must generate its own registry-backed inventory and may change the total.

## Important observations for Item 9

- Vanilla already includes five village variants and seven ruined-portal variants; variants are not automatically distinct gameplay families.
- Trial chambers are the clearest vanilla proper-dungeon candidate.
- Strongholds, ancient cities, bastions, fortresses, monuments and End cities have major-objective potential but differ sharply in encounter authoring.
- Mineshafts are large but may be mechanically shallow/repetitive; size is not a tier.
- Buried treasure and trail ruins are discovery/excavation systems, not combat dungeons.
- Villages are civilization, not ambient landmarks or dungeons.
- Loot-free structures can have meaningful salvage, objective or encounter value; Item 15 evaluates that separately.

These are inputs, not final tier decisions. Item 9 owns classification and redundancy flags.

## Historical exit decision, superseded

All structures actually present in the baseline are enumerated exactly once at registry level and grouped into clear gameplay families with every requested attribute. Candidate-only families remain explicitly absent. Item 9 may now classify the 21 baseline families provisionally.
