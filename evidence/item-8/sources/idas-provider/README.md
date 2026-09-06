# IDAS remaining provider source

Extractor 0f875a1 captures eighteen previously uncaptured classes from
idas-1.13.7+1.21.1-neoforge.jar. The prior idas-suppression capture contains the
other three classes. The independent r2 extraction reproduced every generated
file byte for byte before this README was added.

Archive SHA-256:
7f5031dd90ae0b32d7fe5c6c47c877cac1eb95a178bc78d196cb24c17ce82522.
Source manifest SHA-256:
b3c57a302eacff4c8a957037fa610e7480d0d5a29d0715eeedea159d27cc20fe.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive idas-1.13.7+1.21.1-neoforge.jar \
  --class-name architectury_inject_IDAS_common_dac55d1c3d7c43d0b24fcf81e4608720_ada83c3f6ff40818e1642131a53d09761e2621fbd5744848c87d68aaef472d6eidas11371211commondevjar/PlatformMethods.class \
  --class-name com/craisinlord/idas/IDAS.class \
  --class-name com/craisinlord/idas/IDASTags.class \
  --class-name 'com/craisinlord/idas/config/ConfigModule$General.class' \
  --class-name com/craisinlord/idas/config/ConfigModule.class \
  --class-name com/craisinlord/idas/config/IDASConfigNeoforge.class \
  --class-name com/craisinlord/idas/item/IDASItems.class \
  --class-name com/craisinlord/idas/mixins/LabyrinthBossKilledMixin.class \
  --class-name com/craisinlord/idas/mixins/LocateStructuresCommandMixin.class \
  --class-name com/craisinlord/idas/mixins/ServerLevelMixin.class \
  --class-name com/craisinlord/idas/mixins/ServerPlayerTickMixin.class \
  --class-name com/craisinlord/idas/neoforge/IDASNeoForgeRegistries.class \
  --class-name com/craisinlord/idas/neoforge/IDASNeoforge.class \
  --class-name com/craisinlord/idas/sound/IDASSounds.class \
  --class-name com/craisinlord/idas/state/IStateCacheProvider.class \
  --class-name com/craisinlord/idas/state/stateCache.class \
  --class-name com/craisinlord/idas/state/stateRegion.class \
  --class-name com/craisinlord/idas/tab/IDASTabs.class \
  --output evidence/raw/item8/idas-provider-r2
```

The NeoForge entry registers item, sound and creative-tab content, initializes
common IDAS, initializes tags, and loads the prior configuration path. Common
IDAS adds a server-start callback whose body returns without further work.

The remaining captures preserve direct locate handling, Labyrinth boss-death
handling, server/player hooks and their cleared-state storage, as well as the
configuration and registry implementations. These are relevant to existing
structure behavior and need scope interpretation alongside the packaged roots
and component graph. Do not infer a new family from a state class or mixin name.
Do not repeat the prior suppression evidence or treat these captures alone as
provider closure, successful runtime behavior or final attribute acceptance.

This isolated generated evidence increment supports the open IDAS provider row.
The remaining work is its packaged component partition and interpretation of the
captured hooks. No new measurement system or baseline modification is included.

The unfiltered pilot also emitted unrelated archive mixin metadata. It is
retained under evidence/raw/item8/idas-provider-unfiltered and idas-provider-r1.
The accepted command selects only the IDAS archive; class identities are unchanged.
