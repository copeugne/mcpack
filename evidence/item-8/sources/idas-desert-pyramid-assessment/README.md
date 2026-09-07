# IDAS desert pyramid content assessment

Seven content/placement attributes resolved from existing immutable artifacts.
The initial content increment left two dimension attributes open; the accepted generated examples below now resolve them.

## mob_source

Intersection1 authors skeletons; rooms1,6 author husks. Entrance3 Create glue and room1 Quark glass frame are non-mob data. No unresolved authored entity compounds in the31 reachable templates. Physical spawners have separate selected sources. Entrance2 connectors21,52 target missing desert_pyramid/desert_pyramid_villager pool; do not substitute the differently named villager pool or claim its disconnected entity as generated.

## loot_table_source

Six defined literal tables under idas:chests/desert_pyramid/: desert_pyramid,desert_pyramid_surface,desert_pyramid_treasure,desert_pyramid_tools,desert_pyramid_library,desert_pyramid_tomb. Existing raw references preserve template ownership. Selected desert_pyramid_processor conditionally appends two additional defined archaeology tables (suspicious_sand_desert_pyramid,suspicious_gravel_desert_pyramid) to matching suspicious blocks using modern append_loot. Room8 selects ticking-only processing, so that append rule does not apply there. References and selection weights do not establish reward yields.

## generated_spawners

Eleven ordinary spawner blocks across reachable source templates, not a per-assembly count because branches can repeat or be omitted. Eight in intersection1(1),library(1),main(2),rooms1,4,5,6(1 each) select husk15,stray10 via desert_pyramid_processor. Three empty raw entity compounds in library31,room4 block13,room5 block4 are replaced. Settings delay20,min200,max800,count4,nearby6,player16,range4,block-light0..7. Room8 uses ticking-only processor and retains three raw sources: husk1,cave_spider2. All eleven raw potential arrays empty. No trial spawners. Entrance1 marker220 and entrance1_bottom marker6 are empty-metadata CORNER markers, not DATA enemy instructions.

## authored_or_natural_enemies

Direct skeletons/husks and processor-selected or retained ordinary spawners are authored hostile sources. Root spawn_overrides is empty, with no family-specific natural override. Environmental spawning remains separate. Missing villager pool does not establish villager generation, and source templates do not determine a realized encounter count.

## intended_hostility

Surface pyramid entrance and branching underground tomb/room network with authored hostile sources and loot. Missing villager-pool connection is a preserved baseline defect. No Item9 tier, measured difficulty or successful full layout is inferred.

## visual_discoverability

The63 by62 horizontal,29-high entrance1 template supplies an above-ground architectural cue, with a separate surface entrance2 component. Those are source component dimensions, not complete family extents. The branching underground network is not visible from its full footprint; actual sightlines and occlusion are unmeasured.

## underground_surface_classification

Surface entrance components lead downward into a branching underground network. Root generic_structure projects WORLD_SURFACE_WG offset0,size28,fixed rotation,center-distance250,allowed_y_range_from_start200,terrain range12/radius1,biome radius1,ignore_waterlogging,enhanced adaptation none. Entrance1 and2 elements separately specify custom beards/carves kernel size/distance18/50 and35/35. All reachable elements rigid. Placement limits are not measured dimensions; missing villager pool and disconnected cave components retain their existing dispositions.

## Source selection and geometry limit

Family evidence binds packaged-json-redacted, templates-redacted and
pool-traces-content catalogs by SHA-256. The default root reaches31 templates.
Hallway pool has eight alternatives (six halls,two stairs), intersection four,
turn four (library,three turns), room nine. Each listed weight is1. Hallway,
intersection and turn fall back to room, whose fallback is empty. Repeated
branching means a list of template extents is not an assembled-size observation.
Existing raw Item8 chunks.jsonl search found no retained desert_pyramid start.
Use the existing frozen geometry-capture workflow for one full-start example;
no new measurement system or representative pacing study is needed for Item8.

All selected elements use desert_pyramid_processor except room8, which uses
waterlogging_fix_processor. Pyramid processor applies probability1 modern
minecraft:append_loot to matching suspicious sand/gravel, then randomizes ordinary
spawners with husk15,stray10. Reuse modern modifier inspection in
../idas-dig-site-assessment/README.md, randomizer/manager inspection in
../integrated-villages-provider/README.md and ticking inspection in
../idas-desert-market-assessment/README.md. Room8 retains its authored spawner NBT.
The empty raw spawner compounds are library/block_entities/31,
room4/block_entities/13,room5/block_entities/4. All source potentials empty.
CORNER markers occur at entrance1/block_entities/220 and
entrance1_bottom/block_entities/6, with empty metadata. No unresolved entity NBT.

Six literal chest tables and both archaeology tables are defined in the packaged
catalog. Preserve exact template ownership from the raw references. Borrowed
contents, disconnected cave templates and the differently named villager pool
are not new families or automatic repairs. Missing villager pool remains a defect.
No baseline tuning, reward experiment or additional tooling added for this assessment.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-desert-pyramid-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only desert_pyramid and input identity may change.
At the initial content checkpoint two size attributes remained open. See the accepted generated examples below for their resolution. Final integration, acceptance and PR/review/main remain open.

