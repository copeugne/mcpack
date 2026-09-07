# C2ME module initialization: c2me-notickvd-entry

Extractor d7063da7914b7ba910021b92aae7b77cd250a497. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
b1ded4e25460de314c80eaea2b1ce7d19949121fe1237d2bacf880b4ef2b7825

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-notickvd-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/notickvd/ModuleEntryPoint.class --class-name com/ishland/c2me/notickvd/common/NoTickVDInitializer.class --output evidence/raw/item8/c2me-notickvd-entry-r1
```

This capture preserves the module entry and locally declared plugin boundaries.
Existing base-plugin and worldgen-threading captures are reused separately.
Module generation hooks require their own disposition before whole-provider
closure; this initialization capture does not establish a new family.

Reads no-tick view-distance configuration; registers ServerExtNetworking.registerListeners.
