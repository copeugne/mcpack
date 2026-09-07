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
