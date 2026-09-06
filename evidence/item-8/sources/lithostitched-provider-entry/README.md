# Lithostitched provider registration

Extractor 9dbb13dcf75a363499e9a916783bd04787bea63b. Manifest SHA-256:
86a0259a201e3198d49e62e81834e93e8aff50ea14ca7d93703a02c99cade3c8.
Independent r1 matches every generated file.

Retains the sole annotated NeoForge entry, central utilities and platform registry
dispatch. The entry loads configuration and initializes built-in registrations;
the platform dispatch attaches registry callbacks. Combine with existing modifier,
pool, processor and lifecycle captures. This source increment is not full provider
closure; remaining declared hooks and packaged component data require disposition.

```sh
uv run -m tools.inspect_item8_pool_elements --archive lithostitched-1.7.10+beta4-neoforge-21.1.jar --class-name dev/worldgen/lithostitched/Lithostitched.class --class-name dev/worldgen/lithostitched/LithostitchedNeoforge.class --class-name dev/worldgen/lithostitched/registry/LithostitchedRegistrations.class --output evidence/raw/item8/lithostitched-provider-entry-r1
```
