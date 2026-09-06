# Fabric pack discovery boundary

Extractor: 6cf2878e1df5f2ddc73cd0a4329709b89accff72.
The complete class independently reproduces byte for byte.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-resource-loader-v0-1.3.1+4ea8954419.jar --class-name net/fabricmc/fabric/impl/resource/loader/ModResourcePackCreator.class --output evidence/raw/item8/fabric-pack-discovery-r1
```
