# Explorify standalone source descriptions

Six families cover 15 roots and 16 standalone templates: badlands_pyramid,
desert_shrine, guide_post, supply_cache, watchtower and mausoleum. Integrated
32 missing descriptions and reconciled 24 existing attribution answers. All
traces and biome resolutions have no missing/unresolved entries. Raw templates
contain no jigsaw block entities; two mausoleums are whole-building alternatives.
Geometry reads template_size_xyz directly, including padding and rotation limits.

Exact root definitions come from packaged-json-redacted.json.gz. Standard jigsaw
surface offsets are pyramid -12..-9, shrine -10..-6, guide post -11 and others 0.
Mausoleum projects to WORLD_SURFACE; others WORLD_SURFACE_WG. No measured burial
or exposed height is inferred. Existing whole-template geometry is retained.

No top-level entity source occurs. Mausoleum supplies legacy zombie-spawner NBT;
other selected templates have no physical-spawner input. All spawn overrides are
empty, which does not suppress biome spawning. Pyramid includes TNT, not tested
trap operation. Exact saved loot references remain attributed to templates.
Guide post processors can change signal_fire or remove a campfire, so a guaranteed
smoke cue is not asserted. Stone/moss/cobweb/candle processors alter material and
presentation, not a measured discovery distance.

## Mausoleum overlay attribution

The existing generic resource selector excludes non-Lithostitched prefixes, so
its root-only processor selection cannot alone describe mausoleum loot. Direct
retained archive inspection establishes an additional source without changing
the selection framework. pack.mcmeta is copied byte-for-byte from
Explorify v1.6.5.mod.jar, archive SHA-256
2dc76398b48b2aae9b4024642da098b0880125572de160cb5ecf91d102890cad.
Metadata SHA-256 is
eb6b11cfa493820b871090a5b58abe2f4f132a56eca77b3218e3df9e3084ed2b.

It declares overlay f15 formats 15..512, covering baseline data format 48.
The retained f15/data/explorify/worldgen/processor_list/mausoleum_processor.json
adds a rule matching potted_dead_bush with probability 0.33, producing decorated_pot
and append_loot explorify:chest/mausoleum_pot. Both mausoleum templates contain
that input block. The exact processor hash and source-declared overlay attribution
are in loot_table_source, separate from saved dungeon loot references. This is
not a runtime pot-yield observation. Metadata capture is necessary to explain why
the root processor is insufficient; no new measurement or generalized tool.

Direct metadata reproduction: use retained_sources(Path.cwd()) to select the
exact named archive, verify its SHA-256 above, and read ZipFile member pack.mcmeta
without transformation. Compare its bytes/hash with the committed file. Processor
and template logic already reside in the retained catalogs with exact identities.
An initial inspection assumed an AdoraBuild-specific variants key; Explorify
instead uses generation_settings/common_generation_definition. The lookup failed
without edits; exact root JSON was then inspected and used for these answers.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-explorify-standalone-descriptions.json
uv run pytest -q tests/item8/test_explorify_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

## Black Spiral assembly

Ten explicit answers complete source assessment: six missing descriptions and
four reconciled attributions. Existing resolved biome answers are retained.
world-bounds observations 225/620 are the same ocean-heavy-seed start in two runs
at structure_starts, not full chunks. Inclusive envelope [116,31,346,128,78,442]
gives 13x48x97 planned-layout blocks. This is one layout reproduced, not two
independent samples, populated blocks or a family-wide bound. The root uses
standard jigsaw absolute 32, depth 7, no projection and no terrain adaptation.

Twenty reachable templates include the tower, bridges, resource/dungeon features
and vanilla bastion mob components. There are no missing graph references,
unresolved entity IDs or generation markers. Preserve template-owned piglin/brute
entities and legacy blaze/hoglin spawner inputs separately. No realized population,
conversion or simultaneous component selection is asserted. Empty spawn overrides
do not disable ambient spawning. Exact bridge/treasure chest sources remain saved
loot references; resource blocks remain distinct from container rewards.

Complete retained spiral_tower_randomization rules only replace material, including
blackstone to lava at a configured 0.01 match probability. The bridge processor
removes matching blackstone at 0.25. These are authored hazard ingredients and
rule probabilities, not observed hazard frequency or tested traversal difficulty.
No processor adds a mob, physical spawner or loot assignment. The graph and saved
assembly supply visual form while Nether terrain and chunk stage limit exposure
claims. No new source capture or measurement was necessary.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-explorify-spiral-descriptions.json
uv run pytest -q tests/item8/test_explorify_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

## Mangrove hut and End shipwreck

Two families each have three templates and no missing graph references. Twelve
missing descriptions and eight existing attributions are integrated. Hut main
is 14x32x16. Its upward connectors [3,22,10] and [3,26,10] meet downward connectors
at [0,0,0] of 1x2x1 entity templates, placing them inside the main envelope at
Y=23..24 and 27..28. Children terminate at empty pools. Cat is an animal; witch
is the authored enemy source. The hut processor only replaces mangrove logs with
stone where location matches base_stone_overworld. No saved loot table occurs.

