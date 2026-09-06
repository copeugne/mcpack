# fabric-transfer-api-v1-entry source checkpoint

Extractor a6fa580. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: fd7982f42faf3e553baf9e444fbf8beb643ab432c5d79da2d6436c704954b081.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-transfer-api-v1-5.4.3+a25cb45619.jar --class-name net/fabricmc/fabric/mixin/transfer/AbstractFurnaceBlockEntityMixin.class --class-name net/fabricmc/fabric/mixin/transfer/BucketItemMixin.class --class-name net/fabricmc/fabric/mixin/transfer/BundleContentsComponentAccessor.class --class-name net/fabricmc/fabric/mixin/transfer/ContainerComponentAccessor.class --class-name net/fabricmc/fabric/mixin/transfer/DoubleInventoryAccessor.class --class-name net/fabricmc/fabric/mixin/transfer/FluidMixin.class --class-name net/fabricmc/fabric/mixin/transfer/ItemMixin.class --class-name net/fabricmc/fabric/mixin/transfer/JukeboxBlockEntityMixin.class --class-name net/fabricmc/fabric/mixin/transfer/LockableContainerBlockEntityMixin.class --class-name net/fabricmc/fabric/mixin/transfer/SimpleInventoryMixin.class --class-name org/sinytra/fabric/transfer_api/TransferApiNeoCompat.class --class-name org/sinytra/fabric/transfer_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-transfer-api-v1-entry-r1
```

The generated initializer is empty. Automatic capability registration wraps existing item/fluid inventories and installs lookup fallbacks. Common hooks adapt existing container mutations and item/fluid variants or sounds. No independent authored site.

Source capture alone does not close whole-provider membership.
