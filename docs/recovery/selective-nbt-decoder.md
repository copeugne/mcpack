# Selective NBT Decoder Reconstruction Contract

The lost decoder streamed only the fields required for slot integrity, chunk status, heightmaps, saved quart biomes, and structure starts. The replacement must:

- preserve signed chunk coordinates;
- reject stored coordinates inconsistent with the Anvil location-table slot;
- distinguish unreadable, missing, non-full, and coordinate-shifted targets;
- cross-check selective output against a trusted full decoder on a fixed sample;
- never accept a biome boundary comparison as a decoder correctness oracle;
- remain memory-bounded across 131,072 chunks.

