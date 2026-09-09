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

The remaining sections resolve the other included families. Concrete sample
selection and measurement integration are still pending. Update this document
in place; an unresolved sample is not excluded or declared source-only complete.

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

## Aether and YUNG generator scopes

Each family below keeps the same-named registry root except Better Mineshafts,
whose thirteen roots are explicitly listed afterward. Dimension Aether means
`aether:the_aether`. Source authority is the accepted inventory's grouping and
required attributes, including generator code and packaged alternatives bound by
that family's evidence. All source pools/templates remain component evidence until
saved blocks establish playable connections.

| Family | Dimension | Required design/component scope |
| --- | --- | --- |
| aether:bronze_dungeon | Aether | Procedural room/tunnel network with Slider goal, chest/mimic alternatives and conditional surface ruins. At least two distinct-seed layouts; ordinary melee timing is not a supported Slider model |
| aether:silver_dungeon | Aether | Fixed multi-floor temple architecture with internal floor/wall/door/stair/chest alternatives, trapped-floor Valkyries and Queen goal. Retain chest/mimic selection. Unselected test_door is not a required live variant |
| aether:gold_dungeon | Aether | Island/boss-room/tunnel/cave assembly and Sun Spirit goal. Cave carving and goal access must be validated; a generic sword workload cannot replace its encounter mechanics |
| deep_aether:brass_dungeon | Aether | Four rotated lower/upper quadrants, five room designs and corresponding boss forms, with one selected boss quadrant. Require each material room/boss form as component coverage; cloud bedding is terrain/support evidence |
| betterdeserttemples:desert_temple | Overworld | Procedural entrance, puzzle, parkour, throne and room alternatives. At least two distinct-seed layouts plus unrepresented material puzzle/goal mechanisms; conditional Pharaoh behavior and processor-selected enemies need their own inputs |
| betterdungeons:skeleton_dungeon | Overworld | Procedural skeleton dungeon with its room/connector alternatives, authored spawner placement and reward distributions. At least two distinct-seed layouts, not a graph made from jigsaw choices |
| betterdungeons:small_dungeon | Overworld | Six shell sizes and three skeleton/spider/zombie themes. The two-case pilot covers only the 9x7 skeleton and 9x5 spider samples. Remaining shell/theme and material loot-pile differences must be resolved before family coverage passes |
| betterdungeons:spider_dungeon | Overworld | Custom big/small tunnels, nests and egg rooms. At least two distinct-seed layouts with every material space/encounter role covered; no fabricated start pool |
| betterdungeons:zombie_dungeon | Overworld | Procedural rooted zombie assembly and natural override, with internal room/reward alternatives. At least two distinct-seed layouts and separate saved spawner versus natural population claims |
| betterfortresses:fortress | Nether | Keep, bridge, hall, room and blaze-platform assemblies. At least two distinct-seed layouts; depth/altitude/Create-dependent alternatives remain conditional inputs and missing halls/hall_4 stays a frozen source defect |
| betterjungletemples:jungle_temple | Overworld | Alternative start shells, entrance/stairs/rooms and material puzzle mechanisms. At least two distinct-seed layouts plus uncovered shell/mechanism alternatives; inactive crocodile data is not a required generated enemy |
| bettermineshafts:mineshaft | Overworld | Thirteen material/support/decoration configurations of the custom branching generator. Two distinct-seed layouts per root, with configuration-specific environment and spawner inputs preserved |
| betteroceanmonuments:ocean_monument | Overworld | Room/shrine/main-section assembly and variable supports; at least two distinct-seed layouts. Water traversal, guardian source distinctions and actual external bypass routes need separate model treatment |
| betterstrongholds:stronghold | Overworld | Room/stair/passage system, portal goal and source spawner-removal/reward transformations. At least two distinct-seed layouts; missing spiral_stairs reference is not repaired. Retain the separate Integrated Stronghold family |

Better Mineshafts roots are `bettermineshafts:mineshaft_` plus each of:
`acacia`, `desert`, `dripstone`, `ice`, `jungle`, `lush`, `mesa`, `mushroom`,
`oak`, `overgrown`, `red_desert`, `spruce`, `spruce_snowy`. These are all thirteen
accepted roots, not every possible biome or every random corridor. Compare each
configuration's actual generated support/route state; common generator code alone
does not establish equal external access or encounter composition.

