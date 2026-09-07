# CristelLib pack contribution sources

Extractor de505599. Ten classes bind entries, consumer API discovery, pack
registration and runtime pack storage. Independent r1 reproduction matches
all source and manifest bytes. Manifest SHA-256:
e6ef7ec929f496a08887bd704480e3523c9bb7f4fdf2c6352b712c4281fafd9e

```sh
uv run -m tools.inspect_item8_pool_elements --archive cristellib-neoforge-1.21.1-3.1.7.jar --class-name de/cristelknight/cristellib/CristelLib.class --class-name de/cristelknight/cristellib/CristelLibRegistry.class --class-name de/cristelknight/cristellib/autoconfig/ModFinder.class --class-name de/cristelknight/cristellib/builtinpacks/BuiltInPackLoader.class --class-name de/cristelknight/cristellib/builtinpacks/RuntimePack.class --class-name de/cristelknight/cristellib/neoforge/CristelLibNeoForge.class --class-name de/cristelknight/cristellib/neoforge/PlatformHelperImpl.class --class-name de/cristelknight/cristellib/neoforge/client/CristelLibNeoForgeClient.class --class-name de/cristelknight/cristellib/neoforge/extraapiutil/APIFinder.class --class-name de/cristelknight/cristellib/neoforge/mixin/PathPackResourcesAccessor.class --output evidence/raw/item8/cristellib-provider-r1
```

Initialization reads consumer APIs/configurations and adds their structure sets
to a runtime pack. Pack repository injection requires the supplied condition
and exclusion from disabledPacks. Platform loading resolves paths inside the
consumer archive; the accessor exposes a pack root for overlays. RuntimePack
is storage for supplied resources, not an authored design. Auto-configuration
wraps existing structure sets. The actual structure-set writer and data-reader
delegates remain to bind before provider closure.
