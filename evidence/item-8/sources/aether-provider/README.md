# Aether remaining candidate entry paths

Extractor 8976b7a captures 23 main-entry, mixin-plugin, custom-feature, holiday
decoration and Silver/Gold assembly classes. Existing Bronze and shared-piece
sources are reused. Independent r1 extraction matches every generated file.
Manifest SHA-256: 917c3ffbb199539bfbe375f4a7381d4498f327a2ce9d5cdc28ad01d978f604ee.

```sh
uv run -m tools.inspect_item8_pool_elements --archive aether-1.21.1-1.5.10-neoforge.jar --class-name com/aetherteam/aether/Aether.class --class-name com/aetherteam/aether/mixin/AetherMixinPlugin.class --class-name com/aetherteam/aether/world/feature/AetherFeatures.class --class-name com/aetherteam/aether/world/feature/AercloudFeature.class --class-name com/aetherteam/aether/world/feature/AetherLakeFeature.class --class-name com/aetherteam/aether/world/feature/CrystalIslandFeature.class --class-name com/aetherteam/aether/world/feature/ShelfFeature.class --class-name com/aetherteam/aether/world/treedecorator/HolidayTreeDecorator.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldBossRoom.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldDungeonPiece.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldIsland.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldProcessorSettings.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldStub.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldStubCave.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldTunnel.class --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverBossRoom.class --class-name 'com/aetherteam/aether/world/structurepiece/silverdungeon/SilverDungeonBuilder$1.class' --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverDungeonBuilder.class --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverDungeonPiece.class --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverDungeonRoom.class --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverFloorPiece.class --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverProcessorSettings.class --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverTemplePiece.class --output evidence/raw/item8/aether-provider-r1
```

These sources support candidate/component reconciliation. Capture alone does
not establish provider closure, final family counts or runtime placement.
