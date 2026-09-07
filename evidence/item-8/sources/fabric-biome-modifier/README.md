# Fabric biome modifier boundary

Extractor: bbdf6f394fc3f32f2112e7548c350b5ed48e2551.
Five complete class captures reproduce byte for byte in the independent run.
This source increment addresses the sole packaged biome modifier and its
registration/consumer boundary, not complete provider membership.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-biome-api-v1-13.0.31+1e62d33c19.jar --class-name net/fabricmc/fabric/api/biome/v1/BiomeModifications.class --class-name 'net/fabricmc/fabric/impl/biome/modification/BiomeModificationImpl$FabricBiomeModifier.class' --class-name net/fabricmc/fabric/impl/biome/modification/BiomeModificationImpl.class --class-name org/sinytra/fabric/biome_api/FabricBiomeApiV1.class --class-name org/sinytra/fabric/biome_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-biome-modifier-r1
```

## Frozen-stack direct consumers

The remaining Item 8 question was whether another retained provider registers
Fabric biome-modification callbacks affecting end_platform, end_spike or
end_gateway_return. The dispatcher capture alone could not answer it. A focused
check in the existing Fabric test now inspects every class in the hash-verified
retained archives and all nested JARs for the API/implementation owner strings.
The API prefix includes BiomeModifications, BiomeModification and context types.
All 16 matching classes belong to this one nested Fabric biome module. There is
no packaged direct consumer outside it. This inspection does not assert absence
of reflective or dynamically generated calls; no such registration is evidenced
by the retained consumer records. Reopen this disposition if one is demonstrated.

The captured BiomeModificationImpl constructor starts with an empty list;
addModifier adds caller records. FabricBiomeApiV1 registers the modifier codec
using that list, and FabricBiomeModifier only dispatches its entries. Together
these establish no supported direct Fabric callback altering the three packaged
End routes in this frozen stack. The additive Zeta route is recorded separately.
This does not make the packaged routes exhaustive of lifecycle invocation or
prove successful placement.

Reproduce the complete archive inspection using the committed test logic:

```sh
uv run pytest tests/item8/test_fabric_provider_scope.py -k external_fabric -q
```

This adds one focused check because the existing source capture bound only the
dispatcher, not its consumers. No new archive capture, schema or runtime experiment.
