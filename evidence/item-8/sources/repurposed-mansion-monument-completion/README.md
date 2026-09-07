# Repurposed mansion and monument completion

## Quantified remaining work and capture declaration

After 8e4400bb these two families have seven unresolved entries, not five.
Both existing approximate_vertical_size attributes contain UNKNOWN values and
must remain counted as open. Across Item 8 that corrects 474 remaining entries
to 476. Their foundation limitations are valid but do not resolve height.

Three descriptive entries can use existing source evidence: mansion visibility,
monument visibility and monument placement. Four size entries need representative
assembled observations. Neither the main world-bounds catalog nor the additional
original Item 8 chunks.jsonl captures contains a start for either family's roots.

Predeclare one fresh ordinary seed42 Overworld run targeting, in order,
repurposed_structures:mansion_oak and repurposed_structures:monument_desert.
Request81 chunks around each located target through the existing gap runner.
Require readiness, both matching completions, correlated save-all flush, clean
exit and frozen configuration acceptance. Preserve failures and raw warnings.
Accept saved envelopes only after archive, local restore, remote delivery and
fresh downloaded restore. One example per family is not all-variant extrema,
occupied volume or total foundation extent. No new measurement tool is required.

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
  --target instances/item8/repurposed-mansion-monument-geometry-r1 \
  --log-path evidence/raw/item8/repurposed-mansion-monument-geometry-r1/console.log \
  --captured-config evidence/raw/item8/repurposed-mansion-monument-geometry-r1/configuration \
  --receipt evidence/raw/item8/repurposed-mansion-monument-geometry-r1/run.json \
  --timeout-seconds 900 \
  --structure repurposed_structures:mansion_oak \
  --structure repurposed_structures:monument_desert
```

## Descriptive assessment

The existing repurposed-mansion, repurposed-mansion-bindings and
repurposed-mansion-layout evidence establishes the room/wall/roof/entrance assembly
and surface anchor. These support a qualitative large surface-building visual cue;
terrain, vegetation and biome/material variants prevent a guaranteed sightline.
Foundation support length is not a visible-building height.

The existing repurposed-monument report documents the placement algorithm, and
repurposed-monument-rooms binds the body, entrance and room components. Selected
root JSON under data/repurposed_structures/worldgen/structure/monument_*.json sets
center_terrain_height_weight to1.5 desert,1.4 icy and1.25 jungle, all with terrain
adaptation none. The Nether variant instead fixes Y30 with beard_box adaptation.
For nonfixed variants the entry takes C as central WORLD_SURFACE_WG height minus1,
M as the minimum of C and four diagonal samples at offsets +/-29, minus1, then
anchors at C+Java-int((M-C)/weight). This is terrain-rooted placement intent, not
measured exposure of every room. Fixed Nether altitude may be enclosed or exposed;
its strongholds generation step does not prove a particular burial depth.

These facts resolve three descriptive entries in the two authoritative family
records. The four size entries remain open pending accepted capture geometry.


## Geometry acceptance

Both targets passed readiness, matching81-chunk completion, correlated flush,
clean exit0 and frozen configuration acceptance. Normalized comment changes remain
in run.json. Decode produced2764 records, including surrounding generation stages.
One-based chunks.jsonl line1443 is full mansion_oak chunk967,1060:644 pieces,
envelope[15461,141,16957,15521,171,17035],size61x31x79. Line1924 is full
monument_desert chunk218,-2331:74 pieces,envelope[3467,65,-37317,3524,86,-37260],
size58x22x58. These saved examples exclude foundation extensions outside piece
bounds and do not establish typical sizes, every variant or complete population.

The raw invalid-item loading error (minecraft:air), warnings and logs are retained.
It does not invalidate saved structure boxes, but this run cannot establish loot
loading correctness. No baseline repair or broader compatibility claim is made.

Archive item8-repurposed-mansion-monument-geometry-r1-57addac8.tar.gz has264 files,
5,428,486 compressed bytes and32,256,742 uncompressed bytes. SHA-256:
3bf2fc5cfc5877d3aec7bdc26ac6d92fb6833afefa83710b1db45105b05dbcfc.
Decoded chunks SHA-256:
5aed2b83ab09955fe6f396d5452f934cadd68fb7c3cf7fb95934b5640380f155.
Both local and fresh downloaded restores verify264 files; downloaded line1443
and1924 reproduce the respective full start and bounds through existing
observed_bounds. Release/tag item-8-repurposed-mansion-monument-geometry-2026-09-07-r1
is verified at declaration57addac85bd8a7ef3df29ac158ba9ca55a7d5fe0. Local copies
share a disk; GitHub is separate storage. Three custody records under
raw-custody/repurposed-mansion-monument-geometry-r1-* are bound in both families.

The four size entries now supersede UNKNOWN values while preserving foundation
limitations. Three descriptive entries and observed Overworld dimensions are
integrated. This completes these two family assessments, not Item8 delivery.

Reproduction with unused destinations:

```sh
uv run python -c 'from pathlib import Path; from tools.stage_item7_world import copy_world_boundary; copy_world_boundary(Path("instances/item8/repurposed-mansion-monument-geometry-r1"), Path("evidence/raw/item8/repurposed-mansion-monument-geometry-r1/world"))'
uv run -m tools.decode_item7_world evidence/raw/item8/repurposed-mansion-monument-geometry-r1/world --output evidence/raw/item8/repurposed-mansion-monument-geometry-r1/chunks.jsonl
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/repurposed-mansion-monument-geometry-r1 --archive evidence/raw/item8/item8-repurposed-mansion-monument-geometry-r1-57addac8.tar.gz --manifest evidence/item-8/raw-custody/repurposed-mansion-monument-geometry-r1-manifest.json --revision 57addac85bd8a7ef3df29ac158ba9ca55a7d5fe0
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/item8-repurposed-mansion-monument-geometry-r1-57addac8.tar.gz --manifest evidence/item-8/raw-custody/repurposed-mansion-monument-geometry-r1-manifest.json --target evidence/raw/item8/repurposed-mansion-monument-geometry-r1-restored --receipt evidence/item-8/raw-custody/repurposed-mansion-monument-geometry-r1-local-restore.json
gh release download item-8-repurposed-mansion-monument-geometry-2026-09-07-r1 --repo copeugne/mcpack --pattern item8-repurposed-mansion-monument-geometry-r1-57addac8.tar.gz --dir evidence/raw/item8/repurposed-mansion-monument-geometry-r1-download
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/repurposed-mansion-monument-geometry-r1-download/item8-repurposed-mansion-monument-geometry-r1-57addac8.tar.gz --manifest evidence/item-8/raw-custody/repurposed-mansion-monument-geometry-r1-manifest.json --target evidence/raw/item8/repurposed-mansion-monument-geometry-r1-downloaded-restore --receipt evidence/item-8/raw-custody/repurposed-mansion-monument-geometry-r1-downloaded-restore.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-mansion-monument-completion-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

For each downloaded one-based line1443 and1924, apply
`observed_bounds(ChunkRecord.model_validate_json(line))` from the existing
mcpack_evidence.item8_world_bounds and item7_nbt_models modules. Require the
matching structure_id and chunk_full=true. The documented envelopes and sizes
are inclusive saved bounds, not a new measurement algorithm.
