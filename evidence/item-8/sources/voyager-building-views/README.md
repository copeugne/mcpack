# Voyager building comparisons

Renderer f35c3b1b selects 23 architecture templates from the hash-verified retained
MoogsVoyagerStructures-1.21-5.0.11.jar archive, covering seventeen pending house,
outbuilding and tower decisions. Shared vanilla villager templates remain in the
existing component graph. All four sheets were manually inspected and independently
reproduced byte for byte. The selected-path pilot and scoped Ruff/Basedpyright pass.

```sh
uv run -m tools.view_item8_betterend_ruins --voyager-buildings --output evidence/raw/item8/voyager-building-views-r1
```

The existing cube projection omits occluded cells and rescales each template
independently. These are individual pieces, not assembled buildings. Partial block
models, hidden rooms and generated-world placement are not rendered. Wide tower
panels approach adjacent labels, and bottom-row house bases approach the sheet
edge. Use template names and the preserved graph for attribution. Floating small
blocks and thin lower pieces remain part of the raw templates. Screen size is not
a dimension measurement, and shared villager pieces do not establish family identity.

Compressed SHA-256 identities:

- houses.svg.gz: a68584f4b24843dd737c9c1382dfa42fa5b8c615c0aaaff5047215027634c2d2
- nether_towers.svg.gz: f6a7fe318791e114ff98daf8dc6f90e58f57ef43e6ed13a438d4dd410c8bbfc3
- outbuildings.svg.gz: 91b5fa5e60774580ad5a8d7178d8c0ed90a120c1fd9634711ab4cb97d4d5441f
- towers.svg.gz: a4b8869c67f916d779fe3e4cdfdf6f4f32fb406b8477fcd635954a2efbe2ce95
