# fabric-item-group-entry source checkpoint

Extractor b4c5d26. Independent r1 reproduction matches the manifest and all
disassembly bytes. Manifest SHA-256: b7ad297470f753293f94ea1519ca76b23e352c0952946b6452d43a52410cd5d3.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-item-group-api-v1-4.1.7+e324903319.jar --class-name net/fabricmc/fabric/mixin/itemgroup/ItemGroupMixin.class --class-name org/sinytra/fabric/item_group_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-item-group-entry-r1
```

The generated initializer is empty. ItemGroupMixin forwards creative-tab modification callbacks and replaces display/search collections. No independent generated family is introduced by these entries.

Source capture is not whole-provider closure or effective-consumer evidence.
