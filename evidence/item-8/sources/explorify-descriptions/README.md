# Explorify standalone source descriptions

Six families cover 15 roots and 16 standalone templates: badlands_pyramid,
desert_shrine, guide_post, supply_cache, watchtower and mausoleum. Integrated
32 missing descriptions and reconciled 24 existing attribution answers. All
traces and biome resolutions have no missing/unresolved entries. Raw templates
contain no jigsaw block entities; two mausoleums are whole-building alternatives.
Geometry reads template_size_xyz directly, including padding and rotation limits.

Exact root definitions come from packaged-json-redacted.json.gz. Standard jigsaw
surface offsets are pyramid -12..-9, shrine -10..-6, guide post -11 and others 0.
Mausoleum projects to WORLD_SURFACE; others WORLD_SURFACE_WG. No measured burial
or exposed height is inferred. Existing whole-template geometry is retained.

No top-level entity source occurs. Mausoleum supplies legacy zombie-spawner NBT;
other selected templates have no physical-spawner input. All spawn overrides are
empty, which does not suppress biome spawning. Pyramid includes TNT, not tested
trap operation. Exact saved loot references remain attributed to templates.
Guide post processors can change signal_fire or remove a campfire, so a guaranteed
smoke cue is not asserted. Stone/moss/cobweb/candle processors alter material and
presentation, not a measured discovery distance.

## Mausoleum overlay attribution

The existing generic resource selector excludes non-Lithostitched prefixes, so
its root-only processor selection cannot alone describe mausoleum loot. Direct
retained archive inspection establishes an additional source without changing
the selection framework. pack.mcmeta is copied byte-for-byte from
Explorify v1.6.5.mod.jar, archive SHA-256
2dc76398b48b2aae9b4024642da098b0880125572de160cb5ecf91d102890cad.
Metadata SHA-256 is
eb6b11cfa493820b871090a5b58abe2f4f132a56eca77b3218e3df9e3084ed2b.

It declares overlay f15 formats 15..512, covering baseline data format 48.
The retained f15/data/explorify/worldgen/processor_list/mausoleum_processor.json
adds a rule matching potted_dead_bush with probability 0.33, producing decorated_pot
and append_loot explorify:chest/mausoleum_pot. Both mausoleum templates contain
that input block. The exact processor hash and source-declared overlay attribution
are in loot_table_source, separate from saved dungeon loot references. This is
not a runtime pot-yield observation. Metadata capture is necessary to explain why
the root processor is insufficient; no new measurement or generalized tool.

Direct metadata reproduction: use retained_sources(Path.cwd()) to select the
exact named archive, verify its SHA-256 above, and read ZipFile member pack.mcmeta
without transformation. Compare its bytes/hash with the committed file. Processor
and template logic already reside in the retained catalogs with exact identities.
An initial inspection assumed an AdoraBuild-specific variants key; Explorify
instead uses generation_settings/common_generation_definition. The lookup failed
without edits; exact root JSON was then inspected and used for these answers.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-explorify-standalone-descriptions.json
uv run pytest -q tests/item8/test_explorify_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

## Black Spiral assembly

Ten explicit answers complete source assessment: six missing descriptions and
four reconciled attributions. Existing resolved biome answers are retained.
world-bounds observations 225/620 are the same ocean-heavy-seed start in two runs
at structure_starts, not full chunks. Inclusive envelope [116,31,346,128,78,442]
gives 13x48x97 planned-layout blocks. This is one layout reproduced, not two
independent samples, populated blocks or a family-wide bound. The root uses
standard jigsaw absolute 32, depth 7, no projection and no terrain adaptation.

Twenty reachable templates include the tower, bridges, resource/dungeon features
and vanilla bastion mob components. There are no missing graph references,
unresolved entity IDs or generation markers. Preserve template-owned piglin/brute
entities and legacy blaze/hoglin spawner inputs separately. No realized population,
conversion or simultaneous component selection is asserted. Empty spawn overrides
do not disable ambient spawning. Exact bridge/treasure chest sources remain saved
loot references; resource blocks remain distinct from container rewards.

