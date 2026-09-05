# Zeta enablement inputs

Captured with extractor revision f1ace70. Exact archive, class and disassembly
hashes are in identities.json. Both captures and identities reproduced byte for
byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zeta/module/ZetaCategory.class --class-name org/violetmoon/zeta/module/ZetaLoadModuleAnnotationData.class --output evidence/raw/item8/zeta-enablement-f1ace70
```

ZetaCategory stores requiredMod and caches whether it is null or loaded. Its
two-argument name/item constructor supplies null; requiredModsLoaded returns
that cached Boolean. This resolves the category predicate but does not yet
identify the constructor used for Quark's world category.

ZetaLoadModuleAnnotationData.fromForgeThing uses an empty list when antiOverlap
is absent, true when enabledByDefault is absent, false for clientReplacement,
and zero for loadPhase. fromAnnotation instead reads the annotation accessors.
The MonsterBoxModule verbose capture specifies only category="world". Binding
the actual loader path is still required before claiming effective overlap
state from these defaults.

The existing ConfigManager capture shows that isCategoryEnabled tests the
enabledCategories set, and setModuleEnabled calls ZetaModule.setEnabled. The
frozen configuration enables categories.world and world."Monster Box".
The remaining direct inputs are world-category construction and the loader's
annotation conversion path. No runtime enablement or world occurrence is
claimed. Do not repeat field-mapping, activation or loot investigations.

Scoped extractor Ruff and Basedpyright checks passed. No new measurement
system was added; these captures use the existing identity-bound extractor.
