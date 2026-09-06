# Nether paired design views

The existing template renderer at e8fa2b45 selects ten exact templates from the
hash-verified MoogsNetherStructures-1.21-3.0.0-alpha.2.jar archive. Two compressed
sheets cover eight design candidates, including both lower pool components.
Both sheets were manually inspected. Every compressed output reproduces exactly.

```sh
uv run -m tools.view_item8_betterend_ruins --nether --output evidence/raw/item8/nether-pair-views-r1
```

For inspection, decompress a sheet with gzip -dc and convert its SVG to PNG using
the installed ImageMagick converter. This uses the existing projection: partial
block models are cubes, fully occluded cells are omitted, each template rescales
independently, and green is only a block-name hint. Diagrams do not show hidden
interiors, complete assembled placement or observed world dimensions. Join them
to the existing packaged content and full pool graph for membership decisions.
The ten-path pilot succeeded; no new rendering behavior or measurement was added.
Scoped Ruff and Basedpyright pass for the selector change.

Compressed identities:

- pools.svg.gz: ae53730181d5c51cbefa414946802b0b18cbcdf48cf44a91974df1d5aa572efe
- skulls_shrines_towers.svg.gz: d4c7b3d3ca94a80b81e418622a4e958773b93dd44269f03d8b5847dbca61900c
