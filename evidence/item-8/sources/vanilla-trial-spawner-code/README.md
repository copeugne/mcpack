# Vanilla trial-spawner selection

This source inspection addresses the five preserved vanilla templates whose
inline ominous configuration omits `spawn_potentials`. It uses the existing
extractor, not a new measurement system or runtime experiment. Extraction tool
change: `ed49f84`. Generated evidence: `776dcdb`.

Identities manifest SHA-256:
`aa43a73247921fd7ece2e3a71d811c0bddba492a6ea04e198825fc111082449e`.
The manifest binds each complete disassembly and class to mapped Minecraft server
archive SHA-256 `26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.

Executed extraction, using the pinned Temurin javap selected by the tool:

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/block/entity/trialspawner/TrialSpawner.class --class-name net/minecraft/world/level/block/entity/trialspawner/TrialSpawnerConfig.class --class-name net/minecraft/world/level/block/entity/trialspawner/TrialSpawnerData.class --output evidence/item-8/sources/vanilla-trial-spawner-code
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Extraction and both scoped checks passed. For reproduction, choose a new output
directory; the existing extractor refuses to overwrite evidence. The earlier
two-class exploratory extraction remains in
`evidence/raw/item8/trial-spawner-code-pilot`; it did not contain the data-selection
method and was not sufficient for a selection claim.

## Selection rule established by source

- `TrialSpawnerConfig.lambda$static$0`, bytecode offsets 182 through 200:
  `spawn_potentials` uses the spawn-data list codec with an empty weighted list
  as its lenient optional-field default. An omitted list therefore decodes empty.
- `TrialSpawner.getConfig`, offsets 0 through 18: `isOminous` selects the ominous
  or normal configuration. The codec and constructor preserve two configurations;
  there is no unconditional copy of normal potentials into ominous potentials.
- `TrialSpawnerData.resetAfterBecomingOminous`, offsets 36 through 56: it clears
  `nextSpawnData` only when the ominous potential list is nonempty. An empty list
  preserves the existing next-spawn data during this transition.
- `TrialSpawnerData.getOrCreateNextSpawnData`, offsets 0 through 92: an existing
  next-spawn value is returned first. Otherwise the selected configuration's
  nonempty list is sampled. For an empty list the method retains the existing
  optional value and takes the supplier path if it is absent.
- `TrialSpawnerData.reset`, offsets 33 through 37, clears next-spawn data. Thus
  a prior value cannot be assumed across every lifecycle transition.

For breeze, spider, cave spider, silverfish and slime, the missing ominous list
does not establish either a missing mob definition or a normal-list copy. The
source establishes preservation of existing next-spawn data on the ominous
transition. The exact resulting entity depends on that data and the preceding
lifecycle. This is a source-derived conditional behavior, not an observed spawn.

## Remaining boundary

The working inventory still conservatively records these five omitted lists in
`unresolved_sources`. This evidence explains their selection semantics, but does
not yet bind a lifecycle-derived entity set or audit mod transformations of these
classes. Do not silently replace the five entries with normal-mode mob IDs.
No spawn counts, encounter frequencies, successful world placement, or completed
Item 8 gate are claimed. The current trace and inventory identities are unchanged.
