# YUNG vanilla-generation suppression sources

This source increment preserves six retained replacement hooks and the configuration
bindings for the five configurable hooks. Stronghold suppression is unconditional
once the structure type matches. Each hook injects at the head of
ChunkGenerator.tryGenerateStructure, is cancellable, and returns false for its
vanilla structure type. Required mixin and NeoForge loader declarations are
preserved beside the disassembly. This supports normal-generation disposition,
not command placement or an instrumented invocation of each hook.

The existing extractor now accepts these exact classes and retains metadata for
the current YUNG archive consumers. It preserves the prior mineshaft metadata
ordering. No measurement system or server run is added. The first extraction
commands were rejected by argparse because only class suffixes had been added
to its exact-name choices. Full class names fixed selection before any output
was written. Existing source evidence was not overwritten.

## Reproduction

Use fresh output directories. These are the actual source selections; unrelated
methods inside the selected compiled configuration classes remain in their
irreducible disassemblies. No JAR is committed.

```sh
uv run -m tools.inspect_item8_pool_elements --archive YungsBetterDesertTemples-1.21.1-NeoForge-4.1.5.jar --class-name com/yungnickyoung/minecraft/betterdeserttemples/config/ConfigGeneralNeoForge.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/mixin/DisableVanillaPyramidsMixin.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/module/ConfigModuleNeoForge.class --output evidence/item-8/sources/desert-temple-suppression
uv run -m tools.inspect_item8_pool_elements --archive YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar --class-name com/yungnickyoung/minecraft/betterfortresses/config/ConfigGeneralNeoForge.class --class-name com/yungnickyoung/minecraft/betterfortresses/mixin/DisableVanillaFortressesMixin.class --class-name com/yungnickyoung/minecraft/betterfortresses/module/ConfigModuleNeoForge.class --output evidence/item-8/sources/fortress-suppression
uv run -m tools.inspect_item8_pool_elements --archive YungsBetterJungleTemples-1.21.1-NeoForge-3.1.2.jar --class-name com/yungnickyoung/minecraft/betterjungletemples/config/ConfigGeneralNeoForge.class --class-name com/yungnickyoung/minecraft/betterjungletemples/mixin/DisableVanillaJungleTempleMixin.class --class-name com/yungnickyoung/minecraft/betterjungletemples/module/ConfigModuleNeoForge.class --output evidence/item-8/sources/jungle-temple-suppression
uv run -m tools.inspect_item8_pool_elements --archive YungsBetterOceanMonuments-1.21.1-NeoForge-4.1.2.jar --class-name com/yungnickyoung/minecraft/betteroceanmonuments/config/ConfigGeneralForge.class --class-name com/yungnickyoung/minecraft/betteroceanmonuments/mixin/DisableVanillaMonumentsMixin.class --class-name com/yungnickyoung/minecraft/betteroceanmonuments/module/ConfigModuleNeoForge.class --output evidence/item-8/sources/monument-suppression
uv run -m tools.inspect_item8_pool_elements --archive YungsBetterStrongholds-1.21.1-NeoForge-5.1.3.jar --class-name com/yungnickyoung/minecraft/betterstrongholds/mixin/DisableVanillaStrongholdsMixin.class --output evidence/item-8/sources/stronghold-suppression
uv run -m tools.inspect_item8_pool_elements --archive YungsBetterWitchHuts-1.21.1-NeoForge-4.1.1.jar --class-name com/yungnickyoung/minecraft/betterwitchhuts/config/ConfigGeneralNeoForge.class --class-name com/yungnickyoung/minecraft/betterwitchhuts/mixin/DisableVanillaWitchHutsMixin.class --class-name com/yungnickyoung/minecraft/betterwitchhuts/module/ConfigModuleNeoForge.class --output evidence/item-8/sources/witch-hut-suppression
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Extraction and scoped checks passed. Manifest identities:

- desert-temple-suppression: `20a9cee456cc7df91632272752f855c9c972bc860d0155c267ea9067f6bb26f6`.
- fortress-suppression: `100e268d617b82cd28a20aa2adbdff2eef29976b3a60bf8627337e2f1ada9bb4`.
- jungle-temple-suppression: `40fa52b38f8b195be2e65b9f3846312b32024f5825c064ac703b8ba31a6d8611`.
- monument-suppression: `ac148bb2b65821f70b7402c9681844a378bcc3918f57d6076d670af78a53b53d`.
- stronghold-suppression: `56e90dc542fe8ef9a152ccaa201cfa79e2e4f629f4b9b68623a4bf9c96f7224b`.
- witch-hut-suppression: `b76bb19b6c7552b13b7b07b350826c84774a492932639636e87ed4bffa525c9a`.

The inventory is unchanged at this source milestone. Next bind frozen settings
and these hook identities to each applicable registered vanilla family, keeping
existing source-derived descriptions separate from effective generation.
Do not continue detailed inactive-generator inspection merely for completeness.