There are 14 families and 26 roots in this section. No additional source mob type
is inferred from a pool name. Required boss, swimming, ladder and special-action
models remain to be specified from their own evidence before dependent calculation;
the compact pilot's flat path and naked-adult workload do not cover them.

## Vanilla generator scopes

The seven included families retain their Minecraft namespace. Existing retained-mod
replacements, aliases, processors and rejected optional content come from Item 8,
not a newly generated vanilla-only reference world.

| Family | Root(s) and dimension | Required design/component scope |
| --- | --- | --- |
| minecraft:ancient_city | minecraft:ancient_city, Overworld | Procedural city with center and room/wall alternatives; at least two distinct-seed layouts. Sculk ingredients are not observed Warden encounters; preserve missing wall-stairs source reference |
| minecraft:bastion_remnant | minecraft:bastion_remnant, Nether | Bridge, housing/units, hoglin-stable and treasure starting designs, with two distinct-seed assemblies per starting design. Components and mob rolls remain within those designs |
| minecraft:end_city | minecraft:end_city, End | Procedural tower/bridge layouts both with and without the optional ship. At least two distinct-seed layouts with both outcomes represented; unreferenced tower_floor stays unselected |
| minecraft:mansion | minecraft:mansion, Overworld | Procedural custom mansion room layouts and all material retained-mod replacement/goal room classes. At least two distinct-seed layouts; source template counts do not determine rooms |
| minecraft:ocean_ruin | minecraft:ocean_ruin_cold, minecraft:ocean_ruin_warm, Overworld | Both temperatures, small/large layouts and clustered/isolated outcomes where the generator permits them. Cold material layers are one ruin. Each selected fragment/layout and archaeology/reward difference remains in coverage |
| minecraft:pillager_outpost | minecraft:pillager_outpost, Overworld | Complete tower plus site attachments, including material cage/inhabitant alternatives. One detached tower does not cover the camp. Preserve natural overrides separately |
| minecraft:trial_chambers | minecraft:trial_chambers, Overworld | Procedural chamber/connector/goal graph, ordinary/ominous trial and vault source states, and every retained alias-selected enemy mechanism, including Regions Unexplored ashen contribution. At least two distinct-seed layouts; alias index coupling is not independent enemy sampling |

Vanilla family denominator is seven, with eight roots because ocean ruins have
two. Concrete chamber configurations and source-selected templates are the exact
ones in each accepted family record. Source exposure to an ominous configuration
is not an observed activated ominous encounter or acquired vault reward. Their
modeled scenarios must predeclare activation conditions and state before use.

## Smaller temple, tower and settlement scopes

These tables finish the remaining registered-family population. Exact source
layouts, processors, entity data and missing-component lists are retained by each
family's accepted Item 8 grouping decision and linked source assessments. The
compact-room pilot does not authorize treating a tower or water-filled site as a
flat air-only route. Fixed designs initially need one complete saved example per
listed alternative; procedural designs need two distinct-seed examples plus the
unrepresented material component/goal cases. Neither minimum guarantees coverage.

| Family | Root/design alternatives | Dimension | Material scope |
| --- | --- | --- | --- |
| explorations:jungle_temple | Same root; temple plus outside-stair and chest alternatives | Overworld | Connected assembly and every material stair/reward placement alternative |
| explorations:slime_cave | Same root; one selected cave template | Overworld | Rotations and below-zero stone replacement are placement/processing states of this cave, not additional families; retain Slime encounter source |
| explorations:underground_temple | Same root | Overworld | Procedural rooms, walkways, shafts, intersections and terminal spaces |
| explorify:badlands_pyramid | Same root; one whole-building template | Overworld | Fixed pyramid geometry and actual hazard/reward connectivity |
| explorify:black_spiral | Same root | Nether | Procedural spiral tower/bridge/dungeon-feature assembly, retaining natural and authored mob distinctions |
| explorify:mausoleum | Same root; two whole-building alternatives | Overworld | Both layouts, not one representative chosen for better contents |
| explorify:ruins | Same root | Overworld | Procedural settlement with square, house, monument, path and treasure components |
| explorify:watchtower | explorify:watchtower/plains, explorify:watchtower/savanna, explorify:watchtower/taiga | Overworld | Three layouts with variant-owned village loot; equal dimensions alone do not remove a variant |
| illagerinvasion:illager_fort | Same root; one building plus entity components | Overworld | Fort architecture, inquisitor/provoker/vindicator components and separate natural override |
| illagerinvasion:illusioner_tower | Same root; three starting tower templates | Overworld | All furnishing/mob-connector alternatives despite shared dimensions |
| illagerinvasion:labyrinth | Same root | Overworld | Procedural tower/hall/room network, distinct from the self-contained towers |

