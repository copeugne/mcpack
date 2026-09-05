# Better End Island platform and gateway sources

Retained archive SHA-256: `8005f1ea798d09fc05dad07a21ed1f393a523a718197cdbd37b1ce6d9a17e4a4`.
Manifest SHA-256: `6d6944ae221e62182308d1ac3cdcc10a9b028d98bb0e2fa0d72e910cd366b48a`.

The platform mixin injects at createEndPlatform HEAD. When
useVanillaSpawnPlatform is false it calls BetterEndSpawnPlatformFeature.place,
discards its boolean and cancels vanilla execution. The gateway mixin injects
at place HEAD; when useVanillaEndGateways is false it supplies the custom
BetterEndGatewayFeature.place boolean as the return value. True leaves the
vanilla path alone in both hooks. These are code paths, not verified effective
configuration or observed successful world generation. Configuration-field
binding, mixin activation, template/content attribution and provider completion
remain open. The two full custom generator classes are preserved for that work.

Reproduce using extractor revision `599debf` and a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar \
  --class-name com/yungnickyoung/minecraft/betterendisland/mixin/EndGatewayFeatureMixin.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/mixin/EndPlatformFeatureMixin.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/world/feature/BetterEndGatewayFeature.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/world/feature/BetterEndSpawnPlatformFeature.class \
  --output evidence/raw/item8/better-end-island-platform-gateway-reproduction
```

Before adding this README, recursive comparison with the fresh reproduction
matched all files byte-for-byte. Scoped extractor Ruff/Basedpyright passed.
The two mixin captures retain verbose annotations. No new measurement system
or runtime was added.
