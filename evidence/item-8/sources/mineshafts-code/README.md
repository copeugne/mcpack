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

The resolved grouping is recorded in `evidence/item-8/family-decisions.json`:
the 13 Better Mineshafts structure IDs form one family of biome, material,
decoration and support variants. `tests/item8/test_family_decisions.py` checks
exact runtime membership, the shared specialized definition fields and preserved
code identities. This grouping decision does not resolve every family attribute.

Remaining: finish effective biome/dimension constraints,
generated physical size and visual discoverability, and
effective loot attribution. This source inspection does not close Item 8.

## Explicit normal-generation disposition

Both vanilla mineshaft variants now carry normal_generation.status=SUPPRESSED
in family-decisions.json, with the derivation and command-placement boundary
beside that value. Their runtime IDs and compatible biome memberships remain
inventoried. No absence-based inference, new server run or inspection of the
inactive vanilla piece generator is required for this disposition.

The focused family test binds the frozen TOML, source manifest and disassembly
hashes, configuration-field binding, cancellable HEAD injection, vanilla type
predicate, false return and required loader/mixin metadata. It checks both roots.
The already preserved metadata is now directly included in the family evidence.

```sh
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-mineshaft-disposition.json
```

Decision SHA-256:
`303874189f6806bc565d51e5cc234c2b57279cc7c621b161646de5c098400c23`.
This resolves normal-generation availability; it does not claim the attributes
of command-placed vanilla structures or complete Item 8.

All 62 affected tests passed. Scoped Ruff and Basedpyright passed after splitting
compound assertions and wrapping long test lines. No source or disposition data
changed during those formatting fixes.

Decision/test increment: `9e8f032`. Rebuilt inventory SHA-256:
`3ac3368b6de3d939f9ac78d117eb0397bbe0c2092967b72e71b6d2b4223d13f3`.
The inventory diff adds only the two variant dispositions, metadata evidence
identity and updated decision hash. Other family fields remain unchanged.

## Dimension and discoverability attribution

The effective biome union for all13 Better Mineshafts IDs intersects only the
captured Overworld biome set. These exact catalogs are now directly bound in
family evidence. VerticalEntrance.postProcess invokes generateVerticalShaft and
generateSurfaceTunnel. Record the conditional possibility of a surface entry
cue, while subterranean tunnels remain concealed; no successful visible opening
or human discovery distance is established by source inspection.

Retained world-bounds indexes90/270/291 and repeated493/659/680 are non-full
starts (structure_starts or biomes). Their generation envelopes extend toY320
because the initial entrance uses maximum build height. They are not completed
physical-height measurements. Four dimension/discoverability attributes across
this family and Spider Dungeon are integrated; both families' four geometry
attributes remain open. Reuse the source explanation before interpreting any
future saved entrance bounding box as occupied geometry.

## Two-family geometry capture declaration

Four required size attributes remain for Better Mineshafts and Spider Dungeon.
Existing starts are non-full. The mineshaft VerticalEntrance.determineDirection
updates yAxisLen/localYEnd from terrain, but does not shrink boundingBox.
getInitialBoundingBox reserves center X/Z plus or minus24 and maximum build Y.
Thus even a saved full start's raw entrance box is not occupied shaft height.
Inspect its saved hasTunnel, centerPos, yAxisLen and floorAltitude alongside
non-entrance pieces before deriving an approximate vertical extent. Preserve the
raw envelope separately. Spider uses recursively assembled custom tunnel pieces.
Neither a single piece nor initial placement Y establishes its assembled size.

Declare one fresh frozen seed42 capture, two targets,81 requested chunks each
(162 total), timeout900. Select the lush mineshaft variant as one illustration
of the shared generator, not all13 variants or a size distribution. Require full
starts, correlated save, clean exit and accepted frozen configuration. Preserve
all failures. Reuse existing runner, NBT decoder and archive/restore workflow;
no new measurement system. An observed piece envelope is approximate assembly
geometry, not occupied volume or proof that every distant piece was placed.

```sh
uv run -m tools.run_item7_gap_targets \
  --pristine instances/pristine-baseline-v0 \
  --artifact-manifest evidence/item-3/artifact-acquisition-manifest.json \
  --retained-manifest evidence/item-3/runtime/retained-server-candidates.txt \
  --seed-suite test-environment/seed-suite.json \
  --frozen-config evidence/item-6/frozen \
  --frozen-manifest evidence/item-6/generated-config-manifest.json \
  --config-audit evidence/item-6/config-audit.json \
  --java-home downloads/item2/temurin/extracted/jdk-21.0.12.1+1 \
  --target instances/item8/mineshaft-spider-geometry-r1 \
  --log-path evidence/raw/item8/mineshaft-spider-geometry-r1/console.log \
  --captured-config evidence/raw/item8/mineshaft-spider-geometry-r1/configuration \
  --receipt evidence/raw/item8/mineshaft-spider-geometry-r1/run.json \
  --timeout-seconds 900 \
  --structure bettermineshafts:mineshaft_lush \
  --structure betterdungeons:spider_dungeon
```

### Two-family results and custody

