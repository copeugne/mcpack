# Diesel Generators entry and hook boundaries

Extractor aa6148b47f195b24ab6f225bef5bbdd32e151a49. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
ae941c8805f0a988eed4218a8d7f230e477dae513494e5c18ac2384b96d439d3

```sh
uv run -m tools.inspect_item8_pool_elements --archive createdieselgenerators-1.21.1-1.3.15.jar --class-name com/jesz/createdieselgenerators/mixins/BasinRecipeMixin.class --class-name com/jesz/createdieselgenerators/mixins/ContraptionMixin.class --class-name com/jesz/createdieselgenerators/mixins/CopycatBlockMixin.class --class-name com/jesz/createdieselgenerators/mixins/CreeperMixin.class --class-name com/jesz/createdieselgenerators/mixins/EntityMixin.class --class-name com/jesz/createdieselgenerators/mixins/LootItemAccessor.class --class-name com/jesz/createdieselgenerators/mixins/LootPoolAccessor.class --class-name com/jesz/createdieselgenerators/mixins/LootTableAccessor.class --class-name com/jesz/createdieselgenerators/mixins/MechanicalPressBlockEntityMixin.class --class-name com/jesz/createdieselgenerators/mixins/ShaftBlockMixin.class --class-name com/jesz/createdieselgenerators/mixins/UseOnContextInvoker.class --class-name com/jesz/createdieselgenerators/mixins/SableAssemblyMixin.class --class-name com/jesz/createdieselgenerators/CreateDieselGenerators.class --class-name com/jesz/createdieselgenerators/events/GameEvents.class --class-name com/jesz/createdieselgenerators/events/ModEvents.class --output evidence/item-8/sources/diesel-provider
```

Provider membership inspection. Sable-related code is not proof that the excluded
Sable mod is enabled, and no general machine compatibility claim is implied.
