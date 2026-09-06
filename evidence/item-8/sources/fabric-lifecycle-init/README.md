# fabric-lifecycle-init source roles

Extractor 2e74941. Independent r1 reproduction matches identities.json and every
disassembly byte for byte. Manifest SHA-256:
1abb7ebad9fe2aee3ce06b5d23c59aec1beb4509d798793e9717f66f324826fe.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-lifecycle-events-v1-2.6.0+e40d8add19.jar --class-name net/fabricmc/fabric/impl/event/lifecycle/LifecycleEventsImpl.class --output evidence/raw/item8/fabric-lifecycle-init-r1
```

The initializer forwards server, world, entity, tag and chunk lifecycle events. CHUNK_GENERATE reports an already generated new chunk; it does not generate one. Unload paths enumerate existing chunks, block entities and entities. The existing WorldMixin maintains loaded-chunk membership. No independent site is introduced.

Reuse the corresponding entry capture. Client initializers are guarded by
Dist.isClient. These source roles do not prove effective consumer behavior.
