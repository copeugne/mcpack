# C2ME module initialization: c2me-client-uncapvd-entry

Extractor d7063da7914b7ba910021b92aae7b77cd250a497. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
cc7094266aa9a1baaec1a4080c6fa2ed04659f8e29783097faf7a9d5b32d4e6b

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-client-uncapvd-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/client/uncapvd/ModuleEntryPoint.class --class-name com/ishland/c2me/client/uncapvd/common/UncapVDInitializer.class --output evidence/raw/item8/c2me-client-uncapvd-entry-r1
```

This capture preserves the module entry and locally declared plugin boundaries.
Existing base-plugin and worldgen-threading captures are reused separately.
Module generation hooks require their own disposition before whole-provider
closure; this initialization capture does not establish a new family.

Reads view-distance enablement and configuration; registers ClientExtNetworking.registerListeners.
