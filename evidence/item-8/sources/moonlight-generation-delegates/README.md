# Moonlight generation and reload delegates

Extractor 945bc3e68921c781bb54c75960923f6b9180de91. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
eee5815a67288e010a4d111e5ce759515d13604db6de351e9474be933fb7f3e0

```sh
uv run -m tools.inspect_item8_pool_elements --archive moonlight-neoforge-1.21.1-3.0.17.jar --class-name net/mehvahdjukaar/moonlight/core/worldgen/SpawnBoxStructurePiece.class --class-name net/mehvahdjukaar/moonlight/core/worldgen/JigsawCodecWithExtra.class --class-name net/mehvahdjukaar/moonlight/core/misc/ReloadInstanceWrapper.class --output evidence/item-8/sources/moonlight-generation-delegates
```

Spawn-box component, jigsaw codec and dynamic reload boundary evidence.
