# Vanilla shipwreck source disposition

Tool `5e750e4`, source evidence `5f82e86`, and frozen-catalog check `db53fd6`
resolve the vanilla shipwreck template alternatives, nominal dimensions and
chest markers. Manifest SHA-256:
`313d8031a873de27b39ca5fa8fed9ab1ea1f3694fc56db8afcd7127a3e4415b8`.
All three classes come from mapped-server archive SHA-256
`26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/levelgen/structure/structures/ShipwreckStructure.class --class-name net/minecraft/world/level/levelgen/structure/structures/ShipwreckPieces.class --class-name 'net/minecraft/world/level/levelgen/structure/structures/ShipwreckPieces$ShipwreckPiece.class' --output evidence/item-8/sources/vanilla-shipwreck-code
uv run pytest -q tests/item8/test_shipwreck_sources.py
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
uv run ruff check tests/item8/test_shipwreck_sources.py
uv run basedpyright tests/item8/test_shipwreck_sources.py
```

Extraction, the final focused test and scoped checks passed. The first test
incorrectly assumed a single palette and failed because templates contain
alternative palettes. The corrected test inspects all palettes. No source data
was changed. For reproduction, use a fresh output directory.

## Components and nominal geometry

`ShipwreckStructure.generatePieces` calls `ShipwreckPieces.addRandomPiece`
once. The latter chooses one template from the isBeached-selected array and
adds one piece. The beached array has 11 alternatives and the ocean array 20;
the first is a subset of the second. All 20 resolve in the frozen template
catalog. Degraded designs, orientations and palette choices remain variants
within the shipwreck family.

The complete dimension mapping is asserted in the frozen-catalog test. Each
template is 9 blocks wide. Its other horizontal dimension is 16, 17, 22, 24
or 28 blocks; rotation can exchange horizontal axes. Ordinary templates are
9 blocks tall; the two with-mast templates are 21 blocks tall. These are nominal
single-template envelopes, not occupied volume or visible size after burial.

Placement ignores structure blocks and air, uses no mirror, and rotates about
pivot (4, 0, 15). `postProcess` samples WORLD_SURFACE_WG for beached variants
and OCEAN_FLOOR_WG for ocean variants. Beached placement uses the sampled minimum
height minus half template height (integer division) minus nextInt(3); ocean
placement uses the integer mean of sampled heights. It then calls the base
template post-processing path. Initial construction at Y 90 is not the final
placement height.

The frozen code's `isTooBigToFitInWorldGenRegion` checks template X and Y against
32, not X and Z. Preserve this detail. All verified vanilla template X and Y
values fit that check, so their height adjustment uses the ordinary postProcess
branch. No game-code fix or hypothetical larger-template experiment is needed
for this source disposition.

## Content

The marker map assigns `map_chest`, `treasure_chest` and `supply_chest` to
SHIPWRECK_MAP, SHIPWRECK_TREASURE and SHIPWRECK_SUPPLY respectively. The marker
handler assigns the selected table to the block below the marker and creates
no entities. Reused `BuiltInLootTables` evidence under `../vanilla-end-city-code`
maps these constants to `minecraft:chests/shipwreck_map`,
`minecraft:chests/shipwreck_treasure`, and `minecraft:chests/shipwreck_supply`.
Its identities manifest SHA is
`ca7cb2c777ad0fc638e28cded50a78ab048ca26ad243eeb564fa72be7cac943c`.

Full and with-mast templates have one of each marker. Back halves have map and
treasure markers. Front halves have supply markers; upside-down front halves
also have a map marker. The test preserves these differences for degraded and
non-degraded variants. All 20 templates have empty authored entity lists and
no ordinary or trial-spawner block types across their palettes.

Natural mobs, retained-mod generation changes and effective loot modifications
are not resolved by this vanilla-source inspection. Template and marker counts
are not observed encounter frequencies or claims of successful placement.

## Next integration

Populate the existing shipwreck family attributes and per-root component lists
from these sources, retaining beached versus ocean selection and burial details.
The current inventory and family decisions are unchanged by this source milestone.
No additional runtime measurement system was needed for nominal geometry.

## Delivered integration

`4363af9` integrates per-root components and seven family attributes using the
existing override mechanism. `3c30ead` delivers the rebuilt inventory. This
supersedes the pending integration instruction above. The source check now binds
both template arrays and nominal dimensions to the family record and verifies
its evidence hashes.

```sh
uv run pytest -q tests/item8/test_shipwreck_sources.py tests/item8/test_family_decisions.py
uv run pytest -q tests/item8/test_shipwreck_sources.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-shipwreck-content.json
```

All 59 affected checks passed. The final focused check and scoped Ruff/basedpyright
passed after narrow annotation and iteration cleanup. Decision SHA-256:
`da5faabb91380aaa6fc09b36a941ded23a633dc50888705eb0a5776e2f8a3bb3`.
Inventory SHA-256:
`7f15e3abd77c380cfccfc836f677027f65d94782fac7ebf2ed033af010f1dcee`.
Only this family's grouping and seven attributes change semantically. The trace,
raw world bounds and world_observations links are unchanged. The dimension
attributes now report nominal template envelopes instead of sample-only sizes;
observed geometry remains available through those original links. Overall Item 8
and remaining effective family attributes are still incomplete.
