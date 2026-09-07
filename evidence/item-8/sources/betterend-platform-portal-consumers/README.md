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


## Village geometry capture declaration

Two required claims remain: assembled village footprint and height. The retained
pool/template data describes components and size6/distance80 placement inputs,
not an observed assembly. There is no retained full-start village observation.
A single ordinary-seed42 End target using the existing81-chunk gap protocol is
the smallest direct assembled example. Do not infer a population range, occupied
volume, full realization of every component or repeatability from that example.

The existing runner was hard-coded to Overworld locate, Chunky completion and
configuration paths. It now accepts the End explicitly through those same paths;
Overworld remains its default. This fixes the concrete inability to target this
End-only family without a new runner, schema version or capture framework. Focused
lifecycle/configuration tests pass (17 tests), including both dimension command
sequences and rejecting the other dimension's completion marker. Scoped Ruff and
Basedpyright pass. The actual End run below remains necessary to validate its
runtime behavior and supply the missing geometry evidence.

Require fresh frozen materialization, readiness, a matching81-chunk End completion,
correlated save flush, clean stop, frozen configuration acceptance and stopped-world
decoding. Preserve missing templates and all other warnings. Use the existing
archive/restore/release workflow before accepting dimensions. No baseline repair.

```sh
uv run -m tools.run_item7_gap_targets \
  --pristine instances/pristine-baseline-v0 \
  --artifact-manifest evidence/item-3/artifact-acquisition-manifest.json \
  --retained-manifest evidence/item-3/runtime/retained-server-candidates.txt \
  --seed-suite test-environment/seed-suite.json \
  --frozen-config evidence/item-6/frozen \
  --frozen-manifest evidence/item-6/generated-config-manifest.json \
  --config-audit evidence/item-6/config-audit.json \
  --java-home downloads/item2/temurin/extracted/jdk-21.0.12.1+1 \
  --target instances/item8/betterend-village-geometry-r1 \
  --log-path evidence/raw/item8/betterend-village-geometry-r1/console.log \
  --captured-config evidence/raw/item8/betterend-village-geometry-r1/configuration \
  --receipt evidence/raw/item8/betterend-village-geometry-r1/run.json \
  --timeout-seconds 900 --dimension minecraft:the_end --structure betterend:end_village
```


## Village geometry acceptance

The declared seed42 End target passed readiness,81 requested chunks, correlated
save flush, clean exit0 and frozen configuration acceptance. Allowed comment-only
normalization differences remain in run.json. The stopped world decoded1802 chunk
records; this is retained coverage, not the requested sampling denominator.

Full start chunk34,-316 is chunks.jsonl line478, with45 pieces and envelope
[482,56,-5139,581,76,-5034], giving100x21x106 blocks by inclusive subtraction.
Both required dimensions now use this assembled example. It includes air/padding,
not occupied volume, a typical size, all-layout extrema or proof that every
component chunk's population was completed. Terrain adaptation and feature writes
may differ from saved bounds. Existing missing work_01/stree_terminator_01 inputs
remain disclosed; no repair or general compatibility acceptance is implied.
Raw logs preserve existing optional/integration warnings, including nonexistent
Integrated Villages villager_random pools and multiple-Overworld Biolith warnings.

Archive item8-betterend-village-geometry-r1-f2f5b2b6.tar.gz contains247 files,
1,873,483 compressed bytes and18,313,798 uncompressed bytes. Archive SHA-256:
ed725ed290e01baee8d29ad4d180ee11ef03642fe20f563e21e7aa5c19235813.
Manifest SHA-256: cbc316bc5cf6cc3a2d026840f24d0b72e23cac1b5e98110061576497f65c39f9.
Decoded chunks SHA-256: 22fc7e6b0ee458864eceab8d6c0d999a08d39c297c3a0c6bac6b5e92a2b1d2fb.
Release/tag item-8-betterend-village-geometry-2026-09-07-r1 points to source revision
f2f5b2b64513e3d2acfd14f5df2ddbf56602fc8c, verified remotely. Both local and fresh
GitHub-download restores verified all247 files. observed_bounds on downloaded
line478 reproduced the full start,45 pieces and100x21x106 envelope. Local copies
share a filesystem; the GitHub release is separate durable storage.

Reproduce with fresh output paths using the existing tools:

```sh
uv run python -c 'from pathlib import Path; from tools.stage_item7_world import copy_world_boundary; copy_world_boundary(Path("instances/item8/betterend-village-geometry-r1"), Path("evidence/raw/item8/betterend-village-geometry-r1/world"))'
uv run -m tools.decode_item7_world evidence/raw/item8/betterend-village-geometry-r1/world --output evidence/raw/item8/betterend-village-geometry-r1/chunks.jsonl
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/betterend-village-geometry-r1 --archive evidence/raw/item8/item8-betterend-village-geometry-r1-f2f5b2b6.tar.gz --manifest evidence/item-8/raw-custody/betterend-village-geometry-r1-manifest.json --revision f2f5b2b64513e3d2acfd14f5df2ddbf56602fc8c
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/item8-betterend-village-geometry-r1-f2f5b2b6.tar.gz --manifest evidence/item-8/raw-custody/betterend-village-geometry-r1-manifest.json --target evidence/raw/item8/betterend-village-geometry-r1-restored --receipt evidence/item-8/raw-custody/betterend-village-geometry-r1-local-restore.json
gh release download item-8-betterend-village-geometry-2026-09-07-r1 --repo copeugne/mcpack --pattern item8-betterend-village-geometry-r1-f2f5b2b6.tar.gz --dir evidence/raw/item8/betterend-village-geometry-r1-download
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/betterend-village-geometry-r1-download/item8-betterend-village-geometry-r1-f2f5b2b6.tar.gz --manifest evidence/item-8/raw-custody/betterend-village-geometry-r1-manifest.json --target evidence/raw/item8/betterend-village-geometry-r1-downloaded-restore --receipt evidence/item-8/raw-custody/betterend-village-geometry-r1-downloaded-restore.json
uv run python -c 'from pathlib import Path; from mcpack_evidence.item7_nbt_models import ChunkRecord; from mcpack_evidence.item8_world_bounds import observed_bounds; print(observed_bounds(ChunkRecord.model_validate_json(Path("evidence/raw/item8/betterend-village-geometry-r1-downloaded-restore/chunks.jsonl").read_text().splitlines()[477])))'
```
