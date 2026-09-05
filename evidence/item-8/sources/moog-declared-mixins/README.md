# Declared Moog mixin paths

Extractor c388784. All sixteen classes declared in the common and NeoForge
mixin lists reproduced byte for byte before this README was added. Manifest:
f5623e71057ea5d31c90897e105ef11d2cf5400443617e7ffc76fef61e6138c3.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar \
  --class-name com/finndog/moogs_structures/mixins/features/NoBasaltColumnsInStructuresMixin.class \
  --class-name com/finndog/moogs_structures/mixins/features/NoDeltasInStructuresMixin.class \
  --class-name com/finndog/moogs_structures/mixins/neoforge/structures/StructurePoolMixin.class \
  --class-name com/finndog/moogs_structures/mixins/resources/NamespaceResourceManagerAccessor.class \
  --class-name com/finndog/moogs_structures/mixins/structures/JigsawReplacementProcessorMixin.class \
  --class-name com/finndog/moogs_structures/mixins/structures/ListPoolElementAccessor.class \
  --class-name com/finndog/moogs_structures/mixins/structures/LocateCommandMixin.class \
  --class-name com/finndog/moogs_structures/mixins/structures/PoolElementStructurePieceAccessor.class \
  --class-name com/finndog/moogs_structures/mixins/structures/SinglePoolElementAccessor.class \
  --class-name com/finndog/moogs_structures/mixins/structures/StructurePieceAccessor.class \
  --class-name com/finndog/moogs_structures/mixins/structures/StructurePoolAccessor.class \
  --class-name com/finndog/moogs_structures/mixins/structures/StructureProcessorAccessor.class \
  --class-name com/finndog/moogs_structures/mixins/structures/StructureTemplateManagerAccessor.class \
  --class-name com/finndog/moogs_structures/mixins/structures/TemplateAccessor.class \
  --class-name com/finndog/moogs_structures/mixins/terrainadaptation/BeardifierAccessor.class \
  --class-name com/finndog/moogs_structures/mixins/terrainadaptation/BeardifierMixin.class \
  --output evidence/raw/item8/moog-declared-mixins-r1
```

Ten accessors expose existing resource-manager fallbacks, pool elements/templates,
processors, structure-piece rotation/bounds, template palettes and beardifier
iterators. They declare no additional authored content or automatic generation.
A caller can mutate exposed fields; accessor availability alone is not evidence
that a caller injects components. The six behavioral mixins are:

- NoBasaltColumnsInStructuresMixin: at canPlaceAt entry, return false when the
  WorldGenRegion position satisfies MixinUtils with the no_basalt structure tag.
- NoDeltasInStructuresMixin: at DeltaFeature.place entry, return false when its
  origin satisfies the corresponding no_delta test.
- StructurePoolMixin: wrap the selected Codec.intRange call, preserving its lower
  bound and supplying upper bound 5000. This is not pool-content injection. The
  injection is optional (require=0, remap=false); source presence alone does not
  establish that the target matched at runtime.
- JigsawReplacementProcessorMixin: when DebugFlags.isKeepJigsawBlocks is true,
  return the supplied relative block info before normal replacement. No separate
  authored root is introduced. Initial flag state is not inferred here.
- LocateCommandMixin: when any requested structure has larger_locate_search,
  call findNearestMapStructure with radius argument 2000, then report the result
  or throw the existing not-found exception. The injection uses require=0 and
  CAPTURE_FAILSOFT. This changes a search, not a structure registration.
- BeardifierMixin: pass existing chunk structures/beardifier to
  EnhancedBeardifierHelper.forStructuresInChunk and existing density to
  computeDensity; store enhanced piece/junction iterators. No template or root
  identifier is declared in the mixin. The helper's content boundary remains
  unresolved until inspected; do not assume its implementation from its name.

These exact hooks replace the earlier loose "pool replacement" description.
Remaining direct boundaries: registry/service dispatch, MixinUtils tag lookup,
EnhancedBeardifierHelper and DebugFlags state. Inspect only those paths needed to
resolve candidate coverage. Do not expand into a general geometry/noise audit.
Provider and Item 8 remain open. Scoped extractor Ruff/Basedpyright pass; no new
runtime or measurement system is introduced.
