# C2ME module initialization: c2me-rewrites-chunk-system-entry

Extractor d7063da7914b7ba910021b92aae7b77cd250a497. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
99c302c49b5096ddb28f9063c46c2be0fb7678b8598474c933e408f09a67c38f

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-rewrites-chunk-system-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/rewrites/chunksystem/MixinPlugin.class --class-name com/ishland/c2me/rewrites/chunksystem/ModuleEntryPoint.class --output evidence/raw/item8/c2me-rewrites-chunk-system-entry-r1
```

This capture preserves the module entry and locally declared plugin boundaries.
Existing base-plugin and worldgen-threading captures are reused separately.
Module generation hooks require their own disposition before whole-provider
closure; this initialization capture does not establish a new family.

Initializes chunk-system configuration. Plugin selects fluid-postprocessing and async-serialization hooks using configuration flags.
