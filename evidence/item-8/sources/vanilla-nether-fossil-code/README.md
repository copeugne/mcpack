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

## Family integration

The family decision now resolves all fourteen references against the frozen
catalog and records seven source-backed attributes: nominal footprint and height,
authored mobs, container loot, spawners, enemy source and placement classification.
Each selected template has only air and bone-block palette entries, with empty
entity and block-entity lists. Dimensions are retained per template to preserve
paired axes. The focused test derives those dimensions directly from the catalog
and checks the complete reference set, content and source hashes.

```sh
uv run pytest -q tests/item8/test_nether_fossil_sources.py tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_nether_fossil_sources.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_nether_fossil_sources.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-nether-fossil-content.json
```

These checks concern the affected family and existing inventory joins. They do
not introduce a measurement system. Intended hostility, visual discoverability
and effective retained-mod transformations remain unresolved. No family is added
or removed, and existing dimension and world-observation evidence is preserved.

All 62 affected tests passed. Scoped Ruff and Basedpyright passed after fixing
a line wrap and explicitly converting palette names to strings in the new test.
The final focused test passed as well. Decision SHA-256:
`d1af44e8dd07c4ab772e223d52f16984520eb5ba6517db884bc0d06c99c69593`.
