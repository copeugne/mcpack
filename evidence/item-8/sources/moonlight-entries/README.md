# Moonlight entry boundaries

Extractor f1d6b260527afacd421743f0366d33b5fd64657b. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
8e3ae9145da3c936b9cb3c38f238ee73b9c215419e6ff52cfd0e213d5ffd9751

```sh
uv run -m tools.inspect_item8_pool_elements --archive moonlight-neoforge-1.21.1-3.0.17.jar --class-name net/mehvahdjukaar/moonlight/api/client/platform/ForgeFluidTypeHelper.class --class-name net/mehvahdjukaar/moonlight/platform/MoonlightForge.class --class-name net/mehvahdjukaar/moonlight/core/mixins/MixinPlugin.class --output evidence/item-8/sources/moonlight-entries
```

Entry and plugin evidence only; whole-provider disposition remains open.