## Predeclared final IDAS geometry capture

Two ordinary seed42 targets: idas:desert_pyramid and idas:castle. Existing Pyramid
scans contain no saved start; Castle occurs in explorations-campsite-r1/chunks.jsonl
line501 at chunk10,-110 but is only structure_starts,full=false. Both need full-start
example geometry for their branching layouts. This reuses the existing runner,
81 requested chunks per target, without a new measurement system or pacing claim.
Free space before launch3.1GB; earlier stronghold instance657MB/raw22MB supplies a
comparison, not a guaranteed upper bound. Monitor available space and preserve
failed attempts. Frozen identity, lifecycle and configuration validation remain
mandatory under INFRASTRUCTURE-INSTALLATION-AND-SERVER-TESTING.md.

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
  --target instances/item8/idas-final-geometry-r1 \
  --log-path evidence/raw/item8/idas-final-geometry-r1/console.log \
  --captured-config evidence/raw/item8/idas-final-geometry-r1/configuration \
  --receipt evidence/raw/item8/idas-final-geometry-r1/run.json \
  --timeout-seconds 900 --structure idas:desert_pyramid --structure idas:castle
```

Acceptance requires full start chunks, saved envelopes, clean lifecycle and frozen
configuration acceptance, then archive/restore/durable delivery before accepting
size attributes. A saved envelope is not occupied volume or all-layout bounds.

## Accepted generated examples and custody

The run completed81 requested chunks for each target, readiness, correlated flush
and clean exit0. Frozen configuration validation accepted228 base files with only
the recorded allowed comment-line normalization. No baseline tuning. The stopped
world decoded2765 records; that count is retained coverage, not the requested
denominator. No run Java process remained.

Full Castle start chunk10,-110 is chunks.jsonl line609:61 pieces, envelope
[133,57,-1831,237,114,-1681], inclusive size105x58x151(X,Y,Z).
Full Pyramid start chunk850,1209 is line2255:104 pieces, envelope
[13497,12,19169,13667,92,19376], size171x81x208. These are saved-piece examples
including air/padding, not typical/all-layout bounds, occupied volume, or proof
that every component chunk was fully populated. They resolve the two size
attributes of each family without substituting configured placement limits.

Archive item8-idas-final-geometry-r1-cfe1b06f.tar.gz contains263 files,31354743
uncompressed bytes,4553430 archive bytes. SHA-256
2f8662353b9f6c7d9fd8dcc3844a588712f8e686a93e201b15833e7ef9ea69a6.
Manifest and local/downloaded restore receipts are under evidence/item-8/raw-custody/.
GitHub release item-8-idas-final-geometry-2026-09-07-r1 retains the archive at
runner revision cfe1b06ff1fa06a70036ff2502fe2359897d6e0a. Downloaded restore verified
all263 files; decoding the preserved lines with existing observed_bounds confirmed
both sizes and full status. Raw warnings/errors remain preserved.

```sh
uv run python -c 'from pathlib import Path; from tools.stage_item7_world import copy_world_boundary; copy_world_boundary(Path("instances/item8/idas-final-geometry-r1"), Path("evidence/raw/item8/idas-final-geometry-r1/world"))'
uv run -m tools.decode_item7_world evidence/raw/item8/idas-final-geometry-r1/world --output evidence/raw/item8/idas-final-geometry-r1/chunks.jsonl
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/idas-final-geometry-r1 --archive evidence/raw/item8/item8-idas-final-geometry-r1-cfe1b06f.tar.gz --manifest evidence/item-8/raw-custody/idas-final-geometry-r1-manifest.json --revision cfe1b06ff1fa06a70036ff2502fe2359897d6e0a
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/item8-idas-final-geometry-r1-cfe1b06f.tar.gz --manifest evidence/item-8/raw-custody/idas-final-geometry-r1-manifest.json --target evidence/raw/item8/idas-final-geometry-r1-restored --receipt evidence/item-8/raw-custody/idas-final-geometry-r1-local-restore.json
gh release download item-8-idas-final-geometry-2026-09-07-r1 --repo copeugne/mcpack --pattern item8-idas-final-geometry-r1-cfe1b06f.tar.gz --dir evidence/raw/item8/idas-final-geometry-r1-download
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/idas-final-geometry-r1-download/item8-idas-final-geometry-r1-cfe1b06f.tar.gz --manifest evidence/item-8/raw-custody/idas-final-geometry-r1-manifest.json --target evidence/raw/item8/idas-final-geometry-r1-downloaded-restore --receipt evidence/item-8/raw-custody/idas-final-geometry-r1-downloaded-restore.json
```

Use fresh outputs. Existing ChunkRecord.model_validate_json and observed_bounds
from mcpack_evidence.item7_nbt_models/item8_world_bounds reproduce lines609,2255.
Final integration, acceptance, backup/history and PR/review/main remain open.

Inventory integration command (fresh output path):

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-final-geometry-integration-r1.json
```
