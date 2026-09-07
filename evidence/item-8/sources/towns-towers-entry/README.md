# Towns and Towers source assessments

## Ocean sites and Desert Mimic

Four canonical families use four registry roots: pillager_outpost_ocean,
village_ocean, wreckage_ocean and mimic_desert in towns_and_towers. Their
traces contain 22, 11, 1 and 3 template references respectively, with 34 unique
templates because three vanilla villager templates are shared. Aliases and
components remain distinct from family identity. Exact selected source archive,
NBT path and hash are already bound by pool-traces-content.json.gz. Root JSON
is data/towns_and_towers/worldgen/structure/<root>.json; provider pools live
under data/kaisyn/worldgen/template_pool, not the registry namespace.

All selected single/legacy pool elements have empty processors. Ocean Outpost
uses a base/variant selection of weights 80:1, authored illager components,
saved allays, optional villagers/animals and a full-bounds natural pillager
override. Ocean Village selects its base with weight 1 versus empty weight 2,
then uses ship alternatives and vanilla villagers. Wreckage has no authored
entities/spawners. Desert Mimic passage_2 block_entities 1 authors a husk
spawner; passage_1 index 2 contains arrow stacks 2,3,3,2,3,2,3,3,2. TNT in its
pyramid palette is source content, not proof of a functioning trap.

Fixed payloads are separate from table rolls. Both outpost bases preserve a
framed crossbow, fuel, luck potion, shells, books and four diamonds. The village
mothership preserves smoker coal and a luck potion. Retain legacy item NBT as
source data; this assessment does not claim tested component conversion,
combat activation, drop yield, trade behavior or recoverability.

World-bounds observation pairs retain repeated runs of the same seed/location:

| Family | Indexes | Start chunk | Seed | Envelope size XYZ | Start status |
| --- | --- | --- | --- | --- | --- |
| Ocean Outpost | 63,466 | -40,26 | 42 | 27,65,76 | structure_starts |
| Ocean Village | 285,674 | 2,30 | 95920844204830198 | 80,41,81 | full |
| Ocean Wreckage | 77,480 | 12,18 | 42 | 14,3,14 | full |
| Desert Mimic | 383,763 | 21,17 | -3503646078644842058 | 40,35,21 | full |

Wreckage additionally has biomes-stage observations 68/471 at (13,-34), seed42,
with the same size. Inclusive envelope dimensions are max minus min plus one.
They describe example piece-box layouts, including air/padding. Full start
chunks do not prove that every distant component is fully placed. Repeated
runs are not independent sites. Outpost's planned envelope matches its rotated
76x65x27 base template; wreckage matches its sole 14x3x14 template. No new
measurement is required for these approximate dimensions and explicit limits.

All roots use fixed absolute heights (58,59,62,35 respectively) without surface
projection. Step names do not prove underground placement. Overworld biome
intersections agree with observed dimensions. Visibility is qualitative
architectural inference, not measured discovery distance or guaranteed exposure.

Rebuild: `uv run -m tools.build_item8_inventory --output <absent-path>`.
Validation: `uv run pytest -q tests/item8/test_towns_towers_provider_scope.py tests/item8/test_inventory_sources.py`.
All six tests pass. Semantic comparison changes only these four families and
the decisions pin; unrelated families, biomes, identities and observations are
preserved. Inventory SHA-256: `0441e3ad4343bb732cd8e3df24818a5cabf93800dfdbb4c173a4fd84b5c00d08`.

## Fort and Tower outposts

Two families preserve 25 variants and 42 unique selected templates. Nine Fort
and sixteen Tower roots retain their existing placement definitions. All base
templates have only upward small mob attachments except the Mediterranean
fort's two architectural fields. The authoritative assessment records each
base's XYZ size directly from its selected NBT. Upward receiver Y plus three
blocks remains below the base top, and single-column footprints stay inside it.
These source dimensions do not imply observed generation or exposed area.

