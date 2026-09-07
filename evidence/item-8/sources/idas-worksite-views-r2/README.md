# IDAS worksite views with corrected framing

Generated with tools/view_item8_betterend_ruins.py at 381867b2 from retained
idas-1.13.7+1.21.1-neoforge.jar, SHA-256
7f5031dd90ae0b32d7fe5c6c47c877cac1eb95a178bc78d196cb24c17ce82522.

The first attempt at 4d60aff5 remains preserved under idas-worksite-views with its
clipping limitation. This revision changes only the worksite selection's row
spacing/height and horizontal origin. The exact eleven source templates, scale,
block projection and content remain unchanged. All four SVG gzip sheets reproduce
independently and were visually inspected. Their complete template silhouettes
now fit inside the sheets, including train, log and stable geometry previously
clipped. This resolves the demonstrated framing defect without a new renderer or
measurement system.

The dig-site pieces remain components, not additional families. Roofed structures,
terrain and vegetation still obscure interiors; preserved contents and full pool
and placement definitions are required for decisions. The renderer independently
rescales templates and treats partial blocks as cubes. These inspection views do
not prove assembled dimensions, runtime operation, placement or discovery distance.
Green is only a plant-name hint; no water is omitted.

```sh
uv run -m tools.view_item8_betterend_ruins --idas-worksites --output evidence/item-8/sources/idas-worksite-views-r2
uv run -m tools.view_item8_betterend_ruins --idas-worksites --output evidence/raw/item8/idas-worksite-views-r2
uv run ruff check tools/view_item8_betterend_ruins.py
uv run basedpyright tools/view_item8_betterend_ruins.py
```

Use fresh output directories and compare the four SVG gzip files before adding
this README. PNGs are scratch inspection views.

| File | SHA-256 |
| --- | --- |
| desert_dig.svg.gz | 784e12db3f6c6c53fd3eae9002dd8aa9bde7d8115281cb62cc48f4d8aa421361 |
| dig_site.svg.gz | 81cc201696671dc6a93b8ce95d044d65fc343f7d8b5f1fea9e331624374b9074 |
| transport.svg.gz | c445822b5e31c2335ee6030717c55a4c6f0e6196c0f125757ade7cea53691b2a |
| worksites.svg.gz | d69402d349cefde7d7c35022541fd06fe067697d06e96edd9f35c04e391a7e8e |
