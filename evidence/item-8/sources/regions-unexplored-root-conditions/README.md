# RU remaining root and condition registrations

Extractor: fbe9cc4b00e734417191b81921056c72064f7b60.
Eight classes reproduce byte-for-byte independently. This isolated generated
source increment closes the root-placer and processor-condition registration
coverage gap found in the common initializer. Full disassembly is retained.

```sh
uv run -m tools.inspect_item8_pool_elements --archive regions-unexplored-0.6.1-neoforge-21.1.jar \
  --class-name net/regions_unexplored/registry/RUBlockStateProviderTypes.class \
  --class-name net/regions_unexplored/registry/RULoadPredicateTypes.class \
  --class-name net/regions_unexplored/registry/RUProcessorConditionTypes.class \
  --class-name net/regions_unexplored/registry/RURootPlacerTypes.class \
  --class-name net/regions_unexplored/registry/RURuleSources.class \
  --class-name net/regions_unexplored/worldgen/processorcondition/ConfigCondition.class \
  --class-name net/regions_unexplored/worldgen/processorcondition/MatchingBiomesCondition.class \
  --class-name net/regions_unexplored/worldgen/rootplacer/MagnoliaRootPlacer.class \
  --output evidence/raw/item8/regions-unexplored-root-conditions-r1
```
