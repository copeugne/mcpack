# IDAS portal, camp and ship comparisons

Generated with tools/view_item8_betterend_ruins.py at de940fd2 from retained
idas-1.13.7+1.21.1-neoforge.jar, SHA-256
7f5031dd90ae0b32d7fe5c6c47c877cac1eb95a178bc78d196cb24c17ce82522.

Thirteen templates cover ancient portals (four pieces), underground camps
(four alternatives), sunken ships (three alternatives) and detached ship ruins
(two alternatives). All three SVG gzip sheets independently reproduce exactly
and were visually inspected. Portal halves show corresponding Overworld/Nether
architecture. Camps show paired small workstation arrangements. Ships share a
long hull form distinct from detached wreckage. Full pool graphs, contents,
processors and placement definitions accompany the separate canonical decisions.

The renderer independently rescales templates, uses full cubes for partial blocks
and omits fully occluded cells. It does not omit water in this selection. Long
titles approach or overlap adjacent cells; the tracked selection preserves names.
Bottom wreckage geometry crosses the sheet boundary. Source NBT preserves full
dimensions and content. Projections do not prove effective assembly, portal use,
machinery operation, mob creation, placement or discovery distance. Green is only
a plant-name hint. Template components are not additional families.

```sh
uv run -m tools.view_item8_betterend_ruins --idas-related --output evidence/item-8/sources/idas-related-views
uv run -m tools.view_item8_betterend_ruins --idas-related --output evidence/raw/item8/idas-related-views-r1
uv run ruff check tools/view_item8_betterend_ruins.py
uv run basedpyright tools/view_item8_betterend_ruins.py
```

Use fresh directories and compare the three SVG gzip files before adding this
README. PNGs are scratch inspection views.

| File | SHA-256 |
| --- | --- |
| camps.svg.gz | 0485afb5dc85a8b038a50a4850778a0dd8b9140242342a5961fecbec4f02692c |
| portals.svg.gz | 0a4053abbd39c653300a4b3bfae8662dce33270038c8414dc28065bc9ceadaad |
| ships.svg.gz | 4d6437867341af61d2b4a157d8ff680d8ae59275bea635b5e8b37c0815669986 |