This table has 11 families and 13 roots. Source enemy IDs, modded special attacks
and conversion-dependent payloads need supported model treatment before any combat
calculation; the ordinary skeleton pilot is not a fallback.

| Family | Root/design alternatives | Dimension | Material scope |
| --- | --- | --- | --- |
| terralith:desert_outpost | Same root; one open compound | Overworld | Usable activity space, archaeological and facility/reward content |
| terralith:mage_complex | Same root | Overworld | Procedural tower/house/barracks/road site, including material building alternatives |
| terralith:mage_tower | terralith:mage_tower, terralith:mage_tower_autumn, terralith:mage_tower_spring, terralith:mage_tower_summer, terralith:mage_tower_winter | Overworld | All five root variants, preserving fixed seasonal heights and winter stray source |
| terralith:spire | Same root | Overworld | Four vertical layers and two base halves are a connected assembly with lower encounters/loot and a furnished top |
| terralith:underground/frosted_dungeon | Same root; one chamber template | Overworld | Stray spawner and dedicated reward source; validate actual burial/access |
| terralith:underground/mining_outpost | Same root; small and large templates | Overworld | Both framed shelter arrangements with barrel/furnace facilities |
| terralith:underground/old_refinery | Same root; one elongated installation | Overworld | Layered interior access and facilities; no inferred functioning refinery machinery |
| terralith:underground/sunken_tower | Same root; one ruined vertical tower | Overworld | Actual floor connections and exposure; the name does not prove water coverage |

Terralith denominator: eight families and twelve roots. The two Mining Outpost
whole-template alternatives remain within one root and need separate coverage.

| Family | Root/design alternatives | Dimension | Material scope |
| --- | --- | --- | --- |
| ctov:pillager_outpost | Twelve roots listed below, eleven distinct definitions | Overworld | Full tower/camp/cage layouts. Badlands/mesa are a verified definition/pool duplicate. Missing Savage & Ravage target and variant-specific cage/target/tower references stay frozen defects |
| integrated_stronghold:stronghold | Same root | Overworld | Procedural fountain-rooted dining/library/prison/portal system. Both this and Better Strongholds remain separate active custom types; no Eye-of-Ender outcome is inferred |
| integrated_villages:village | Twelve roots listed below | Overworld | Each architectural/placement design, including elevated airship, coastal, submerged and Quark-dependent content. Two distinct-seed sites per procedural design; empty-data Mossy Mounds spawner is not a default enemy |
| supplementaries:galleon | Same root; main plus hull/room/orlop/sail alternatives listed below | Overworld | Complete internal ship and spawn-box mechanisms, distinct from ordinary spawners; incompatible back02 connector remains a frozen rejection |
| towns_and_towers:desert_mimic | towns_and_towers:mimic_desert | Overworld | Fixed-height three-component mimic assembly; the name is not an enemy mechanism |
| towns_and_towers:ocean_outpost | towns_and_towers:pillager_outpost_ocean | Overworld | Ship/outpost at fixed Y58 with natural pillager override and actual aquatic access |
| towns_and_towers:outpost_fort | Nine roots listed below | Overworld | All enclosure-oriented layouts and their encounter/reward fixtures |
| towns_and_towers:outpost_tower | Sixteen roots listed below | Overworld except ineligible Nilotic | All fifteen naturally eligible layouts. Nilotic has an empty resolved biome set, so it has a source-supported natural-sampling inapplicability disposition, not a missing generated sample |

