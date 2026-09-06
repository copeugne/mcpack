# Better Mineshafts remaining provider entries

Extractor 8746a17 captures eleven remaining initialization, service, piece
registration and mixin classes. Together with mineshafts-code, the preserved
sources cover all 51 classes. An independent r1 extraction matches every generated
file. No existing generator capture was repeated.

Manifest SHA-256: 5fe961b0858c511f20ec7d8e5a858ded64899576f6685e721c4e3113d914a707.

```sh
uv run -m tools.inspect_item8_pool_elements --archive YungsBetterMineshafts-1.21.1-NeoForge-5.1.1.jar --class-name com/yungnickyoung/minecraft/bettermineshafts/BetterMineshaftsCommon.class --class-name com/yungnickyoung/minecraft/bettermineshafts/BetterMineshaftsNeoForge.class --class-name com/yungnickyoung/minecraft/bettermineshafts/mixin/BlockBehaviourAccessor.class --class-name com/yungnickyoung/minecraft/bettermineshafts/mixin/BoundingBoxAccessor.class --class-name com/yungnickyoung/minecraft/bettermineshafts/mixin/SuppressLogMixin.class --class-name com/yungnickyoung/minecraft/bettermineshafts/module/StructurePieceTypeModule.class --class-name com/yungnickyoung/minecraft/bettermineshafts/services/IModulesLoader.class --class-name com/yungnickyoung/minecraft/bettermineshafts/services/IPlatformHelper.class --class-name com/yungnickyoung/minecraft/bettermineshafts/services/NeoForgeModulesLoader.class --class-name com/yungnickyoung/minecraft/bettermineshafts/services/NeoForgePlatformHelper.class --class-name com/yungnickyoung/minecraft/bettermineshafts/services/Services.class --output evidence/raw/item8/mineshafts-provider-r1
```

Common initialization scans the module package through YUNG API and loads the
module service. NeoForge initialization binds the existing configuration module.
The module-loader implementation delegates to an empty default. The platform
service reports NeoForge, mod presence and development mode. Services selects the
packaged implementations or throws when none is available.

The piece registry exposes eleven component types for the existing specialized
mineshaft generator. These include tunnels, entrances, rooms, ore deposits and
intersections, not additional structure families. Two accessor mixins expose
block survival checks and bounding-box coordinates.

SuppressLogMixin cancels the diagnostic callback only when its message starts
with Detected setBlock in a far chunk and contains bettermineshafts:mineshaft.
It does not cancel the underlying block write. Preserve this diagnostic limitation:
absence of that warning cannot prove absence of far-chunk writes. The existing
vanilla suppression and locate hooks remain in mineshafts-code.

This source capture requires provider payload/root reconciliation before closure;
it does not prove runtime behavior or complete all family attributes.
