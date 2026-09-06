# BCLib entry points and generation hooks

Extractor commit: 6dc79d34a524931de84d81082b8ddb23a9441c39.
Independent r1 reproduction matches all 16 disassemblies and the identity
manifest byte for byte. Manifest SHA-256:
92b75f9b0a82c47cfbc2be5f2fe3606e4894ba90b8d5fe922e30af908eb4b56a

```sh
uv run -m tools.inspect_item8_pool_elements --archive bclib-21.0.24.jar --class-name org/betterx/bclib/api/v2/dataexchange/handler/DataExchange.class --class-name org/betterx/bclib/api/v2/dataexchange/handler/DataExchangeClientEvents.class --class-name org/betterx/bclib/api/v2/spawning/SpawnRuleBuilder.class --class-name org/betterx/bclib/client/BCLibClient.class --class-name org/betterx/bclib/mixin/common/BiomeGenerationSettingsAccessor.class --class-name org/betterx/bclib/mixin/common/BiomeMixin.class --class-name org/betterx/bclib/mixin/common/BoneMealItemMixin.class --class-name org/betterx/bclib/mixin/common/ChunkGeneratorMixin.class --class-name org/betterx/bclib/mixin/common/MobSpawnSettingsAccessor.class --class-name org/betterx/bclib/mixin/common/RegistryDataLoaderMixin.class --class-name org/betterx/bclib/mixin/common/ServerLevelMixin.class --class-name org/betterx/bclib/mixin/common/WorldGenRegionMixin.class --class-name org/betterx/bclib/particles/ParticleFactoryRegistry.class --class-name org/betterx/bclib/registry/BaseBlockEntityRenders.class --class-name org/betterx/bclib/registry/FuelRegistry.class --class-name org/betterx/bclib/server/BCLibServer.class --output evidence/raw/item8/bclib-provider-entry-r1
```

This capture covers the eight automatic entry classes beyond the previously
retained BCLib main class, plus eight biome/generation-related common hooks.
Client entries manage models, particles, renderers and data exchange. The server
entry invokes integration registration, server data exchange and PostInitAPI.
FuelRegistry handles existing fuel burn time. SpawnRuleBuilder starts with an
empty pending list and registers consumer-supplied entity spawn placements.

ChunkGeneratorMixin changes feature seeds through a rotating seed and resets
its counter at biome decoration entry. WorldGenRegionMixin replaces the write
check with a chunk-distance condition, permitting coordinates within one chunk
of the center on both horizontal axes. These affect generation behavior but do
not themselves introduce a named family. Preserve these effects for attribution.
Biome generation/spawn accessors expose existing data; BiomeMixin has only its
constructor. RegistryDataLoaderMixin's injected initializer is empty, alongside
its mutable registry accessor. ServerLevelMixin remembers the world identifier.
BoneMealItemMixin delegates consumer spreading to BonemealAPI.

The capture does not yet close the complete provider. Resolve PostInitAPI's
registered consumers and reconcile the remaining packaged/hook roles before
closing BCLib membership. Do not expand this into generic networking, recipe,
rendering or fuel-behavior audits.
