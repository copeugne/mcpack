# Item 13 material variants and sample coverage

Status: IN PROGRESS. The complete inclusion/exclusion population is [intake.json](intake.json).
This record resolves material variants within that population before selecting and
processing their samples. A scoped design is not yet a measured design. No full
sampling matrix or expensive expansion is authorized by this unfinished record.

## Adorabuild variant scope

All IDs in this table use the `adorabuild_structures:` namespace. Dimension labels
mean `minecraft:overworld`, `minecraft:the_nether` and `minecraft:the_end`.
Each listed registry root is retained as its own material alternative. The existing
source decisions establish layout, encounter, access or reward differences, not
merely different filenames. No root is discarded because it is absent in Item 10.

Sources are the exact `families/<family>/grouping_decision` records in the accepted
Item 8 inventory, their `variants/<root>/definition` and `rationale`, and
`structures/<root>` in `evidence/item-8/sources/pool-traces-content.json.gz`.
The latter has SHA-256 `703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5`.
Dimension scope is the per-root evidence already retained in the intake.
These are direct inspections of accepted sources, not another classification audit.

| Family | Material roots | Dimension | Sampling distinction that must be preserved |
| --- | --- | --- | --- |
| ancient_palace | ancient_palace_1 | End | Multilevel columned building, upper window band and ladder |
| ancient_palace_hall | ancient_palace_2 | End | Broad stepped-roof hall and ladder, separate from the first palace |
| basalt_chambers | basalt_chambers_large_1 | Nether | Modular network; empty, debris, blaze and tripwire/magma component roles. Missing `minecraft:basalt_chambers/chambers` pool can truncate assembly and must remain a measured limitation |
| blackstone_bastion | blackstone_bastion_medium_1, blackstone_bastion_medium_2, blackstone_bastion_small_1 | Nether | Square, elongated and stepped layouts, piglin/brute and chest/trapped-chest differences |
| blackstone_bastion_towers | blackstone_bastion_medium_3 | Nether | Central and surrounding towers, distinct vertical compound |
| blackstone_temple | blackstone_temple_small_1 | Nether | Open-sided gold-bearing shrine; retain as a shallow-form comparison |
| buried_sand_castle | sand_castle_small_1, sand_underground_castle_1 | Overworld | Different buried depth/layout and lava versus TNT/pressure-plate ingredients; inspect actual mechanism connectivity |
| crimson_hall | crimson_house_medium_2 | Nether | Broad fenced hall with hoglin/brute source content |
| crimson_tower_house | crimson_house_medium_1 | Nether | Stacked form, lever/lamp and different access |
| dark_oak_mansion | dark_oak_mansion_medium_1 | Overworld | Broad furnished illager residence and ladder |
| end_house | end_house_medium_2, end_house_small_1, end_house_small_2 | End | Entrance/roof layouts differ; first two author shulkers, third does not |
| end_raised_house | end_house_medium_1, end_house_medium_3 | End | Raised rooms; roof opening, windows, ladder and ender-chest differences |
| end_ship | end_ship_small_1 | End | Compact deck/frame and authored shulker; effective access must be measured |
| end_temple | end_temple_large_1, end_temple_small_1 | End | Larger layout additionally authors end crystal and different contents |
| mountain_mine | mountain_mine_1, mountain_mine_2 | Overworld | Ladder/timber versus rail/minecart access; equal envelopes do not establish equivalent traversal |
| nether_fortress | nether_fortress_large_1 | Nether | Modular towers/stairs/bridges, alternative tower heights and reward-bearing components |
| nether_fortress_courtyard | nether_fortress_large_2 | Nether | Low enclosed courtyard and authored fortress enemies |
| nether_fortress_wart_house | nether_fortress_medium_1 | Nether | Roofed crop-bearing building; natural override differs from authored entities |
| nether_temple | nether_temple_medium_1 | Nether | Tiered shrine, lava/fire/gold and fortress spawn override |
| ocean_bubble | ocean_bubble_1 | Overworld | Bounded underwater sculk installation; no inferred Warden encounter |
| ocean_temple | ocean_temple_medium_1, ocean_temple_medium_2 | Overworld | Raised roof versus projecting entrance, underwater guardian-spawn context |
| prison | prison_large_1, prison_small_1 | Overworld | Different footprint, guards/captives and additional large-design residents |
| red_sand_temple | red_sand_temple_medium_1 | Overworld | Low open-window hall without authored encounter/reward nodes, retained as shallow-form comparison |
| sand_pyramid | sand_pyramid_1 | Overworld | Trapped-chest/piston/lava ingredients require actual topology and trigger assessment |
| watercraft | dark_oak_ship_1, mangrove_ship_1, oak_ship_1, spruce_ship_1 | Overworld | Deck arrangements differ; illager, civilian and stray alternatives all remain in scope |

