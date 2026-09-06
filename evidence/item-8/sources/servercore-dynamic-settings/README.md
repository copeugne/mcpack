# ServerCore dynamic setting boundary

Extractor 7f2b8b0089d7cec25b09cd1181be6a5b0c0681c0. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
89ca2250b255166ddc1e54c4628d33b97b7de6e65a756f45e4b72acc173cfa16

```sh
uv run -m tools.inspect_item8_pool_elements --archive servercore-neoforge-1.5.17+1.21.1.jar --class-name me/wesley1808/servercore/common/dynamic/DynamicManager.class --class-name me/wesley1808/servercore/common/dynamic/DynamicSetting.class --output evidence/item-8/sources/servercore-dynamic-settings
```

Server tick callback boundary for provider membership, not performance acceptance.
