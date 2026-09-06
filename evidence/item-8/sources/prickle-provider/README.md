# prickle-provider source checkpoint

Extractor faafc001. Independent r1 reproduction matches the manifest and all
3 source files byte for byte. Manifest SHA-256:
d74e45ef3f358e66f265369bb421d84e372521a0c2ba2e5b9e99080ce7a108e5

```sh
uv run -m tools.inspect_item8_pool_elements --archive prickle-neoforge-1.21.1-21.1.11.jar --class-name net/darkhax/pricklemc/common/impl/config/property/MinecraftPropertyPlugin.class --class-name net/darkhax/pricklemc/neoforge/impl/NeoForgeMod.class --class-name net/darkhax/pricklemc/neoforge/impl/util/NeoForgePlatformHelper.class --output evidence/raw/item8/prickle-provider-r1
```

Captures automatic entries, declared common hooks and service implementations.
Contribution interpretation and full archive accounting remain separate.
