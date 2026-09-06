# resourcefulconfig-provider source checkpoint

Extractor faafc001. Independent r1 reproduction matches the manifest and all
5 source files byte for byte. Manifest SHA-256:
f1d2c276dedab09562346f4dec4afdb7039c9b056602aa31e263c1ce0c47a021

```sh
uv run -m tools.inspect_item8_pool_elements --archive resourcefulconfig-neoforge-1.21-3.0.11.jar --class-name com/teamresourceful/resourcefulconfig/common/loader/JavaConfigParser.class --class-name com/teamresourceful/resourcefulconfig/mixins/common/DedicatedServerAccessor.class --class-name com/teamresourceful/resourcefulconfig/mixins/common/PlayerListAccessor.class --class-name com/teamresourceful/resourcefulconfig/mixins/common/SettingsAccessor.class --class-name com/teamresourceful/resourcefulconfig/neoforge/ResourcefulConfigNeoForge.class --output evidence/raw/item8/resourcefulconfig-provider-r1
```

Captures automatic entries, declared common hooks and service implementations.
Contribution interpretation and full archive accounting remain separate.
