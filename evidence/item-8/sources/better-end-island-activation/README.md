# Better End Island activation and respawn sources

Manifest SHA-256: `65c8b9e69ad267dced5a68b6035808345da4d67193d919e1760028ccf8ec399a`.
Archive SHA-256: `8005f1ea798d09fc05dad07a21ed1f393a523a718197cdbd37b1ce6d9a17e4a4`.

Eight exact classes cover selected respawn generator callers, surface origin
selection and NeoForge initialization/service binding. The existing metadata
format additionally retains the two packaged service declarations. Earlier
mixin and mod metadata entries are unchanged; preserve both capture revisions.
This is source evidence, not a new runtime observation.

Reproduce with extractor revision `fd83868` and a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar \
  --class-name com/yungnickyoung/minecraft/betterendisland/BetterEndIslandNeoForge.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/services/NeoForgeModulesLoader.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/services/NeoForgePlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/services/Services.class \
  --class-name 'com/yungnickyoung/minecraft/betterendisland/world/DragonRespawnStage$3.class' \
  --class-name 'com/yungnickyoung/minecraft/betterendisland/world/DragonRespawnStage$5.class' \
  --class-name com/yungnickyoung/minecraft/betterendisland/world/DragonRespawnStage.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/world/util/WorldgenUtils.class \
  --output evidence/raw/item8/better-end-island-activation-reproduction
```

Recursive comparison before adding this README matched the fresh reproduction
exactly. Scoped Ruff/Basedpyright passed at fd83868. The preceding 97b2aae
selection commit had a line-length failure, corrected separately without
rewriting history. No measurement system or validation framework was added.
