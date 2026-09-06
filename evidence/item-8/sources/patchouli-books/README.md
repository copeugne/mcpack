# Patchouli book and multiblock roles

Extractor 16d67c28. Six classes. Independent r1 reproduction matches all
source and manifest bytes. Manifest SHA-256:
93320b5af0e1803d4d60cfce77976ace1dec956970af16ce26eb6cf4a67b2d25

```sh
uv run -m tools.inspect_item8_pool_elements --archive Patchouli-1.21.1-93-NEOFORGE.jar --class-name vazkii/patchouli/common/book/BookRegistry.class --class-name vazkii/patchouli/common/handler/LecternEventHandler.class --class-name vazkii/patchouli/common/handler/ReloadContentsHandler.class --class-name vazkii/patchouli/common/multiblock/AbstractMultiblock.class --class-name vazkii/patchouli/common/multiblock/MultiblockRegistry.class --class-name vazkii/patchouli/neoforge/network/NeoForgeNetworkHandler.class --output evidence/raw/item8/patchouli-books-r1
```

BookRegistry loads consumer book definitions into a book map. Server startup
sends book reload messages. Both registered packets are client-bound, opening
or reloading books. Lectern interaction places, removes or opens books in an
existing lectern. MultiblockRegistry starts with an empty consumer map.
AbstractMultiblock supports validation/display and an explicit caller-driven
place method that writes blocks. It is not an automatically registered world
generator or an independent authored family. Preserve this placement capability;
do not claim the library cannot write blocks.
