# Simply Swords entry and hook boundaries

Extractor e171263c0af16735b6219647e97312a81f1527a9. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
3dfcec4b5d6d6978a0ecd4e7ac17effacc71008592940006b42c2d408ee40bb4

```sh
uv run -m tools.inspect_item8_pool_elements --archive simplyswords-neoforge-1.63.0-1.21.1.jar --class-name net/sweenus/simplyswords/neoforge/SimplySwordsForge.class --class-name net/sweenus/simplyswords/neoforge/client/SimplySwordsClientForge.class --class-name net/sweenus/simplyswords/mixin/LivingEntityMixin.class --class-name net/sweenus/simplyswords/mixin/ServerPlayerEntityMixin.class --class-name net/sweenus/simplyswords/mixin/PlayerEntityMixin.class --class-name net/sweenus/simplyswords/mixin/AnimalEntityMixin.class --output evidence/item-8/sources/simplyswords-entries
```

Both automatic entries and all four common hooks. Provider membership remains open.
