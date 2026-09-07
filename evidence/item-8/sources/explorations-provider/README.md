# Explorations provider entry boundaries

Selector b454032 captures the complete 33-class archive. The existing scarecrow,
Slime Cave and deepslate interpretations remain in their earlier source records;
this pass resolves the remaining provider entries and component consumers.
The independent capture reproduced exactly before this README was added.
Archive SHA-256: 420d0373711877a5e1a86b7f9b4f54848f3debb2f116c2509a5cc4eb496c979e.
Identity manifest SHA-256:
7889daf6336c190cec169bc57eac369ebf863eb4c72e2b7895341aa12b4e9b8f.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive explorations-neoforge-1.21.1-1.6.2.jar \
  --output evidence/raw/item8/explorations-provider-r1
```

NeoforgeExplorations loads ModRegistry and attaches ServerAboutToStartEvent.
The callback loads and verifies configuration, then calls addStatuesToVillages.
The two service implementations provide DeferredRegister registration and platform
access. The declared mixins expose pool entries and tree-decorator registration.

ModRegistry registers the scarecrow feature, underground-temple and slime-cave
structure types, slime-cave piece, lantern and cave-vine decorators, and deepslate,
stone-brick-aging and wool-replacement processors. The temple uses its configured
start pool and JigsawPlacement. The Slime Cave's single template and marker
behavior were already resolved; neither type is an additional family merely
because it has a custom codec. The processors transform existing piece blocks.

WorldGenHelper reads the configured village/statue lists, resolves each target
pool and constructs legacy single elements with the empty processor list and
RIGID projection. It updates both expanded and raw weighted lists. A missing
compatible pool causes that addition to return without mutation. Frozen statue
entries target plains, savanna, snowy and taiga village houses pools, with four
statues in each. These are components of consuming villages, not four new roots.

LanternDecorator chooses positions below leaf blocks and writes chains and
lanterns. The packaged large_mushroom tree uses this decorator. Its leaf-position
shuffle uses Collections.shuffle without the generation RandomSource argument;
do not claim deterministic decoration from this source or repair it here.
CaveVineDecorator supplies hanging vegetation to a consuming tree; no packaged
configured feature in this archive uses it. Keep any external consumer separate.

The source capture supports provider reconciliation, not observed placement,
successful block writes or final family attributes. Preserve the underground
temple's missing references and the named mushroom/decoration grouping question
in provider-scope.md rather than silently modifying the frozen content.

## Five standalone family descriptions

After d4cc7261, Desert Ruin, Floating Island, Forgotten Well, Logs and Shrine
had 48 missing explicit descriptions. Shrine's two existing geometry answers
are retained unchanged. This batch integrates those 48 answers using existing
source artifacts; no new capture, measurement or tooling is introduced.

Direct inspection of the complete pool traces and template catalog establishes
thirteen standalone templates, no attachments, no authored entities, physical
spawner NBT, generation markers or missing graph resources:

| Family | Template alternatives | Stored XYZ sizes |
| --- | ---: | --- |
| desert_ruin | 8 | 6x7x7, 6x5x7, 6x5x7, 6x6x7, 6x5x7, 6x5x7, 6x3x7, 6x6x7 |
| floating_island | 1 | 11x14x9 |
| forgotten_well | 1 | 5x6x5 |
| logs | 2 | small 5x4x5; large 5x4x8 |
| shrine | 1 | 9x8x9 |

The desert rows correspond to ruins/desert_1 through desert_8; the other template
IDs are retained directly in each inventory entry. Absence of jigsaw blocks
makes these template envelopes adequate nominal assembly dimensions, including
air/padding. Rotation may exchange X/Z. They are not occupied-world or exposed
height measurements.

The five root definitions under data/explorations/worldgen/structure use vanilla
jigsaw, depth one, WORLD_SURFACE_WG and empty spawn_overrides. Start offsets are
0/60/1/0/0 in table order. Floating Island has no terrain adaptation, Shrine has
beard_box, and the others have beard_thin. Resolved biome sets contain 1/12/41/56/56
biomes, all intersecting only the Overworld runtime possible-biome set. Existing
world observation links remain unchanged.

Desert Ruin, Floating Island and Shrine reference their same-named
explorations:chests tables. Well and Logs have no saved container table references;
that does not imply absence of block salvage. Floating Island uses randomize_stone:
eight ordered 0.05 random stone-match rules yield coal, iron, copper, redstone,
lapis, gold, diamond or emerald ore. These are individual rule inputs, not eight
independent observed 5% yields. Shrine uses randomize_stonebrick, whose captured
StoneBrickAgingProcessor changes stone-brick/masonry states to aged variants.
The other pools use minecraft:empty processors. No processor here adds spawners.

Qualitative discovery descriptions follow the small surface ruins, well, low
logs, shrine and elevated island forms. No viewing distance or safety guarantee
is inferred. Empty authored enemy sources leave conditional natural spawning;
Floating Island also presents access and fall hazards through its elevation.

Seven provider/inventory tests and scoped builder quality checks pass. Only
these five rows and input identity changed; prior Shrine geometry, biomes,
world observations and nonregistry content are unchanged. Inventory matches
`evidence/raw/item8/inventory-explorations-standalone.json`, SHA-256
3ee3f9bef8a1f391f8336285d67e91714234143defb373e9b0cfa4164084ef39.

## Large Oak Tree and Slime Cave completion

After d0693aaa, this batch integrates fourteen descriptions: ten for the tree
and four for the cave. Slime Cave's six earlier entity, marker, loot and placement
answers remain unchanged. No capture, runtime experiment or tool was added.
The earlier cave processor gap is already resolved in explorations-deepslate;
do not reopen it from the dated wording in the original cave capture README.

Existing inventory joins expose full-start-chunk world-bounds observations:
tree footprint 14x15 or 15x14 and height 12; cave footprint 15x15 and height 12.
These values and their exact observation indexes are integrated into the explicit
family attributes, bound to the existing world-bounds artifact hash. They remain
saved piece envelopes with padding, not occupied volume or family-wide extrema.
Tree observations 148,165,169,170 record the mountainous-seed run-a examples;
545,562,566,567 retain their run-b counterparts. Repeated runs are not independent
layout samples. Existing cave observation indexes and all source limitations
remain attached without inventing a frequency denominator.

Tree base is 6x4x5 with a connector to the 15x8x14 top; this confirms why one
component alone would not describe its assembled size. Both pools use vanilla
rigid single elements with minecraft:empty processors. Templates contain only
their jigsaw block entities, with no authored entities, loot references, spawners
or generation markers. The surface-projected tree is an environmental feature;
ordinary biome spawning and ordinary block drops remain separate possibilities.

Both families' resolved biome sets intersect only the Overworld runtime possible
biomes, consistent with the retained saved starts. Tree uses WORLD_SURFACE_WG,
offset zero and beard_thin. The cave's captured generator rejects sea level <=30
or a height span below ten, then selects its below-sea-level start and one rotated
piece. DeepslateProcessor changes stone/mossy cobblestone below Y0 without changing
the envelope or erasing marker/chest metadata. The cave may be exposed by natural
terrain, but neither exposure rate nor a guaranteed surface landmark is claimed.

Eight affected tests in the provider, slime-cave-source and inventory-source
suites pass, along with scoped builder quality checks. Only these two families
and the decisions input hash changed; existing cave source answers, biome and
observation links, and nonregistry content remain unchanged. Inventory matches
`evidence/raw/item8/inventory-explorations-tree-cave.json`, SHA-256
4dc15e0a4513ab56f5794cd7e872131d20d4f29f40e2d1dab0d83f7740920d86.
