# Moog arena processor attribution

This source increment resolves a concrete Item 8 boundary: arena templates have
empty ordinary/trial spawner entity fields and omitted vault loot fields that
are populated by selected processor lists. Large and Dragon Arena also have
pillar processing that extends outside nominal template boxes. Treating raw
fields as unknown effective mobs, or template height as the full placed height,
would misstate the required inventory. The existing extractor captures five
implementation classes; no new measurement system, runtime capture or validator.
The same processor path is used by the pending Mega Fortress assessment.

The identities manifest SHA-256 is
9cee936ea43986ec9d79f979e1f49c9dd220fc8d9c07da90131cba33cb21c5e2.
It binds complete disassemblies and class hashes to the retained
moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar, SHA-256
9cdb525229470ac7801cc2ed74912eca610daa1d2bde10bf6afaf53c1afe66db.
Registration is already preserved in moog-provider-entries, and the trial config
manager was captured in moog-provider-callbacks. Reuse it rather than extracting again.

Reproduction command (use an absent output directory):

```sh
uv run -m tools.inspect_item8_pool_elements --archive moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar --class-name com/finndog/moogs_structures/world/processors/PillarProcessor.class --class-name com/finndog/moogs_structures/world/processors/SpawnerRandomizingProcessor.class --class-name 'com/finndog/moogs_structures/world/processors/SpawnerRandomizingProcessor$WeightedEntity.class' --class-name com/finndog/moogs_structures/world/processors/TrialSpawnerRandomizingProcessor.class --class-name com/finndog/moogs_structures/world/processors/VaultRandomizingProcessor.class --output evidence/item-8/sources/moog-arena-processors
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Extraction and both scoped checks passed. No changes to extraction behavior,
only five class names added to the existing allowed set.

Direct source findings:

- SpawnerRandomizingProcessor.processBlock handles SpawnerBlock and calls
  buildSpawnerNbt with placement-position random. It replaces the source NBT
  with its selected weighted entity and configured parameters; an empty or
  unselectable list instead uses replacementState. Raw empty SpawnData is not
  evidence of an unassigned effective spawner when this processor applies.
- TrialSpawnerRandomizingProcessor.processBlock handles TrialSpawnerBlock,
  clears saved server/shared/spawn/cooldown state, obtains normal and optional
  ominous configs from TrialSpawnerConfigManager and writes copies into NBT.
  Missing normal configuration logs a warning. Packaged config existence and
  manager loading remain distinct from observed activation.
- VaultRandomizingProcessor.processBlock reads the block's OMINOUS property,
  selects the configured ordinary/ominous table and key, clears server/shared
  data and replaces config.loot_table and config.key_item. Preserved raw vault
  table omissions do not establish effective default loot when it applies.
- PillarProcessor.processBlock matches a trigger state, replaces the original
  marker, checks WorldGenRegion chunk ownership, and handles downward terrain
  contact. Its loop checks obstruction, ground Y, build height and distance
  from the trigger against pillarLength. Declared length 128 is a bound, not
  an observed extension. Its selected direction is down, preserving horizontal
  footprint while making full vertical extent terrain-dependent.

Relevant packaged resources, all in packaged-json-redacted.json.gz:

- data/mns/worldgen/processor_list/small_arena_spawners.json: ordinary
  zombified_piglin/magma_cube/skeleton weights 5/3/2.
- data/mns/worldgen/processor_list/large_arena_pillars.json: down pillars,
  ordinary wither_skeleton/skeleton weights 3/2, normal/ominous trial configs
  under mns:large_arena, and main/main_ominous vault tables.
- data/mns/worldgen/processor_list/dragon_arena_pillars.json: down pillars,
  ordinary wither_skeleton/blaze/magma_cube weights 6/3/3, trial configs under
  mns:dragon_arena and main/main_ominous vault tables.
- data/mns/trial_spawner/{large_arena,dragon_arena}/{normal,ominous}.json:
  explicit spawn potentials and reward-key tables. Dragon normal includes
  Size-2 magma_cube; its ominous config includes breeze. Large configs retain
  equipped wither_skeleton/skeleton variants. Weights and count parameters
  are source settings, not observed frequencies or simultaneous populations.

Next integrate these facts, exact pool-to-processor ownership, fixed payloads
and finite connector geometry into Arena/Dragon attributes. There are 36 unique
selected templates across those two families, including three shared mob pieces.
Small Arena uses middle as its start, Large Arena r1, Dragon Arena head.
Mob templates occupy 1x3x1 or 1x4x1 source boxes and are optional attachments,
not additional canonical families. Keep source-authored health/equipment,
conditional dispensers, books and archaeology payloads distinct from live
encounters, functioning recipes and loot-table rolls. Do not count these two
families as assessed until integration and focused validation are finished.

## Arena and Dragon inventory integration

The following direct derivation integrates two families after the processor
capture. Use exact selected templates in pool-traces-content.json.gz and their
source NBT paths from MoogsNetherStructures-1.21-3.0.0-alpha.2.jar in
templates-redacted.json.gz. The authoritative family evidence maps bind hashes.
Architectural pools select one rigid weight-1 element with empty fallback.
Large Arena architecture selects original 1.21-1.21.3 paths; mob pools select
1.21 paths via their 1.21-1.21.4 mappings. The 36 unique templates include three
shared mob pieces, which are not extra families.

Put each root's initial architecture at (0,0,0). Align opposing jigsaw fronts
and their top orientation; child origin equals parent origin plus outgoing
position plus outward unit vector minus incoming position. Architectural
orientations need no relative rotation. Direct component origins and sizes:

| Root/component | Origin XYZ | Size XYZ |
| --- | --- | --- |
| small/middle | 0,0,0 | 48,18,48 |
| small/front | 16,0,-41 | 24,18,41 |
| small/left | 48,0,0 | 8,16,48 |
| small/back | 11,0,48 | 34,12,4 |
| large/r1 | 0,0,0 | 31,47,48 |
| large/r2 | 0,0,48 | 31,47,23 |
| large/r3 | 0,0,71 | 31,47,28 |
| large/l1 | 31,0,0 | 31,47,48 |
| large/l2 | 31,0,48 | 31,47,23 |
| large/l3 | 31,0,71 | 31,47,28 |
| dragon/head | 0,0,0 | 48,41,47 |
| dragon/c1 | 48,0,0 | 21,35,47 |
| dragon/c2 | 69,0,0 | 48,31,47 |
| dragon/l1 | 37,0,-24 | 48,24,24 |
| dragon/l2 | 85,0,-26 | 13,19,26 |
| dragon/r1 | 19,0,47 | 48,22,44 |
| dragon/r2 | 67,0,47 | 43,25,35 |
| dragon/lower_1 | -12,-4,-3 | 48,4,48 |
| dragon/lower_2 | 6,-4,45 | 30,4,9 |
| dragon/lower_3 | 8,-4,54 | 48,4,40 |
| dragon/lower_4 | 56,-4,46 | 38,4,48 |
| dragon/lower_5 | 94,-4,28 | 17,4,48 |
| dragon/lower_6 | 111,-4,12 | 6,4,29 |
| dragon/lower_7 | 94,-4,-12 | 17,4,40 |
| dragon/lower_8 | 63,-4,-26 | 38,4,14 |
| dragon/lower_9 | 46,-4,-12 | 48,4,48 |
| dragon/lower_10 | 36,-4,36 | 20,4,18 |
| dragon/lower_11 | 56,-4,36 | 38,4,10 |
| dragon/lower_12 | 18,-4,-12 | 28,4,9 |
| dragon/lower_13 | 36,-4,-3 | 10,4,39 |

Examples: Small middle (28,2,0) north matches front (12,2,40) south;
Large r1 (30,3,0) east matches l1 (0,3,0) west. Dragon head (47,1,32) east
matches c1 (0,1,32) west, c1 (3,2,0) north matches l1 (14,2,23) south,
and head (1,0,26) down_east matches lower_1 (13,3,29) up_east.
The remaining edges follow their exact named component targets in source NBT.
Optional mob pieces are 1x3x1 or 1x4x1 and attach one block above their receiver;
all possible receiver boxes fit within the architecture's overall envelope,
including rotation about their single-column footprints.

Inclusive architectural unions: Small (0,0,-41)..(55,17,51), 56x18x93;
Large (0,0,0)..(61,46,98), 62x47x99;
Dragon (-12,-4,-26)..(116,40,93), 129x45x120.
These include air/padding and assume successful attachments. Large/Dragon
pillars extend down conditionally, bounded by the captured processor; do not
present architectural height as full placed height. Source pillar_length 128
is not observed extension. Enhanced terrain adaptation is likewise separate
from architectural footprint, and whole-structure rotation can exchange X/Z.

All Small architectural pieces use small_arena_spawners; all Large architectural
pieces use large_arena_pillars. Dragon's seven upper pieces use
dragon_arena_pillars; its thirteen lower pieces and all mob templates use empty
processors. Thus Small's eight ordinary blocks, Large's 22 ordinary/four trial,
and Dragon's ten ordinary/three trial blocks get the applicable source
assignments despite raw empty entity fields. Normal/ominous trial configs are
preserved in full with their mob equipment, weights and reward tables. The
manager's existing callback disassembly establishes JSON-to-NBT loading from
trial_spawner resources. This is source attribution, not live activation.

mob_any weights are Bowman 3, Vanguard 3, Sentinel 2. Dedicated receivers choose
Pit Brute (Small), Arena Gladiator (Large), or Drakebone Tyrant (Dragon).
Saved health values are 35, 45, 40, 50, 90 and 160 respectively; equipment and
PersistenceRequired are retained as saved source payloads. They do not prove
runtime attribute interpretation, encounter balance or drop yield. Dragon
architecture and lore do not establish an Ender Dragon entity.

Processor-configured Large/Dragon vault main/main_ominous and trial reward-key
tables are integrated alongside template-owned chest refs. Fixed payloads remain
separate: Small's two five-potion harming dispensers and two 64-arrow dispensers;
Large's paired weakness/harming dispensers, dropper blocks and saved journal;
Dragon's framed book. Large r1's eleven brushable blocks have no item/table
payload. Books are authored lore, not executable recipe/ritual evidence.

Runtime biome intersections identify only Nether. Small uses LOWEST_LAND,
liquid exclusion and beard_box. Large/Dragon use fixed heights 35/31 and their
explicit enhanced carve/bury settings, plus conditional down pillars. These
source inputs support qualitative visibility, not measured exposure or
traversability. No runtime capture or new measurement was required.

Rebuild: `uv run -m tools.build_item8_inventory --output <absent-path>`.
Shared checks: `uv run pytest -q tests/item8/test_moog_data_provider_scope.py tests/item8/test_moog_library_provider_scope.py tests/item8/test_inventory_sources.py`.

Integration validation: all ten shared tests pass. Rebuilt inventory SHA-256:
`4c5eb68aa0ac4f2151935ce30d0666f81c2ee4f269ba073569096b42ad8773ea`.
Semantic comparison changes only Arena/Dragon family rows and the decisions input
pin; unrelated rows, registry identities, biomes and observations are preserved.

## Mega Fortress integration

The same preserved pillar and ordinary spawner implementations support the
Mega Fortress assessment, without another capture or tool. Exact source JSON
paths are data/mns/worldgen/processor_list/{pillars,pillars_armored,pillars_blaze}.json
in the retained Nether Structures archive. The first two assign equal-weight
wither skeleton/blaze/skeleton spawners; the third assigns blaze only. Each
uses nearby 6, delay 200..800, player range 16, count 4 and spawn range 4.
The three selected spawners/spawner_{end_1,side_1,side_2} templates use
pillars_blaze. The root center uses pillars_armored. Other selected spawner
pieces use pillars. Raw source spawner IDs do not supersede those processors.

The full selected template list and exact NBT identities already exist in
pool-traces-content.json.gz under structures[mns:mega_fortress]. Its 196
components remain one branching family. Mob pool JSON selects six versioned
1.21 mob templates, separately from ordinary spawners and the root's explicit
piece-bounded natural spawn override. Armor-stand sets in pillars_armored are
recorded as declared configuration, not proven placed equipment or recoverable
loot. Empty-metadata SAVE structure blocks do not author additional enemies.
Per-template loot references remain authoritative; fixed payloads additionally
include central-room tipped-arrow dispensers (block_entities 2/3), eastern-room
potion dispensers, northern-room arrow dispensers and journal, and the fork's
framed note. Their exact selected NBT paths are recorded in the family assessment.

Existing world-bounds observations 29/441 are repeated run-a/run-b records of
seed 42, Nether start chunk (16,20), source ordinary/chunks.jsonl line 2637.
Both have structure_starts status, not full placement. Their planned envelope
[128,19,193,384,74,452] gives inclusive dimensions 257x56x260 by subtracting each
minimum from its corresponding maximum and adding one. This supports the
required approximate architectural size with an explicit lifecycle boundary;
it does not prove finished blocks, two independent sites or size distribution.
Down pillars (configured length 128), up chains (40) and terrain carving are
separate conditional effects. Boundary-exempt end pools prevent treating the
configured 128 center distance as a strict whole-layout cap. No additional
experiment is needed to report this approximate layout and its limits.

All ten shared tests pass. The final direct attribution correction adds the
central-room dispenser reference only; rebuilding changes only Mega Fortress
and the decisions input pin. Inventory SHA-256: `af5a9899efe6ed451a87a6c60817d421ffb0a75d3bfe3970df7d090273859737`.
