# IDAS wizard tower and nexus comparisons

Generated with tools/view_item8_betterend_ruins.py at 81454aa4 from retained
idas-1.13.7+1.21.1-neoforge.jar, SHA-256
7f5031dd90ae0b32d7fe5c6c47c877cac1eb95a178bc78d196cb24c17ce82522.

The selection includes all six wizard-tower main/bottom components and all six
nexus alternatives. All three SVG gzip files independently reproduce exactly.
Wizard tower and bottom sheets were visually inspected and fit within the frames.
The main tower silhouettes correspond; lower pieces preserve material and terrain
differences. Interior spawners and loot must also inform the family decision.
Nexus visual inspection is pending; source generation alone does not settle it.

Templates are independently scaled. Opaque blocks hide interiors. Partial blocks
appear as cubes, and fully occluded cells are omitted. Green is a plant-name hint.
These views do not prove effective placement, encounters or discovery distance.
No family decision is closed by this source increment alone.

```sh
uv run -m tools.view_item8_betterend_ruins --idas-tower-nexus --output evidence/item-8/sources/idas-tower-nexus-views
uv run -m tools.view_item8_betterend_ruins --idas-tower-nexus --output evidence/raw/item8/idas-tower-nexus-views-r1
uv run ruff check tools/view_item8_betterend_ruins.py
uv run basedpyright tools/view_item8_betterend_ruins.py
```

Use fresh output directories and compare SVG gzip files before adding this README.
PNG conversions are scratch inspection views.

| File | SHA-256 |
| --- | --- |
| wizard_towers.svg.gz | 1c220e475cc0c338c08036ca39421db3cb80e93a81b0cb0be0b25d3a1ecbb2e6 |
| wizard_bottoms.svg.gz | d9c1e09d8ca8f1af5b5971e14a9e43e5abdae99db6d1e7fd90dd75fa5d79b116 |
| nexus.svg.gz | cbf028bb067a98fca3595c78e082902f2f7718ef35d8f69d445470294d4a7f4c |