For Mediterranean, put the 16x15x19 base at (0,0,0). Its field receivers are
(0,1,9) west_up and (15,1,9) east_up. Field_1 is 14x3x24 with incoming
(13,1,12) east_up; field_2 is 13x5x18 with incoming (0,1,9) west_up.
Align opposite faces and translate by outgoing plus outward unit vector minus
rotated incoming. Left field_1 origin is (-14,0,-3); right field_1, rotated
180 degrees, is (16,0,-2). Right field_2 origin is (16,0,0); left field_2,
rotated 180 degrees, is (-13,0,1). Both field_1 yields 44x25 XZ; both field_2
42x19; mixed choices 43x24. Failed attachments can leave only the central
footprint. Field_1's terrain_matching projection means these nominal origins
do not establish final Y or terrain-warped height. Record that limitation.

All variants share authored captain/grunt choices already inspected above.
No spawners or generation markers occur in the selected trace. Iberian uses
kaisyn:village/exclusives/iberian/house_iberian and Nilotic uses
kaisyn:outpost/exclusives/outpost_nilotic; both are minecraft:rule lists with
building-material substitutions only. Other selected lists are empty. Their
source JSON is under data/kaisyn/worldgen/processor_list. Neutral allays,
captive villagers, bees/hive occupants, cats and decorative equipment retain
variant ownership; none are automatically hostile encounters. Fixed container
items and frames are attributed separately from the existing exact loot refs.

The initial dimension assertion rejected Nilotic before any file write: its
resolved biome constraint has no intersection with frozen runtime biomes.
The accepted result preserves this ineligible packaged variant explicitly;
the other 24 variants intersect Overworld only. Neither family has retained
direct start observations. Do not turn biome compatibility into generation proof.

Eighteen attributes complete these two assessments. Six applicable tests pass
using the command above. Semantic comparison preserves identities, biome and
world observations, existing placement classification and unrelated families.
Inventory SHA-256: `ab41272b615fda7958bbf685cbcc698c2b50a83d5ebacecb38341d0ac47ca96a`.

## Camp outposts

Five roots, 35 present unique templates, nine added attributes. Existing placement
classification is preserved. All present selected pools use empty processors;
shared illager source attribution applies, and saved allays remain neutral.
No spawners occur in those present templates. Exact source loot refs and fixed
base diamond/book chests, beach charcoal and kitchen coal remain distinct.

Geometry uses the same opposite-connector derivation. Beach/snowy-beach are
single 14x12x28 bases; their mob receivers are at most Y2. The other centers
are 9x4x9 with side receivers west (0,1,4), north (4,1,0), south (4,1,8),
east (8,1,4). Kitchen/workshop incoming joints are (4,0,14) south, except
Savanna workshop (7,0,14). For Sparse Jungle, north tent origin is (2,1,-7),
west tent (-7,1,2), kitchen (9,1,0), workshop (0,1,9). Union is
(-7,0,-7)..(23,9,23), giving 31x10x31. Wooded Badlands tents are 9x5x9
with (4,0,8) south incoming, yielding north (0,1,-9), west (-9,1,0)
and union (-9,0,-9)..(23,9,23), 33x10x33. Mob attachments fit these boxes.

Savanna has weighted alternatives and repeatable towers. Available tent_5
is 13x21x13 with incoming (6,1,0) north; rotating for the north or west
receiver permits a footprint reaching -13 on those axes. Kitchen/workshop
reach +23, giving up to nominal 37x37 for available primary pieces. Their
roughly 21..22-block height is separate from optional four-high tower segments
and three-to-five-high fallback caps. Root size is 4 with expansion hack;
collision and fallback selection mean this is not a completed-world envelope.

The preserved trace already records eight missing resources: tent_6 and seven
camp-path tower_top templates. The fallback pool references present village-path
caps instead. Do not silently substitute those caps for the missing primary
choices, claim the graph complete, infer absent payloads or repair the frozen
mod as inventory work. Its available-design dimensions and content are reported
with this packaged defect. No runtime failure outcome was inferred or fabricated.

Six applicable tests pass using the command above. Semantic comparison changes
only Camp and the decisions pin, preserving placement, biomes, identities and
observations. Inventory SHA-256:
`1b22f228c91204f7b548287885c80dc70ae85eaf387490b002b3a9596660cd0c`.

## Village attribution, geometry still open