Denominators: 25 canonical families and 38 registry-root alternatives. The accepted
pool traces select one template for each of 36 roots. The two exceptions are basalt
chambers (seven selected components, one missing pool) and modular Nether fortress
(eight selected components). These counts distinguish fixed source arrangements
from procedural assembly; they are never room counts or proof of playable links.

For the 36 fixed arrangements, the minimum proposed generated coverage is one
complete occurrence per root. For the two procedural roots, propose two occurrences
from distinct seed roles, preserving different assemblies and failures. This yields
40 proposed occurrences before any necessary terrain or mechanism supplement.
It is a minimum design sample, not a population uncertainty bound. Texture variation
is not an automatic extra occurrence; water, interrupted assembly or changed access
that invalidates the modeled route must be separately resolved. Both civilian ship
alternatives remain because their layouts are material alternatives within the
included mixed family, not evidence for classifying every ship as hostile.

Exact selected occurrence IDs, extraction envelopes, supported movement/encounter
models and resource totals are still required before this batch runs. Existing
baseline and prior generated examples take precedence over an additional experiment.
A forced placement, if necessary, must retain the correct custom root, dimension,
terrain/height conditions and frozen identity, and cannot claim natural frequency.
The missing basalt pool is not permission to repair or tune upstream configuration.

## Other current scopes and remaining work

