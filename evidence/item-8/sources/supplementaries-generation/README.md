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

## Galleon placement and architectural geometry

Four attributes integrate dimension eligibility, approximate footprint/height
and surface classification. Six encounter, reward and visibility attributes
remain open. This increment uses existing sources; no capture or tool is added.
The 17 templates are at data/supplementaries/structure/galleon/ in the pinned
supplementaries-neoforge-1.21.1-3.6.8.jar catalog.

Main galleon is19x37x47. At origin0,0,0, its sail receiver (8,25,15) south
joins sail incoming(5,1,0) north, giving origin(3,24,16). Every sail alternative
is13x7x2, wholly inside the main envelope. Orlop receiver(9,2,11) north joins
(2,1,4) south, origin(7,1,6), size5x3x5. Room receiver(9,5,11) north joins
(2,1,5) south, origin(7,4,5), size5x4x6. All room/orlop alternatives share
these dimensions. These are interior components, not appended family footprints.

Main hull receiver(9,5,12) south joins back01 incoming(4,1,0) north, origin
(5,4,13), size9x4x8. Its outgoing(4,1,7) south joins either mid's incoming
(4,1,0) north, origin(5,4,21), size9x4x4. The mid outgoing(4,2,3) south
requires the front's south-facing(4,2,3) incoming connector to turn180 degrees.
The resulting front origin(13,4,28), rotated size9x4x4, occupies X5..13,
Y4..7,Z25..28. Back03 instead directly joins the end at the same front origin;
its size9x4x12 fits origin(5,4,13). All these components stay inside the main
19x37x47 architectural envelope.

Back02 is preserved as a packaged alternative but its incoming name is
supplementaries:target while the main receiver targets minecraft:bottom.
Its outgoing target also differs from the available mid connector names.
Do not claim this alternative successfully attaches or silently repair it.
Attachment success is not required to expand the nominal outer architecture:
these interior choices and failures do not enlarge the main envelope. Pool
weights are selection inputs, not observed frequencies. Urn features, boat
placement attempts and later entity movement are not architectural piece sizes.

GalleonStructure.getSuitablePosition computes WORLD_SURFACE_WG first occupied
height+1 at chunk center, requires equality with sea level, applies the packaged
climate parameter point and adds offset-3. findGenerationPoint uses size10,
no expansion hack or additional heightmap projection, and max distance64.
The latter is a placement limit, not ship width. The resolved root biome set
intersects twelve captured Overworld biomes and no other captured dimension.
No retained Galleon start exists. These source assessments do not prove actual
exposure, occurrence, populations or successful reward/boat behavior.

Validation for this increment: `uv run pytest -q tests/item8/test_supplementaries_provider_scope.py tests/item8/test_inventory_sources.py`.
Semantic comparison changes only Galleon and the decisions identity; original
biomes, membership and observations remain unchanged. Inventory SHA-256:
`e330e017db912e263e9c9750835ca86c4605a3fa43cef9483a738ee848a7e4a3`.

## Galleon encounter, rewards and visibility

Six attributes complete Galleon using the existing sources. Geometry/placement
remain unchanged. Use SpawnEntityWithPassengersFeature here, Moonlight's
ChunkGeneratorMixin in moonlight-common-hooks and SpawnBoxStructurePiece in
moonlight-generation-delegates, existing supplementaries-placement-processor,
and urn-reward-behavior/urn-patch-geometry. Their identity manifests are linked
in the family. No new capture, validator or measurement tool is introduced.

Main template block_entities28/41/42/45 are moonlight:spawn_box markers named
galleon_enemies, not physical spawners. Their exact positions, offsets and sizes
remain in the assessment. The structure supplies a monster list: pillager
weight5/group1 and plunderer weight7/group1. GalleonStructure exposes its settings;
ChunkGeneratorMixin.getMobsAt requests special spawn lists and the retained
SpawnBoxStructurePiece.getNamedBoxesAt resolves a containing named box. This
attributes the regional spawn source without claiming measured spawn counts or
frequency. All seventeen templates have no ordinary/trial spawner blocks.

hull_back03 saves ravager Health100/PersistenceRequired1; hull_room02 saves
iron_golem Health100/PersistenceRequired0; both have empty hands/armor.
hull_front02 saves an armor stand with chainmail helmet. Only ravager belongs
to the hostile crew assessment. Plunderer feature weights are4 plunderer,1
pillager,1 empty. Boat pool weights1/1/2/1/2 choose boat with plunderer+pillager,
boat with plunderer, cannon boat with plunderer, empty boat, or empty element.
These are selection weights, not actual populations.

SpawnEntityWithPassengersFeature.place loops attempts+5, so the declared4 boat
attempts permit up to9 candidate positions, returning on first success. X/Z
spread4 means inclusive offsets-4..4. Terrain-matching height is sampled at the
feature origin, not each randomized candidate. Candidate air, ground-rule and
chunk checks remain required. trySpawningAt creates passengers, starts riding,
finalizes mobs with STRUCTURE type and applies configured persistence before
adding the entity with passengers. Null creation/failing candidates can yield
no entity. The declared cannon loot table is assigned only to ContainerEntity;
it must not be generalized to an ordinary non-container boat inventory.

The urn pool selects urns_patch directly:9 tries, spreads4/1, supported-air
filter and treasure=true. It does not apply cave_urns' six separate-origin
repetitions. The already assessed urn break path can select an actual urn_spawn
tag entity after the frozen0.01 random check, doTileDrops and enchantment guard.
Required packaged entries are silverfish/slime/bat; optional declarations retain
the existing uncertainty rather than being invented as available entities.
Urn creature releases are conditional interactions, not resident mobs/spawners.
The existing urn assessment records common/uncommon/rare/epic reward tables,
weight/quality60/-5,32/-2,7/2,1/5, separate silk-touch/treasure conditions and
appending stored contents. Reuse those exact sources rather than duplicate them.

Main template loot refs include key, cannon, safe and chest; front01/front02
also bind chest. Exact NBT paths remain in the inventory. Fixed contents:
main block_entities35 pulley has one rope; front02 block_entities1 urn has one
ash; room01 block_entities1 jar has six cookies in slots0..5 and empty fluid;
front02's armor stand has the helmet. Source contents are not verified runtime
recovery. remove_disabled_blocks preserves incoming position/NBT when replacing
a disabled block. Frozen cannon/urn/jar/globe/cannonball/ash/candle-holder/gold
and sconce settings inspected here are enabled. Sail04 uses empty processors.
The processor does not introduce a block-spawner path.

The ship/sails and sea-level placement support a qualitative maritime landmark,
with hull rooms concealed by the hull and water. This is not measured visibility,
encounter difficulty or exploration pace. No retained Galleon start is claimed.

Thirteen focused tests pass using the preceding command. Semantic comparison
changes only these six Galleon attributes, rationale/evidence and decisions pin;
its prior four attributes and all original membership/observations are preserved.
Inventory SHA-256: `ce61f4dd05b1e4c70b2b3fab5fc62b1ee7a9a5cad6f6765c908e9859c0953983`.
