# Fabric v2 conventional tag roles

Extractor: 27f6181ec2ccd270a6c9f7fa8e89214cad4c1c83.
Four complete classes independently reproduce byte for byte.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-convention-tags-v2-2.11.1+87e5848019.jar --class-name org/sinytra/fabric/convention_tags/generated/GeneratedEntryPoint.class --class-name net/fabricmc/fabric/mixin/tag/TagKeyMixin.class --class-name net/fabricmc/fabric/impl/tag/convention/v2/TagRegistration.class --class-name net/fabricmc/fabric/impl/tag/convention/v2/TranslationConventionLogWarnings.class --output evidence/raw/item8/fabric-v2-tags-r1
```
