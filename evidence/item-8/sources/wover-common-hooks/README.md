# WorldWeaver common hooks

Extractor 42729dd58c5b1b9e78de471c7c86f4819f9b44fb. Independent r1 reproduction
matches all 45 declared common-hook disassemblies and the identity manifest.
Manifest SHA-256: 4cd9101a82b4be679faa5f0e691a0f6fd095bb6f8c4d9542ab2de3b23f173fb2

```sh
uv run -m tools.inspect_item8_pool_elements --archive worldweaver-21.0.24.jar --class-name org/betterx/wover/biome/mixin/BiomeGenerationSettingsAccessor.class --class-name org/betterx/wover/biome/mixin/ChunkGeneratorAccessor.class --class-name org/betterx/wover/biome/mixin/HolderSetNamedAccessor.class --class-name org/betterx/wover/biome/mixin/NoiseBasedChunkGeneratorMixin.class --class-name org/betterx/wover/block/mixin/BlockAccessorMixin.class --class-name org/betterx/wover/block/mixin/ModelProviderMixin.class --class-name org/betterx/wover/common/mixin/BiomeSourceAccessor.class --class-name org/betterx/wover/core/mixin/registry/MappedRegistryMixin.class --class-name org/betterx/wover/core/mixin/registry/RegistryDataLoaderMixin.class --class-name org/betterx/wover/core/mixin/registry/RegistryDataLoaderMixinEarly.class --class-name org/betterx/wover/core/mixin/registry/VanillaRegistriesMixin.class --class-name org/betterx/wover/events/mixin/MinecraftServerMixin.class --class-name org/betterx/wover/events/mixin/ReloadableServerResourcesMixin.class --class-name org/betterx/wover/events/mixin/create_new_world_folder/WorldDimensionDataMixin.class --class-name org/betterx/wover/events/mixin/dimension_load/WorldStemMixin.class --class-name org/betterx/wover/events/mixin/resource_manager/MinecraftServerMixin.class --class-name org/betterx/wover/events/mixin/resource_manager/WorldStemMixin.class --class-name org/betterx/wover/events/mixin/server_level_ready/ServerLevelMixin.class --class-name org/betterx/wover/events/mixin/world_folder/MainMixin.class --class-name org/betterx/wover/events/mixin/world_registry/WorldDimensionDataMixin.class --class-name org/betterx/wover/events/mixin/world_registry/WorldLoaderMixin.class --class-name org/betterx/wover/events/mixin/world_registry/WorldStemMixin.class --class-name org/betterx/wover/generator/mixin/biomesource/BiomeSourcePrintMixin.class --class-name org/betterx/wover/generator/mixin/biomesource/MultiNoiseBiomeSourceParameterListAccessor.class --class-name org/betterx/wover/generator/mixin/biomesource/MultiNoiseBiomeSourceParameterListMixin.class --class-name org/betterx/wover/generator/mixin/biomesource/ServerLevelMixin.class --class-name org/betterx/wover/generator/mixin/biomesource/TheEndBiomeSourceMixin.class --class-name org/betterx/wover/generator/mixin/generator/ChunkGeneratorMixin.class --class-name org/betterx/wover/generator/mixin/generator/ChunkGeneratorPrintMixin.class --class-name org/betterx/wover/generator/mixin/generator/NoiseBasedChunkGeneratorMixin.class --class-name org/betterx/wover/item/mixin/item_stack_setup/CraftingRecipeMixin.class --class-name org/betterx/wover/item/mixin/item_stack_setup/ItemInputMixin.class --class-name org/betterx/wover/item/mixin/item_stack_setup/LootItemFunctionMixin.class --class-name org/betterx/wover/item/mixin/item_stack_setup/SmithingTransformRecipeMixin.class --class-name org/betterx/wover/poi/mixin/PoiTypeMixin.class --class-name org/betterx/wover/potions/mixin/PotionBrewingMixin.class --class-name org/betterx/wover/preset/mixin/DedicatedServerPropertiesMixin.class --class-name org/betterx/wover/preset/mixin/WorldDimensionDataMixin.class --class-name org/betterx/wover/preset/mixin/WorldPresetAccessor.class --class-name org/betterx/wover/recipe/mixin/RecipeManagerMixin.class --class-name org/betterx/wover/recipe/mixin/ServerAdvancementManagerMixin.class --class-name org/betterx/wover/surface/mixin/NoiseBasedChunkGeneratorMixin.class --class-name org/betterx/wover/surface/mixin/NoiseGeneratorSettingsMixin.class --class-name org/betterx/wover/surface/mixin/SurfaceRulesContextAccessor.class --class-name org/betterx/wover/tag/mixin/TagLoaderMixin.class --output evidence/raw/item8/wover-common-hooks-r1
```

The hooks expose registry/generation state and dispatch lifecycle, resource and
registry events. RegistryDataLoader invokes DatapackRegistryBuilderImpl's
consumer bootstrap. Biome generation rebuilds feature steps and integrates
consumer Nether/End biome choices. Generator hooks expose preset/noise settings
and diagnostics; surface hooks inject rules. Other hooks handle model datagen,
item-stack setup, potions, POIs, runtime recipes/advancements and tags.

These are real generation and gameplay effects, not proof of unchanged
behavior. NoiseGeneratorSettingsMixin permits replacing an already replaced
surface-rule set and logs a warning. Its getOriginalSurfaceRules method returns
the current field, not an independently retained original value. Preserve this
limitation; no compatibility fix or tuning is part of membership enumeration.

This is an isolated generated source increment, with no unrelated code changes.
The size follows the complete finite declared-hook list. Do not expand it into
generic event/recipe/network implementation audits. Reconcile the remaining
direct registry/bootstrap inputs before closing WorldWeaver membership.
