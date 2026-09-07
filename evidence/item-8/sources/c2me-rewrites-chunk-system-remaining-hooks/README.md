# C2ME declared hooks: c2me-rewrites-chunk-system-remaining-hooks

Extractor 5347ff21fd07a10e07ed7fc4c6057342100cf211. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
04e397af4ba1f01ddcd4210b154512e60d0ea8d083a4be022ba816cf7e63c1a8

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-rewrites-chunk-system-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/rewrites/chunksystem/mixin/MixinChunkHolder.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/MixinChunkTicketManager.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/MixinChunkTicketManagerTicketDistanceLevelPropagator.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/MixinMinecraftServer.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/MixinPointOfInterestStorage.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/MixinSerializingRegionBasedStorage.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/MixinServerChunkManager.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/MixinThreadedAnvilChunkStorage.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/async_serialization/MixinBlender.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/async_serialization/MixinChunkRegion.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/async_serialization/MixinChunkSerializer.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/async_serialization/MixinProtoChunk.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/async_serialization/MixinSerializingRegionBasedStorage.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/async_serialization/MixinStorageIoWorker.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/async_serialization/MixinThreadedAnvilChunkStorage.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/async_serialization/gc_free_serializer/MixinChunkDataSerializer.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/fixes/MixinServerEntityManager.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/fluid_postprocessing/MixinWorldChunk.class --output evidence/raw/item8/c2me-rewrites-chunk-system-remaining-hooks-r1
```

This retains the remaining declared common/server hooks in this module.
Previously captured hooks are reused. The null scheduling declaration has
no class target and is preserved as packaged, not replaced or counted.
The raw disassemblies are isolated generated evidence for membership review;
this capture alone is not whole-provider closure or operational validation.

Hooks replace chunk holder/ticket lifecycle, manage POI/chunk storage, defer main-thread I/O work, track blending futures, unload entities and reschedule existing fluid ticks. They operate on existing world/chunk state; no authored structure is registered.

This identifies membership roles. It does not prove runtime activation,
unchanged world generation, persistence safety or concurrency correctness.
Do not turn this into a generic scheduler, I/O or network implementation audit.
