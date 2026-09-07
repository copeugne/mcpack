# Feature modifier and surface-rule implementation inputs

These seven exact classes continue the existing Item 8 source inspection.
The extractor verified the frozen Lithostitched archive. Disassembly hashes
match `identities.json`, whose SHA-256 is
`b7138be0cec7822f8e4fb19c6c9175e3ac1ba7ab174cb58015c34be488b9aaa1`.

Executed successfully with tool `d0043b6`, into an absent output directory:

```sh
uv run -m tools.inspect_item8_pool_elements --archive lithostitched-1.7.10+beta4-neoforge-21.1.jar --class-name dev/worldgen/lithostitched/impl/worldgen/modifier/AddFeaturesModifier.class --class-name dev/worldgen/lithostitched/impl/worldgen/modifier/RemoveFeaturesModifier.class --class-name dev/worldgen/lithostitched/impl/worldgen/surface/rule/ReferenceRule.class --class-name dev/worldgen/lithostitched/worldgen/feature/CompositeFeature.class --class-name dev/worldgen/lithostitched/worldgen/feature/WeightedSelectorFeature.class --class-name dev/worldgen/lithostitched/worldgen/feature/config/WeightedSelectorConfig.class --class-name dev/worldgen/lithostitched/worldgen/modifier/AddSurfaceRuleModifier.class --output evidence/item-8/sources/lithostitched-feature-modifier-code
```

Scoped Ruff and basedpyright passed. This generated source increment retains
the complete inspected classes, not another measurement framework or runtime
capture. Packaged references and runtime applicability remain separate checks.

`WeightedSelectorConfig` decodes a weighted list of placed-feature holders.
`WeightedSelectorFeature.place` selects a holder and invokes its placed feature,
returning false for an empty selection. `CompositeFeature.place` visits its
configured holders and consults `placementType.shouldContinue` after each
placement result. Preserve the original configuration and branching; these
methods do not establish probabilities or successful world placement.

`ReferenceRule.apply` returns a single referenced rule directly or constructs a
surface-rule sequence from multiple references. `AddSurfaceRuleModifier.apply`
is empty, so that method alone cannot establish that the injection is inactive.
`AddFeaturesModifier.apply` returns immediately outside Fabric; its separate
`createNeoforgeModifier` constructs NeoForge's `AddFeaturesBiomeModifier` with
the declared biomes, features and generation step. The platform dispatch must
be followed before making an effective-modifier claim.

Next implementation references located in the same frozen archive are
`dev/worldgen/lithostitched/mixin/common/ServerLifecycleHooksMixin`,
`impl/worldgen/modifier/NeoforgeModifierHolder`, and
`worldgen/surface/SurfaceRuleManager`. They have not yet been retained or
inspected here. The current machine-readable modifier entries remain open.

## Packaged feature reference closure

Source check `a774424` follows all 30 selected feature additions and four
removals, using the existing resource selector on the pinned packaged catalog.
All are Regions Unexplored modifiers. Their references resolve to 34 named
placed features and 41 named configured features, with inline features also
traversed. Patch/flower, weighted-selector, composite and random-selector
branches are followed, including weighted entries and selector defaults.
The six implementation endpoints are `minecraft:simple_block`, `minecraft:tree`,
`regions_unexplored:saguaro_cactus`, `regions_unexplored:palm_tree`,
`regions_unexplored:bamboo_tree`, and `regions_unexplored:giant_lily`.

Executed successfully:

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_surface_rule_contribution.py tests/item8/test_resource_selection.py
uv run ruff check src/mcpack_evidence/item8_resource_selection.py tests/item8/test_feature_modifier_references.py
uv run basedpyright src/mcpack_evidence/item8_resource_selection.py tests/item8/test_feature_modifier_references.py
```

Ten tests and scoped checks passed. Ruff's initial complexity/statement findings
were resolved by documenting a local exemption for the single frozen-grammar
proof, avoiding a new traversal framework. No behavior was changed for that
exemption. The trace covers potential references regardless of configuration
activation. Counts describe referenced resources, not families or placements.
The implementation endpoints, their state providers/decorators and effective
config predicates still need final contribution dispositions. This check does
not establish absent enemies or loot merely from generator names.

The platform follow-up above is superseded by the delivered source under
`../lithostitched-platform-modifier-code` and
`../lithostitched-surface-lifecycle-code`; its README records dispatch and
surface-rule closure. No further platform recapture is needed.
