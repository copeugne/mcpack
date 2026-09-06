# CristelLib conditional pack binding

Extractor bf7da611. Independent r1 reproduction matches all source and
manifest bytes. Manifest SHA-256:
978790f35e5af270a4b6949b6e1c80b6780b5506a129d1d2c6e202bb58484afe

```sh
uv run -m tools.inspect_item8_pool_elements --archive cristellib-neoforge-1.21.1-3.1.7.jar --class-name de/cristelknight/cristellib/data/condition/ConditionNode.class --class-name de/cristelknight/cristellib/data/condition/ConditionRegistry.class --class-name de/cristelknight/cristellib/data/condition/conditions/ModLoadedCondition.class --class-name de/cristelknight/cristellib/neoforge/ModLoadingUtilImpl.class --output evidence/raw/item8/cristellib-conditions-r1
```

ConditionRegistry binds mod_loaded to ModLoadedCondition. Without a version
constraint it tests actual mod presence, through the NeoForge loaded or loading
mod list. ConditionNode requires its supplied conditions to pass. Combined with
the preserved Towns and Towers declaration and absent Waystones runtime mod,
the optional Waystones replacement pack is ineligible. No version-comparator
audit is needed for that version-free declaration.
