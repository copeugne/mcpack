# NeoForge modifier dispatch and surface application

The three exact classes here were extracted with tool `59df00e`; the three
companion classes under `../lithostitched-surface-lifecycle-code` were extracted
with `643c1d4`. They close the dispatch question raised by the empty/Fabric-only
entry points in the earlier feature-modifier source inspection.

Executed successfully, into absent output directories:

```sh
uv run -m tools.inspect_item8_pool_elements --archive lithostitched-1.7.10+beta4-neoforge-21.1.jar --class-name dev/worldgen/lithostitched/mixin/common/ServerLifecycleHooksMixin.class --class-name dev/worldgen/lithostitched/impl/worldgen/modifier/NeoforgeModifierHolder.class --class-name dev/worldgen/lithostitched/worldgen/surface/SurfaceRuleManager.class --output evidence/item-8/sources/lithostitched-platform-modifier-code
uv run -m tools.inspect_item8_pool_elements --archive lithostitched-1.7.10+beta4-neoforge-21.1.jar --class-name dev/worldgen/lithostitched/impl/LithostitchedInternalHooks.class --class-name dev/worldgen/lithostitched/mixin/server/DedicatedServerMixin.class --class-name dev/worldgen/lithostitched/impl/worldgen/surface/rule/TransientMergedRule.class --output evidence/item-8/sources/lithostitched-surface-lifecycle-code
```

The extractor verified the frozen archive before reading classes. All six
disassembly hashes match their identity records. Scoped Ruff and basedpyright
passed. Identity SHA-256 values are
`b9705872460fd2c8aac838cfc70780fc4085700ab1aaa92b9ca66fb4ba3f52d5`
for platform dispatch and
`ed1f626e586466a933457e0bc18859254fc483cd062e4c359d58f6e8aa084885`
for the companion lifecycle source. Complete class bodies are preserved as
one generated dispatch-evidence increment. No new measurement system is used.

`ServerLifecycleHooksMixin` modifies the list stored in NeoForge's
`ServerLifecycleHooks.runModifiers`. It copies that list, obtains Lithostitched
modifiers from `ModifierManager.getAllModifiers`, selects instances of
`NeoforgeModifierHolder`, and appends each `createNeoforgeModifier()` result.
The previously retained add/remove feature classes provide that conversion.
The Fabric-only `apply` path therefore does not establish inactivity on
NeoForge. The preserved runtime debug log at line 13027 records this mixin
being applied to NeoForge's lifecycle class.

`DedicatedServerMixin` injects into `initServer` immediately before
`DedicatedServer.loadLevel`. It calls `LithostitchedInternalHooks`, which calls
`ModifierManager.applyModifiers` and then `SurfaceRuleManager.applySurfaceRules`.
The preserved debug log at line 12905 records the dedicated-server mixin being
applied; nearby callback transformation diagnostics remain in the raw log.

`SurfaceRuleManager` obtains add-surface-rule modifiers, groups them by target
dimension and handles noise-based chunk generators. It retains the original
noise settings, default block/fluid, noise router, spawn target, sea level and
generation flags while substituting merged surface rules. It sorts additions
by priority, places PREPEND rules before the original and APPEND rules after it.
It calls `LithostitchedVersion.handleRuleMerging`, already retained under
`../lithostitched-processor-registration-code`. That method creates or extends
a `TransientMergedRule`; the companion class retains and applies the rules.

Runtime log: `evidence/raw/item8/registry-r1/debug.log`, SHA-256
`e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b`,
restored through the existing Item 8 registry raw-custody records. The log also
retains the Mixin class-version diagnostics. These lines establish mixin
application, not observed feature placement or an independently dumped final
surface-rule tree. The latter is not claimed here.

The selected Regions Unexplored surface modifier declares PREPEND for the
Overworld. Its referenced rule bodies and the feature modifiers' configuration
predicates still require disposition before the combined machine-readable
update. Do not infer inactive modifiers from their no-op direct methods, or
claim complete provider coverage from this dispatch evidence alone.
