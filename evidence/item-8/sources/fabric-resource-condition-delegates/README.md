# Fabric resource-condition delegate roles

Extractor a30e961. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256:
e6103740fe144f96a30b6d57d87bc672b35fffa3b9553f52b2a4cb4188bb6697.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-resource-conditions-api-v1-4.3.0+5bdd099819.jar --class-name net/fabricmc/fabric/impl/resource/conditions/ResourceConditionsImpl.class --class-name net/fabricmc/fabric/impl/resource/conditions/OverlayConditionsMetadata.class --output evidence/raw/item8/fabric-resource-condition-delegates-r1
```

Initialization registers nine predicate types: true, not, and, or, all/any mods
loaded, tags populated, features enabled and registry contains. Evaluation
filters supplied JSON resources and reports failed parsing. Overlay metadata
returns only supplied directories whose conditions pass. Other methods inspect
existing mods, registries, tags and feature flags. These routes do not supply an
independent structure family. Effective conditions on individual consumer data
remain separate eligibility evidence; this capture does not assert they pass.
