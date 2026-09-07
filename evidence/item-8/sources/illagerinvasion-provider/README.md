# Illager Invasion provider boundaries

Parent archive SHA-256:
5adfdd0df0c5dbe81e4458da50442b58863f9db9f22abc182f81e487eef0e6db.
Selector 41d4e39 preserves 24 directly relevant classes; manifest SHA-256:
74b6cb2b01b81d99417d139334cf85e7629fb6fef50947d06227b864ec7574c9.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive IllagerInvasion-v21.1.6-1.21.1-NeoForge.jar \
  --output evidence/raw/item8/illagerinvasion-provider-r1
```

Selector 6c26385 adds the concrete nested dependency to the existing capture path.
All sixteen bundled Extensible Enums classes are preserved in
../illagerinvasion-extensible-enums. Nested archive SHA-256:
35720e0569288b37fe59dfd3781691019d24ce1fab48623980b9d7a9b5af2e1c.
Nested source identity manifest SHA-256:
3ede180202e65323e4c3b9af92c03a0b81e2fff01c16562946291c0b08500d9f.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive IllagerInvasion-v21.1.6-1.21.1-NeoForge.jar \
  --nested-archive META-INF/jars/extensibleenums-neoforge-21.1.1.jar \
  --output evidence/raw/item8/illagerinvasion-extensible-enums-r1
```

Both independent captures reproduced exactly before this README was added.
The parent entry delegates registration and lifecycle callbacks through Puzzles
Lib. Common registration installs mob/item content, the Labyrinth structure type
and pool codecs. Event callbacks concern existing entity goals, player/block
interaction, loot injection and brewing. Common setup extends raid members using
the bundled enum factory and initializes villager avoidance. These are mob and
loot provenance, not additional authored layout entry points.

LabyrinthStructure delegates to vanilla JigsawStructure and filters the resulting
generation stub to Y <= 47. It consumes its configured start pool. Both no-liquid
pool elements are already covered by the existing pool-codec evidence and affect
component placement, not independent families.

WoodlandMansionPieceMixin handles Provoker, Warrior, Archivist and invoker data
markers with mod entity types, persistence, STRUCTURE spawn finalization and
entity insertion requests. It clears the marker and cancels the original handler
for those cases. This operates on existing mansion pieces. The thirteen packaged
vanilla-namespace mansion templates are replacements/components of that family.
Do not infer successful entity insertion from these source requests.

Other declared mixins concern food, illusioner behavior, patrols, villager enemy
sensing and client illager models. The empty NeoForge mixin list adds no route.
The nested Extensible Enums entry constructors add no authored content. Its APIs
construct caller-supplied enum values, including raid members, mob categories,
rarities, spell types, minecart types and client recipe categories. Its two mixin
lists are empty and its payload has no generation data or templates. Enum mutation
internals do not need a separate correctness audit for this candidate census.

Full payload and graph reconciliation belong to the focused provider check.
Keep the disconnected pillager pool/template and effective mansion replacement
selection explicit. Provider coverage does not settle combined loot, encounter
attributes or generated-world outcomes.

## Three building assessments

After 20900e85, Illager Fort, Illusioner Tower and Sorcerer Hut each had two
recorded descriptions. This batch integrates their eight remaining attributes,
24 answers total, without a new capture or measurement. Firecaller Hut and
Labyrinth are not included in this building batch.

Direct source derivation uses the retained packaged JSON and template catalogs,
pool-traces-content, structure-inputs and runtime dimension-biomes. Their hashes
are linked in each family decision. All three roots use vanilla jigsaw,
WORLD_SURFACE_WG, offset zero and beard_thin. Resolved biome counts are 33, 5 and
1 respectively; intersection with runtime possible-biome sets yields only the
Overworld. This is eligibility, not an observed population or generation rate.

| Family | Architecture XYZ | Upward connector Y | Child top Y |
| --- | --- | --- | --- |
| illager_fort | 26x30x28 | 0,1,4,6,11 | at most 14 |
| illusioner_tower | 15x37x15 for all three alternatives | 0,5,10,15,21 | at most 24 |
| sorcerer_hut | 9x11x9 | 1 | 4 |

