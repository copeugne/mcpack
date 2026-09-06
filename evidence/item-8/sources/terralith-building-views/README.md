# Terralith building comparison views

Generated with tools/view_item8_betterend_ruins.py at 308b0df2 from the frozen
Terralith_1.21.1_v2.6.2_Neoforge.jar, SHA-256
 d38bd304897731b42f6c013cdc07e082e74411e80c74aabcee385251beb3b546.

These four fixed sheets cover the remaining ten Terralith design records with
24 architectural templates. Entity-only components are preserved in the existing
pool/content catalog; the sheets do not enumerate a generated population.
The accepted compressed SVGs reproduce byte-for-byte in an independent run.
All four sheets were visually inspected. Surface and mage-complex bottom edges
clip some low geometry; preserved NBT dimensions and content remain authoritative.
The diagrams scale templates independently, use full cubes for partial blocks,
and omit fully occluded cells. They do not expose interiors, model textures,
simulate assembly or establish world placement, exposure or discovery distance.
Green is only a plant-name hint. Canonical decisions remain a separate increment.

```sh
uv run -m tools.view_item8_betterend_ruins --terralith-buildings --output evidence/item-8/sources/terralith-building-views
uv run -m tools.view_item8_betterend_ruins --terralith-buildings --output evidence/raw/item8/terralith-building-views-r1
uv run ruff check tools/view_item8_betterend_ruins.py
uv run basedpyright tools/view_item8_betterend_ruins.py
```

Compare the four generated SVG gzip files before adding this README. Both output
directories must be fresh. PNGs used for inspection are derived scratch views.

| File | SHA-256 |
| --- | --- |
| mage_complex.svg.gz | 21a90b91e0c67042eada4785954f465ae4caf9010909ce7729c9e14a145bbf10 |
| mage_towers.svg.gz | 98af6018c4d0365f032ba16f028587e893985fbd68e0ce8c5e5c51c2c78c1748 |
| surface.svg.gz | 20fe7fff318d9198f10e6d13f45714c359277fbe3e293b8d5d544ffc3b9bbb5f |
| underground.svg.gz | 99a68218e2919185d4d06aef24d7baf7023d20495300e6d02a483e2f71c08a52 |
