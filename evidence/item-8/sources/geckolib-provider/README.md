# GeckoLib contribution sources

Extractor ab875d95. Eight classes bind the loader, four services and three
common hooks. Independent r1 reproduction matches every source and manifest
byte. Manifest SHA-256:
70b343b81e834cdbd79556a18890c018ef9dd83a8a2b8565988e5b9a7d3b8fc5

```sh
uv run -m tools.inspect_item8_pool_elements --archive geckolib-neoforge-1.21.1-4.8.4.jar --class-name software/bernie/geckolib/GeckoLib.class --class-name software/bernie/geckolib/event/GeckoLibEventsNeoForge.class --class-name software/bernie/geckolib/mixin/common/AbstractContainerMenuMixin.class --class-name software/bernie/geckolib/mixin/common/ItemStackMixin.class --class-name software/bernie/geckolib/mixin/common/LivingEntityMixin.class --class-name software/bernie/geckolib/network/GeckoLibNetworkingNeoForge.class --class-name software/bernie/geckolib/platform/GeckoLibClientNeoForge.class --class-name software/bernie/geckolib/platform/GeckoLibNeoForge.class --output evidence/raw/item8/geckolib-provider-r1
```

Sources establish rendering event dispatch, supplied item models, platform
lookups, packet transport and item animation identity comparison/copy behavior.
The constants initializer and concrete packet registration remain to be
bound before this provider membership disposition is complete.
