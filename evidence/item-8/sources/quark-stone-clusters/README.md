# Quark stone contribution paths

Captured with extractor revision dae3bbe. The five captures and identities.json
reproduced byte for byte with this command before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name org/violetmoon/quark/content/world/module/BigStoneClustersModule.class --class-name org/violetmoon/quark/content/world/module/NewStoneTypesModule.class --class-name org/violetmoon/quark/content/experimental/module/VanillaStoneClustersModule.class --class-name org/violetmoon/quark/content/world/gen/BigStoneClusterGenerator.class --class-name 'org/violetmoon/quark/content/world/gen/BigStoneClusterGenerator$1.class' --output evidence/raw/item8/quark-stone-clusters-dae3bbe
```

BigStoneClustersModule registers calcite, limestone, jasper, shale and myalite
with BigStoneClusterGenerator at UNDERGROUND_DECORATION, weight zero.
VanillaStoneClustersModule registers granite, diorite and andesite through the
same generator. This establishes registered paths, not effective enablement.

BigStoneClusterGenerator uses configured rarity, height and biome constraints
for candidate sources. Its context calls canPlaceBlock and writes only its
single placeState with flag zero, discarding the returned success boolean.
AirStoneClusterConfig with generateInAir permits only air positions; other
cases use BigStoneClustersModule.blockReplacePredicate. The inspected writer
does not place entities, spawners, containers or authored rooms. This supports
a working terrain-contribution boundary for the cluster writer, including
air-generated terrain. Exact cluster extent and world occurrence are not proven.

NewStoneTypesModule additionally queues a callback that registers two
Zeta OreGenerator instances at UNDERGROUND_ORES with ALL_DIMS_STONE_MATCHER.
This separate delegated path remains to be inspected before a complete
NewStoneTypes contribution disposition. Do not infer its behavior from its name
or repeat the already captured cluster writer. Shared cluster enumeration,
effective configuration and complete Quark coverage are not claimed here.

Scoped extractor Ruff and Basedpyright checks passed. No server or measurement
was added. An initial exploratory archive listing omitted retained_sources'
required root argument and failed with TypeError; the corrected listing supplied
Path.cwd(). It was discovery only, not accepted evidence extraction.
