# fabric-loader-mod-list source checkpoint

Extractor 34269a8. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: 329ecd4c85011b336075d95309f9f9fd0820551ec9e8b854b0413a7fad8bba70.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/forgified-fabric-loader-2.5.68+0.18.4+1.21.1-full.jar --class-name net/fabricmc/loader/impl/FabricLoaderImpl.class --output evidence/raw/item8/fabric-loader-mod-list-r1
```

The startup delegate consumes caller registrations or existing FML mod metadata.
Provider closure and full payload accounting remain separate.
