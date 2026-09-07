# Zeta provider entry and hook sources

Extractor 053d8a2 captures 25 previously uncaptured entry, proxy, plugin,
structure-replacement and declared common mixin classes. Existing configuration
and generation dispatch captures are reused. Independent r1 extraction matches
every generated file byte for byte.
Manifest SHA-256: 735e88c82e649abe73822a432ba2e9a71c1c67387e0236aaa0ca88bbfea94099.

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zeta/Zeta.class --class-name org/violetmoon/zeta/mixin/mixins/AccessorBlock.class --class-name org/violetmoon/zeta/mixin/mixins/AccessorContextAwarePredicate.class --class-name org/violetmoon/zeta/mixin/mixins/AccessorItem.class --class-name org/violetmoon/zeta/mixin/mixins/AccessorLootPool.class --class-name org/violetmoon/zeta/mixin/mixins/AccessorLootTable.class --class-name org/violetmoon/zeta/mixin/mixins/AccessorPistonStructureResolver.class --class-name org/violetmoon/zeta/mixin/mixins/CreativeModeTabsMixin.class --class-name org/violetmoon/zeta/mixin/mixins/InvokerBlockBehavior.class --class-name org/violetmoon/zeta/mixin/mixins/InvokerSpawnPlacements.class --class-name org/violetmoon/zeta/mixin/mixins/PistonBaseBlockMixin.class --class-name org/violetmoon/zeta/mixin/mixins/RegistryDataLoaderMixin.class --class-name org/violetmoon/zeta/mixin/mixins/StructurePieceMixin.class --class-name org/violetmoon/zeta/mixin/mixins/StructureStartMixin.class --class-name org/violetmoon/zeta/mixin/mixins/StructureTemplateMixin.class --class-name org/violetmoon/zeta/mixin/plugin/InterfaceDelegateMixinPlugin.class --class-name org/violetmoon/zeta/mod/ZetaMod.class --class-name org/violetmoon/zeta/util/handler/StructureBlockReplacementHandler.class --class-name org/violetmoon/zetaimplforge/ForgeZeta.class --class-name org/violetmoon/zetaimplforge/mixin/mixins/AccessorPotionBrewing.class --class-name org/violetmoon/zetaimplforge/mixin/mixins/WeatheringCopperMixin.class --class-name org/violetmoon/zetaimplforge/mixin/mixins/self/IZetaBlockMixin.class --class-name org/violetmoon/zetaimplforge/mixin/mixins/self/IZetaItemMixin.class --class-name org/violetmoon/zetaimplforge/mod/ZetaModCommonProxy.class --class-name org/violetmoon/zetaimplforge/mod/ZetaModForge.class --output evidence/raw/item8/zeta-provider-r1
```

ZetaMod starts a Zeta instance and calls loadModules with null categories and
module finder plus ZetaGeneralConfig. The common proxy bridges loader/play
events and registers the existing Zeta biome modifier. StructureStart hooks
set and clear current structure context; StructurePiece and StructureTemplate
hooks call registered block-state transformations on existing generated content.
The handler stores consumer-supplied replacement functions.

The interface-delegate plugin transforms declared annotated interface methods,
not a packaged structure layout. RegistryDataLoaderMixin invokes
RegisterDynamicUtil.onRegisterDynamic; that exact registration callback remains
to be reconciled before closing provider scope. Piston and creative-tab hooks
modify existing behavior, and accessors expose underlying game state.

This is a source increment, not a provider closure or runtime placement claim.
