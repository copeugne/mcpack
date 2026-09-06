# Kotlin for Forge language boundary

Extractor 2d22e7dc5ae86322203a01f3b95667d2f926b13a. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
7aa167a9ab8cb42d77871c7149d8455c2cf9837aeb7c85c1a787d8cf888a0c5e

```sh
uv run -m tools.inspect_item8_pool_elements --archive kotlinforforge-5.11.0-all.jar --nested-archive META-INF/jarjar/thedarkcolour.kfflang-5.11.0.jar --class-name thedarkcolour/kotlinforforge/neoforge/KotlinLanguageLoader.class --class-name thedarkcolour/kotlinforforge/neoforge/KotlinModContainer.class --class-name thedarkcolour/kotlinforforge/neoforge/AutoKotlinEventBusSubscriber.class --class-name thedarkcolour/kotlinforforge/KotlinLanguageProvider.class --output evidence/item-8/sources/kff-language
```

Provider membership evidence for language loading and consumer event discovery.