The declared seed42 run completed both targets, readiness, correlated flush,
clean exit0 and frozen configuration acceptance. No process-group kill. The raw
logs preserve baseline warnings and errors; successful lifecycle is not a claim
of universal compatibility. Archive250 files,6,047,640 bytes (32,433,811 bytes
uncompressed), SHA-256 d14c00bb34a7151b312ca18b8f82820772aca904659cfa2e3e19b8cfd16ea536.
Source revision9a8159147c846e1b07451405d8eaea40dc48b2c7 is also the verified tag
item-8-mineshaft-spider-geometry-2026-09-07-r1 on copeugne/mcpack. Local and
published-download restores verified all250 files. Manifest and both restore
receipts are under evidence/item-8/raw-custody/mineshaft-spider-geometry-r1-*.
Manifest SHA-256 771509208ba54aae65a35a114d896131caf7f04b049934d21f057cff922d1aa8.
The archive contains2763 decoded records, not the requested162-chunk denominator.
chunks.jsonl SHA-256 86d9c76862de2fd08c9b4ea6b554f88edef58c7241ac31054178ad46f4342dba.

Line1517: mineshaft_lush, full chunk32,-39,91 pieces, raw envelope
[446,-26,-743,580,320,-597]. Region world/region/r.1.-2.mca slot800,
structures.starts[bettermineshafts:mineshaft_lush].Children[0] is
bettermineshafts:bmsverticalentrance, BB[491,-22,-645,539,320,-597],
centerPos[515,-22,-621],hasTunnel0,yAxisLen83,tunnelLen0,floorAltitude0.
VerticalEntrance.postProcess branches directly to return when hasTunnel is false
after determineDirection. Thus yAxisLen83 alone is not a generated shaft.
Exclude this unused entrance reservation. Children[1:] contain90 network pieces;
axis-wise inclusive union is[446,-26,-743,580,-1,-624],135x26x120 blocks.
This is an approximate assembly envelope, not a count of occupied blocks or
proof that every distant piece was placed. Keep the raw reserved box unchanged.

Line2680: Spider Dungeon, full chunk129,-133,20 pieces, envelope
[2042,11,-2130,2118,74,-2069],77x64x62 blocks. Existing observed_bounds derives
this inclusive union. Both are illustrative assemblies, not family-wide extrema.
The published-download restore reproduced both results and saved entrance fields.
An initial offline inspection incorrectly accessed the observed_bounds dictionary
as an object and failed; corrected dictionary access produced these results.
No raw evidence was changed by that failed inspection.

Executed after the clean run:

```sh
uv run python -c 'from pathlib import Path; from tools.stage_item7_world import copy_world_boundary; copy_world_boundary(Path("instances/item8/mineshaft-spider-geometry-r1"), Path("evidence/raw/item8/mineshaft-spider-geometry-r1/world"))'
uv run -m tools.decode_item7_world evidence/raw/item8/mineshaft-spider-geometry-r1/world --output evidence/raw/item8/mineshaft-spider-geometry-r1/chunks.jsonl
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/mineshaft-spider-geometry-r1 --archive evidence/raw/item8/item8-mineshaft-spider-geometry-r1-9a815914.tar.gz --manifest evidence/item-8/raw-custody/mineshaft-spider-geometry-r1-manifest.json --revision 9a8159147c846e1b07451405d8eaea40dc48b2c7
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/item8-mineshaft-spider-geometry-r1-9a815914.tar.gz --manifest evidence/item-8/raw-custody/mineshaft-spider-geometry-r1-manifest.json --target evidence/raw/item8/mineshaft-spider-geometry-r1-restored --receipt evidence/item-8/raw-custody/mineshaft-spider-geometry-r1-local-restore.json
gh release download item-8-mineshaft-spider-geometry-2026-09-07-r1 --repo copeugne/mcpack --pattern item8-mineshaft-spider-geometry-r1-9a815914.tar.gz --dir evidence/raw/item8/mineshaft-spider-geometry-r1-download
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/mineshaft-spider-geometry-r1-download/item8-mineshaft-spider-geometry-r1-9a815914.tar.gz --manifest evidence/item-8/raw-custody/mineshaft-spider-geometry-r1-manifest.json --target evidence/raw/item8/mineshaft-spider-geometry-r1-downloaded-restore --receipt evidence/item-8/raw-custody/mineshaft-spider-geometry-r1-downloaded-restore.json
```

For direct NBT inspection, use existing item7_anvil._slots/_chunk_payload and
item7_nbt.decode_compound_nbt on the exact retained region/slot above. No custom
binary decoder is needed. The explicit child selection and inclusive union
above define the derivation; do not use the unfiltered347-block reserved height.

Validation:85 tests passed with the existing command
`uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py`.
Rebuild command: `uv run -m tools.build_item8_inventory --output evidence/raw/item8/mineshaft-spider-finished-inventory-r2.json`.
Semantic comparison changed only the two families' four geometry attributes,
archive evidence references and corresponding input identity. No schema or
measurement tooling was added. Registry313/409 and nonregistry40/40 assessed,
total353/449,96 remaining; final canonical integration and acceptance stay open.

Final staged inspection clarified both visibility limitations: only baseline
starts are non-full; supplemental full starts do not measure visibility. The
rebuild passed after this prose correction; no measurement or source changed.
