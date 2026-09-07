# Resourceful Lib startup delegates

Extractor 1101f0d1a40dc15b54dd68aa8c86e22ee8560d25. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
4f0c368751adf3de24c46be01bac5bebcfabe62347c6ddc9f5617fd0f66f1ac9

```sh
uv run -m tools.inspect_item8_pool_elements --archive resourcefullib-neoforge-1.21-3.0.12.jar --class-name com/teamresourceful/resourcefullib/ResourcefulLib.class --class-name com/teamresourceful/resourcefullib/neoforge/NeoForgeServerApiProxy.class --class-name com/teamresourceful/resourcefullib/common/network/neoforge/NeoForgeNetworking.class --output evidence/item-8/sources/resourcefullib-startup
```

Direct common initialization and server consumer API boundaries.
This capture does not establish networking or gameplay correctness.
