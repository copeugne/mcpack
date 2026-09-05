# Zeta biome modifier implementation

Extractor revision: `8849e7e558e51594348268aee16799dffcb24b14`.
Exact archive, class and disassembly identities are in identities.json.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive Zeta-1.1-40.jar \
  --class-name org/violetmoon/zetaimplforge/world/ZetaBiomeModifier.class \
  --output evidence/raw/item8/zeta-biome-modifier-8849e7e-reproduction
diff -r --exclude=README.md evidence/item-8/sources/zeta-biome-modifier \
  evidence/raw/item8/zeta-biome-modifier-8849e7e-reproduction
```

Fresh reproduction matched exactly before this README was added. Scoped Ruff
and Basedpyright passed for the extractor selection.

The static RESOURCE is zeta:biome_modifier, matching the packaged JSON type.
modify acts only during ADD. It calls modifyBiome, then iterates ZetaList's
instances and delegates entity spawning to ZetaSpawnModifier with each
instance's EntitySpawnHandler. modifyBiome loops all Decoration values and
appends WorldGenHandler.defers.get(step) to each generation feature list.
It neither filters biomes nor directly removes existing features in this method.

This resolves the immediate modifier's mutation: deferred feature additions
and a separate spawn delegation. It does not resolve the deferred generators or
spawn rules. WorldGenHandler and ZetaSpawnModifier are the concrete next source
dependencies if needed for effective feature and natural-mob attribution.
No End-specific change, actual callback execution or complete Zeta provider
coverage is inferred from the modifier alone.
