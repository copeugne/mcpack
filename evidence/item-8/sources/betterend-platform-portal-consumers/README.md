# BetterEnd platform and portal consumers

Selector d14f2ea captures four classes. The independent r1 capture reproduces all
files byte for byte. Manifest SHA-256:
816d2f16a1da5e6778d7d4f1f5a00104444dc94403d430c752c141926b0f8f0c.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BetterEnd-21.0.31.jar --class-name org/betterx/betterend/world/generator/TerrainGenerator.class --class-name org/betterx/betterend/world/generator/GeneratorOptions.class --class-name org/betterx/betterend/world/features/BiomeIslandFeature.class --class-name org/betterx/betterend/world/structures/features/EternalPortalStructure.class --output evidence/raw/item8/betterend-platform-portal-consumers-r1
```

TerrainGenerator.makeObsidianPlatform cancels vanilla creation when
GeneratorOptions.generateObsidianPlatform is false. When that option is true and
changeSpawn is false it returns without changing the platform. When both are
true, it clears space and writes the platform at the configured spawn position,
then cancels vanilla creation. This is relocation/suppression of the existing
spawn platform, not an additional independent template design. Other methods in
TerrainGenerator implement terrain sampling, density and noise filling.

GeneratorOptions.init copies typed values from GeneratorConfig into static fields
and its getters return those fields. GeneratorConfig remains the exact key-to-
field binding to reconcile before claiming the frozen branch selection. Do not
infer that mapping solely from matching field names.

BiomeIslandFeature fills a terrain island through a capped-cone SDF, displacement,
world-seeded noise and surface materials. It does not request a building template,
loot table or authored encounter. Its `overworld_island` registry name does not
prove dimension placement. Treat it as terrain support, retaining activation and
shared SDF consumers in their existing scope rows.

EternalPortalStructure binds only portal/eternal_portal. Its static initializer
loads that template through EndStructureHelper. The custom generation stub checks
biome validity and uses an NBTPiece with this same template. Constructor config
and generatePieces use different offsets; do not turn this candidate-scope read
into an unverified assembled-size claim. The corresponding packaged root already
uses type betterend:eternal_portal. The template is a component of that existing
root, not a fourth independent portal family.
