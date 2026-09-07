# BetterEnd entry and template consumer boundaries

## Building and ruin attribute integration

The sixteen canonical building/ruin designs now record all eleven Item 8
descriptive attributes in family-decisions.json and the generated inventory.
The increment adds 128 answers: dimension, biome constraints, placement, intended
hostility, mob source, spawners, enemy attribution and loot source for each design.
Existing nominal geometry and qualitative form are preserved.

Reproduce the inventory and run the affected existing checks:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-building-complete-descriptions.json
uv run pytest -q tests/item8/test_betterend_feature_candidates.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Derivation: join each design's exact template paths to the configured building
lists, their placed features and packaged biome consumers. Match those biomes
to dimension-r3/dimension-biomes.json. Preserve every offset_y and terrain_merger
choice. BuildingListFeature.canSpawn requires even chunk-coordinate sum, Y>58,
air and TERRAIN support; NBTFeature applies ground selection, rotation, mirror
and the configured offset. Member templates have empty entity lists and no
spawner palette states. The captured direct building/processor path authors no
enemy. These are source descriptions, not observed successful placement.

For loot, each saved LootTable field retains its exact template, block-entity
index, position and ID. The recorded table paths and hashes bind the packaged
definitions. ChestProcessor (betterend-remaining-features) tests ChestBlock,
creates a block entity and calls LootTableUtil.getTable (betterend-common-entries)
using the noise biome at the processed position. That selector maps five named
biomes to their chest tables and otherwise returns common. It does not select
barrels. The processor returns the original block record, including its NBT;
do not equate its transient assignment with the final saved table.

EndStructureHelper's existing absolute-resource path reads compressed NBT and
calls StructureTemplate.load with the block registry, without an explicit data
fixer call. Preserve legacy bclib block-entity IDs and saved loot references.
Successful legacy conversion, final reward realization and actual population
are not established or required by this source-attribution answer. Do not reopen
those as generic unfinished work, and do not claim they succeeded. No new runtime,
source capture, renderer, validator or measurement system was needed.

Selector dd6ed45 captures six classes from the frozen BetterEnd archive.
Manifest SHA-256: 22dee10074c502f7026b266335c5d2966a47374504ae836d2f1da17e79a895d8.
An independent capture reproduced all disassemblies and identities byte for byte.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BetterEnd-21.0.31.jar --class-name org/betterx/betterend/BetterEnd.class --class-name org/betterx/betterend/client/BetterEndClient.class --class-name org/betterx/betterend/world/features/BuildingListFeatureConfig.class --class-name 'org/betterx/betterend/world/features/BuildingListFeature$StructureInfo.class' --class-name org/betterx/betterend/world/features/NBTFeature.class --class-name org/betterx/betterend/util/EndStructureHelper.class --output evidence/raw/item8/betterend-entry-template-consumers-r1
```

BuildingListFeatureConfig decodes a nonempty `structures` list. getRandom chooses
one index from that list. StructureInfo decodes exactly `path`, `offset_y` and
`terrain_merger`; getStructure passes its stored path to EndStructureHelper.
For the present absolute template paths, that helper reads the BetterEnd class
resource, then parses the compressed NBT as a StructureTemplate. Only a missing
class resource delegates to BCLib. There is no directory enumeration or adjacent
structures.json loading in this path. All 63 configured resources already exist
and decode in test_betterend_feature_candidates.py. The old `nbt`, `offsetY` and
`terrainMerge` lists are not this configuration codec.

NBTFeature places the template selected by its subclass after finding ground and
checking canSpawn. It applies rotation, mirror, offsets, processors and terrain
merging. These transformations do not discover additional template choices.
Preserve its getGround behavior: it tests the biome namespace for `moutain`
(actual spelling) and `lake`, not the biome path. Do not reinterpret or repair it
as a biome-name test. This capture is not a success-rate or geometry measurement.

The verbose common entry captures registration listeners, world configuration,
biome and structure registration, generator options, loot support, commands,
integrations and the BetterEndPlugin ServiceLoader. It conditionally registers
BYG feature callbacks when BYG is loaded. The client entry records client-only
render/model/color callbacks. These are entry boundaries for the remaining
provider reconciliation, not proof that every referenced subsystem is closed.
No unrelated rendering, item or combat helper tracing is required.
