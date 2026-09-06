# Fabric biome modifier boundary

Extractor: bbdf6f394fc3f32f2112e7548c350b5ed48e2551.
Five complete class captures reproduce byte for byte in the independent run.
This source increment addresses the sole packaged biome modifier and its
registration/consumer boundary, not complete provider membership.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-biome-api-v1-13.0.31+1e62d33c19.jar --class-name net/fabricmc/fabric/api/biome/v1/BiomeModifications.class --class-name 'net/fabricmc/fabric/impl/biome/modification/BiomeModificationImpl$FabricBiomeModifier.class' --class-name net/fabricmc/fabric/impl/biome/modification/BiomeModificationImpl.class --class-name org/sinytra/fabric/biome_api/FabricBiomeApiV1.class --class-name org/sinytra/fabric/biome_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-biome-modifier-r1
```
