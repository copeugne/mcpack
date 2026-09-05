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

## Family dispositions

The source milestone above is delivered in `40922f3`. Six existing vanilla
family variants now record normal_generation.status=SUPPRESSED:

| Registry root | Cancelling retained mod | Frozen predicate |
|---|---|---|
| minecraft:desert_pyramid | betterdeserttemples | Disable Vanilla Pyramids=true |
| minecraft:fortress | betterfortresses | Disable Vanilla Nether Fortresses=true |
| minecraft:jungle_pyramid | betterjungletemples | Disable Vanilla Jungle Temples=true |
| minecraft:monument | betteroceanmonuments | Disable Vanilla Ocean Monuments=true |
| minecraft:stronghold | betterstrongholds | Unconditional after STRONGHOLD type match |
| minecraft:swamp_hut | betterwitchhuts | Disable Vanilla Witch Huts=true |

Each family binds its source manifest and mixin metadata; configurable cases
also bind the frozen TOML. Existing content descriptions remain vanilla source
information, not proof of active generation. Registered IDs and biome memberships
remain intact. This supersedes the pending integration instruction above but
not the remaining Item 8 work. IDAS and Integrated Villages hooks are separate
remaining provider checks; these six dispositions do not infer their behavior.

The parameterized test verifies preserved source hashes, loader/mixin declarations,
exact structure-type guards, cancellable HEAD injection, false return, config
labels and runtime-field binding. It covers all six current cases without adding
a new validation framework or collecting another runtime.

```sh
uv run pytest -q tests/item8/test_yung_suppression.py tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_yung_suppression.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py tools/inspect_item8_pool_elements.py
uv run basedpyright tests/item8/test_yung_suppression.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py tools/inspect_item8_pool_elements.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yung-suppression.json
```

Decision SHA-256:
`216306ee257892d8bb21d0b25a9b0ce797dbaa1fa00c9f6b6a449168783a7167`.

All 69 affected tests passed. Scoped Ruff and Basedpyright passed.

Dispositions and tests are delivered in `f1f4649`. Inventory rebuilt at that
commit, SHA-256:
`385100c3e7f984662e7e9eaad598d4b858553a13c5965caabb29f764b2d61816`.
Only the six variant dispositions, their evidence and decision input hash change.
