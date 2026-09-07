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

## Two-family attribute assessment

Scope: two active families, twenty explicit attributes. Reused the six distinct
reachable templates, existing packaged definitions and all five preserved
processors. No new extraction, runtime, measurement or tooling was needed.
Direct references below use YungsBetterWitchHuts-1.21.1-NeoForge-4.1.1.jar
members in the existing packaged/template catalogs. Identities are bound in
family-decisions.json; biome constraints remain derived by the inventory builder.

The effective circle tag resolves minecraft:swamp; the hut tag resolves swamp
and mangrove_swamp. Neither has missing required or unresolved biome tags.
Only the captured Overworld intersects these sets. Structure definitions use
surface_structures and WORLD_SURFACE_WG with circle offset0 and hut offset1.
The circle is a low masonry/campfire site; huts have wood roofs and terrain
supports. These are source-based discoverability descriptions, not visibility
measurements. There are no retained world-bounds observations for these roots.

Under data/betterwitchhuts/structure/, witch_circle.nbt is9x5x9. Hut alternatives
witch_hut_sm/lg/double are7x8x9,11x7x11,15x9x13. Each main template is rigid and
has exactly one witch and one cat connector into mobs. The pool selects by the
matching target name; its equal weights do not interchange witch and cat.
The components are witch1x3x1 and cat1x2x1 with downward incoming connector at
local0,0,0. Main upward connectors lie inside the architecture:

- Circle: cat[4,1,2],witch[4,1,6].
- Small hut: cat[4,3,4],witch[3,3,5].
- Large hut: cat[3,2,7],witch[7,2,7].
- Double hut: cat[3,2,9],witch[10,4,3].

Connecting above these positions leaves all component bounds within the main
size. Nominal footprint and height are therefore the corresponding template
sizes, with X/Z exchanged by rotation. LegProcessor, FenceLegProcessor and
WitchCircleProcessor add downward terrain-dependent supports at the same X/Z.
Their air/fluid loops stop at nonfluid solid terrain or build bounds. Nominal
height explicitly excludes that variable extension; no fixed total occupied
height or typical terrain depth is claimed. This source description satisfies
the approximate-size requirement without a new sampling experiment.

Both structures override monster spawning with piece-bounded witch weight1,
min/max1, and creature spawning with cat weight1,min/max1. Independently, the
witch template saves a Health26 persistent witch; cat saves a Health10 persistent
all-black cat. These are authored and natural sources, not observed populations.
None of the six templates has ordinary/trial spawner blocks. The five main
processors add no entity spawners; their effects are described above.

The circle has no container loot-table references and an empty campfire Items
list. The hut's packaged table is betterwitchhuts:chests/hut_0: double template
block_entities indexes1,5,6; large indexes2,5; small has none. Each hut has one
brewing stand, at double index9,large6,small4. BrewingStandProcessor.populateItemsList
chooses among glistering_melon_slice/healing,sugar/swiftness,pufferfish/water_breathing,
golden_carrot/night_vision,phantom_membrane/slow_falling. This is a direct item
source separate from table loot. Source serialization is retained without claiming
runtime survival, effective quantities or loot-economy validation. Circle contains
no brewing stand, so that processor does not create this reward there.

All twenty attributes are integrated into family decisions and rebuilt inventory.
Reproduction: `uv run -m tools.build_item8_inventory --output evidence/raw/item8/witch-hut-assessed-inventory.json`
with an absent output path. The semantic comparison changes only these two
families and the input identity. Existing focused validation:
`uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py`.

All85 focused tests passed. Total355/449 families assessed,94 remaining.
This completes these two assessments, not the final Item8 gate.
