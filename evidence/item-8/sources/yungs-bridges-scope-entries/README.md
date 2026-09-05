# Remaining YUNG Bridges entry paths

Extractor dfca574. Seven previously uncaptured classes reproduced byte for byte
before adding this README. Identity manifest SHA-256:
195e399064827ba1881a062e2f823d4242ede6a3bc736f8f1d94d013c21734b2.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBridges-1.21.1-NeoForge-5.1.1.jar \
  --class-name com/yungnickyoung/minecraft/yungsbridges/mixin/SuppressLogMixin.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/module/FeatureModule.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/module/PlacementModifierTypeModule.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/services/IPlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/services/NeoForgePlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/services/Services.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/feature/config/MultipleAttemptSingleRandomFeatureConfig.class \
  --output evidence/raw/item8/yungs-bridges-scope-entries-r1
```

FeatureModule constructs the already captured bridge and multiple-attempt selector.
PlacementModifierTypeModule exposes the already captured bridge and RNG placement
codecs. MultipleAttemptSingleRandomFeatureConfig stores and exposes a supplied
placed-feature list; it adds no independently authored content.

Services loads IPlatformHelper and IModulesLoader through ServiceLoader. The
archive declares NeoForgePlatformHelper and NeoForgeModulesLoader respectively.
The platform helper only reports platform name, loaded-mod status and development
status. The module loader and its empty default were already captured. Shared
YUNG API annotation scanning remains attributable to that library.

SuppressLogMixin injects into Util.logAndPauseIfInIde with require=0. It cancels
when the message starts with "Detected setBlock in a far chunk" and contains
"yungsbridges:bridge_list". This does not add a family, but absence of this warning
cannot prove absence of far-chunk placement. Do not silently reinterpret clean
logs as that proof. No new runtime experiment or baseline modification.

These classes complete the provider's class capture set when combined with
existing generation, processor and module-loader captures. Full payload and
existing contribution checks still determine provider coverage closure.
