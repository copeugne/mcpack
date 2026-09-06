# Repurposed assembly boundaries

Extractor c12cab1 captures seven structure generators, the common jigsaw manager
and assembler, and the piece-count reload manager. Independent r1 extraction
matches every generated file.
Manifest SHA-256: 10a3a2a15d647c5c52c171034c84be9c2fc68e1fe42dd571e8a6c725a6de6746.

```sh
uv run -m tools.inspect_item8_pool_elements --archive repurposed_structures-7.5.21+1.21.1-neoforge.jar --class-name com/telepathicgrunt/repurposedstructures/world/structures/CityNetherStructure.class --class-name com/telepathicgrunt/repurposedstructures/world/structures/GenericJigsawStructure.class --class-name com/telepathicgrunt/repurposedstructures/world/structures/GenericNetherJigsawStructure.class --class-name com/telepathicgrunt/repurposedstructures/world/structures/MineshaftEndStructure.class --class-name com/telepathicgrunt/repurposedstructures/world/structures/MineshaftStructure.class --class-name com/telepathicgrunt/repurposedstructures/world/structures/ShipwreckNetherStructure.class --class-name com/telepathicgrunt/repurposedstructures/world/structures/StrongholdEndStructure.class --class-name com/telepathicgrunt/repurposedstructures/world/structures/pieces/PieceLimitedJigsawManager.class --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/PieceLimitedJigsawManager$Assembler.class' --class-name com/telepathicgrunt/repurposedstructures/misc/structurepiececounter/StructurePieceCountsManager.class --output evidence/raw/item8/repurposed-assembly-r1
```

These sources resolve the remaining assembly consumers of existing candidates.
Source capture alone does not establish provider closure or runtime placement.
