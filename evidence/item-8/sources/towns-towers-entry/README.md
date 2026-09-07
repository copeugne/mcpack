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
