# Supplementaries generation and elevator sources

Extractor 24f0a7545218356b416aed0ab750292b49aa719c. Manifest SHA-256: 0eb64c666c0db4bd45091038bb2b3d622a1e57f896d31fe0df1279f2ff357e5d. Independent r1 matches every generated file.

Eleven sources cover ModWorldgen, four custom features, two structure implementations, the mineshaft elevator and its direction helper, and the two mineshaft injection mixins. This is the concrete generation boundary identified by the packaged components and elevator class consumers, not full provider closure.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --class-name net/mehvahdjukaar/supplementaries/reg/ModWorldgen.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/BarnaclesMultifaceGrowthFeature.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/BasaltAshFeature.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/RoadSignFeature.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/SpawnEntityWithPassengersFeature.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/GalleonStructure.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/RoadSignStructure.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/MineshaftElevatorPiece.class --class-name 'net/mehvahdjukaar/supplementaries/common/worldgen/MineshaftElevatorPiece$1.class' --class-name net/mehvahdjukaar/supplementaries/mixins/MineshaftCorridorMixin.class --class-name net/mehvahdjukaar/supplementaries/mixins/MineshaftPiecesMixin.class --output evidence/raw/item8/supplementaries-generation-r1
```
