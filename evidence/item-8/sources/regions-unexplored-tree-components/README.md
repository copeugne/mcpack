# Regions Unexplored tree components and configuration

Extractor: 16127c9fadd0cb389c28e4981fdca8aea5083e22.
All 24 classes reproduce byte-for-byte in the independent capture. This isolated
generated increment retains the registration, trunk, foliage and decoration
implementations still missing from the previous source set, their direct tree
utilities and the parent configuration loader. Full disassembly accounts for its
size. No library parser internals or general gameplay helpers are included.
Source capture does not by itself close provider membership.

```sh
uv run -m tools.inspect_item8_pool_elements --archive regions-unexplored-0.6.1-neoforge-21.1.jar \
  --class-name net/regions_unexplored/config/RUConfigHandler.class \
  --class-name net/regions_unexplored/registry/RUFoliagePlacerTypes.class \
  --class-name net/regions_unexplored/registry/RUTreeDecoratorTypes.class \
  --class-name net/regions_unexplored/registry/RUTrunkPlacerTypes.class \
  --class-name net/regions_unexplored/util/TrunkPlacerDirtUtil.class \
  --class-name net/regions_unexplored/worldgen/foliageplacer/AspenFoliagePlacer.class \
  --class-name net/regions_unexplored/worldgen/foliageplacer/BioshroomFoliagePlacer.class \
  --class-name net/regions_unexplored/worldgen/foliageplacer/FancyPineFoliagePlacer.class \
  --class-name net/regions_unexplored/worldgen/foliageplacer/MagnoliaFoliagePlacer.class \
  --class-name net/regions_unexplored/worldgen/foliageplacer/MapleFoliagePlacer.class \
  --class-name 'net/regions_unexplored/worldgen/foliageplacer/RUFoliagePlacerUtils$Context.class' \
  --class-name net/regions_unexplored/worldgen/foliageplacer/RUFoliagePlacerUtils.class \
  --class-name net/regions_unexplored/worldgen/foliageplacer/RedwoodFoliagePlacer.class \
  --class-name net/regions_unexplored/worldgen/foliageplacer/SakuraFoliagePlacer.class \
  --class-name net/regions_unexplored/worldgen/foliageplacer/SkinnyPineFoliagePlacer.class \
  --class-name net/regions_unexplored/worldgen/foliageplacer/WillowFoliagePlacer.class \
  --class-name net/regions_unexplored/worldgen/treedecorator/GroupBranchDecorator.class \
  --class-name net/regions_unexplored/worldgen/treedecorator/HangingVinesDecorator.class \
  --class-name net/regions_unexplored/worldgen/treedecorator/RandomBranchDecorator.class \
  --class-name net/regions_unexplored/worldgen/treedecorator/WillowTrunkDecorator.class \
  --class-name net/regions_unexplored/worldgen/trunkplacer/AspenTrunkPlacer.class \
  --class-name net/regions_unexplored/worldgen/trunkplacer/MagnoliaTrunkPlacer.class \
  --class-name net/regions_unexplored/worldgen/trunkplacer/RUTrunkPlacer.class \
  --class-name net/regions_unexplored/worldgen/trunkplacer/RedwoodTrunkPlacer.class \
  --output evidence/raw/item8/regions-unexplored-tree-components-r1
```
