# NeoForge biome tag constant for Fairy Ring

The retained FairyRingGenerator reads NeoForge Tags.Biomes.IS_PLAINS. The
existing generator capture did not identify its resource key. The single captured
Tags$Biomes class binds that field to tag("is_plains"); the private tag helper
constructs a BIOME TagKey with namespace "c". Thus its key is c:is_plains.
Archive, class and disassembly hashes are recorded in identities.json.

Reproduce into a fresh directory with the existing extractor:

```sh
uv run -m tools.inspect_item8_pool_elements --archive neoforge-21.1.249-universal.jar --class-name 'net/neoforged/neoforge/common/Tags$Biomes.class' --output evidence/raw/item8/neoforge-biome-tag-constants-reproduction
```

The first attempt was rejected by the extractor's explicit class allowlist.
Only this class was added to that existing list. An initially duplicated archive
allowlist entry was caught by Ruff and removed; the archive was already allowed.
No new extractor, runtime experiment or general reflection machinery was added.

For the Fairy Ring attribute, reuse biome_constraint from
mcpack_evidence.item8_biomes with each reference (#minecraft:is_forest and
#c:is_plains), structure-inputs.json's biome_tags, and the frozenset of lines in
runtime/registry-r1/dumps/registry/minecraft/worldgen_biome.txt. Both resolve
without missing required members or unresolved tags. The resulting lists contain
41 forest and 27 plains biomes, with one overlap. Forest selection has priority,
so the plains-only list has 26 entries. The inventory preserves those lists and
their dimension overlap. This is tag eligibility, not frequency or successful
placement; module/callback enablement and delegated flower effects remain separate.
