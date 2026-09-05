# Conditional village additions: source inspection

The existing pool trace omitted packaged Lithostitched pool additions. Item 8
requires Village Taverns and CTOV contributions, so their loading conditions
must be resolved before adding their templates to the village families.
This is source inspection using the existing tool, not a new measurement system.

Reproduce from tool commit `7ca24fd` into absent output directories:

```sh
uv run -m tools.inspect_item8_pool_elements --archive lithostitched-1.7.10+beta4-neoforge-21.1.jar --output evidence/item-8/sources/lithostitched-pool-additions-code
uv run -m tools.inspect_item8_pool_elements --archive neoforge-21.1.249-universal.jar --output evidence/item-8/sources/neoforge-condition-code
uv run -m tools.inspect_item8_pool_elements --archive neoforge-21.1.249-server.jar --output evidence/item-8/sources/neoforge-registry-loading-code
```

All three commands succeeded. The six prior Lithostitched disassemblies were
byte-identical; only the manager and priority interface were added there.
Whole-class disassembly is retained so the evidence is reproducible without
hand-selected method excerpts. The patched server hash is also recorded in
`evidence/item-2/baseline-manifest.json`. The unpatched mapped Minecraft JAR
does not contain NeoForge's conditional-loading hook.

The patched `RegistryDataLoader.loadElementFromResource` wraps decoding with
`ConditionalOps.createConditionalCodec`, registering only present results.
`ConditionalOps` defaults to `neoforge:conditions`. Its decoder requires all
conditions to pass. `ModLoadedCondition.test` calls `ModList.isLoaded`;
`OrCondition.test` succeeds when any child succeeds. These are code semantics,
not a claim that every packaged modifier was registered in the captured run.

Lithostitched's manager gathers registry modifiers and event additions, then
sorts by priority. The default addition priority is 1000. The addition codec
and application code are retained in `lithostitched-pool-additions-code`.
Filtering against the frozen loaded-mod identity and integrating the applicable
additions into the trace remain outstanding. Equal-priority order must not be
claimed from lexicographic source order. Other runtime pool changes remain open.

The initial patched-server selector also emitted an unrelated StructureTemplate
class. That output is retained locally in the ignored
`evidence/raw/item8/neoforge-registry-loading-initial` directory and is not
acceptance evidence. The selector was narrowed and the accepted output rerun.
