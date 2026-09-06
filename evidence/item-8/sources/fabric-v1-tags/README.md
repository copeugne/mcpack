# Fabric v1 conventional tag entry roles

Extractor: ff7e1047206d37e634050f85ba0e03c83de3890d.
Three complete classes independently reproduce byte for byte.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-convention-tags-v1-2.1.5+7f945d5b19.jar --class-name org/sinytra/fabric/convention_tags_v1/generated/GeneratedEntryPoint.class --class-name net/fabricmc/fabric/impl/tag/convention/TagRegistration.class --class-name net/fabricmc/fabric/impl/tag/convention/ConventionLogWarnings.class --output evidence/raw/item8/fabric-v1-tags-r1
```
