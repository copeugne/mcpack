# Resourceful Lib storage initializer

Extractor cb9ebbbf5898051d9296ae16a0f1a5c88ac75597. Independent r1 reproduction matches the
disassembly and identity manifest. Manifest SHA-256:
46287b67e6639ab6c2221f5ef5cab188c0ee46182920254ca63a84ab5353aa7a

```sh
uv run -m tools.inspect_item8_pool_elements --archive resourcefullib-neoforge-1.21-3.0.12.jar --class-name com/teamresourceful/resourcefullib/common/utils/files/GlobalStorage.class --output evidence/item-8/sources/resourcefullib-storage
```

Direct initialization target from ResourcefulLib.init, for membership inspection.
No general persistence or serialization correctness claim.
