# ServerCore lifecycle delegates

Extractor 2231051d3bfc4fed823a0d76338fbfd212ca26b0. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
a56b6cd495a2513f8dc23e0982526a9eb85cb18866260821059dc66ea7de8c4c

```sh
uv run -m tools.inspect_item8_pool_elements --archive servercore-neoforge-1.5.17+1.21.1.jar --class-name me/wesley1808/servercore/common/ServerCore.class --class-name me/wesley1808/servercore/common/services/Events.class --output evidence/item-8/sources/servercore-lifecycle
```

Startup and server event boundary evidence for provider membership.
