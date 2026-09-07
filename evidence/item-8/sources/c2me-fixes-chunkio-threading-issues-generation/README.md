# C2ME generation hooks: c2me-fixes-chunkio-threading-issues-generation

Extractor 736d66fa99506e243106ed8b93d63410546b5417. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
6166aed243bd1e1b4e92614bc95f2c603be22b945f82758ab0f1aeb12f9c8d31

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-fixes-chunkio-threading-issues-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/fixes/chunkio/threading_issues/mixin/MixinStructurePoolElement.class --output evidence/raw/item8/c2me-fixes-chunkio-threading-issues-generation-r1
```

This capture retains the pool/generation boundary for membership inspection.
It does not establish whole-provider closure or unchanged generation outcomes.

The sole hook wraps StructurePoolElement.CODEC in SynchronizedCodec at class initialization. Inspect that wrapper to finish this module membership boundary; it is not a new pool-element registration.
