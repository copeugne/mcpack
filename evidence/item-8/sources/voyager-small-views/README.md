# Voyager small-design comparisons

Renderer bfc31ecc selects twelve templates from the hash-verified retained
MoogsVoyagerStructures-1.21-5.0.11.jar archive. All three sheets were manually
inspected and independently reproduced byte for byte. The selected-path pilot
and scoped Ruff/Basedpyright pass. Existing Nether landmark outputs remain
byte-identical after the narrow CLI and output-serialization change.

```sh
uv run -m tools.view_item8_betterend_ruins --voyager-small --output evidence/raw/item8/voyager-small-views-r1
```

These reuse the existing cube projection, with occluded cells omitted and each
template rescaled independently. Partial block models and hidden interiors are
not rendered. The path layouts extend beyond the sheet's lower edge; compare
layout orientation with their preserved template sizes and contents, not screen
scale or visible area. These diagrams are not footprint measurements or actual
generated-world observations. Benches use partial blocks whose exact furniture
shape must be read with the preserved palette and block-entity records.

Compressed SHA-256 identities:

- benches.svg.gz: 35d62597055436a8849566932cecb757102980b541c59675fbfc5733ec848461
- harvest_heaps.svg.gz: d14995e3e1a09241336a73414285231ca606f6ecf972200e6bb00cbef79b9aae
- paths.svg.gz: 0898adbfdaa79be0c7f2bc0cf04016188ae56c63cd5695ba48a70f14553884b1