In `templates-redacted.json.gz`, inspect the respective architectural templates
under `data/illagerinvasion/structure/`, including tower_1 through tower_3.
All architectural connectors point upward at interior X/Z positions. Every
reachable mob template is 1x3x1 with downward connector [0,0,0] and terminal
minecraft:empty pool. Thus a child occupies parent connector Y+1 through Y+3
without enlarging the architectural envelope. Rotation does not enlarge a
1x1 horizontal child. All relevant pool elements are rigid with empty processor
lists. Fort architecture and mob components use single_pool_element; tower and
hut architecture use legacy_single_pool_element. The initial check assumed only
single_pool_element and failed on these legacy alternatives. The source text
now records both. This does not change nominal dimensions, and no generated or
occupied-volume claim is made.

The complete reachable graphs contain no missing resources, unresolved entities,
spawner blocks or generation markers. Authored mob components supply fort
inquisitor/provoker/vindicator; tower alchemist/archivist/basher/provoker,
illusioner/vindicator plus nonhostile allay/villager; hut sorcerer/vindicator.
Fort separately declares a full-bounds natural monster spawn override for
pillager/marauder/basher/provoker. The other two overrides are empty. Neither
source proves simultaneous inhabitants. Container references resolve by template
to fort ground/tower tables, tower entrance/stairs tables and sorcerer_hut table,
all under illagerinvasion:chests. The inventory retains exact table owners.

Surface fort/tower/hut form supplies qualitative discoverability; sight distance
and exposure are not measured. Existing hostility and placement answers, biome
constraints and world observation links remain unchanged. Only these three rows
and the decisions input identity changed. Inventory matches
`evidence/raw/item8/inventory-illager-buildings-final.json`, SHA-256
c4e80a428427523e29b1f54fa7f315a556b57900bf05bd7198a8893345b212b5.

## Firecaller and Labyrinth attribution

After 3a2c6d78, these two assemblies had seventeen outstanding descriptions.
Thirteen are now integrated: six each for dimension, entity sources, loot,
spawners, enemy origin and qualitative discoverability; Labyrinth additionally
receives its underground-placement description. Four geometry answers remain.
The retained bounds catalog has no observations for either family. The component
sizes do not establish a whole-assembly size, and no new measurement was run.

The existing root definitions and runtime biome intersection support Overworld
eligibility. Firecaller uses surface projection with offset zero. For Labyrinth,
`LabyrinthStructure.findGenerationPoint` delegates to vanilla jigsaw and filters
its result through `lambda$findGenerationPoint$12`, accepting generation-stub
Y <= 47 (disassembly lines 26-52 in this provider capture). Combined with the
configured WORLD_SURFACE_WG offset -40 and bury adaptation, that establishes
underground-biased placement, not whole-layout burial or tower exposure.

Firecaller's complete graph has nine templates: base plate, hut, five feature
alternatives, firecaller and llama. Vanilla single/legacy-single pool elements
have empty processor lists. There are no saved loot-table references, physical
spawners, generation markers or unresolved entities. This does not imply absence
of ordinary block salvage or entity drops. The llama is not a hostile enemy.

Labyrinth has thirty templates including halls, rooms, tower and mob components.
Its architectural pools use the previously inspected no-liquid single element
and empty declared processor lists. The graph retains authored alchemist,
archivist, basher, marauder, necromancer, provoker, evoker and vindicator entities.
Room armor stand and item frame entities are decorative. There are no physical
spawner blocks, markers or unresolved entities. Root full-bounds monster spawning
has an empty list; authored components remain separate enemy sources. This does
not claim that other mobs cannot wander in or arise through other events.
Rooms reference illagerinvasion:chests/labyrinth and labyrinth_map; tower references
minecraft:chests/woodland_mansion. Exact template owners are integrated.

Seven affected provider/inventory tests and scoped builder quality checks pass.
Only these two rows and input identity changed. Existing geometry, biomes,
observations, hostility and nonregistry content are unchanged. Inventory matches
`evidence/raw/item8/inventory-illager-assemblies-attribution.json`, SHA-256
229401ae20ea01d07325fd0738b4fd13c851fd76c7729c0e18eadf24c5479a25.
Retire the thirteen supported descriptions; neither family is yet fully assessed.

## Targeted assembly geometry r1

Four claims remain: footprint and height for Firecaller Hut and Labyrinth. Reuse
the existing gap lifecycle with two explicit targets, ordinary seed 42, frozen
configuration and 136 retained JARs plus the established Chunky instrumentation.
No simulator, probe, schema or new measurement implementation is introduced.
Saved piece envelopes will describe targeted examples, including air/padding,
not family-wide extrema or occupied geometry. A failed locate or missing saved
start is a failed observation, not a substituted component-size answer.
Runtime code source is 84a92353befacf1b6e567acb2fb539f06b33c080.

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
  --target instances/item8/illager-geometry-r1 \
  --log-path evidence/raw/item8/illager-geometry-r1/console.log \
  --captured-config evidence/raw/item8/illager-geometry-r1/configuration \
  --receipt evidence/raw/item8/illager-geometry-r1/run.json \
  --timeout-seconds 900 \
  --structure illagerinvasion:firecaller_hut \
  --structure illagerinvasion:labyrinth
