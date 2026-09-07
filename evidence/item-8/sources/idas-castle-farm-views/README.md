# IDAS castle and farmhouse comparisons

Generated with tools/view_item8_betterend_ruins.py at 3356f800 from retained
idas-1.13.7+1.21.1-neoforge.jar, SHA-256
7f5031dd90ae0b32d7fe5c6c47c877cac1eb95a178bc78d196cb24c17ce82522.

The selection includes all three castle main/bottom pairs and the ordinary
farmhouse, abandoned farmhouse and path. All three SVG gzip files independently
reproduce exactly. Castle bottom and corrected farmhouse sheets were visually
inspected and fit within the frames. The farmhouse alternatives share the main
building arrangement, with visible condition and furnishing differences.
Castle main conversion completed successfully and all three layouts fit within
their frames. They have different tower, courtyard and roof arrangements, not
merely material substitutions. Their distinct layouts and extents must remain
explicit in the grouping decision. No canonical family decision is closed by
this source increment alone.

The initial renderer at 7c00d51e clipped the left end of the farmhouse path.
That rejected view is reproducible at that commit using the command below.
Its farmhouse.svg.gz SHA-256 was
f6187f17b61e08b745c6fd6a162b360c9a475f085acdba1310dcfad4eb513632.
Commit 3356f800 shifts only that template within its frame. Castle sheets
remain byte-identical. The original outputs remain in the local raw evidence
directories idas-castle-farm-views-r1 and idas-castle-farm-views-rejected-r1.

Templates are independently scaled. Opaque blocks hide interiors. Partial blocks
appear as cubes, and fully occluded cells are omitted. Green is a plant-name hint.
These views do not prove effective placement, encounters or discovery distance.
Pool declarations, full template contents and connector evidence must also
inform the family decisions.

```sh
uv run -m tools.view_item8_betterend_ruins --idas-castle-farm --output evidence/item-8/sources/idas-castle-farm-views
uv run -m tools.view_item8_betterend_ruins --idas-castle-farm --output evidence/raw/item8/idas-castle-farm-views-r2
uv run ruff check tools/view_item8_betterend_ruins.py
uv run basedpyright tools/view_item8_betterend_ruins.py
```

Use fresh output directories and compare SVG gzip files before adding this README.
PNG conversions are scratch inspection views.

| File | SHA-256 |
| --- | --- |
| castle_main.svg.gz | 7b0992014147e431b322aff6a29cb2887f495ac4ad37bc2e874c2dc6c37a81cf |
| castle_bottom.svg.gz | 5d2e40ed8957e97b3c95fa3b710dfdd7756ef381767ab83f4ef485f3fd8e4d26 |
| farmhouse.svg.gz | 8c2f8e832583b85d7683dfa0398f8f82aac7585d8df643ed999b9297e102686c |
