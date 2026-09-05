# Zeta deferred feature execution link

Extractor revision: `d554c8d9002a1d13b3b84e5065e4e9b455cc654a`.
Exact identities are in identities.json. Fresh reproduction matched exactly
before this README was added; scoped extractor Ruff/Basedpyright passed.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive Zeta-1.1-40.jar \
  --class-name org/violetmoon/zeta/world/DeferredFeature.class \
  --output evidence/raw/item8/zeta-deferred-feature-d554c8d-reproduction
diff -r --exclude=README.md evidence/item-8/sources/zeta-deferred-feature \
  evidence/raw/item8/zeta-deferred-feature-d554c8d-reproduction
```

The constructor stores its Decoration stage. place(context) forwards that
context and stored stage to WorldGenHandler.generateChunk, then returns false.
This completes the direct link from the added biome feature to the captured
handler. The false return does not establish that its consumers placed no
blocks; their generation occurs before the return. Effective consumer contents
and applicability remain separate from this library call-chain finding.
