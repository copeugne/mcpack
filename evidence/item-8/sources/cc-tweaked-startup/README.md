# CC:Tweaked startup and common events

Extractor 962f13cd9a05aa7bbab4467aa1b143dcc894de90. Independent r1 reproduction matches
all five disassemblies and the identity manifest. Manifest SHA-256:
86915681e8cb6ccb41a0cecf9c444fc9c15a8f1a20c23df146a0429acfb2fb26

```sh
uv run -m tools.inspect_item8_pool_elements --archive cc-tweaked-1.21.1-forge-1.119.0.jar --class-name dan200/computercraft/shared/CommonHooks.class --class-name dan200/computercraft/shared/ModRegistry.class --class-name dan200/computercraft/impl/AbstractComputerCraftAPI.class --class-name dan200/computercraft/shared/integration/CreateIntegration.class --class-name dan200/computercraft/shared/integration/MoreRedIntegration.class --output evidence/raw/item8/cc-tweaked-startup-r1
```

ModRegistry registers computer blocks/items/block entities, upgrade types, data
components, menus, commands, recipe/loot types and peripheral APIs. Main-thread
setup adds turtle cauldron interactions. Create integration supplies block
movement checks; More Red integration supplies bundled-redstone capability.
AbstractComputerCraftAPI exposes computer filesystem/network/upgrade APIs.
CommonHooks manages server computers, scheduled block ticks, monitors, drops,
player lectern interaction and existing loot. The direct registration and
computer-lifecycle boundaries remain to bind before whole-provider closure.

getExtraLootPool adds computercraft:treasure_disk to ten existing vanilla table
keys: SIMPLE_DUNGEON, ABANDONED_MINESHAFT, STRONGHOLD_CORRIDOR,
STRONGHOLD_CROSSING, STRONGHOLD_LIBRARY, DESERT_PYRAMID, JUNGLE_TEMPLE,
IGLOO_CHEST, WOODLAND_MANSION and VILLAGE_CARTOGRAPHER. Retain this as an
existing-family loot modifier, not an independent family. This does not prove
a disk appeared in any particular generated chest.
