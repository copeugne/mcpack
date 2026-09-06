# Better Witch Huts provider consumers

Extractor bacb544 captures seventeen classes not present in the prior
witch-hut-suppression capture. Together they preserve all twenty packaged classes.
An independent r1 capture reproduced all generated files byte for byte before
this README. Archive SHA-256:
888b1e6d1ada21982a75abfb4afb040c9bc2cc68777ec5fcd1199b978e3d4f8d.
Manifest SHA-256:
a5945737834c9c643fa966de790d0e63f40c1d4df9b301b4856ffb66e1c9e098.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBetterWitchHuts-1.21.1-NeoForge-4.1.1.jar \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/BetterWitchHutsCommon.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/BetterWitchHutsNeoForge.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/config/BWHConfigNeoForge.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/mixin/LocateVanillaWitchHutCommandMixin.class \
  --class-name 'com/yungnickyoung/minecraft/betterwitchhuts/module/ConfigModule$General.class' \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/module/ConfigModule.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/module/StructureProcessorTypeModule.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/services/IModulesLoader.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/services/IPlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/services/NeoForgeModulesLoader.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/services/NeoForgePlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/services/Services.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/world/processor/BrewingStandProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/world/processor/FenceLegProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/world/processor/LegProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/world/processor/PottedMushroomProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterwitchhuts/world/processor/WitchCircleProcessor.class \
  --output evidence/raw/item8/witch-hut-provider-r1
```

The NeoForge constructor invokes common initialization and the already captured
configuration loader. Common initialization asks YungAutoRegister to scan the
module package and invokes the modules service. The packaged service providers
are NeoForgeModulesLoader and NeoForgePlatformHelper. The former delegates to an
empty interface default; the latter supplies loader/platform lookups. Services
uses ServiceLoader.findFirst and throws if no implementation exists. The module
registration class declares exactly the five processors in the packaged main
processor list. Shared YUNG API registration remains a separate provider input.

These processors modify existing template components:

- LegProcessor replaces brown stained glass markers with oak-log supports and
  extends them downward through air/fluid within build-height bounds.
- FenceLegProcessor replaces crimson-fence markers with oak fence supports and
  extends them downward, preserving fence properties.
- WitchCircleProcessor varies the supplied circle masonry/stairs and extends
  gray stained-glass support markers downward with its brick randomizer.
- BrewingStandProcessor populates brewing-stand item NBT with one of five
  ingredient/potion combinations. The capture preserves the exact serialization;
  this is not proof that all resulting item contents survive runtime loading.
- PottedMushroomProcessor varies a potted red mushroom among its seven declared
  potted plant states.

The direct-write support branches check the WorldGenRegion center chunk.
Their extent can exceed the original template bounds and must remain visible
in later vertical-size attribution. They do not independently register or place
another structure family. LocateVanillaWitchHutCommandMixin modifies the direct
vanilla locate request; reuse the prior suppression and frozen setting evidence.

Provider closure additionally requires the packaged root/pool/template partition.
This source capture alone does not establish final family attributes or Item 8
completion. No frozen runtime input is changed.
