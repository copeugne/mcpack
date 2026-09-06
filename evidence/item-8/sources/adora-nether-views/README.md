# AdoraBuild Nether architecture comparison views

Generated with tools/view_item8_betterend_ruins.py at cb501199 from retained
adorabuild-structures-2.11.0-neoforge-1.21.3.jar, SHA-256
6f399680da36dbb95b9a0dbf8b600f173e650be4d6bc25f50fcac792dcce081e.

Twenty-three templates cover five existing records: basalt chambers, blackstone
bastions, blackstone temple, Nether fortresses and Nether temple. All four SVG
gzip sheets reproduce byte-for-byte independently and were visually inspected.
The fortress pieces show towers, stairs and bridges; the standalone fortress
templates show a courtyard and a roofed building. Basalt chambers share a chamber
and passage vocabulary. Bastions include low buildings and a tower compound.
Canonical decisions follow separately and are not established by names alone.

The existing pool trace preserves the missing minecraft:basalt_chambers/chambers
reference. These views neither repair that reference nor prove successful assembly.
Source contents and placement inputs must accompany the projections.

The renderer independently rescales templates, uses full cubes for partial blocks,
and omits fully occluded cells. Opaque surfaces hide interiors. Bottom geometry
approaches or crosses the basalt, temple and bastion sheet boundaries; preserved
NBT supplies full dimensions. These views do not prove effective world placement,
assembled geometry, exposure, machinery operation or discovery distance. Green
is only a plant-name hint.

```sh
uv run -m tools.view_item8_betterend_ruins --adora-nether --output evidence/item-8/sources/adora-nether-views
uv run -m tools.view_item8_betterend_ruins --adora-nether --output evidence/raw/item8/adora-nether-views-r1
uv run ruff check tools/view_item8_betterend_ruins.py
uv run basedpyright tools/view_item8_betterend_ruins.py
```

Use fresh output directories and compare the four SVG gzip files before adding
this README. PNGs are scratch inspection views.

| File | SHA-256 |
| --- | --- |
| basalt_chambers.svg.gz | b27f6b13901ae43cac01580a366284d9baf0974899559f043f740ae9d791373b |
| bastions.svg.gz | 215398b3b090ed44f8071305b793043b0fa88933893838c2899a2162159dd4a5 |
| fortress_parts.svg.gz | 6aaca282864926c55d24d231f83b509934319d0632fad9f74e3855a3453823a1 |
| fortresses_temples.svg.gz | cba4d724c8ed6f1a981f09d5776ed135f16c4a95a8a24484862af4c66a4bdfe7 |
