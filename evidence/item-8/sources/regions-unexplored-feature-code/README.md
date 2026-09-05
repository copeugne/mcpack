# Regions Unexplored feature implementation inputs

These exact classes supply code missing from the packaged feature documents
referenced by the remaining village/vanilla-biome modifier checks. They are
source inputs to Item 8, not a completed provider disposition or a new runtime
measurement. The existing extractor verified the retained archive identity.
The seven disassembly hashes match `identities.json`, whose SHA-256 is
`d27de44a59aedb2dd41e12dcc0f35db1328207314c8cbe59dae6120de5b9953b`.

Executed successfully with tool `d0043b6`, into an absent output directory:

```sh
uv run -m tools.inspect_item8_pool_elements --archive regions-unexplored-0.6.1-neoforge-21.1.jar --class-name net/regions_unexplored/registry/RUFeatureTypes.class --class-name net/regions_unexplored/world/level/feature/GiantLilyPadFeature.class --class-name net/regions_unexplored/world/level/feature/tree/BambooTreeFeature.class --class-name net/regions_unexplored/world/level/feature/tree/PalmTreeFeature.class --class-name net/regions_unexplored/world/level/feature/tree/SaguaroCactusFeature.class --class-name net/regions_unexplored/worldgen/rootplacer/WillowRootPlacer.class --class-name net/regions_unexplored/worldgen/rulesource/ConfigRuleSource.class --output evidence/item-8/sources/regions-unexplored-feature-code
```

Scoped Ruff and basedpyright passed. Full class disassemblies are kept together
as one generated source increment so the bodies and registration remain
reviewable, rather than retaining only favorable excerpts. No binaries or
worlds are included.

`RUFeatureTypes` binds `giant_lily` to `GiantLilyPadFeature`. Its `place` method
checks water below and air at the origin, south, south-west and west positions.
If those checks pass, it attempts four `GIANT_LILY_PAD` block writes with north,
east, south and west facing states respectively. It returns false even after
those writes. Preserve this distinction: a false placement result is not proof
of absent generated blocks. No frozen artifact was modified to repair it.

`ConfigRuleSource.apply` selects its `onEnabled` or `onDisabled` rule using
`RUCommonConfig.test(key)` and delegates to that rule. This does not itself
establish the effective setting or close referenced rule bodies.

The tree and root-placer bodies are retained for continued content inspection.
Their inclusion is not yet an accepted absence-of-structures claim. Complete
the placed/configured feature references, custom implementation attribution and
platform hook checks before resolving the machine-readable modifier entries.
