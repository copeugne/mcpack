# Chipped contribution sources

Extractor be235a87. Seven classes cover entries, common initialization,
common hooks and crafting packet registration. Independent r1 reproduction
matches every source and manifest byte. Manifest SHA-256:
64a01288e53c71d7055d8d87ecb37488a556b7681c6317199ff23fc889876e42

```sh
uv run -m tools.inspect_item8_pool_elements --archive chipped-neoforge-1.21.1-4.0.2.jar --class-name earth/terrarium/chipped/Chipped.class --class-name earth/terrarium/chipped/client/neoforge/ChippedClientNeoForge.class --class-name earth/terrarium/chipped/common/network/NetworkHandler.class --class-name earth/terrarium/chipped/common/network/ServerboundCraftPacket.class --class-name earth/terrarium/chipped/mixins/BlockBehaviourMixin.class --class-name earth/terrarium/chipped/mixins/NetherWartBlockMixin.class --class-name earth/terrarium/chipped/neoforge/ChippedNeoForge.class --output evidence/raw/item8/chipped-provider-r1
```

Startup initializes blocks/items, creative tabs, menus and recipes, and adds
Chipped barrels to the vanilla barrel block-entity type. Common hooks handle
Chipped block drops and nether-wart support blocks. The registered crafting
packet type handler remains to be bound before provider closure.
