# fabric-registry-sync-v0-entry source checkpoint

Extractor a6fa580. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: c90f9978bdaed1e208676fdcad9b108f560aa95b5f6f539bdfc205460c5c056c.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-registry-sync-v0-5.3.1+f9aace1619.jar --class-name net/fabricmc/fabric/mixin/registry/sync/BaseMappedRegistryAccessor.class --class-name net/fabricmc/fabric/mixin/registry/sync/DebugChunkGeneratorAccessor.class --class-name net/fabricmc/fabric/mixin/registry/sync/MappedRegistryAccessor.class --class-name net/fabricmc/fabric/mixin/registry/sync/RegistryLoaderMixin.class --class-name net/fabricmc/fabric/mixin/registry/sync/RegistryManagerAccessor.class --class-name org/sinytra/fabric/registry_sync/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-registry-sync-v0-entry-r1
```

The initializer calls FabricRegistryInit.onInitialize, still open. RegistryLoaderMixin forwards consumer dynamic-registry setup using current registry objects; the four other hooks expose existing registry/debug state.

Source capture alone does not close whole-provider membership.
