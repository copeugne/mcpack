# ServerCore entry boundaries

Extractor d996068c77498177246daa9fdbe4d80fb545f084. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
a6d8b88a096224c94e16092de36f70c5b082333b7d8200511480e1df81abae51

```sh
uv run -m tools.inspect_item8_pool_elements --archive servercore-neoforge-1.5.17+1.21.1.jar --class-name me/wesley1808/servercore/neoforge/common/ServerCoreNeoForge.class --class-name me/wesley1808/servercore/mixin/ServerCoreMixinPlugin.class --class-name me/wesley1808/servercore/neoforge/common/NeoForgeMinecraftPlatform.class --class-name me/wesley1808/servercore/neoforge/common/NeoForgeModPlatform.class --class-name servercore_libs/net/kyori/adventure/text/serializer/gson/impl/GsonDataComponentValueConverterProvider.class --class-name servercore_libs/net/kyori/adventure/text/serializer/gson/impl/JSONComponentSerializerProviderImpl.class --output evidence/item-8/sources/servercore-entries
```

Automatic mod entry, mixin plugin and four service providers. Membership remains open.
