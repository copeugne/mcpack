# Moonlight dynamic registration boundaries

Extractor ee53fecc32fecca0526f8fb740893f50c96e3525. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
b409463d0d9db29ee765d36879c987e68f26d744b066a0f8f58976bd0d9e05b9

```sh
uv run -m tools.inspect_item8_pool_elements --archive moonlight-neoforge-1.21.1-3.0.17.jar --class-name net/mehvahdjukaar/moonlight/core/pack/DynamicResourcesInternals.class --class-name net/mehvahdjukaar/moonlight/api/platform/platform/RegHelperImpl.class --class-name net/mehvahdjukaar/moonlight/core/commands/ModCommands.class --class-name net/mehvahdjukaar/moonlight/core/misc/platform/ModLootModifiers.class --output evidence/item-8/sources/moonlight-dynamic-registration
```

Dynamic pack registration, init queue, commands and loot type boundaries.
