# Remaining Extras scope entries

Extractor 04db73f. All seven selected classes reproduced byte for byte before
adding this README. Identity manifest SHA-256:
52f5fcab568040cb935607cc31924f50d8588881f4a273b9433e2f721f514578.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsExtras-1.21.1-NeoForge-5.1.1.jar \
  --class-name com/yungnickyoung/minecraft/yungsextras/module/PlacementModifierTypeModule.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/services/IPlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/services/NeoForgePlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/services/Services.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/config/DesertWellFeatureConfiguration.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/config/ResourceLocationFeatureConfiguration.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/placement/RngInitializerPlacement.class \
  --output evidence/raw/item8/yungs-extras-scope-entries-r1
```

The two feature configurations expose a supplied template resource location and,
for wells, a nonnegative radius. Their string constructors prefix yungsextras.
They do not enumerate additional templates. PlacementModifierTypeModule exposes
RngInitializerPlacement.CODEC. That modifier reseeds the supplied RandomSource
using two random longs and the input X/Z coordinates, then returns that same
position. It neither selects an additional template nor creates an independent
feature route.

Services resolves IModulesLoader and IPlatformHelper using ServiceLoader. The
archive's two descriptors select NeoForgeModulesLoader and NeoForgePlatformHelper.
The module loader/default were already captured. The platform helper reports
NeoForge, loaded-mod status and development status. No further content is added.
Shared YUNG API annotation scanning remains a separate provider responsibility.

Combined with existing initialization, generator, registration and processor
captures these account for all 29 archive classes. Full resource reconciliation
and contribution regressions remain required before provider closure.
