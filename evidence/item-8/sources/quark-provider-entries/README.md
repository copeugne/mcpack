# Remaining Quark generation entries

Extractor 3fbd2bb captures 26 previously uncaptured entry, module, feature and
mixin classes. Independent r1 extraction matches every generated file. Existing
Quark generators and module-enablement captures are reused, not repeated.
Manifest SHA-256: 46024fc051bacf39814edca480d0bf72a26ad8f1f7839b50536d13bd93910a0d.

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name 'org/violetmoon/quark/base/Quark$QuarkEventBusSubscriber.class' --class-name org/violetmoon/quark/base/Quark.class --class-name org/violetmoon/quark/content/building/module/GoldBarsModule.class --class-name org/violetmoon/quark/content/building/module/VariantChestsModule.class --class-name org/violetmoon/quark/content/mobs/module/WraithModule.class --class-name org/violetmoon/quark/content/world/feature/AncientTreeTopperDecorator.class --class-name org/violetmoon/quark/content/world/feature/GlowExtrasFeature.class --class-name org/violetmoon/quark/content/world/feature/GlowShroomsFeature.class --class-name org/violetmoon/quark/content/world/feature/MultiFoliageStraightTrunkPlacer.class --class-name org/violetmoon/quark/content/world/feature/OffsetFancyFoliagePlacer.class --class-name org/violetmoon/quark/content/world/module/AncientWoodModule.class --class-name org/violetmoon/quark/content/world/module/AzaleaWoodModule.class --class-name org/violetmoon/quark/content/world/module/GlimmeringWealdModule.class --class-name org/violetmoon/quark/content/world/module/NoMoreLavaPocketsModule.class --class-name org/violetmoon/quark/mixin/mixins/ChunkGeneratorMixin.class --class-name org/violetmoon/quark/mixin/mixins/ClimateParameterPointMixin.class --class-name org/violetmoon/quark/mixin/mixins/HugeBrownMushroomFeatureMixin.class --class-name org/violetmoon/quark/mixin/mixins/HugeRedMushroomFeatureMixin.class --class-name 'org/violetmoon/quark/mixin/mixins/NetherFortressPiecesMixin$CastleEntranceMixin.class' --class-name org/violetmoon/quark/mixin/mixins/NetherFortressPiecesMixin.class --class-name org/violetmoon/quark/mixin/mixins/ServerLevelMixin.class --class-name org/violetmoon/quark/mixin/mixins/SpawnerBlockEntityMixin.class --class-name org/violetmoon/quark/mixin/mixins/SpringFeatureMixin.class --class-name org/violetmoon/quark/mixin/mixins/WorldGenRegionMixin.class --class-name org/violetmoon/quark/mixin/mixins/accessor/AccessorOverworldBiomes.class --class-name org/violetmoon/quark/mixin/mixins/accessor/AccessorSinglePoolElement.class --output evidence/raw/item8/quark-provider-entries-r1
```

GlimmeringWealdModule calls Biolith BiomePlacement.addOverworld. Glow features
write mushroom/vegetation blocks; tree features/decorators support ancient and
azalea/blossom wood. GoldBarsModule and VariantChestsModule register structure
block replacement callbacks. These are modifications of consuming structures.

Generation mixins expose jigsaw/pool context, adjust disabled climate parameters,
modify mushroom replacement and fortress fence behavior, suppress selected lava
springs and repair WorldGenRegion chunk access. ServerLevelMixin stores a magnet
tracker. SpawnerBlockEntityMixin calls experimental SpawnerReplacerModule; its
configuration and implementation remain to be reconciled before provider closure.

Quark provider coverage remains open. Remaining work includes bundled Biolith,
full packaged-resource and remaining entry-role accounting, and the named
spawner-replacement path. This source increment establishes no final family
count or successful world placement.
