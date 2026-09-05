# Better End Island spike and podium sources

Manifest SHA-256: `edd47178444d8218268335284bbe3ae1b394d4249c22b02ad85208caa2d63c52`.
Archive SHA-256: `8005f1ea798d09fc05dad07a21ed1f393a523a718197cdbd37b1ce6d9a17e4a4`.

SpikeFeatureMixin replaces getSpikesForLevel at HEAD with the custom result.
Its placeSpike HEAD hook calls BetterSpikeFeature.placeSpike with the supplied
arguments and an accessor-is-WorldGenRegion flag, then cancels vanilla execution.
Neither hook contains a configuration condition. This establishes direct code
behavior, not observed runtime transformation or successful generation.
The full spike and podium generators are preserved for subsequent interpretation.

Reproduce with extractor revision `8ceabcf` and a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar \
  --class-name com/yungnickyoung/minecraft/betterendisland/mixin/SpikeFeatureMixin.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/world/feature/BetterEndPodiumFeature.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/world/feature/BetterSpikeFeature.class \
  --output evidence/raw/item8/better-end-island-spike-podium-reproduction
```

Before adding this README, recursive comparison against fresh reproduction
matched every file byte-for-byte. The generated mixin-metadata.json is identical
to the authoritative copy in better-end-island-platform-gateway and is not
committed again. Scoped extractor Ruff/Basedpyright passed. No runtime or new
measurement system was added.
