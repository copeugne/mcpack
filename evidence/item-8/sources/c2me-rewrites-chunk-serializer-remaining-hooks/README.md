# C2ME declared hooks: c2me-rewrites-chunk-serializer-remaining-hooks

Extractor 5347ff21fd07a10e07ed7fc4c6057342100cf211. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
71fbca4721b7268102b908436312ca7df47a36d5920b2e3e4eef9813cc7d112b

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-rewrites-chunk-serializer-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/rewrites/chunk_serializer/mixin/ChunkStatusMixin.class --class-name com/ishland/c2me/rewrites/chunk_serializer/mixin/GenerationStepCarverMixin.class --class-name com/ishland/c2me/rewrites/chunk_serializer/mixin/HeightMapTypeMixin.class --class-name com/ishland/c2me/rewrites/chunk_serializer/mixin/IStarlightSaveState.class --class-name com/ishland/c2me/rewrites/chunk_serializer/mixin/IdentifierMixin.class --class-name com/ishland/c2me/rewrites/chunk_serializer/mixin/MixinThreadedAnvilChunkStorage.class --output evidence/raw/item8/c2me-rewrites-chunk-serializer-remaining-hooks-r1
```

This retains the remaining declared common/server hooks in this module.
Previously captured hooks are reused. The null scheduling declaration has
no class target and is preserved as packaged, not replaced or counted.
The raw disassemblies are isolated generated evidence for membership review;
this capture alone is not whole-provider closure or operational validation.

Hooks cache existing identifiers and serialize supplied chunks into region storage. No generation definition or family is added.

This identifies membership roles. It does not prove runtime activation,
unchanged world generation, persistence safety or concurrency correctness.
Do not turn this into a generic scheduler, I/O or network implementation audit.
