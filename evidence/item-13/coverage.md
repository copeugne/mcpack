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

## IDAS variant scope

All 24 included IDAS families remain in scope. Ordinary root names equal their
family names in the `idas:` namespace, with two exceptions: Ancient Portal has
roots `ancient_portal/ancient_portal` and `ancient_portal/nether_ancient_portal`;
Sunken Ship has `sunken_ship/sunken_ship` and `sunken_ship/sunken_ship_coral`.
There are 26 roots. Use the exact accepted inventory grouping rationale and
per-root definitions, plus the bound pool traces and family-specific
`evidence/item-8/sources/idas-*-assessment/README.md` where linked. No optional mod
or inactive compatibility pool is re-enabled to make a sample more complete.

| Family | Material design alternatives | Dimension | Coverage and failure treatment |
| --- | --- | --- | --- |
| abandoned_lighthouse | One narrow capped tower | Overworld | One generated arrangement; vertical access and reused guild loot do not make it a guild building |
| abandonedhouse | `abandonedhouse`, `abandonedhouse2` | Overworld | Both roofed arrangements, with different zombie/villager/spider sources and loot; preserve the second template's missing-ID entity |
| ancient_mines | One entrance/room/hall assembly | Overworld | Validate the connected chain and hall network; missing `ancient_mines_entrance2` branch stays absent if rejected, rather than inventing a second entrance |
| ancient_portal | Overworld pair, Nether pair | Overworld, Nether | Each two-piece portal in its own dimension; different land-search/underground placement, spawn overrides and loot remain material |
| apothecary_abode | One paired abode | Overworld | Both connected sections; illusioner/pillager residents and spawners, not a presumed peaceful house |
| brickhouse | One house/path/windmill assembly | Overworld | Terrain-matching path and processor-specific windmill; a detached house alone does not establish site access |
| castle | `castle1`, `castle2`, `castle3` with matching foundations | Overworld | All three main designs. First two also have procedural plains-village extensions; include their reachable normal/zombie settlement branches in selection. Third has no village connector |
| collectors_museum | One main/lower museum assembly | Overworld | Both vertically joined components, internal content and final access; enormous template envelope is not room count |
| desert_pyramid | One procedural entrance/hall/room system | Overworld | At least two distinct-seed assemblies, plus unrepresented material room/goal mechanisms. Missing villager pool and source loot defects remain dispositions |
| farmhouse | Ordinary with path, abandoned without path | Overworld | Both alternatives. Civilian residents versus zombie-villager spawners, different path attachment and furnishings cannot be averaged away |
| frozen_crypt | One entrance/crypt pair | Overworld | Both sections; optional troll declaration does not create a retained-runtime enemy |
| haunted_manor | Packaged default manor only | Overworld | Frozen namespace mismatch rejects the intended piece-2/4 attachment. Measure the actually saved result and retain detached source content separately; inactive Ice and Fire compatibility templates are excluded by the verified loader condition |
| labyrinth | One entrance/floor/tomb chain | Overworld | Fixed numbered components and floor-specific processor behavior; inactive Ice and Fire compatibility branch is excluded, legacy loot references remain unchanged |
| necromancers_spire | One four-component spire | Nether | Over-lava placement at absolute Y31, branching attachments and conditional wraith override; optional soul-vulture declaration remains source-only potential unless supported by the frozen runtime |
| nexus | Default, blue, prismarine, red, sculk, white | Overworld | All six single-template arrangements. Shared shape does not merge barrel-position, height or sculk differences; raw pig spawner NBT and ineffective declared loot assignment need their existing processor dispositions |
| pillager_fortress | One eight-component fortress | Overworld | Connected numbered sections, authored illagers/ravagers and spawners; optional entities remain separate |
| ruined_church | One gabled hall/tower ruin | Overworld | One arrangement, no source spawner or authored entity; assess quiet/dead rooms without inventing an encounter |
| ruined_fort | One narrow broken fort | Overworld | One arrangement, distinct from church and inhabited castle variants |
| ruins_of_the_deep | One entrance/tunnel/two-ruin chain | Overworld | All four connected stages; quiet tunnel may have necessary access purpose and is not automatically a dead room |
| sunken_ship | `sunken_ship`, `sunken_ship2`, `sunken_ship_coral` | Overworld | All three hull alternatives across two roots. Spawner-randomizing versus empty processor and coral/shark references are material even with equal envelopes |
| tinkers_citadel | One main building with three attachments | Overworld | Branching site and elevated vault attachment, distinct from the serial workshop; source machinery is not proven operable |
| tinkers_workshop | One entrance plus seven workshop sections | Overworld | Complete descending serial route and final-vault access; keep per-stage spawner/reward content |
| windswept_shrine | One three-section shrine with corresponding bottoms | Overworld | Six pieces are a connected assembly, not six design alternatives; measure actual section access |
| wizard_tower | Purple, red, yellow paired towers | Overworld | Each main/bottom pair. Purple/yellow source spawners differ from spawner-free red; bottom zoglin and processor effects remain explicit |

