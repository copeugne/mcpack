# fabric-events-interaction-v0-entry source checkpoint

Extractor f633bf8. Independent r1 reproduction matches the manifest and all
disassembly bytes. Manifest SHA-256: 614f8f550bebcc2f4247a0be3905dbafc49647536eb93c547efac92c4f26bbd3.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-events-interaction-v0-0.7.13+86e0887119.jar --class-name net/fabricmc/fabric/impl/event/interaction/InteractionEventHooks.class --class-name net/fabricmc/fabric/mixin/event/interaction/PlayerAdvancementTrackerMixin.class --class-name net/fabricmc/fabric/mixin/event/interaction/ServerPlayerInteractionManagerMixin.class --class-name org/sinytra/fabric/events_interaction/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-events-interaction-v0-entry-r1
```

The common entry calls InteractionEventsRouter.onInitialize; this remains open. Captured hooks forward existing player/entity/block interaction and block-break callbacks. Client initialization is guarded.

Source capture alone does not close whole-provider membership.
