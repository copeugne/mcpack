# Integrated Villages and IDAS suppression sources

Six selected classes preserve both cancellation hooks, configuration labels and
runtime-field bindings. Required mixin lists and NeoForge loader declarations
are retained beside the disassembly. The existing extractor now supports the
mixins package spelling and these exact archive/class selections. No server run
or new measurement system is required.

```sh
uv run -m tools.inspect_item8_pool_elements --archive integrated_villages-1.3.3+1.21.1-neoforge.jar --class-name com/craisinlord/integrated_villages/mixins/DisableVanillaVillagesMixin.class --class-name com/craisinlord/integrated_villages/config/ConfigGeneralNeoforge.class --class-name com/craisinlord/integrated_villages/config/ConfigModuleNeoforge.class --output evidence/item-8/sources/integrated-village-suppression
uv run -m tools.inspect_item8_pool_elements --archive idas-1.13.7+1.21.1-neoforge.jar --class-name com/craisinlord/idas/mixins/DisableStructuresMixin.class --class-name com/craisinlord/idas/config/ConfigGeneralNeoforge.class --class-name com/craisinlord/idas/config/ConfigModuleNeoforge.class --output evidence/item-8/sources/idas-suppression
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Reproduce into fresh directories. Extraction and scoped checks passed.
Manifest SHA-256 values:

- Integrated Villages: `1e13f934a2a29c03d56bfdb610aaea5c53b28367e4a554a0ecf3abaf58942320`.
- IDAS: `d6b5776443ad0f76f42e94d3e54fa497dbdea94fd6eef096ee3595c3a48be376`.

Both hooks inject at HEAD of the exact ChunkGenerator.tryGenerateStructure
signature, with cancellation enabled. Integrated Villages first checks
ConfigModule.General.disableVanillaVillages, then the unwrapped registry key.
When present and contained in DISABLED_VILLAGES it returns false. The set contains
the five vanilla village keys plus terralith:fortified_desert_village and
terralith:fortified_village. It does not test the generic jigsaw type. Its frozen
Disable Vanilla Villages setting is true. This is wider than the setting label,
but does not extend to CTOV or IDAS castle keys.

IDAS separately checks disableIaFStructures against iceandfire:mausoleum,
iceandfire:gorgon_temple and iceandfire:graveyard, then disableDesertPyramid
against StructureType.DESERT_PYRAMID. Both frozen settings are true. The three
Ice and Fire keys are absent from the preserved structure registry; no extra
family is created for that inactive compatibility branch. The desert-pyramid
hook is an additional suppression source alongside Better Desert Temples.

These are source-and-configuration derivations for normal generation. They do
not prove command-placement behavior or an instrumented invocation of each hook.
The inventory is unchanged at this source milestone. Bind these identities and
frozen settings to all seven village roots and the desert-pyramid record next.
