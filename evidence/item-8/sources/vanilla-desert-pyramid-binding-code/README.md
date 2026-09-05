# Desert pyramid constructor binding

This supplements the ordinary disassembly in `../vanilla-desert-pyramid-code`.
That output omitted the invokedynamic bootstrap target, so it could not directly
bind the structure's constructor callback to its piece class. The existing
extractor's verbose mode now preserves that target; the shared wrapper is also
preserved to show how the callback is invoked. No measurement system is added.

Manifest SHA-256: `f83997815e0225442cdcd1819b3b7b1c210c8296da1b22191c7bba31df5e3b1c`.
The structure's archive and class hashes match the earlier non-verbose capture.
Only the disassembly form differs; the earlier evidence remains intact.

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/levelgen/structure/SinglePieceStructure.class --class-name net/minecraft/world/level/levelgen/structure/structures/DesertPyramidStructure.class --output evidence/item-8/sources/vanilla-desert-pyramid-binding-code
uv run pytest -q tests/item8/test_desert_pyramid_binding.py
uv run ruff check tools/inspect_item8_pool_elements.py tests/item8/test_desert_pyramid_binding.py
uv run basedpyright tools/inspect_item8_pool_elements.py tests/item8/test_desert_pyramid_binding.py
```

Extraction, the focused binding test and scoped checks passed. Reproduce into a
fresh directory. Bootstrap entry 0 targets DesertPyramidPiece's constructor
(RandomSource, int, int). SinglePieceStructure stores the callback and supplied
width/depth, then invokes it with the generation random source and chunk minimum
X/Z, adding the returned piece once. findGenerationPoint returns empty when
getLowestY(context,width,depth) is below the generator sea level; otherwise it
uses WORLD_SURFACE_WG for the generation stub. This does not prove successful
post-processing, loot generation or the final extent of underground additions.

The complete verbose structure output is preserved because the bootstrap and
its call site must remain reproducibly linked. This is source evidence, not
another inventory, receipt or review framework. Continue cellar/content
reconciliation before integrating the desert pyramid family.
