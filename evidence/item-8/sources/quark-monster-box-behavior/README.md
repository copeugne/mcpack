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

## Selected packaged loot sources

The existing resource selector, with vanilla/mod_data and the verified
Lithostitched overlay, selects the following Quark-4.1-480.jar resources from
packaged-json-redacted.json.gz. The tracked test binds the catalog hash, selected
archive and resource hashes, and the complete spawn-selection document:

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py -k monster_box
```

- quark:misc/monster_box_spawns: b8f5f6566c55bb61ce0b0415ac256aee6a2bec157d882270054539f6b0116a22.
- quark:misc/monster_box: d55a75d3ff4510472cf68eed41fc5c2a40aa898629493d90b4ff57f4a444423d.
- quark:blocks/monster_box: 54529647aa2f43bc3a48fe1cf9379926ea6cbff35d1fbfee70fd74498d00288e.

The spawn-selection table has one pool and one roll, with witch, cave-spider
and zombie spawn eggs weighted 1, 2 and 7. These are authored selection weights,
not measured encounter frequencies or successful entity counts. The block's
ordinary loot table declares no pools. The separate misc/monster_box table is
an entity-context reward table, with one roll across weighted resources, food,
equipment and rarities. Its exact entries remain in the preserved catalog.

The already captured MonsterBoxModule.onDrops uses that reward table only when
enableExtraLootTable is true, the entity is on a ServerLevel and carries
quark:monster_box_spawned, doMobLoot is true, and the accessor's last-hurt-by-player
time is positive. It appends the resulting captured drops to the event's drops.
This is not a container reward and does not replace the spawn-selection table.
Event binding and the accessor's target semantics remain unresolved.

The first test execution passed but the type check rejected loot_table as an
undeclared selector kind. Adding that existing resource kind to the Literal
annotation required no selection-logic change. All 31 focused tests, Ruff and
Basedpyright then passed. No runtime or measurement system was added. Family
integration, effective callback/configuration binding and world attribution
remain open; the packaged table identity and entries need no further extraction.
