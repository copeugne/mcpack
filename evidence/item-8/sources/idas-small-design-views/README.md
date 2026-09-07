# Remaining IDAS design comparisons

Generated with tools/view_item8_betterend_ruins.py at 4323e1e3 from retained
idas-1.13.7+1.21.1-neoforge.jar, SHA-256
7f5031dd90ae0b32d7fe5c6c47c877cac1eb95a178bc78d196cb24c17ce82522.

All twelve selected templates were visually inspected across the four sheets.
All fit within their frames. The abandoned-house alternatives share a tall
roofed dwelling form; the cottage alternatives share a much smaller dwelling
form. Brickhouse, windmill and connecting path remain separate component views.
The low camp and tall guild, church and narrow ruined fort, and irregular stump
have distinct forms. Full contents, processors and connectors must also inform
the canonical decisions. No family decision closes from this source alone.

All four SVG gzip files independently reproduce exactly. Templates are
independently scaled. Opaque blocks hide interiors. Partial blocks appear as
cubes, and fully occluded cells are omitted. Green is a plant-name hint. These
views do not prove effective placement, encounters or discovery distance.

```sh
uv run -m tools.view_item8_betterend_ruins --idas-small-designs --output evidence/item-8/sources/idas-small-design-views
uv run -m tools.view_item8_betterend_ruins --idas-small-designs --output evidence/raw/item8/idas-small-design-views-r1
uv run ruff check tools/view_item8_betterend_ruins.py
uv run basedpyright tools/view_item8_betterend_ruins.py
```

Use fresh output directories and compare SVG gzip files before adding this README.
PNG conversions are scratch inspection views.

| File | SHA-256 |
| --- | --- |
| houses.svg.gz | 8c9891bf5a9932d60f23728de08ad19daced475c2201d51e75fc9ced04aa5965 |
| brickhouse.svg.gz | bab0ce429e5446ef455fcc71fe43b312c5e3f09ce5f33b1e0703c4fb7140af60 |
| camp_guild.svg.gz | dbb73bdd1debd6cd178f76d14f11c7f3ba47308d718af82f200ffc3c2576923e |
| ruins_stump.svg.gz | d41652050b41e0649cee3fc89ab5602b4bd519371a328174770285a3dfa91cef |
