# fabric-data-attachment-entry source checkpoint

Extractor b4c5d26. Independent r1 reproduction matches the manifest and all
disassembly bytes. Manifest SHA-256: bee13b060b3c64abbb8d20e4da62404f7b4d1ee1d2e12b21e7dce2bd490daf9d.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-data-attachment-api-v1-1.4.5+26d408aa19.jar --class-name net/fabricmc/fabric/impl/attachment/AttachmentModImpl.class --class-name net/fabricmc/fabric/mixin/attachment/AttachmentHolderAccessor.class --class-name net/fabricmc/fabric/mixin/attachment/AttachmentTypeAccessor.class --class-name net/fabricmc/fabric/mixin/attachment/BaseMappedRegistryAccessor.class --class-name net/fabricmc/fabric/mixin/attachment/IAttachmentHolderMixin.class --class-name org/sinytra/fabric/data_attachment_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-data-attachment-entry-r1
```

The generated entry calls AttachmentEntrypoint.onInitialize, which remains to inspect. Its client initializer is guarded. The attached-data subscriber and four common access hooks are preserved for role reconciliation.

Source capture is not whole-provider closure or effective-consumer evidence.
