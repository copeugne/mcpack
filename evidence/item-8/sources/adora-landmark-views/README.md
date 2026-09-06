# AdoraBuild landmark comparison views

Generated with tools/view_item8_betterend_ruins.py at 0ea3ed6a from retained
adorabuild-structures-2.11.0-neoforge-1.21.3.jar, SHA-256
6f399680da36dbb95b9a0dbf8b600f173e650be4d6bc25f50fcac792dcce081e.

Ten templates cover the five existing bubble, gateway, portal and fossil records.
All three compressed SVG sheets reproduced byte-for-byte independently and were
visually inspected. End bubbles include broad and pedestal habitat forms; the
ocean installation differs in envelope and contents. Gateway frames and decorated
fossil alternatives retain design differences. Canonical decisions follow separately.

The renderer scales templates independently, uses full cubes for partial blocks,
and omits fully occluded cells. Glass and water render as opaque cells, so the
existing NBT contents are necessary for habitat attribution. The ocean bubble's
bottom edge is clipped; use preserved dimensions and content for the full template.
These views do not establish generated placement, portal behavior, sculk behavior,
exposure or discovery distance. Green is only a plant-name hint.

```sh
uv run -m tools.view_item8_betterend_ruins --adora-landmarks --output evidence/item-8/sources/adora-landmark-views
uv run -m tools.view_item8_betterend_ruins --adora-landmarks --output evidence/raw/item8/adora-landmark-views-r1
uv run ruff check tools/view_item8_betterend_ruins.py
uv run basedpyright tools/view_item8_betterend_ruins.py
```

Use fresh output directories and compare the three SVG gzip files before adding
this README. Derived PNGs are scratch inspection views.

| File | SHA-256 |
| --- | --- |
| bubbles.svg.gz | 6e6d7894a258b901b10d308d8b89621ad73e0d9bd45611dfe40c5a39477cffe5 |
| fossils.svg.gz | 93ef706364521ea33bc004315c70a21742382e08efa5ce70e3c6dc48227ed2f8 |
| gateways_portal.svg.gz | dc96d67d325a1a21aa72e274076880c0a4e847a5c05f992bcfda0761b5aa9028 |