CTOV roots are `ctov:pillager_outpost_` plus `badlands`, `beach`, `dark_forest`,
`desert`, `jungle`, `mesa`, `mountain`, `plains`, `savanna`, `snowy`, `swamp`,
`taiga`. The accepted `common_generation_definition` and equal badlands/mesa
variant records prove the duplicate, including identical start pools. One shared
design sample can cover that definition; both registry IDs remain in the inventory.
No other pair is merged merely because the biome/material label looks similar.

Integrated Village roots, all in `integrated_villages:`, are `airship_village`,
`cabin_village`, `clockwork_village`, `kutcha_village`, `marketstead_village`,
`mediterranean_village`, `mossy_mounds`, `oasis_village`, `pirate_village`,
`quark/minka_village`, `sunken_village`, `tavern_village`. Optional-content
predicates remain those of the frozen runtime; no compatibility branch is enabled
for measurement.

Galleon selected templates use `supplementaries:galleon/`: `galleon`,
`hull_back01`, `hull_back02`, `hull_back03`, `hull_front01`, `hull_front02`,
`hull_mid01`, `hull_mid02`, `hull_room01`, `hull_room02`, `hull_room03`,
`orlop_room01`, `orlop_room02`, `sail01`, `sail02`, `sail03`, `sail04`.
The [existing connector and content derivation](../item-8/sources/supplementaries-generation/README.md)
explains back02's incompatible incoming name. Preserve that rejected attachment
outcome rather than claiming all seventeen templates occur in every ship. All
compatible material room/hull alternatives require generated coverage; sail
variation is retained for external form assessment and is not another room.

Towns and Towers uses these complete root sets in `towns_and_towers:`:

- Fort: `exclusives/pillager_outpost_classic`,
  `exclusives/pillager_outpost_iberian`, `exclusives/pillager_outpost_mediterranean`,
  `exclusives/pillager_outpost_rustic`, `pillager_outpost_badlands`,
  `pillager_outpost_desert`, `pillager_outpost_grove`, `pillager_outpost_jungle`,
  `pillager_outpost_old_growth_taiga`.
- Tower: `exclusives/pillager_outpost_nilotic`,
  `exclusives/pillager_outpost_oriental`, `exclusives/pillager_outpost_swedish`,
  `exclusives/pillager_outpost_tudor`, `pillager_outpost_birch_forest`,
  `pillager_outpost_flower_forest`, `pillager_outpost_forest`,
  `pillager_outpost_meadow`, `pillager_outpost_mushroom_fields`,
  `pillager_outpost_savanna`, `pillager_outpost_snowy_plains`,
  `pillager_outpost_snowy_slopes`, `pillager_outpost_snowy_taiga`,
  `pillager_outpost_sunflower_plains`, `pillager_outpost_swamp`,
  `pillager_outpost_taiga`.

Nilotic's accepted `biome_constraints` record contains `biomes=[]`, no missing
required entries and no unresolved tags. Its dimension intersection is empty.
This is positive source evidence of no naturally eligible location in the frozen
baseline, not absence in the sampled worlds. Retain its spelling-sensitive
`minecraft:emptY` defect and source architecture. Do not generate a forced
Nilotic example solely to disguise natural inapplicability. Mushroom Fields,
which is eligible, retains its empty spawn override and still requires a sample.

This final settlement table contains eight families and 53 roots. Together, the
three tables in this section cover 27 families and 78 roots. Their source
exceptions are exact dispositions, not permission to reduce other missing samples.

## Complete population boundary, incomplete sampling gate

