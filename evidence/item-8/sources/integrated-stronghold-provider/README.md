# Integrated Stronghold provider code

All nine packaged classes captured with extractor f70a1a0. An independent
extraction reproduced the files byte for byte before this README. Manifest SHA-256:
0044580a6b6f71c9b32c8d385d539779c7b0b2ad22d4c21bf1a5bfbbf2785d5b.
Archive SHA-256: c6ac6ad68de806524615238f8a7efe511c417b8cd56ffceb7dd62aad9c8b821b.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive integrated_stronghold-1.1.4+1.21.1-neoforge.jar \
  --output evidence/raw/item8/integrated-stronghold-provider-r1
```

The NeoForge constructor calls IntegratedStrongholdNeoForgeRegistries.register.
That class registers sounds, music-disc items and a creative tab. Item and sound
factories construct vanilla objects; the tab displays those items. Common entry
only initializes a logger. The generated Architectury bridge returns neoforge.
None of these classes registers a structure or independently places content.
The packaged root instead uses the separately attributed Integrated API type.

DisableVanillaStrongholdsMixin injects at ChunkGenerator.tryGenerateStructure
HEAD and returns false for StructureType.STRONGHOLD. Its second HEAD injection,
in the concentric-ring nearest-structure lookup, returns the supplied vanilla
stronghold holder with position (29000000, 0, 29000000). That position is an
artificial locate result, not an observed or authored structure location.

LocateStrongholdCommandMixin intercepts a direct minecraft:stronghold resource
key and throws an exception directing the caller to locate
integrated_stronghold:stronghold. It does not itself redirect the search or
generate that structure. A tag argument is not the direct-key branch. Both
mixins are declared in the required packaged config; source declaration alone
does not prove every runtime interaction or mixin ordering.

Reuse the existing registry and family-decision regression for the sole root.
The provider-scope check separately binds all packaged resources and component
dispositions to the preserved pool graph. Keep missing armory references and
disconnected alternate templates unchanged. Shared Integrated API behavior and
effective family attributes remain separate downstream attribution work.
