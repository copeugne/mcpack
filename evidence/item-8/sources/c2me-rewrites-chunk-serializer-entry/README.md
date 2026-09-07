# C2ME module initialization: c2me-rewrites-chunk-serializer-entry

Extractor d7063da7914b7ba910021b92aae7b77cd250a497. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
319118d996369d674cc6f00798fc4eb92166af1a8c698d308143a5d7f28a79a2

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-rewrites-chunk-serializer-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/rewrites/chunk_serializer/ModuleEntryPoint.class --class-name com/ishland/c2me/rewrites/chunk_serializer/TheMod.class --output evidence/raw/item8/c2me-rewrites-chunk-serializer-entry-r1
```

This capture preserves the module entry and locally declared plugin boundaries.
Existing base-plugin and worldgen-threading captures are reused separately.
Module generation hooks require their own disposition before whole-provider
closure; this initialization capture does not establish a new family.

Reads serializer enablement. TheMod registers a serializer of supplied ServerLevel/ChunkAccess state using ChunkDataSerializer and NbtWriter; this is persistence of existing chunks, not content registration.
