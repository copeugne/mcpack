# Collective active contribution entries

Extractor a0b6df90. Eight entry/event/common-hook classes. Independent r1
reproduction matches source and manifest bytes. Manifest SHA-256:
54dc3bdb078a2638a1c0368bd5883e4d5721bb2e24f5f94ed37cfa5ca86e576e

```sh
uv run -m tools.inspect_item8_pool_elements --archive collective-1.21.1-8.25.jar --class-name com/natamus/collective/CollectiveNeoForge.class --class-name com/natamus/collective/neoforge/events/RegisterCollectiveNeoForgeEvents.class --class-name com/natamus/collective/neoforge/mixin/BaseSpawnerMixin.class --class-name com/natamus/collective/neoforge/mixin/BlockEntityMixin.class --class-name com/natamus/collective/neoforge/mixin/BoneMealItemMixin.class --class-name com/natamus/collective/neoforge/mixin/PrimaryLevelDataMixin.class --class-name com/natamus/collective_common_neoforge/CollectiveCommon.class --class-name com/natamus/collective_common_neoforge/events/CollectiveEvents.class --output evidence/raw/item8/collective-provider-r1
```

The common event path dispatches consumer entity replacement and queued
entity/runnable actions, handles player-head caching and block breaking, and
initializes shared world constants. Hooks forward block-entity/bonemeal events
and conditionally suppress experimental-world warnings. Preserve these effects;
this capture does not prove compatibility or absence of gameplay changes.
Initialization delegates and nine active NeoForge service implementations remain
to be reconciled before whole-provider membership closure. The shared mixin
plugin was already captured in 55d1c0ea and must be reused.
