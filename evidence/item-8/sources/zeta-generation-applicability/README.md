# Zeta shared generation applicability

Extractor revision: `85cd526bdc275d177944d8b6288386b761ba5e58`.
Exact archive, class and disassembly hashes are in identities.json.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive Zeta-1.1-40.jar \
  --class-name org/violetmoon/zeta/world/generator/multichunk/MultiChunkFeatureGenerator.class \
  --class-name org/violetmoon/zeta/config/type/DimensionConfig.class \
  --output evidence/raw/item8/zeta-generation-applicability-85cd526-reproduction
diff -r --exclude=README.md evidence/item-8/sources/zeta-generation-applicability \
  evidence/raw/item8/zeta-generation-applicability-85cd526-reproduction
```

Fresh reproduction matched exactly before this README was added. Scoped
extractor Ruff and Basedpyright passed.

MultiChunkFeatureGenerator.generateChunk returns for radius <= 0, otherwise
searches source chunks within ceil(radius/16) of the target chunk on both axes,
inclusive. Each candidate source position is that chunk's minimum X/Z and Y=0.
It calls getSourcesInChunk, then generateChunkPart for each returned source with
the original target position. Thus the source search radius is not directly a
block footprint or an unlimited propagation mechanism. Frozen module radii 7
and 15 would each select one neighboring chunk in either direction if bound to
the captured fields. Effective configuration binding and the inherited
Generator.generate/canGenerate dispatch remain separate dependencies.

DimensionConfig.end(false) constructs an allowlist containing minecraft:the_end.
The resource-location overload accepts when list membership differs from
isBlacklist. The LevelAccessor overload returns false unless its argument is a
Level, then checks that Level's dimension. WorldGenRegion is not accepted by
that overload merely by implementing LevelAccessor. Inspect the inherited
Generator caller before deciding whether it unwraps the region or invokes a
different overload; do not infer disabled generation from this method alone.

No observed world result or complete provider disposition is asserted here.
