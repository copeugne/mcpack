# fabric-interaction-router source roles

Extractor e957cf9. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: 1f6918e1d747541523585d23f29310ceb4a298516a221e80e05251cfa02d41e3.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-events-interaction-v0-0.7.13+86e0887119.jar --class-name net/fabricmc/fabric/impl/event/interaction/InteractionEventsRouter.class --output evidence/raw/item8/fabric-interaction-router-r1
```

Initialization registers block-attack and cancelled-break callbacks. The former forwards an existing block or state interaction. The latter sends existing block-state packets to the player. Neither generates a site.
