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
