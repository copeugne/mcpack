# Integrated API dependency selection

Extractor 581e274d captures OptionalDependencyStructure and ModAdaptiveStructure
from the retained integrated_api-1.7.3+1.21.1-neoforge.jar. Both disassemblies and
identities independently reproduce byte for byte. Manifest SHA-256:
32a23f9fe7a1ae8dbf99532a070147dd857956b401e50d04ea29da31ba99b8a3.

```sh
uv run -m tools.inspect_item8_pool_elements --archive integrated_api-1.7.3+1.21.1-neoforge.jar --class-name com/craisinlord/integrated_api/world/structures/OptionalDependencyStructure.class --class-name com/craisinlord/integrated_api/world/structures/ModAdaptiveStructure.class --output evidence/raw/item8/integrated-api-dependency-selection-r1
```

OptionalDependencyStructure.extraSpawningChecks first preserves the superclass
check, then rejects any missing required mod or present illegal mod. Its isLoaded
method delegates to PlatformHooks.isModLoaded. ModAdaptiveStructure starts with
the original pool and substitutes newPool only when its change-mod list is nonempty
and all entries are loaded. These are dependency/pool decisions, not extra roots.

The loader lookup and inherited generation caller still require binding before
accepting frozen-stack inactivity claims. The exact next classes are PlatformHooks,
its NeoForge PlatformHooksImpl and JigsawStructure. No new provider discovery or
world measurement is implied. Scoped extractor Ruff/Basedpyright pass.
