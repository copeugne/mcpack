# Zeta inherited generator dispatch

Extractor revision: `307574d6730e20bbfff6e9ca60dfdc3808ff9bd5`.
Exact archive, class and disassembly hashes are in identities.json.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive Zeta-1.1-40.jar \
  --class-name org/violetmoon/zeta/world/generator/Generator.class \
  --output evidence/raw/item8/zeta-generator-dispatch-307574d-reproduction
diff -r --exclude=README.md evidence/item-8/sources/zeta-generator-dispatch \
  evidence/raw/item8/zeta-generator-dispatch-307574d-reproduction
```

Fresh reproduction matched exactly before this README was added. Scoped
extractor Ruff and Basedpyright passed.

canGenerate evaluates the supplied BooleanSupplier and then calls
DimensionConfig.canSpawnHere with ServerLevelAccessor.getLevel(), which returns
the backing ServerLevel. Thus the previously inspected Level-specific check
does not reject the WorldGenRegion path on account of its wrapper type.
generate sets the feature seed, calls the virtual generateChunk with the same
region, chunk generator and origin, and returns the incremented feature index.
For the two captured Quark subclasses, this dispatch reaches the inspected
MultiChunkFeatureGenerator.generateChunk implementation.

getBiome with its boolean argument true samples at the supplied X/Z and
maxBuildHeight-1; false samples at the supplied position. Chorus Vegetation's
true calls therefore use the top-of-build-height biome, whereas Spiral Spire's
false call uses its supplied sample height. These are source-defined biome
queries, not observed biome membership at generated structures.

This completes the direct inherited dispatch and dimension-unwrapping link.
Consumer configuration binding and generated-world attribution remain separate.
