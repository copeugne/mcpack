# fabric-message-api-v1-entry source checkpoint

Extractor 4cc1096. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: 9222255dfc0fe5fdf7b15eab08a4d6c45db376e76a6299bcc4629a08ca9a7f96.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-message-api-v1-6.0.14+6a754fce19.jar --class-name net/fabricmc/fabric/mixin/message/MinecraftServerMixin.class --class-name net/fabricmc/fabric/mixin/message/PlayerManagerMixin.class --class-name org/sinytra/fabric/message_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-message-api-v1-entry-r1
```

The initializer is empty. Common hooks decorate chat and forward allow/notification callbacks for chat, game and command messages. No independent site-generation route.

Source capture alone does not close whole-provider membership.