This identifies 38 named main-layout/dimension alternatives within the 24 families,
counting a connected fixed assembly once. This number excludes procedural extension
outcomes and component permutations; it is not the final sample denominator. Castle1
and Castle2 each need two distinct-seed site samples for their village extensions;
all three main layouts remain required. A missing normal/zombie or other material
extension mechanism requires an explicit remaining coverage disposition, not a
claim that two random samples necessarily cover it. For other fixed layouts, one
complete saved example per listed alternative is the initial architectural minimum.
Desert Pyramid has the procedural minimum above. The actual selected examples and
resource total must be recorded before processing.

The distinction between incomplete raw geometry and a completely observed broken
baseline is essential here. Complete saved chunks showing the frozen Haunted Manor
connector rejection can support a quality result about that truncated building.
Partially generated distant chunks cannot. Neither warrants repairing the frozen
configuration or replacing the failed sample with a more attractive one.

## Moog variant scope

This section covers all included `mes`, `mns`, `mss` and `mvs` families, using the
accepted inventory's per-family grouping, exact root definitions, template content
and connector derivations. Reuse [Moog generator source](../item-8/sources/moog-generator-code/README.md)
and [arena processor source](../item-8/sources/moog-arena-processors/README.md),
not template totals as room topology. Registry IDs below are explicit because
several families combine materially different roots.