The [compact representative](pilot/report.md) retains six small-dungeon shell sizes
and three themes as source alternatives, with two generated cases so far. The
[three non-registry scopes](README.md#non-registry-variants-and-reference-correction)
identify their feature/lifecycle routes and existing central-End evidence.

All other included families still require explicit material-variant resolution,
concrete sample selection and measurement integration. This document will be updated
in place; an unresolved variant is not excluded or declared source-only complete.

## WDA and Seven Seas variant scope

The 35 included `dungeons_arise` roots and five included
`dungeons_arise_seven_seas` roots each retain their canonical family name as the
registry-root name. No root alias or extra family is introduced. The following
scope comes from the accepted inventory's `grouping_decision`, `dimension`,
`approximate_footprint`, `mob_source`, `generated_spawners` and
`loot_table_source`, with exact alternatives in the bound pool trace
`structures/<root>` and `template_contents/<template>` records. Reuse the
[WDA source derivations](../item-8/sources/wda-provider-scope/README.md).

Sampling terms below are specific to design coverage, not a quality score:

- Fixed assembly: inspect at least one complete generated assembly in each listed
  dimension. Aligned authored sections are parts of that assembly, not extra rooms.
  Equal source envelopes alone do not prove equal playable topology.
- Procedural assembly: inspect at least two complete generated assemblies from
  different seed roles per listed dimension. Missing/unreadable generated chunks
  censor topology coverage. A fully saved assembly truncated by an established
  frozen connector or missing-component defect is instead a valid baseline result
  with that defect retained. Never count the absent intended pieces as rooms.
- Component coverage: retain every named architectural alternative as a required
  variant input. Generated sample selection must expose each alternative, or give
  its exact remaining gap before a minimal additional experiment. Do not multiply
  every independent loot/spawner roll into an invented family. Interactions that
  change connectivity, hazards or objectives cannot be disposed of as cosmetics.

Every selected assembly also needs source-supported assessment of all reachable
encounter/reward mechanisms, including the exact nested NBT in the accepted
records. A skeleton rider, potion passenger, evoker fangs, trial spawner and direct
saved entity cannot be collapsed into one ordinary skeleton workload. Source
alternatives remain potential; generated sample counts use only their saved data.
A missing component is not an observed empty room or a reason to repair the frozen
pack. These requirements may increase the minimum sample count once actual saved
component membership is inspected; no full processing budget is asserted yet.

All unqualified family names in the next table use `dungeons_arise:`.

| Family/root | Dimension | Required architectural variant coverage | Material conditions to preserve |
| --- | --- | --- | --- |
| abandoned_temple | Overworld | Procedural temple assembly | Authored illusioner/skeletons versus conditional stray override; buried and exposed portions |
| aviary | End | Fixed three-layer assembly | Five different spawner alternatives, crystal content and external vertical access |
| bandit_towers | Overworld | Procedural tower/bridge assembly | Rocket/passenger and different spawner payloads; actual bridge continuity |
| bandit_village | Overworld | Procedural village assembly | Hoglin/passenger and rocket mechanisms; missing `bandit_village_deco_3` remains a failed source reference |
| bathhouse | Overworld | Component coverage: six bases, four middles, seven tops | Source height combinations differ; curse dispenser/cloud and three spawner alternatives are not interchangeable decoration |
| ceryneian_hind | Overworld | Fixed three-section ship | Surface-relative -16 placement, reward-bearing hull without authored enemy source in its selected templates |
| coliseum | Overworld | Fixed four-quadrant arena | Phantom/skeleton spawner has its own long interval/count; entity-drop reward differs from container loot |
| foundry | Overworld | Procedural underground assembly | Missing `underworld/foundry/foundry_corridor_gears` pool; retain resulting omissions and machinery access |
| giant_mushroom | Overworld | Two separate assemblies: red and twins | Matching connector names keep these layouts separate; one sample of either does not cover the other |
| greenwood_pub | Overworld | Procedural pub/lower-room assembly | Surface-relative -18 placement and buried lower access |
| heavenly_challenger | Overworld, End | Fixed six-section ship in each dimension | Absolute Y200, mounted/flying enemy sources and access over distinct terrain/void context |
| heavenly_conqueror | Overworld, End | Fixed four-quadrant ship in each dimension | Absolute Y200 and four spawner alternatives; no inferred ground entrance |
| heavenly_rider | Overworld, End | Fixed two-layer ship in each dimension | Absolute Y200, mounted/flying sources including a distinct 2400/4800-tick interval |
| illager_campsite | Overworld | Procedural terrain-following camp | Street/tent continuity, direct illager residents and zombie-villager decoration source; no physical spawner substitution |
| illager_corsair | Overworld | Fixed two-section ship | Starting from either half translates the same authored assembly; evoker/pillager residents and vindicator spawner remain separate |
| illager_fort | Overworld | Fixed enclosing assembly plus all nine internal room alternatives | Room alternatives and four saved-entity alternatives; equal room envelopes do not establish equal contents |
| illager_galley | Overworld | Fixed two-section ship | Half-start translation is not a new design; direct pillager and vindicator spawner, with retained arrow/equipment differences |
| illager_windmill | Overworld | Fixed two-section core plus procedural terrain-matching fields | Core access and attached field continuity must be assessed together; one isolated core is incomplete site coverage |
| infested_temple | Overworld | Fixed main assembly plus five level and ten room alternatives | Five trial-spawner and three vault alternatives; final objectives and trial/vault state stay explicit |
| jungle_tree_house | Overworld | Two anchor alternatives: main-start and roots-start | Same connected source shape, different surface-relative placement because vertical start piece changes; direct husk/skeleton residents |
| keep_kayra | Overworld | Fixed main assembly | Connector-specific high/middle/low spawners, incompatible horizontal connector, fixed harmful-potion inventory and decorative/passive residents |
| kisegi_sanctuary | Overworld | Fixed main/lower/middle/final top sections plus three `top_room_0` alternatives | Twelve trial-spawner and four vault alternatives; selected top-room variant must be identified |
| lighthouse | Overworld | Fixed two-section tower | Vertical access and reward distribution without invented authored enemies |
| mechanical_nest | Overworld | Procedural elevated assembly | Missing decoration pool, bridge terminator 6 and spawner 6 references; preserve actual access gaps |
| mining_complex | Overworld | Procedural mining assembly | Fixed low anchor with tall architecture/blimp components; underground flag does not establish total burial |
| mushroom_house | Overworld | Component coverage: four bottoms and five tops joined to roots | Shared connector envelope does not establish equal interior contents or routes |
| mushroom_mines | Overworld | Fixed eight-section assembly | Two authored layers and conditional encounter/reward attachment content |
| mushroom_village | Overworld | Fixed central house plus procedural perimeter houses | All reachable small-house alternatives; collisions/failed attachments affect actual branches |
| plague_asylum | Overworld | Procedural underground assembly | Six different spawner alternatives, including fangs; ordinary block spawner does not imply an evoker mob |
| scorched_mines | Overworld | Procedural surface-anchored mine | Buried route continuity and three distinct enemy payloads |
| shiraz_palace | Overworld | Fixed three-layer assembly | Fourteen reachable spawner alternatives and their passenger/equipment differences |
| small_blimp | Overworld | Fixed ladder and two hull sections | No matching connector supports an invented repeating ladder; three spawner payloads and fixed dispenser contents require separate treatment |
| thornborn_towers | Overworld | Procedural towers/hanging architecture | Missing hanging-bridge terminator; flying/mounted and other spawner alternatives |
| typhon | Overworld | Fixed three-section ship | Ocean-floor-relative -4 placement and waterlogging differ materially from Hind; no authored enemy source in selected templates |
| undead_pirate_ship | Overworld | Fixed two-section ship | Direct skeletons and nested skeleton/carrier/passenger spawners; carrier types do not replace hostile passenger counts |

The five Seven Seas rows use `dungeons_arise_seven_seas:`. Each has one main hull
with subordinate spawner components, all in the Overworld. One generated hull per
root is the architectural minimum; its complete room/connector graph remains to be
validated. The selected spawner alternatives and all nested NBT remain required
source inputs, not five universal enemy-per-room assumptions.

| Family/root | Main hull template | Material content distinction |
| --- | --- | --- |
| corsair_corvette | corsair_corvette/corsair_corvette_0 | Skeleton and silverfish source types |
| pirate_junk | pirate_junk/pirate_junk_0 | Illusioner, pillager and vindicator source types |
| small_yacht | small_yacht/small_yacht_0 | Pillager/vindicator source types; missing `small_yacht_spawner_3` template remains an unresolved authored alternative |
| unicorn_galleon | unicorn_galleon/unicorn_galleon_0 | Bat, skeleton and zombie source types; bats are not automatically hostile enemies |
| victory_frigate | victory_frigate/victory_frigate_0 | Bat, hoglin, illager, skeleton and zombie source types; retain nested riders and attributes rather than count base IDs alone |

Dimension denominator: 40 canonical families, 40 roots and 43 root/dimension
combinations. The three extra combinations are the Heavenly designs in the End.
Aviary is End-only in the accepted biome intersection. This is independent of
Item 12's Overworld observation frame. The source's inactive Mining System is
not reintroduced as a family. Fishing Hut, Merchant Campsite and Wishing Well
retain their existing exclusion decisions in the complete intake.

No WDA/Seven Seas quality score, source-to-room conversion or new experiment is
accepted by this scope table. Concrete existing sample IDs, whole-envelope block
availability, component membership, actor models and resource costs remain the
next required selection work.
