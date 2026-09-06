# BetterEnd entry and template consumer boundaries

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