| Family | Required roots/design alternatives | Dimension | Required distinction |
| --- | --- | --- | --- |
| mes:enderkeep_courtyard | mes:enderkeep_courtyard | End | Single courtyard layout |
| mes:enderwatch_tower | mes:enderwatch_tower | End | Single tower layout, vertical access rather than envelope height |
| mes:mega_ship | mes:mega_ship, mes:mega_ship_basic, mes:mega_ship_crashed, mes:mega_ship_crashed_2, mes:mega_ship_crashed_deepslate, mes:mega_ship_deepslate, mes:mega_ship_deepslate_2, mes:mega_ship_deepslate_3 | End | Eight finite hull/middle/end assemblies with different side/upper attachments; three wreck roots versus five airborne roots, with distinct terrain and content |
| mes:monolith | mes:monolith, templates monolith_1, monolith_2, monolith_3 | End | Three independent whole-template alternatives, each required despite equal horizontal envelopes |
| mes:mystical_archway | mes:mystical_archway | End | Single archway layout retained as a shallow-form comparison |
| mes:phantom_citadel | mes:phantom_citadel | End | Single authored citadel layout |
| mes:starlight_voyager | mes:starlight_voyager | End | Single ship layout; reuse the identified full Item 7 candidate before new generation |
| mns:arena | mns:small_arena, mns:large_arena | Nether | Separate bounded-court layouts, different vertical galleries, encounters and rewards |
| mns:circle_ruin | mns:circle_blackstone, mns:circle_nether_brick | Nether | Layout, spawner and loot differences, not a purely cosmetic material pair |
| mns:dragon_arena | mns:dragon_arena | Nether | Fixed sculptural dragon/platform assembly with ordinary/trial spawners and vaults; not a claim of a live dragon boss |
| mns:giant_skull | mns:giant_skull | Nether | One articulated head/jaw layout with reward and spawner source |
| mns:large_house_1 | mns:large_house_1 | Nether | One long hall/tower design, using the selected 1.21.1 template |
| mns:medium_house | mns:medium_house, mns:medium_house_2 | Nether | Two gabled layouts and different spawner payloads; empty entity objects must not become invented default mobs |
| mns:mega_fortress | mns:mega_fortress | Nether | Procedural corridor/stair/room network, including boundary-exempt pools and the version-selected start |
| mns:nether_tower | mns:nether_tower | Nether | One multilevel furnished tower, with accessible floors validated individually |
| mns:warped_dome | mns:warped_dome | Nether | One empty-source dome retained for shallow-form/usable-space assessment |
| mss:arena | mss:arena | Overworld | Numbered assembly with trial/vault mechanisms. The 1_21_9 template paths are inactive on frozen 1.21.1, not omitted live variants |
| mss:castle_ruin | mss:castle_ruin | Overworld | One broad low island ruin with encounter/reward content |
| mss:castle_tower | mss:castle_tower | Overworld | Tower plus corresponding top, one connected site |
| mss:desert_pyramid | mss:desert_pyramid | Overworld | Base, side and top are one pyramid assembly |
| mss:jungle | mss:jungle | Overworld | Finite main/east/south/upper site, not interchangeable forest-island decoration |
| mss:large_tower | mss:large_tower | Overworld | Full base/lower/side/top complex and its real access links |
| mss:leaf_hollow | mss:leaf_hollow | Overworld | Main mound and projecting sides, with inhabited interior |
| mss:mangrove | mss:mangrove | Overworld | Deep tapered island plus upper piece; interior and fall/external approach assessed separately |
| mss:muddy_water_hole | mss:muddy_water_hole | Overworld | Bowl-like main/side/upper encounter site |
| mss:mushroom | mss:mushroom | Overworld | One low multi-lobed furnished encounter island |
| mss:red_sand | mss:red_sand | Overworld | Main and projecting side, with distinct terrace access |
| mss:small_deepslate_house | mss:small_deepslate_house | Overworld | One gabled dwelling/island with pillager/spawner source |
| mss:small_tower | mss:small_tower | Overworld | One vertically fragmented ruin composition; separated fragments do not automatically form reachable floors |
| mss:taiga | mss:taiga | Overworld | Main conifer island and upper component |
| mss:volcano | mss:volcano | Overworld | Main crater and five attached side pieces, with actual attachment/route continuity |
| mvs:castle_ruins | mvs:castle_ruins | Overworld | One linked masonry ruin without authored enemies/spawners |
| mvs:cathedral | mvs:cathedral | Overworld | Procedural building/lower/corridor network; excluded cathedral_start/corridor_8 templates stay inactive and wrong-namespace loot references remain unchanged |
| mvs:large_warped_tower | mvs:large_warped_tower | Overworld | Base/side turret plus finial; warped material does not make this a Nether root; unresolved empty spawner payloads stay explicit |
| mvs:mine_with_campsite | mvs:mine_with_campsite | Overworld | Fixed upper/lower site and villager alternatives, distinct from the procedural mineshaft |
| mvs:mineshaft | mvs:mineshaft | Overworld | Procedural entrance/corridor/intersection/stair network, including boundary-exempt corridor_overflow |
| mvs:ocean_tower | mvs:ocean_tower | Overworld | One cylindrical aquatic tower; direct drowned/guardian entities versus physical spawners |
| mvs:small_pillager_tower | mvs:small_pillager_tower | Overworld | One open vertical platform tower; route links must be validated |
| mvs:tiered_tower | mvs:jungle_tower, mvs:red_tower | Overworld | Jungle base/bottom/top versus red body/top; different encounters, loot and terrain constraints |

Denominators: 39 families, 50 roots, 52 named root/whole-template alternatives.
The extra two are Monolith's three layouts under one root. Each dimension is
retained separately: End for MES, Nether for MNS and Overworld for MSS/MVS.
None of the Soaring island roots is reassigned to the Aether based on appearance.
The eight Mega Ship roots have finite connector-derived assemblies, so repeating
middle pieces is not assumed from the word modular.

The proposed architectural minimum is one complete generated example per named
alternative, except two distinct-seed examples for each of Mega Fortress,
Cathedral and MVS Mineshaft. This gives 55 proposed examples before any necessary
unrepresented component/mechanism or terrain supplement. Sample IDs, extraction
bounds, actor/model support and resource totals are still pending. Saved-block
coverage and the actual outcome of versioned/conditional processors must be
checked before asserting a room graph or encounter potential for a sample.

## Repurposed Structures variant scope

All 13 included families retain all 91 registry roots. In this table each entry
is a root suffix: the exact root is `repurposed_structures:<family>_<suffix>`.
A blank dimension column means no compatible dimension in the accepted per-root
biome intersection, not a failed experiment. The source is each family's
`grouping_decision/variants`, `dimension/biome_compatible_by_structure`, template
trace and linked `repurposed-*-assessment` record in Item 8. The complete roots
and dimensions are also preserved in the intake.

