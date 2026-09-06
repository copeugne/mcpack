# aether-cumulus-platform

Extractor 4e20de58bb735db220e924d88edf9c22351f8209. Manifest SHA-256: 6d24efec98521b40e946c3fca20f1749c3668d0827efec0d1aee713fe782f707. Independent r1 matches every generated file. These are the concrete delegates left by the captured entry boundaries, using the existing extractor.

```sh
uv run -m tools.inspect_item8_pool_elements --archive aether-1.21.1-1.5.10-neoforge.jar --nested-archive META-INF/jarjar/cumulus_menus-1.21.1-2.0.7-neoforge.jar --class-name com/aetherteam/cumulus/platform/NeoForgePlatformHelper.class --output evidence/raw/item8/aether-cumulus-platform-r1
```

NeoForgePlatformHelper discovers CumulusEntrypoint-annotated MenuInitializer implementations through mod scan data, instantiates matching menu providers, and forwards supplied payloads through PacketDistributor. It contains no structure selection or placement implementation. Menu initialization belongs to the captured client entry path; the globally declared storage mixin is accounted for in aether-cumulus-entry.
