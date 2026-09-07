# Repurposed village assessment

Seven remaining required entries for one family/14 variants are integrated.
1345 distinct templates are shared across variant graphs; summing variant counts
would double-count shared components. Existing oak saved geometry under
repurposed-final-geometry is reused. No new runtime or tool is needed.

## mob_source

1345 distinct pool-traced templates shared across14 variants. Exact template entity sources retained below. Land variants generally author villagers, domestic animals, cats and iron golems, with zombie-villager templates except mushroom. Mushroom additionally authors mooshroom. Ocean authors drowned. Crimson and warped author piglin, piglin_brute, hoglin, zoglin, zombified_piglin and strider. Item/item_frame are non-mob entities. Tree features with beehive decorators supply an additional potential bee source. No unresolved template entity sources or generation markers; no realized populations inferred.

## loot_table_source

34 literal loot-table sources resolve:12 minecraft:chests/village tables and22 repurposed_structures:chests/villages tables. Exact identifiers and referencing templates retained below. Referenced processors alter crops, materials, supports, paths, coral or placement; neither candidate of the nine competing crop lists appends loot-table NBT. Crop selection and harvest yield are not a container loot-source claim.

## generated_spawners

No ordinary or trial spawners and no generation markers in the1345-template trace. Referenced processor definitions, including both candidates of each competing crop list and nested swamp path delegates, do not select a spawner randomizer or introduce spawner blocks. Authored hostile entities are not spawners. This does not preclude ordinary natural spawning.

## authored_or_natural_enemies

Template-authored zombie villagers occur in land variants except mushroom; ocean authors drowned; crimson/warped author piglin brutes, hoglins, zoglins and other Nether inhabitants. All14 roots have empty spawn_overrides: no family-specific natural spawn override, while ordinary environmental spawning remains possible. Villagers, golems, domestic animals and non-mob entities are retained separately in source mappings. Population and successful placement are not measured.

## intended_hostility

Settlement family with variant-dependent inhabitants and threats. Most land designs include ordinary and zombie-villager template alternatives; mushroom has no hostile template entity in this trace. Ocean drowned and Nether piglin-brute/hoglin/zoglin sources prevent a uniformly peaceful classification. No spawners, measured intensity or Item9 tier is assigned.

## visual_discoverability

Town centers, buildings, connecting paths and farms provide settlement cues. Land designs use biome-related materials and vegetation; giant mushrooms, jungle/swamp trees and terrain can obscure buildings. Ocean uses seabed construction and coral; Nether uses crimson/warped materials. Qualitative cues only, with no measured visibility distance or guaranteed visible entrance.

## underground_surface_classification

Land variants project to WORLD_SURFACE_WG with offset0 and beard_thin; swamp runs at top_layer_modification. Ocean projects to OCEAN_FLOOR_WG with offset0, maxY52, terrain range26/radius2 and biome radius2: seabed/submerged intent. Its path processor declares OCEAN_FLOOR_WG gravity and require_water_surface. Crimson/warped use generic_nether_jigsaw_structure, HIGHEST_LAND offset0 and beard_box: Nether land-associated settlements. Other root differences remain explicit in variants. Saved oak geometry is one family example, not a size bound on every variant; supports and path projection do not prove occupied volume or burial.

## Resource conflict disposition and scope

The pool graph references103 processor identities. Nine crop_randomizer paths
have both Repurposed Structures and Farmer's Delight compatibility definitions:
bamboo,birch,cherry,dark_forest,giant_taiga,jungle,mountains,oak,swamp. Both candidate
documents are retained in packaged-json-redacted.json.gz. They contain minecraft:rule
crop substitutions without loot-table, entity or spawner modifiers. Base lists
also contain bottom-pillar supports that compatibility lists omit. Neither
candidate is used to assert final support extent; saved-piece dimensions exclude
that claim. An initial inspection assertion wrongly expected rule-only lists;
the support difference was inspected and this description corrected.
Their unresolved selection is not used to assert a crop output, harvest yield,
container loot source, enemy source or geometry size. The smallest sufficient
proof is inspection of both candidates for the required claims, not a new
runtime precedence experiment. Exact crop output remains unspecified, with no
Item8 experiment backlog created. Existing resource selection must still reject
this conflict if a future consumer asks it to choose an actual crop definition.

The14 bottom-pillar delegates use material rules, block ignore and waterlogging;
no additional rule modifiers or spawner outputs occur.
Other referenced processors use material rules, bottom/pillar supports, noise,
coral, mushroom placement, structure void, ocean path gravity and swamp post
processing. The swamp path delegates apply material/ignore/air/floating-block
rules, not an enemy or loot injection. Existing bottom-pillar and structure-void
inspections are described in repurposed-outpost-assessment and
repurposed-temple-assessment. The root's terrain adaptation and saved piece
bounds are not claims about the final extent of processor-created supports.

Selected birch_bees_002 and fancy_oak_bees_002 configured trees declare vanilla
beehive decorator probability0.02; azalea_bees_05 and cherry_bees_05 declare0.5.
This is a feature source, not an observed bee count. Tree, crop, pile, coral and
vegetation features are not additional canonical families.

All34 literal loot references resolve in the preserved packaged JSON catalog.
Their identifiers and template attribution remain in inventory.json. All14
root definitions and exact template entity mappings are retained. Catalog,
assembly and accepted geometry identities are bound in family-decisions.json.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-village-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only village and input identity may change.
Final Item8 integration, acceptance and PR/review/main remain open.
