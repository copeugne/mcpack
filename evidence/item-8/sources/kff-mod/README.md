# Kotlin for Forge mod entries

Extractor 2d22e7dc5ae86322203a01f3b95667d2f926b13a. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
66a33c92310269a68c6939921fa997abd7b5b366dc3730b278a44e0139c786d2

```sh
uv run -m tools.inspect_item8_pool_elements --archive kotlinforforge-5.11.0-all.jar --nested-archive META-INF/jarjar/thedarkcolour.kffmod-5.11.0.jar --class-name thedarkcolour/kotlinforforge/neoforge/test/KotlinForForge.class --class-name thedarkcolour/kotlinforforge/test/KotlinForForge.class --output evidence/item-8/sources/kff-mod
```

Provider membership evidence for both packaged loader-specific mod entries.
