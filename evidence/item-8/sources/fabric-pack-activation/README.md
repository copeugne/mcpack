# Fabric pack activation consumers

Extractor: 149e849a65ae3291d30c7a6abbe6d74939dab6cf.
Both complete consumers independently reproduce byte for byte.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-resource-loader-v0-1.3.1+4ea8954419.jar --class-name net/fabricmc/fabric/impl/resource/loader/ModResourcePackUtil.class --class-name net/fabricmc/fabric/impl/resource/loader/ModNioResourcePack.class --output evidence/raw/item8/fabric-pack-activation-r1
```
