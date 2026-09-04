# Better Mineshafts custom generation inspection

Source artifact: `YungsBetterMineshafts-1.21.1-NeoForge-5.1.1.jar`, SHA-256
`5625930dfb3240820d6e4ecf55fff0c39f70ce782fad117a4d418251184c7be0`.
Extraction implementation: `9669fb1` (extends `c51973c`). `identities.json`, SHA-256
`5e78a733f4198752de93fb640557a87fae13334a92a3fbad422cd33bb5d41127`,
binds every disassembly to its original class and archive hashes.

```sh
uv run -m tools.inspect_item8_pool_elements --archive YungsBetterMineshafts-1.21.1-NeoForge-5.1.1.jar --output evidence/raw/item8/mineshafts-code-reproduction
```

The committed-source extraction and a second extraction were byte-identical.
The directory ending in `.jar` contains text disassemblies only. No classes or
JAR binaries are included. This generated increment is isolated because the
custom structure has no template-pool path: its piece generation, configuration
binding, spawners and loot behavior require inspection of these code paths.

## Findings for family assembly

- The packaged structure definitions use `bettermineshafts:mineshaft` and carry
  per-variant biome tags and configuration. `BetterMineshaftStructure` invokes
  `BetterMineshaftGenerator` and starts with `VerticalEntrance`; piece classes
  are components of that structure, not separate canonical families.
- `SideRoomDungeon` sets a spawner to `EntityType.CAVE_SPIDER`.
  `ZombieVillagerRoom` sets a spawner to `EntityType.ZOMBIE_VILLAGER`.
  These are authored generation paths. They do not establish that every
  mineshaft contains both room types or that the spawners are active in every
  generated sample.
- `SideRoomDungeon`, `ZombieVillagerRoom`, `SideRoom`, `SmallTunnel`, and
  `BigTunnel` reference `BuiltInLootTables.ABANDONED_MINESHAFT`. The latter two
  include chest-minecart paths. Effective loot injections still need attribution.
- The frozen `config/bettermineshafts-neoforge-1_21.toml` sets the initial
  generation Y range to -55 through 30, and small shaft chain length to 9.
  These inputs are not a structure's total vertical extent or block length.
  The configuration also enables the vanilla-generation suppression hook
  described below.
- `BetterMineshaftStructure.generatePieces` passes `getMaxBuildHeight()` to
  `VerticalEntrance`. Its constructor passes that value to
  `getInitialBoundingBox`. Consequently the initial entrance bounding box is
  a generation envelope, not a measurement of occupied blocks. Preserve the
  chunk-status limitation in `world-bounds.json.gz` when estimating size.

## Vanilla-generation suppression

`DisableVanillaMineshaftsMixin` injects at the head of
`ChunkGenerator.tryGenerateStructure` with cancellation enabled. When
`ConfigModule.disableVanillaMineshafts` is true and the structure type equals
`StructureType.MINESHAFT`, it returns false through the injection callback.
The frozen TOML enables this setting; `ConfigModuleNeoForge` binds it to the
runtime field. The preserved `mixin-metadata.json` includes both the NeoForge
loader declaration and required mixin list, with original member hashes.

This establishes the source-and-configuration basis for treating
`minecraft:mineshaft` and `minecraft:mineshaft_mesa` as registered but suppressed
in normal generation under this stack. Registry presence is not evidence that
they generate. This is a derivation from the installed hook, not a separately
instrumented invocation of that hook. The callback tests the vanilla structure
type, not the `bettermineshafts:mineshaft` custom type.

`LocateVanillaMineshaftCommandMixin` separately checks a direct request for
`minecraft:mineshaft` and displays a redirect message. Do not infer the
generation suppression scope from this narrower command check.

The mixin disassemblies include annotations via verbose `javap`. The tool
replaces only the leading local `Classfile` path with archive/member identity;
the exact transformation is tracked. The original pilot containing a host path
remains outside Git. Existing generation disassemblies remain unchanged.

Remaining: finish canonical grouping, effective biome/dimension constraints,
generated physical size and visual discoverability, and
effective loot attribution. This source inspection does not close Item 8.
