# fabric-lifecycle-entry source roles

Extractor a2c1e65. Independent r1 reproduction matches the manifest and every
disassembly byte for byte. Manifest SHA-256:
81ff99421170db72fbeeb1e0bb07befbddf71c8dae57b6a037860883a83409b6.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-lifecycle-events-v1-2.6.0+e40d8add19.jar --class-name net/fabricmc/fabric/mixin/event/lifecycle/ChunkGeneratingMixin.class --class-name net/fabricmc/fabric/mixin/event/lifecycle/ChunkHolderMixin.class --class-name net/fabricmc/fabric/mixin/event/lifecycle/MinecraftServerMixin.class --class-name net/fabricmc/fabric/mixin/event/lifecycle/ServerWorldMixin.class --class-name net/fabricmc/fabric/mixin/event/lifecycle/ServerWorldServerEntityHandlerMixin.class --class-name net/fabricmc/fabric/mixin/event/lifecycle/WorldMixin.class --class-name net/fabricmc/fabric/mixin/event/lifecycle/server/WorldChunkMixin.class --class-name org/sinytra/fabric/lifecycle_events/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-lifecycle-entry-r1
```

Declared common/server mixins forward chunk-status, entity/block-entity load/unload, save, reload and tick notifications. WorldMixin tracks loaded chunks. The loader calls net/fabricmc/fabric/impl/event/lifecycle/LifecycleEventsImpl.onInitialize; that server initializer remains open. Client initialization is guarded.

The initial extraction attempt was rejected by argument parsing because the
new nested archives were absent from the allowlist. No output was produced;
a2c1e65 adds the exact nested identities before this successful capture.
These are source roles, not whole-provider closure or effective-consumer proof.
