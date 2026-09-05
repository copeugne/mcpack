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

## Selected feature-modifier contribution disposition

The existing reference test now checks the terminal configuration components
and block identifiers as well as the complete feature graph and enabled config
predicates. It binds all 34 modifiers to 34 placed and 41 configured features.
Terminal configurations contain 11 component types and 44 configured block
identifiers, explicitly listed in `tests/item8/test_feature_modifier_references.py`.
This count excludes additional blocks selected directly in generator code and
does not describe observed placements, structure families or the whole mod.

The vanilla tree configurations use straight trunks, blob/pine foliage,
ordinary dirt/log/leaf providers, and only `minecraft:leave_vine` decoration.
The custom willow root placer checks candidate positions and delegates root
placement using the configured block provider. The palm, bamboo and saguaro
implementations build their geometry through block-state reads and writes,
replaceability checks and their local placement methods. Their configured
providers supply plant/log/leaf blocks. Additional fixed block references are
soil variants, podzol, hanging roots and saguaro cactus. There is no template,
structure pool, entity-spawn, spawner-NBT or loot-table generation in these
implementation paths. Palm branch-mode checks constrain branch placement;
they do not introduce a separate content source. Some methods construct
`java.util.Random`, so this inspection makes no reproducibility or frequency
claim about their placement geometry.

Simple-block features cover grasses, flowers, shrubs, lilies, bioshrooms and
ash vents. The custom ground-cover provider, retained under
`../regions-unexplored-feature-config-code`, varies the configured block's
amount and facing. The random-block provider under
`../lithostitched-random-block-code` chooses a configured block's default state.
Neither adds an authored entity, spawner or loot reference. The giant-lily
return-value limitation described above remains part of this disposition.

Together, these 30 additions and four removals contribute vegetation and
ground-cover/ash-vent features to existing biomes. They add no canonical
structure family: these paths place individual plants or tree geometry rather
than a distinct structure layout. They must remain attributed to Regions
Unexplored as non-family content rather than silently omitted or counted as
34 families. The disposition covers these selected modifiers only; other mod
hooks, providers and the broader Item 8 inventory remain separate work.

Executed successfully:

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py
uv run ruff check tests/item8/test_feature_modifier_references.py
uv run basedpyright tests/item8/test_feature_modifier_references.py
```

The focused test and scoped checks passed. Apply these feature dispositions
with the completed compiler, street-processor and surface-rule checks in the
combined machine-readable update. No placement simulator is needed for this
source contribution claim.
