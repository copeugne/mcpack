# CC:Tweaked registries and computer lifecycle

Extractor aeacdd6fcab12c72340007bcf74252bea2bd83d7. Independent r1 reproduction matches
all 15 disassemblies and the identity manifest. Manifest SHA-256:
3ea31124fc41a1706c6e2c8c656446b18c4047ffff2677d25b1133ed9313b815

```sh
uv run -m tools.inspect_item8_pool_elements --archive cc-tweaked-1.21.1-forge-1.119.0.jar --class-name 'dan200/computercraft/shared/ModRegistry$Blocks.class' --class-name 'dan200/computercraft/shared/ModRegistry$BlockEntities.class' --class-name 'dan200/computercraft/shared/ModRegistry$DataComponents.class' --class-name 'dan200/computercraft/shared/ModRegistry$Items.class' --class-name 'dan200/computercraft/shared/ModRegistry$TurtleUpgradeTypes.class' --class-name 'dan200/computercraft/shared/ModRegistry$PocketUpgradeTypes.class' --class-name 'dan200/computercraft/shared/ModRegistry$Menus.class' --class-name 'dan200/computercraft/shared/ModRegistry$ArgumentTypes.class' --class-name 'dan200/computercraft/shared/ModRegistry$LootItemConditionTypes.class' --class-name 'dan200/computercraft/shared/ModRegistry$RecipeSerializers.class' --class-name 'dan200/computercraft/shared/ModRegistry$RecipeFunctions.class' --class-name 'dan200/computercraft/shared/ModRegistry$Permissions.class' --class-name 'dan200/computercraft/shared/ModRegistry$CreativeTabs.class' --class-name dan200/computercraft/shared/computer/core/ServerContext.class --class-name dan200/computercraft/shared/util/TickScheduler.class --output evidence/raw/item8/cc-tweaked-registry-lifecycle-r1
```

The registry holders bind the declared content to block, block-entity, item,
data-component, command-argument, menu, creative-tab, loot-condition, recipe
and computer-upgrade registries. They do not register structure/feature types.
ServerContext constructs the computer execution context and computer registry;
its tick updates that registry and its main-thread scheduler. TickScheduler
queues tokens belonging to existing block entities and schedules their ticks.
These are player-computer and existing-block lifecycle paths, not an authored
generation family. No further generic Lua, scheduler, filesystem or turtle
implementation audit is needed for this membership boundary.
