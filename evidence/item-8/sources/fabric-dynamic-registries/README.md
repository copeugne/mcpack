# fabric-dynamic-registries source checkpoint

Extractor 34269a8. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: 648c159c662bbd522074b4b61f7f1814689803cb8aa125918ac4614f83868ac1.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-registry-sync-v0-5.3.1+f9aace1619.jar --class-name net/fabricmc/fabric/impl/registry/sync/DynamicRegistriesImpl.class --output evidence/raw/item8/fabric-dynamic-registries-r1
```

The startup delegate consumes caller registrations or existing FML mod metadata.
Provider closure and full payload accounting remain separate.
