# Integrated Stronghold provider code

All nine packaged classes captured with extractor f70a1a0. An independent
extraction reproduced the files byte for byte before this README. Manifest SHA-256:
0044580a6b6f71c9b32c8d385d539779c7b0b2ad22d4c21bf1a5bfbbf2785d5b.
Archive SHA-256: c6ac6ad68de806524615238f8a7efe511c417b8cd56ffceb7dd62aad9c8b821b.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive integrated_stronghold-1.1.4+1.21.1-neoforge.jar \
  --output evidence/raw/item8/integrated-stronghold-provider-r1
```

The NeoForge constructor calls IntegratedStrongholdNeoForgeRegistries.register.
That class registers sounds, music-disc items and a creative tab. Item and sound
factories construct vanilla objects; the tab displays those items. Common entry
only initializes a logger. The generated Architectury bridge returns neoforge.
None of these classes registers a structure or independently places content.
The packaged root instead uses the separately attributed Integrated API type.

DisableVanillaStrongholdsMixin injects at ChunkGenerator.tryGenerateStructure
HEAD and returns false for StructureType.STRONGHOLD. Its second HEAD injection,
in the concentric-ring nearest-structure lookup, returns the supplied vanilla
stronghold holder with position (29000000, 0, 29000000). That position is an
artificial locate result, not an observed or authored structure location.

LocateStrongholdCommandMixin intercepts a direct minecraft:stronghold resource
key and throws an exception directing the caller to locate
integrated_stronghold:stronghold. It does not itself redirect the search or
generate that structure. A tag argument is not the direct-key branch. Both
mixins are declared in the required packaged config; source declaration alone
does not prove every runtime interaction or mixin ordering.

Reuse the existing registry and family-decision regression for the sole root.
The provider-scope check separately binds all packaged resources and component
dispositions to the preserved pool graph. Keep missing armory references and
disconnected alternate templates unchanged. Shared Integrated API behavior and
effective family attributes remain separate downstream attribution work.

## Content assessment

The five content/discoverability attributes are now integrated in
family-decisions.json. Footprint and vertical size remain open. Provider discovery
is closed; this assessment does not add families or repair missing templates.

Inspect the stronghold root and its reachable template entries in the preserved
pool-traces-content.json.gz, with original NBT in the template catalog. There are
58 reachable templates, including 23 with ordinary spawner NBT, and 19 referenced
processor lists. The two missing armory templates remain explicit failures.
All retained structure-block markers have CORNER mode, not DATA spawn markers.

The authoritative attributes list all 16 packaged entity IDs. Creepers, spiders
and zombies are authored hostile sources. Animals, vehicles, displays, Create
seat/glue entities and Quark frames are not additional enemy species. AlexsMobs
and MowziesMobs are absent from the retained runtime mod list, so their authored
entries do not establish live enemies. Reuse registry-r1/debug.log, SHA-256
e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b,
with the existing runtime_mod_ids parser. Create and Quark occur at lines1544
and1660. The piece-bounds silverfish/enderman natural override is separate.

The packaged resource paths below are in packaged-json-redacted.json.gz under
data/integrated_stronghold/. Resolve a template's pool element processors field
to worldgen/processor_list/<name>.json, then its
integrated_api_spawner_resourcelocation to integrated_structure_spawners/<name>.json.
The complete processor-to-list mapping and seven weighted lists are recorded in
generated_spawners. Every spawner processor declares the same settings recorded
there. Bedroom has no spawner processor. Library selects cave spiders/spiders;
nether_portal selects skeletons; portal_room selects Quark forgotten; enchanting,
maze, prison and stronghold select skeletons/zombies/forgotten with weights10/10/5.

Raw ordinary spawner defaults name pig with empty SpawnPotentials. Reuse the
shared SpawnerRandomizingProcessor and MobSpawnerManager inspection in
integrated-villages-provider/README.md#content-assessment, with exact JAR/class
identities in processor_inspection. The processor replaces NBT for surviving
spawner blocks; it does not preserve the raw pig selection. The manager's
missing-list, unresolved-entity, zero-total and exception paths remain documented
limitations, not observed failures in this family.

Several rule processors convert monster boxes to ordinary spawners with
probability0.1. Unconverted boxes are distinct one-use sources. Their source and
frozen setting bindings are already preserved under quark-monster-box-behavior
and quark-monster-box-bindings. The spawn-selection table weights witch1,
cave-spider2 and zombie7. Neither template occurrence nor selection weight is
an observed encounter count. Floating-block removal and container removal rules
also prevent treating template contents as guaranteed placed contents.

Six literal template loot-table references and fourteen processor-assigned
references are listed separately in loot_table_source; the sets overlap at maze.
Each has a packaged definition at data/<namespace>/loot_table/<path>.json.
Append-loot rules identify sources, not realized rewards. Fixed inventory Items,
dispenser traps and Quark's separate mob-selection/extra-drop tables retain their
different roles. No reward-value measurement is required for this attribution.

The root declares absolute start Y15, strongholds generation step and no surface
heightmap projection. The preserved JigsawStructure.findGenerationPoint samples
that start height and passes placement settings into PieceLimitedJigsawManager.
This supports a qualitative underground discovery assessment, with exposure
dependent on layout and terrain. It does not establish final dimensions or a
measured sightline. The declared max_distance_from_center128 is not itself an
observed footprint, so the two geometry attributes remain open.

## Geometry capture declaration

Two required attributes remain: footprint and vertical size. There is no retained
full-start geometry observation. The declared size30 and max-distance128, plus
individual template sizes, do not describe a realized assembled layout. A direct
look at the pinned PieceLimitedJigsawManager confirms that root placement and
subsequent assembly are separate; no numerical size claim is derived from it.
One existing targeted capture is sufficient and avoids extending source analysis
into a new assembly measurement implementation.

Predeclare integrated_stronghold:stronghold, ordinary seed42, the existing
81-chunk target protocol under the frozen Item6 baseline. Use the fresh paths
below. Preserve locate failure, missing armory references and optional entity
failures without repairing the baseline. Require readiness, correlated save flush,
clean shutdown, accepted frozen configuration, stopped-world decoding and a full
structure start. Its saved piece envelope supplies one approximate layout, not
typical size, all-layout extrema, occupied volume or complete entity population.
Retain raw evidence through the existing archive, restore and release workflow
before accepting dimensions. Follow the infrastructure document's lifecycle and
process-group rules. No new runner or measurement system is introduced.

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
  --target instances/item8/integrated-stronghold-geometry-r1 \
  --log-path evidence/raw/item8/integrated-stronghold-geometry-r1/console.log \
  --captured-config evidence/raw/item8/integrated-stronghold-geometry-r1/configuration \
  --receipt evidence/raw/item8/integrated-stronghold-geometry-r1/run.json \
  --timeout-seconds 900 --structure integrated_stronghold:stronghold
```

