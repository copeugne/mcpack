# BetterEnd remaining declared common mixins

Selector e1bffd9 captures the remaining 26 of 32 declared common mixins. The six
previous End-city, dragon, platform, podium and spike hooks are reused from
betterend-pillar-end-hooks. The complete new capture reproduces exactly against
fresh r1 output. Manifest SHA-256: 5dd3d155fcd660a11f2950742cffce16b67fba212735daa59ef83c8948d7d9a1.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BetterEnd-21.0.31.jar --class-name org/betterx/betterend/mixin/common/BlueprintModdedBiomeSourceAccessor.class --class-name org/betterx/betterend/mixin/common/CauldronFluidContentMixin.class --class-name org/betterx/betterend/mixin/common/ChorusFlowerBlockMixin.class --class-name org/betterx/betterend/mixin/common/ChorusPlantBlockMixin.class --class-name org/betterx/betterend/mixin/common/ChorusPlantFeatureMixin.class --class-name org/betterx/betterend/mixin/common/CraftingMenuMixin.class --class-name org/betterx/betterend/mixin/common/EndPortalBlockMixin.class --class-name org/betterx/betterend/mixin/common/EnderManMixin.class --class-name org/betterx/betterend/mixin/common/LevelMixin.class --class-name org/betterx/betterend/mixin/common/LivingEntityMixin.class --class-name org/betterx/betterend/mixin/common/NoiseBasedChunkGeneratorAccessor.class --class-name org/betterx/betterend/mixin/common/NoiseBasedChunkGeneratorHeightMixin.class --class-name org/betterx/betterend/mixin/common/NoiseChunkAccessor.class --class-name org/betterx/betterend/mixin/common/NoiseChunkMixin.class --class-name org/betterx/betterend/mixin/common/NoiseGeneratorSettingsMixin.class --class-name org/betterx/betterend/mixin/common/NoiseInterpolatorAccessor.class --class-name org/betterx/betterend/mixin/common/PlayerAdvancementsMixin.class --class-name org/betterx/betterend/mixin/common/PlayerMixin.class --class-name org/betterx/betterend/mixin/common/RecipeOutputExtensionMixin.class --class-name org/betterx/betterend/mixin/common/RecipeOutputMixin.class --class-name org/betterx/betterend/mixin/common/RegistrationEventsMixin.class --class-name org/betterx/betterend/mixin/common/ServerLevelMixin.class --class-name org/betterx/betterend/mixin/common/SlimeMixin.class --class-name org/betterx/betterend/mixin/common/StructureMixin.class --class-name org/betterx/betterend/mixin/common/WorldGenRegionMixin.class --class-name org/betterx/betterend/mixin/common/portal/EntityMixin.class --output evidence/raw/item8/betterend-common-mixins-r1
```

| Remaining declared hooks | Consumer role |
| --- | --- |
| BlueprintModdedBiomeSourceAccessor, NoiseBasedChunkGeneratorAccessor, NoiseChunkAccessor, NoiseInterpolatorAccessor | Access to existing biome-source and terrain-generator fields. |
| NoiseGeneratorSettingsMixin, NoiseChunkMixin, NoiseBasedChunkGeneratorHeightMixin | Target flags, density-slice filling and base-height/column queries through the already captured TerrainGenerator. Terrain generation, not a separate authored structure root. |
| ServerLevelMixin | TerrainGenerator server-level initialization, dragon-fight option and BetterEnd ice ticking behavior. |
| StructureMixin | Looks up the existing structure's registry key and applies the configured toggle. Disabled structures return INVALID_START; no additional generator. |
| WorldGenRegionMixin | Replaces ensureCanWrite with a check that each chunk-axis distance from the center is less than two. This changes the write boundary for existing generation, with no new candidate identity. |
| ChorusFlowerBlockMixin, ChorusPlantBlockMixin, ChorusPlantFeatureMixin | Chorus growth, survival, connections, shape and vegetation placement on chorus nylium. |
| EndPortalBlockMixin, LevelMixin | Configured End spawn location. Reuse the previously bound changeSpawn=false setting. |
| PlayerMixin | Respawn positioning around a respawn obelisk. Existing player/block interaction, not world-generated architecture. |
| EnderManMixin, LivingEntityMixin, SlimeMixin | Existing entity equipment/effects, attributes, damage/knockback and slime sizing/removal. |
| PlayerAdvancementsMixin | Dispatches the existing advancement callback. This does not by itself register any listener or place a structure. |
| CraftingMenuMixin, RecipeOutputMixin, RecipeOutputExtensionMixin | Crafting-table validity and recipe identifier support. |
| CauldronFluidContentMixin, RegistrationEventsMixin | Guards against repeated initialization. |
| portal.EntityMixin | Empty packaged mixin body apart from its constructor. |

These are candidate-coverage roles of the declared hooks, not proof that every
injection executed or that competing mods have identical behavior. Keep generation
write-boundary and structure-toggle effects in their existing placement inputs;
do not repair the baseline or add a geometry/performance investigation here.
Remaining BetterEnd census work concerns other feature consumers and the shared
Wover modifiers. Existing roots, templates and compatibility boundaries stay closed.
