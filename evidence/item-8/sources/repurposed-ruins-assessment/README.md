# Repurposed ruins descriptive assessment

Seven required entries are integrated. Approximate footprint and vertical size
remain open: the existing catalog has no full-start envelope. No new capture or
measurement tool is introduced in this descriptive increment.

## Direct evidence

Five roots under data/repurposed_structures/worldgen/structure/ cover land_cold,
land_hot, land_icy, land_warm and nether ruins. Pool-traces-content resolves13
possible templates for each land root and5 for Nether,57 total, with no missing
components. Only cold/warm small_brick_7 author minecraft:item entities. These are
not mobs. No generation markers, spawner blocks or unresolved entities occur.
All root spawn overrides are empty, leaving natural biome spawning possible.

Inspect the selected processor lists under
 data/repurposed_structures/worldgen/processor_list/ruins/.
Land lists each contain material rules and one capped archaeology rule. Cold,
icy and warm convert matching grass blocks to suspicious gravel; hot uses a0.25
random sand match and suspicious sand. Each caps modifications at5 and appends
repurposed_structures:archaeology/ruins_land_{cold,hot,icy,warm}. These are processor
caps, not per-family reward quantities. They supplement nine literal chest tables:
large/small for each land variant and one Nether table. All13 table definitions
exist under the same namespace's loot_table directory. Exact template/table
mappings and archaeology identifiers are retained in the authoritative attributes.

Nether randomization has material rules and11 pillar processors, including duplicate
orange and brown trigger entries as packaged. Pillars extend down with length5;
colored-glass triggers become netherrack, blackstone variants or planks. Referenced
self-lists process replacement material, which no longer matches colored-glass
pillar triggers. The existing PillarProcessor source in repurposed-monument-processors
preserves trigger matching, terrain/build guards, child processing and direct block
writes. No selected processor adds a mob, ordinary/trial spawner or infested block.
Magma output in Nether rules and powder snow in icy rules are environmental hazards.

Land roots project WORLD_SURFACE_WG with offset0, beard_thin, terrain-radius1 and
allowed terrain range8; liquids are prohibited. Nether root uses the already
captured GenericNetherJigsawStructure LOWEST_LAND search with ledge offset-1 and
start offset-2. These are terrain-placement inputs, not guaranteed open-sky exposure
or measured burial. Pillar length is not an occupied-height measurement.

Fragmentary building/masonry form supports qualitative visibility descriptions,
with terrain and vegetation occlusion possible. Loot-bearing ruins and land
archaeology do not establish an authored combat population. No sightline, density,
reward-rate or safe-area claim is added.

The family binds packaged catalogs and existing assembly/processor manifests.
The57 templates remain pieces and alternatives of one family. Two geometry entries
still need adequate evidence, and Item8 remains open.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-ruins-content-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only this family and input identity may change. Descriptions
are source-derived; focused checks validate existing evidence/integration boundaries.

## Geometry capture declaration

After262fc206, additional original Item8 chunks.jsonl captures were inspected and
contain no ruins-family starts. The main catalog has no full-start envelope.
Predeclare one fresh seed42 Overworld target repurposed_structures:ruins_land_warm,
81 requested chunks, using the existing gap runner. Require readiness, matching
completion, correlated flush, clean exit and frozen config acceptance, then archive,
local restore, remote delivery and downloaded restore before accepting geometry.
This is one assembled example for two size entries, not every variant or occupied
pillar extent. No new tooling or baseline tuning is needed.

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
  --target instances/item8/repurposed-ruins-geometry-r1 \
  --log-path evidence/raw/item8/repurposed-ruins-geometry-r1/console.log \
  --captured-config evidence/raw/item8/repurposed-ruins-geometry-r1/configuration \
  --receipt evidence/raw/item8/repurposed-ruins-geometry-r1/run.json \
  --timeout-seconds 900 --structure repurposed_structures:ruins_land_warm
```
