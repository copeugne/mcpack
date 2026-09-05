# Vanilla Nether fossil source inspection

The existing extractor preserves three classes from the frozen mapped server.
Manifest SHA-256: `611e91bd71be08103760e8cd78339d1f904655941601f37214db08dd6a31b44e`.
Archive SHA-256: `26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/levelgen/structure/structures/NetherFossilStructure.class --class-name net/minecraft/world/level/levelgen/structure/structures/NetherFossilPieces.class --class-name 'net/minecraft/world/level/levelgen/structure/structures/NetherFossilPieces$NetherFossilPiece.class' --output evidence/item-8/sources/vanilla-nether-fossil-code
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Extraction and scoped checks passed. Reproduce into a fresh output directory.
The manifest binds archive, class and disassembly hashes. No new measurement
system or server run is needed for this source inspection.

`NetherFossilPieces.addPieces` selects a random rotation and one entry from
FOSSILS, then adds exactly one piece. The array contains the fourteen default
namespace references `nether_fossils/fossil_1` through `fossil_14`. They are
alternatives within one family, not fourteen families.

`NetherFossilStructure.findGenerationPoint` chooses X and Z within the chunk,
samples its configured height provider, and searches downward in the generator's
base column. It requires air above soul sand or a block with a sturdy upward
face. The final support Y must exceed the generator's sea level; otherwise the
candidate is rejected. The piece uses that support position without an added
vertical offset. The packaged definition samples uniformly from absolute Y 32
to two below the world's top; this is the initial sample, not the final Y.

Piece settings use the selected rotation, no mirror and STRUCTURE_AND_AIR.
The data-marker handler returns immediately. Post-processing expands the supplied
bounding box to encompass the template box before calling base template placement.
There is no additional mob, loot or spawner action in these three classes.

Source behavior is distinct from generated-world observation. Template content,
effective retained-mod behavior and remaining family attributes must still be
reconciled before Item 8 closure. Existing dimension and world observations are
preserved; this inspection does not establish exposure or visual range.
