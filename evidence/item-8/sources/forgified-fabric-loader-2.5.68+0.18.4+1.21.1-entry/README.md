# forgified-fabric-loader-2.5.68+0.18.4+1.21.1-entry source checkpoint

Extractor a6fa580. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: f36fb741b2e5a6cb1061b83f9a2e049c68ecee80b44ec3404e0e49a5e153c25d.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/forgified-fabric-loader-2.5.68+0.18.4+1.21.1-full.jar --class-name net/fabricmc/loader/impl/bootstrap/FabricLoaderHackyInjector.class --output evidence/raw/item8/forgified-fabric-loader-2.5.68+0.18.4+1.21.1-entry-r1
```

The declared language-loader service installs FabricLoaderBootstrap into the launch-plugin map. That bootstrap remains open. No ordinary mod annotation or mixin declaration exists in this archive.

Source capture alone does not close whole-provider membership.
