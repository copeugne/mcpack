# Explorations provider entry boundaries

Selector b454032 captures the complete 33-class archive. The existing scarecrow,
Slime Cave and deepslate interpretations remain in their earlier source records;
this pass resolves the remaining provider entries and component consumers.
The independent capture reproduced exactly before this README was added.
Archive SHA-256: 420d0373711877a5e1a86b7f9b4f54848f3debb2f116c2509a5cc4eb496c979e.
Identity manifest SHA-256:
7889daf6336c190cec169bc57eac369ebf863eb4c72e2b7895341aa12b4e9b8f.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive explorations-neoforge-1.21.1-1.6.2.jar \
  --output evidence/raw/item8/explorations-provider-r1
```

NeoforgeExplorations loads ModRegistry and attaches ServerAboutToStartEvent.
The callback loads and verifies configuration, then calls addStatuesToVillages.
The two service implementations provide DeferredRegister registration and platform
access. The declared mixins expose pool entries and tree-decorator registration.

ModRegistry registers the scarecrow feature, underground-temple and slime-cave
structure types, slime-cave piece, lantern and cave-vine decorators, and deepslate,
stone-brick-aging and wool-replacement processors. The temple uses its configured
start pool and JigsawPlacement. The Slime Cave's single template and marker
behavior were already resolved; neither type is an additional family merely
because it has a custom codec. The processors transform existing piece blocks.

WorldGenHelper reads the configured village/statue lists, resolves each target
pool and constructs legacy single elements with the empty processor list and
RIGID projection. It updates both expanded and raw weighted lists. A missing
compatible pool causes that addition to return without mutation. Frozen statue
entries target plains, savanna, snowy and taiga village houses pools, with four
statues in each. These are components of consuming villages, not four new roots.

LanternDecorator chooses positions below leaf blocks and writes chains and
lanterns. The packaged large_mushroom tree uses this decorator. Its leaf-position
shuffle uses Collections.shuffle without the generation RandomSource argument;
do not claim deterministic decoration from this source or repair it here.
CaveVineDecorator supplies hanging vegetation to a consuming tree; no packaged
configured feature in this archive uses it. Keep any external consumer separate.

The source capture supports provider reconciliation, not observed placement,
successful block writes or final family attributes. Preserve the underground
temple's missing references and the named mushroom/decoration grouping question
in provider-scope.md rather than silently modifying the frozen content.

## Five standalone family descriptions

After d4cc7261, Desert Ruin, Floating Island, Forgotten Well, Logs and Shrine
had 48 missing explicit descriptions. Shrine's two existing geometry answers
are retained unchanged. This batch integrates those 48 answers using existing
source artifacts; no new capture, measurement or tooling is introduced.

Direct inspection of the complete pool traces and template catalog establishes
thirteen standalone templates, no attachments, no authored entities, physical
spawner NBT, generation markers or missing graph resources:

| Family | Template alternatives | Stored XYZ sizes |
| --- | ---: | --- |
| desert_ruin | 8 | 6x7x7, 6x5x7, 6x5x7, 6x6x7, 6x5x7, 6x5x7, 6x3x7, 6x6x7 |
| floating_island | 1 | 11x14x9 |
| forgotten_well | 1 | 5x6x5 |
| logs | 2 | small 5x4x5; large 5x4x8 |
| shrine | 1 | 9x8x9 |

The desert rows correspond to ruins/desert_1 through desert_8; the other template
IDs are retained directly in each inventory entry. Absence of jigsaw blocks
makes these template envelopes adequate nominal assembly dimensions, including
air/padding. Rotation may exchange X/Z. They are not occupied-world or exposed
height measurements.

The five root definitions under data/explorations/worldgen/structure use vanilla
jigsaw, depth one, WORLD_SURFACE_WG and empty spawn_overrides. Start offsets are
0/60/1/0/0 in table order. Floating Island has no terrain adaptation, Shrine has
beard_box, and the others have beard_thin. Resolved biome sets contain 1/12/41/56/56
biomes, all intersecting only the Overworld runtime possible-biome set. Existing
world observation links remain unchanged.

Desert Ruin, Floating Island and Shrine reference their same-named
explorations:chests tables. Well and Logs have no saved container table references;
that does not imply absence of block salvage. Floating Island uses randomize_stone:
eight ordered 0.05 random stone-match rules yield coal, iron, copper, redstone,
lapis, gold, diamond or emerald ore. These are individual rule inputs, not eight
independent observed 5% yields. Shrine uses randomize_stonebrick, whose captured
StoneBrickAgingProcessor changes stone-brick/masonry states to aged variants.
The other pools use minecraft:empty processors. No processor here adds spawners.

Qualitative discovery descriptions follow the small surface ruins, well, low
logs, shrine and elevated island forms. No viewing distance or safety guarantee
is inferred. Empty authored enemy sources leave conditional natural spawning;
Floating Island also presents access and fall hazards through its elevation.

Seven provider/inventory tests and scoped builder quality checks pass. Only
these five rows and input identity changed; prior Shrine geometry, biomes,
world observations and nonregistry content are unchanged. Inventory matches
`evidence/raw/item8/inventory-explorations-standalone.json`, SHA-256
3ee3f9bef8a1f391f8336285d67e91714234143defb373e9b0cfa4164084ef39.

## Large Oak Tree and Slime Cave completion

After d0693aaa, this batch integrates fourteen descriptions: ten for the tree
and four for the cave. Slime Cave's six earlier entity, marker, loot and placement
answers remain unchanged. No capture, runtime experiment or tool was added.
The earlier cave processor gap is already resolved in explorations-deepslate;
do not reopen it from the dated wording in the original cave capture README.

Existing inventory joins expose full-start-chunk world-bounds observations:
tree footprint 14x15 or 15x14 and height 12; cave footprint 15x15 and height 12.
These values and their exact observation indexes are integrated into the explicit
family attributes, bound to the existing world-bounds artifact hash. They remain
saved piece envelopes with padding, not occupied volume or family-wide extrema.
Tree observations 148,165,169,170 record the mountainous-seed run-a examples;
545,562,566,567 retain their run-b counterparts. Repeated runs are not independent
layout samples. Existing cave observation indexes and all source limitations
remain attached without inventing a frequency denominator.

Tree base is 6x4x5 with a connector to the 15x8x14 top; this confirms why one
component alone would not describe its assembled size. Both pools use vanilla
rigid single elements with minecraft:empty processors. Templates contain only
their jigsaw block entities, with no authored entities, loot references, spawners
or generation markers. The surface-projected tree is an environmental feature;
ordinary biome spawning and ordinary block drops remain separate possibilities.

Both families' resolved biome sets intersect only the Overworld runtime possible
biomes, consistent with the retained saved starts. Tree uses WORLD_SURFACE_WG,
offset zero and beard_thin. The cave's captured generator rejects sea level <=30
or a height span below ten, then selects its below-sea-level start and one rotated
piece. DeepslateProcessor changes stone/mossy cobblestone below Y0 without changing
the envelope or erasing marker/chest metadata. The cave may be exposed by natural
terrain, but neither exposure rate nor a guaranteed surface landmark is claimed.

Eight affected tests in the provider, slime-cave-source and inventory-source
suites pass, along with scoped builder quality checks. Only these two families
and the decisions input hash changed; existing cave source answers, biome and
observation links, and nonregistry content remain unchanged. Inventory matches
`evidence/raw/item8/inventory-explorations-tree-cave.json`, SHA-256
4dc15e0a4513ab56f5794cd7e872131d20d4f29f40e2d1dab0d83f7740920d86.

## Remaining assembly source assessments

After 00cda891, Campsite, Jungle Temple and Underground Temple had thirty
unintegrated descriptions. Twenty-six now have explicit answers: eight each
for Campsite and Jungle Temple, and all ten for Underground Temple. Footprint
and height remain open for the first two. No new capture, measurement or tool.

All three resolved biome sets intersect only Overworld runtime possible biomes.
Campsite and Jungle Temple are vanilla jigsaw roots, WORLD_SURFACE_WG offset zero,
depth three, with empty spawn_overrides and beard_thin/beard_box respectively.
Their complete graphs have no authored entities, physical spawners or generation
markers. The pen template is not evidence of authored animals. Campsite tents
reference explorations:chests/campsite/tent; their wool_replacing processor changes
wool state and retains position/NBT, leaving non-wool unchanged. Other components
use empty processors. Jungle Temple's empty-processor elements preserve main
chest/dispenser table references and the outside-stairs chest alternative.
Dispenser_main contains arrow and slowness/weakness tipped-arrow inputs, supporting
hazard intent without claiming successful trap firing.

UndergroundTempleStructure.generateStartPos rejects sea level <=30 and a computed
height span below ten, then chooses chunk-middle X/Z and
Y=minY+15+nextInt(abs(seaLevel-15-(minY+15))). Its parent JigsawStructure delegates
to JigsawPlacement. The underground step and start algorithm establish placement
intent, not guaranteed burial of all connected pieces. Existing saved full-start
bounds are integrated with exact observation indexes. Minimal 2x2x2 layouts at
indexes 51,255,267 and repeat-run counterparts 454,644,656 remain included;
they are not described as typical complete dungeons. Other retained envelopes
are not family-wide extrema. No independent-sample or pacing claim.

Known missing templates remain explicit:
explorations:underground_temple/intrusions/corner and
explorations:underground_temple/rooms/small_hall_down. Their intended contents
are not fabricated. Available rooms/walkways retain legacy mob_spawner NBT for
cave_spider, skeleton, spider, witch and zombie. The root separately specifies
piece-bounds illusioner/pillager/vindicator natural spawning, each weight 100,
group inputs 4..9. Armor stand is decorative, not an enemy. Table references and
exact owners cover barrel, bedrooms, dead_end, dispenser, dungeon, enchanting,
large_room, library and quest_tower under explorations:chests/underground_temple.
The dispenser source includes arrow inputs; masonry-aging processors do not
establish loot rolls or population. Missing graph branches retain their source
failure disposition despite observed partial/successful layouts.

Seven affected provider/inventory tests and builder quality checks pass. Only
these three families and the input identity changed; biome/observation links and
nonregistry content remain unchanged. Inventory matches
`evidence/raw/item8/inventory-explorations-assemblies.json`, SHA-256
ec0ab5295d23c674f933300468b5c68d5562eefc29a234b46c2226092f8627ea.

## Final two geometry assessments

Four remaining answers concern Campsite and Jungle Temple. Jungle Temple can be
derived directly from the retained templates, avoiding a runtime measurement.
Main is 17x18x17 with outward connectors at [0,1,8], [8,1,0], [8,1,16] and
[16,1,8]. All three exterior-stair alternatives are 7x6x6 with inward connector
[3,1,0], empty downstream pool, rigid projection and empty processors. Adjacent
connector placement adds six blocks outside each attached side, at unchanged Y.
With all four sides attached, the source envelope is 29x18x29. Stairs remain
below the main roof and do not intersect each other. This is a fully attached
nominal layout, including air/padding, not proof of attachment success everywhere.

Campsite has two 7x3x7 bases and eight competing horizontal attachment positions.
Six child alternatives have different lengths/widths and can collide; largest
component sizes alone are not an observed assembly. A single ordinary-seed target
uses the existing gap runtime for its footprint/height example. No new simulator,
probe or tool is introduced. Runtime source: 22c81eb4f5c83cddaf6ae103aea05d46ddd60920.

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
  --target instances/item8/explorations-campsite-r1 \
  --log-path evidence/raw/item8/explorations-campsite-r1/console.log \
  --captured-config evidence/raw/item8/explorations-campsite-r1/configuration \
  --receipt evidence/raw/item8/explorations-campsite-r1/run.json \
  --timeout-seconds 900 --structure explorations:campsite
```

