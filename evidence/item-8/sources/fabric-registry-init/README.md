# fabric-registry-init source checkpoint

Extractor be54e72. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: ea158b38e8bf3ee48080a442721fc1e796bee22b6fb4e37e794315e7e5d5f1af.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-registry-sync-v0-5.3.1+f9aace1619.jar --class-name net/fabricmc/fabric/impl/registry/sync/FabricRegistryInit.class --output evidence/raw/item8/fabric-registry-init-r1
```

Preserves the remaining startup boundary. Provider disposition remains separate.
