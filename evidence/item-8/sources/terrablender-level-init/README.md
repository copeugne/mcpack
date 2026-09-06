# TerraBlender server initialization

Extractor 3c802c77. Independent r1 reproduction matches the manifest and source
byte for byte. Manifest SHA-256:
53230a431dda07c58b9c5be768a13002a9bcc40d4e846bda2346a3578747b8ab

```sh
uv run -m tools.inspect_item8_pool_elements --archive TerraBlender-neoforge-1.21.1-4.1.0.8.jar --class-name terrablender/util/LevelUtils.class --output evidence/raw/item8/terrablender-level-init-r1
```

The server-start path enumerates existing dimension stems and initializes their
biome sources using the world seed and region/dimension tags. It appends consumer
biomes, initializes region parameter maps and selects surface-rule categories.
It does not define or place an independent authored structure.
