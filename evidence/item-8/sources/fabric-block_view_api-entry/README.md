# Fabric block_view_api contribution paths

Captured with 231284d; independent repeat matched all source files exactly.
Manifest SHA-256: 24fb28fc00e6da4260ca6a0aec22aa5520f73b3a20b0c441eb8956c236ca3ca4.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-block-view-api-v2-1.0.11+e9036fd419.jar --class-name net/fabricmc/fabric/mixin/blockview/BlockEntityMixin.class --class-name net/fabricmc/fabric/mixin/blockview/BlockViewMixin.class --class-name net/fabricmc/fabric/mixin/blockview/WorldViewMixin.class --class-name org/sinytra/fabric/block_view_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-block_view_api-entry-r1
```

The loader is empty. Common mixins add block/render-data interfaces and forward existing biome reads; hasBiomes returns true for a LevelReader. They add no generation path.

Complete module payload and mixin membership are checked separately. This
capture is not whole Fabric provider closure. Do not follow generic interface
helpers beyond a demonstrated content-contribution question.
