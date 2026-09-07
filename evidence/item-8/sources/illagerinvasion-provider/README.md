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
