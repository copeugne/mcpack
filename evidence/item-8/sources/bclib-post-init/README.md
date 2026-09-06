# BCLib post-init

Extractor 565fa06d6f970e5eb45c15596f3299e4ee56ff5d. Independent r1 reproduction matches every
disassembly and identity manifest byte. Manifest SHA-256:
655110f279def6342e06afd6adbabd856a66474899d3e38ae20d18ee3e9266ad

```sh
uv run -m tools.inspect_item8_pool_elements --archive bclib-21.0.24.jar --class-name org/betterx/bclib/api/v2/PostInitAPI.class --output evidence/raw/item8/bclib-post-init-r1
```

PostInitAPI handles existing blocks/items: client rendering, shears dispenser
behavior, composting, block entity registration and consumer callbacks. The
callback list starts empty. This is shared initialization, not a family root.

Whole-provider closure still requires the nested library disposition and final
payload binding. Do not treat these captures alone as Item 8 completion.
