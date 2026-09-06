# AdoraBuild palace, temple and sand design comparisons

Generated with tools/view_item8_betterend_ruins.py at e84a5261 from retained
adorabuild-structures-2.11.0-neoforge-1.21.3.jar, SHA-256
6f399680da36dbb95b9a0dbf8b600f173e650be4d6bc25f50fcac792dcce081e.

Sixteen templates cover eight existing records: ancient palace, dark oak mansion,
End temple, ocean temple, red sand temple, buried sand castle, surface sand castle
and sand pyramid. All three SVG gzip sheets reproduce byte-for-byte independently
and were visually inspected. Palace layouts differ in enclosure and roof shape;
End temples share corner-column detailing; buried castles share a tiered form.
Canonical decisions follow separately with packaged contents and definitions.

Opaque cells obscure the ocean templates, so this projection alone does not
resolve their architecture. The renderer independently rescales templates, uses
full cubes for partial blocks and omits fully occluded cells. Full template
height, including empty space, affects displayed scale. Bottom geometry crosses
the palace/mansion and ocean sheet boundaries. Preserved NBT supplies full sizes
and hidden contents. These views do not prove effective placement, exposure,
discovery distance or assembled world geometry. Green is a plant-name hint only.

```sh
uv run -m tools.view_item8_betterend_ruins --adora-monuments --output evidence/item-8/sources/adora-monument-views
uv run -m tools.view_item8_betterend_ruins --adora-monuments --output evidence/raw/item8/adora-monument-views-r1
uv run ruff check tools/view_item8_betterend_ruins.py
uv run basedpyright tools/view_item8_betterend_ruins.py
```

Use fresh output directories and compare the SVG gzip files before adding this
README. PNGs are scratch inspection views.

| File | SHA-256 |
| --- | --- |
| end_ocean_temples.svg.gz | 99538d48190234027b950e59c0bdbbd1f1719b83bebab086435d41437757a8f9 |
| palaces_mansion.svg.gz | 8852228e8bb443076ff655f63e50e4491471a327cc64b39c529f50582f7347bd |
| sand_designs.svg.gz | 829df11804c58354fae0d55fc0e000d7259312217a267e94270dea7058348fb8 |
