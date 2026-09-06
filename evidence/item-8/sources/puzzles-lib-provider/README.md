# Puzzles Lib membership entry paths

Extractor 57e3faba. Independent r1 reproduction matches all source and manifest
bytes. Manifest SHA-256:
c78df917ecd4e021c8aa397744fc270c2769e4408f94cf2eb8b404af0f6e07df

```sh
uv run -m tools.inspect_item8_pool_elements --archive PuzzlesLib-v21.1.52-1.21.1-NeoForge.jar --class-name fuzs/puzzleslib/impl/PuzzlesLib.class --class-name fuzs/puzzleslib/impl/PuzzlesLibMod.class --class-name fuzs/puzzleslib/mixin/AbstractMinecartMixin.class --class-name fuzs/puzzleslib/mixin/DataCommandsMixin.class --class-name fuzs/puzzleslib/mixin/EnchantCommandMixin.class --class-name fuzs/puzzleslib/mixin/MixinConfigPluginImpl.class --class-name fuzs/puzzleslib/mixin/server/DedicatedServerSettingsMixin.class --class-name fuzs/puzzleslib/mixin/server/EulaMixin.class --class-name fuzs/puzzleslib/neoforge/impl/PuzzlesLibNeoForge.class --class-name fuzs/puzzleslib/neoforge/impl/client/PuzzlesLibNeoForgeClient.class --class-name fuzs/puzzleslib/neoforge/impl/client/core/NeoForgeClientProxy.class --class-name fuzs/puzzleslib/neoforge/impl/core/NeoForgeCommonProxy.class --class-name fuzs/puzzleslib/neoforge/impl/core/NeoForgeEnvironment.class --class-name fuzs/puzzleslib/neoforge/mixin/AbstractPackResourcesNeoForgeMixin.class --class-name fuzs/puzzleslib/neoforge/mixin/DatagenModLoaderNeoForgeMixin.class --class-name fuzs/puzzleslib/neoforge/mixin/EnchantedCountIncreaseFunctionNeoForgeMixin.class --class-name fuzs/puzzleslib/neoforge/mixin/EnchantmentHelperNeoForgeMixin.class --class-name fuzs/puzzleslib/neoforge/mixin/LootItemRandomChanceWithEnchantedBonusConditionNeoForgeMixin.class --class-name fuzs/puzzleslib/neoforge/mixin/MenuProviderWithDataNeoForgeMixin.class --class-name fuzs/puzzleslib/neoforge/mixin/MixinConfigPluginNeoForgeImpl.class --class-name fuzs/puzzleslib/neoforge/mixin/TagsProviderNeoForgeMixin.class --class-name fuzs/puzzleslib/neoforge/mixin/accessor/BiomeSpecialEffectsBuilderNeoForgeAccessor.class --class-name fuzs/puzzleslib/neoforge/mixin/accessor/MobSpawnSettingsBuilderNeoForgeAccessor.class --class-name fuzs/puzzleslib/neoforge/mixin/accessor/NewRegistryEventNeoForgeAccessor.class --output evidence/raw/item8/puzzles-lib-provider-r1
```

Captures both automatic entries, three services, two common initializers, both
plugins and all 15 declared common/server hooks. Hooks expose consumer minecart,
loot-bonus, menu, data-generation and biome/registry APIs. Plugins gate development
command, EULA, settings and resource hooks. Remaining membership check is the
common proxy/event registration delegate, not generic consumer API internals.
