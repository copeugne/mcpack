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

## Village and portal assessment

This two-family batch started with18 outstanding attributes. Sixteen are now
integrated: seven village descriptions and all nine remaining portal attributes.
Village assembled footprint and height remain open; no retained full-start
observation exists for either root. Provider discovery is already closed.

Village uses vanilla jigsaw with center_piece, size6, maximum distance80,
WORLD_SURFACE_WG projection, start offset0 and beard_thin terrain adaptation.
These parameters are not an assembled size. The retained trace has41 reachable
templates, no authored entities, no spawners and no structure-block markers.
Missing work_01 and stree_terminator_01 templates remain explicit dispositions.
The street rules replace end-stone bricks/dust according to water/material
predicates and random cracked/weathered/path choices. crying_10_percent changes
obsidian to crying obsidian; the feature component uses vanilla chorus_plant.
These do not author inhabitants or an encounter. Do not infer villagers from
the structure's name. Natural biome spawning remains possible.

Village literal tables are betterend:chests/end_village_bonus_loot,
end_village_loot and end_village_template_loot. All have definitions under
data/betterend/loot_table/chests/ in the preserved packaged catalog. No selected
processor appends another table. These sources do not prove final reward contents
or successful legacy block-entity conversion. Streets/buildings/decorations give
surface discovery cues, not a measured visibility distance.

EternalPortalStructure loads only data/betterend/structure/portal/eternal_portal.nbt,
template SHA-256:
632a67019dff904e0ed940c0d9c009f77ea7f30bae4dcc0982c8303be64da884.
The template is21x12x19, with empty entities and six betterend:pedestal compounds
without Items or LootTable fields. Its palette contains no spawners. Runed
flavolite, stairs, pillars and eternal pedestals are its visible architectural
cues. This does not establish portal activation or a reward.

Direct pinned NBTPiece inspection establishes random rotation/mirror, offsetPos,
template placement without extra processors, then optional erode and cover.
Class SHA-256:
5105bbc0348e13274ebf32fcbe1cd902d36ec4a4fbb77f9327b71b7413f500cb.
The archive identity is recorded in family-decisions processor_inspection.

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/BetterEnd-21.0.31.jar org.betterx.betterend.world.structures.piece.NBTPiece
```

The root rejects invalid biomes, squared chunk radius below1024 and sampled
surface height below5. Its generatePieces uses surface height minus4, erosion
nextInt(5), and cover=true. Constructor config offset-2 is a different input.
Reuse the preserved StructureErode class under crashed-ship-erosion for erode
and cover, not its separate erodeIntense behavior. These paths remove/relocate
block states and apply surface cover, without directly assigning mobs or loot.
Biome-selected cover and block behavior are not asserted as observed population.

Concrete limitation: NBTPiece.postProcess bytecode offset37 calls
boundingBox.maxX for the upper corner's Y coordinate. That malformed box is
passed into template placement and erosion/cover. Preserve it without changing
the frozen baseline; successful full placement and exact affected-world extent
are not claimed. Nominal21x19 footprint (axes may swap) and12-block template
height satisfy approximate architectural description, not surviving occupied
bounds. Existing missing components and this defect remain visible for later
decisions; neither is silently repaired or hidden by Item8 assessment.
