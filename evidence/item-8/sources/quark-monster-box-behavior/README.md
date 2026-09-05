# Monster Box encounter behavior

Captured at `7e7f16c`; exact identities are in identities.json. Reproduction
matched both captures and identities byte for byte:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name org/violetmoon/quark/content/world/block/MonsterBoxBlock.class --class-name org/violetmoon/quark/content/world/block/be/MonsterBoxBlockEntity.class --output evidence/raw/item8/quark-monster-box-7e7f16c
```

Adding these selections exceeded the type checker's tuple inference capacity.
The first scoped check failed with Unknown tuple element types. An explicit
tuple[str, ...] annotation fixed the error without changing runtime behavior;
Ruff and Basedpyright then passed before capture.

## Direct block-entity interpretation

tick returns immediately in Peaceful difficulty. Otherwise, a non-spectator
player strictly within activationRange of the block center starts breakProgress.
There is no line-of-sight or creative-player exclusion in this method. Once
progress is positive it continues without requiring a nearby player. The first
increment plays a growl. When progress exceeds 40, tick calls spawnMobs, emits
the block-break event and requests removal of the block. The client branch also
emits flame or smoke particles. Actual spawning inside spawnMobs requires a
ServerLevel. This describes a one-use source, not a renewable vanilla spawner.

spawnMobs obtains MonsterBoxModule.MONSTER_BOX_SPAWNS_LOOT_TABLE from the
server's reloadable loot registry. It builds BLOCK context with block-center
origin, block state, empty tool and this block entity. It chooses
minMobCount + nextInt(max(maxMobCount-minMobCount+1,1)) table draws. For each
draw it calls getRandomItemsRaw with the captured consumer. The count therefore
does not independently establish successful spawned mobs.

The consumer ignores non-spawn-egg items. For spawn eggs it obtains their entity
type and calls EntityType.spawn with MobSpawnType.SPAWNER, the egg stack, null
player and both boolean arguments true. A non-null returned entity is moved to
the box center, receives random velocity components in [-0.2,0.2), and gets
persistent boolean quark:monster_box_spawned=true. Spawn failure is not retried
in this consumer. The caller emits ENTITY_PLACE after the draw loop.

The loot table is an authored mob-selection input, not evidence of a player
container reward. Resolve its selected packaged definition and module event
handlers before finalizing mob IDs or later spawned-mob behavior. Frozen field
binding, ticker callback binding and saved-world attribution also remain open.
Do not mistake the SPAWNER spawn reason for a placed minecraft:spawner block.
