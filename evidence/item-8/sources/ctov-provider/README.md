# CTOV provider entry and component code

Twelve packaged classes captured with extractor 61663b4. Independent extraction
reproduced all files byte for byte before this README. Manifest SHA-256:
892790797564491473c7bf42d1e92f182cdb640721aa5e00c9a9b9c044de489e.
Archive SHA-256: 4815b19b83541f09cba556e222612bc5ddcc31f7c4ba2198f4b4d6376cca8b2e.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive '[Neoforge]ctov-3.6.3.jar' \
  --output evidence/raw/item8/ctov-provider-r1
```

The NeoForge constructor registers the common configuration, its server event
listener and the modular compatibility processor. Common init is empty.
ServerAboutToStartEvent invokes CTOV.registerstructure, which subscribes a
Lithostitched AddWorldgenModifiersEvent callback. Verbose bootstrap bindings
preserve this callback and the four root-name construction patterns.

The callback obtains existing vanilla outpost/village structure sets and the
structure registry. Enabled size flags, village names and weights are read from
the NeoForge config through captured platform wrappers. The outpost loop uses
its own eleven-name list, not enabledpillageroutpost. CTOVStructureHelper resolves
the corresponding ctov root with getOrThrow and adds a weighted selection entry
to the supplied set. This modifies eligibility of existing roots; it does not
define a new structure family. Frozen configuration and runtime selection must
still be reconciled with this path rather than inferred from config labels.

CTOVConfigHelper.enabledpillageroutpost calls an array-returning implementation
descriptor, while the captured implementation declares a List return. The
captured startup callback does not invoke that wrapper, so this is a retained
source-level mismatch, not a reproduced runtime failure or a reason to modify
the baseline. Config loading/reloading handlers contain no generation action.

ModularCompatProcessor returns the incoming block when its target mod is absent.
When present, it looks up the configured processor list and applies its processors
in order, stopping when a block result becomes null. An absent list preserves the
incoming block. PlatformHelper resolves mod presence through NeoForge ModList;
TextUtils constructs resource IDs and messages. WorldgenRegistry registers only
this processor type. The generated Architectury bridge identifies NeoForge.

Provider coverage remains open for full resource reconciliation: bundled
compatibility directories/ZIP, modifier-driven components outside root graphs,
and explicit dispositions for disconnected and missing components. Reuse this
complete code capture, the packaged catalog and existing CTOV family regressions.
Do not count source classes, processor lists or component templates as families.

## Family description integration

Ten outstanding attributes are integrated from existing evidence: six for the
village and four for the outpost. Village is fully assessed; outpost footprint
and height remain pending. The provider discovery checkpoint above was closed
by later commits, including188a37c9 and the CTOV section of provider-scope.md.
It is not a request to repeat provider discovery.

The existing inventory joins all66 village roots and12 outpost roots to effective
biomes and captured dimension membership. Every root matches only the Overworld.
The village has22 design variants with three sizes each; these remain variants
of one family. All roots use WORLD_SURFACE_WG projection; underground village
roots start14 blocks lower and the other roots use zero offset.

Preserved world-bounds observations include three distinct full-start layouts,
each repeated in run-a and run-b. They are not six independent samples:

| Root | Seed role | Chunk | Saved size X,Y,Z | Decoded line |
| --- | --- | --- | --- | --- |
| ctov:small/village_mountain_alpine | mountainous | 9,9 | 122,35,107 | 13639 |
| ctov:medium/village_mountain_alpine | mountainous | -27,9 | 123,109,143 | 10065 |
| ctov:medium/village_desert | biome-diverse | -22,10 | 129,29,120 | 10102 |

Sources are run-a/run-b role-specific chunks.jsonl paths recorded in
world-bounds.json.gz. The decoder and existing world-bound extractor preserve
piece envelopes including air and padding. A full start chunk does not establish
that all surrounding component chunks were populated. These examples supply
approximate family dimensions without claiming every design, size or extremum.
The109-block mountain envelope includes vertical spread of terrain-following
pieces; it is not an assertion that a single village building is109 high.

Village reachable templates author civilian/passive/defensive mobs and display
entities, with no hostile entity IDs in the resolved set. Empty spawn overrides
leave natural spawning to biome/world conditions. Outpost templates author
allays, iron golems and ravagers. Their full-box monster override separately
selects pillager, evoker, vindicator and witch, each weight1 and group1..1.
This is possible-source attribution, not actual population. Existing per-template
entity bindings and missing-component dispositions remain preserved.

Literal LootTable IDs are now recorded in each family attribute, with the exact
per-template associations in pool-traces-content.json.gz. Village references
include CTOV, vanilla village and Chef's Delight cooker tables. Three village
references have no current-path definition in the packaged catalog:
`ctov:village/desert/`, `ctov:village/desert_fortified/bakery`, and
`ctov:village/swamp/leatherworker`. Outpost references are the vanilla outpost
table and `ctov:pillager_outpost/halloween/tower`; the latter also has no current
packaged definition. Preserve these literal missing bindings as content defects.
Do not silently replace them or claim working loot from their names.

Source architecture supports potential visibility of settlement buildings,
fortifications and canopy designs, with reduced exposure for the underground
variant. Outposts combine towers and surrounding camp features. Neither statement
measures discovery range or guarantees an unobstructed view.

## Outpost geometry capture declaration

Only two required CTOV attributes still lack sufficient assembled evidence:
outpost footprint and vertical size. No retained full-start outpost observation
exists. The plains root uses a16x30x16 rigid base plate, a13x26x13 rigid tower,
terrain-matching15x1x13 feature plates and optional camp components. Its
size4/max-distance80 settings and individual template sizes are not a realized
layout. One targeted observation using the existing runner is the smallest
current evidence increment. No runner extension or new measurement system is
needed.

Predeclare `ctov:pillager_outpost_plains`, ordinary seed42, existing81-chunk target
protocol under the exact frozen Item6 baseline. Preserve locate failure or
missing-component warnings. Existing traces include absent plains allays_cage
and optional Savage and Ravage target references; a successful sample does not
resolve those defects or establish all12 variants. Do not alter the baseline.
Use fresh paths `instances/item8/ctov-outpost-geometry-r1` and
`evidence/raw/item8/ctov-outpost-geometry-r1`. After ready/flush/clean stop,
verify frozen configuration, decode the stopped world, select the full start,
and retain the raw evidence with the existing archive/restore/release workflow.
Do not claim geometry before those steps pass.

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
  --target instances/item8/ctov-outpost-geometry-r1 \
  --log-path evidence/raw/item8/ctov-outpost-geometry-r1/console.log \
  --captured-config evidence/raw/item8/ctov-outpost-geometry-r1/configuration \
  --receipt evidence/raw/item8/ctov-outpost-geometry-r1/run.json \
  --timeout-seconds 900 --structure ctov:pillager_outpost_plains
```
