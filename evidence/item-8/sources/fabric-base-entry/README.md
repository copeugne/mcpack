# Fabric base entry

Extractor: 77dc50e4db46423fa1c925d1133a5b987cbc3b50.
The complete loader entry independently reproduces byte for byte.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-api-base-0.4.42+d1308ded19.jar --class-name org/sinytra/fabric/api_base/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-base-entry-r1
```
