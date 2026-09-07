# C2ME module initialization: c2me-rewrites-chunkio-entry

Extractor d7063da7914b7ba910021b92aae7b77cd250a497. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
3b3cc808b3a6e0a9e3fa857f1e41d21cc75192f4adaf1ad87ac1f4fdc7ac12b7

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-rewrites-chunkio-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/rewrites/chunkio/ModuleEntryPoint.class --output evidence/raw/item8/c2me-rewrites-chunkio-entry-r1
```

This capture preserves the module entry and locally declared plugin boundaries.
Existing base-plugin and worldgen-threading captures are reused separately.
Module generation hooks require their own disposition before whole-provider
closure; this initialization capture does not establish a new family.

Reads chunk I/O rewrite enablement using the existing config accessor.
