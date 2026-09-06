# C2ME module initialization: c2me-opts-allocs-entry

Extractor d7063da7914b7ba910021b92aae7b77cd250a497. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
0fd8478f10ff57f721588b80f195afde870087dddbf84975f4c6105c4de970da

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-opts-allocs-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/opts/allocs/MixinPlugin.class --class-name com/ishland/c2me/opts/allocs/ModuleEntryPoint.class --output evidence/raw/item8/c2me-opts-allocs-entry-r1
```

This capture preserves the module entry and locally declared plugin boundaries.
Existing base-plugin and worldgen-threading captures are reused separately.
Module generation hooks require their own disposition before whole-provider
closure; this initialization capture does not establish a new family.

Module entry is empty. Plugin delegates to the captured base plugin, including its empty preApply.
