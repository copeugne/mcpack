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

## Packaged mixin declaration

The extractor also produced `mixin-metadata.json`, initially omitted from staging
because its parent directory ends in .jar. It is now retained alongside these
classes. Its SHA-256 is
`9edd653c4d2fb45318c02ff41838941b914774d87f8d799d20aa99aa8fa91813`.
The preserved NeoForge metadata declares betterendisland.mixins.json; that file
lists EndPlatformFeatureMixin and EndGatewayFeatureMixin among its common mixins,
with required=true and defaultRequire=1. There is no plugin entry in that mixin
configuration. This is the packaged application declaration, not direct proof of
runtime transformation or successful generated-world placement.

The existing fresh reproduction contains an identical metadata file. No new
capture or runtime was needed. Metadata copies produced by later processor and
configuration captures are identical duplicate outputs, not separate evidence.