Shipwreck's 1x1x1 base points up to the hull's downward Y=0 connector. Sideways
hull is 12x13x27 with connector [11,0,0]; upside-down is 13x11x25 with connector
[12,0,0]. Thus one selected hull sits one layer above the base. The base remains
within its horizontal projection: assembled envelopes are 12x14x27 or 13x12x25,
including the one air-final-state base layer. Hulls are alternatives, not summed
pieces, and their connectors terminate at empty pools. No top-level entities or
physical spawners occur; both preserve End-city loot references. All pools are
rigid and ship processors empty. Rotation may exchange X/Z; these are nominal
piece envelopes including padding, not occupied or observed geometry.

Standard jigsaw WORLD_SURFACE_WG start offsets are hut -21..-17 and wreck -7..-5,
with no terrain adaptation. Empty spawn overrides do not disable ambient spawning.
Connector/form evidence supports qualitative visibility limitations without a
world run or measured discovery distance. No new source capture or tooling.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-explorify-hut-wreck-descriptions.json
uv run pytest -q tests/item8/test_explorify_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

## Five settlement-family attributions, geometry still open

Campsite, dark forest settlement, farmstead, ruins and tavern now integrate eight
explicit attributes each, plus their existing resolved biome answers. This is
40 answers: 20 missing placement/design interpretations and 20 reconciled source
attributions. Ten approximate assembled-geometry answers remain unresolved.
There are no retained saved layout observations for these families; piece sizes
are not substituted for whole settlements. No family completion count advances.

All five roots have complete traces with no missing references, unresolved entity
IDs or generation markers. Preserve exact template-owned animals/villagers/cats/
golem where present, and ruins monument/02's saved zombie-spawner input. These
are authored sources, not simultaneous realized populations. Empty spawn overrides
do not disable ambient spawning. Exact saved loot tables remain attributed to
components. Other than the ruins overlays below, inspected processors only alter
material, aging or path/water adaptation, not entities or physical spawners.

Root offset is 0 and adaptation beard_thin. Preserve projection/depth/expansion
choices: campsite WORLD_SURFACE/7/false, dark forest WORLD_SURFACE_WG/3/true,
farmstead MOTION_BLOCKING_NO_LEAVES/6/false, ruins OCEAN_FLOOR_WG/4/true,
tavern WORLD_SURFACE/7/true. These describe starts, not terrain exposure or the
extent of the assembled network. Qualitative component roles supply visual forms.

The same pack metadata retained above declares f15 applicability. Overlay
ruins_house_processor adds capped suspicious-gravel append_loot delegates with
limits 3 for minecraft:archaeology/trail_ruins_common and 1 for trail_ruins_rare.
ruins_path_processor uses limits 5 and 2 respectively. Both match the
minecraft:trail_ruins_replaceable tag. Exact overlay hashes, table IDs, inputs
and limits are now explicit in ruins loot_table_source. Limits are processor
inputs, not guaranteed whole-family counts. Root-only generic selection would
omit this evidence, so do not drop it in final integration. No new selector,
source capture or world measurement was added.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-explorify-settlement-attribution.json
uv run pytest -q tests/item8/test_explorify_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

## Five settlement geometry run

The ten outstanding claims are approximate footprint and vertical size for
campsite, dark_forest_settlement, farmstead, ruins and tavern. The retained bounds
catalog has no observations for these five assemblies, and component sizes do
not establish settlement dimensions. Reuse the Item 7 locate/Chunky lifecycle,
with explicit target IDs, rather than introducing a simulator or runtime agent.
The only tool extension accepts targets while preserving the existing defaults,
frozen materialization, 81-chunk target regions and correlated save/stop checks.
This uses the previously established Chunky instrumentation, 136 retained JARs
plus Chunky, with the pinned Java, heap, configuration and ordinary seed 42.

One fresh run requests five locations. Saved start-piece envelopes, if present,
will describe examples, including air/padding, not global family bounds or fully
populated component chunks. A failed locate or missing start remains a failed
observation; neither configuration radius nor component size substitutes for it.
No gameplay, encounter-rate or pacing claim is intended.

Reproduction from the repository root (new output and target paths required):

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
  --target instances/item8/explorify-geometry-r1 \
  --log-path evidence/raw/item8/explorify-geometry-r1/console.log \
  --captured-config evidence/raw/item8/explorify-geometry-r1/configuration \
  --receipt evidence/raw/item8/explorify-geometry-r1/run.json \
  --timeout-seconds 900 \
  --structure explorify:campsite \
  --structure explorify:dark_forest_settlement \
  --structure explorify:farmstead \
  --structure explorify:ruins \
  --structure explorify:tavern
