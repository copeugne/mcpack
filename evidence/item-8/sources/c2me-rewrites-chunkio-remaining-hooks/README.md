# C2ME declared hooks: c2me-rewrites-chunkio-remaining-hooks

Extractor 5347ff21fd07a10e07ed7fc4c6057342100cf211. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
441febfb28f7f9f538938045b550da27fd2a17c6ca8c2167625fb52f717ab0c5

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-rewrites-chunkio-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/rewrites/chunkio/mixin/MixinChunkPosKeyedStorage.class --class-name com/ishland/c2me/rewrites/chunkio/mixin/MixinRecreatedChunkStorage.class --class-name com/ishland/c2me/rewrites/chunkio/mixin/MixinRecreationStorage.class --class-name com/ishland/c2me/rewrites/chunkio/mixin/MixinStorageIoWorker.class --class-name com/ishland/c2me/rewrites/chunkio/mixin/MixinVersionedChunkStorage.class --output evidence/raw/item8/c2me-rewrites-chunkio-remaining-hooks-r1
```

This retains the remaining declared common/server hooks in this module.
Previously captured hooks are reused. The null scheduling declaration has
no class target and is preserved as packaged, not replaced or counted.
The raw disassemblies are isolated generated evidence for membership review;
this capture alone is not whole-provider closure or operational validation.

Hooks replace storage workers for existing chunk/region data. They do not register structure content.

This identifies membership roles. It does not prove runtime activation,
unchanged world generation, persistence safety or concurrency correctness.
Do not turn this into a generic scheduler, I/O or network implementation audit.