Seven attributes are integrated across 26 variants and 777 unique present
templates. Existing surface/underground assessment is unchanged. Per-root
selected template_contents retain exact source identities and entity/loot
ownership. Nilotic and Piglin have no runtime biome intersection; the other
24 intersect Overworld. Neither compatible biomes nor inhabited template
names prove observed population or generation.

Present identified inhabitants comprise villagers/traders, livestock, cats,
wolves, camels, defensive golems and Piglin-variant hoglins, alongside decorative
entities. Saved trader Offers and equipment remain source NBT, not tested live
trade availability. Sparse Jungle tiki_torch_1 /entities/0/nbt has no ID;
keep that source payload unresolved rather than inventing its entity type.
Missing pools include Mediterranean bishop, Beach lighthouse master, Meadow
villagers and Sparse Jungle chief; Nilotic has three missing houses and Swamp
two missing crossroads. Exact IDs remain in the authoritative assessment.

No spawners occur in the present template trace. Selected processors are empty,
block-substitution rules or jigsaw_replacement. Inspected final states contain
architectural/material blocks, not spawners. Forest street rules are a material
loot exception: data/kaisyn/worldgen/processor_list/village/forest_ruins/street_forest.json
converts grass candidates to suspicious gravel and appends
kaisyn:archeology/forest_ruins_common (configured rule chance .01) or
forest_ruins_rare (.005). Ordered rules do not imply independent observed loot
probabilities. These processor sources supplement per-template container refs.

Whole-settlement footprint and vertical size remain unresolved. No retained
starts exist for this family; adding individual building dimensions would not
prove an assembled branching settlement envelope. Do not count this family as
fully assessed yet. Determine the smallest adequate geometry evidence next,
reusing existing tools and distinguishing bounded concentrated variants from
branching streets. No new runtime or measurement was performed for attribution.

Six applicable tests pass. Only Village attribution and the decisions pin
change; geometry, existing placement, biomes, identities and observations remain
unchanged. Inventory SHA-256:
`ef7e3b2a9c099eddb88c50f4b34f0a1262b0a1abea4f3d3baed9dc6ceb791c05`.

### Predeclared Village geometry capture

Two illustrative roots on ordinary seed42: Forest for branching streets and
Savanna Plateau for vertical ramshackle assemblies. Reuse the existing gap
harness, 81 requested chunks per target (162 total), timeout 900 seconds.
This addresses approximate assembled dimensions, not all-variant extrema,
frequency, pacing or complete gameplay. Compact source-bounded variants can be
attributed separately. Keep all variant definitions and source limitations.
No new measurement tool or schema is necessary. The absent assembled evidence,
not a desire for additional assurance, warrants this run.

Use fresh verified frozen materialization with the existing Chunky instrument,
readiness, correlated save and clean stop. Preserve failures. Decode the stopped
world using existing tools, require a full start chunk for accepted placed-start
envelopes, and record inclusive dimensions with existing observed_bounds.
Archive raw evidence and test local/published-download restores with the existing
archive tool, retaining source revision. Do not repeat an unchanged passing run.
The following command is predeclared and not yet claimed successful:

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
  --target instances/item8/towns-village-geometry-r1 \
  --log-path evidence/raw/item8/towns-village-geometry-r1/console.log \
  --captured-config evidence/raw/item8/towns-village-geometry-r1/configuration \
  --receipt evidence/raw/item8/towns-village-geometry-r1/run.json \
  --timeout-seconds 900 \
  --structure towns_and_towers:village_forest \
  --structure towns_and_towers:village_savanna_plateau
