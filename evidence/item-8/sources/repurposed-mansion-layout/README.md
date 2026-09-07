# Mansion layout and room selectors

Captured with extractor revision b56db35. All five captures and identities.json
reproduced byte for byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive repurposed_structures-7.5.21+1.21.1-neoforge.jar --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$LayoutGenerator.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$RoomCollection.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$FirstFloor.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$SecondFloor.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$ThirdFloor.class' --output evidence/raw/item8/repurposed-mansion-layout-b56db35
```

LayoutGenerator calls saveJigsawPiece for layout components and room selectors.
That method obtains a pool, selects a random element, wraps single elements in
MirroringSingleJigsawPiece, creates a pool piece and calls spawnChildPieces.
It then adds the parent. Thus direct room names alone do not establish complete
template reachability: attached child pools must also be reconciled. The
MirroringSingleJigsawPiece implementation is already preserved in pool-codecs;
reuse it rather than capture it again.

These ordinary disassemblies omit invokedynamic string-concatenation recipes
used for pool names. They cannot establish the exact complete component IDs.
Preserve this attempt and capture LayoutGenerator and the three floor selectors
with the existing verbose mode before deriving pool-name coverage. Do not
invent concatenated paths from packaged names. RoomCollection records the
floor/type fields; FirstFloor, SecondFloor and ThirdFloor provide selectors.
This is partial component evidence, not a completed family attribution.

Scoped extractor Ruff and Basedpyright passed. No new measurement or server run.