Every one of the 192 included canonical families now has a variant-scope entry:
189 registered families in the tables above, with all 357 roots retained, plus
the three [non-registry feature/lifecycle families](README.md#non-registry-variants-and-reference-correction).
The 256 excluded families retain their individual rationale and evidence in the
complete intake. No decision uses absence in Item 12 as insignificance.

This completes the family-to-design scope pass, not measurement acceptance.
The smallest next deliverable is the concrete selected sample set with exact
variant/component membership, baseline/control separation, complete saved-block
bounds, missing-evidence dispositions and runtime/storage totals. The two pilot
samples may be reused. No other quality result follows from a scope table.
Source-only inapplicability is established here only for the explicitly ineligible
Nilotic root and inactive source branches; missing generated evidence elsewhere
must still be resolved under the original Item 13 requirements.

## First fixed-layout instance selection declaration

For the seven observed fixed MNS roots (`circle_nether_brick`, `giant_skull`,
`large_house_1`, `medium_house`, `medium_house_2`, `nether_tower`, `warped_dome`)
and the two observed fixed MSS roots (`desert_pyramid`, `small_tower`), select one
saved baseline instance each. These are nine root alternatives in eight families,
not the complete Moog population. Require a saved start, a full padded chunk
envelope and every template listed for that root in the accepted pool trace.
Rank eligible IDs by SHA-256 of the full candidate ID, then lexical ID. Do not
prefer an appealing score, a small envelope or a particular seed. Preserve all
other candidates and known incomplete cases in the assembly index.

This step selects instances only. Room graphs, block section coverage, processors,
movement support and encounter models remain required before scoring. Whole-layout
source scope comes from the Moog section above, not a template-count heuristic.
Selection reads only the small bound metadata files; budget one minute, 512 MiB
memory and 1 MiB output. No world or block read is needed.

The [fixed-layout selection](fixed-moog-selection.json) now records all nine exact
candidate IDs, dimension, padded bounds, declared components, eligibility counts
and deterministic selection. It reproduces byte for byte with:

```sh
uv run python -m evidence.item-13.select_samples --fixed-moog --output /tmp/item13-fixed-moog-reproduction.json
cmp evidence/item-13/fixed-moog-selection.json /tmp/item13-fixed-moog-reproduction.json
```

Selection took 0.162 seconds and 82,184 KiB peak RSS. Output is 4,883 bytes,
SHA-256 `1fa54ed1163eff5119515d0545579d60af800719582ccfab5216af754d0e39f6`.
The nine padded volumes total 556,065 voxels, including 219,834 for Desert Pyramid.
This is an extraction cost input, not mechanical size or playable topology. The
nine samples cover these declared alternatives only; Circle Ruin's blackstone
alternative and all other absent designs remain required. Models and a block
extraction budget must be declared before processing these samples. The initial
selection failure and narrow versioned-component summary correction are preserved
in the authoritative README; no world was reread to resolve that metadata defect.

## Fixed-layout block preparation

The existing point reader decodes all 4,096 palette indices on every lookup.
The selected 556,065-voxel batch needs the same exact decoding once per section,
not a second block format or a different geometry approximation. Refactor that
existing reader to expose its section result, retain the point API, and check
packed order and negative coordinates with the affected saved-content tests.
Before world reads, benchmark 4,096 synthetic alternating-palette lookups against
one section decode, requiring identical returned states. Budget 30 seconds and
128 MiB memory for this code-path benchmark. It is not a game timing experiment.

Protocol `item13-fixed-blocks-v1`: extract only the nine already selected fixed
instances, using their exact envelope-plus-three bounds, saved block entities,
start NBT and WORLD_SURFACE columns. These are raw saved-block observations, not
room counts, traversal routes or combat estimates. The first extraction is
`mns:medium_house`, ordinary r1 Nether start 29,27, bounds
`[452,40,424,476,59,440]`: 8,500 voxels in `DIM-1/region/r.0.0.mca`.
Require full chunks and every selected block section; preserve failure without
silently substituting air. Verify the accepted world inventory before and after
under the existing lock. No server or gameplay actor is involved in this read.

Budget: five minutes and 10 MiB compressed output per selected instance, 1.5 GiB
peak memory and a 5 GiB free-space floor. The complete nine-instance extraction
budget is fifteen minutes and 90 MiB raw compressed output. Stop expansion if the
first extraction exceeds its cap. Its measured cost will inform the next block
reads; the synthetic section benchmark does not predict whole-world read cost.
Room boundaries, collision/movement rules and encounter assumptions must be
resolved before dependent quality scoring or timing models are run.
