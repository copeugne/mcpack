# Aether trap registration and event bindings

Extractor revision 0c645d6. The three disassemblies and identities reproduced
byte for byte. AetherBlocks is verbose because its registration and constructor
suppliers require bootstrap-method bindings. The large generated class capture
is isolated here, without unrelated implementation changes.

```sh
uv run -m tools.inspect_item8_pool_elements --archive aether-1.21.1-1.5.10-neoforge.jar --class-name com/aetherteam/aether/block/AetherBlocks.class --class-name com/aetherteam/aether/event/AetherEventDispatch.class --class-name com/aetherteam/aether/event/TriggerTrapEvent.class --output evidence/raw/item8/aether-trap-bindings-r1
```

For trapped_carved_stone, the registration's InvokeDynamic #94 binds
lambda$static$76. It constructs TrappedBlock with AetherEntityTypes.SENTRY
through DeferredHolder.get (bootstrap 8), and a facade supplier through
bootstrap 14 to lambda$static$75, which returns CARVED_STONE.defaultBlockState.
For trapped_sentry_stone, InvokeDynamic #95 binds lambda$static$78, again using
SENTRY through bootstrap 8. Its facade supplier uses bootstrap 13 to
lambda$static$77, which returns SENTRY_STONE.defaultBlockState.
This resolves the two Bronze processor output blocks to a Sentry-supplying
TrappedBlock implementation. Exact entity registry-key binding is distinct
from this verified Java field/type relationship.

AetherEventDispatch.onTriggerTrap creates TriggerTrapEvent, posts it to
NeoForge.EVENT_BUS and returns the inverse of isCanceled. TriggerTrapEvent
extends BlockEvent, implements ICancellableEvent, and retains the Player.
Together with aether-trapped-block, the source chain is a player step, an
uncancelled event, facade replacement, and a server TRIGGERED spawn attempt.
It is not a conventional spawner or a natural-spawn rule. The captured
caller discards spawn success. Retained event handlers and actual runtime
activation remain separate evidence questions; do not claim they cannot cancel.

These findings resolve the constructor/event implementation gaps recorded in
aether-trapped-block/README.md. Integrate the Sentry source into the Bronze
family decision using these identities. Do not repeat the supplier captures.
Scoped extractor Ruff and Basedpyright passed. No runtime measurement.
