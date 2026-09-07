# owo-lib startup and content callbacks

Extractor 1d1e0da8f492b78a9b88f0ba964a24c26676d8c2. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
4a3c3c2463c3903b37c3d5c3a17b1b48651924523a5f8a62050897b0ae36f7dd

```sh
uv run -m tools.inspect_item8_pool_elements --archive owo-lib-neoforge-0.12.15.5-beta.1+1.21.jar --class-name io/wispforest/owo/ops/LootOps.class --class-name io/wispforest/owo/util/TagInjector.class --class-name io/wispforest/owo/util/Maldenhagen.class --class-name io/wispforest/owo/command/debug/OwoDebugCommands.class --class-name io/wispforest/owo/network/neoforge/NeoOwoNetworking.class --class-name io/wispforest/owo/util/Wisdom.class --output evidence/item-8/sources/owo-delegates
```

Startup, loot/tag consumer callbacks and ore placement boundary evidence.
