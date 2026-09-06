# Architectury startup and biome membership boundary

Extractor fc0d12d4. Independent r1 reproduction matches all source and manifest
bytes. Manifest SHA-256:
6cba03224fd0a49c2d65ad146c6611943639c7efb3e4b1dbd5bd6fe4968b1fe8

```sh
uv run -m tools.inspect_item8_pool_elements --archive architectury-13.0.8-neoforge.jar --class-name dev/architectury/event/EventHandler.class --class-name dev/architectury/event/forge/EventHandlerImpl.class --class-name dev/architectury/event/forge/EventHandlerImplCommon.class --class-name 'dev/architectury/event/forge/EventHandlerImplCommon$ModBasedEventHandler.class' --class-name dev/architectury/event/forge/EventHandlerImplServer.class --class-name 'dev/architectury/event/forge/EventHandlerImplServer$ModBasedEventHandler.class' --class-name dev/architectury/registry/level/biome/forge/BiomeModificationsImpl.class --class-name 'dev/architectury/registry/level/biome/forge/BiomeModificationsImpl$BiomeModifierImpl.class' --output evidence/raw/item8/architectury-startup-r1
```

Common startup registers existing-event forwarding and setup callbacks. Server
event registration returns without adding handlers. The biome modifier serializer
applies predicate/consumer pairs from four initially empty lists. Consumers
supply their modifications; these paths define no independent family. Preserve
consumer biome/spawn effects for attribution. The entry also references entity
spawn packet initialization, which remains to be bound before provider closure.
