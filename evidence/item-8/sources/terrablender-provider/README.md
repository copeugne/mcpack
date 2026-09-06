# TerraBlender contribution sources

Extractor 2290d8e5. All thirteen sources and the manifest independently reproduce
byte for byte. Manifest SHA-256:
9b97ec0fcf96fdafc905d63d11397ef8caf502f9930d32ac7a470e86977c7875

```sh
uv run -m tools.inspect_item8_pool_elements --archive TerraBlender-neoforge-1.21.1-4.1.0.8.jar --class-name terrablender/core/TerraBlender.class --class-name terrablender/core/TerraBlenderNeoForge.class --class-name terrablender/handler/InitializationHandler.class --class-name terrablender/mixin/MixinBiomeSource.class --class-name terrablender/mixin/MixinBuiltInRegistries.class --class-name terrablender/mixin/MixinChunkGenerator.class --class-name terrablender/mixin/MixinMultiNoiseBiomeSource.class --class-name terrablender/mixin/MixinNoiseBasedChunkGenerator.class --class-name terrablender/mixin/MixinNoiseGeneratorSettings.class --class-name terrablender/mixin/MixinParameterList.class --class-name terrablender/mixin/MixinPrimaryLevelData.class --class-name terrablender/mixin/MixinTheEndBiomeSource.class --class-name terrablender/mixin/MultiNoiseBiomeSourceAccess.class --output evidence/raw/item8/terrablender-provider-r1
```

Preserves common/NeoForge entry, startup handler and all ten common hooks.
Hooks modify biome selection, noise/surface rules, registry bootstrap, generator
validation and world lifecycle metadata. Startup delegates to LevelUtils; resolve
that concrete initialization boundary before whole-provider closure.
