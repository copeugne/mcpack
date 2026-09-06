# Integrated API dependency caller and loader lookup

Extractor 0b2a9040 captures the three direct remaining boundaries from the retained
integrated_api-1.7.3+1.21.1-neoforge.jar. All disassemblies and identities independently
reproduce byte for byte. Manifest SHA-256:
d48afad5e1c7a3ca12a455587d1a9b8da139d1ab479a9aaf2bae2a25c5f74a3a.

```sh
uv run -m tools.inspect_item8_pool_elements --archive integrated_api-1.7.3+1.21.1-neoforge.jar --class-name com/craisinlord/integrated_api/world/structures/JigsawStructure.class --class-name com/craisinlord/integrated_api/utils/PlatformHooks.class --class-name com/craisinlord/integrated_api/utils/neoforge/PlatformHooksImpl.class --output evidence/raw/item8/integrated-api-dependency-caller-r1
```

JigsawStructure.findGenerationPoint invokes the virtual extraSpawningChecks and
returns Optional.empty when it fails. OptionalDependencyStructure's override is
preserved in integrated-api-dependency-selection. PlatformHooks.isModLoaded calls
the NeoForge implementation, which delegates directly to ModList.get().isLoaded.
These complete the dependency consumer path without an additional world experiment.

The existing runtime_mod_ids parser reads the captured registry-run Mod List from
evidence/raw/item8/registry-r1/debug.log, SHA-256
e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b.
That list contains idas and integrated_api, but neither ars_nouveau nor iceandfire.
Use the existing capture/archive retention for the raw log. The source path proves
dependency eligibility only, not successful placement or effective gameplay.
Scoped extractor Ruff/Basedpyright pass.
