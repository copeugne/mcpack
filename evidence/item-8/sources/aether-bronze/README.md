# Aether Bronze dungeon assembly and pieces

Captured using extractor revision 1b05806. The nine disassemblies and identities
reproduced byte for byte. This is direct source evidence, not a completed family
attribution or a world-placement measurement.

```sh
uv run -m tools.inspect_item8_pool_elements --archive aether-1.21.1-1.5.10-neoforge.jar --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeBossRoom.class --class-name 'com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonBuilder$Connection.class' --class-name 'com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonBuilder$RoomProvider.class' --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonBuilder.class --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonPiece.class --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonRoom.class --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonSurfaceRuins.class --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeProcessorSettings.class --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeTunnel.class --output evidence/raw/item8/aether-bronze-r1
```

BronzeDungeonRoom.handleDataMarker clears the marker position. For `Chest`,
nextInt(5) greater than 1 selects an ordinary chest; the other two outcomes
select CHEST_MIMIC. It calls createChest with AetherLoot.BRONZE_DUNGEON and
discards the success result. This is a source selection rule, not observed
chest or mimic counts. The inherited chest writer and mimic block behavior
still need attribution before claiming effective encounter generation.

BronzeBossRoom enables entity finalization in its placement settings. For
`Treasure Chest`, it assigns AetherLoot.BRONZE_DUNGEON_REWARD to a randomizable
container below the marker when present, sets dungeon type aether:bronze via
the treasure-chest helper, then clears the marker. That method itself does not
establish the boss entity identity. Join the selected template entities and
shared AetherTemplateStructurePiece behavior.

The builder references boss_room, chest_room, end_corridor, entrance, lobby
and square_tunnel. Its room-provider registrations and assembly conditions
remain to be read completely and joined to the packaged template catalog.
BronzeDungeonSurfaceRuins is a component of this builder, not a separate
family inferred from its class name. Processor settings distinguish generic
rooms, tunnels and boss rooms. Resolve the selected definitions before
attributing effective processor behavior from static helper fields.

Next: finish the builder and surface-ruins reading, join the six named template
candidates and selected processor lists, then resolve the shared piece writer,
loot constants and direct encounter-producing blocks where required. Reuse
these captures. No new measurement system or runtime acceptance claim.

Scoped extractor Ruff and Basedpyright passed before capture.
