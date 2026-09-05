# Better End Island generator dependencies

Manifest SHA-256: `8c3ce129b5cdde84f33f705a24735cff5c219462b9b0a5db494b927c21d3ca3e`.
Archive SHA-256: `8005f1ea798d09fc05dad07a21ed1f393a523a718197cdbd37b1ce6d9a17e4a4`.

Seven selected classes resolve direct inventory dependencies. Verbose generator
captures expose string-concatenation bootstrap constants omitted by the earlier
nonverbose capture; that original capture remains preserved. Additional classes
cover spike indices, crystal offsets, block replacement, podium invocation and
the Better End detection flag. This is source evidence, not runtime observation.

Reproduce with extractor revision `a9d9add` and a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar \
  --class-name com/yungnickyoung/minecraft/betterendisland/BetterEndIslandCommon.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/mixin/EndDragonFightMixin.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/mixin/EndSpikeMixin.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/world/SpikeCacheLoader.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/world/feature/BetterEndPodiumFeature.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/world/feature/BetterSpikeFeature.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/world/processor/BlockReplaceProcessor.class \
  --output evidence/raw/item8/better-end-island-generator-dependencies-reproduction
```

Before this README was added, recursive comparison with the fresh reproduction
matched every file. Generated mixin metadata matches the authoritative copy in
better-end-island-platform-gateway and is not committed again. Scoped extractor
Ruff and Basedpyright passed. No new measurement system was added.