### Campsite runtime result and custody

The ordinary-seed target [288,-1616] completed, followed by correlated save,
clean exit and passing configuration capture. Committed receipt:
`evidence/item-8/runtime/explorations-campsite-r1/run.json`. Existing locked world
copying excludes session.lock; original instance and capture remain preserved.
The decoder produced 1,802 records including surrounding and locate-created
partial chunks, not a completed sampling denominator. Decoded line 770 is the
full Campsite start at chunk [18,-101], with seven pieces and inclusive envelope
[283,65,-1629,301,69,-1611]. Max-minus-min-plus-one gives 19x5x19 XYZ, using the
existing observed_bounds derivation. It is one example with padding, not occupied
volume or family-wide extrema. Decoded chunks.jsonl SHA-256:
66e1a6c364bf52eae599f8c9a66ee6f276a0451ba3332f6c3450e88b8f0f5301.

```sh
uv run python -c 'from pathlib import Path; from tools.stage_item7_world import copy_world_boundary; copy_world_boundary(Path("instances/item8/explorations-campsite-r1"), Path("evidence/raw/item8/explorations-campsite-r1/world"))'
uv run -m tools.decode_item7_world evidence/raw/item8/explorations-campsite-r1/world --output evidence/raw/item8/explorations-campsite-r1/chunks.jsonl
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/explorations-campsite-r1 --archive evidence/raw/item8/item8-explorations-campsite-r1-22c81eb4.tar.gz --manifest evidence/item-8/raw-custody/explorations-campsite-r1-manifest.json --revision 22c81eb4f5c83cddaf6ae103aea05d46ddd60920
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/item8-explorations-campsite-r1-22c81eb4.tar.gz --manifest evidence/item-8/raw-custody/explorations-campsite-r1-manifest.json --target evidence/raw/item8/explorations-campsite-r1-restored --receipt evidence/item-8/raw-custody/explorations-campsite-r1-local-restore.json
```

