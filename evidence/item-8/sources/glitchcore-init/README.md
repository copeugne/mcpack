# GlitchCore common initializer

Extractor ff38ad2. Independent r1 reproduction matches the manifest and source
byte for byte. Manifest SHA-256:
fe4eab4820bf598f4c279b41fba270159e389a15a6778e6a3c9da2073245c64a

```sh
uv run -m tools.inspect_item8_pool_elements --archive GlitchCore-neoforge-1.21.1-2.1.0.2.jar --class-name glitchcore/core/GlitchCore.class --output evidence/raw/item8/glitchcore-init-r1
```

Initialization registers the sync_config packet on the main channel. Static
initialization creates the logger, channel ID and packet handler. No independent
world content is registered. Existing packet-handler mixin evidence is reused.
