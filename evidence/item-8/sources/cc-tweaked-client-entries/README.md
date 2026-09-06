# CC:Tweaked client entry declarations

Extractor 7200a89a95adaef4d11f56c741ef9d62af6761e2. Independent r1 reproduction matches
both disassemblies and the identity manifest. Manifest SHA-256:
c0ed967d981853b4d4d2254cfec2babaab165dd5fc263ab385ab2c8612eb0ad4

```sh
uv run -m tools.inspect_item8_pool_elements --archive cc-tweaked-1.21.1-forge-1.119.0.jar --class-name dan200/computercraft/client/ForgeClientHooks.class --class-name dan200/computercraft/client/ForgeClientRegistry.class --output evidence/raw/item8/cc-tweaked-client-entries-r1
```

Both automatic event subscribers explicitly declare Dist.CLIENT. They cannot
be dedicated-server generation entrypoints. The client-only mixin declaration
and client service providers remain rendering, UI and client-network inputs;
no client renderer audit is needed for server-family membership.
