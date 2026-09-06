# Fabric loot_api entry roles

Captured with 5049826 and independently reproduced exactly. Manifest SHA-256:
651e7b5dc634205e9dd736041958177205b0ebf3b5e0ff97991d7ed1ff6a7371.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-loot-api-v3-1.0.3+333dfad919.jar --class-name net/fabricmc/fabric/mixin/loot/JsonDataLoaderMixin.class --class-name net/fabricmc/fabric/mixin/loot/LootPoolAccessor.class --class-name net/fabricmc/fabric/mixin/loot/LootPoolBuilderMixin.class --class-name net/fabricmc/fabric/mixin/loot/LootTableAccessor.class --class-name net/fabricmc/fabric/mixin/loot/LootTableBuilderMixin.class --class-name net/fabricmc/fabric/mixin/loot/ReloadableRegistriesMixin.class --class-name org/sinytra/fabric/loot_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-loot_api-entry-r1
```

Empty generated loader. Source-map and reload hooks supply loot provenance and consumer replace/modify/all-loaded callbacks; accessor and builder methods operate on supplied tables/pools. No independent structure content is declared. Effective consumer loot changes remain Item 8 attribute work.

Complete payload and declared-hook coverage are verified by the existing Fabric
provider check. This capture is not whole-provider or effective-loot acceptance.
