# Quark world category construction

Captured with extractor revision f19c6ea. identities.json binds the exact
retained archive, class and verbose disassembly. Reproduction matched the
capture and identities byte for byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name org/violetmoon/quark/base/proxy/CommonProxy.class --output evidence/raw/item8/quark-world-category-f19c6ea
```

CommonProxy.start constructs the world category with name "world" and the
grass-block item using the two-argument ZetaCategory constructor. The captured
constructor in zeta-enablement-inputs supplies requiredMod=null, making its
requiredModsLoaded predicate true. The category list and a
ModFileScanDataModuleFinder("quark") are supplied together to Zeta.loadModules.
Thus the world category does not impose an additional required-mod gate.

The frozen categories.world and world."Monster Box" settings are true.
The already captured ConfigManager.lambda$new$8 reads the category option and
calls setCategoryEnabled; lambda$new$10 reads the module option and calls
setModuleEnabled. Combined with the recorded initial refresh and empty overlap
input, these sources resolve the inputs previously missing from the Monster Box
enablement analysis. This does not establish a saved-world occurrence, successful
entity spawning or live encounter. Those remain separate evidence questions.

Scoped extractor checks passed. No new runtime or measurement system was added.

## Initial enable state

The existing verbose ConfigManager capture also resolves callback order.
Its constructor inserts lambda$new$12 at index zero in the databindings list.
onReload traverses that list before reload listeners. lambda$new$12 first
applies categoryEnabledOptions through lambda$new$8, then overlap options,
then moduleEnabledOptions through lambda$new$10. The bootstrap table binds
these actual targets. Thus the world category is enabled before the true
Monster Box option reaches setEnabled. The category has no required mod and
the module has no overlap candidates, so the captured setEnabled logic retains
true. This closes the initial enablement gap by source/configuration/log
derivation, not a runtime field dump. The preserved initial-refresh return log
and exact configuration equality are recorded in quark-monster-box-bindings.

No further enablement capture is needed. Saved-world attribution and relevant
ambient spawning remain unresolved. Existing generator and mob/reward source
interpretations must not be repeated to address those separate gaps.