```

### Village geometry result and custody

Executed from 4075bc17b2890f3b76ebd9522f2b95d1ac9abe25. Both targets completed,
with readiness, correlated save, clean exit and accepted frozen configuration.
No runtime remains. The existing decoder retained 2,763 chunk records, including
partial and locate-created chunks, not a sampling denominator.

| Root | Decoded line | Start chunk XZ | Pieces | Envelope | Size XYZ |
| --- | --- | --- | --- | --- | --- |
| towns_and_towers:village_forest | 118 | 30,-186 | 148 | 375,87,-3053,572,126,-2917 | 198,40,137 |
| towns_and_towers:village_savanna_plateau | 2103 | 1756,-1488 | 17 | 28096,115,-23808,28112,142,-23789 | 17,28,20 |

Both saved starts are in full chunks. Existing
mcpack_evidence.item8_world_bounds.observed_bounds derives these envelopes from
preserved piece boxes and inclusive max-min+1 dimensions. Full start chunks do
not imply every distant component is fully placed. Decoded SHA-256:
a05f6105a442330494ff5542e5b2e163f54c28b49bd5f7782d2029b9c7ac1765.

Compact source examples supplement, rather than extrapolate, these layouts.
Grove's grove_meeting_point_1 is 25x15x21; small villager/cat/golem attachments
stay within that envelope. Snowy Slopes' snowy_slopes_meeting_point_1 is
21x12x15. Its table is 10x3x6, incoming (4,1,0) north_up. The inn's north
receiver (10,1,0) north_up attaches the 180-degree table at (5,0,-6); south
receiver (10,1,14) south_up attaches the unrotated table at (6,0,15).
Union (0,0,-6)..(20,11,20) is 21x12x27. Decor is rigid with common_swiss
material rules; small inhabitant pieces stay inside. Waystone content remains
subject to the previously assessed optional integration and is not assumed
available. Neither compact example establishes dimensions for all 26 variants.

Executed preservation commands (use absent destinations when reproducing):

```sh
uv run python -c 'from pathlib import Path; from tools.stage_item7_world import copy_world_boundary; copy_world_boundary(Path("instances/item8/towns-village-geometry-r1"), Path("evidence/raw/item8/towns-village-geometry-r1/world"))'
uv run -m tools.decode_item7_world evidence/raw/item8/towns-village-geometry-r1/world --output evidence/raw/item8/towns-village-geometry-r1/chunks.jsonl
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/towns-village-geometry-r1 --archive evidence/raw/item8/item8-towns-village-geometry-r1-4075bc17.tar.gz --manifest evidence/item-8/raw-custody/towns-village-geometry-r1-manifest.json --revision 4075bc17b2890f3b76ebd9522f2b95d1ac9abe25
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/item8-towns-village-geometry-r1-4075bc17.tar.gz --manifest evidence/item-8/raw-custody/towns-village-geometry-r1-manifest.json --target evidence/raw/item8/towns-village-geometry-r1-restored --receipt evidence/item-8/raw-custody/towns-village-geometry-r1-local-restore.json
gh release download item-8-towns-village-geometry-2026-09-07-r1 --repo copeugne/mcpack --dir evidence/raw/item8/towns-village-geometry-download --pattern item8-towns-village-geometry-r1-4075bc17.tar.gz
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/towns-village-geometry-download/item8-towns-village-geometry-r1-4075bc17.tar.gz --manifest evidence/item-8/raw-custody/towns-village-geometry-r1-manifest.json --target evidence/raw/item8/towns-village-geometry-downloaded-restore --receipt evidence/item-8/raw-custody/towns-village-geometry-r1-downloaded-restore.json
```

Archive: 4,805,146 bytes, 252 files, 31,684,214 uncompressed bytes. SHA-256:
ebf11d6046dd7f688feadf84493fe4863312ec87fd6253e703870f859ca366e9.
It retains stopped-world data excluding session.lock, decoded chunks, complete
logs, captured configuration, sanitization record and run receipt. Local copies
share a disk. The separate durable copy is the
[published archive](https://github.com/copeugne/mcpack/releases/tag/item-8-towns-village-geometry-2026-09-07-r1).
Local and downloaded restores each verified 252 files; the remote tag resolves
to the exact source revision above. Custody does not establish Item 8 completion.

Two geometry attributes and the directly affected dimension/visibility text
are integrated; source attribution, original observation links and unrelated
families remain unchanged. Eight tests pass:
`uv run pytest -q tests/item8/test_world_bounds.py tests/item8/test_towns_towers_provider_scope.py tests/item8/test_inventory_sources.py`.
Inventory SHA-256:
`35f2d8ff90f72fd1765b875a70d0e9a5f4d444efb05d5810d0a23f697123090b`.
