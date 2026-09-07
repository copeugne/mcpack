# Supplementaries generation and elevator sources

Extractor 24f0a7545218356b416aed0ab750292b49aa719c. Manifest SHA-256: 0eb64c666c0db4bd45091038bb2b3d622a1e57f896d31fe0df1279f2ff357e5d. Independent r1 matches every generated file.

Eleven sources cover ModWorldgen, four custom features, two structure implementations, the mineshaft elevator and its direction helper, and the two mineshaft injection mixins. This is the concrete generation boundary identified by the packaged components and elevator class consumers, not full provider closure.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --class-name net/mehvahdjukaar/supplementaries/reg/ModWorldgen.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/BarnaclesMultifaceGrowthFeature.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/BasaltAshFeature.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/RoadSignFeature.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/SpawnEntityWithPassengersFeature.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/GalleonStructure.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/RoadSignStructure.class --class-name net/mehvahdjukaar/supplementaries/common/worldgen/MineshaftElevatorPiece.class --class-name 'net/mehvahdjukaar/supplementaries/common/worldgen/MineshaftElevatorPiece$1.class' --class-name net/mehvahdjukaar/supplementaries/mixins/MineshaftCorridorMixin.class --class-name net/mehvahdjukaar/supplementaries/mixins/MineshaftPiecesMixin.class --output evidence/raw/item8/supplementaries-generation-r1
```

## Registered Road Sign assessment

Ten attributes integrate one family/root, one trigger template and its existing
feature/callback path. Exact sources: this directory's RoadSignStructure.txt and
RoadSignFeature.txt, supplementaries-road-sign-callback/BlockGeneratorBlockTile
under its archive directory, and pinned packaged-json/templates-redacted catalogs
at data/supplementaries/worldgen/ and data/supplementaries/structure/road_sign.nbt.
The catalogs bind supplementaries-neoforge-1.21.1-3.6.8.jar. No new capture/tool.

The template is7x7x7 but contains only two jigsaws at(3,0,3)/(3,1,3). The lower
upward connector selects a feature pool, not another architectural template.
RoadSignFeature.place writes ground over X/Z -2..2 excluding corners, giving a
5x5 patch. With base=feature origin below1, the support/ground occupies base-1
and base, with temporary blocks/post/generator through base+4. The working
vertical span is six levels, not seven blocks of visible sign. applyPostProcess
replaces the generator and adds nearby signs, lanterns/candle details or a notice
board, all within this small local design. Source geometry is not observed
exposure or proof of the asynchronous callback's completion.

Existing world-bounds observations374/754 are repeated run-a/run-b records of
one full-chunk start at chunk10,2 in the biome-diverse Overworld seed. Inclusive
box [162,75,40,168,81,46] gives7x7x7. Observations407/787 are repeated records
of one other start at chunk41,7, box [664,79,114,670,85,120], but that chunk is
only structure_starts. Do not count repeats as independent samples or the
planned-only start as a populated sign. Original observation links are retained.

RoadSignStructure.getSuitablePosition requires destination-cache biome overlap
with the dimension's possible biomes. It samples WORLD_SURFACE_WG at the chunk
center and four +/-2 corners, requires center height40..105 and at least sea
level, rejects fluid corner surfaces and height spread greater than1, then uses
Math.round(sum/5.0f)+1. This is a surface landmark despite the strongholds step.
Captured root-biome overlap is Overworld, also supported by the retained start.

Neither template nor feature/callback adds mobs or ordinary/trial spawners.
spawn_overrides is empty. BLOCK_GENERATOR is a deferred sign helper, not a mob
spawner. No loot-table binding occurs. Empty destination results instead create
a writable book containing "nothing here but monsters" and three newlines,
placed on a notice board two blocks below the callback. That fixed content
neither creates monsters nor proves recoverable loot. Nonempty results configure
pointing signs and optional decorations. Frozen enabled flags and distance text
are true; exit_search_early=true and max_structures_searches=12. Callback code
passes250 directly as its lookup radius argument; do not substitute the common
config max_search_radius200 into a claim about this call. Lookup can fail or
finish without destinations; full chunk status does not verify its result.

Rebuild: `uv run -m tools.build_item8_inventory --output <absent-path>`.
Validation: `uv run pytest -q tests/item8/test_supplementaries_provider_scope.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py`.

Fifteen focused tests pass. Semantic comparison changes only Road Sign and the
decisions identity; source membership, biomes and observations remain unchanged.
Inventory SHA-256: `99be3abcf4eb55f3d1864658a58cabd5a465307743cf37e5c0e5acf659d53303`.
