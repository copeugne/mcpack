# C2ME module initialization: c2me-opts-chunkio-entry

Extractor d7063da7914b7ba910021b92aae7b77cd250a497. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
13d8ec20161c97f7de3fd3f4b764b928a477ffa62dc1205f3edb5af76375ee4d

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-opts-chunkio-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/opts/chunkio/MixinPlugin.class --class-name com/ishland/c2me/opts/chunkio/ModuleEntryPoint.class --output evidence/raw/item8/c2me-opts-chunkio-entry-r1
```

This capture preserves the module entry and locally declared plugin boundaries.
Existing base-plugin and worldgen-threading captures are reused separately.
Module generation hooks require their own disposition before whole-provider
closure; this initialization capture does not establish a new family.

Initializes chunk I/O configuration. Plugin delegates to the captured base plugin.