```

### Geometry r1 accepted results

Both target regions completed. The correlated save and clean exit passed, as did
frozen configuration capture. `evidence/item-8/runtime/illager-geometry-r1/run.json` records the identities and lifecycle. The original instance
and source capture remain preserved.

| Family | Decoded line | Inclusive envelope (min XYZ, max XYZ) | Size XYZ | Pieces |
| --- | ---: | --- | --- | ---: |
| firecaller_hut | 287 | -3731,248,-2549,-3704,256,-2529 | 28,9,21 | 7 |
| labyrinth | 2127 | 4698,23,-974,4855,84,-844 | 158,62,131 | 76 |

Both targeted start chunks are minecraft:full in the Overworld. The entire
decoded stream has 2,763 chunks, including locate-created and surrounding partial
chunks; that is not a full-chunk sampling denominator. `chunks.jsonl` SHA-256:
49ef0b8a410fc1a1ec7469106d1711e582c0334bb3823db229964aff6f0a4404.
For the exact rows above, take minimum piece minima and maximum piece maxima,
then max-minus-min-plus-one on each axis, as implemented in the existing
`mcpack_evidence.item8_world_bounds.observed_bounds`. X/Z supplies footprint and
Y height. The Labyrinth envelope reaching Y84 does not contradict its generation
stub Y <= 47 filter; a start-position filter is not a cap on all attached pieces.
No whole-layout exposure, occupancy or family-wide size-range claim is made.

After verified shutdown, existing tools preserved and decoded the world:

```sh
uv run python -c 'from pathlib import Path; from tools.stage_item7_world import copy_world_boundary; copy_world_boundary(Path("instances/item8/illager-geometry-r1"), Path("evidence/raw/item8/illager-geometry-r1/world"))'
uv run -m tools.decode_item7_world evidence/raw/item8/illager-geometry-r1/world --output evidence/raw/item8/illager-geometry-r1/chunks.jsonl
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/illager-geometry-r1 --archive evidence/raw/item8/item8-illager-geometry-r1-84a92353.tar.gz --manifest evidence/item-8/raw-custody/illager-geometry-r1-manifest.json --revision 84a92353befacf1b6e567acb2fb539f06b33c080
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/item8-illager-geometry-r1-84a92353.tar.gz --manifest evidence/item-8/raw-custody/illager-geometry-r1-manifest.json --target evidence/raw/item8/illager-geometry-r1-restored --receipt evidence/item-8/raw-custody/illager-geometry-r1-local-restore.json
```

World copying uses the Java-compatible POSIX record lock and excludes session.lock.
Archive size is 6,018,145 bytes, 259 files, 32,811,498 uncompressed bytes. SHA-256:
98599a56e3e0841a71d7b3a530f4c3685e363fe5a2abf149b8fbb50bf9687ef3.
It retains logs, run receipt, configuration, stopped-world boundary and decoded
chunks, without server binaries.

[Published raw archive](https://github.com/copeugne/mcpack/releases/tag/item-8-illager-geometry-2026-09-07-r1).
Local and downloaded copies both restored all 259 files with verified hashes:

```sh
gh release download item-8-illager-geometry-2026-09-07-r1 --dir evidence/raw/item8/illager-geometry-download --pattern item8-illager-geometry-r1-84a92353.tar.gz
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/illager-geometry-download/item8-illager-geometry-r1-84a92353.tar.gz --manifest evidence/item-8/raw-custody/illager-geometry-r1-manifest.json --target evidence/raw/item8/illager-geometry-downloaded-restore --receipt evidence/item-8/raw-custody/illager-geometry-r1-downloaded-restore.json
```

Local copies share a disk; GitHub supplies the separate durable copy. Use absent
archive and restore destinations for reproduction. All four geometry answers are
integrated. Seven affected tests and builder quality checks pass. Inventory
matches `evidence/raw/item8/inventory-illager-geometry.json`, SHA-256
3715e2e9625840de9c1fdb28638ca430a2ffcb8393d393126e2084ae5936337c.
Only these two rows' geometry, associated evidence and discoverability limitation
changed; prior source attribution and nonregistry content are unchanged.
