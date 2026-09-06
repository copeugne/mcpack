# Fabric loot_api_v2 entry roles

Captured with 5049826 and independently reproduced exactly. Manifest SHA-256:
39948838d282ea95917661b003571449b503449615810c9e78d61eb0ca95ed67.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-loot-api-v2-3.0.15+a3ee712d19.jar --class-name net/fabricmc/fabric/mixin/loot/v2/LootPoolBuilderMixin.class --class-name net/fabricmc/fabric/mixin/loot/v2/LootTableBuilderMixin.class --class-name org/sinytra/fabric/loot_api_v2/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-loot_api_v2-entry-r1
```

Common mixins add legacy loot-builder interfaces. The generated loader calls LootInitializer.onInitialize; that initializer remains to be inspected before closure.

Complete payload and declared-hook coverage are verified by the existing Fabric
provider check. This capture is not whole-provider or effective-loot acceptance.
