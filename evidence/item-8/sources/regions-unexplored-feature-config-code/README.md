# Feature predicates and ground-cover state selection

Executed successfully with existing tool `78eca8f`, into an absent directory:

```sh
uv run -m tools.inspect_item8_pool_elements --archive regions-unexplored-0.6.1-neoforge-21.1.jar --class-name net/regions_unexplored/lithostitched/ConfigPredicate.class --class-name net/regions_unexplored/config/state/common/RUCommonConfig.class --class-name net/regions_unexplored/worldgen/stateprovider/RandomizedGroundCoverStateProvider.class --output evidence/item-8/sources/regions-unexplored-feature-config-code
```

The extractor verified the frozen archive. All three disassembly hashes match
the identity records; identities SHA-256:
`1b447725ac61174b8cf0f35ed5457291460c54938c49b9d8296809781a87ba8d`.
Scoped Ruff and basedpyright passed for the tool.

`ConfigPredicate.test` delegates to `RUConfigHandler.COMMON.test(key)`.
`RUCommonConfig.test` recognizes `vanilla_changes/`, removes that 16-character
prefix and reads the matching toggle, defaulting to false for absent keys.
This is the exact predicate shape declared by all 34 selected feature modifiers.

The frozen file `evidence/item-6/frozen/config/regions_unexplored/common.json`
has SHA-256 `300dda462e31f6f1bcce0d67308e4939d1b461a03c8cc92ba805f7ac9d1cb66c`.
The extended reference test checks every declared modifier predicate against
this file and requires the corresponding toggle to be true. It removes only
standalone comment lines from this hash-bound file before parsing JSON.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py
uv run ruff check tests/item8/test_feature_modifier_references.py
uv run basedpyright tests/item8/test_feature_modifier_references.py
```

The focused test passed. The initial Ruff run found one overlong path line,
which was split before the final passing quality check. Predicate truth is not
evidence of successful placement or observed frequency.

`RandomizedGroundCoverStateProvider.getState` takes the configured block's
default state, assigns AMOUNT from 1 through 4, and a random horizontal FACING.
It returns that block state without selecting a different block or adding an
entity, spawner or loot reference. Remaining tree/root/decorator and state
provider contributions must still be reconciled before the combined modifier
disposition update. No new runtime capture or measurement system was added.
