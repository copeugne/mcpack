# Architectury provider entry paths

Extractor b91775ad. Independent r1 reproduction matches all source and manifest
bytes. Manifest SHA-256:
74ab5cf158c0e545d102726828fd146a836d24c24010809d2aa02f3a17f672c1

```sh
uv run -m tools.inspect_item8_pool_elements --archive architectury-13.0.8-neoforge.jar --class-name dev/architectury/mixin/MixinLightningBolt.class --class-name dev/architectury/mixin/forge/MixinFallingBlockEntity.class --class-name dev/architectury/mixin/forge/MixinInventory.class --class-name dev/architectury/mixin/forge/MixinItemExtension.class --class-name dev/architectury/mixin/forge/MixinLevelEvent.class --class-name dev/architectury/mixin/forge/neoforge/BucketItemAccessor.class --class-name dev/architectury/mixin/forge/neoforge/LiquidBlockAccessor.class --class-name dev/architectury/mixin/forge/neoforge/MixinBucketItem.class --class-name dev/architectury/mixin/forge/neoforge/MixinChunkSerializer.class --class-name dev/architectury/mixin/inject/MixinBlock.class --class-name dev/architectury/mixin/inject/MixinBucketItem.class --class-name dev/architectury/mixin/inject/MixinEntityType.class --class-name dev/architectury/mixin/inject/MixinFluid.class --class-name dev/architectury/mixin/inject/MixinFoodPropertiesBuilder.class --class-name dev/architectury/mixin/inject/MixinItem.class --class-name dev/architectury/mixin/inject/MixinItemProperties.class --class-name dev/architectury/mixin/inject/MixinLiquidBlock.class --class-name dev/architectury/neoforge/ArchitecturyNeoForge.class --class-name dev/architectury/plugin/forge/ArchitecturyMixinPlugin.class --output evidence/raw/item8/architectury-provider-r1
```

One automatic entry, all 17 common hooks and the plugin. Hooks expose consumer
item/fluid extensions, forward existing events and attach level context to chunk
events. The plugin returns the already declared NeoForge chunk serializer hook.
Remaining membership boundary: startup event and biome modification registration.
