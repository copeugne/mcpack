# Eight IDAS building comparisons

Generated with tools/view_item8_betterend_ruins.py at 15a4efcb from retained
idas-1.13.7+1.21.1-neoforge.jar, SHA-256
7f5031dd90ae0b32d7fe5c6c47c877cac1eb95a178bc78d196cb24c17ce82522.

Eight complete templates cover abandoned lighthouse, fisherman's lodge, hermit's
hollow, hunter's cabin, botanist, mason house, pumpkin cafe and wacky wares. All
four SVG gzip sheets independently reproduce exactly and were visually inspected.
The corrected worksite framing also contains these full silhouettes. They show
separate architectural forms, including the lodge on tall supports, low planted
hollow and tall pumpkin cafe. The final decisions must also preserve authored
inhabitants, loot, furnishings and exact placement definitions.

Templates are independently scaled; this is not a common-scale size comparison.
Opaque roof, terrain and vegetation hide interiors. Partial blocks appear as
cubes and fully occluded cells are omitted. Long labels approach or overlap at
column edges; the tracked selector preserves exact names. These views do not
prove effective placement, inhabited status, machinery operation or discovery
distance. Green is only a plant-name hint. Optional and nested entity references
remain declarations until their runtime status is established separately.

```sh
uv run -m tools.view_item8_betterend_ruins --idas-buildings --output evidence/item-8/sources/idas-building-views
uv run -m tools.view_item8_betterend_ruins --idas-buildings --output evidence/raw/item8/idas-building-views-r1
uv run ruff check tools/view_item8_betterend_ruins.py
uv run basedpyright tools/view_item8_betterend_ruins.py
```

Use fresh output directories and compare the four SVG gzip files before adding
this README. PNGs are scratch inspection views. This source increment does not
by itself close any family record.

| File | SHA-256 |
| --- | --- |
| lighthouse_fishing.svg.gz | c19c7c98eddccb49e1b8d1cdf59185d8a8d5f683acee915953c8880640711d9b |
| shops.svg.gz | f5a681a08ca1792bbfd7d81ceb2906db2c93a51c421ed8a4c89dfa704f2e8924 |
| woodland.svg.gz | 0faf539dc4d8996b7720220a38ae31757a458a96529f0da6aaa801bc14ff7f15 |
| workshops.svg.gz | 21e457c9a0f7fa42900d96f9c27b52a6b8a9573a92ea0059ab1de10921ca30dd |
