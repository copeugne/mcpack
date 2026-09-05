# Zeta deferred generation and spawn delegation

Extractor revision: `49c9586068103dca0a6ed53906f0863869b28ee2`.
Exact archive, class and disassembly hashes are recorded in identities.json.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive Zeta-1.1-40.jar \
  --class-name org/violetmoon/zeta/world/WorldGenHandler.class \
  --class-name org/violetmoon/zetaimplforge/world/ZetaSpawnModifier.class \
  --output evidence/raw/item8/zeta-generation-spawn-49c9586-reproduction
diff -r --exclude=README.md evidence/item-8/sources/zeta-generation-spawn \
  evidence/raw/item8/zeta-generation-spawn-49c9586-reproduction
```

Fresh reproduction matched exactly before this README was added. Scoped Ruff
and Basedpyright passed for the extractor selection.

WorldGenHandler.register creates one DeferredFeature per Decoration step, wraps
it in a configured feature with NONE configuration and a placed feature with an
empty modifier list, then stores a direct holder in defers. addGenerator stores
module/generator/weight records in a per-step sorted set. generateChunk returns
unless the level is a WorldGenRegion. For each registered generator it requires
the owning module to be enabled and generator.canGenerate(region) to pass before
calling generate. These are consumer-dependent eligibility checks; no specific
End generation or absence can be inferred without the registered consumers.
The optional watchdog path does not need broader operational investigation to
identify those consumers.

ZetaSpawnModifier processes EntitySpawnHandler.trackedSpawnConfigs. A primary
entry requests removal of existing entries of its entity type; a secondary entry
skips that removal. Enabled configurations whose biome predicate passes add their
spawn entry. CostSensitiveEntitySpawnConfig also supplies mob charges outside
that enabled/biome branch. These are biome natural-spawn settings, not physical
spawner blocks or template-authored entities. Actual entity types and affected
biomes depend on consumer registration and frozen configuration, still open.

The ordinary disassembly retains the removal predicate's implementation, but
does not expose invokedynamic bootstrap targets. No acceptance claim here
requires identifying an unrecorded bootstrap target. DeferredFeature execution
and consumer registration remain the next relevant dependencies; no completed
provider or family-attribute claim is made from these library handlers alone.
