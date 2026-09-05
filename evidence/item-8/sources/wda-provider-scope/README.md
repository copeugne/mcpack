# WDA provider generation boundary

Extractor revision f3ac5ab. All six archive classes are captured, including the
complete custom jigsaw implementation. The output reproduced byte for byte.

```sh
uv run -m tools.inspect_item8_pool_elements --archive DungeonsArise-1.21.1-2.1.68-release.jar --output evidence/raw/item8/wda-provider-scope-r1
```

identities.json SHA-256:
1878d9890c8dbb9dae7b3edb7e07b760b1e59f0cb560519ef9b257ec79135d5f.

DungeonsAriseMain registers WDAStructures on the supplied mod bus. WDAStructures
registers one structure type, dungeons_arise:generic_structures, with the
WDAGenericStructures codec. Its generation point consumes the configured start
pool and calls ModifiedJigsawPlacement with an empty alias lookup. Placement
selects pool elements, reads child pool keys from template jigsaw NBT, follows
fallback pools and assembles PoolElementStructurePiece instances. PieceState is
an assembly record. The public ServerLevel placement overload also consumes a
caller-supplied pool; it supplies no additional authored root or registration.

These captures establish the executable candidate routes. Full packaged-resource
reconciliation, including function commands and disconnected components, belongs
to the provider-scope disposition. Do not count this source capture alone as
provider closure or as evidence of observed successful placement.
