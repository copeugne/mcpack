# C2ME module initialization: c2me-opts-scheduling-entry

Extractor d7063da7914b7ba910021b92aae7b77cd250a497. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
9e09f9372f53d604bc12756992c6dfcc310a8d993e7487dd2278d219ee989daa

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-opts-scheduling-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/opts/scheduling/ModuleEntryPoint.class --class-name com/ishland/c2me/opts/scheduling/mixin/MixinPlugin.class --output evidence/raw/item8/c2me-opts-scheduling-entry-r1
```

This capture preserves the module entry and locally declared plugin boundaries.
Existing base-plugin and worldgen-threading captures are reused separately.
Module generation hooks require their own disposition before whole-provider
closure; this initialization capture does not establish a new family.

Initializes scheduling configuration. Its plugin selects autosave and mid-tick task hooks using configuration values.
