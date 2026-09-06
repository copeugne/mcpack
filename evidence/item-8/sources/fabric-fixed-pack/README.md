# Fabric fixed pack supplier

Extractor: e29938a545339fa3b03fa22b1cce5260ea761959.
Both complete classes independently reproduce byte for byte.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-resource-loader-v0-1.3.1+4ea8954419.jar --class-name net/fabricmc/fabric/impl/resource/loader/PlaceholderResourcePack.class --class-name 'net/fabricmc/fabric/impl/resource/loader/PlaceholderResourcePack$Factory.class' --output evidence/raw/item8/fabric-fixed-pack-r1
```