| Family | Overworld suffixes | Nether suffixes | End suffixes |
| --- | --- | --- | --- |
| ancient_city | ocean | nether | end |
| bastion | underground | | |
| city | overworld | nether | |
| fortress | jungle | | |
| mansion | birch, desert, jungle, mangrove, oak, savanna, snowy, taiga | | |
| mineshaft | birch, dark_forest, desert, icy, jungle, ocean, savanna, stone, swamp, taiga | basalt, crimson, nether, soul, warped | end |
| monument | desert, icy, jungle | nether | |
| outpost | badlands, birch, desert, giant_tree_taiga, icy, jungle, mangrove, oak, ocean, savanna, snowy, taiga | basalt, crimson, nether_brick, soul, warped | end |
| pyramid | badlands, dark_forest, flower_forest, giant_tree_taiga, icy, jungle, mushroom, ocean, snowy | nether | end |
| shipwreck | | crimson, nether_bricks, warped | end |
| stronghold | | nether | end |
| temple | ocean, taiga | nether_basalt, nether_crimson, nether_soul, nether_warped, nether_wasteland | |
| village | badlands, bamboo, birch, cherry, dark_forest, giant_taiga, jungle, mountains, mushroom, oak, ocean, swamp | crimson, warped | |

Root coverage alone is insufficient. Preserve these architectural and mechanical
alternatives within each applicable root:

| Family | Required within-root coverage |
| --- | --- |
| ancient_city | Procedural city assembly in each dimension; authored residents, physical spawners and natural overrides stay distinct. Dimension-specific source reward/encounter content must not be borrowed from vanilla Ancient City |
| bastion | Four starting designs: units, skeleton-horse stable, treasure and bridge. The packaged starts pool selects `units/air_base`, `skeleton_horse_stable/air_base`, `treasure/big_air_full`, and `bridge/starting_pieces/entrance_base` under `repurposed_structures:bastions/underground/`. Each starts a procedural assembly; two generic bastion examples cannot establish all four |
| city | Procedural tower/bridge network, preserving Overworld villagers versus Nether authored enemies and separate feature-selected bow skeletons |
| fortress | Procedural jungle fortress, including reward/archaeology content and the conditional water-dependent drowned feature; dry absence is not a failed enemy source |
| mansion | Procedural mansion generator for each `mansion_type`, with room selectors and one-level child/fallback attachments. Equal generator code does not make biome-specific component contents identical |
| mineshaft | Procedural network for each environment, with feature-selected minecart loot and processor-selected spawners retained separately; water/lava, support and external access are sample conditions |
| monument | Custom room graph and ordered fitters per root; at least two generated graphs per root. Nether's fixed Y30 placement differs from terrain-weighted surface variants |
| outpost | Tower/camp site per root, including cage and other material attachments. End feature shulkers and different natural overrides are not a universal pillager count |
| pyramid | Complete body/pit arrangement per root, plus Jungle's hidden room. Nether selects its single `pyramids/nether` template. Spawner replacement, infested blocks and archaeology require their own source and saved-state attribution |
| shipwreck | Three single-template Nether hulls and all 18 End fragment/position alternatives. Partial hull alternatives carry different map/supply/treasure nodes and access; the one accepted End example does not cover them all |
| stronghold | Procedural room/corridor system in both dimensions; portal-room versus general spawners, End feature shulkers and low-elevation access stay distinct |
| temple | One selected compact template per root, with its own spawner replacement and literal/processor-appended loot treatment; no universal trap-operation claim |
| village | Procedural village per root. Normal/zombie branches where reachable, Nether inhabitants and aquatic layouts must remain material coverage cases, not averaged into a peaceful-village assumption |

The Bastion start alternatives are read directly from
`data/repurposed_structures/worldgen/template_pool/bastions/underground/starts.json`
in the accepted packaged JSON catalog (member SHA-256
`060b3c17ce4b74d6274f38af8f66a019860aca7c720450bfdadabb5301432a7e`).
End wreck alternatives are the exact 18 template IDs in
`pool-traces-content.json.gz#/structures/repurposed_structures:shipwreck_end/templates`;
these are selected fragment/position alternatives, not 18 new families. No new
source extractor is needed to preserve those already enumerated IDs.

Apply the procedural minimum of two distinct-seed examples per root/design for
cities, Bastion starting designs, fortress, mansions, mineshafts, monuments,
strongholds and villages. Outposts require the complete tower/camp arrangement
and every unrepresented material attachment, rather than a detached tower.
Fixed temple, pyramid and wreck alternatives initially require one complete saved
example each. Source enemy/loot rolls are assessed as potential under their exact
root and processor; a missing architectural or consequential mechanism alternative
still needs a concrete gap and minimal experiment before dependent claims.
This is a design coverage policy, not a completed sample list or a runtime budget.
