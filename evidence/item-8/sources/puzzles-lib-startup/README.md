# Puzzles Lib startup membership boundary

Extractor ac5eb21d. Independent r1 reproduction matches all source and manifest
bytes. Manifest SHA-256:
76e803aeacdd3c17a5ddb4bdcc6e7aba430ba189902f46876d6b1647182ccf4e

```sh
uv run -m tools.inspect_item8_pool_elements --archive PuzzlesLib-v21.1.52-1.21.1-NeoForge.jar --class-name fuzs/puzzleslib/impl/core/proxy/ProxyImpl.class --class-name fuzs/puzzleslib/neoforge/impl/core/NeoForgeProxy.class --class-name fuzs/puzzleslib/neoforge/impl/event/NeoForgeEventInvokerRegistryImpl.class --output evidence/raw/item8/puzzles-lib-startup-r1
```

ProxyImpl registers a load-complete callback which initializes consumer mod
contexts and event invokers. NeoForge registration maps native events to consumer
callbacks. Both registration methods call only EventInvokerRegistry.register.
This is shared event wiring, not independent generated content. Combined with
the provider entry/payload capture it closes membership without tracing generic
consumer callbacks, networking, configuration or development tools. The large
event class is retained unchanged for reproducibility, not as a new audit scope.
