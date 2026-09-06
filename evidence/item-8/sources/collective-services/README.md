# Collective active NeoForge services

Extractor d0e87d7a. Nine service implementations. Independent r1 reproduction
matches source and manifest bytes. Manifest SHA-256:
be2d268ae5cce33d21ff9bbb098f7669de1d870882c31e070c2d4034836eef8d

```sh
uv run -m tools.inspect_item8_pool_elements --archive collective-1.21.1-8.25.jar --class-name com/natamus/collective/neoforge/services/NeoForgeBlockTagsHelper.class --class-name com/natamus/collective/neoforge/services/NeoForgeClientUtilsHelper.class --class-name com/natamus/collective/neoforge/services/NeoForgeEventTriggerHelper.class --class-name com/natamus/collective/neoforge/services/NeoForgeModLoaderHelper.class --class-name com/natamus/collective/neoforge/services/NeoForgeRegisterBlockHelper.class --class-name com/natamus/collective/neoforge/services/NeoForgeRegisterItemHelper.class --class-name com/natamus/collective/neoforge/services/NeoForgeRegisterKeyMappingHelper.class --class-name com/natamus/collective/neoforge/services/NeoForgeTeleportHelper.class --class-name com/natamus/collective/neoforge/services/NeoForgeToolFunctionsHelper.class --output evidence/raw/item8/collective-services-r1
```

Services register consumer-supplied blocks/items/key mappings, query tool/tag
and loader properties, set client rendering, forward portal events and teleport
existing entities to supplied destinations. They do not define independent
authored sites. Registration maps start empty. Reuse these roles without
tracing generic loader or teleport internals. Whole-provider initialization
and full payload/source binding remain open.
