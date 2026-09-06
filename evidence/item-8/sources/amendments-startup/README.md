# Amendments startup and Blueprint integration

Extractor 0f2e1b1a570659ec4becb580c0a49b6d7b575ba8. Independent r1 reproduction
matches all three disassemblies and the identity manifest. Manifest SHA-256:
f861ebbe6b01e0593fab776764dc771e6c8f0fadd14dedfc75f067508630d59c

```sh
uv run -m tools.inspect_item8_pool_elements --archive amendments-1.21-2.0.15-neoforge.jar --class-name net/mehvahdjukaar/amendments/Amendments.class --class-name net/mehvahdjukaar/amendments/events/ModEvents.class --class-name net/mehvahdjukaar/amendments/integration/neoforge/BlueprintIntegration.class --output evidence/raw/item8/amendments-startup-r1
```

Amendments.init registers configuration, mod registries, networking, setup and
reload callbacks, dispenser behavior, recipe flags, tabs and POI states.
Setup invokes Supplementaries compatibility and additional block placements;
reload installs interaction overrides. ModEvents handles player block/item/
entity interactions. BlueprintIntegration registers StructureCauldronHack and
the blockstate_replace repaletter codec used by the three packaged replacements.

These captures establish the direct delegates. Resolve the registry, temporary
cauldron block and replacement implementation before concluding the provider
membership disposition. No independent family or provider closure is asserted
by this source increment.
