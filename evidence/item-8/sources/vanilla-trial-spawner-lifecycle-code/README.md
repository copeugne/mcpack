# Trial-spawner initial lifecycle attribution

This completes the vanilla-source explanation of the five omitted ominous
potential lists investigated in `../vanilla-trial-spawner-code/README.md`.
It uses the existing extractor and frozen template catalog. No new measurement
system, simulation, world generation, or encounter-frequency model was added.

Tool change: `2c43578`. Generated evidence: `bb9582a`. Catalog check: `c5531da`.
Manifest SHA-256:
`658728eebd2eec80ac69ecf077c4ca305efa3102a3f4d2b2c9655ca95d962aab`.
The manifest binds the complete class disassembly to the frozen mapped-server
archive. Companion selection-code manifest SHA-256:
`aa43a73247921fd7ece2e3a71d811c0bddba492a6ea04e198825fc111082449e`.

Executed commands:

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/block/entity/trialspawner/TrialSpawnerState.class --output evidence/item-8/sources/vanilla-trial-spawner-lifecycle-code
uv run pytest -q tests/item8/test_template_nbt.py
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
uv run ruff check tests/item8/test_template_nbt.py
uv run basedpyright tests/item8/test_template_nbt.py
```

The two files received the listed scoped checks separately; both passed.
The final focused test run passed all 10 tests. An initial assertion incorrectly
expected one normal potential entry per template. It failed on slime, whose
two entries use the same entity ID with distinct Size values. The corrected
check preserves both entries exactly rather than changing the source data.

## Conditional mob attribution

The hash-bound catalog test verifies that each of the five templates has
`ominous=false`, `trial_spawner_state=waiting_for_players`, no saved `spawn_data`,
and exactly one distinct normal-mode entity ID among positive-weight entries.
The template catalog SHA is
`b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705`.

`TrialSpawnerState.tickAndGetNext` dispatches ordinal 1 to WAITING_FOR_PLAYERS.
When spawning is allowed, offsets 106 through 116 invoke `hasMobToSpawn` before
offset 130 invokes `tryDetectPlayers`. The companion `TrialSpawnerData` source
shows that `hasMobToSpawn` first calls `getOrCreateNextSpawnData`. Thus the
initial non-ominous configuration supplies next-spawn data before player
detection can trigger `applyOminous` through `lambda$tryDetectPlayers$8`.
The already inspected ominous transition retains that data for an empty list.

Under this unmodified packaged initial state and vanilla lifecycle, the retained
entity IDs are:

| Template suffix under `minecraft:trial_chambers/spawner/` | Retained entity ID |
| --- | --- |
| `breeze/breeze` | `minecraft:breeze` |
| `melee/spider` | `minecraft:spider` |
| `small_melee/cave_spider` | `minecraft:cave_spider` |
| `small_melee/silverfish` | `minecraft:silverfish` |
| `small_melee/slime` | `minecraft:slime` |

Slime's preserved normal entries have Size 1 with weight 3 and Size 2 with
weight 1. These are configuration weights, not measured encounter frequencies.
The selected spawn data, including its size, is retained on this transition.

This closes the initial-state attribution question for the vanilla source path.
It does not claim that a missing ominous list is copied from the normal list,
that arbitrary saved or command-modified states behave identically, or that
retained mods cannot transform this path. The existing inventory's raw
`unresolved_sources` entries still identify absent explicit ominous lists;
this conditional disposition must accompany them when the final effective
family attributes are assembled. Do not repeat this lifecycle extraction or
build a simulator to reproduce the same source-derived attribution.