## Geometry acceptance

The predeclared seed42 target completed81 requested chunks and passed readiness,
correlated flush, clean exit0 and frozen configuration acceptance. Accepted
comment-line normalization differences remain in run.json. No baseline tuning
was performed. The stopped world decoded to1803 records; that is retained
coverage, not the requested sampling denominator. No Java process remained.

Full start chunk-112,-662 is chunks.jsonl line326:50 saved pieces with envelope
[-1906,-60,-10690,-1665,51,-10486]. Inclusive subtraction gives242x112x205 blocks
(X,Y,Z). Footprint and height now use this observed example. It includes air and
padding and does not establish occupied volume, typical/all-layout dimensions or
full population of every component chunk. The low start and saved Y-60..51
support the underground assessment without proving complete terrain concealment.

The raw console preserves missing optional-mod items, invalid air item stacks,
and skipped optional or empty entity IDs, including AlexsMobs entries at
lines2763-2765 and2781-2783. These do not invalidate the saved piece bounds, but
preclude treating this capture as successful realization of every authored
entity or reward. Existing missing armory components remain dispositioned.
No general compatibility acceptance is claimed.

Archive item8-integrated-stronghold-geometry-r1-84a0377b.tar.gz contains263 files,
3,986,103 bytes (21,730,301 uncompressed), SHA-256:
ec6abe3716322313e0294fadcee622c0b1f5416c4e699ee5c9871846723b72ab.
Manifest SHA-256:
3dc7b8f3d835d629850c7300919a235f94673010dced59545a06b0ea6c0e966d.
Decoded chunks SHA-256:
5c861017eab639e754d396e7c8897b64c59daa686efac5e65014f6d1d0834c0e.
Release/tag item-8-integrated-stronghold-geometry-2026-09-07-r1 references
84a0377b7f27187f3008129b99711119b2ba97e7, verified remotely. Local and downloaded
restores verified all263 files; existing observed_bounds on downloaded line326
reproduced the full start,50 pieces and242x112x205 size. Local copies share the
workspace filesystem; the GitHub release is separate durable storage.

Reproduce using fresh output paths:

```sh
uv run python -c 'from pathlib import Path; from tools.stage_item7_world import copy_world_boundary; copy_world_boundary(Path("instances/item8/integrated-stronghold-geometry-r1"), Path("evidence/raw/item8/integrated-stronghold-geometry-r1/world"))'
uv run -m tools.decode_item7_world evidence/raw/item8/integrated-stronghold-geometry-r1/world --output evidence/raw/item8/integrated-stronghold-geometry-r1/chunks.jsonl
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/integrated-stronghold-geometry-r1 --archive evidence/raw/item8/item8-integrated-stronghold-geometry-r1-84a0377b.tar.gz --manifest evidence/item-8/raw-custody/integrated-stronghold-geometry-r1-manifest.json --revision 84a0377b7f27187f3008129b99711119b2ba97e7
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/item8-integrated-stronghold-geometry-r1-84a0377b.tar.gz --manifest evidence/item-8/raw-custody/integrated-stronghold-geometry-r1-manifest.json --target evidence/raw/item8/integrated-stronghold-geometry-r1-restored --receipt evidence/item-8/raw-custody/integrated-stronghold-geometry-r1-local-restore.json
gh release download item-8-integrated-stronghold-geometry-2026-09-07-r1 --repo copeugne/mcpack --pattern item8-integrated-stronghold-geometry-r1-84a0377b.tar.gz --dir evidence/raw/item8/integrated-stronghold-geometry-r1-download
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/integrated-stronghold-geometry-r1-download/item8-integrated-stronghold-geometry-r1-84a0377b.tar.gz --manifest evidence/item-8/raw-custody/integrated-stronghold-geometry-r1-manifest.json --target evidence/raw/item8/integrated-stronghold-geometry-r1-downloaded-restore --receipt evidence/item-8/raw-custody/integrated-stronghold-geometry-r1-downloaded-restore.json
uv run python -c 'from pathlib import Path; from mcpack_evidence.item7_nbt_models import ChunkRecord; from mcpack_evidence.item8_world_bounds import observed_bounds; print(observed_bounds(ChunkRecord.model_validate_json(Path("evidence/raw/item8/integrated-stronghold-geometry-r1-downloaded-restore/chunks.jsonl").read_text().splitlines()[325])))'
```
