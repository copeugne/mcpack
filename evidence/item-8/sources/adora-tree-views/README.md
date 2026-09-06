# AdoraBuild furnished tree comparison views

Generated with tools/view_item8_betterend_ruins.py at 4aa39101 from retained
adorabuild-structures-2.11.0-neoforge-1.21.3.jar, SHA-256
6f399680da36dbb95b9a0dbf8b600f173e650be4d6bc25f50fcac792dcce081e.
The archive filename is its identity, not a compatibility inference.

Seven templates cover the existing tree, tree-house and mushroom records.
Both compressed SVG sheets reproduce byte-for-byte independently and were visually
inspected. The birch template includes a substantial below-tree room volume;
cherry/oak have tree-and-camp forms; the houses have tree-integrated building forms;
the mushroom has a stem-and-cap residence form. Source contents supply furnishing
and loot details hidden by this projection. Decisions follow separately.

The diagrams independently rescale templates and use full cubes for partial blocks.
They omit fully occluded cells and do not show interiors, textures or generated
terrain. Green is a plant-name hint. They do not establish effective world placement,
exposure, functioning equipment or discovery distance. The oak low base approaches
the sheet edge; raw NBT supplies complete dimensions and content.

```sh
uv run -m tools.view_item8_betterend_ruins --adora-trees --output evidence/item-8/sources/adora-tree-views
uv run -m tools.view_item8_betterend_ruins --adora-trees --output evidence/raw/item8/adora-tree-views-r1
uv run ruff check tools/view_item8_betterend_ruins.py
uv run basedpyright tools/view_item8_betterend_ruins.py
```

Use fresh output directories; compare the two SVG gzip files before adding this
README. Derived PNGs are scratch inspection views.

| File | SHA-256 |
| --- | --- |
| tree_houses.svg.gz | dc9ed52cfcae6cf8d7044ccd11269bcc24319a58bfb74449152b4d57be4c59c5 |
| trees_mushroom.svg.gz | 5eac4c0520ce6979b2192b3a80f746747ae2c22c0fc68efd0635ac68ad2a9ce6 |
