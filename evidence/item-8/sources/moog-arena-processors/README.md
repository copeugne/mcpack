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
manager was captured there as well. Reuse it rather than extracting again.

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
