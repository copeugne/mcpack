# aether-reload-consumers

Extractor 4e20de58bb735db220e924d88edf9c22351f8209. Manifest SHA-256: 5e8b0cfc4241fadf9419c14dc71c1c204ee0b3ccd8a566034497ce9f067e38a1. Independent r1 matches every generated file. These are the concrete delegates left by the captured entry boundaries, using the existing extractor.

```sh
uv run -m tools.inspect_item8_pool_elements --archive aether-1.21.1-1.5.10-neoforge.jar --class-name 'com/aetherteam/aether/data/ReloadListeners$RecipeReloadListener.class' --class-name 'com/aetherteam/aether/data/ReloadListeners$BannerReloadListener.class' --output evidence/raw/item8/aether-reload-consumers-r1
```

RecipeReloadListener clears FreezingBlock.cachedBlocks and cachedResults. BannerReloadListener resets AetherItems.SWET_BANNER to null. These reload handlers invalidate caches; neither selects or places a structure. This closes the two reload-handler contribution questions.
