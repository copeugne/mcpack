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