```

The target-input change is checked by the existing lifecycle regression with
both legacy and explicit Explorify targets, including exact commands and clean
flush/stop completion. Run results and geometry acceptance are pending.

### Accepted geometry r1 results

Run source: `5bc81f0e3bcb7d0ebfd9d760145ca00021f069b8`. All five target
regions completed, the correlated save succeeded, exit code was zero and the
frozen configuration capture passed. The committed lifecycle receipt is
`evidence/item-8/runtime/explorify-geometry-r1/run.json`.

| Family | Decoded line | Inclusive envelope (min XYZ, max XYZ) | Size XYZ | Pieces |
| --- | ---: | --- | --- | ---: |
| campsite | 1666 | -2606,66,1375,-2592,71,1401 | 15,6,27 | 4 |
| dark_forest_settlement | 3364 | 185,144,9571,279,173,9647 | 95,30,77 | 54 |
| farmstead | 2217 | 243,66,-2437,270,75,-2410 | 28,10,28 | 8 |
| ruins | 569 | -5816,113,-2880,-5728,128,-2808 | 89,16,73 | 104 |
| tavern | 5037 | 1622,63,-2013,1646,80,-1991 | 25,18,23 | 13 |

Each targeted start is `minecraft:full` in `minecraft:overworld`. Take the minimum
of all saved piece minima and maximum of all piece maxima, then subtract minima
from maxima and add one, as implemented by
`mcpack_evidence.item8_world_bounds.observed_bounds`. X/Z gives footprint and Y
vertical size. This direct derivation uses the exact `chunks.jsonl` lines above;
its SHA-256 is 3edc76f13e4c711f241df3391cdd956523a484bd0b72ce243415047ec3469c4f.
The 5,646 decoded chunks include locate-generated and surrounding partial chunks,
not 5,646 completed sampling chunks. An incidental tavern at line 3501 has a
21x12x25 planned envelope at `minecraft:structure_starts`; it is preserved but
not substituted for the predeclared targeted example. No frequency estimate.

The ten geometry attributes are integrated into `family-decisions.json` and
`inventory.json`. All fourteen Explorify family descriptions are now assessed.
Only these five inventory rows and the decisions input hash changed. Six affected
inventory tests, Ruff and Basedpyright passed. Inventory matches
`evidence/raw/item8/inventory-explorify-settlement-geometry-final.json`, SHA-256
41bfb09c46df6a52c9af2b25ddaddd2b496bed90b275b67abfb6eb6121a3ef71.

Preservation and reproduction use existing tools. After verified clean stop:

```sh
uv run python -c 'from pathlib import Path; from tools.stage_item7_world import copy_world_boundary; copy_world_boundary(Path("instances/item8/explorify-geometry-r1"), Path("evidence/raw/item8/explorify-geometry-r1/world"))'
uv run -m tools.decode_item7_world evidence/raw/item8/explorify-geometry-r1/world --output evidence/raw/item8/explorify-geometry-r1/chunks.jsonl
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/explorify-geometry-r1 --archive evidence/raw/item8/item8-explorify-geometry-r1-5bc81f0e.tar.gz --manifest evidence/item-8/raw-custody/explorify-geometry-r1-manifest.json --revision 5bc81f0e3bcb7d0ebfd9d760145ca00021f069b8
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/item8-explorify-geometry-r1-5bc81f0e.tar.gz --manifest evidence/item-8/raw-custody/explorify-geometry-r1-manifest.json --target evidence/raw/item8/explorify-geometry-r1-restored --receipt evidence/item-8/raw-custody/explorify-geometry-r1-local-restore.json
```

World copying holds the Java-compatible POSIX record lock and excludes
`session.lock`. Original instance and capture remain preserved. The archive is
12,675,799 bytes, 271 files, 65,478,116 uncompressed bytes, SHA-256
513dd78e1fd108cbb477d96039a9cd4da9ea74714aa14695dc54b59daea227e2.
It includes logs, captured configuration, the stopped-world boundary, decoded
chunks and run receipt. No server binaries are included.

[Published raw archive](https://github.com/copeugne/mcpack/releases/tag/item-8-explorify-geometry-2026-09-07-r1).
The release is non-draft; fetched and remote tags resolve to the run source above.
Release metadata is retained in `raw-custody/explorify-geometry-r1-release.json`.
The downloaded archive restored all 271 files with verified hashes:

```sh
gh release download item-8-explorify-geometry-2026-09-07-r1 --dir evidence/raw/item8/explorify-geometry-download --pattern item8-explorify-geometry-r1-5bc81f0e.tar.gz
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/explorify-geometry-download/item8-explorify-geometry-r1-5bc81f0e.tar.gz --manifest evidence/item-8/raw-custody/explorify-geometry-r1-manifest.json --target evidence/raw/item8/explorify-geometry-downloaded-restore --receipt evidence/item-8/raw-custody/explorify-geometry-r1-downloaded-restore.json
```

Local copies share one disk; the GitHub asset is the separate durable copy.
Use absent destinations when reproducing archive or restore operations.
