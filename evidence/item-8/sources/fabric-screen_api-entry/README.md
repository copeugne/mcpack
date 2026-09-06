# Fabric screen_api entry roles

Captured with e2ae798. Independent repeat matched all source files exactly.
Manifest SHA-256: 26c940bebeaf35260b92164b7b8c736bf981a4b8bf4de0daffc709f3aa83813d.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-screen-api-v1-2.0.25+0ae1214819.jar --class-name org/sinytra/fabric/screen_api/ScreenEventHooks.class --class-name org/sinytra/fabric/screen_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-screen_api-entry-r1
```

The generated loader is empty. ScreenEventHooks forwards client screen render, keyboard and mouse events to Fabric client event callbacks and supports input cancellation. It has no world-generation entry.

Full payload and declared-hook coverage are verified separately by the existing
Fabric provider check. No further client-helper tracing is required for these
entry contribution roles. This capture alone is not whole-provider closure.
