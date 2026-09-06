# Fabric biome selection hooks

Extractor: 2426342939f348480e8d6bd6ae4a2d9a069d6806.
Eight complete classes independently reproduced byte for byte. All six declared
biome mixins and their Nether/End selection data consumers are retained.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-biome-api-v1-13.0.31+1e62d33c19.jar --class-name net/fabricmc/fabric/mixin/biome/BiomeSourceMixin.class --class-name net/fabricmc/fabric/mixin/biome/ChunkNoiseSamplerMixin.class --class-name net/fabricmc/fabric/mixin/biome/MultiNoiseUtilMultiNoiseSamplerMixin.class --class-name net/fabricmc/fabric/mixin/biome/NetherBiomePresetMixin.class --class-name net/fabricmc/fabric/mixin/biome/NoiseConfigMixin.class --class-name net/fabricmc/fabric/mixin/biome/TheEndBiomeSourceMixin.class --class-name net/fabricmc/fabric/impl/biome/NetherBiomeData.class --class-name net/fabricmc/fabric/impl/biome/TheEndBiomeData.class --output evidence/raw/item8/fabric-biome-selection-r1
```
