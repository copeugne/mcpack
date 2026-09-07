# Quark annotation conversion

Captured with extractor revision f19c6ea. identities.json binds the retained
archive, class and verbose disassembly. Reproduction matched the capture and
identity manifest byte for byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zetaimplforge/module/ModFileScanDataModuleFinder.class --output evidence/raw/item8/quark-enablement-callers-f19c6ea
```

The initial command mistakenly repeated the singular --archive option. Only
the last value, Zeta, applied. Its valid output is preserved here; the Quark
caller was then captured separately under quark-world-category. No missing
Quark output is represented as captured by this manifest.

ModFileScanDataModuleFinder.get filters scan annotations to ZetaLoadModule and
maps them with lambda$get$1. The verbose bootstrap table binds both callbacks.
The mapper loads the annotated class and passes its annotation data map to
ZetaLoadModuleAnnotationData.fromForgeThing. CommonProxy.start, captured in
quark-world-category, supplies this finder for mod ID quark to loadModules.
This resolves which of the two captured annotation converters Quark selects.

MonsterBoxModule's annotation specifies only category="world". The selected
converter therefore supplies an empty antiOverlap list and enabledByDefault
true. TentativeModule and ZetaModuleManager already preserve the transfer into
the module. Empty overlap candidates cannot disable the module through the
captured anyMatch check. No additional mod-overlap scan is needed for this box.

Scoped extractor checks passed. This is source-derived applicability evidence,
not an observed encounter. No new runtime or measurement system was added.
