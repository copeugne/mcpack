# Aether trapped-block encounter source

Captured using extractor revision 11564b4. The disassembly and identities
reproduced byte for byte:

```sh
uv run -m tools.inspect_item8_pool_elements --archive aether-1.21.1-1.5.10-neoforge.jar --class-name com/aetherteam/aether/block/dungeon/TrappedBlock.class --output evidence/raw/item8/aether-trapped-block-r1
```

TrappedBlock stores an entity-type supplier and a facade-state supplier.
stepOn only enters its activation path for a Player and a true result from
AetherEventDispatch.onTriggerTrap. It replaces its block with the supplied
facade state before checking for ServerLevel. On the server it projects a
point from the block using player yaw, clips from the player's position,
and adjusts a block hit to the adjacent position on the hit face. It then
calls the supplied EntityType.spawn with MobSpawnType.TRIGGERED and plays
the trap sound. Both the block-write and spawn results are discarded.

This is a player-triggered entity source, not natural spawning or a conventional
spawner block. It does not prove a successful spawn: the activation hook,
supplied type, engine conditions and retained handlers can affect the result.
The source alone also does not establish which registered trapped blocks use
which entities. Bind AetherBlocks constructor suppliers and the trap event
before assigning exact species or effective trigger conditions in the inventory.
Do not infer the entity from a trapped block's name.

The selected Bronze processor inputs already contain trapped_carved_stone
and trapped_sentry_stone output states. Their registration join remains open;
this capture resolves the shared block implementation, not that missing join.
Scoped extractor Ruff and Basedpyright passed. No runtime experiment or new
measurement system was added.
