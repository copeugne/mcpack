# Aether placement, processors and chest source dependencies

Extractor revision c6cbcda. Six disassemblies and identities reproduce byte for
byte. Capture is isolated from inventory integration; no runtime claim.

```sh
uv run -m tools.inspect_item8_pool_elements --archive aether-1.21.1-1.5.10-neoforge.jar --class-name com/aetherteam/aether/block/dungeon/ChestMimicBlock.class --class-name com/aetherteam/aether/blockentity/ChestMimicBlockEntity.class --class-name com/aetherteam/aether/loot/AetherLoot.class --class-name com/aetherteam/aether/world/processor/BossRoomProcessor.class --class-name com/aetherteam/aether/world/processor/DoubleDropsProcessor.class --class-name com/aetherteam/aether/world/structurepiece/AetherTemplateStructurePiece.class --output evidence/raw/item8/aether-placement-r1
```

## Direct findings

BossRoomProcessor.processEntity obtains the rotated template bounding box,
constructs a Nitrogen BossRoomTracker with the processed entity position and
an AABB whose maximum coordinates are each bounding-box maximum plus one,
and inserts its serialized data under Dungeon in the processed entity NBT.
It then delegates to the parent processEntity method. The captured method
contains no new entity-type selection. This explains a source modification
of the authored boss entity; it does not prove boss encounter behavior.

DoubleDropsProcessor changes DOUBLE_DROPS to true when the processed block
state has that property, preserving position and NBT. Otherwise it delegates
to the parent processor. It does not directly assign a container loot table.

ChestMimicBlock.useWithoutItem calls spawnMimic on the server if the chest
position is not blocked. spawnAfterBreak also calls spawnMimic. That method
creates AetherEntityTypes.MIMIC, and if non-null positions it, calls
addFreshEntity, clears the block, plays a sound and invokes spawnAnim.
The addFreshEntity result is discarded. Thus the block is an interaction or
break-triggered authored encounter source, not a normal natural spawn or a
conventional mob-spawner block. Successful spawning remains unmeasured.
ChestMimicBlockEntity extends BlockEntity, not a randomizable container;
the inherited createChest behavior still matters for marker loot assignment.

AetherLoot registers keys in the aether namespace. BRONZE_DUNGEON resolves to
chests/dungeon/bronze/bronze_dungeon, and BRONZE_DUNGEON_REWARD resolves to
chests/dungeon/bronze/bronze_dungeon_reward. These identify the two marker
call-site loot sources; join selected packaged tables before final attribution.

AetherTemplateStructurePiece supplies the configured processor holder to
addProcessors during construction. Its pivot helper sets rotation around
(template-size-X >> 1, 0, template-size-Z >> 1). Ordinary javap does not expose
the addProcessors consumer bootstrap target, so the capture alone is not a
complete binding of that callback. Reuse existing engine sources and inspect
that exact bootstrap if needed, without recapturing unrelated classes.

## Continuation

Join these source findings to the Bronze decision alongside the selected
components bound by tests/item8/test_aether_bronze_components.py. Remaining
Bronze work includes full assembly/surface-ruins interpretation, inherited
chest placement, relevant sentry/trap block behavior, selected loot resources,
and required geometry/placement/visibility attribution. These are family
attributes and direct dependencies, not additional families. Do not expand
into encounter balancing or reward renewability analysis.

Scoped extractor Ruff and Basedpyright passed before capture.
