# Polymorph membership entry paths

Extractor 04670f32. Independent r1 reproduction matches source and manifest
bytes. Manifest SHA-256:
859c8ec69e6a3db415b633697ab588e0f874b69a69cfaca6440743e5ca07476a

```sh
uv run -m tools.inspect_item8_pool_elements --archive polymorph-neoforge-1.1.0+1.21.1.jar --class-name com/illusivesoulworks/polymorph/PolymorphCommonMod.class --class-name com/illusivesoulworks/polymorph/PolymorphNeoForgeMod.class --class-name com/illusivesoulworks/polymorph/mixin/IntegratedMixinPlugin.class --class-name com/illusivesoulworks/polymorph/mixin/core/AccessorAbstractFurnaceBlockEntity.class --class-name com/illusivesoulworks/polymorph/mixin/core/AccessorCrafterMenu.class --class-name com/illusivesoulworks/polymorph/mixin/core/AccessorCraftingMenu.class --class-name com/illusivesoulworks/polymorph/mixin/core/AccessorInventoryMenu.class --class-name com/illusivesoulworks/polymorph/mixin/core/AccessorSmithingTransformRecipe.class --class-name com/illusivesoulworks/polymorph/mixin/core/AccessorSmithingTrimRecipe.class --class-name com/illusivesoulworks/polymorph/mixin/core/MixinCrafterMenu.class --class-name com/illusivesoulworks/polymorph/mixin/core/MixinCraftingMenu.class --class-name com/illusivesoulworks/polymorph/mixin/core/MixinLevelChunk.class --class-name com/illusivesoulworks/polymorph/mixin/core/MixinPolymorphApi.class --class-name com/illusivesoulworks/polymorph/mixin/core/MixinPolymorphWidgets.class --class-name com/illusivesoulworks/polymorph/mixin/core/MixinRecipeCache.class --class-name com/illusivesoulworks/polymorph/mixin/core/MixinRecipeManager.class --class-name com/illusivesoulworks/polymorph/mixin/core/MixinServerLevel.class --class-name com/illusivesoulworks/polymorph/mixin/core/MixinSmithingMenu.class --class-name com/illusivesoulworks/polymorph/mixin/integration/emi/MixinEmiRecipeFiller.class --class-name com/illusivesoulworks/polymorph/mixin/integration/fastbench/MixinFastBenchUtil.class --class-name com/illusivesoulworks/polymorph/mixin/integration/jei/MixinPacketRecipeTransfer.class --class-name com/illusivesoulworks/polymorph/mixin/integration/jei/MixinRecipeTransferUtil.class --class-name com/illusivesoulworks/polymorph/mixin/integration/roughlyenoughitems/MixinInternalWidgets.class --class-name com/illusivesoulworks/polymorph/platform/NeoForgeClientPlatform.class --class-name com/illusivesoulworks/polymorph/platform/NeoForgeIntegrationPlatform.class --class-name com/illusivesoulworks/polymorph/platform/NeoForgePlatform.class --output evidence/raw/item8/polymorph-provider-r1
```

Captures the sole automatic entry, three services, all 15 core common hooks,
five declared integration hooks, their plugin and common initialization. Chunk
and server-level hooks set recipe context around existing block ticks. Other
hooks support recipe selection/transfers, caches, menus and widgets. Integration
failures can disable modules with warnings; do not treat startup as compatibility
proof. Startup capability, event, payload and integration delegates remain to
be bound before provider closure.
