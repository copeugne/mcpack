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
