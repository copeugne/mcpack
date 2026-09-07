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