Archive: 2,834,850 bytes, 249 files, 20,477,930 uncompressed bytes. SHA-256:
3a3222648745f3228e2809c5aa81529a5c9bfd05dc878c17b287b3fbd5cf1cb6.
It retains world boundary, decoded chunks, logs, run receipt and configuration,
without server binaries. Local copies share a disk; the published GitHub asset
is the separate durable copy. Local and downloaded restores verify all 249 files.
Use absent archive/restore destinations for reproduction.

[Published archive](https://github.com/copeugne/mcpack/releases/tag/item-8-explorations-campsite-2026-09-07-r1).

```sh
gh release download item-8-explorations-campsite-2026-09-07-r1 --dir evidence/raw/item8/explorations-campsite-download --pattern item8-explorations-campsite-r1-22c81eb4.tar.gz
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/explorations-campsite-download/item8-explorations-campsite-r1-22c81eb4.tar.gz --manifest evidence/item-8/raw-custody/explorations-campsite-r1-manifest.json --target evidence/raw/item8/explorations-campsite-downloaded-restore --receipt evidence/item-8/raw-custody/explorations-campsite-r1-downloaded-restore.json
```

All four geometry answers are integrated. Seven affected tests and scoped builder
checks pass. Only Campsite/Jungle Temple geometry and evidence references changed;
prior source answers, biome/observation links and nonregistry content are unchanged.
Inventory matches `evidence/raw/item8/inventory-explorations-final-geometry.json`,
SHA-256 3f3955752c7796c666df1bee7a7188cc6f9ad286d976d381c90ddb11ef31295e.
All ten Explorations family descriptions are now assessed.
