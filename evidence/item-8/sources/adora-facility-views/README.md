# AdoraBuild vessel and facility comparison views

Generated with tools/view_item8_betterend_ruins.py at a02d4bd5 from retained
adorabuild-structures-2.11.0-neoforge-1.21.3.jar, SHA-256
6f399680da36dbb95b9a0dbf8b600f173e650be4d6bc25f50fcac792dcce081e.

Seventeen templates cover six existing records: watercraft, End ship, frozen
shelters, libraries, mountain mines and prisons. All four compressed SVG sheets
reproduce byte-for-byte independently and were visually inspected. The vessels
show distinct raft, covered-boat and sailing-ship forms. Source contents preserve
inhabitants, furnishings and loot hidden by the projection. Decisions follow separately.

The renderer independently rescales templates, uses full cubes for partial blocks,
and omits fully occluded cells. Source dirt/stone enclosures obscure interiors;
NBT content and placement inputs are required alongside these views. Bottom
edges of the vessel, frozen-shelter and prison rows approach or cross the sheet
boundary; preserved NBT supplies full dimensions. Filename size labels are not
measurements: library_small_1 has a larger template envelope than library_large_1.
The views do not prove effective world placement, geometry, exposure, machinery
operation or discovery distance. Green is only a plant-name hint.

```sh
uv run -m tools.view_item8_betterend_ruins --adora-facilities --output evidence/item-8/sources/adora-facility-views
uv run -m tools.view_item8_betterend_ruins --adora-facilities --output evidence/raw/item8/adora-facility-views-r1
uv run ruff check tools/view_item8_betterend_ruins.py
uv run basedpyright tools/view_item8_betterend_ruins.py
```

Use fresh output directories and compare the four SVG gzip files before adding
this README. PNGs are scratch inspection views.

| File | SHA-256 |
| --- | --- |
| frozen_shelters.svg.gz | 3c944682c913092e23d77685c7dbde544209b172effaa76e49cf87f3499325d4 |
| libraries.svg.gz | 636da4408fd96d08077ab5a32f80faaed476d632964379cc29dd5fb53be60e58 |
| mines_prisons.svg.gz | 5105ffeaaf5c58bbb77df4bec81df60667563307af4b674f45d43fd9d2ecfdea |
| vessels.svg.gz | 258dd16f8cc65f277e0e540de07dfefff051937e7b25dfdfe74d0141c697edb6 |
