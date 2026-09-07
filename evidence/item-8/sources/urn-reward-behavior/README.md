# Cave urn descriptive assessment

Three urn classes resolve the previously missing reward and creature behavior.
One RandomPatchFeature selection in the existing extractor resolves whether the
configured spreads are radii or total extents. This is necessary for Item 8's
geometry and mob/loot-source answers; no new measurement or framework is added.
The separate urn-patch-geometry directory retains that mapped-server capture.
Each identities.json binds archive, class and disassembly hashes.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --class-name net/mehvahdjukaar/supplementaries/common/block/blocks/UrnBlock.class --class-name net/mehvahdjukaar/supplementaries/common/block/tiles/UrnBlockTile.class --class-name net/mehvahdjukaar/supplementaries/common/entities/FallingUrnEntity.class --output evidence/raw/item8/urn-reward-behavior-r1
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/levelgen/feature/RandomPatchFeature.class --output evidence/raw/item8/urn-patch-geometry-r1
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-urn-descriptions.json
uv run pytest -q tests/item8/test_supplementaries_provider_scope.py::test_supplementaries_components_and_road_sign_feature_chain tests/item8/test_structure_biomes.py tests/item8/test_biome_tag_inputs.py tests/item8/test_biome_resolution.py
uv run ruff check tools/build_item8_inventory.py tools/inspect_item8_pool_elements.py
uv run basedpyright tools/build_item8_inventory.py tools/inspect_item8_pool_elements.py
```

Direct derivation uses packaged urns_patch, cave_urns and blocks/urn resources,
the six urn loot tables, and tags/entity_type/urn_spawn in the retained JSON
catalog. Exact table identities are recorded in the authoritative family row.
RandomPatchFeature.place computes nextInt(spread+1)-nextInt(spread+1) per axis.
Spreads 4/1 therefore give -4..4 horizontally and -1..1 vertically: 9x9x3
candidate block positions per patch, with nine tries and six separate-origin
placement repetitions. Supported-air filtering and later falling prevent treating
this as a filled or persistent cache bound.

Existing supplementaries-tags-code captures ModServerDynamicResources publishing
HAS_CAVE_URNS in its Forge branch, adding IS_OVERWORLD if URN_PILE_ENABLED.
ModTags binds has_cave_urns. CommonConfigs$Functional binds that supplier to
functional.urn.cave_urns, true in the frozen common config. Urn enabled is also
true. The generated pack is enabled in registry-r1/world-context.json.
Apply existing item8_biomes.biome_constraint to #minecraft:is_overworld using
structure-inputs.json biome_tags and the retained worldgen_biome registry.
It returns 280 biomes, no missing required values and no unresolved tags.
Intersect with dimension-r3/dimension-biomes.json: only minecraft:overworld
has overlap. Full results and provenance are integrated in family-decisions.
This derives eligibility from retained sources, not a runtime urn-tag dump.

UrnBlock.spawnAfterBreak requires treasure=true, random check below the frozen
0.01 value, doTileDrops and absence of a prevents_infested_spawns tool enchantment.
It selects an actual urn_spawn tag holder and directly creates an entity;
empty tags or null creation yield none. The packaged required declarations are
silverfish, slime and bat; optional cross-mod entries are preserved as declarations,
not asserted present. No physical spawner or resident mob is placed by the feature.
FallingUrnEntity supplies movement/shattering behavior, not another family.

The block table independently tests silk touch for the urn-item pool and treasure
state for the reward pool. The latter references common/uncommon/rare/epic tables
with weight/quality pairs 60/-5, 32/-2, 7/2, 1/5. Conditional leaf entries remain
conditional. UrnBlock.getDrops appends existing container items to base drops;
FallingUrnEntity.shatter invokes Block.dropResources with reconstructed tile data
when present. These establish reward sources, not observed item outcomes.

An initial read-only lookup used a nonexistent entity_type registry filename.
No membership result was obtained or used; the assessment retains packaged
required/optional declarations and describes selection from actual tag holders.
An initial source lookup used the wrong ModServerDynamicResources package path;
the existing captured file was located and inspected. Neither failed lookup is
acceptance evidence. No additional entity registry capture is required for the
source attribution claimed here.
