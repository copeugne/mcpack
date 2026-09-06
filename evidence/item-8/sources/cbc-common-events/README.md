# Big Cannons shared event handlers

Extractor 6f4d82bc1f015af874159f4eed0505ef9345e4ab. Independent r1 reproduction matches the
disassembly and identity manifest. Manifest SHA-256:
a8899d3cba54bb5c7e0da30952234cc3c540eb4df9aa4851bceeefacaaf5ad83

```sh
uv run -m tools.inspect_item8_pool_elements --archive createbigcannons-5.11.6+mc.1.21.1.jar --class-name rbasamoyai/createbigcannons/CBCCommonEvents.class --output evidence/item-8/sources/cbc-common-events
```

Shared world lifecycle and reload-listener boundary for provider membership.
No general persistence or gameplay correctness claim is made.
