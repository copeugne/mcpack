# fabric-entity-events-entry source roles

Extractor a2c1e65. Independent r1 reproduction matches the manifest and every
disassembly byte for byte. Manifest SHA-256:
f856b1bc1999cd9d480f5d8142b5561d05e62796bc6febf77d22588847531798.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-entity-events-v1-1.8.0+5ede667619.jar --class-name net/fabricmc/fabric/impl/entity/event/EntityEventHooks.class --class-name net/fabricmc/fabric/mixin/entity/event/EntityMixin.class --class-name net/fabricmc/fabric/mixin/entity/event/IItemStackExtensionMixin.class --class-name net/fabricmc/fabric/mixin/entity/event/LivingEntityMixin.class --class-name net/fabricmc/fabric/mixin/entity/event/MobEntityMixin.class --class-name net/fabricmc/fabric/mixin/entity/event/PlayerEntityMixin.class --class-name net/fabricmc/fabric/mixin/entity/event/PlayerManagerMixin.class --class-name net/fabricmc/fabric/mixin/entity/event/ServerPlayerEntityMixin.class --class-name net/fabricmc/fabric/mixin/entity/event/elytra/LivingEntityMixin.class --class-name net/fabricmc/fabric/mixin/entity/event/elytra/PlayerEntityMixin.class --class-name org/sinytra/fabric/entity_events/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-entity-events-entry-r1
```

The loader is empty. EntityEventHooks and nine declared common mixins forward damage, death, combat, conversion, respawn, join/leave, dimension-change, sleeping and elytra decisions to consumer callbacks. Bed position/state and flight flags affect existing entities. No independent site is composed by these paths.

The initial extraction attempt was rejected by argument parsing because the
new nested archives were absent from the allowlist. No output was produced;
a2c1e65 adds the exact nested identities before this successful capture.
These are source roles, not whole-provider closure or effective-consumer proof.
