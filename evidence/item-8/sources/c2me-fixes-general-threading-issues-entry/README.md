# C2ME module initialization: c2me-fixes-general-threading-issues-entry

Extractor d7063da7914b7ba910021b92aae7b77cd250a497. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
59da04ec1ccd5946482039b42033f74ac28c11b7bdf5d75fcbadb7683a88dbd1

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-fixes-general-threading-issues-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/fixes/general/threading_issues/ModuleEntryPoint.class --output evidence/raw/item8/c2me-fixes-general-threading-issues-entry-r1
```

This capture preserves the module entry and locally declared plugin boundaries.
Existing base-plugin and worldgen-threading captures are reused separately.
Module generation hooks require their own disposition before whole-provider
closure; this initialization capture does not establish a new family.

The module entry is empty; its declared hooks remain the executable boundary to inspect.