Complete retained spiral_tower_randomization rules only replace material, including
blackstone to lava at a configured 0.01 match probability. The bridge processor
removes matching blackstone at 0.25. These are authored hazard ingredients and
rule probabilities, not observed hazard frequency or tested traversal difficulty.
No processor adds a mob, physical spawner or loot assignment. The graph and saved
assembly supply visual form while Nether terrain and chunk stage limit exposure
claims. No new source capture or measurement was necessary.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-explorify-spiral-descriptions.json
uv run pytest -q tests/item8/test_explorify_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

## Mangrove hut and End shipwreck

Two families each have three templates and no missing graph references. Twelve
missing descriptions and eight existing attributions are integrated. Hut main
is 14x32x16. Its upward connectors [3,22,10] and [3,26,10] meet downward connectors
at [0,0,0] of 1x2x1 entity templates, placing them inside the main envelope at
Y=23..24 and 27..28. Children terminate at empty pools. Cat is an animal; witch
is the authored enemy source. The hut processor only replaces mangrove logs with
stone where location matches base_stone_overworld. No saved loot table occurs.

Shipwreck's 1x1x1 base points up to the hull's downward Y=0 connector. Sideways
hull is 12x13x27 with connector [11,0,0]; upside-down is 13x11x25 with connector
[12,0,0]. Thus one selected hull sits one layer above the base. The base remains
within its horizontal projection: assembled envelopes are 12x14x27 or 13x12x25,
including the one air-final-state base layer. Hulls are alternatives, not summed
pieces, and their connectors terminate at empty pools. No top-level entities or
physical spawners occur; both preserve End-city loot references. All pools are
rigid and ship processors empty. Rotation may exchange X/Z; these are nominal
piece envelopes including padding, not occupied or observed geometry.

Standard jigsaw WORLD_SURFACE_WG start offsets are hut -21..-17 and wreck -7..-5,
with no terrain adaptation. Empty spawn overrides do not disable ambient spawning.
Connector/form evidence supports qualitative visibility limitations without a
world run or measured discovery distance. No new source capture or tooling.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-explorify-hut-wreck-descriptions.json
uv run pytest -q tests/item8/test_explorify_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

## Five settlement-family attributions, geometry still open

Campsite, dark forest settlement, farmstead, ruins and tavern now integrate eight
explicit attributes each, plus their existing resolved biome answers. This is
40 answers: 20 missing placement/design interpretations and 20 reconciled source
attributions. Ten approximate assembled-geometry answers remain unresolved.
There are no retained saved layout observations for these families; piece sizes
are not substituted for whole settlements. No family completion count advances.

All five roots have complete traces with no missing references, unresolved entity
IDs or generation markers. Preserve exact template-owned animals/villagers/cats/
golem where present, and ruins monument/02's saved zombie-spawner input. These
are authored sources, not simultaneous realized populations. Empty spawn overrides
do not disable ambient spawning. Exact saved loot tables remain attributed to
components. Other than the ruins overlays below, inspected processors only alter
material, aging or path/water adaptation, not entities or physical spawners.

Root offset is 0 and adaptation beard_thin. Preserve projection/depth/expansion
choices: campsite WORLD_SURFACE/7/false, dark forest WORLD_SURFACE_WG/3/true,
farmstead MOTION_BLOCKING_NO_LEAVES/6/false, ruins OCEAN_FLOOR_WG/4/true,
tavern WORLD_SURFACE/7/true. These describe starts, not terrain exposure or the
extent of the assembled network. Qualitative component roles supply visual forms.

The same pack metadata retained above declares f15 applicability. Overlay
ruins_house_processor adds capped suspicious-gravel append_loot delegates with
limits 3 for minecraft:archaeology/trail_ruins_common and 1 for trail_ruins_rare.
ruins_path_processor uses limits 5 and 2 respectively. Both match the
minecraft:trail_ruins_replaceable tag. Exact overlay hashes, table IDs, inputs
and limits are now explicit in ruins loot_table_source. Limits are processor
inputs, not guaranteed whole-family counts. Root-only generic selection would
omit this evidence, so do not drop it in final integration. No new selector,
source capture or world measurement was added.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-explorify-settlement-attribution.json
uv run pytest -q tests/item8/test_explorify_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```
